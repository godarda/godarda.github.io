package com.godarda

import android.Manifest
import android.annotation.SuppressLint
import android.content.Intent
import android.content.pm.PackageManager
import android.content.res.Configuration
import android.graphics.Bitmap
import android.graphics.Color
import android.net.ConnectivityManager
import android.net.Network
import android.net.NetworkCapabilities
import android.net.NetworkRequest
import android.os.Bundle
import android.view.View
import android.view.ViewStub
import android.webkit.CookieManager
import android.webkit.JavascriptInterface
import android.webkit.PermissionRequest
import android.webkit.WebChromeClient
import android.webkit.WebResourceRequest
import android.webkit.WebSettings
import android.webkit.WebStorage
import android.webkit.WebView
import android.webkit.WebViewClient
import android.widget.Button
import android.widget.FrameLayout
import androidx.activity.OnBackPressedCallback
import androidx.activity.enableEdgeToEdge
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import androidx.core.content.edit
import androidx.core.net.toUri
import androidx.core.view.WindowCompat
import androidx.core.view.isVisible

/**
 * The main activity of the application, serving as a container for the WebView-based UI.
 * This activity manages network connectivity, system theme synchronization, custom URL schemes,
 * and standard web browser features within the application context.
 */
class MainActivity : BaseActivity() {

    // --- UI Components ---

    /** Primary WebView used to render the application content. */
    private val webview: WebView by lazy { findViewById(R.id.webView) }

    /** Root container layout for applying system window insets. */
    private val rootLayout: FrameLayout by lazy { findViewById(R.id.webViewContainer) }

    /** ViewStub for lazily inflating the 'No Internet' error view. */
    private val noInternetStub: ViewStub by lazy { findViewById(R.id.noInternetStub) }

    /** Inflated 'No Internet' view. */
    private var noInternetView: View? = null

    /** Inflated 'App Down' view. */
    private var appDownView: View? = null

    // --- State Management ---

    /** Holds a pending permission request (e.g., for camera or microphone access). */
    private var pendingPermissionRequest: PermissionRequest? = null

    /** Unique request code for audio recording permissions. */
    private val recordAudioRequestCode = 101

    /** Caches the last successfully loaded URL for recovery purposes. */
    private var lastVisitedUrl: String = Urls.BASE

    /** Tracks the current active theme (light/dark) synchronization status. */
    private var currentTheme: String? = null

    // --- Hardware & Services ---

    /** Manager for monitoring system-wide network connectivity state. */
    private val connectivityManager: ConnectivityManager by lazy {
        getSystemService(ConnectivityManager::class.java) as ConnectivityManager
    }

    /** Callback that triggers UI updates based on network availability. */
    private val networkCallback by lazy {
        object : ConnectivityManager.NetworkCallback() {
            override fun onAvailable(network: Network) {
                runOnUiThread {
                    // Reload the WebView if an error screen was previously displayed
                    if (noInternetView?.isVisible == true || appDownView?.isVisible == true) {
                        showWebView()
                        webview.loadUrl(lastVisitedUrl)
                    }
                }
            }
        }
    }

    // --- Lifecycle Methods ---

    override fun onCreate(savedInstanceState: Bundle?) {
        // Enable edge-to-edge display early in the lifecycle
        enableEdgeToEdge()
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Adjust padding to account for status and navigation bars
        applyWindowInsetsTo(rootLayout)

        // Pre-emptively apply the last saved theme to prevent UI flashing
        val sharedPref = getSharedPreferences("app_settings", MODE_PRIVATE)
        currentTheme = sharedPref.getString("theme", null)
        applyThemeToSystemBars(currentTheme)

        setupWebView()
        setupConnectivity()
        setupBackButton()

        // Initial load based on connectivity status
        if (isInternetAvailable()) {
            showWebView()
            webview.loadUrl(lastVisitedUrl)
        } else {
            showNoInternet()
        }
    }

    override fun onDestroy() {
        super.onDestroy()
        // Prevent memory leaks by unregistering network callbacks
        connectivityManager.unregisterNetworkCallback(networkCallback)
    }

    // --- Configuration ---

    /**
     * Configures WebView settings for performance, security, and hybrid app behavior.
     */
    private fun setupWebView() {
        webview.settings.apply {
            @SuppressLint("SetJavaScriptEnabled")
            javaScriptEnabled = true
            @Suppress("DEPRECATION")
            safeBrowsingEnabled = true
            domStorageEnabled = true
            useWideViewPort = false
            displayZoomControls = false
            builtInZoomControls = false
            allowFileAccess = false
            allowContentAccess = false
            mediaPlaybackRequiresUserGesture = false
            setSupportZoom(false)
            textZoom = 100
            cacheMode = WebSettings.LOAD_DEFAULT
            loadsImagesAutomatically = true
            // Append custom identification to User Agent
            userAgentString += " GoDarda"
        }
        
        webview.apply {
            isVerticalScrollBarEnabled = false
            isHorizontalScrollBarEnabled = false
            overScrollMode = View.OVER_SCROLL_NEVER
            isHapticFeedbackEnabled = false

            // Bridge native Kotlin methods to the WebView context
            addJavascriptInterface(WebAppInterface(), "AndroidInterface")

            webViewClient = AppWebViewClient()
            webChromeClient = object : WebChromeClient() {
                /**
                 * Intercepts and handles permission requests from the web content.
                 */
                override fun onPermissionRequest(request: PermissionRequest) {
                    if (request.resources.contains(PermissionRequest.RESOURCE_AUDIO_CAPTURE)) {
                        if (ContextCompat.checkSelfPermission(this@MainActivity, Manifest.permission.RECORD_AUDIO) == PackageManager.PERMISSION_GRANTED) {
                            request.grant(request.resources)
                        } else {
                            pendingPermissionRequest = request
                            ActivityCompat.requestPermissions(this@MainActivity, arrayOf(Manifest.permission.RECORD_AUDIO), recordAudioRequestCode)
                        }
                    } else {
                        super.onPermissionRequest(request)
                    }
                }
            }
        }
    }

    /**
     * Updates the status and navigation bars to match the provided theme or system default.
     * @param theme The requested theme ("light", "dark", or null for system default).
     */
    private fun applyThemeToSystemBars(theme: String?) {
        currentTheme = theme
        val isDark = when (theme) {
            "dark" -> true
            "light" -> false
            else -> (resources.configuration.uiMode and Configuration.UI_MODE_NIGHT_MASK) == Configuration.UI_MODE_NIGHT_YES
        }

        val bgColor = if (isDark) Color.BLACK else Color.WHITE
        
        rootLayout.setBackgroundColor(bgColor)
        
        // Apply theme to error views if they are currently inflated
        noInternetView?.let { view ->
            view.findViewById<View>(R.id.noInternetLayout)?.setBackgroundColor(bgColor)
        }

        @Suppress("DEPRECATION")
        window.statusBarColor = bgColor
        @Suppress("DEPRECATION")
        window.navigationBarColor = bgColor

        // Ensure system icons contrast correctly with the bar colors
        val insetsController = WindowCompat.getInsetsController(window, window.decorView)
        insetsController.isAppearanceLightStatusBars = !isDark
        insetsController.isAppearanceLightNavigationBars = !isDark
    }

    /**
     * Sets up active monitoring for internet connectivity changes.
     */
    private fun setupConnectivity() {
        val networkRequest = NetworkRequest.Builder()
            .addCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
            .build()
        connectivityManager.registerNetworkCallback(networkRequest, networkCallback)
    }

    /**
     * Configures back button logic to navigate within the WebView history or exit the app.
     */
    private fun setupBackButton() {
        onBackPressedDispatcher.addCallback(this, object : OnBackPressedCallback(true) {
            override fun handleOnBackPressed() {
                handleBackNavigation()
            }
        })
    }

    // --- Utility Methods ---

    override fun onRequestPermissionsResult(requestCode: Int, permissions: Array<out String>, grantResults: IntArray) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        if (requestCode == recordAudioRequestCode) {
            if (grantResults.isNotEmpty() && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                pendingPermissionRequest?.grant(pendingPermissionRequest?.resources)
            } else {
                pendingPermissionRequest?.deny()
            }
            pendingPermissionRequest = null
        }
    }

    /**
     * Performs a check for active internet connectivity.
     */
    private fun isInternetAvailable(): Boolean {
        val network = connectivityManager.activeNetwork ?: return false
        val capabilities = connectivityManager.getNetworkCapabilities(network) ?: return false
        return capabilities.hasCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
    }

    /**
     * Displays the offline error view and hides the WebView.
     */
    private fun showNoInternet() {
        if (noInternetView == null) {
            noInternetView = noInternetStub.inflate()
            val tryAgainBtn: Button = noInternetView!!.findViewById(R.id.tryagain)
            val exitBtn: Button = noInternetView!!.findViewById(R.id.exit_button_no_internet)

            tryAgainBtn.setOnClickListener {
                if (isInternetAvailable()) {
                    showWebView()
                    webview.loadUrl(lastVisitedUrl)
                }
            }
            exitBtn.setOnClickListener {
                finishAffinity()
            }
        }
        noInternetView?.isVisible = true
        webview.isVisible = false
        applyThemeToSystemBars(currentTheme)
    }

    /**
     * Resets the UI to show the WebView and hide any error states.
     */
    private fun showWebView() {
        noInternetView?.isVisible = false
        appDownView?.isVisible = false
        webview.isVisible = true
        applyThemeToSystemBars(currentTheme)
    }

    /**
     * Processes custom URL schemes (like share: or reset:) and external links.
     * @return True if the URL was handled by native logic, False to let WebView process it.
     */
    private fun handleCustomUrl(url: String): Boolean {
        return when {
            url.startsWith("share:") -> {
                val shareUrl = url.removePrefix("share:").removeSuffix(".html")
                val intent = Intent(Intent.ACTION_SEND).apply {
                    type = "text/plain"
                    putExtra(Intent.EXTRA_TITLE, webview.title)
                    putExtra(Intent.EXTRA_TEXT, shareUrl)
                }
                startActivity(Intent.createChooser(intent, getString(R.string.share_via)))
                true
            }
            url.startsWith("reset:") -> {
                // 1. Clear WebView specific data
                webview.clearHistory()
                webview.clearCache(true)
                webview.clearFormData()
                
                // 2. Clear Cookies
                CookieManager.getInstance().removeAllCookies(null)
                CookieManager.getInstance().flush()
                
                // 3. Clear Web Storage (localStorage, WebSQL, IndexedDB)
                WebStorage.getInstance().deleteAllData()
                
                // 4. Clear App Preferences (including theme)
                getSharedPreferences("app_settings", MODE_PRIVATE).edit { clear() }
                
                // 5. Reset internal state and re-apply system theme
                currentTheme = null
                applyThemeToSystemBars(null)

                // 6. Reload the initial URL with a small delay to ensure cleanup is complete
                webview.postDelayed({
                    webview.loadUrl(Urls.BASE)
                }, 500)
                true
            }
            url.startsWith(Urls.GISCUS) || url.startsWith(Urls.GITHUB_LOGIN) || url.startsWith(Urls.GITHUB_SESSION) -> {
                webview.loadUrl(url)
                true
            }
            !url.startsWith(Urls.BASE) -> {
                startActivity(Intent(Intent.ACTION_VIEW, url.toUri()))
                true
            }
            else -> false
        }
    }

    /**
     * Manages internal WebView navigation history for a consistent user experience.
     */
    private fun handleBackNavigation() {
        if (noInternetView?.isVisible == true || appDownView?.isVisible == true) {
            finishAffinity()
            return
        }

        val homeUrl = "${Urls.BASE}/"
        val currentUrl = webview.url

        if (webview.canGoBack() && currentUrl != homeUrl) {
            webview.goBack()
        } else if (currentUrl != homeUrl) {
            webview.loadUrl(homeUrl)
        } else {
            finishAffinity()
        }
    }

    // --- Inner Classes ---

    /**
     * Handles calls from JavaScript in the WebView and the native Android code.
     */
    private inner class WebAppInterface {
        /**
         * Triggered by web content when the user preference for theme changes.
         * Syncs the native system UI with the web theme.
         */
        @JavascriptInterface
        @Suppress("unused")
        fun onThemeChanged(theme: String?) {
            runOnUiThread {
                val sharedPref = getSharedPreferences("app_settings", MODE_PRIVATE)
                val oldTheme = sharedPref.getString("theme", null)
                
                if (oldTheme != theme) {
                    sharedPref.edit { putString("theme", theme) }
                    applyThemeToSystemBars(theme)
                }
            }
        }
    }

    /**
     * Custom WebViewClient to handle page load events and URL overrides.
     */
    private inner class AppWebViewClient : WebViewClient() {
        override fun onPageStarted(view: WebView?, url: String?, favicon: Bitmap?) {
            super.onPageStarted(view, url, favicon)
            if (url != null && url.startsWith(Urls.BASE)) {
                lastVisitedUrl = url
            }
        }

        /**
         * Injects JavaScript into the page to monitor theme changes in localStorage.
         */
        override fun onPageFinished(view: WebView?, url: String?) {
            super.onPageFinished(view, url)
            view?.evaluateJavascript("""
                (function() {
                    function notifyTheme() {
                        const theme = localStorage.getItem('theme');
                        if (window.AndroidInterface && window.AndroidInterface.onThemeChanged) {
                            window.AndroidInterface.onThemeChanged(theme);
                        }
                    }
                    if (!window.themeObserverSet) {
                        const originalSetItem = localStorage.setItem;
                        localStorage.setItem = function(key, value) {
                            originalSetItem.apply(this, arguments);
                            if (key === 'theme') {
                                notifyTheme();
                            }
                        };
                        window.themeObserverSet = true;
                    }
                    notifyTheme();
                })();
            """.trimIndent(), null)
        }

        override fun shouldOverrideUrlLoading(view: WebView, request: WebResourceRequest): Boolean {
            val url = request.url.toString()
            if (!isInternetAvailable()) {
                showNoInternet()
                return true
            }
            return handleCustomUrl(url) || url == view.url
        }
    }
}

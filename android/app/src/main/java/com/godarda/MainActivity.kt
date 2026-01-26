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
import android.webkit.PermissionRequest
import android.webkit.WebChromeClient
import android.webkit.WebResourceRequest
import android.webkit.WebSettings
import android.webkit.WebView
import android.webkit.WebViewClient
import android.widget.Button
import android.widget.FrameLayout
import androidx.activity.OnBackPressedCallback
import androidx.activity.enableEdgeToEdge
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import androidx.core.net.toUri
import androidx.core.view.WindowCompat
import androidx.core.view.isVisible

/**
 * The main activity of the application, which primarily displays a WebView.
 * It handles network connectivity, custom URL schemes, and back navigation within the WebView.
 */
class MainActivity : BaseActivity() {

    // UI components, lazily initialized for performance.
    private val webview: WebView by lazy { findViewById(R.id.webView) }
    private val rootLayout: FrameLayout by lazy { findViewById(R.id.webViewContainer) }
    private val noInternetStub: ViewStub by lazy { findViewById(R.id.noInternetStub) }

    // Nullable views that are inflated via ViewStub when needed.
    private var noInternetView: View? = null
    private var appDownView: View? = null

    // Holds the pending permission request for audio capture.
    private var pendingPermissionRequest: PermissionRequest? = null
    private val recordAudioRequestCode = 101

    // Caches the last successfully visited URL for smart reloading on connectivity changes.
    private var lastVisitedUrl: String = Urls.BASE

    private val connectivityManager: ConnectivityManager by lazy {
        getSystemService(ConnectivityManager::class.java) as ConnectivityManager
    }

    /**
     * Network callback to monitor connectivity changes.
     * When an internet connection becomes available, it reloads the last visited URL
     * if an error screen is currently displayed.
     */
    private val networkCallback by lazy {
        object : ConnectivityManager.NetworkCallback() {
            override fun onAvailable(network: Network) {
                runOnUiThread {
                    if (noInternetView?.isVisible == true || appDownView?.isVisible == true) {
                        showWebView()
                        webview.loadUrl(lastVisitedUrl)
                    }
                }
            }
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        enableEdgeToEdge()
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Apply window insets to the root layout to handle system UI.
        applyWindowInsetsTo(rootLayout)

        // Configure the status bar for edge-to-edge display.
        val insetsController = WindowCompat.getInsetsController(window, window.decorView)
        insetsController.isAppearanceLightStatusBars = false // Use light icons for a dark status bar.

        // Initialize core components.
        setupWebView()
        setupConnectivity()
        setupBackButton()

        // Load the initial URL if internet is available, otherwise show the no-internet screen.
        if (isInternetAvailable()) {
            webview.loadUrl(lastVisitedUrl)
        } else {
            showNoInternet()
        }
    }

    override fun onDestroy() {
        super.onDestroy()
        // Unregister the network callback to prevent memory leaks.
        connectivityManager.unregisterNetworkCallback(networkCallback)
    }

    /**
     * Configures the WebView with optimal settings for displaying the website.
     */
    private fun setupWebView() {
        webview.settings.apply {
            // Enable JavaScript, which is required for site functionality. This is safe as we only load trusted content.
            @SuppressLint("SetJavaScriptEnabled")
            javaScriptEnabled = true

            // Standard security and performance settings.
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
            userAgentString += " GoDarda"
        }
        webview.apply {
            // Disable scrollbars and overscroll effects for a cleaner look.
            isVerticalScrollBarEnabled = false
            isHorizontalScrollBarEnabled = false
            overScrollMode = View.OVER_SCROLL_NEVER
            isHapticFeedbackEnabled = false

            // Set the custom WebViewClient to handle URL loading and errors.
            webViewClient = AppWebViewClient()
            webChromeClient = object : WebChromeClient() {
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
     * Initializes and registers a network callback to monitor for internet connectivity.
     */
    private fun setupConnectivity() {
        val networkRequest = NetworkRequest.Builder()
            .addCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
            .build()
        connectivityManager.registerNetworkCallback(networkRequest, networkCallback)
    }

    /**
     * Sets up the custom back button behavior to navigate within the WebView or exit the app.
     */
    private fun setupBackButton() {
        onBackPressedDispatcher.addCallback(this, object : OnBackPressedCallback(true) {
            override fun handleOnBackPressed() {
                handleBackNavigation()
            }
        })
    }

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
     * Checks if the device has an active internet connection.
     */
    private fun isInternetAvailable(): Boolean {
        val network = connectivityManager.activeNetwork ?: return false
        val capabilities = connectivityManager.getNetworkCapabilities(network) ?: return false
        return capabilities.hasCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
    }

    /**
     * Inflates and displays the "No Internet" screen using the ViewStub for efficiency.
     */
    private fun showNoInternet() {
        if (noInternetView == null) {
            // Inflate the "No Internet" layout only when needed for the first time.
            noInternetView = noInternetStub.inflate()

            // Configure buttons in the newly inflated view.
            val tryAgainBtn: Button = noInternetView!!.findViewById(R.id.tryagain)
            val exitBtn: Button = noInternetView!!.findViewById(R.id.exit_button_no_internet)

            tryAgainBtn.setOnClickListener {
                if (isInternetAvailable()) {
                    showWebView()
                    webview.loadUrl(lastVisitedUrl) // Use the last visited URL on retry.
                }
            }
            exitBtn.setOnClickListener {
                finishAffinity() // Close the app.
            }
        }
        noInternetView?.isVisible = true
        webview.isVisible = false

        // Match Splash status bar style by updating root background and icon appearance.
        rootLayout.setBackgroundResource(R.color.backgroundColor)
        @Suppress("DEPRECATION")
        window.statusBarColor = ContextCompat.getColor(this, R.color.backgroundColor)
        val insetsController = WindowCompat.getInsetsController(window, window.decorView)
        val isLightMode = (resources.configuration.uiMode and Configuration.UI_MODE_NIGHT_MASK) == Configuration.UI_MODE_NIGHT_NO
        insetsController.isAppearanceLightStatusBars = isLightMode
    }

    /**
     * Ensures the WebView is visible and hides any overlay screens like the no-internet view.
     */
    private fun showWebView() {
        noInternetView?.isVisible = false
        appDownView?.isVisible = false
        webview.isVisible = true

        // Revert to WebView status bar style: black background with light icons.
        rootLayout.setBackgroundResource(android.R.color.black)
        @Suppress("DEPRECATION")
        window.statusBarColor = Color.TRANSPARENT
        val insetsController = WindowCompat.getInsetsController(window, window.decorView)
        insetsController.isAppearanceLightStatusBars = false
    }

    /**
     * Handles custom URL schemes to trigger native app actions from the WebView.
     */
    private fun handleCustomUrl(url: String): Boolean {
        return when {
            // Share scheme: e.g., "share:https://example.com"
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
            // Clear cache scheme: e.g., "clear:"
            url.startsWith("clear:") -> {
                webview.clearHistory()
                webview.clearCache(true)
                webview.clearFormData()
                true
            }
            // External links that should still load in the WebView.
            url.startsWith(Urls.GISCUS) || url.startsWith(Urls.GITHUB_LOGIN) || url.startsWith(Urls.GITHUB_SESSION) -> {
                webview.loadUrl(url)
                true
            }
            // Any other external link should open in the default browser.
            !url.startsWith(Urls.BASE) -> {
                startActivity(Intent(Intent.ACTION_VIEW, url.toUri()))
                true
            }
            else -> false
        }
    }

    /**
     * Defines the logic for the system back button.
     * Navigates back in WebView history if possible, otherwise exits the app.
     */
    private fun handleBackNavigation() {
        // If an error screen is showing, exit the app on back press instead of navigating.
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

    /**
     * A custom WebViewClient to intercept URL loading and handle page errors.
     */
    private inner class AppWebViewClient : WebViewClient() {

        override fun onPageStarted(view: WebView?, url: String?, favicon: Bitmap?) {
            super.onPageStarted(view, url, favicon)
            if (url != null && url.startsWith(Urls.BASE)) {
                // Cache the URL if it belongs to the base website domain.
                lastVisitedUrl = url
            }
        }

        override fun shouldOverrideUrlLoading(view: WebView, request: WebResourceRequest): Boolean {
            val url = request.url.toString()
            if (!isInternetAvailable()) {
                showNoInternet()
                return true
            }
            // Intercept the URL. If it's a custom scheme, handle it. Otherwise, let the WebView proceed.
            // A URL that is the same as the current one is also considered handled to prevent reloads.
            return handleCustomUrl(url) || url == view.url
        }
    }
}

package com.godarda

import android.annotation.SuppressLint
import android.content.Context
import android.content.Intent
import android.graphics.Bitmap
import android.graphics.Color
import android.net.ConnectivityManager
import android.net.Network
import android.net.NetworkCapabilities
import android.net.NetworkRequest
import android.os.Build
import android.os.Bundle
import android.view.View
import android.view.ViewStub
import android.webkit.WebResourceError
import android.webkit.WebResourceRequest
import android.webkit.WebResourceResponse
import android.webkit.WebSettings
import android.webkit.WebView
import android.webkit.WebViewClient
import android.widget.Button
import android.widget.FrameLayout
import androidx.activity.OnBackPressedCallback
import androidx.core.net.toUri
import androidx.core.view.isVisible

/**
 * The main activity of the application, which primarily displays a WebView.
 * It handles network connectivity, custom URL schemes, and back navigation within the WebView.
 */
class MainActivity : BaseActivity() {

    // Lazily initialized views to improve performance.
    private val webview: WebView by lazy { findViewById(R.id.webView) }
    private val rootLayout: FrameLayout by lazy { findViewById(R.id.webViewContainer) }
    private val noInternetStub: ViewStub by lazy { findViewById(R.id.noInternetStub) }
    private val appDownStub: ViewStub by lazy { findViewById(R.id.appDownStub) }

    // These views are only inflated when needed, saving resources.
    private var noInternetView: View? = null
    private var appDownView: View? = null

    // Stores the last successfully visited URL to allow for smart reloading.
    private var lastVisitedUrl: String = Urls.BASE

    private val connectivityManager: ConnectivityManager by lazy {
        getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
    }

    /**
     * A network callback to listen for changes in internet connectivity.
     * If the internet becomes available, it reloads the last visited URL.
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
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Apply insets to the root container, as was the original logic.
        applyWindowInsetsTo(rootLayout)
        window.statusBarColor = Color.BLACK

        // Configure the components of the activity.
        setupWebView()
        setupConnectivity()
        setupBackButton()

        // Load the initial URL or show the "No Internet" screen.
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
            // JavaScript is required for the website to function correctly.
            // This is safe as we only load content from our own trusted website.
            @SuppressLint("SetJavaScriptEnabled")
            javaScriptEnabled = true

            // Standard security and performance settings.
            safeBrowsingEnabled = true
            domStorageEnabled = true
            useWideViewPort = false
            displayZoomControls = false
            builtInZoomControls = false
            allowFileAccess = false
            allowContentAccess = false
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
        }
    }

    /**
     * Registers the network callback to listen for connectivity changes.
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
            // Inflate the layout only when it's needed for the first time.
            noInternetView = noInternetStub.inflate()

            // Set up the buttons in the newly inflated view.
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
    }

    /**
     * Hides other overlay screens and shows the WebView.
     */
    private fun showWebView() {
        noInternetView?.isVisible = false
        appDownView?.isVisible = false
        webview.isVisible = true
    }

    /**
     * Inflates and displays the "App Down" screen for handling loading errors.
     */
    private fun showAppDown() {
        if (appDownView == null) {
            appDownView = appDownStub.inflate()
            val backButton: Button = appDownView!!.findViewById(R.id.back_button)
            val exitButton: Button = appDownView!!.findViewById(R.id.exit_button_app_down)

            backButton.setOnClickListener {
                if (webview.canGoBack()) {
                    showWebView()
                    webview.goBack()
                } else {
                    finishAffinity()
                }
            }
            exitButton.setOnClickListener {
                finishAffinity() // Close the app.
            }
        }
        appDownView?.isVisible = true
        webview.isVisible = false
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
        // If an error screen is showing, exit the app on back press.
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
            // If the URL is part of our website, save it as the last visited URL.
            if (url != null && url.startsWith(Urls.BASE)) {
                lastVisitedUrl = url
            }
        }

        override fun shouldOverrideUrlLoading(view: WebView, request: WebResourceRequest): Boolean {
            val url = request.url.toString()
            if (!isInternetAvailable()) {
                showNoInternet()
                return true
            }
            // If handleCustomUrl returns true, the URL is handled. Otherwise, let the WebView handle it.
            return handleCustomUrl(url) || url == view.url
        }

        override fun onReceivedError(view: WebView, request: WebResourceRequest, error: WebResourceError) {
            super.onReceivedError(view, request, error)
            // Show the error screen only for main frame errors on our own domain.
            if (request.isForMainFrame && request.url.toString().startsWith(Urls.BASE)) {
                showAppDown()
            }
        }

        override fun onReceivedHttpError(view: WebView, request: WebResourceRequest, errorResponse: WebResourceResponse) {
            super.onReceivedHttpError(view, request, errorResponse)
            // Show the error screen only for main frame errors on our own domain.
            if (request.isForMainFrame && request.url.toString().startsWith(Urls.BASE)) {
                showAppDown()
            }
        }
    }
}

package com.godarda

import android.annotation.SuppressLint
import android.content.Context
import android.content.Intent
import android.graphics.Color
import android.net.*
import android.os.Build
import android.os.Bundle
import android.view.View
import android.view.WindowInsetsController
import android.view.WindowManager
import android.webkit.*
import android.widget.Button
import android.widget.FrameLayout
import android.widget.LinearLayout
import androidx.activity.OnBackPressedCallback
import androidx.core.net.toUri
import androidx.core.view.isVisible

class MainActivity : BaseActivity() {

    private lateinit var webview: WebView
    private lateinit var noInternetLayout: LinearLayout
    private lateinit var tryAgainBtn: Button
    private lateinit var connectivityManager: ConnectivityManager
    private lateinit var networkCallback: ConnectivityManager.NetworkCallback

    private fun isInternetAvailable(): Boolean {
        val cm = getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
        val network = cm.activeNetwork ?: return false
        val capabilities = cm.getNetworkCapabilities(network) ?: return false
        return capabilities.hasCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
    }

    @SuppressLint("SetJavaScriptEnabled")
    private fun configureWebView() = webview.settings.apply {
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
        javaScriptEnabled = true
        loadsImagesAutomatically = true
        userAgentString += "GoDarda"
    }

    private fun showNoInternet() {
        noInternetLayout.isVisible = true
        webview.isVisible = false
    }

    private fun showWebView() {
        noInternetLayout.isVisible = false
        webview.isVisible = true
    }

    private fun showAppDown() {
        setContentView(R.layout.app_down)
    }

    private fun handleCustomUrl(url: String): Boolean {
        return when {
            url.startsWith("share") -> {
                val shareUrl = url.removePrefix("share:").removeSuffix(".html")
                val intent = Intent(Intent.ACTION_SEND).apply {
                    type = "text/plain"
                    putExtra(Intent.EXTRA_TITLE, webview.title)
                    putExtra(Intent.EXTRA_TEXT, shareUrl)
                }
                startActivity(Intent.createChooser(intent, title))
                true
            }
            url.startsWith("clear:") -> {
                webview.clearHistory()
                webview.clearCache(true)
                webview.clearFormData()
                true
            }
            url.startsWith(Urls.GISCUS) ||
                    url.startsWith(Urls.GITHUB_LOGIN) ||
                    url.startsWith(Urls.GITHUB_SESSION) -> {
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

    private fun handleBackNavigation() {
        val homeUrl = "${Urls.BASE}/"
        val currentUrl = webview.url ?: ""
        when {
            webview.canGoBack() && currentUrl != homeUrl -> webview.goBack()
            currentUrl != homeUrl -> webview.loadUrl(homeUrl)
            else -> finishAffinity()
        }
    }

    @SuppressLint("SetJavaScriptEnabled")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val rootLayout = findViewById<FrameLayout>(R.id.webViewContainer)
        applyWindowInsetsTo(rootLayout)

        webview = findViewById(R.id.webView)
        noInternetLayout = findViewById(R.id.noInternetLayout)
        tryAgainBtn = findViewById(R.id.tryagain)

        window.setSoftInputMode(WindowManager.LayoutParams.SOFT_INPUT_ADJUST_NOTHING)
        configureWebView()

        // Force black status bar and white text in light mode
        window.statusBarColor = Color.BLACK
        val isLightMode = resources.configuration.uiMode and
                android.content.res.Configuration.UI_MODE_NIGHT_MASK ==
                android.content.res.Configuration.UI_MODE_NIGHT_NO

        if (isLightMode) {
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
                window.insetsController?.setSystemBarsAppearance(
                    0,
                    WindowInsetsController.APPEARANCE_LIGHT_STATUS_BARS
                )
            } else {
                @Suppress("DEPRECATION")
                window.decorView.systemUiVisibility =
                    window.decorView.systemUiVisibility and View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR.inv()
            }
        }

        if (!isInternetAvailable()) {
            showNoInternet()
            tryAgainBtn.setOnClickListener { recreate() }
            return
        } else {
            showWebView()
            webview.loadUrl(Urls.BASE)
        }

        webview.apply {
            isVerticalScrollBarEnabled = false
            isHorizontalScrollBarEnabled = false
            overScrollMode = View.OVER_SCROLL_NEVER
            isHapticFeedbackEnabled = false
            webViewClient = object : WebViewClient() {
                override fun shouldOverrideUrlLoading(view: WebView, request: WebResourceRequest): Boolean {
                    if (!isInternetAvailable()) {
                        showNoInternet()
                        tryAgainBtn.setOnClickListener { recreate() }
                        return true
                    }
                    val url = request.url.toString()
                    return handleCustomUrl(url) || "$url/" == webview.url
                }

                override fun onReceivedError(view: WebView, request: WebResourceRequest, error: WebResourceError) {
                    super.onReceivedError(view, request, error)
                    if (request.isForMainFrame && request.url.toString().startsWith(Urls.BASE)) {
                        showAppDown()
                    }
                }

                override fun onReceivedHttpError(view: WebView, request: WebResourceRequest, errorResponse: WebResourceResponse) {
                    super.onReceivedHttpError(view, request, errorResponse)
                    if (request.isForMainFrame && request.url.toString().startsWith(Urls.BASE)) {
                        showAppDown()
                    }
                }
            }
        }

        onBackPressedDispatcher.addCallback(this, object : OnBackPressedCallback(true) {
            override fun handleOnBackPressed() = handleBackNavigation()
        })

        connectivityManager = getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
        val networkRequest = NetworkRequest.Builder()
            .addCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
            .build()

        networkCallback = object : ConnectivityManager.NetworkCallback() {
            override fun onAvailable(network: Network) {
                runOnUiThread {
                    if (noInternetLayout.isVisible) {
                        showWebView()
                        webview.loadUrl(Urls.BASE)
                    }
                }
            }
        }
        connectivityManager.registerNetworkCallback(networkRequest, networkCallback)
    }

    override fun onDestroy() {
        super.onDestroy()
        connectivityManager.unregisterNetworkCallback(networkCallback)
    }
}
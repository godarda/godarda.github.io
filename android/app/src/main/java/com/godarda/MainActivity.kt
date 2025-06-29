package com.godarda

import android.annotation.SuppressLint
import android.content.Context
import android.content.Intent
import android.net.ConnectivityManager
import android.net.Network
import android.net.NetworkCapabilities
import android.net.NetworkRequest
import android.os.Bundle
import android.view.View
import android.view.WindowManager
import android.webkit.WebResourceError
import android.webkit.WebResourceRequest
import android.webkit.WebResourceResponse
import android.webkit.WebSettings
import android.webkit.WebView
import android.webkit.WebViewClient
import android.widget.Button
import android.widget.FrameLayout
import android.widget.LinearLayout
import androidx.activity.OnBackPressedCallback
import androidx.core.net.toUri
import androidx.core.view.isVisible

class MainActivity : BaseActivity() {
    private lateinit var webview: WebView
    private lateinit var noInternetLayout: LinearLayout
    private lateinit var connectivityManager: ConnectivityManager
    private lateinit var networkCallback: ConnectivityManager.NetworkCallback

    private fun isInternetAvailable(): Boolean {
        val connectivityManager =
            getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
        val network = connectivityManager.activeNetwork ?: return false
        val networkCapabilities =
            connectivityManager.getNetworkCapabilities(network) ?: return false
        return networkCapabilities.hasCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
    }

    @SuppressLint("SetJavaScriptEnabled")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val rootLayout = findViewById<FrameLayout>(R.id.webViewContainer)
        applyWindowInsetsTo(rootLayout)
        webview = findViewById(R.id.webView)
        noInternetLayout = findViewById(R.id.noInternetLayout)
        val tryAgainBtn = findViewById<Button>(R.id.tryagain)

        fun showNoInternet() {
            noInternetLayout.visibility = View.VISIBLE
            webview.visibility = View.GONE
        }
        fun showWebView() {
            noInternetLayout.visibility = View.GONE
            webview.visibility = View.VISIBLE
        }
        fun showAppDown() {
            setContentView(R.layout.app_down)
        }

        if (!isInternetAvailable()) {
            showNoInternet()
            tryAgainBtn.setOnClickListener { recreate() }
            return
        } else {
            showWebView()
            webview.loadUrl("https://godarda.github.io")
        }

        webview.settings.apply {
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
        webview.isVerticalScrollBarEnabled = false
        webview.isHorizontalScrollBarEnabled = false
        webview.overScrollMode = View.OVER_SCROLL_NEVER
        webview.isHapticFeedbackEnabled = false
        window.setSoftInputMode(WindowManager.LayoutParams.SOFT_INPUT_ADJUST_NOTHING)

        webview.webViewClient = object : WebViewClient() {
            override fun shouldOverrideUrlLoading(
                view: WebView,
                request: WebResourceRequest
            ): Boolean {
                if (!isInternetAvailable()) {
                    showNoInternet()
                    tryAgainBtn.setOnClickListener { recreate() }
                    return true
                }
                val url = request.url.toString()
                if (url.startsWith("https://godarda.github.io")) {
                    return "$url/" == webview.url
                }
                if (url.startsWith("share")) {
                    val shareUrl = url.replace("share:", "").replace(".html", "")
                    val shareIntent = Intent(Intent.ACTION_SEND)
                    shareIntent.type = "text/plain"
                    shareIntent.putExtra(Intent.EXTRA_TITLE, view.title.toString())
                    shareIntent.putExtra(Intent.EXTRA_TEXT, shareUrl)
                    startActivity(Intent.createChooser(shareIntent, title))
                    return true
                }
                if (url.startsWith("clear:")) {
                    webview.clearHistory()
                    webview.clearCache(true)
                    webview.clearFormData()
                    return true
                }
                if (url.startsWith("https://giscus.app/") ||
                    url.startsWith("https://github.com/login") ||
                    url.startsWith("https://github.com/session")
                ) {
                    webview.loadUrl(url)
                    return true
                }
                if (!url.startsWith("https://godarda.github.io")) {
                    startActivity(Intent(Intent.ACTION_VIEW, url.toUri()))
                    return true
                }
                return true
            }

            override fun onReceivedError(
                view: WebView,
                request: WebResourceRequest,
                error: WebResourceError
            ) {
                super.onReceivedError(view, request, error)
                if (request.isForMainFrame && request.url.toString().startsWith("https://godarda.github.io")) {
                    showAppDown()
                }
            }

            override fun onReceivedHttpError(
                view: WebView,
                request: WebResourceRequest,
                errorResponse: WebResourceResponse
            ) {
                super.onReceivedHttpError(view, request, errorResponse)
                if (request.isForMainFrame && request.url.toString().startsWith("https://godarda.github.io")) {
                    showAppDown()
                }
            }
        }

        onBackPressedDispatcher.addCallback(this, object : OnBackPressedCallback(true) {
            override fun handleOnBackPressed() {
                val homeUrl = "https://godarda.github.io/"
                val currentUrl = webview.url ?: ""
                if (webview.canGoBack() && currentUrl != homeUrl) {
                    webview.goBack()
                } else if (currentUrl != homeUrl) {
                    webview.loadUrl(homeUrl)
                } else {
                    finishAffinity()
                }
            }
        })

        connectivityManager = getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
        val networkRequest = NetworkRequest.Builder()
            .addCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
            .build()

        networkCallback = object : ConnectivityManager.NetworkCallback() {
            override fun onAvailable(network: Network) {
                runOnUiThread {
                    if (noInternetLayout.isVisible) {
                        noInternetLayout.visibility = View.GONE
                        webview.visibility = View.VISIBLE
                        webview.loadUrl("https://godarda.github.io")
                    }
                }
            }
        }
        connectivityManager.registerNetworkCallback(networkRequest, networkCallback)
    }

    override fun onDestroy() {
        super.onDestroy()
        val connectivityManager = getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
        networkCallback?.let { connectivityManager.unregisterNetworkCallback(it) }
    }
}
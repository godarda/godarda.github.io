package com.godarda

import android.os.Bundle
import android.view.View
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

open class BaseActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        enableEdgeToEdge()
        super.onCreate(savedInstanceState)
    }

    fun applyWindowInsetsTo(view: View) {
        ViewCompat.setOnApplyWindowInsetsListener(view) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            val ime = insets.getInsets(WindowInsetsCompat.Type.ime())
            v.setPadding(
                systemBars.left,
                systemBars.top,
                systemBars.right,
                systemBars.bottom + ime.bottom
            )
            WindowInsetsCompat.CONSUMED
        }
    }
}

/*

val windowInsetsController = ViewCompat.getWindowInsetsController(window.decorView)
        window.statusBarColor = Color.BLACK
        val isDarkModeEnabled = (resources.configuration.uiMode and Configuration.UI_MODE_NIGHT_MASK) == Configuration.UI_MODE_NIGHT_YES
        if (isDarkModeEnabled) {
            // Dark mode: Set navigation bar color to white and icons to dark
            window.navigationBarColor = Color.WHITE
            windowInsetsController?.isAppearanceLightNavigationBars = false // Dark icons for white background
        } else {
            // Light mode: Set navigation bar color to black and icons to light
            window.navigationBarColor = Color.BLACK
            windowInsetsController?.isAppearanceLightNavigationBars = true // Light icons for black background
        }

        windowInsetsController?.isAppearanceLightStatusBars = !isDarkModeEnabled
        windowInsetsController?.isAppearanceLightNavigationBars = !isDarkModeEnabled

open class BaseActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        enableEdgeToEdge()
        val uiModeManager = getSystemService(Context.UI_MODE_SERVICE) as UiModeManager
        val currentMode = uiModeManager.nightMode
        if (currentMode == UiModeManager.MODE_NIGHT_YES) {
            setTheme(R.style.AppTheme_Dark)
        } else {
            setTheme(R.style.AppTheme_Light)
        }
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val webViewContainer = findViewById<FrameLayout>(R.id.webViewContainer)
        val webview = findViewById<WebView>(R.id.webView)
        val windowInsetsController = ViewCompat.getWindowInsetsController(window.decorView)
        // Set status bar color to black
        window.statusBarColor = Color.BLACK
        // Set navigation bar color to black
        window.navigationBarColor = Color.BLACK
        // Set status bar icons to be light (black background)
        windowInsetsController?.isAppearanceLightStatusBars = true
        // Set navigation bar icons to be light (black background)
        windowInsetsController?.isAppearanceLightNavigationBars = true

        // Handle window insets for edge-to-edge display
        ViewCompat.setOnApplyWindowInsetsListener(webViewContainer) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            val displayCutout = insets.getInsets(WindowInsetsCompat.Type.displayCutout())
            val ime = insets.getInsets(WindowInsetsCompat.Type.ime())

            // Apply insets as padding to the container
            v.setPadding(
                systemBars.left,
                systemBars.top,
                systemBars.right,
                systemBars.bottom + ime.bottom
            )

            WindowInsetsCompat.CONSUMED
        }
    }
}*/
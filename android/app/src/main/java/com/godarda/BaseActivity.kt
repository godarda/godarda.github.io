package com.godarda

import android.content.res.Configuration
import android.graphics.Color
import android.os.Bundle
import android.view.View
import android.view.Window
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.app.AppCompatDelegate
import androidx.core.graphics.drawable.toDrawable
import androidx.core.view.ViewCompat
import androidx.core.view.WindowCompat
import androidx.core.view.WindowInsetsCompat

/**
 * A foundational activity that provides common functionality for other activities in the app.
 * It manages the global theme preference to prevent UI flickering on startup.
 */
open class BaseActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        // 1. Read theme preference.
        val sharedPref = getSharedPreferences("app_settings", MODE_PRIVATE)
        val theme = sharedPref.getString("theme", null)
        val isDark = isDarkTheme(theme)

        // 2. Set Window Background immediately to match preference.
        // This covers the area before the layout is inflated.
        window.setBackgroundDrawable((if (isDark) Color.BLACK else Color.WHITE).toDrawable())

        // 3. Ensure AppCompat uses the correct night mode before super.onCreate.
        // We do this check to avoid unnecessary activity recreations which cause flashes.
        val targetMode = when (theme) {
            "dark" -> AppCompatDelegate.MODE_NIGHT_YES
            "light" -> AppCompatDelegate.MODE_NIGHT_NO
            else -> AppCompatDelegate.MODE_NIGHT_FOLLOW_SYSTEM
        }
        if (AppCompatDelegate.getDefaultNightMode() != targetMode) {
            AppCompatDelegate.setDefaultNightMode(targetMode)
        }

        super.onCreate(savedInstanceState)
        
        // 4. Apply theme settings to system bars (status and navigation)
        applyThemeToSystemBars(window, theme)
    }

    /**
     * Determines if the dark theme should be used based on app settings or system preference.
     */
    fun isDarkTheme(theme: String?): Boolean {
        return when (theme) {
            "dark" -> true
            "light" -> false
            else -> (resources.configuration.uiMode and Configuration.UI_MODE_NIGHT_MASK) == Configuration.UI_MODE_NIGHT_YES
        }
    }

    /**
     * A utility function to apply system window insets (like the status and navigation bars)
     * as padding to a given view.
     */
    fun applyWindowInsetsTo(view: View) {
        ViewCompat.setOnApplyWindowInsetsListener(view) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }
    }

    /**
     * Updates the system bars (status and navigation) color and icon appearance
     * based on the provided theme or the system default.
     */
    fun applyThemeToSystemBars(window: Window, theme: String?) {
        val isDark = isDarkTheme(theme)
        val bgColor = if (isDark) Color.BLACK else Color.WHITE
        
        @Suppress("DEPRECATION")
        window.statusBarColor = bgColor
        @Suppress("DEPRECATION")
        window.navigationBarColor = bgColor

        val insetsController = WindowCompat.getInsetsController(window, window.decorView)
        insetsController.isAppearanceLightStatusBars = !isDark
        insetsController.isAppearanceLightNavigationBars = !isDark
    }
}

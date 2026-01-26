package com.godarda

import android.content.Context
import android.content.res.Configuration
import android.graphics.Color
import android.graphics.drawable.ColorDrawable
import android.os.Bundle
import android.view.View
import android.view.Window
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowCompat
import androidx.core.view.WindowInsetsCompat

/**
 * A foundational activity that provides common functionality for other activities in the app.
 */
open class BaseActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        // Read theme before super.onCreate and apply it to the window background to prevent flashing.
        val sharedPref = getSharedPreferences("app_settings", Context.MODE_PRIVATE)
        val theme = sharedPref.getString("theme", null)
        val isDark = isDarkTheme(theme)
        
        // Immediately set the window background color. 
        // This is the most effective way to prevent the "black/white flash" during activity transitions.
        window.setBackgroundDrawable(ColorDrawable(if (isDark) Color.BLACK else Color.WHITE))

        super.onCreate(savedInstanceState)
        
        // Apply theme settings to system bars (status and navigation)
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
     * Reads the stored theme and applies it to the system bars.
     */
    fun applyStoredThemeToSystemBars() {
        val sharedPref = getSharedPreferences("app_settings", Context.MODE_PRIVATE)
        val theme = sharedPref.getString("theme", null)
        applyThemeToSystemBars(window, theme)
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
        
        window.statusBarColor = bgColor
        window.navigationBarColor = bgColor

        val insetsController = WindowCompat.getInsetsController(window, window.decorView)
        insetsController.isAppearanceLightStatusBars = !isDark
        insetsController.isAppearanceLightNavigationBars = !isDark
    }
}

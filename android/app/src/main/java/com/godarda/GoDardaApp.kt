package com.godarda

import android.app.Application
import android.content.Context
import androidx.appcompat.app.AppCompatDelegate

/**
 * Custom Application class to handle global initialization.
 * Specifically used to apply the stored theme as early as possible.
 */
class GoDardaApp : Application() {
    override fun onCreate() {
        super.onCreate()
        applyStoredTheme()
    }

    private fun applyStoredTheme() {
        val sharedPref = getSharedPreferences("app_settings", Context.MODE_PRIVATE)
        val theme = sharedPref.getString("theme", null)
        
        val mode = when (theme) {
            "dark" -> AppCompatDelegate.MODE_NIGHT_YES
            "light" -> AppCompatDelegate.MODE_NIGHT_NO
            else -> AppCompatDelegate.MODE_NIGHT_FOLLOW_SYSTEM
        }
        
        AppCompatDelegate.setDefaultNightMode(mode)
    }
}

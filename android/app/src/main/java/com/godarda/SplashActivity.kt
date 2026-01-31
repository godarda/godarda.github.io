package com.godarda

import android.annotation.SuppressLint
import android.content.Context
import android.content.Intent
import android.graphics.Color
import android.os.Bundle
import android.view.View
import androidx.lifecycle.lifecycleScope
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch

/**
 * Splash screen activity displaying app branding.
 * Transitions to MainActivity after a predefined delay.
 */
@SuppressLint("CustomSplashScreen")
class SplashActivity : BaseActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash)

        // Sync theme with stored preference for the splash screen background
        applyStoredThemeToBackground()

        // Initiate transition delay using lifecycle-aware coroutine.
        lifecycleScope.launch {
            delay(1500) // 1.5 second delay
            val i = Intent(this@SplashActivity, MainActivity::class.java)
            startActivity(i)
            finish()
        }
    }

    /**
     * Applies the stored theme color to the splash screen background layout.
     */
    private fun applyStoredThemeToBackground() {
        val sharedPref = getSharedPreferences("app_settings", Context.MODE_PRIVATE)
        val theme = sharedPref.getString("theme", null)
        
        val isDark = when (theme) {
            "dark" -> true
            "light" -> false
            else -> (resources.configuration.uiMode and android.content.res.Configuration.UI_MODE_NIGHT_MASK) == 
                    android.content.res.Configuration.UI_MODE_NIGHT_YES
        }

        val bgColor = if (isDark) Color.BLACK else Color.WHITE
        findViewById<View>(R.id.splashContainer)?.setBackgroundColor(bgColor)
    }
}

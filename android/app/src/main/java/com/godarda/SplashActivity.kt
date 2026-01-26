package com.godarda

import android.annotation.SuppressLint
import android.content.Intent
import android.content.res.Configuration
import android.os.Bundle
import androidx.core.content.ContextCompat
import androidx.core.view.WindowCompat
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

        // Align status bar color with splash background.
        @Suppress("DEPRECATION")
        window.statusBarColor = ContextCompat.getColor(this, R.color.backgroundColor)

        // Configure status bar icon appearance based on current theme.
        val insetsController = WindowCompat.getInsetsController(window, window.decorView)
        val isLightMode = (resources.configuration.uiMode and Configuration.UI_MODE_NIGHT_MASK) == Configuration.UI_MODE_NIGHT_NO
        insetsController.isAppearanceLightStatusBars = isLightMode

        // Initiate transition delay using lifecycle-aware coroutine.
        lifecycleScope.launch {
            delay(1500) // 1.5 second delay
            val i = Intent(this@SplashActivity, MainActivity::class.java)
            startActivity(i)
            finish()
        }
    }
}

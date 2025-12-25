package com.godarda

import android.content.Intent
import android.content.pm.PackageManager
import android.content.res.Configuration
import android.os.Build
import android.os.Bundle
import android.widget.TextView
import androidx.core.content.ContextCompat
import androidx.core.view.WindowCompat
import androidx.lifecycle.lifecycleScope
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch

/**
 * A simple, stable splash screen activity that displays the app logo and version.
 * It transitions to MainActivity after a fixed delay.
 */
class SplashActivity : BaseActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash)

        // Set status bar to match the splash background color for a seamless look.
        window.statusBarColor = ContextCompat.getColor(this, R.color.backgroundColor)

        // Ensure status bar icons are visible in both light and dark themes.
        val insetsController = WindowCompat.getInsetsController(window, window.decorView)
        val isLightMode = (resources.configuration.uiMode and Configuration.UI_MODE_NIGHT_MASK) == Configuration.UI_MODE_NIGHT_NO
        insetsController.isAppearanceLightStatusBars = isLightMode

        val versionTextView = findViewById<TextView>(R.id.appversion)

        // Safely retrieve and display the application's version name.
        val versionName = try {
            val packageInfo = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
                packageManager.getPackageInfo(packageName, PackageManager.PackageInfoFlags.of(0))
            } else {
                @Suppress("DEPRECATION")
                packageManager.getPackageInfo(packageName, 0)
            }
            packageInfo.versionName
        } catch (_: PackageManager.NameNotFoundException) {
            ""
        }
        versionTextView.text = getString(R.string.app_version, versionName)

        // Use a lifecycle-aware coroutine to handle the delay before transitioning.
        lifecycleScope.launch {
            delay(1500) // 1.5 second delay
            val i = Intent(this@SplashActivity, MainActivity::class.java)
            startActivity(i)
            finish()
        }
    }
}

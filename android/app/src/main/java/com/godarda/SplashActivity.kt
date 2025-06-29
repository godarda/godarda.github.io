package com.godarda

import android.annotation.SuppressLint
import android.content.Intent
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.widget.FrameLayout
import android.widget.TextView

@SuppressLint("CustomSplashScreen")
class SplashActivity : BaseActivity() {
    lateinit var version: TextView

    @SuppressLint("SetTextI18n")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash)
        val splashContainer = findViewById<FrameLayout>(R.id.splashContainer)
        applyWindowInsetsTo(splashContainer)
        version = findViewById(R.id.appversion)
        version.text = "App Version " + packageManager.getPackageInfo(packageName, 0).versionName
        Handler(Looper.getMainLooper()).postDelayed({
            val i = Intent(this@SplashActivity, MainActivity::class.java)
            startActivity(i)
            finish()
        }, 2000)
    }
}
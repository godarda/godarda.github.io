package com.godarda

import android.os.Bundle
import android.view.View
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

/**
 * A foundational activity that provides common functionality for other activities in the app.
 * This base class is designed for a standard, non-edge-to-edge screen layout.
 */
open class BaseActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
    }

    /**
     * A utility function to apply system window insets (like the status and navigation bars)
     * as padding to a given view. This is used to prevent content from being drawn behind
     * the system bars in a non-edge-to-edge layout.
     *
     * @param view The view to which the insets will be applied as padding.
     */
    fun applyWindowInsetsTo(view: View) {
        ViewCompat.setOnApplyWindowInsetsListener(view) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }
    }
}

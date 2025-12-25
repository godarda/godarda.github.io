// Frame busting protection: Ensures the site is not loaded within an iframe.
try {
    self !== top && (top.location = self.location);
} catch (e) {
    document.documentElement.style.display = 'none';
}

// Touch event variables for swipe detection
var xDown = null, yDown = null, xUp = null, yUp = null;
document.addEventListener('touchstart', touchstart, { passive: true });
document.addEventListener('touchmove', touchmove, { passive: true });
document.addEventListener('touchend', touchend, { passive: true });

// Capture the starting coordinates of a touch event
function touchstart(evt) { const firstTouch = (evt.touches || evt.originalEvent.touches)[0]; xDown = firstTouch.clientX; yDown = firstTouch.clientY; }

// Track the movement coordinates during a touch event
function touchmove(evt) { if (!xDown || !yDown) return; xUp = evt.touches[0].clientX; yUp = evt.touches[0].clientY; }

// Handle the end of a touch event to determine swipe direction
function touchend() {
    var xDiff = xUp - xDown, yDiff = yUp - yDown;
    // Check if the horizontal movement is significant enough to be considered a swipe
    if ((Math.abs(xDiff) > Math.abs(yDiff)) && (Math.abs(xDiff) > 0.6 * document.body.clientWidth)) {
        if (xDiff > 0) {
            // Swipe right: Open left sidebar
            $('.leftsidebar-collapse').toggleClass('open')
        }
        else {
            // Swipe left: Close left sidebar
            $('.leftsidebar-collapse').removeClass('open')
        }
    }
    xDown = null, yDown = null;
}

// Sidebar and UI interaction handlers
$(function () {
    // Toggle left sidebar visibility
    $('[data-bs-toggle="leftsidebar"]').on('click', function () {
        $('.rightsidebar-collapse').removeClass('open')
        $('.leftsidebar-collapse').toggleClass('open')
    })
    // Toggle right sidebar visibility
    $('[data-bs-toggle="rightsidebar"]').on('click', function () {
        $('.leftsidebar-collapse').removeClass('open')
        $('.rightsidebar-collapse').toggleClass('open')
    })
    // Collapse all sidebars
    $('[data-bs-toggle="collapseall"]').on('click', function () {
        $('.leftsidebar-collapse').removeClass('open')
        $('.rightsidebar-collapse').removeClass('open')
    })
    // Prevent dragging of anchor tags
    $('html').on('dragstart', 'a', function () { return false; });
});

// Disable specific keyboard shortcuts (F12, Inspect Element, View Source, Save)
$(document).keydown(function (event) {
    if (event.keyCode == 123 || // F12
        (event.ctrlKey && event.shiftKey && event.keyCode == 73) || // Ctrl+Shift+I
        (event.ctrlKey && event.keyCode == 85) || // Ctrl+U
        (event.ctrlKey && event.keyCode == 83)) { // Ctrl+S
        return false;
    }
});

/* --------------------------------------------------------------------------------------------- */
// User Agent Detection
/* --------------------------------------------------------------------------------------------- */

const navigator = window.navigator;
window.userAgent = navigator.userAgent;
const normalizedUserAgent = window.userAgent.toLowerCase();
const standalone = navigator.standalone;
const isAndroid = /android/.test(normalizedUserAgent);
// Detect if running inside an Android WebView
window.isWebview = (isAndroid && /; wv\)/.test(normalizedUserAgent));

/* --------------------------------------------------------------------------------------------- */
// Scroll and Modal Logic
/* --------------------------------------------------------------------------------------------- */

$(document).ready(function () {
    // Smooth scroll to top
    $('.back-to-top').click(function () { $('html, body').animate({ scrollTop: 0 }, 100); });

    var today = new Date().toLocaleDateString();
    var is_shown = sessionStorage.getItem('status');
    var backToTop = document.getElementById("backtotop");
    var leftSidebar = $('.leftsidebar-collapse');
    var rightSidebar = $('.rightsidebar-collapse');

    $(window).scroll(function (e) {
        var scrollTop = $(window).scrollTop();
        
        // Show modal once per day when user scrolls past 50% of the page
        if (is_shown != today) {
            var scrollPercent = ((scrollTop) / ($(document).height() - $(window).height())) * 100;
            if (scrollPercent >= 50) {
                $('#staticBackdrop').modal('show');
                sessionStorage.setItem('status', today);
                is_shown = today;
            }
        }

        // Toggle "Back to Top" button visibility
        if (scrollTop > 100) {
            if (backToTop.style.display !== "block") backToTop.style.display = "block";
        } else {
            if (backToTop.style.display !== "none") backToTop.style.display = "none";
        }
        
        // Auto-close sidebars on scroll
        if (leftSidebar.hasClass('open')) {
            leftSidebar.removeClass('open')
        }
        if (rightSidebar.hasClass('open')) {
            rightSidebar.removeClass('open')
        }
    });
});

/* --------------------------------------------------------------------------------------------- */
// Theme Management (Dark/Light Mode)
/* --------------------------------------------------------------------------------------------- */

const getStoredTheme = () => localStorage.getItem('theme')
const setStoredTheme = theme => localStorage.setItem('theme', theme)

// Determine preferred theme based on storage or system preference
const getPreferredTheme = () => {
    const storedTheme = getStoredTheme()
    if (storedTheme) {
        return storedTheme
    }
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
}

// Apply the selected theme to the document
const setTheme = theme => {
    if (theme === 'auto') {
        document.documentElement.setAttribute('data-bs-theme', window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')
    } else {
        document.documentElement.setAttribute('data-bs-theme', theme)
    }
}

// Update the theme switcher UI to reflect the active theme
const showActiveTheme = (theme, focus = false) => {
    const androidTheme = document.querySelector('#android_theme')
    if (androidTheme) {
        androidTheme.classList.remove('bi-moon-stars', 'bi-sun', 'bi-circle-half')
        if (theme === 'auto') {
            androidTheme.classList.add('bi-circle-half')
        } else if (theme === 'dark') {
            androidTheme.classList.add('bi-moon-stars')
        } else {
            androidTheme.classList.add('bi-sun')
        }
    }

    const themeSwitcher = document.querySelector('#bd-theme')
    if (!themeSwitcher) {
        return
    }

    const themeSwitcherText = document.querySelector('#bd-theme-text')
    const activeThemeIcon = document.querySelector('#bd-theme-icon')
    const btnToActive = document.querySelector(`[data-bs-theme-value="${theme}"]`)
    const svgOfActiveBtn = btnToActive.querySelector('i').getAttribute('class')

    document.querySelectorAll('[data-bs-theme-value]').forEach(element => {
        element.classList.remove('active')
        element.setAttribute('aria-pressed', 'false')
    })

    btnToActive.classList.add('active')
    btnToActive.setAttribute('aria-pressed', 'true')
    activeThemeIcon.setAttribute('class', svgOfActiveBtn)
    const themeSwitcherLabel = `${themeSwitcherText.textContent} (${btnToActive.dataset.bsThemeValue})`
    themeSwitcher.setAttribute('aria-label', themeSwitcherLabel)

    if (focus) {
        themeSwitcher.focus()
    }
}

// Listen for system theme changes
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
    const storedTheme = getStoredTheme()
    if (storedTheme !== 'light' && storedTheme !== 'dark') {
        setTheme(getPreferredTheme())
    }
})

// Initialize theme on DOM load
window.addEventListener('DOMContentLoaded', () => {
    if (window.isWebview) {
        const at = document.getElementById('android_theme');
        if (at) at.style.display = 'block';
    }
    showActiveTheme(getStoredTheme() || 'auto')
    document.querySelectorAll('[data-bs-theme-value], #android_theme')
        .forEach(toggle => {
            toggle.addEventListener('click', (event) => {
                event.preventDefault()
                let theme = toggle.getAttribute('data-bs-theme-value')
                // If no specific value is set (e.g., Android toggle), switch between light/dark
                if (!theme) {
                    const stored = getStoredTheme() || 'auto'
                    const cycles = ['auto', 'light', 'dark']
                    theme = cycles[(cycles.indexOf(stored) + 1) % cycles.length]
                }
                setStoredTheme(theme)
                setTheme(theme)
                showActiveTheme(theme, true)
            })
        })
})

/* --------------------------------------------------------------------------------------------- */
// Google Analytics Configuration
/* --------------------------------------------------------------------------------------------- */

window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());

gtag('config', 'G-8ZJLP1KH1R', {
    ignore_referrer: 'true',
    'linker': {
        'domains': ['godarda.in']
    }
});

/* --------------------------------------------------------------------------------------------- */

var year = new Date().getFullYear();
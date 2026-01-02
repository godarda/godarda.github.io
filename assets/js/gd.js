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
function touchstart(evt) {
    if (!evt.touches || evt.touches.length === 0) return;
    const firstTouch = evt.touches[0];
    xDown = firstTouch.clientX;
    yDown = firstTouch.clientY;
}

// Track the movement coordinates during a touch event
function touchmove(evt) {
    if (!xDown || !yDown || !evt.touches || evt.touches.length === 0) return;
    xUp = evt.touches[0].clientX;
    yUp = evt.touches[0].clientY;
}

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
    // Force the default cursor to prevent the I-beam from appearing over text.
    $('body').css('cursor', 'default');
    // Ensure input fields and textareas still show the text cursor for editing.
    $('input, textarea').css('cursor', 'text');

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

// Disable specific keyboard shortcuts, right-click, and text selection
$(document).on('keydown', function (event) {
    if (event.keyCode == 123 || // F12
        (event.ctrlKey && event.shiftKey && event.keyCode == 73) || // Ctrl+Shift+I
        (event.ctrlKey && event.keyCode == 85) || // Ctrl+U
        (event.ctrlKey && event.keyCode == 83)) { // Ctrl+S
        return false;
    }
}).on('contextmenu selectstart', function () {
    return false;
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
window.isGoDardaApp = window.isWebview || (window.userAgent && window.userAgent.includes("GoDarda"));

/* --------------------------------------------------------------------------------------------- */
// Scroll and Modal Logic
/* --------------------------------------------------------------------------------------------- */

$(document).ready(function () {
    // Smooth scroll to top
    $('.back-to-top').click(function () { $('html, body').animate({ scrollTop: 0 }, 100); });

    // Scroll active sidebar item into view on page load.
    var activeItems = document.querySelectorAll('.sidebar-item-active');
    if (activeItems.length > 0) {
      var lastActiveItem = activeItems[activeItems.length - 1];
      lastActiveItem.scrollIntoView({ block: 'center', behavior: 'auto' });
    }

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
// Update the theme switcher UI to reflect the active theme
const showActiveTheme = (theme, focus = false) => {
    const themeCard = document.querySelector('#app-theme-switcher');
    if (themeCard) {
        if (theme === 'auto') {
            themeCard.textContent = 'Theme: System Default';
        } else if (theme === 'dark') {
            themeCard.textContent = 'Theme: Dark';
        } else {
            themeCard.textContent = 'Theme: Light';
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

// Initialize theme on DOM load
window.addEventListener('DOMContentLoaded', () => {
    const storedTheme = getStoredTheme() || 'auto';
    showActiveTheme(storedTheme);
    document.querySelectorAll('[data-bs-theme-value], #app-theme-switcher')
        .forEach(toggle => {
            toggle.addEventListener('click', (event) => {
                event.preventDefault()
                let theme = toggle.getAttribute('data-bs-theme-value')
                // If no specific value is set, switch between light/dark
                if (!theme) {
                    const stored = getStoredTheme() || 'auto'
                    const cycles = ['auto', 'light', 'dark']
                    theme = cycles[(cycles.indexOf(stored) + 1) % cycles.length]
                }
                setStoredTheme(theme)
                setTheme(theme)
                showActiveTheme(theme, toggle.matches('[data-bs-theme-value]'))
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

/* --------------------------------------------------------------------------------------------- */
// Copy to Clipboard for Code Blocks
/* --------------------------------------------------------------------------------------------- */
document.addEventListener('DOMContentLoaded', function() {
    const copyButtons = document.querySelectorAll('.copy-btn');

    copyButtons.forEach(button => {
        button.addEventListener('click', function() {
            const card = this.closest('.card');
            if (card) {
                const pre = card.nextElementSibling;
                if (pre && pre.tagName === 'PRE') {
                    const pageUrl = window.location.href;
                    const codeToCopy = pageUrl + '\n\n' + pre.innerText;
                    navigator.clipboard.writeText(codeToCopy).then(() => {
                        this.classList.add('show-tooltip');
                        this.setAttribute('title', 'Copied!');
                        setTimeout(() => {
                            this.classList.remove('show-tooltip');
                            this.setAttribute('title', 'Copy code');
                        }, 2000);
                    }).catch(err => { console.error('Failed to copy text: ', err); });
                }
            }
        });
    });
});
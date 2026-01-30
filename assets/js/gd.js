/**
 * GoDarda - Main JavaScript File (gd.js)
 *
 * Purpose:
 * This file serves as the central hub for client-side interactivity and logic
 * on the GoDarda website. It orchestrates UI behaviors, event handling,
 * security measures, and third-party integrations to ensure a smooth and
 * secure user experience.
 *
 * Key Features and Responsibilities:
 * 1. Security Enhancements:
 *    - Frame Busting: Prevents the site from being loaded inside iframes (clickjacking protection).
 *    - Input Protection: Disables specific keyboard shortcuts (F12, Ctrl+U, etc.) and context menus.
 *
 * 2. User Interface & Interaction:
 *    - Sidebar Management: Handles toggling and collapsing of left/right sidebars.
 *    - Swipe Gestures: Implements touch-based swipe detection for mobile sidebar navigation.
 *    - Scroll Behaviors: Manages "Back to Top" visibility, scroll-triggered modals, and active item highlighting.
 *    - Theme Switcher: Controls Light/Dark mode toggling and persistence via local storage.
 *
 * 3. Utility Functions:
 *    - Clipboard Integration: Provides "Copy to Clipboard" functionality for code blocks.
 *    - User Agent Detection: Identifies Android WebViews or specific app environments.
 *    - Analytics: Configures Google Analytics (GA4) for traffic tracking.
 */

// --------------------------------------------------------------------------
// Frame Busting
// --------------------------------------------------------------------------
// Ensures the site is not loaded within an iframe, which can be a security risk (clickjacking).
try {
    if (self !== top) {
        top.location = self.location;
    }
} catch (e) {
    // If the browser's security policy blocks access, hide the page content.
    $(() => { $('html').hide(); });
}

// --------------------------------------------------------------------------
// Swipe Actions
// --------------------------------------------------------------------------
// Global variables to store touch coordinates for swipe detection.
let xDown = null;
let yDown = null;
let xUp = null;
let yUp = null;

const handleTouchStart = (evt) => {
    const firstTouch = (evt.touches || evt.originalEvent.touches)[0];
    xDown = firstTouch.clientX;
    yDown = firstTouch.clientY;
    xUp = null;
    yUp = null;
};

const handleTouchMove = (evt) => {
    if (!xDown || !yDown) return;
    xUp = (evt.originalEvent || evt).touches[0].clientX;
    yUp = (evt.originalEvent || evt).touches[0].clientY;
};

const handleTouchEnd = () => {
    // Prevent swipe actions if a modal is open
    if ($('body').hasClass('modal-open')) {
        xDown = null;
        yDown = null;
        return;
    }
    if (!xUp || !yUp) return;
    const xDiff = xUp - xDown;
    const yDiff = yUp - yDown;
    // Check if the horizontal movement is significant enough to be considered a swipe
    if ((Math.abs(xDiff) > Math.abs(yDiff)) && (Math.abs(xDiff) > 0.6 * document.body.clientWidth)) {
        if (xDiff > 0) {
            // Swipe right: Open left sidebar
            $('.leftsidebar-collapse').toggleClass('open');
        } else {
            // Swipe left: Close left sidebar
            $('.leftsidebar-collapse').removeClass('open');
        }
    }
    xDown = null;
    yDown = null;
};

// --------------------------------------------------------------------------
// DOM Ready - Main Execution
// --------------------------------------------------------------------------
$(() => {
    // Attach swipe event listeners to the document.
    $(document).on('touchstart', handleTouchStart);
    $(document).on('touchmove', handleTouchMove);
    $(document).on('touchend', handleTouchEnd);

    // --------------------------------------------------------------------------
    // UI Initialization & Event Handlers
    // --------------------------------------------------------------------------
    // Force the default cursor to prevent the I-beam from appearing over text.
    $('body').css('cursor', 'default');
    // Ensure input fields and textareas still show the text cursor for editing.
    $('input, textarea').css('cursor', 'text');

    // Toggle left sidebar visibility
    $('[data-bs-toggle="leftsidebar"]').on('click', () => {
        $('.rightsidebar-collapse').removeClass('open');
        $('.leftsidebar-collapse').toggleClass('open');
    });
    // Toggle right sidebar visibility
    $('[data-bs-toggle="rightsidebar"]').on('click', () => {
        $('.leftsidebar-collapse').removeClass('open');
        $('.rightsidebar-collapse').toggleClass('open');
    });
    // Collapse all sidebars
    $('[data-bs-toggle="collapseall"]').on('click', () => {
        $('.leftsidebar-collapse').removeClass('open');
        $('.rightsidebar-collapse').removeClass('open');
    });
    // Prevent dragging of anchor tags
    $('html').on('dragstart', 'a', () => false);

    // --------------------------------------------------------------------------
    // Security Measures
    // --------------------------------------------------------------------------
    // Disable specific keyboard shortcuts, right-click, and text selection
    $(document).on('keydown', (event) => {
        const { key, ctrlKey, shiftKey } = event;
        // Use event.key instead of deprecated event.keyCode
        if (key === 'F12' || // F12
            (ctrlKey && shiftKey && key.toUpperCase() === 'I') || // Ctrl+Shift+I
            (ctrlKey && key.toUpperCase() === 'U') || // Ctrl+U
            (ctrlKey && key.toUpperCase() === 'S')) { // Ctrl+S
            return false;
        }
    }).on('contextmenu selectstart', () => false);

    // --------------------------------------------------------------------------
    // Scroll-based Behaviors
    // --------------------------------------------------------------------------
    // Smooth scroll to top
    $('.back-to-top').on('click', () => {
        $('html, body').animate({ scrollTop: 0 }, 100);
    });

    // Scroll active sidebar item into view on page load.
    const $activeItems = $('.sidebar-item-active');
    if ($activeItems.length > 0) {
        const lastActiveItem = $activeItems.last()[0];
        lastActiveItem.scrollIntoView({ block: 'center', behavior: 'auto' });
    }

    const today = new Date().toLocaleDateString();
    let isShown = sessionStorage.getItem('status');
    const $backToTop = $("#backtotop");
    const $leftSidebar = $('.leftsidebar-collapse');
    const $rightSidebar = $('.rightsidebar-collapse');
    const $staticBackdrop = $('#staticBackdrop');

    let ticking = false;
    $(window).on('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                const scrollTop = $(window).scrollTop();

                // Show modal once per day when user scrolls past 50% of the page
                if (isShown !== today) {
                    const scrollPercent = ((scrollTop) / ($(document).height() - $(window).height())) * 100;
                    if (scrollPercent >= 50) {
                        $staticBackdrop.modal('show');
                        sessionStorage.setItem('status', today);
                        isShown = today;
                    }
                }

                // Toggle "Back to Top" button visibility
                if (scrollTop > 100) {
                    $backToTop.show();
                } else {
                    $backToTop.hide();
                }

                // Auto-close sidebars on scroll
                if ($leftSidebar.hasClass('open')) {
                    $leftSidebar.removeClass('open');
                }
                if ($rightSidebar.hasClass('open')) {
                    $rightSidebar.removeClass('open');
                }
                ticking = false;
            });
            ticking = true;
        }
    });

    // --------------------------------------------------------------------------
    // Theme Management (Dark/Light Mode)
    // --------------------------------------------------------------------------
    // Updates the theme switcher UI to reflect the active theme.
    const showActiveTheme = (theme, focus = false) => {
        const $appThemeRadios = $('#app [name="theme-radio"]');
        if ($appThemeRadios.length) {
            $appThemeRadios.filter(`[data-bs-theme-value="${theme}"]`).prop('checked', true);
        }

        const $themeSwitcher = $('#bd-theme');
        if (!$themeSwitcher.length) {
            return;
        }

        const $themeSwitcherText = $('#bd-theme-text');
        const $activeThemeIcon = $('#bd-theme-icon');
        const $btnToActive = $(`[data-bs-theme-value="${theme}"]`);
        const svgOfActiveBtn = $btnToActive.find('i').attr('class');
        $('[data-bs-theme-value]').removeClass('active').attr('aria-pressed', 'false');
        $btnToActive.addClass('active').attr('aria-pressed', 'true');
        $activeThemeIcon.attr('class', svgOfActiveBtn);
        const themeSwitcherLabel = `${$themeSwitcherText.text()} (${$btnToActive.data('bs-theme-value')})`;
        $themeSwitcher.attr('aria-label', themeSwitcherLabel);

        if (focus) {
            $themeSwitcher.focus();
        }
    };

    // Initialize theme on DOM load.
    const storedTheme = getStoredTheme() || 'auto';
    showActiveTheme(storedTheme);

    // Handle theme switching from the dropdown menu
    $('.dropdown-menu [data-bs-theme-value]').on('click', (event) => {
        event.preventDefault();
        const theme = $(event.currentTarget).data('bs-theme-value');
        setStoredTheme(theme);
        setTheme(theme);
        showActiveTheme(theme, true);
    });

    // Handle theme switching from the radio buttons in the app footer
    $('#app input[name="theme-radio"]').on('change', (event) => {
        const theme = $(event.currentTarget).data('bs-theme-value');
        setStoredTheme(theme);
        setTheme(theme);
        showActiveTheme(theme, true);
    });

    // --------------------------------------------------------------------------
    // Clipboard Functionality
    // --------------------------------------------------------------------------
    // Initialize tooltips for copy buttons
    $('.copy-btn').each(function () {
        // Set attributes via JS to avoid repetition in HTML config
        $(this).attr('data-bs-toggle', 'tooltip');
        $(this).css('cursor', 'pointer');
        if (!this.getAttribute('title') && !this.getAttribute('data-bs-original-title')) {
            this.setAttribute('title', 'Copy');
        }
        if (typeof bootstrap !== 'undefined' && bootstrap.Tooltip) {
            new bootstrap.Tooltip(this);
        }
    });

    // Lazy-initialize tooltip on hover to handle cases where Bootstrap loads late.
    $('.copy-btn').on('mouseenter', function () {
        // Ensure attributes exist
        $(this).attr('data-bs-toggle', 'tooltip');
        $(this).css('cursor', 'pointer');
        if (!this.getAttribute('title') && !this.getAttribute('data-bs-original-title')) {
            this.setAttribute('title', 'Copy');
        }
        if (typeof bootstrap !== 'undefined' && bootstrap.Tooltip && !bootstrap.Tooltip.getInstance(this)) {
            new bootstrap.Tooltip(this).show();
        }
    });

    // Handles the "copy" button on code blocks.
    $('.copy-btn').on('click', (event) => {
        const $button = $(event.currentTarget);
        const $card = $button.closest('.card');
        if ($card.length) {
            const $pre = $card.next('pre');
            if ($pre.length) {
                const pageUrl = window.location.href;
                const codeToCopy = `${pageUrl}\n\n${$pre.text()}`;
                navigator.clipboard.writeText(codeToCopy).then(() => {
                    const $icon = $button.find('i');
                    const originalIconClass = $icon.attr('class');
                    $icon.attr('class', 'bi bi-clipboard-check');

                    if (typeof bootstrap !== 'undefined' && bootstrap.Tooltip) {
                        const btnElement = $button[0];
                        let tooltip = bootstrap.Tooltip.getInstance(btnElement);
                        if (!tooltip) {
                            tooltip = new bootstrap.Tooltip(btnElement);
                        }
                        $button.attr('data-bs-original-title', 'Copied!');
                        tooltip.show();
                        setTimeout(() => {
                            tooltip.hide();
                            $button.attr('data-bs-original-title', 'Copy');
                            $icon.attr('class', originalIconClass);
                        }, 2000);
                    }
                }).catch(err => {
                    console.error('Failed to copy text: ', err);
                });
            }
        }
    });
});

// --------------------------------------------------------------------------
// User Agent Detection
// --------------------------------------------------------------------------
window.userAgent = navigator.userAgent;
const normalizedUserAgent = (window.userAgent || '').toLowerCase();
const isAndroid = /android/.test(normalizedUserAgent);
// Detect if running inside an Android WebView
window.isWebview = (isAndroid && /; wv\)/.test(normalizedUserAgent));
window.isGoDardaApp = window.isWebview || (window.userAgent && window.userAgent.includes("GoDarda"));

// --------------------------------------------------------------------------
// Google Analytics Configuration
// --------------------------------------------------------------------------
window.dataLayer = window.dataLayer || [];
function gtag(){ window.dataLayer.push(arguments); }
gtag('js', new Date());

if (window.location.hostname !== "localhost" && window.location.hostname !== "127.0.0.1" && window.location.protocol !== "file:") {
    gtag('config', 'G-8ZJLP1KH1R', {
        ignore_referrer: 'true'
    });
}

// --------------------------------------------------------------------------
// Set the current year for use in the footer or other parts of the site.
const year = new Date().getFullYear();

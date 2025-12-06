this.top.location !== this.location && (this.top.location = this.location);

var xDown = null, yDown = null, xUp = null, yUp = null;
document.addEventListener('touchstart', touchstart);
document.addEventListener('touchmove', touchmove);
document.addEventListener('touchend', touchend);
function touchstart(evt) { const firstTouch = (evt.touches || evt.originalEvent.touches)[0]; xDown = firstTouch.clientX; yDown = firstTouch.clientY; }
function touchmove(evt) { if (!xDown || !yDown) return; xUp = evt.touches[0].clientX; yUp = evt.touches[0].clientY; }
function touchend() {
    var xDiff = xUp - xDown, yDiff = yUp - yDown;
    if ((Math.abs(xDiff) > Math.abs(yDiff)) && (Math.abs(xDiff) > 0.6 * document.body.clientWidth)) {
        if (xDiff > 0) {
            $('.leftsidebar-collapse').toggleClass('open')
        }
        else {
            $('.leftsidebar-collapse').removeClass('open')
        }
    }
    xDown = null, yDown = null;
}

$(function () {
    $('[data-bs-toggle="leftsidebar"]').on('click', function () {
        $('.rightsidebar-collapse').removeClass('open')
        $('.leftsidebar-collapse').toggleClass('open')
    })
    $('[data-bs-toggle="rightsidebar"]').on('click', function () {
        $('.leftsidebar-collapse').removeClass('open')
        $('.rightsidebar-collapse').toggleClass('open')
    })
    $('[data-bs-toggle="collapseall"]').on('click', function () {
        $('.leftsidebar-collapse').removeClass('open')
        $('.rightsidebar-collapse').removeClass('open')
    })
    $('html').on('dragstart', 'a', function () { return false; });
});

$(document).keydown(function (event) {
    if (event.keyCode == 123) { return false; }
});

/* --------------------------------------------------------------------------------------------- */

const navigator = window.navigator;
window.userAgent = navigator.userAgent;
const normalizedUserAgent = window.userAgent.toLowerCase();
const standalone = navigator.standalone;
const isAndroid = /android/.test(normalizedUserAgent);
window.isWebview = (isAndroid && /; wv\)/.test(normalizedUserAgent));

/* --------------------------------------------------------------------------------------------- */

$(document).ready(function () {
    $('.back-to-top').click(function () { $('html, body').animate({ scrollTop: 0 }, 100); });
    $(window).scroll(function (e) {
        var is_shown = sessionStorage.getItem('status');
        var scrollTop = $(window).scrollTop();
        var docHeight = $(document).height();
        var winHeight = $(window).height();
        var scrollPercent = ((scrollTop) / (docHeight - winHeight)) * 100;
        var today = new Date().toLocaleDateString();
        if (scrollPercent >= 50 && is_shown != today) {
            $('#staticBackdrop').modal('show');
            sessionStorage.setItem('status', today);
        }
        else {
            $('#staticBackdrop').modal('hide');
        }
    });
});
window.onscroll = function () {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        document.getElementById("backtotop").style.display = "block";
    }
    else {
        document.getElementById("backtotop").style.display = "none";
    }
    $('.leftsidebar-collapse').removeClass('open')
    $('.rightsidebar-collapse').removeClass('open')
};

/* --------------------------------------------------------------------------------------------- */

const getStoredTheme = () => localStorage.getItem('theme')
const setStoredTheme = theme => localStorage.setItem('theme', theme)

const getPreferredTheme = () => {
    const storedTheme = getStoredTheme()
    if (storedTheme) {
        return storedTheme
    }
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
}

const setTheme = theme => {
    if (theme === 'auto' && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.documentElement.setAttribute('data-bs-theme', 'dark')
    } else {
        document.documentElement.setAttribute('data-bs-theme', theme)
    }
}

setTheme(getPreferredTheme())

const showActiveTheme = (theme, focus = false) => {
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

window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
    const storedTheme = getStoredTheme()
    if (storedTheme !== 'light' && storedTheme !== 'dark') {
        setTheme(getPreferredTheme())
    }
})

window.addEventListener('DOMContentLoaded', () => {
    showActiveTheme(getPreferredTheme())
    document.querySelectorAll('[data-bs-theme-value]')
        .forEach(toggle => {
            toggle.addEventListener('click', () => {
                const theme = toggle.getAttribute('data-bs-theme-value')
                setStoredTheme(theme)
                setTheme(theme)
                showActiveTheme(theme, true)
            })
        })
})

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
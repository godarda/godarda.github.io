// Externalized search JS for GoDarda
// Expects `window.gd_path1` to be set by the page (Liquid assigns it in the include).
(function () {
    document.addEventListener('DOMContentLoaded', function () {
        const containerId = window.gd_path1 || '';
        const container = document.getElementById(containerId);
        if (!container) return;

        // Cache frequently-used DOM nodes
        const matchCountEl = document.getElementById('matchCount');
        const input = document.getElementById('KSEInput');
        if (!input) return;

        // Utilities (used by loader and renderers)
        function escapeRegExp(s) { return s.replace(/[.*+?^${}()|[\\]\\]/g, '\\$&'); }
        function escapeHtml(unsafe) { return (unsafe || '').replace(/[&<>\"]/g, function (ch) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[ch]; }); }

        // Lazy-loaded items. We avoid parsing JSON blobs until the user actually
        // interacts with the search input to keep initial page load light.
        let items = null; // null = not loaded; [] = loaded but empty
        function loadItemsIfNeeded() {
            if (items !== null) return;
            items = [];
            const dataScript = document.getElementById('search-data-' + containerId);
            if (dataScript) {
                try {
                    const data = JSON.parse(dataScript.textContent || dataScript.innerText || '[]');
                    items = data.map(o => ({
                        title: (o.title || '').trim(),
                        href: o.href || '#',
                        safeTitle: escapeHtml(o.title || ''),
                        lowerTitle: (o.title || '').toLowerCase()
                    }));
                    return;
                } catch (e) {
                    items = [];
                    return;
                }
            }

            if (containerId === 'search') {
                // Aggregate all segment blobs only when needed (main search page)
                const scripts = Array.from(document.querySelectorAll('script[type="application/json"][id^="search-data-"]'));
                const agg = [];
                scripts.forEach(s => {
                    try {
                        const d = JSON.parse(s.textContent || s.innerText || '[]');
                        d.forEach(o => agg.push(o));
                    } catch (e) { /* ignore malformed segment */ }
                });
                items = agg.map(o => ({ title: (o.title || '').trim(), href: o.href || '#', safeTitle: escapeHtml(o.title || ''), lowerTitle: (o.title || '').toLowerCase() }));
                return;
            }

            // Fallback: if the page still contains anchors (older templates), read them
            const anchors = Array.from(container.querySelectorAll('a'));
            items = anchors.map(a => ({ title: (a.textContent || '').trim(), href: a.getAttribute('href') || a.getAttribute('data-href') || '#', safeTitle: escapeHtml(a.textContent || ''), lowerTitle: (a.textContent || '').toLowerCase() }));
        }

        // Scoring helper (operates on precomputed lowerTitle)
        function scoreFor(lowerTitle, qtrim, tokens) {
            if (lowerTitle === qtrim) return { score: 100, type: 'exact' };
            if (qtrim && lowerTitle.startsWith(qtrim)) return { score: 90, type: 'prefix' };
            if (qtrim.length > 1 && lowerTitle.indexOf(qtrim) !== -1) return { score: 80, type: 'substring' };
            if (tokens.length > 0 && tokens.every(t => lowerTitle.indexOf(t) !== -1)) return { score: 70 + tokens.length, type: 'alltokens' };
            const matches = tokens.reduce((c, t) => c + (lowerTitle.indexOf(t) !== -1 ? 1 : 0), 0);
            if (matches > 0) return { score: 40 + matches, type: 'anytokens' };
            return { score: 0, type: null };
        }

        // Highlighting: use pre-escaped safeTitle to avoid re-escaping repeatedly.
        function buildHighlighted(item, qtrim, tokens, type) {
            const safe = item.safeTitle;
            if (!qtrim) return safe;
            try {
                if (type === 'exact' || type === 'prefix' || type === 'substring') {
                    const re = new RegExp('(' + escapeRegExp(qtrim) + ')', 'ig');
                    return safe.replace(re, '<mark>$1</mark>');
                }
                const uniq = Array.from(new Set(tokens)).sort((a, b) => b.length - a.length);
                let out = safe;
                uniq.forEach(token => {
                    if (!token) return;
                    const re = new RegExp('(' + escapeRegExp(token) + ')', 'ig');
                    out = out.replace(re, '<mark>$1</mark>');
                });
                return out;
            } catch (err) {
                const orig = item.title || '';
                const lowerOrig = orig.toLowerCase();
                const uniq = Array.from(new Set(tokens)).sort((a, b) => b.length - a.length);
                const ranges = [];
                uniq.forEach(token => {
                    if (!token) return;
                    const lowerToken = token.toLowerCase();
                    let startPos = 0;
                    while (true) {
                        const pos = lowerOrig.indexOf(lowerToken, startPos);
                        if (pos === -1) break;
                        ranges.push([pos, pos + lowerToken.length]);
                        startPos = pos + Math.max(1, lowerToken.length);
                    }
                });

                if (ranges.length === 0) return escapeHtml(orig);

                ranges.sort((a, b) => a[0] - b[0]);
                const merged = [ranges[0].slice()];
                for (let i = 1; i < ranges.length; i++) {
                    const cur = ranges[i];
                    const last = merged[merged.length - 1];
                    if (cur[0] <= last[1]) {
                        last[1] = Math.max(last[1], cur[1]);
                    } else {
                        merged.push(cur.slice());
                    }
                }

                const parts = [];
                let idx = 0;
                merged.forEach(r => {
                    const s = r[0], e = r[1];
                    if (idx < s) parts.push(escapeHtml(orig.substring(idx, s)));
                    parts.push('<mark>' + escapeHtml(orig.substring(s, e)) + '</mark>');
                    idx = e;
                });
                if (idx < orig.length) parts.push(escapeHtml(orig.substring(idx)));
                return parts.join('');
            }
        }

        // Render: compute scores, pick top 25, and update DOM efficiently.
        function renderMatches(q) {
            const qtrim = (q || '').trim().toLowerCase();
            if (qtrim.length === 0) {
                container.style.display = 'none';
                if (matchCountEl) matchCountEl.style.display = 'none';
                return;
            }

            // Ensure data is loaded lazily on first interaction
            loadItemsIfNeeded();

            const tokens = qtrim.split(/\s+/).filter(Boolean);

            // Fast path: map with precomputed lowerTitle
            const scoredAll = items.map(it => {
                const s = scoreFor(it.lowerTitle, qtrim, tokens);
                return Object.assign({}, it, s);
            }).filter(r => r.score > 0)
                .sort((a, b) => (b.score - a.score) || a.title.localeCompare(b.title));

            const totalMatches = scoredAll.length;
            const displayed = scoredAll.slice(0, 25);

            // Build DOM off-screen
            const frag = document.createDocumentFragment();
            displayed.forEach(r => {
                const a = document.createElement('a');
                a.className = 'codecard card';
                a.href = r.href;
                a.onclick = function () { clear_input(); };
                a.style.display = 'block';
                a.style.marginBottom = '6px';
                a.innerHTML = buildHighlighted(r, qtrim, tokens, r.type);
                frag.appendChild(a);
            });

            // Batch DOM update
            window.requestAnimationFrame(() => {
                container.innerHTML = '';
                container.appendChild(frag);
                container.style.display = 'block';
                if (matchCountEl) {
                    matchCountEl.textContent = 'Showing ' + Math.min(25, totalMatches) + ' of ' + totalMatches + (totalMatches === 1 ? ' result' : ' results');
                    matchCountEl.style.display = 'block';
                }
            });
        }

        // Attach a debounced input handler to the search input (id="KSEInput").
        // We debounce to avoid running expensive work on every keystroke.
        let tid = null;
        input.addEventListener('input', function (e) {
            clearTimeout(tid);
            const v = e.target.value || '';
            // Toggle icons immediately for UX
            if (v.length === 0) {
                document.getElementById('search_icon') && (document.getElementById('search_icon').style.display = 'inline-block');
                document.getElementById('close_icon') && (document.getElementById('close_icon').style.display = 'none');
                renderMatches('');
                return;
            } else {
                document.getElementById('search_icon') && (document.getElementById('search_icon').style.display = 'none');
                document.getElementById('close_icon') && (document.getElementById('close_icon').style.display = 'inline-block');
            }
            // 150ms debounce gives a balance of responsiveness and work reduction
            tid = setTimeout(() => renderMatches(v), 150);
        });

    });

    // Clear the search input and hide any visible results or icons.
    window.clear_input = function () {
        const inputEl = document.getElementById("KSEInput");
        if (inputEl) inputEl.value = "";
        if (window.gd_path1) {
            const el = document.getElementById(window.gd_path1);
            if (el) el.style.display = "none";
        }
        const searchEl = document.getElementById("search");
        if (searchEl) searchEl.style.display = "none";
        const closeIcon = document.getElementById("close_icon");
        if (closeIcon) closeIcon.style.display = "none";
        const searchIcon = document.getElementById("search_icon");
        if (searchIcon) searchIcon.style.display = "inline-block";
        var mc = document.getElementById('matchCount');
        if (mc) mc.style.display = 'none';
    };

    // Update UI controls based on whether the input contains text. This is a
    // small helper used by the onkeypress/onkeyup attributes on the input field.
    window.display_results = function () {
        if (typeof jQuery !== 'undefined' && jQuery("#KSEInput").val().length == 0) {
            const closeIcon = document.getElementById("close_icon"); if (closeIcon) closeIcon.style.display = "none";
            const searchIcon = document.getElementById("search_icon"); if (searchIcon) searchIcon.style.display = "inline-block";
            if (window.gd_path1) {
                const el = document.getElementById(window.gd_path1); if (el) el.style.display = "none";
            }
            const searchEl = document.getElementById("search"); if (searchEl) searchEl.style.display = "none";
            var mc2 = document.getElementById('matchCount'); if (mc2) mc2.style.display = 'none';
        } else if (typeof jQuery !== 'undefined' && jQuery("#KSEInput").val().length >= 1) {
            const searchEl = document.getElementById("search"); if (searchEl) searchEl.style.display = "block";
            const closeIcon = document.getElementById("close_icon"); if (closeIcon) { closeIcon.style.display = "inline-block"; closeIcon.style.cursor = "pointer"; }
            const searchIcon = document.getElementById("search_icon"); if (searchIcon) searchIcon.style.display = "none";
        }
    };

    if (typeof jQuery !== 'undefined') {
        jQuery(document).ready(function () {
            jQuery("html").on("contextmenu", function (e) { return false; });
        });
        jQuery(document).keydown(function (event) {
            if (event.keyCode == 123) { return false; }
        });
    }

})();

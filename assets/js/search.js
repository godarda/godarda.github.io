/**
 * GoDarda - Search Functionality (search.js)
 *
 * Purpose:
 * This file implements the client-side search engine for the GoDarda website.
 * It handles lazy loading of search indices, fuzzy matching (Levenshtein),
 * auto-correction, and dynamic result rendering.
 *
 * Key Features:
 * 1. Lazy Loading: Fetches search data (JSON) only when the user interacts with the input.
 * 2. Fuzzy Search: Uses Levenshtein distance for typo tolerance and auto-correction.
 * 3. Real-time Feedback: Provides a progress bar during data fetch and debounced result rendering.
 * 4. Context Awareness: Filters results based on the current page section (e.g., /learn, /tools).
 */

(function () {
document.addEventListener('DOMContentLoaded', function () {
    const containerId = window.gd_path1;
    // --------------------------------------------------------------------------
    // Initial Setup & DOM Caching
    // --------------------------------------------------------------------------
    const container = document.getElementById(containerId);
    if (!container) return;

    // Cache frequently-used DOM nodes
    const matchCountEl = document.getElementById('matchCount');
    const input = document.getElementById('GDSInput');
    if (!input) return;
    const inputContainer = document.getElementById('GDS_input-' + containerId);

    // --------------------------------------------------------------------------
    // Utilities
    // --------------------------------------------------------------------------
    // Utilities (used by loader and renderers)
    function escapeRegExp(s) { return s.replace(/[.*+?^${}()|[\\]\\]/g, '\\$&'); }
    function escapeHtml(unsafe) { return (unsafe || '').replace(/[&<>\"]/g, function (ch) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[ch]; }); }

    // --------------------------------------------------------------------------
    // Data Loading & State
    // --------------------------------------------------------------------------
    // Lazy-loaded items. We avoid parsing JSON blobs until the user actually
    // interacts with the search input to keep initial page load light.
    let items = null; // null = not loaded; [] = loaded but empty. This will hold the search items.
    let loadPromise = null;
    let searchConfig = {}; // To store the config part of the JSON (e.g., category lists).

    function loadItemsIfNeeded() {
        if (items !== null) return Promise.resolve();
        if (loadPromise) return loadPromise;

        if (inputContainer) {
            inputContainer.classList.add('search-loading');
            inputContainer.style.setProperty('--search-progress', '0%');
        }

        let realProgress = 0;
        let isFetching = true;
        let dataResult = [];
        const animationDuration = 1000;
        const startTime = performance.now();

        const dataScript = document.getElementById('search-data-' + containerId);
        if (dataScript) {
            try {
                const data = JSON.parse(dataScript.textContent || dataScript.innerText || '[]');
                items = processItems(data);
                if (inputContainer) inputContainer.classList.remove('search-loading', 'indeterminate');
                return Promise.resolve();
            } catch (e) {
                items = [];
                if (inputContainer) inputContainer.classList.remove('search-loading', 'indeterminate');
                return Promise.resolve();
            }
        }

        // If no embedded script is found, fetch the global search.json and filter if necessary
        const fetchP = fetch(window.gd_search_url || '/search.json')
            .then(response => {
                const contentLength = response.headers.get('content-length');
                const total = parseInt(contentLength, 10);
                if (!contentLength || isNaN(total)) {
                    realProgress = 100;
                    return response.json();
                }
                let loaded = 0;
                const reader = response.body.getReader();
                const stream = new ReadableStream({
                    start(controller) {
                        function push() {
                            reader.read().then(({ done, value }) => {
                                if (done) { controller.close(); return; }
                                loaded += value.byteLength;
                                realProgress = (loaded / total) * 100;
                                controller.enqueue(value);
                                push();
                            });
                        }
                        push();
                    }
                });
                return new Response(stream).json();
            })
            .then(data => {
                dataResult = data.items || []; // Search items are in the 'items' property.
                searchConfig = data.config || {}; // Configuration is in the 'config' property.
                realProgress = 100;
                isFetching = false;
            })
            .catch(e => {
                console.error("Search data load failed", e);
                dataResult = [];
                realProgress = 100;
                isFetching = false;
            });

        const animationP = new Promise(resolve => {
            function frame(time) {
                const elapsed = time - startTime;
                const virtualProgress = Math.min((elapsed / animationDuration) * 100, 100);
                const display = Math.min(realProgress, virtualProgress);

                if (inputContainer) {
                    inputContainer.style.setProperty('--search-progress', display + '%');
                }

                if (elapsed < animationDuration || isFetching) {
                    requestAnimationFrame(frame);
                } else {
                    if (inputContainer) inputContainer.style.setProperty('--search-progress', '100%');
                    setTimeout(resolve, 250);
                }
            }
            requestAnimationFrame(frame);
        });

        loadPromise = Promise.all([fetchP, animationP])
            .then(() => {
                const allItems = processItems(dataResult); // dataResult is now just the array of items.
                if (containerId === 'search') {
                    items = allItems;
                } else if (searchConfig[containerId]) {
                    // This is for /learn and /tools pages. Filter using the config from search.json.
                    const categorySet = new Set(searchConfig[containerId]);
                    items = allItems.filter(it => categorySet.has(it.category));
                } else {
                    // Filter items that belong to the current segment (e.g., "java" or "java/...")
                    items = allItems.filter(it => it.category === containerId);
                }
            })
            .finally(() => {
                loadPromise = null;
                if (inputContainer) {
                    inputContainer.classList.remove('search-loading');
                }
            });
        return loadPromise;
    }

    // --------------------------------------------------------------------------
    // Fuzzy Search & Auto-Correction
    // --------------------------------------------------------------------------
    let vocabulary = new Set();

    function levenshtein(a, b) {
        const alen = a.length;
        const blen = b.length;
        if (alen === 0) return blen;
        if (blen === 0) return alen;

        if (alen > blen) return levenshtein(b, a);

        const row = new Array(alen + 1);
        for (let i = 0; i <= alen; i++) row[i] = i;

        for (let i = 1; i <= blen; i++) {
            let prev = i;
            for (let j = 1; j <= alen; j++) {
                const val = (b.charAt(i - 1) === a.charAt(j - 1)) ? row[j - 1] : Math.min(row[j - 1], prev, row[j]) + 1;
                row[j - 1] = prev;
                prev = val;
            }
            row[alen] = prev;
        }
        return row[alen];
    }

    function findCorrection(word) {
        if (vocabulary.has(word)) return null;

        // Heuristic: Don't correct short words aggressively.
        const maxDist = (word.length <= 4) ? 1 : 2;

        let bestWord = null;
        let minDistance = maxDist + 1;
        for (const vocabWord of vocabulary) {
            if (Math.abs(vocabWord.length - word.length) > maxDist) continue;
            const dist = levenshtein(word, vocabWord);
            if (dist < minDistance) {
                minDistance = dist;
                bestWord = vocabWord;
            }
        }
        return bestWord;
    }

    // --------------------------------------------------------------------------
    // Data Processing & Scoring
    // --------------------------------------------------------------------------
    function processItems(data) {
        vocabulary.clear();
        const seen = new Map();
        const processed = [];

        data.forEach(o => {
            const href = o.href || '#';
            const lowerTitle = (o.title || '').toLowerCase();
            const lowerContent = (o.content || '').toLowerCase();

            if (seen.has(href)) {
                const existing = seen.get(href);
                if (!existing.lowerContent && lowerContent) {
                    existing.lowerContent = lowerContent;
                }
                return;
            }

            const tokens = lowerTitle.split(/[^a-z0-9]+/);
            tokens.forEach(t => { if (t.length > 2) vocabulary.add(t); });

            if (lowerContent) {
                const contentTokens = lowerContent.split(/[^a-z0-9]+/);
                contentTokens.forEach(t => { if (t.length > 2) vocabulary.add(t); });
            }

            let matchTitle = lowerTitle;
            if (lowerTitle.indexOf("'") > -1) {
                const lowerNoApos = lowerTitle.replace(/'/g, '');
                matchTitle += ' ' + lowerNoApos;
                const tokensNoApos = lowerNoApos.split(/[^a-z0-9]+/);
                tokensNoApos.forEach(t => { if (t.length > 2) vocabulary.add(t); });
            }

            const item = {
                title: (o.title || '').trim(),
                href: href,
                category: o.category,
                safeTitle: escapeHtml(o.title || ''),
                lowerTitle: matchTitle,
                lowerContent: lowerContent
            };
            seen.set(href, item);
            processed.push(item);
        });

        // Dynamic Vocabulary: Add words from the current page content using the DOM API.
        // This acts as a dynamic whitelist for common words present in the UI/content.
        try {
            const pageText = (document.body.innerText || '').slice(0, 100000).toLowerCase();
            const pageTokens = pageText.split(/[^a-z0-9]+/);
            pageTokens.forEach(t => { if (t.length > 2) vocabulary.add(t); });
        } catch (e) { /* ignore */ }

        return processed;
    }

    // Scoring helper (operates on precomputed lowerTitle)
    function scoreFor(item, qtrim, tokens) {
        const lowerTitle = item.lowerTitle;
        const lowerContent = item.lowerContent || '';

        if (lowerTitle === qtrim) return { score: 100, type: 'exact' };
        if (qtrim && lowerTitle.startsWith(qtrim)) return { score: 90, type: 'prefix' };
        if (qtrim.length > 1 && lowerTitle.indexOf(qtrim) !== -1) return { score: 80, type: 'substring' };
        if (tokens.length > 0 && tokens.every(t => lowerTitle.indexOf(t) !== -1)) return { score: 70 + tokens.length, type: 'alltokens' };

        // Content matches
        if (lowerContent.indexOf(qtrim) !== -1) return { score: 60, type: 'content' };
        if (tokens.length > 0 && tokens.every(t => lowerContent.indexOf(t) !== -1)) return { score: 50 + tokens.length, type: 'content_all' };

        const matches = tokens.reduce((c, t) => c + (lowerTitle.indexOf(t) !== -1 ? 1 : 0), 0);
        if (matches > 0) return { score: 40 + matches, type: 'anytokens' };
        return { score: 0, type: null };
    }

    // --------------------------------------------------------------------------
    // Result Rendering
    // --------------------------------------------------------------------------
    // Highlighting: use pre-escaped safeTitle to avoid re-escaping repeatedly.
    function buildHighlighted(item, qtrim, tokens, type) {
        const safe = item.safeTitle;
        if (!qtrim) return safe;

        function getPattern(t) {
            if (/^[a-zA-Z0-9]+$/.test(t)) {
                return t.split('').map(c => escapeRegExp(c) + "[']?").join('');
            }
            return escapeRegExp(t);
        }

        try {
            if (type === 'exact' || type === 'prefix' || type === 'substring') {
                const re = new RegExp('(' + getPattern(qtrim) + ')', 'ig');
                return safe.replace(re, '<mark>$1</mark>');
            }
            const uniq = Array.from(new Set(tokens)).sort((a, b) => b.length - a.length);
            let out = safe;
            uniq.forEach(token => {
                if (!token) return;
                const re = new RegExp('(' + getPattern(token) + ')', 'ig');
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
        loadItemsIfNeeded().then(() => {
        const tokens = qtrim.split(/\s+/).filter(Boolean);

        // Fast path: map with precomputed lowerTitle
        const scoredAll = items.map(it => {
            const s = scoreFor(it, qtrim, tokens);
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
        });
    }

    // --------------------------------------------------------------------------
    // Event Listeners
    // --------------------------------------------------------------------------
    // Attach a debounced input handler to the search input (id="GDSInput").
    // We debounce to avoid running expensive work on every keystroke.
    let tid = null;
    input.addEventListener('input', function (e) {
        clearTimeout(tid);

        // Autocorrect logic: triggers when the last character typed is a space
        const cursor = input.selectionStart;
        if (items !== null && cursor > 0 && input.value[cursor - 1] === ' ') {
            const val = input.value;
            const textBefore = val.slice(0, cursor - 1);
            const match = textBefore.match(/([a-zA-Z0-9]+)$/);
            if (match) {
                const word = match[1];
                const lowerWord = word.toLowerCase();
                if (word.length > 2 && !vocabulary.has(lowerWord)) {
                    const correction = findCorrection(lowerWord);
                    if (correction) {
                        const before = val.slice(0, match.index);
                        const after = val.slice(cursor);
                        input.value = before + correction + ' ' + after;
                        const newCursor = before.length + correction.length + 1;
                        input.setSelectionRange(newCursor, newCursor);
                    }
                }
            }
        }

        const v = input.value || '';
        // Toggle icons immediately for UX via the shared helper
        if (typeof window.display_results === 'function') window.display_results();

        if (v.length === 0) {
            renderMatches('');
            return;
        }
        // 150ms debounce gives a balance of responsiveness and work reduction
        tid = setTimeout(() => renderMatches(v), 150);
    });

    // Prefetch on focus
    input.addEventListener('focus', function() {
        loadItemsIfNeeded();
    });

});

// --------------------------------------------------------------------------
// Global Helper Functions
// --------------------------------------------------------------------------
// Clear the search input and hide any visible results or icons.
window.clear_input = function () {
    const inputEl = document.getElementById("GDSInput");
    if (inputEl) inputEl.value = "";
    if (typeof window.display_results === 'function') window.display_results();
};

// Update UI controls based on whether the input contains text. This is a
// small helper used by the onkeypress/onkeyup attributes on the input field.
window.display_results = function () {
    const input = document.getElementById("GDSInput");
    const val = input ? input.value : "";
    const searchEl = document.getElementById("search");
    const closeIcon = document.getElementById("close_icon");
    const searchIcon = document.getElementById("search_icon");
    const matchCount = document.getElementById('matchCount');
    const gdPathEl = window.gd_path1 ? document.getElementById(window.gd_path1) : null;

    if (val.length === 0) {
        if (closeIcon) closeIcon.style.display = "none";
        if (searchIcon) searchIcon.style.display = "inline-block";
        if (gdPathEl) gdPathEl.style.display = "none";
        if (searchEl) searchEl.style.display = "none";
        if (matchCount) matchCount.style.display = 'none';
    } else {
        if (searchEl) searchEl.style.display = "block";
        if (closeIcon) { closeIcon.style.display = "inline-block"; closeIcon.style.cursor = "pointer"; }
        if (searchIcon) searchIcon.style.display = "none";
    }
};

// --------------------------------------------------------------------------
// jQuery-specific Security
// --------------------------------------------------------------------------
if (typeof jQuery !== 'undefined') {
    jQuery(document).ready(function () {
        jQuery("html").on("contextmenu", function (e) { return false; });
    });
    jQuery(document).keydown(function (event) {
        if (event.keyCode == 123) { return false; }
    });
}

})();

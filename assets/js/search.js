/**
 * GoDarda - Search Functionality (search.js)
 *
 * @file This script implements the client-side search engine for the GoDarda website.
 * @summary It handles lazy loading of search data, fuzzy matching, auto-correction,
 * and dynamic result rendering in a performant and context-aware manner.
 *
 * Key Features:
 * 1. Lazy Loading: Fetches search data (JSON) only on user interaction to minimize initial page load.
 * 2. Fuzzy Search: Employs Levenshtein distance for typo tolerance and suggests corrections.
 * 3. Real-time Feedback: Provides a progress bar during data fetch and debounced result rendering.
 * 4. Context-Aware Filtering: Narrows down search results based on the current site section (e.g., /learn, /tools).
 * 5. Performant Rendering: Uses string concatenation and requestAnimationFrame for efficient result display.
 */

// Encapsulate the script in an IIFE (Immediately Invoked Function Expression)
// to prevent polluting the global scope and avoid variable collisions.
(() => {
    // Use the native DOMContentLoaded event to ensure the DOM is ready and to guarantee
    // that this script runs correctly even if jQuery is loaded with `defer`.
    document.addEventListener('DOMContentLoaded', () => {
        // Safely acquire the jQuery object. If it's not available, exit gracefully.
        const $ = window.jQuery;
        if (!$) return;

        // Determine the current search context (e.g., 'learn', 'tools') from a global variable
        // set by the Jekyll template. Defaults to 'search' for the main search page.
        const containerId = window.gd_path1 || 'search';

        // --------------------------------------------------------------------------
        // SECTION: Initial Setup & DOM Caching
        // --------------------------------------------------------------------------
        // Cache jQuery objects for DOM elements that are frequently accessed. This avoids
        // repeated, costly DOM queries and improves performance, especially in event handlers.
        const $container = $('#' + containerId);
        if (!$container.length) return; // Exit if the main results container is not found.

        const $matchCount = $('#matchCount');
        const $input = $('#GDSInput');
        if (!$input.length) return; // Exit if the search input is not found.

        const $inputContainer = $('#GDS_input-' + containerId);
        const $closeIcon = $('#close_icon');
        // Fallback to the generic 'search' container if a context-specific one isn't present.
        const $resultsContainer = $container;
        const $hintsParentContainer = $('#hints-container');

        // Hide keyboard on scroll of results (GoDarda App specific)
        $resultsContainer.on('scroll', () => {
            if (window.isGoDardaApp && document.activeElement) {
                document.activeElement.blur();
            }
        });

        // --------------------------------------------------------------------------
        // SECTION: Sticky Search Bar
        // --------------------------------------------------------------------------
        const $navbar = $('.navbar');

        // Create a placeholder element to occupy the space of the search input when it becomes fixed.
        // This prevents layout shifts in the navbar/header when the input is taken out of the document flow.
        const $stickyPlaceholder = $('<div>').attr('id', 'search-placeholder').hide();
        $inputContainer.before($stickyPlaceholder);

        const $backdrop = $('#search-backdrop');
        $backdrop.on('click', () => window.clear_input());

        /**
         * Updates the position and visual state of the search container.
         *
         * This function handles the transition of the search bar from its natural flow position
         * to a fixed "overlay" position when a search is active.
         *
         * Key behaviors:
         * 1. Activates the placeholder to maintain layout stability.
         * 2. Calculates the exact screen coordinates to position the fixed search bar.
         * 3. Adjusts z-indices to ensure the search UI sits above the backdrop (1050).
         * 4. Dynamically sizes the results container to fit within the viewport (90% height).
         */
        const updateSearchPosition = () => {
            const isSearchActive = $input.val().length > 0;
            if (isSearchActive) {
                // Calculate top offset based on navbar height to position just below it.
                const navHeight = ($navbar.outerHeight() || 0) + 10;
                $stickyPlaceholder.css({ height: $inputContainer.outerHeight(true) }).show();

                const rect = $stickyPlaceholder[0].getBoundingClientRect();
                const targetWidth = rect.width;
                const targetLeft = rect.left;
                const topPos = navHeight;

                // Promote input container to fixed position.
                $inputContainer.css({
                    'position': 'fixed',
                    'width': targetWidth,
                    'top': topPos + 'px',
                    'left': targetLeft + 'px',
                    'z-index': '1050'
                });

                const inputHeight = $inputContainer.outerHeight();
                let nextTop = topPos + inputHeight + 5;

                // Position hints container if visible.
                if ($hintsParentContainer.is(':visible')) {
                    $hintsParentContainer.css({
                        'position': 'fixed',
                        'width': targetWidth,
                        'top': nextTop + 'px',
                        'left': targetLeft + 'px',
                        'z-index': '1050'
                    });
                    nextTop += $hintsParentContainer.outerHeight() + 5;
                } else {
                    $hintsParentContainer.css({ 'position': '', 'width': '', 'top': '', 'left': '', 'z-index': '' });
                }

                // Position match count indicator if visible.
                if ($matchCount.is(':visible')) {
                    $matchCount.css({
                        'position': 'fixed',
                        'width': targetWidth,
                        'top': nextTop + 'px',
                        'left': targetLeft + 'px',
                        'z-index': '1050'
                    });
                    nextTop += $matchCount.outerHeight() + 15;
                } else {
                    $matchCount.css({ 'position': '', 'width': '', 'top': '', 'left': '', 'z-index': '' });
                }

                // Position and size the results container.
                const maxHeight = ($(window).height() * 0.90) - nextTop;
                $resultsContainer.css({
                    'position': 'fixed',
                    'width': targetWidth,
                    'top': nextTop + 'px',
                    'left': targetLeft + 'px',
                    'max-height': maxHeight + 'px',
                    'overflow-y': 'auto',
                    'z-index': '1050'
                });
            } else {
                // Reset all elements to their default static positioning.
                $stickyPlaceholder.hide();
                $inputContainer.css({ 'position': '', 'width': '', 'top': '', 'left': '', 'z-index': '' });
                $hintsParentContainer.css({ 'position': '', 'width': '', 'top': '', 'left': '', 'z-index': '' });
                $matchCount.css({ 'position': '', 'width': '', 'top': '', 'left': '', 'z-index': '' });
                $resultsContainer.css({ 'position': '', 'width': '', 'top': '', 'left': '', 'max-height': '', 'overflow-y': '', 'z-index': '' });
            }
        };

        // Update position on resize to handle orientation changes or window resizing.
        $(window).on('resize', () => {
            if ($input.val().length > 0) window.requestAnimationFrame(updateSearchPosition);
        });
        // Ensure position is correct once all page resources (images, fonts) are loaded.
        $(window).on('load', updateSearchPosition);

        // --------------------------------------------------------------------------
        // SECTION: Utilities
        // --------------------------------------------------------------------------
        /**
         * Escapes special characters in a string for use in a regular expression.
         * @param {string} s - The string to escape.
         * @returns {string} The escaped string.
         */
        const escapeRegExp = (s) => s.replace(/[.*+?^${}()|[\\]\\]/g, '\\$&');

        /**
         * Escapes HTML special characters to prevent XSS vulnerabilities when rendering content.
         * @param {string} unsafe - The potentially unsafe string.
         * @returns {string} The HTML-escaped string.
         */
        const escapeHtml = (unsafe) => (unsafe || '').replace(/[&<>\"]/g, (ch) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[ch]));

        // --------------------------------------------------------------------------
        // SECTION: Data Loading & State Management
        // --------------------------------------------------------------------------
        // State variables for managing the search data lifecycle.
        let items = null;       // Holds the processed search items. `null` means not loaded.
        let loadPromise = null; // Prevents multiple concurrent fetch requests.
        let searchConfig = {};  // Stores configuration from search.json (e.g., category lists).

        /**
         * Lazily loads and processes the search data from an embedded script or a remote JSON file.
         * This function is idempotent; it only fetches data once.
         * @returns {Promise<void>} A promise that resolves when the data is loaded and processed.
         */
        const loadItemsIfNeeded = () => {
            // If items are already loaded or a load is in progress, return the existing promise.
            if (items !== null) return Promise.resolve();
            if (loadPromise) return loadPromise;

            // Show a loading indicator and progress bar on the input field.
            if ($inputContainer.length) {
                $inputContainer.addClass('search-loading');
                $inputContainer.css('--search-progress', '0%');
            }

            // Variables for managing the fetch and animation progress.
            let realProgress = 0;
            let isFetching = true;
            let dataResult = [];
            const animationDuration = 1000;
            const startTime = performance.now();

            // First, try to load data from an embedded <script> tag. This is an optimization
            // for category-specific pages to avoid a separate network request.
            const $dataScript = $('#search-data-' + containerId);
            if ($dataScript.length) {
                try {
                    const data = JSON.parse($dataScript.text() || '[]');
                    items = processItems(data);
                    $inputContainer.removeClass('search-loading indeterminate');
                    return Promise.resolve();
                } catch (e) {
                    console.error("Failed to parse embedded search data.", e);
                    items = [];
                    // Set to empty on failure to prevent retries.
                    $inputContainer.removeClass('search-loading indeterminate');
                    return Promise.resolve();
                }
            }

            // If no embedded data, fetch the global search.json file.
            // This promise handles the network request and progress tracking.
            const fetchP = fetch(window.gd_search_url || '/search.json')
                .then(response => {
                    const contentLength = response.headers.get('content-length');
                    const total = parseInt(contentLength, 10);

                    // If content length is unknown, we can't show determinate progress.
                    if (!contentLength || isNaN(total)) {
                        realProgress = 100; // Assume it will finish quickly.
                        return response.json();
                    }

                    // Use a ReadableStream to track download progress.
                    let loaded = 0;
                    const reader = response.body.getReader();
                    const stream = new ReadableStream({
                        start(controller) {
                            const push = () => {
                                reader.read().then(({ done, value }) => {
                                    if (done) { controller.close(); return; }
                                    loaded += value.byteLength;
                                    realProgress = (loaded / total) * 100;
                                    controller.enqueue(value);
                                    push();
                                });
                            };
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
                const frame = (time) => {
                    const elapsed = time - startTime;
                    const virtualProgress = Math.min((elapsed / animationDuration) * 100, 100);
                    const display = Math.min(realProgress, virtualProgress);

                    if ($inputContainer.length) {
                        $inputContainer.css('--search-progress', display + '%');
                    }

                    if (elapsed < animationDuration || isFetching) {
                        requestAnimationFrame(frame);
                    } else {
                        $inputContainer.css('--search-progress', '100%');
                        setTimeout(resolve, 250);
                    }
                };
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
                    if ($inputContainer.length) {
                        $inputContainer.removeClass('search-loading');
                    }
                });
            return loadPromise;
        };

        // --------------------------------------------------------------------------
        // SECTION: Fuzzy Search & Auto-Correction
        // --------------------------------------------------------------------------
        // A vocabulary of all known words from search data and page content.
        // Used for efficient auto-correction.
        let vocabulary = new Set();

        /**
         * Calculates the Levenshtein distance between two strings.
         * This is a measure of the difference between two sequences.
         * @param {string} a - The first string.
         * @param {string} b - The second string.
         * @returns {number} The Levenshtein distance.
         */
        const levenshtein = (a, b) => {
            // Standard, optimized Levenshtein implementation.
            const alen = a.length;
            const blen = b.length;
            if (alen === 0) return blen;
            if (blen === 0) return alen;

            if (alen > blen) return levenshtein(b, a); // Ensure a is the shorter string.

            const row = new Array(alen + 1);
            for (let i = 0; i <= alen; i++) {
                row[i] = i;
            }

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
        };

        /**
         * Finds the closest matching word from the vocabulary for a given misspelled word.
         * @param {string} word - The word to correct.
         * @returns {string|null} The corrected word, or null if no good match is found.
         */
        const findCorrection = (word) => {
            if (vocabulary.has(word)) return null;

            // Heuristic: Allow more typos for longer words.
            const maxDist = (word.length <= 4) ? 1 : 2;

            let bestWord = null;
            let minDistance = maxDist + 1;
            for (const vocabWord of vocabulary) {
                // Optimization: skip words with a large length difference.
                if (Math.abs(vocabWord.length - word.length) > maxDist) continue;
                const dist = levenshtein(word, vocabWord);
                if (dist < minDistance) {
                    minDistance = dist;
                    bestWord = vocabWord;
                }
            }
            return bestWord;
        };

        // --------------------------------------------------------------------------
        // SECTION: Data Processing & Scoring
        // --------------------------------------------------------------------------
        /**
         * Processes the raw search data array into a structured, optimized format.
         * This includes de-duplication, building the vocabulary, and pre-calculating values.
         * @param {Array<Object>} data - The raw array of search items from JSON.
         * @returns {Array<Object>} The processed array of search items.
         */
        const processItems = (data) => {
            vocabulary.clear();
            const seen = new Map(); // Used to de-duplicate items by their href.
            const processed = [];

            data.forEach(o => {
                const href = o.href || '#';
                const lowerTitle = (o.title || '').toLowerCase();
                const lowerContent = (o.content || '').toLowerCase();

                // If we've already seen this link, merge content if necessary but don't add a new entry.
                if (seen.has(href)) {
                    const existing = seen.get(href);
                    if (!existing.lowerContent && lowerContent) {
                        existing.lowerContent = lowerContent;
                    }
                    return;
                }

                // Add all words from the title and content to the vocabulary.
                const tokens = lowerTitle.split(/[^a-z0-9]+/);
                tokens.forEach(t => { if (t.length > 2) vocabulary.add(t); });

                if (lowerContent) {
                    const contentTokens = lowerContent.split(/[^a-z0-9]+/);
                    contentTokens.forEach(t => { if (t.length > 2) vocabulary.add(t); });
                }

                // Handle apostrophes by creating a version of the title without them for matching.
                let matchTitle = lowerTitle;
                if (lowerTitle.indexOf("'") > -1) {
                    const lowerNoApos = lowerTitle.replace(/'/g, '');
                    matchTitle += ' ' + lowerNoApos;
                    const tokensNoApos = lowerNoApos.split(/[^a-z0-9]+/);
                    tokensNoApos.forEach(t => { if (t.length > 2) vocabulary.add(t); });
                }

                // Create the final processed item object.
                const item = {
                    title: (o.title || '').trim(),
                    href: href,
                    category: o.category,
                    safeTitle: escapeHtml(o.title || ''), // Pre-escaped for safe rendering.
                    lowerTitle: matchTitle,
                    lowerContent: lowerContent
                };
                seen.set(href, item);
                processed.push(item);
            });

            // Dynamic Vocabulary Enhancement: Add words from the current page's visible text.
            // This helps auto-correction recognize context-specific terms not in the search index.
            try {
                const pageText = ($('body').text() || '').slice(0, 100000).toLowerCase();
                const pageTokens = pageText.split(/[^a-z0-9]+/);
                pageTokens.forEach(t => { if (t.length > 2) vocabulary.add(t); });
            } catch (e) { /* Ignore errors, this is a non-critical enhancement */ }

            return processed;
        };

        /**
         * Calculates a relevance score for a search item against a query.
         * @param {Object} item - The search item to score.
         * @param {string} qtrim - The trimmed, lowercased search query.
         * @param {Array<string>} tokens - The query split into words.
         * @returns {{score: number, type: string|null}} The score and match type.
         */
        const scoreFor = (item, qtrim, tokens) => {
            const lowerTitle = item.lowerTitle;
            const lowerContent = item.lowerContent || '';

            // Score is tiered based on match quality. Higher is better.
            if (lowerTitle === qtrim) return { score: 100, type: 'exact' };
            if (qtrim && lowerTitle.startsWith(qtrim)) return { score: 90, type: 'prefix' };
            if (qtrim.length > 1 && lowerTitle.indexOf(qtrim) !== -1) return { score: 80, type: 'substring' };
            if (tokens.length > 0 && tokens.every(t => lowerTitle.indexOf(t) !== -1)) return { score: 70 + tokens.length, type: 'alltokens' };

            // Content matches are scored lower than title matches.
            if (lowerContent.indexOf(qtrim) !== -1) return { score: 60, type: 'content' };
            if (tokens.length > 0 && tokens.every(t => lowerContent.indexOf(t) !== -1)) return { score: 50 + tokens.length, type: 'content_all' };

            // Partial token matches are the lowest score.
            const matches = tokens.reduce((c, t) => c + (lowerTitle.indexOf(t) !== -1 ? 1 : 0), 0);
            if (matches > 0) return { score: 40 + matches, type: 'anytokens' };

            return { score: 0, type: null }; // No match.
        };

        // --------------------------------------------------------------------------
        // SECTION: Result Rendering
        // --------------------------------------------------------------------------
        /**
         * Generates an HTML string with search terms highlighted using <mark> tags.
         * @param {Object} item - The search item, containing a `safeTitle`.
         * @param {string} qtrim - The trimmed, lowercased search query.
         * @param {Array<string>} tokens - The query split into words.
         * @param {string} type - The type of match, used to guide highlighting strategy.
         * @returns {string} The HTML string for the highlighted title.
         */
        const buildHighlighted = (item, qtrim, tokens, type) => {
            const safe = item.safeTitle;
            if (!qtrim) return safe;

            // Creates a regex pattern that can handle optional apostrophes between letters.
            const getPattern = (t) => {
                if (/^[a-zA-Z0-9]+$/.test(t)) {
                    return t.split('').map(c => escapeRegExp(c) + "[']?").join('');
                }
                return escapeRegExp(t);
            };

            try {
                // For simple matches, a single regex replace is fast and effective.
                if (type === 'exact' || type === 'prefix' || type === 'substring') {
                    const re = new RegExp('(' + getPattern(qtrim) + ')', 'ig');
                    return safe.replace(re, '<mark>$1</mark>');
                }
                // For token-based matches, highlight each token.
                const uniq = Array.from(new Set(tokens)).sort((a, b) => b.length - a.length);
                let out = safe;
                uniq.forEach(token => {
                    if (!token) return;
                    const re = new RegExp('(' + getPattern(token) + ')', 'ig');
                    out = out.replace(re, '<mark>$1</mark>');
                });
                return out;
            } catch (err) {
                // Fallback for complex regex or edge cases: manual range-based highlighting.
                // This is slower but more robust.
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

                // Merge overlapping highlight ranges to avoid nested <mark> tags.
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

                // Build the final HTML string from the merged ranges.
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
        };

        /**
         * Renders the top search matches into the DOM.
         * @param {string} q - The raw search query from the input field.
         */
        const renderMatches = (q) => {
            const qtrim = (q || '').trim().toLowerCase();
            if (qtrim.length === 0) {
                $container.hide();
                $matchCount.hide();
                return;
            }

            // Ensure data is loaded before attempting to render results.
            loadItemsIfNeeded().then(() => {
                const tokens = qtrim.split(/\s+/).filter(Boolean);

                // Score all items, filter out non-matches, and sort by score.
                const scoredAll = items.map(it => {
                    const s = scoreFor(it, qtrim, tokens);
                    return Object.assign({}, it, s);
                }).filter(r => r.score > 0)
                    .sort((a, b) => (b.score - a.score) || a.title.localeCompare(b.title));

                const totalMatches = scoredAll.length;
                const displayed = scoredAll.slice(0, 25); // Limit to top 25 results.

                // Performance: Build a single HTML string instead of creating DOM nodes in a loop.
                const html = displayed.map(r => {
                    return `<a class="codecard card" href="${r.href}" data-category="${r.category}" style="display:block; margin-bottom:6px;">${buildHighlighted(r, qtrim, tokens, r.type)}</a>`;
                }).join('');

                // Batch the DOM update using requestAnimationFrame for smoother rendering.
                window.requestAnimationFrame(() => {
                    if (totalMatches > 0) {
                        $container.html(html).show();

                        // Event delegation: attach a single click handler to the container.
                        // This is more efficient than attaching one to each result link.
                        $container.find('a').on('click', window.clear_input);

                        // Update the match count display.
                        if ($matchCount.length) {
                            $matchCount.text(Math.min(25, totalMatches) + ' of ' + totalMatches + (totalMatches === 1 ? ' result' : ' results'));
                            $matchCount[0].style.color = '';
                            $matchCount.show();
                        }
                    } else {
                        $container.hide();
                        if ($matchCount.length) {
                            $matchCount.text('No results found');
                            $matchCount[0].style.setProperty('color', '#e63636', 'important');
                            $matchCount.show();
                        }
                    }
                    updateSearchPosition();
                });
            });
        };

        // --------------------------------------------------------------------------
        // SECTION: Event Listeners
        // --------------------------------------------------------------------------
        let tid = null; // Timer ID for debouncing.
        $input.on('input', function(e) {
            clearTimeout(tid);

            // Auto-correction logic: triggers when the user types a space.
            const cursor = this.selectionStart;
            if (items !== null && cursor > 0 && this.value[cursor - 1] === ' ') {
                const val = this.value;
                const textBefore = val.slice(0, cursor - 1);
                const match = textBefore.match(/([a-zA-Z0-9]+)$/); // Find the last word.
                if (match) {
                    const word = match[1];
                    const lowerWord = word.toLowerCase();
                    // Check if the word is short and not in our vocabulary.
                    if (word.length > 2 && !vocabulary.has(lowerWord)) {
                        const correction = findCorrection(lowerWord);
                        if (correction) {
                            // Replace the misspelled word and restore cursor position.
                            const before = val.slice(0, match.index);
                            const after = val.slice(cursor);
                            this.value = before + correction + ' ' + after;
                            const newCursor = before.length + correction.length + 1;
                            this.setSelectionRange(newCursor, newCursor);
                        }
                    }
                }
            }

            const v = $(this).val() || '';
            // Update UI icons immediately for a responsive feel.
            if (typeof window.display_results === 'function') window.display_results();

            if (v.length === 0) {
                renderMatches(''); // Clear results immediately if input is empty.
                return;
            }
            // Debounce the expensive renderMatches call to avoid running it on every keystroke.
            tid = setTimeout(() => renderMatches(v), 150);
        });

        // Pre-fetch search data when the user focuses on the input, anticipating a search.
        $input.on('focus', () => {
            loadItemsIfNeeded();
        });

        // --------------------------------------------------------------------------
        // SECTION: Search Suggestions & Voice Input
        // --------------------------------------------------------------------------
        const $micIcon = $('#mic_icon');
        const $hintsContainer = $('#search-hints');
        const $hintIcon = $('#hint-icon');

        // Voice Search Logic
        if ($micIcon.length) {
            const $micIconI = $micIcon.find('i');
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            let recognition;
            let isListening = false;

            if (SpeechRecognition) {
                recognition = new SpeechRecognition();
                recognition.continuous = false;
                recognition.lang = 'en-US';
                recognition.interimResults = false;
                recognition.maxAlternatives = 1;

                $micIcon.on('click', () => {
                    if (isListening) {
                        recognition.stop();
                        return;
                    }
                    try {
                        recognition.start();
                    } catch (e) {
                        console.error("Speech recognition could not be started:", e);
                    }
                });

                recognition.onstart = () => {
                    isListening = true;
                    $micIconI.removeClass('bi-mic').addClass('bi-mic-fill text-danger');
                };

                recognition.onresult = (event) => {
                    const transcript = event.results[0][0].transcript;
                    $input.val(transcript);
                    $input.trigger('input');
                };

                recognition.onerror = (event) => {
                    console.error('Speech recognition error:', event.error);
                };

                recognition.onend = () => {
                    isListening = false;
                    $micIconI.removeClass('bi-mic-fill text-danger').addClass('bi-mic');
                };
            } else {
                $micIcon.hide();
            }
        }

        // Suggestions UI Effects
        if ($hintIcon.length) {
            const blinkTotal = 3;
            const intervalTime = 2000;
            let blinkCount = 0;
            const intervalId = setInterval(() => {
                if (blinkCount >= blinkTotal) {
                    clearInterval(intervalId);
                    return;
                }
                $hintIcon.removeClass('bi-lightbulb').addClass('bi-lightbulb-fill light-on');
                setTimeout(() => {
                    $hintIcon.removeClass('bi-lightbulb-fill light-on').addClass('bi-lightbulb');
                }, intervalTime / 2);
                blinkCount++;
            }, intervalTime);
        }

        // Suggestions Logic
        const learnHints = [
        '32 Bit', '64 Bit', 'ALP', 'API', 'ASCII',
        'Abstraction', 'Abstract', 'Algorithm', 'Area', 'Array',
        'Assembly', 'AWT', 'Bash', 'Binary', 'BMI',
        'C', 'C#', 'C++', 'CLI', 'Class',
        'Compile', 'Constructor', 'Control', 'CRUD', 'Currency',
        'DataFrame', 'Database', 'Delete', 'Destructor', 'Dictionary',
        'Dynamic', 'Energy', 'Exception', 'Execute', 'Expression',
        'File', 'Framework', 'F#', 'Function', 'Game',
        'Graph', 'HashMap', 'Heap', 'Inheritance', 'Insert',
        'Input', 'Interface', 'Java', 'Join', 'Julia',
        'LISP', 'Library', 'LinkedList', 'Linux', 'List',
        'Log', 'Loop', 'Math', 'Matrix', 'Memory',
        'Method', 'Module', 'MongoDB', 'MySQL', 'Namespace',
        'NumPy', 'Octave', 'OpenGL', 'Output', 'Pandas',
        'Path', 'Pointer', 'Polymorphism', 'Python', 'Queue',
        'Ranorex', 'R', 'Recursion', 'Reflection', 'Retrieve',
        'Rust', 'Search', 'Searching', 'Select', 'Selenium',
        'Set', 'Socket', 'Sort', 'Sorting', 'Stack',
        'Static', 'Stream', 'String', 'TestNG', 'Thread',
        'Tree', 'Tuple', 'Update', 'VBScript', 'WebDriver',
        'XPath'
        ];

        const toolsHints = [
        'Age', 'Area', 'BMI', 'Calculator', 'Converter',
        'Currency', 'Data', 'Energy', 'Hash', 'Length',
        'Number', 'Physics', 'Power', 'Pressure', 'Speed',
        'String', 'Temperature', 'Time', 'Volume'
        ];

        const deactivateHints = () => {
            $hintsContainer.children().removeClass('active');
        };

        const displayHints = (hints, spin = false) => {
            if (!$hintsContainer.length || !$hintsParentContainer.length || hints.length === 0) return;

            const $activeBtn = $hintsContainer.find('a.btn.active');
            const activeText = $activeBtn.length ? $activeBtn.text() : null;
            let pool = hints.slice();

            if (activeText) {
                pool = pool.filter(h => h !== activeText);
            }

            for (let i = pool.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [pool[i], pool[j]] = [pool[j], pool[i]];
            }

            let selected = pool.slice(0, 3);
            if (activeText) {
                const activeIndex = Math.max(0, $hintsContainer.children('a.btn').not('#refresh-hints').index($activeBtn));
                selected = pool.slice(0, 2);
                selected.splice(activeIndex, 0, activeText);
            }

            const hintsHtml = selected.map(hint => {
                const sanitizedHint = $('<div>').text(hint).html();
                const activeClass = (hint === activeText) ? ' active' : '';
                return `<a href="javascript:void(0);" class="btn btn-sm btn-outline-secondary rounded-pill${activeClass}" style="margin: 2px; font-size: 12px;">${sanitizedHint}</a>`;
            }).join(' ');

            const spinClass = spin ? 'spin-animation' : '';
            const refreshBtn = `<a href="javascript:void(0);" id="refresh-hints" class="btn btn-sm btn-outline-secondary rounded-pill" style="margin: 2px; font-size: 12px;" title="Refresh hints"><i class="bi bi-arrow-clockwise ${spinClass}"></i></a>`;

            $hintsContainer.html(hintsHtml + refreshBtn);

            if (spin) {
                $hintsContainer.find('#refresh-hints i').one('animationend', function() {
                    $(this).removeClass('spin-animation');
                });
            }

            $hintsParentContainer.show();
        };

        $hintsContainer.on('click', 'a.btn', function(event) {
            if (this.id === 'refresh-hints') return;
            event.preventDefault();
            const text = $(this).text();
            $input.val(text);
            $input.trigger('input');
            $input.trigger('blur');
            deactivateHints();
            $(this).addClass('active');
        });

        $hintsContainer.on('click', '#refresh-hints', function(event) {
            event.preventDefault();
            displayHints(currentAllHints, true);
        });

        $closeIcon.on('click', function() {
            if (typeof window.clear_input === 'function') window.clear_input();
            deactivateHints();
        });

        $input.on('input', function() {
            if (!$(this).val()) deactivateHints();
        });

        let currentAllHints = [];

        const loadHints = () => {
            const currentCategory = window.gd_path1;
            if (currentCategory === 'search') {
                currentAllHints = learnHints.concat(toolsHints);
                displayHints(currentAllHints);
            } else if (currentCategory === 'learn') {
                currentAllHints = learnHints;
                displayHints(currentAllHints);
            } else if (currentCategory === 'tools') {
                currentAllHints = toolsHints;
                displayHints(currentAllHints);
            } else {
                $.getJSON(window.gd_search_url || '/search.json')
                    .then(data => {
                        const keywords = new Set();
                        let itemsToProcess = data.items;
                        if (currentCategory) {
                            const categoryItems = data.items.filter(item => item.category === currentCategory);
                            if (categoryItems.length > 0) itemsToProcess = categoryItems;
                        }
                        itemsToProcess.forEach(item => {
                            const words = item.title.match(/[a-zA-Z0-9+.#-]+/g) || [];
                            words.forEach(word => {
                                const firstChar = word.charAt(0);
                                if (word.length > 2 && word.length <= 15 && isNaN(word) && firstChar >= 'A' && firstChar <= 'Z') {
                                    keywords.add(word);
                                }
                            });
                            const cat = item.category?.charAt(0).toUpperCase() + item.category?.slice(1);
                            if (cat && cat.length > 2 && cat.length <= 15) keywords.add(cat);
                        });
                        currentAllHints = Array.from(keywords);
                        displayHints(currentAllHints);
                    })
                    .catch(error => console.error('Error fetching or processing search.json for suggestions:', error));
            }
        };

        loadHints();

        $(window).on('pageshow', (event) => {
            // If the page is loaded from the bfcache (back/forward cache), reload hints and reset input.
            if (event.originalEvent.persisted) {
                loadHints();
                if (typeof window.clear_input === 'function') window.clear_input();
            }
        });

        // --------------------------------------------------------------------------
        // SECTION: Global Helper Functions & History Management
        // --------------------------------------------------------------------------
        // These functions are exposed globally to allow interaction from inline HTML
        // or other scripts. They also manage the browser history state to support
        // "Back button to close" functionality.

        // Flag to track if a history state has been pushed for the open search overlay.
        let searchHistoryStatePushed = false;

        // Listen for the browser's "Back" action.
        $(window).on('popstate', () => {
            if (searchHistoryStatePushed) {
                searchHistoryStatePushed = false;
                // Close the search overlay without triggering another history.back()
                window.clear_input('popstate');
            }
        });

        /**
         * Clears the search input field, hides results, and resets the UI.
         * @param {string} [mode] - Context flag (e.g., 'popstate') to control history manipulation.
         */
        window.clear_input = (mode) => {
            $input.val("");
            $input.blur();
            window.display_results(mode); // Trigger UI update.
        };

        /**
         * Controls the visibility of the search overlay and results.
         *
         * Logic:
         * - If input is empty: Hides overlay, restores body scroll, and reverts history state if needed.
         * - If input has text: Shows overlay, locks body scroll, and pushes a new history state.
         *
         * @param {string} [mode] - Context flag to determine specific history handling behavior.
         */
        window.display_results = (mode) => {
            const val = $input.val();
            const shouldShow = val.length > 0;

            if (!shouldShow) {
                $closeIcon.hide();
                $resultsContainer.hide();
                $matchCount.hide();
                $backdrop.fadeOut(200);
                $inputContainer.removeClass('search-elevated');
                $resultsContainer.removeClass('search-results-elevated');
                $matchCount.removeClass('search-elevated');
                $hintsParentContainer.removeClass('search-elevated');
                deactivateHints();
                $('body').css('overflow', '');
                updateSearchPosition();

                if (searchHistoryStatePushed) {
                    searchHistoryStatePushed = false;
                    if (mode === 'popstate') {
                        // History navigation already happened (user pressed Back), just update UI.
                    } else if (mode) {
                        // Link click or other skip: replace state to remove the search flag without navigating.
                        history.replaceState(null, '', window.location.href);
                    } else {
                        // Manual close (e.g., close icon): trigger a history back action.
                        history.back();
                    }
                }
            } else {
                // Push a new history state so the Back button closes the search instead of leaving the page.
                if (!searchHistoryStatePushed) {
                    history.pushState({ searchOpen: true }, '', window.location.href);
                    searchHistoryStatePushed = true;
                }

                $resultsContainer.show();
                $closeIcon.css({'display': 'flex', 'align-items': 'center', 'cursor': 'pointer'});
                $backdrop.fadeIn(200);
                $inputContainer.addClass('search-elevated');
                $resultsContainer.addClass('search-results-elevated');
                $matchCount.addClass('search-elevated');
                $hintsParentContainer.addClass('search-elevated');
                $('body').css('overflow', 'hidden');
                updateSearchPosition();
            }
        };

        // On page load, ensure the input is cleared (called after definition)
        if (typeof window.clear_input === 'function') window.clear_input();

        // --------------------------------------------------------------------------
        // SECTION: Security Measures
        // --------------------------------------------------------------------------
        // Basic security to deter casual inspection and content scraping.
        // Disables the right-click context menu.
        $("html").on("contextmenu", () => false);
        // Disables the F12 key to open developer tools.
        $(document).on("keydown", (event) => {
            if (event.key === "F12") return false;
        });
    });

})();

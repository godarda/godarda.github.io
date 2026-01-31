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
        const $searchIcon = $('#search_icon');
        // Fallback to the generic 'search' container if a context-specific one isn't present.
        const $resultsContainer = $container.length ? $container : $('#search');

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
                    return `<a class="codecard card" href="${r.href}" style="display:block; margin-bottom:6px;">${buildHighlighted(r, qtrim, tokens, r.type)}</a>`;
                }).join('');

                // Batch the DOM update using requestAnimationFrame for smoother rendering.
                window.requestAnimationFrame(() => {
                    $container.html(html).show();

                    // Event delegation: attach a single click handler to the container.
                    // This is more efficient than attaching one to each result link.
                    $container.find('a').on('click', window.clear_input);

                    // Update the match count display.
                    if ($matchCount.length) {
                        $matchCount.text('Showing ' + Math.min(25, totalMatches) + ' of ' + totalMatches + (totalMatches === 1 ? ' result' : ' results'));
                        $matchCount.show();
                    }
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
        const $suggestionsContainer = $('#search-suggestions');
        const $suggestionsParentContainer = $('#suggestions-container');
        const $light = $('#suggestion-light');

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
        if ($light.length) {
            const blinkTotal = 3;
            const intervalTime = 2000;
            let blinkCount = 0;
            const intervalId = setInterval(() => {
                if (blinkCount >= blinkTotal) {
                    clearInterval(intervalId);
                    return;
                }
                $light.removeClass('bi-lightbulb').addClass('bi-lightbulb-fill light-on');
                setTimeout(() => {
                    $light.removeClass('bi-lightbulb-fill light-on').addClass('bi-lightbulb');
                }, intervalTime / 2);
                blinkCount++;
            }, intervalTime);
        }

        // Suggestions Logic
        const learnSuggestions = [
            'C', 'C++', 'Java', 'Python', 'R', 'Julia', 'Octave', 'C#', 'F#',
            'Rust', 'LISP', 'Linux', 'MySQL', 'MongoDB', 'Selenium', 'Algorithm', 'Assembly', 'VBScript',
            'Ranorex', 'OpenGL', 'AWT', 'Function', 'Method', 'Class', 'Inheritance',
            'Polymorphism', 'Abstraction', 'Array', 'Bash', 'CLI', 'Exception', 'Database',
            'Stack', 'Queue', 'Tree', 'Graph', 'Sorting', 'Searching', 'Recursion', 'XPath', 'WebDriver', 'TestNG',
            'String', 'DataFrame', 'NumPy', 'Pandas', 'Matplotlib', 'List', 'Set', 'Tuple', 'Dictionary',
            'Expression', 'Log', 'Thread', 'Matrix', 'Math', 'CRUD'
        ];
        const toolsSuggestions = [
            'Calculator', 'Converter', 'Data', 'Length', 'Time', 'Currency', 'Physics', 'Hash', 'Area', 'Volume',
            'Speed', 'Temperature', 'Pressure', 'Power', 'Energy', 'Age', 'BMI'
        ];

        const deactivateSuggestions = () => {
            $suggestionsContainer.children().removeClass('active');
        };

        const displaySuggestions = (suggestions) => {
            if (!$suggestionsContainer.length || !$suggestionsParentContainer.length || suggestions.length === 0) return;
            for (let i = suggestions.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [suggestions[i], suggestions[j]] = [suggestions[j], suggestions[i]];
            }
            const suggestionsHtml = suggestions.slice(0, 3).map(suggestion => {
                const sanitizedSuggestion = $('<div>').text(suggestion).html();
                return `<a href="javascript:void(0);" class="btn btn-sm btn-outline-secondary rounded-pill" style="margin: 2px; font-size: 12px;">${sanitizedSuggestion}</a>`;
            }).join(' ');
            $suggestionsContainer.html(suggestionsHtml);
            $suggestionsParentContainer.show();
        };

        $suggestionsContainer.on('click', 'a.btn', function(event) {
            event.preventDefault();
            const text = $(this).text();
            $input.val(text);
            $input.trigger('input');
            $input.trigger('blur');
            deactivateSuggestions();
            $(this).addClass('active');
        });

        $closeIcon.on('click', function() {
            if (typeof window.clear_input === 'function') window.clear_input();
            deactivateSuggestions();
        });

        $input.on('input', function() {
            if (!$(this).val()) deactivateSuggestions();
        });

        const loadSuggestions = () => {
            const currentCategory = window.gd_path1;
            if (currentCategory === 'search') {
                displaySuggestions(learnSuggestions.concat(toolsSuggestions));
            } else if (currentCategory === 'learn') {
                displaySuggestions(learnSuggestions);
            } else if (currentCategory === 'tools') {
                displaySuggestions(toolsSuggestions);
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
                        displaySuggestions(Array.from(keywords));
                    })
                    .catch(error => console.error('Error fetching or processing search.json for suggestions:', error));
            }
        };

        loadSuggestions();

        $(window).on('pageshow', (event) => {
            if (event.originalEvent.persisted) {
                loadSuggestions();
            }
        });

        // On page load, ensure the input is cleared
        if (typeof window.clear_input === 'function') window.clear_input();

        // --------------------------------------------------------------------------
        // SECTION: Global Helper Functions
        // --------------------------------------------------------------------------
        // These functions are exposed on the `window` object to be callable from
        // other scripts or inline HTML event attributes (like the close icon's onclick).

        /**
         * Clears the search input field and hides the results.
         */
        window.clear_input = () => {
            $input.val("");
            window.display_results(); // Trigger UI update.
        };

        /**
         * Updates the visibility of UI controls (close/search icons, results container)
         * based on whether the input field has text.
         */
        window.display_results = () => {
            const val = $input.val();

            if (val.length === 0) {
                $closeIcon.hide();
                $searchIcon.css('display', '');
                $resultsContainer.hide();
                $matchCount.hide();
            } else {
                $resultsContainer.show();
                $closeIcon.css({'display': '', 'cursor': 'pointer'});
                $searchIcon.hide();
            }
        };

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

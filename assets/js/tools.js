/**
 * GoDarda - Common Tools Logic (tools.js)
 *
 * Purpose:
 * This module provides a reusable foundation for both Calculators and Converters.
 * It unifies the logic for UI initialization, state management, and DOM updates.
 *
 * Modes:
 * 1. Calculator Mode: Uses 'stats' and a custom 'calculate' function.
 * 2. Converter Mode: Uses 'units' to auto-generate stats and conversion logic.
 *
 * Key Features:
 * 1. Dynamic UI Generation: Creates result cards and dropdown menus based on configuration.
 * 2. Flexible Inputs: Supports any number of inputs (numbers, dates, text).
 * 3. State Management: Tracks selected stats and persists defaults.
 * 4. Optimized Rendering: Uses caching and efficient DOM updates.
 */

(() => {
    /**
     * Formats a number for display, handling scientific notation for extreme values
     * and limiting precision for readability.
     * @param {number} num - The number to format.
     * @returns {string} The formatted number string.
     */
    const formatNumber = (num) => {
        if (num === 0) return '0';
        const abs = Math.abs(num);
        if (abs < 1e-4 || abs > 1e6) {
            return num.toExponential(4);
        }
        return parseFloat(num.toPrecision(6)).toString();
    };

    /**
     * Normalizes the converter configuration by converting unit factors to functions
     * and generating the statistics structure.
     * @param {Object} units - The units configuration object.
     * @param {Array<string>} [defaultSelectedUnits] - List of unit keys selected by default.
     * @returns {Object} The normalized stats object.
     */
    const normalizeConverterConfig = (units, defaultSelectedUnits) => {
        // Normalize Units: Convert simple factors to toBase/fromBase functions
        Object.keys(units).forEach(key => {
            const u = units[key];
            if (u.factor !== undefined && !u.toBase) {
                u.toBase = v => v * u.factor;
                u.fromBase = v => v / u.factor;
            }
        });

        // Generate Stats from Units
        const stats = {};
        Object.keys(units).forEach(key => {
            stats[key] = {
                name: `${units[key].name} (${units[key].symbol})`,
                default: defaultSelectedUnits ? defaultSelectedUnits.includes(key) : true
            };
        });
        return stats;
    };

    window.setupTool = (config) => {
        let {
            stats,              // [Calculator] Configuration for output tiles: { key: { name, default } }
            inputs = [],        // [Calculator] Array of input element IDs
            calculate,          // [Calculator] Function to compute results based on inputs
            resultsId = 'resultsContainer',
            dropdownId = 'viewOptionsMenu',
            clearBtnId = 'btnClear',

            // [Converter Mode] Specific Config
            units,
            defaultUnit,
            defaultSelectedUnits,
            converterType = 'numeric',
            inputPlaceholder = 'Enter value...',
            inputType = 'number'
        } = config;

        const isConverter = !!units;
        let inputUnitSelect = null;

        // --------------------------------------------------------------------------
        // Converter Mode Initialization
        // --------------------------------------------------------------------------
        if (isConverter) {
            // Normalize units and generate stats structure
            stats = normalizeConverterConfig(units, defaultSelectedUnits);

            // Configure inputs for converter mode
            inputs = ['inputValue'];

            // Adjust input element type (Textarea vs Input) based on configuration
            const inputEl = document.getElementById('inputValue');
            if (inputEl) {
                if (inputType === 'textarea') {
                    const textarea = document.createElement('textarea');
                    textarea.id = 'inputValue';
                    textarea.className = inputEl.className;
                    textarea.placeholder = inputPlaceholder;
                    textarea.setAttribute('aria-label', inputEl.getAttribute('aria-label'));
                    textarea.rows = 2;
                    inputEl.parentNode.replaceChild(textarea, inputEl);
                } else {
                    inputEl.placeholder = inputPlaceholder;
                }
            }

            // Populate the input unit dropdown menu
            inputUnitSelect = document.getElementById('inputUnit');
            if (inputUnitSelect) {
                const frag = document.createDocumentFragment();
                Object.keys(units).forEach(key => {
                    const opt = document.createElement('option');
                    opt.value = key;
                    opt.textContent = `${units[key].name} (${units[key].symbol})`;
                    if (key === defaultUnit) opt.selected = true;
                    frag.appendChild(opt);
                });
                inputUnitSelect.innerHTML = '';
                inputUnitSelect.appendChild(frag);

                // Add listener for unit change
                inputUnitSelect.addEventListener('change', () => {
                    handleInput();
                    updateVisibility();
                });
            }

            // Define the calculation logic for unit conversion
            calculate = (vals) => {
                const valStr = vals.inputValue;
                const currentUnitKey = inputUnitSelect ? inputUnitSelect.value : defaultUnit;
                const res = {};

                if (!units[currentUnitKey]) return res;

                if (converterType === 'numeric') {
                    const val = parseFloat(valStr);
                    const baseValue = isNaN(val) ? 0 : units[currentUnitKey].toBase(val);

                    Object.keys(units).forEach(key => {
                        if (isNaN(val) || valStr === '') {
                            res[key] = '-';
                        } else {
                            const u = units[key];
                            const targetValue = u.fromBase(baseValue);
                            res[key] = formatNumber(targetValue) + ' ' + u.symbol;
                        }
                    });
                } else {
                    // String-based conversion
                    const baseValue = units[currentUnitKey].toBase(valStr);
                    Object.keys(units).forEach(key => {
                        res[key] = (valStr === '') ? '-' : units[key].fromBase(baseValue);
                    });
                }
                return res;
            };
        }

        // --------------------------------------------------------------------------
        // State Management
        // --------------------------------------------------------------------------
        let selectedStats = new Set(Object.keys(stats).filter(k => stats[k].default !== false));
        const defaultStats = new Set(selectedStats);

        // --------------------------------------------------------------------------
        // DOM Elements
        // --------------------------------------------------------------------------
        const resultsContainer = document.getElementById(resultsId);
        const viewOptionsMenu = document.getElementById(dropdownId);
        const btnClear = document.getElementById(clearBtnId);
        const inputElements = inputs.map(id => document.getElementById(id)).filter(el => el);

        /**
         * Initializes the UI components, including result cards and dropdown menus.
         * Uses DocumentFragment for efficient DOM insertion.
         */
        const init = () => {
            // Create "Select All", "Clear All", and "Reset" actions in the dropdown
            if (viewOptionsMenu) {
                const liActions = document.createElement('li');
                liActions.innerHTML = `
            <div class="dropdown-item-text">
                <div class="d-flex gap-2 mb-2">
                    <button type="button" class="btn btn-sm btn-outline-primary w-50" id="btn_calc_select_all">Select All</button>
                    <button type="button" class="btn btn-sm btn-outline-danger w-50" id="btn_calc_clear_all">Clear All</button>
                </div>
                <button type="button" class="btn btn-sm btn-outline-secondary w-100" id="btn_calc_reset">Reset to Default</button>
            </div>
            <li><hr class="dropdown-divider"></li>
        `;
                liActions.addEventListener('click', e => e.stopPropagation());
                viewOptionsMenu.appendChild(liActions);

                // Bind Action Buttons
                liActions.querySelector('#btn_calc_select_all').addEventListener('click', () => {
                    selectedStats = new Set(Object.keys(stats));
                    updateVisibility();
                });
                liActions.querySelector('#btn_calc_clear_all').addEventListener('click', () => {
                    selectedStats.clear();
                    updateVisibility();
                });
                liActions.querySelector('#btn_calc_reset').addEventListener('click', () => {
                    selectedStats = new Set(defaultStats);
                    updateVisibility();
                });
            }

            // Generate result cards and corresponding dropdown toggle options
            const statKeys = Object.keys(stats);

            const resultsFrag = document.createDocumentFragment();
            const dropdownFrag = viewOptionsMenu ? document.createDocumentFragment() : null;

            // Hide the view options dropdown if there are insufficient options to toggle
            if (viewOptionsMenu && statKeys.length <= 1) {
                const dropdown = viewOptionsMenu.closest('.dropdown');
                if (dropdown) {
                    dropdown.style.display = 'none';
                    const col = dropdown.closest('.col-auto');
                    if (col) col.style.display = 'none';
                }
            }

            const category = resultsContainer ? resultsContainer.getAttribute('data-category') : '';
            const borderStyle = category ? `border-left: 5px solid var(--${category});` : '';

            statKeys.forEach(key => {
                const s = stats[key];

                // Create the result card element
                const col = document.createElement('div');
                col.className = 'col';
                col.dataset.stat = key;
                col.innerHTML = `
            <div class="stat position-relative text-center" style="color: var(--bnw); ${borderStyle}">
                <div class="small">${s.name}</div>
                <div class="res-val mb-0" id="res_${key}" style="padding-right: 2rem; padding-left: 2rem;">-</div>
                <div class="small text-primary mt-1" id="sub_${key}" style="display:none"></div>
                <button class="btn btn-sm btn-link text-secondary position-absolute top-50 end-0 translate-middle-y me-2 p-0"
                        id="btn_copy_${key}"
                        style="display:none; z-index: 5; text-decoration: none; border: 0;"
                        data-bs-toggle="tooltip"
                        title="Copy">
                    <i class="bi bi-clipboard"></i>
                </button>
            </div>
        `;
                resultsFrag.appendChild(col);

                // Cache DOM references for efficient updates
                s.element = col;
                s.valElement = col.querySelector(`#res_${key}`);
                s.subElement = col.querySelector(`#sub_${key}`);
                s.copyBtn = col.querySelector(`#btn_copy_${key}`);

                // Initialize tooltip
                if (s.copyBtn && typeof bootstrap !== 'undefined' && bootstrap.Tooltip) {
                    new bootstrap.Tooltip(s.copyBtn);
                }

                // Add click listener for copy button
                if (s.copyBtn) {
                    // Initialize tooltip on hover if not already initialized
                    s.copyBtn.addEventListener('mouseenter', () => {
                        if (typeof bootstrap !== 'undefined' && bootstrap.Tooltip && !bootstrap.Tooltip.getInstance(s.copyBtn)) {
                            new bootstrap.Tooltip(s.copyBtn).show();
                        }
                    });

                    s.copyBtn.addEventListener('click', () => {
                        const text = s.valElement.textContent;
                        if (text && text !== '-') {
                            navigator.clipboard.writeText(text).then(() => {
                                const icon = s.copyBtn.querySelector('i');
                                const originalIconClass = icon.className;
                                icon.className = 'bi bi-clipboard-check';

                                // Tooltip logic is handled here, at click time, to ensure bootstrap is loaded.
                                if (typeof bootstrap !== 'undefined' && bootstrap.Tooltip) {
                                    let tooltip = bootstrap.Tooltip.getInstance(s.copyBtn);
                                    if (!tooltip) {
                                        tooltip = new bootstrap.Tooltip(s.copyBtn);
                                    }
                                    s.copyBtn.setAttribute('data-bs-original-title', 'Copied!');
                                    tooltip.show();
                                    setTimeout(() => {
                                        tooltip.hide();
                                        s.copyBtn.setAttribute('data-bs-original-title', 'Copy');
                                        icon.className = originalIconClass;
                                    }, 2000);
                                }
                            }).catch(err => console.error("Copy failed:", err));
                        }
                    });
                }

                // Create the dropdown toggle item
                if (dropdownFrag) {
                    const li = document.createElement('li');
                    li.innerHTML = `
                <div class="dropdown-item">
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" value="${key}" id="chk_${key}" ${selectedStats.has(key) ? 'checked' : ''}>
                        <label class="form-check-label w-100" for="chk_${key}">${s.name}</label>
                    </div>
                </div>
            `;
                    li.addEventListener('click', e => e.stopPropagation());
                    const chk = li.querySelector('input');
                    chk.addEventListener('change', () => {
                        if (chk.checked) selectedStats.add(key);
                        else selectedStats.delete(key);
                        updateVisibility();
                    });
                    dropdownFrag.appendChild(li);
                    s.checkbox = chk;
                }
            });

            resultsContainer.appendChild(resultsFrag);
            if (viewOptionsMenu && dropdownFrag) viewOptionsMenu.appendChild(dropdownFrag);
        };

        /**
         * Updates the visibility of result cards based on user selection and mode.
         */
        const updateVisibility = () => {
            // In Converter Mode, hide the result card corresponding to the selected input unit
            let visibleCount = 0;
            const currentInputUnit = isConverter && inputUnitSelect ? inputUnitSelect.value : null;

            Object.keys(stats).forEach(key => {
                const s = stats[key];
                // If converter, hide if it matches the input unit
                const isHidden = !selectedStats.has(key) || (key === currentInputUnit);

                s.element.classList.toggle('d-none', isHidden);
                if (s.checkbox) s.checkbox.checked = selectedStats.has(key);

                if (!isHidden) visibleCount++;
            });

            // Dynamically adjust the grid layout based on the number of visible cards
            resultsContainer.className = 'row g-2 mb-3';
            if (visibleCount <= 1) {
                resultsContainer.classList.add('row-cols-1');
            } else {
                resultsContainer.classList.add('row-cols-1', 'row-cols-md-2');
            }
        };

        /**
         * Retrieves input values, executes the calculation, and updates the UI.
         */
        const updateValues = () => {
            // Collect values from all configured input elements
            const inputValues = {};
            inputElements.forEach(el => {
                inputValues[el.id] = el.value;
            });

            // Execute the calculation function
            const results = calculate(inputValues);

            // Update result cards with the computed values
            Object.keys(stats).forEach(key => {
                const s = stats[key];
                const res = results[key];

                if (res === undefined || res === null) {
                    s.valElement.textContent = '-';
                    s.subElement.style.display = 'none';
                } else if (typeof res === 'object' && res !== null) {
                    s.valElement.textContent = res.main || '-';
                    if (res.sub) {
                        s.subElement.textContent = res.sub;
                        s.subElement.style.display = 'block';
                    } else {
                        s.subElement.style.display = 'none';
                    }
                } else {
                    s.valElement.textContent = res;
                    s.subElement.style.display = 'none';
                }

                if (s.copyBtn) {
                    const text = s.valElement.textContent;
                    s.copyBtn.style.display = (text !== '-' && text.trim() !== '') ? 'block' : 'none';
                }
            });
        };

        /**
         * Debounced input handler to prevent excessive recalculations during typing.
         */
        let tId = null;
        const handleInput = () => {
            clearTimeout(tId);
            tId = setTimeout(updateValues, 100);
        };

        // --------------------------------------------------------------------------
        // Event Listeners
        // --------------------------------------------------------------------------
        inputElements.forEach(el => {
            el.addEventListener('input', handleInput);
            el.addEventListener('change', handleInput); // For date pickers/selects
        });

        if (btnClear) {
            btnClear.addEventListener('click', () => {
                inputElements.forEach(el => {
                    // Do not clear select elements, as it can cause unexpected behavior.
                    if (el.tagName.toLowerCase() !== 'select') {
                        el.value = '';
                    }
                });
                updateValues();
                if (inputElements.length > 0) inputElements[0].focus();
            });
        }

        // --------------------------------------------------------------------------
        // Initialization
        // --------------------------------------------------------------------------
        init();
        updateVisibility();
        updateValues();
    };
})();

/**
 * Shared Converter Logic
 *
 * This module provides a reusable foundation for various unit conversion tools.
 * It handles UI initialization, state management, conversion logic normalization,
 * and optimized DOM updates.
 */
(function () {
    // Expose the setup function globally
    window.setupConverter = function (config) {
        const { units, defaultUnit, defaultSelectedUnits, converterType = 'numeric', inputPlaceholder = 'Enter value...', inputType = 'number' } = config;

        // Normalize units to support both 'factor' (simple multiplication) and 'toBase/fromBase' (formulas)
        Object.keys(units).forEach(key => {
            const u = units[key];
            if (u.factor !== undefined && !u.toBase) {
                u.toBase = v => v * u.factor;
                u.fromBase = v => v / u.factor;
            }
        });

        // Default visible units to avoid clutter
        let selectedUnits = new Set(defaultSelectedUnits);
        // Cache for currently visible units to optimize the update loop
        let visibleUnitsCache = new Set();

        // DOM Elements - These IDs must be present in the HTML
        const resultsContainer = document.getElementById('resultsContainer');
        const unitDropdownMenu = document.getElementById('unitDropdownMenu');
        const inputUnitSelect = document.getElementById('inputUnit');
        let inputValue = document.getElementById('inputValue');
        const btnClear = document.getElementById('btnClear');
        let btnReset; // Will be initialized in init()

        // Dynamic Input Type Switching (e.g. for Textarea)
        if (inputType === 'textarea') {
            const textarea = document.createElement('textarea');
            textarea.id = 'inputValue';
            textarea.className = inputValue.className;
            textarea.placeholder = inputPlaceholder;
            textarea.setAttribute('aria-label', inputValue.getAttribute('aria-label'));
            textarea.rows = 2;
            inputValue.parentNode.replaceChild(textarea, inputValue);
            inputValue = textarea;
        }

        /**
         * Initializes the UI components: result cards, dropdown items, and event listeners.
         */
        function init() {
            if (inputType !== 'textarea') {
                inputValue.placeholder = inputPlaceholder;
            }

            // 0. Create Select All / Clear All Actions
            const liActions = document.createElement('li');
            liActions.innerHTML = `
                <div class="dropdown-item">
                    <div class="d-flex gap-2 mb-2">
                        <button type="button" class="btn btn-sm btn-outline-primary w-50" id="btn_select_all_dd">Select All</button>
                        <button type="button" class="btn btn-sm btn-outline-danger w-50" id="btn_clear_all_dd">Clear All</button>
                    </div>
                    <button type="button" class="btn btn-sm btn-outline-secondary w-100" id="btn_reset_dd">Reset to Default</button>
                </div>
            `;
            liActions.addEventListener('click', (e) => e.stopPropagation());
            unitDropdownMenu.appendChild(liActions);

            const liDivider = document.createElement('li');
            liDivider.innerHTML = '<hr class="dropdown-divider">';
            unitDropdownMenu.appendChild(liDivider);

            const btnSelectAllDd = liActions.querySelector('#btn_select_all_dd');
            const btnClearAllDd = liActions.querySelector('#btn_clear_all_dd');
            btnReset = liActions.querySelector('#btn_reset_dd');

            // Use DocumentFragments to batch DOM insertions for better performance
            const resultsFrag = document.createDocumentFragment();
            const menuFrag = document.createDocumentFragment();
            const selectFrag = document.createDocumentFragment();

            Object.keys(units).forEach(key => {
                const u = units[key];

                // 1. Create Result Card
                const col = document.createElement('div');
                col.className = 'col';
                col.dataset.unit = key;
                col.innerHTML = `
                    <div class="stat">
                        <div class="muted small text-truncate" title="${u.name}">${u.name}</div>
                        <div class="res-val mb-0 text-break" data-target="${key}">-</div>
                    </div>
                `;
                resultsFrag.appendChild(col);

                // 2. Create Dropdown Checkbox
                const li = document.createElement('li');
                li.dataset.unit = key;
                li.innerHTML = `
                    <div class="dropdown-item">
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="${key}" id="chk_${key}" ${selectedUnits.has(key) ? 'checked' : ''}>
                            <label class="form-check-label w-100" for="chk_${key}">${u.name}</label>
                        </div>
                    </div>
                `;
                // Prevent dropdown from closing on click
                li.addEventListener('click', (e) => e.stopPropagation());
                li.querySelector('input').addEventListener('change', (e) => {
                    if (selectedUnits.has(key)) selectedUnits.delete(key);
                    else selectedUnits.add(key);

                    updateVisibility();
                    updateValues();
                });
                menuFrag.appendChild(li);

                // 3. Create Dropdown Option
                const opt = document.createElement('option');
                opt.value = key;
                opt.textContent = `${u.name} (${u.symbol})`;
                if (key === defaultUnit) opt.selected = true;
                selectFrag.appendChild(opt);

                // Cache DOM references for faster updates during user interaction
                u.elements = {
                    col: col,
                    val: col.querySelector('.res-val'),
                    li: li,
                    chk: li.querySelector('input')
                };
            });

            // Append fragments to DOM
            resultsContainer.appendChild(resultsFrag);
            unitDropdownMenu.appendChild(menuFrag);
            inputUnitSelect.appendChild(selectFrag);
            
            if (defaultUnit) {
                inputUnitSelect.value = defaultUnit;
            }

            // Select All / Clear All Listeners
            btnSelectAllDd.addEventListener('click', () => {
                selectedUnits = new Set(Object.keys(units));
                updateVisibility();
                updateValues();
            });

            btnClearAllDd.addEventListener('click', () => {
                selectedUnits.clear();
                updateVisibility();
                updateValues();
            });

            btnReset.addEventListener('click', () => {
                selectedUnits = new Set(defaultSelectedUnits);
                updateVisibility();
                updateValues();
            });
        }

        /**
         * Formats a number for display, using scientific notation for extreme values
         * and fixed precision for standard ranges to ensure readability.
         */
        function formatNumber(num) {
            if (num === 0) return '0';
            const abs = Math.abs(num);
            if (abs < 1e-4 || abs > 1e6) {
                return num.toExponential(4);
            }
            return parseFloat(num.toPrecision(6)).toString();
        }

        /**
         * Updates the visibility of result cards based on user selection and current input unit.
         * This function handles DOM layout changes (showing/hiding elements) and is separated
         * from value updates to improve performance.
         */
        function updateVisibility() {
            const currentUnitKey = inputUnitSelect.value;
            let unitsToShow = new Set(selectedUnits);

            if (unitsToShow.has(currentUnitKey)) {
                unitsToShow.delete(currentUnitKey);
            }

            if (unitsToShow.size === 0 && selectedUnits.size > 0) {
                // Generic fallback: find first unit that isn't the current one
                const fallback = Object.keys(units).find(k => k !== currentUnitKey);
                if (fallback) unitsToShow.add(fallback);
            }

            const isDefaultSet = selectedUnits.size === defaultSelectedUnits.length && 
                                 defaultSelectedUnits.every(u => selectedUnits.has(u));

            btnReset.classList.toggle('d-none', isDefaultSet);
            visibleUnitsCache = unitsToShow;

            const count = unitsToShow.size;
            resultsContainer.className = 'row g-2 mb-3';
            if (converterType !== 'numeric' || count <= 1) {
                resultsContainer.classList.add('row-cols-1');
            } else {
                resultsContainer.classList.add('row-cols-2');
                if (count === 3) resultsContainer.classList.add('row-cols-md-3');
                else if (count >= 4) resultsContainer.classList.add('row-cols-md-4');
            }

            Object.keys(units).forEach(key => {
                const u = units[key];
                const els = u.elements;
                els.chk.checked = selectedUnits.has(key);
                els.li.classList.toggle('d-none', key === currentUnitKey);
                els.col.classList.toggle('d-none', !unitsToShow.has(key));
            });
        }

        /**
         * Calculates and updates the text content of visible result cards.
         * This runs on every input event and uses the visibility cache to minimize DOM access.
         */
        function updateValues() {
            const currentUnitKey = inputUnitSelect.value;
            if (!units[currentUnitKey]) return;

            if (converterType === 'numeric') {
                const val = parseFloat(inputValue.value);
                const baseValue = isNaN(val) ? 0 : units[currentUnitKey].toBase(val);

                visibleUnitsCache.forEach(key => {
                    const u = units[key];
                    const els = u.elements;

                    if (isNaN(val) || inputValue.value.length === 0) {
                        els.val.textContent = '-';
                    } else {
                        const targetValue = u.fromBase(baseValue);
                        els.val.textContent = formatNumber(targetValue) + ' ' + u.symbol;
                    }
                });
            } else { // Assumes string-based conversion
                const val = inputValue.value;
                const baseValue = units[currentUnitKey].toBase(val);

                visibleUnitsCache.forEach(key => {
                    const u = units[key];
                    u.elements.val.textContent = (val.length === 0) ? '-' : u.fromBase(baseValue);
                });
            }
        }

        inputValue.addEventListener('input', updateValues);
        inputUnitSelect.addEventListener('change', () => {
            updateVisibility();
            updateValues();
        });
        btnClear.addEventListener('click', () => {
            inputValue.value = '';
            updateValues();
            inputValue.focus();
        });

        init();
        updateVisibility();
        updateValues();
    };
})();
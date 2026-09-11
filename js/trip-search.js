/**
 * ABC Trek in Nepal — Instant Trip Search Autocomplete
 * Indexes all 18 specialized Annapurna trekking routes with zero latency.
 */
(function () {
  'use strict';

  const ALL_TREKS = [
    {
      title: '10-Day Annapurna Base Camp Classic Sanctuary',
      shortTitle: 'Annapurna Base Camp (10 Days)',
      url: '/treks/annapurna-base-camp-classic-10-days',
      duration: '10 Days',
      altitude: '4,130m',
      badge: 'Flagship',
      category: 'Base Camp',
      keywords: 'abc sanctuary pokhara deurali chhomrong machapuchare mbc 10 days classic popular flagship'
    },
    {
      title: '8 Days Annapurna Base Camp Trek',
      shortTitle: '8 Days ABC Trek',
      url: '/treks/8-days-annapurna-base-camp-trek',
      duration: '8 Days',
      altitude: '4,130m',
      badge: '8 Days',
      category: 'Base Camp',
      keywords: 'abc 8 days fast base camp sanctuary pokhara'
    },
    {
      title: 'Short Annapurna Base Camp Trek (Express)',
      shortTitle: 'Short ABC Trek',
      url: '/treks/short-annapurna-base-camp-trek',
      duration: '6-7 Days',
      altitude: '4,130m',
      badge: 'Express',
      category: 'Base Camp',
      keywords: 'short abc express 6 days 7 days quick fast base camp'
    },
    {
      title: 'Annapurna Circuit Trek (Full Classic)',
      shortTitle: 'Annapurna Circuit Trek',
      url: '/treks/annapurna-circuit-trek',
      duration: '16-18 Days',
      altitude: '5,416m',
      badge: 'Classic',
      category: 'Circuit',
      keywords: 'circuit thorong la pass muktinath manang jomsom round annapurna'
    },
    {
      title: '14 Days Annapurna Circuit Trek',
      shortTitle: '14 Days Circuit Trek',
      url: '/treks/14-days-annapurna-circuit-trek',
      duration: '14 Days',
      altitude: '5,416m',
      badge: '14 Days',
      category: 'Circuit',
      keywords: 'circuit 14 days thorong la manang muktinath round'
    },
    {
      title: 'Short Annapurna Circuit Trek',
      shortTitle: 'Short Circuit Trek',
      url: '/treks/annapurna-circuit-short-trek',
      duration: '10-12 Days',
      altitude: '5,416m',
      badge: '10 Days',
      category: 'Circuit',
      keywords: 'short circuit thorong la 10 days 12 days express'
    },
    {
      title: 'Annapurna Circuit with Tilicho Lake Trek',
      shortTitle: 'Circuit with Tilicho Lake',
      url: '/treks/annapurna-circuit-with-tilicho-lake-trek',
      duration: '16-18 Days',
      altitude: '4,919m',
      badge: 'High Alpine',
      category: 'Circuit',
      keywords: 'tilicho lake high altitude turquoise glacial lake thorong la circuit'
    },
    {
      title: 'Ghorepani Poon Hill Sunrise Trek',
      shortTitle: 'Ghorepani Poon Hill',
      url: '/treks/ghorepani-poon-hill-trek',
      duration: '4-5 Days',
      altitude: '3,210m',
      badge: 'Popular',
      category: 'Poon Hill',
      keywords: 'poon hill ghorepani sunrise dhaulagiri panoramic easy family rhododendron'
    },
    {
      title: '3 Days Poon Hill Express Trek',
      shortTitle: '3 Days Poon Hill',
      url: '/treks/3-days-poon-hill-trek',
      duration: '3 Days',
      altitude: '3,210m',
      badge: '3 Days',
      category: 'Poon Hill',
      keywords: '3 days poon hill ulleri ghorepani quick weekend'
    },
    {
      title: '4 Days Poon Hill Trek',
      shortTitle: '4 Days Poon Hill',
      url: '/treks/4-days-poon-hill-trek',
      duration: '4 Days',
      altitude: '3,210m',
      badge: '4 Days',
      category: 'Poon Hill',
      keywords: '4 days poon hill ghorepani gandruk pokhara'
    },
    {
      title: '5 Days Poon Hill & Ghandruk Trek',
      shortTitle: '5 Days Poon Hill',
      url: '/treks/5-days-poon-hill-trek',
      duration: '5 Days',
      altitude: '3,210m',
      badge: '5 Days',
      category: 'Poon Hill',
      keywords: '5 days poon hill ghandruk heritage loop cultural'
    },
    {
      title: 'Mardi Himal High Ridge Trek',
      shortTitle: 'Mardi Himal Trek',
      url: '/treks/mardi-himal-trek',
      duration: '5-6 Days',
      altitude: '4,500m',
      badge: 'Ridge Trek',
      category: 'Mardi Himal',
      keywords: 'mardi himal fishtail machapuchare high camp forest camp ridge view'
    },
    {
      title: 'Khopra Ridge (Khopra Danda) & Khayer Lake',
      shortTitle: 'Khopra Ridge Trek',
      url: '/treks/khopra-ridge-trek',
      duration: '8-9 Days',
      altitude: '4,660m',
      badge: 'Panoramic',
      category: 'Remote',
      keywords: 'khopra danda ridge khayer sacred lake off the beaten path panoramic'
    },
    {
      title: 'Nar Phu Valley Restricted Wilderness Trek',
      shortTitle: 'Nar Phu Valley Trek',
      url: '/treks/nar-phu-valley-trek',
      duration: '9-11 Days',
      altitude: '5,320m',
      badge: 'Restricted',
      category: 'Remote',
      keywords: 'nar phu tibetan culture remote restricted kang la pass wild'
    },
    {
      title: 'Panchase Eco & Cultural Trek',
      shortTitle: 'Panchase Trek',
      url: '/treks/panchase-trek',
      duration: '3-4 Days',
      altitude: '2,065m',
      badge: 'Eco-Walk',
      category: 'Scenic',
      keywords: 'panchase eco easy family peaceful forest pokhara'
    },
    {
      title: 'Sikles Gurung Heritage Trek',
      shortTitle: 'Sikles Trek',
      url: '/treks/sikles-trek',
      duration: '4-5 Days',
      altitude: '2,000m',
      badge: 'Gurung Lore',
      category: 'Cultural',
      keywords: 'sikles gurung cultural village heritage kapuche glacier lake'
    },
    {
      title: 'Jomsom Muktinath Pilgrimage Trek',
      shortTitle: 'Jomsom Muktinath',
      url: '/treks/jomsom-muktinath-trek-with-poon-hill',
      duration: '7-8 Days',
      altitude: '3,760m',
      badge: 'Pilgrimage',
      category: 'Cultural',
      keywords: 'jomsom muktinath kali gandaki temple pilgrimage windy valley'
    },
    {
      title: 'Annapurna View Scenic Panorama Trek',
      shortTitle: 'Annapurna View Trek',
      url: '/treks/annapurna-view-trek',
      duration: '5-6 Days',
      altitude: '3,210m',
      badge: 'Scenic',
      category: 'Scenic',
      keywords: 'annapurna view sunrise scenic mountain photography'
    }
  ];

  function initTripSearch() {
    const searchInput = document.getElementById('tripSearchInput');
    const searchDropdown = document.getElementById('searchDropdown');
    const clearBtn = document.getElementById('searchClearBtn');
    const submitBtn = document.getElementById('searchSubmitBtn');
    const wrapper = document.getElementById('heroSearchWrapper');

    if (!searchInput || !searchDropdown) return;

    let activeIndex = -1;
    let currentResults = [];

    function renderDropdown(items, isDefault) {
      currentResults = items;
      activeIndex = -1;

      if (!items || items.length === 0) {
        searchDropdown.innerHTML = `
          <div class="search-no-results">
            <p>No routes found matching "<strong>${escapeHtml(searchInput.value)}</strong>".</p>
            <a href="/treks" style="color: #F59E0B; font-weight: 700; text-decoration: none; margin-top: 6px; display: inline-block;">
              Browse all 18 Annapurna expeditions &rarr;
            </a>
          </div>
        `;
        searchDropdown.style.display = 'block';
        return;
      }

      const headerTitle = isDefault ? 'Featured & Popular Expeditions' : `Matching Routes (${items.length})`;
      let html = `<div class="search-dropdown-header"><span>${headerTitle}</span><span>18 Routes Total</span></div>`;

      items.forEach(function (trek, idx) {
        const isFlagship = trek.badge === 'Flagship';
        const badgeClass = isFlagship ? 'search-item-badge flagship' : 'search-item-badge';
        html += `
          <a href="${trek.url}" class="search-dropdown-item" data-index="${idx}" role="option">
            <div class="search-item-title-group">
              <span class="search-item-title">${escapeHtml(trek.title)}</span>
              <div class="search-item-meta">
                <span class="${badgeClass}">${trek.badge}</span>
                <span>${trek.duration}</span>
                <span>${trek.altitude}</span>
              </div>
            </div>
            <span class="search-item-arrow">&rarr;</span>
          </a>
        `;
      });

      html += `
        <div style="padding: 8px 20px; background: #F8FAFC; border-top: 1px solid #F1F5F9; text-align: center;">
          <a href="/treks" style="font-size: 0.75rem; font-weight: 700; color: #081B3A; text-decoration: none;">
            View Complete 18-Trek Directory &rarr;
          </a>
        </div>
      `;

      searchDropdown.innerHTML = html;
      searchDropdown.style.display = 'block';
    }

    function searchTrips(query) {
      const q = query.trim().toLowerCase();
      if (!q) {
        // Show top 5 recommended routes by default
        const defaultTrips = [
          ALL_TREKS[0], // 10-day ABC
          ALL_TREKS[3], // Circuit
          ALL_TREKS[7], // Poon Hill
          ALL_TREKS[11], // Mardi Himal
          ALL_TREKS[1]  // 8-day ABC
        ];
        renderDropdown(defaultTrips, true);
        return;
      }

      const matches = ALL_TREKS.filter(function (t) {
        return (
          t.title.toLowerCase().includes(q) ||
          t.shortTitle.toLowerCase().includes(q) ||
          t.keywords.toLowerCase().includes(q) ||
          t.category.toLowerCase().includes(q) ||
          t.duration.toLowerCase().includes(q) ||
          t.altitude.toLowerCase().includes(q)
        );
      });

      renderDropdown(matches, false);
    }

    function updateActiveItem(direction) {
      const items = searchDropdown.querySelectorAll('.search-dropdown-item');
      if (!items || items.length === 0) return;

      if (direction === 'down') {
        activeIndex = (activeIndex + 1) % items.length;
      } else if (direction === 'up') {
        activeIndex = (activeIndex - 1 + items.length) % items.length;
      }

      items.forEach(function (el, i) {
        if (i === activeIndex) {
          el.classList.add('active');
          el.scrollIntoView({ block: 'nearest' });
        } else {
          el.classList.remove('active');
        }
      });
    }

    // Input events
    searchInput.addEventListener('input', function () {
      const val = this.value;
      if (clearBtn) {
        clearBtn.style.display = val.length > 0 ? 'inline-block' : 'none';
      }
      searchTrips(val);
    });

    searchInput.addEventListener('focus', function () {
      searchTrips(this.value);
    });

    if (clearBtn) {
      clearBtn.addEventListener('click', function () {
        searchInput.value = '';
        this.style.display = 'none';
        searchTrips('');
        searchInput.focus();
      });
    }

    if (submitBtn) {
      submitBtn.addEventListener('click', function (e) {
        e.preventDefault();
        if (activeIndex >= 0 && currentResults[activeIndex]) {
          window.location.href = currentResults[activeIndex].url;
        } else if (currentResults.length > 0) {
          window.location.href = currentResults[0].url;
        } else {
          window.location.href = '/treks';
        }
      });
    }

    // Keyboard navigation
    searchInput.addEventListener('keydown', function (e) {
      if (searchDropdown.style.display === 'none') return;

      if (e.key === 'ArrowDown') {
        e.preventDefault();
        updateActiveItem('down');
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        updateActiveItem('up');
      } else if (e.key === 'Enter') {
        e.preventDefault();
        if (activeIndex >= 0 && currentResults[activeIndex]) {
          window.location.href = currentResults[activeIndex].url;
        } else if (currentResults.length > 0) {
          window.location.href = currentResults[0].url;
        } else {
          window.location.href = '/treks';
        }
      } else if (e.key === 'Escape') {
        searchDropdown.style.display = 'none';
      }
    });

    // Close on outside click
    document.addEventListener('click', function (e) {
      if (wrapper && !wrapper.contains(e.target)) {
        searchDropdown.style.display = 'none';
      }
    });

    function escapeHtml(str) {
      return (str || '').replace(/[&<>"']/g, function (m) {
        return {
          '&': '&amp;',
          '<': '&lt;',
          '>': '&gt;',
          '"': '&quot;',
          "'": '&#039;'
        }[m];
      });
    }

    // Test hook for headless visual verification
    if (window.location.hash === '#test-search') {
      searchInput.value = 'poon';
      clearBtn.style.display = 'inline-block';
      searchTrips('poon');
    }

    console.log('[TripSearch] Initialized with 18 Annapurna routes');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTripSearch);
  } else {
    initTripSearch();
  }
})();

/**
 * ABC Trek in Nepal — Universal Mobile Navigation & Drawer Controller
 */
(function () {
  'use strict';

  function initMobileNav() {
    const openBtn = document.getElementById('mobileMenuOpen');
    const closeBtn = document.getElementById('mobileMenuClose');
    const drawer = document.getElementById('mobileMenu');
    const overlay = document.getElementById('mobileOverlay');

    if (!drawer || !overlay) {
      console.warn('[MobileNav] Drawer or overlay element not found');
      return;
    }

    function toggleMenu(open) {
      if (open) {
        drawer.classList.add('active');
        overlay.classList.add('active');
        document.body.style.overflow = 'hidden';
      } else {
        drawer.classList.remove('active');
        overlay.classList.remove('active');
        document.body.style.overflow = '';
      }
    }

    if (openBtn) {
      openBtn.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        toggleMenu(true);
      });
    }

    if (closeBtn) {
      closeBtn.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        toggleMenu(false);
      });
    }

    if (overlay) {
      overlay.addEventListener('click', function (e) {
        e.preventDefault();
        toggleMenu(false);
      });
    }

    // Close on Escape key press
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drawer.classList.contains('active')) {
        toggleMenu(false);
      }
    });

    // Accordion toggle inside mobile drawer
    const accordionToggles = drawer.querySelectorAll('.mobile-accordion-toggle');
    accordionToggles.forEach(function (toggle) {
      toggle.addEventListener('click', function (e) {
        e.preventDefault();
        const panel = this.nextElementSibling;
        if (!panel) return;

        const isOpen = panel.classList.contains('active');
        // Close all sibling panels
        accordionToggles.forEach(function (t) {
          t.classList.remove('active');
          if (t.nextElementSibling) {
            t.nextElementSibling.classList.remove('active');
          }
        });

        if (!isOpen) {
          this.classList.add('active');
          panel.classList.add('active');
        }
      });
    });

    // Close drawer when clicking any standard nav link inside
    const drawerLinks = drawer.querySelectorAll('a:not(.mobile-accordion-toggle)');
    drawerLinks.forEach(function (link) {
      link.addEventListener('click', function () {
        toggleMenu(false);
      });
    });

    console.log('[MobileNav] Initialized successfully');
  }

  function initFloatingActions() {
    // Inject floating action buttons if not already hardcoded in DOM
    let container = document.querySelector('.floating-actions');
    if (!container) {
      container = document.createElement('aside');
      container.className = 'floating-actions';
      container.setAttribute('aria-label', 'Quick Actions');
      container.innerHTML = `
        <button type="button" class="btn-floating btn-scroll-top" id="scrollTopBtn" aria-label="Scroll to top" title="Scroll to top">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 19V5M5 12l7-7 7 7"/>
          </svg>
        </button>
        <a href="https://wa.me/9779818188459" class="btn-floating btn-whatsapp" id="whatsappBtn" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp" title="Chat on WhatsApp">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
            <path d="M17.472 14.382c-.301-.15-1.78-.879-2.056-.98-.276-.101-.477-.151-.678.15-.2.302-.778.98-.953 1.181-.176.201-.351.226-.652.076-.301-.151-1.272-.469-2.423-1.496-.896-.799-1.501-1.787-1.677-2.088-.175-.302-.019-.465.132-.615.136-.135.301-.352.451-.527.151-.176.201-.302.302-.503.101-.201.05-.377-.025-.528-.075-.151-.677-1.633-.928-2.236-.244-.588-.493-.508-.678-.517l-.578-.01c-.201 0-.527.075-.803.377s-1.055 1.03-1.055 2.513c0 1.482 1.08 2.914 1.23 3.115.151.2 2.126 3.247 5.151 4.553.72.31 1.282.496 1.72.636.723.23 1.381.197 1.901.12.58-.087 1.78-.727 2.031-1.431.251-.703.251-1.306.176-1.431-.075-.126-.276-.201-.577-.352z"/>
            <path d="M12.042 2C6.51 2 2.023 6.486 2.023 12.019c0 1.996.587 3.864 1.603 5.441L2 22.062l4.776-1.571c1.517.944 3.308 1.488 5.266 1.488 5.532 0 10.019-4.486 10.019-10.019 0-5.533-4.487-10.019-10.019-10.019zm0 18.238c-1.745 0-3.364-.537-4.708-1.455l-.338-.231-2.83.931.942-2.759-.253-.356c-1.026-1.442-1.57-3.155-1.57-4.908 0-4.664 3.794-8.458 8.458-8.458 4.663 0 8.458 3.794 8.458 8.458 0 4.663-3.795 8.458-8.458 8.458z"/>
          </svg>
        </a>
      `;
      document.body.appendChild(container);
    }

    const scrollBtn = container.querySelector('.btn-scroll-top');
    if (scrollBtn) {
      let ticking = false;
      function onScroll() {
        if (!ticking) {
          window.requestAnimationFrame(function () {
            if (window.scrollY > 280) {
              scrollBtn.classList.add('visible');
            } else {
              scrollBtn.classList.remove('visible');
            }
            ticking = false;
          });
          ticking = true;
        }
      }
      window.addEventListener('scroll', onScroll, { passive: true });
      onScroll(); // initial check

      scrollBtn.addEventListener('click', function (e) {
        e.preventDefault();
        window.scrollTo({
          top: 0,
          behavior: 'smooth'
        });
      });
    }
  }

  function init() {
    initMobileNav();
    initFloatingActions();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

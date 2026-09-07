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

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMobileNav);
  } else {
    initMobileNav();
  }
})();

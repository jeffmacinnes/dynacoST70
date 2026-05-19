/* Right-side preview panel for cross-cutting reference content
 * (components, theory, test-equipment, modifications, appendices).
 *
 * Intercepts clicks on links into those sections and loads the target
 * page's article content into a side panel — so a reader following a
 * build step can glance at a component or theory page without losing
 * their place. */

(() => {
  const PREVIEWABLE = /\/(components|theory|test-equipment|modifications|appendices)\//;
  let panel = null;

  const buildPanel = () => {
    const el = document.createElement('aside');
    el.className = 'md-preview-panel';
    el.setAttribute('aria-label', 'Reference preview');
    el.innerHTML = `
      <div class="md-preview-panel__header">
        <span class="md-preview-panel__label">Reference</span>
        <div class="md-preview-panel__header-actions">
          <a class="md-preview-panel__expand" href="#" target="_self" rel="noopener" title="Open this page in the main view">Open full →</a>
          <button class="md-preview-panel__close" type="button" aria-label="Close preview">×</button>
        </div>
      </div>
      <div class="md-preview-panel__content">
        <div class="md-preview-panel__loading">Loading…</div>
      </div>
    `;
    document.body.appendChild(el);

    el.querySelector('.md-preview-panel__close').addEventListener('click', closePanel);
    return el;
  };

  const ensurePanel = () => {
    if (!panel || !document.body.contains(panel)) {
      panel = buildPanel();
    }
    return panel;
  };

  const openPanel = () => {
    ensurePanel().classList.add('is-open');
    document.body.classList.add('md-preview-open');
  };

  const closePanel = () => {
    if (!panel) return;
    panel.classList.remove('is-open');
    document.body.classList.remove('md-preview-open');
  };

  const isPreviewable = (href) => {
    if (!href) return false;
    if (href.startsWith('#')) return false;
    if (href.startsWith('mailto:')) return false;
    // External absolute URL? skip (unless same origin)
    if (/^https?:/i.test(href)) {
      try {
        const u = new URL(href);
        if (u.host !== window.location.host) return false;
      } catch (e) {
        return false;
      }
    }
    return PREVIEWABLE.test(href);
  };

  const loadIntoPanel = async (url) => {
    const p = ensurePanel();
    const contentEl = p.querySelector('.md-preview-panel__content');
    const expandLink = p.querySelector('.md-preview-panel__expand');

    contentEl.innerHTML = '<div class="md-preview-panel__loading">Loading…</div>';
    expandLink.href = url;
    openPanel();

    try {
      const res = await fetch(url, { credentials: 'same-origin' });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const html = await res.text();
      const doc = new DOMParser().parseFromString(html, 'text/html');
      const article = doc.querySelector('article.md-content__inner') || doc.querySelector('article');
      if (!article) {
        contentEl.innerHTML = '<p>Could not extract page content.</p>';
        return;
      }
      // Rewrite relative links in the embedded article so they resolve from
      // the source page, not the page currently in the address bar.
      const base = new URL(url, window.location.href);
      article.querySelectorAll('a[href]').forEach((a) => {
        const raw = a.getAttribute('href');
        if (!raw || raw.startsWith('#') || /^[a-z]+:/i.test(raw)) return;
        a.setAttribute('href', new URL(raw, base).href);
      });
      article.querySelectorAll('img[src]').forEach((img) => {
        const raw = img.getAttribute('src');
        if (!raw || /^[a-z]+:/i.test(raw) || raw.startsWith('/')) return;
        img.setAttribute('src', new URL(raw, base).href);
      });
      contentEl.innerHTML = '';
      contentEl.appendChild(article);
      contentEl.scrollTop = 0;
    } catch (err) {
      contentEl.innerHTML = `<p>Failed to load preview: ${err.message}</p>`;
    }
  };

  const onClick = (e) => {
    if (e.button !== 0) return;
    if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;

    const link = e.target.closest('a');
    if (!link) return;
    const rawHref = link.getAttribute('href');
    if (!rawHref) return;

    const insidePanel = !!link.closest('.md-preview-panel');

    if (insidePanel) {
      // Clicks inside the panel: keep the user in the panel unless they
      // hit the "Open full" expand link (which navigates normally).
      if (link.classList.contains('md-preview-panel__expand')) return;
      if (rawHref.startsWith('#')) return; // anchor — let it scroll the panel
      e.preventDefault();
      e.stopPropagation();
      loadIntoPanel(link.href);
      return;
    }

    // Only intercept clicks that come from the article body — NOT from the
    // left navigation, the header tabs, or any other Material chrome. Users
    // navigating the nav should get normal navigation; previewing is for
    // following an inline link within the prose.
    if (!link.closest('.md-content')) return;

    // Click in the main view: intercept only previewable cross-cutting links.
    // Material's navigation.instant attaches a bubble-phase listener that
    // would otherwise hijack the navigation — we use capture phase + stop
    // propagation so the preview panel wins for these links.
    if (!isPreviewable(rawHref)) return;
    e.preventDefault();
    e.stopPropagation();
    loadIntoPanel(link.href);
  };

  const onKey = (e) => {
    if (e.key === 'Escape' && panel && panel.classList.contains('is-open')) {
      closePanel();
    }
  };

  // Capture phase so we run before Material's instant-navigation handler.
  document.addEventListener('click', onClick, true);
  document.addEventListener('keydown', onKey);

  // Material's instant navigation replaces the main content but leaves
  // body-level nodes alone — the panel survives and our document-level
  // listeners keep working. Nothing to re-init here.

  // ============ Lightbox for diagram figures ============
  let lightbox = null;

  const ensureLightbox = () => {
    if (lightbox && document.body.contains(lightbox)) return lightbox;
    lightbox = document.createElement('div');
    lightbox.className = 'md-lightbox';
    lightbox.innerHTML = `
      <button class="md-lightbox__close" type="button" aria-label="Close zoom view">×</button>
      <div class="md-lightbox__content"></div>
    `;
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox || e.target.closest('.md-lightbox__close')) {
        closeLightbox();
      }
    });
    document.body.appendChild(lightbox);
    return lightbox;
  };

  const closeLightbox = () => {
    if (!lightbox) return;
    lightbox.classList.remove('is-open');
    lightbox.querySelector('.md-lightbox__content').innerHTML = '';
    document.body.style.overflow = '';
  };

  const openLightbox = (svgUrl) => {
    const lb = ensureLightbox();
    lb.querySelector('.md-lightbox__content').innerHTML =
      `<object type="image/svg+xml" data="${svgUrl}"></object>`;
    lb.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  };

  document.addEventListener('click', (e) => {
    const fig = e.target.closest('figure.diagram-fig');
    if (!fig) return;
    // Clicks on the caption or its "Open full size" link should NOT trigger
    // the lightbox — let the link navigate / let the user select text.
    if (e.target.closest('figcaption')) return;
    const obj = fig.querySelector('object');
    if (!obj) return;
    const data = obj.getAttribute('data');
    if (!data) return;
    e.preventDefault();
    openLightbox(new URL(data, window.location.href).href);
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && lightbox && lightbox.classList.contains('is-open')) {
      closeLightbox();
    }
  });
})();

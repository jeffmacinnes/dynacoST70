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

  // On narrow viewports the side panel would cover the entire screen, which
  // is more confusing than helpful — just let links navigate normally.
  // Matches Material's tablet breakpoint (76.25em).
  const isNarrow = () => window.matchMedia('(max-width: 76.1875em)').matches;

  const onClick = (e) => {
    if (e.button !== 0) return;
    if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;

    const link = e.target.closest('a');
    if (!link) return;
    const rawHref = link.getAttribute('href');
    if (!rawHref) return;

    const insidePanel = !!link.closest('.md-preview-panel');

    // On narrow viewports, don't intercept anything — including links inside
    // a (possibly stale) panel. The panel won't open here, so the user just
    // navigates normally.
    if (isNarrow() && !insidePanel) return;

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

  // If the user resizes from desktop down into mobile range with the panel
  // open, close it — the mobile experience is "navigate normally," and a
  // lingering panel covering the page would be confusing.
  window.matchMedia('(max-width: 76.1875em)').addEventListener('change', (e) => {
    if (e.matches) closePanel();
  });

  // Material's instant navigation replaces the main content but leaves
  // body-level nodes alone — the panel survives and our document-level
  // listeners keep working. Nothing to re-init here.

  // ============ Inline diagram SVGs ============
  // Each <figure class="diagram-fig"> contains an <img src=".svg"> as its
  // initial markup. <img> renders SVG reliably across desktop and mobile
  // (unlike <object>, which has well-known rendering bugs on iOS Safari).
  //
  // For hover tooltips to work, the SVG needs to live in the host document
  // — <img> SVGs don't expose their internal elements to host-page events.
  // We fetch the SVG text and replace each <img> with inline SVG so the
  // diagram becomes part of the host document and hovers fire natively.
  //
  // We also convert each non-root <title> element into a data-tooltip
  // attribute on its parent and DELETE the <title>. That suppresses the
  // browser's slow native tooltip (~1-2 s delay) so our custom JS tooltip
  // can take over and show instantly.
  const convertTitlesToTooltips = (svg) => {
    svg.querySelectorAll('title').forEach((titleEl) => {
      const parent = titleEl.parentNode;
      if (parent === svg) return; // keep root SVG <title> for a11y
      parent.setAttribute('data-tooltip', titleEl.textContent);
      titleEl.remove();
    });
  };

  const inlineFigureSvgs = async (root = document) => {
    const imgs = root.querySelectorAll(
      'figure.diagram-fig img[src$=".svg"]'
    );
    for (const img of imgs) {
      const url = img.getAttribute('src');
      if (!url) continue;
      try {
        const res = await fetch(url, { credentials: 'same-origin' });
        if (!res.ok) continue;
        const text = await res.text();
        const doc = new DOMParser().parseFromString(text, 'image/svg+xml');
        const svg = doc.documentElement;
        if (svg.nodeName !== 'svg') continue;
        // Let the SVG scale to its container width; preserve aspect ratio.
        svg.removeAttribute('width');
        svg.removeAttribute('height');
        svg.style.width = '100%';
        svg.style.height = 'auto';
        svg.style.display = 'block';
        // Stash the source URL so the lightbox click handler can re-fetch
        // the same SVG (we need a separate copy in the zoomed view).
        svg.dataset.svgSrc = url;
        convertTitlesToTooltips(svg);
        img.replaceWith(svg);
      } catch (err) {
        console.warn('Failed to inline SVG', url, err);
      }
    }
  };

  // ============ Custom fast tooltip ============
  let tooltipEl = null;
  let tooltipTarget = null;

  const ensureTooltip = () => {
    if (tooltipEl && document.body.contains(tooltipEl)) return tooltipEl;
    tooltipEl = document.createElement('div');
    tooltipEl.className = 'diagram-tooltip';
    document.body.appendChild(tooltipEl);
    return tooltipEl;
  };

  const positionTooltip = (x, y) => {
    const t = ensureTooltip();
    // Default: offset to the right and below the cursor.
    let left = x + 18;
    let top = y + 18;
    // After layout, flip sides if we'd overflow the viewport.
    const rect = t.getBoundingClientRect();
    if (left + rect.width > window.innerWidth - 8) {
      left = x - rect.width - 18;
    }
    if (top + rect.height > window.innerHeight - 8) {
      top = y - rect.height - 18;
    }
    if (left < 8) left = 8;
    if (top < 8) top = 8;
    t.style.left = `${left}px`;
    t.style.top = `${top}px`;
  };

  const showTooltip = (text, x, y) => {
    const t = ensureTooltip();
    t.textContent = text;
    t.classList.add('is-visible');
    positionTooltip(x, y);
  };

  const hideTooltip = () => {
    if (tooltipEl) tooltipEl.classList.remove('is-visible');
    tooltipTarget = null;
  };

  document.addEventListener('mousemove', (e) => {
    const target = e.target.closest('[data-tooltip]');
    if (target !== tooltipTarget) {
      tooltipTarget = target;
      if (target) {
        showTooltip(target.getAttribute('data-tooltip'), e.clientX, e.clientY);
      } else {
        hideTooltip();
      }
    } else if (target) {
      positionTooltip(e.clientX, e.clientY);
    }
  });

  // Hide the tooltip if the user scrolls or focuses elsewhere — prevents
  // a stale tooltip from hanging around after the cursor moves out via
  // any non-mousemove path.
  document.addEventListener('scroll', hideTooltip, true);
  document.addEventListener('blur', hideTooltip, true);

  // Inline on first load.
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => inlineFigureSvgs());
  } else {
    inlineFigureSvgs();
  }
  // Re-inline after Material's instant navigation swaps the article content.
  if (typeof document$ !== 'undefined') {
    try { document$.subscribe(() => inlineFigureSvgs()); } catch (e) { /* not Material */ }
  }

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

  // Open the lightbox by fetching the SVG text, parsing it, converting
  // <title> elements to data-tooltip attributes (same trick as the inline
  // figures), and injecting it. That way the custom tooltip code works in
  // the zoomed view too.
  const openLightbox = async (svgUrl) => {
    const lb = ensureLightbox();
    const content = lb.querySelector('.md-lightbox__content');
    content.innerHTML = '<div class="md-lightbox__loading">Loading…</div>';
    lb.classList.add('is-open');
    document.body.style.overflow = 'hidden';
    try {
      const res = await fetch(svgUrl, { credentials: 'same-origin' });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const text = await res.text();
      const doc = new DOMParser().parseFromString(text, 'image/svg+xml');
      const svg = doc.documentElement;
      if (svg.nodeName !== 'svg') throw new Error('Not an SVG');
      svg.removeAttribute('width');
      svg.removeAttribute('height');
      svg.style.width = '100%';
      svg.style.height = '100%';
      convertTitlesToTooltips(svg);
      content.innerHTML = '';
      content.appendChild(svg);
    } catch (err) {
      content.innerHTML = `<p style="color:#fff">Failed to load: ${err.message}</p>`;
    }
  };

  document.addEventListener('click', (e) => {
    const fig = e.target.closest('figure.diagram-fig');
    if (!fig) return;
    // Clicks on the caption or its links should NOT trigger the lightbox —
    // let the link navigate / let the user select text.
    if (e.target.closest('figcaption')) return;
    // Find the SVG (post-inlining) or the original img as a fallback,
    // and resolve its source URL.
    const svg = fig.querySelector('svg');
    const img = fig.querySelector('img[src$=".svg"]');
    let url = null;
    if (svg && svg.dataset.svgSrc) {
      url = svg.dataset.svgSrc;
    } else if (img) {
      url = img.getAttribute('src');
    } else if (svg) {
      // We inlined, but didn't stash the source URL. Try to recover by
      // looking at the matching original from the unmodified page. As a
      // fallback, just skip the lightbox.
      return;
    }
    if (!url) return;
    e.preventDefault();
    openLightbox(new URL(url, window.location.href).href);
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && lightbox && lightbox.classList.contains('is-open')) {
      closeLightbox();
    }
  });
})();

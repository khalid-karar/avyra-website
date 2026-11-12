(function () {
  var d = document, root = d.documentElement;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Header: gains a solid edge once the page scrolls.
  var header = d.querySelector('header.site');
  function onScroll() { if (header) header.classList.toggle('scrolled', window.scrollY > 8); }
  onScroll(); window.addEventListener('scroll', onScroll, { passive: true });

  // Scroll reveal: elements fade up once as they approach the viewport.
  // Anything already above the viewport (anchor jump, reload mid-page, fast scroll) is shown at once.
  if (reduce || !('IntersectionObserver' in window)) { return; } // nothing is hidden without the .rv class, so .js stays (it also drives the mobile menu)
  var sel = '.hero .wrap > div > *, .hero-art, .page-hero .wrap > *, section .wrap > .stack, section .wrap > h2,' +
            ' .card, .principle, .rows > div, .work, .cta .wrap > *, section .wrap > .btns, .prose > *';
  var els = d.querySelectorAll(sel);
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting || e.boundingClientRect.bottom < 0) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.01, rootMargin: '0px 0px 12% 0px' });
  els.forEach(function (el) {
    var i = Array.prototype.indexOf.call(el.parentNode.children, el);
    el.style.setProperty('--d', Math.min(i, 3) * 70 + 'ms');
    el.classList.add('rv'); io.observe(el);
  });
  // Safety net: never leave content hidden if the observer is slow or stalls.
  setTimeout(function () { els.forEach(function (el) { el.classList.add('in'); }); }, 6000);
})();

// Mobile menu
(function () {
  var btn = document.querySelector('.menu-btn'), nav = document.getElementById('site-nav');
  if (!btn || !nav) return;
  btn.hidden = false;
  function set(open) {
    nav.classList.toggle('open', open); btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    btn.setAttribute('aria-label', open ? btn.dataset.close : btn.dataset.open);
  }
  btn.addEventListener('click', function () { set(!nav.classList.contains('open')); });
  nav.addEventListener('click', function (e) { if (e.target.closest('a')) set(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') set(false); });
})();

// Contact forms: send to the configured endpoint, or fall back to the visitor's email app.
(function () {
  document.querySelectorAll('form.form').forEach(function (form) {
    var status = form.querySelector('.status'), btn = form.querySelector('button[type="submit"]');
    function say(msg, ok) { status.textContent = msg; status.className = 'status ' + (ok ? 'ok' : 'bad'); }
    function valid() {
      var ok = true;
      form.querySelectorAll('[required]').forEach(function (el) {
        var bad = el.type === 'checkbox' ? !el.checked : !el.value.trim() || (el.type === 'email' && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(el.value));
        el.setAttribute('aria-invalid', bad ? 'true' : 'false'); if (bad) ok = false;
      });
      if (!ok) { say(form.dataset.req, false); var first = form.querySelector('[aria-invalid="true"]'); if (first) first.focus(); }
      return ok;
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.querySelector('[name="_gotcha"]').value) return; // bot
      if (!valid()) return;
      var data = new FormData(form), endpoint = form.dataset.endpoint;
      if (endpoint && form.dataset.key) { data.append('access_key', form.dataset.key); data.append('subject', form.dataset.subject); data.append('from_name', 'Sahm Alkarar Company website'); }
      if (!endpoint) {
        var lines = []; ['name', 'organization', 'email', 'phone', 'division'].forEach(function (k) { if (data.get(k)) lines.push(k + ': ' + data.get(k)); });
        var body = lines.join('\n') + '\n\n' + data.get('message');
        location.href = 'mailto:' + form.getAttribute('action').replace('mailto:', '') + '?subject=' + encodeURIComponent(form.dataset.subject) + '&body=' + encodeURIComponent(body);
        return;
      }
      btn.disabled = true; say(form.dataset.sending, true);
      fetch(endpoint, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
        .then(function (r) { if (!r.ok) throw new Error(r.status); form.reset(); say(form.dataset.ok, true); })
        .catch(function () { say(form.dataset.err, false); })
        .then(function () { btn.disabled = false; });
    });
  });
})();

// Screenshot pop-up: open in an in-page dialog (X, Esc or click outside to close). Without JS the links open the image.
(function () {
  var dlg = document.getElementById('lightbox');
  if (!dlg || typeof dlg.showModal !== 'function') return;
  var img = dlg.querySelector('img');
  document.querySelectorAll('a.win[data-full]').forEach(function (a) {
    a.removeAttribute('target');
    a.addEventListener('click', function (e) {
      e.preventDefault();
      var thumb = a.querySelector('img');
      img.src = a.dataset.full; img.alt = thumb ? thumb.alt : '';
      dlg.showModal();
    });
  });
  dlg.querySelector('.lb-x').addEventListener('click', function () { dlg.close(); });
  dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
})();

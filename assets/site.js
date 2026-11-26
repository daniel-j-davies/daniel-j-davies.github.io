/* Shared navigation + footer for danieldavies.co.
   To add or rename a page in the menu, edit the PAGES list below — once. */
(function () {
  var PAGES = [
    ['index.html', 'Home'],
    ['bio.html', 'Bio'],
    ['research.html', 'Research'],
    ['teaching.html', 'Teaching'],
    ['publications.html', 'Publications'],
    ['resources.html', 'Resources'],
    ['cv.html', 'CV'],
    ['contact.html', 'Contact']
  ];
  // Pages that live "under" a menu item keep that item highlighted.
  var PARENT = {
    'manuscript-research.html': 'resources.html',
    'medieval-research.html': 'resources.html',
    'academic-writing.html': 'resources.html'
  };

  var page = location.pathname.split('/').pop() || 'index.html';
  if (page.indexOf('.') === -1) page += '.html';
  var current = PARENT[page] || page;

  var links = PAGES.map(function (p) {
    var on = p[0] === current;
    return '<li><a href="' + p[0] + '"' + (on ? ' class="active" aria-current="page"' : '') + '>' + p[1] + '</a></li>';
  }).join('');

  var header =
    '<a class="skip-link" href="#main">Skip to content</a>' +
    '<header class="nav-container"><div class="nav-content">' +
    '<a href="index.html" class="nav-brand">Daniel Davies</a>' +
    '<nav aria-label="Main"><ul class="nav-links" id="navLinks">' + links + '</ul></nav>' +
    '<button class="mobile-menu-button" id="mobileMenuButton" type="button" aria-controls="navLinks" aria-expanded="false" aria-label="Open navigation menu">☰</button>' +
    '</div></header>';

  document.currentScript.insertAdjacentHTML('beforebegin', header);

  document.addEventListener('DOMContentLoaded', function () {
    var nav = document.getElementById('navLinks');
    var btn = document.getElementById('mobileMenuButton');

    function setOpen(open) {
      nav.classList.toggle('active', open);
      btn.textContent = open ? '✕' : '☰';
      btn.setAttribute('aria-expanded', String(open));
      btn.setAttribute('aria-label', open ? 'Close navigation menu' : 'Open navigation menu');
    }
    btn.addEventListener('click', function () { setOpen(!nav.classList.contains('active')); });
    document.addEventListener('click', function (e) { if (!e.target.closest('.nav-content')) setOpen(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { setOpen(false); btn.focus(); } });
    window.addEventListener('resize', function () { if (window.innerWidth > 768) setOpen(false); });

    var footer = document.createElement('footer');
    footer.className = 'footer';
    footer.innerHTML = '<div class="footer-content"><p>&copy; ' + new Date().getFullYear() + ' Daniel Davies. All rights reserved.</p></div>';
    document.body.appendChild(footer);
  });
})();

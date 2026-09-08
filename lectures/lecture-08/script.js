// Shared navigation for the split (multi-file) slide deck.
// Each slide page sets data-prev / data-next on <body> (see below);
// this script just wires up keyboard and swipe navigation between real pages.
(function () {
  var prevUrl = document.body.getAttribute('data-prev');
  var nextUrl = document.body.getAttribute('data-next');

  document.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowLeft' || e.key === ' ' || e.key === 'PageDown') {
      if (nextUrl) { e.preventDefault(); window.location.href = nextUrl; }
    }
    if (e.key === 'ArrowRight' || e.key === 'PageUp') {
      if (prevUrl) { e.preventDefault(); window.location.href = prevUrl; }
    }
  });

  var touchStart = 0;
  document.addEventListener('touchstart', function (e) { touchStart = e.touches[0].clientX; });
  document.addEventListener('touchend', function (e) {
    var diff = touchStart - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 50) {
      if (diff > 0 && prevUrl) window.location.href = prevUrl;
      if (diff < 0 && nextUrl) window.location.href = nextUrl;
    }
  });
})();

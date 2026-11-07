(() => {
  const audioPlayers = Array.from(document.querySelectorAll('audio'));
  for (const player of audioPlayers) {
    player.addEventListener('play', () => {
      for (const other of audioPlayers) {
        if (other !== player) other.pause();
      }
    });
  }
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (!reduce.matches && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          entry.target.classList.add('entering');
          observer.unobserve(entry.target);
        }
      }
    }, { threshold: 0.08 });
    document.querySelectorAll('.section-head h2,.section-head>p,.scene-heading,.scene-picture,.word-definition,.cast-listen,.publish-cover-heading').forEach(element => observer.observe(element));
    reduce.addEventListener('change', () => {
      if (reduce.matches) observer.disconnect();
    });
  }
})();

/**
 * Hero Background Video Controller
 * Ensures robust autoplay, graceful poster fallback, and user pause/play interaction.
 */
document.addEventListener('DOMContentLoaded', function () {
  const video = document.getElementById('heroBgVideo');
  const toggleBtn = document.getElementById('heroVideoToggle');
  const pulseDot = document.getElementById('videoPulseDot');
  if (!video) return;

  // Modern browsers require muted for autoplay
  video.muted = true;
  video.setAttribute('muted', '');
  video.setAttribute('playsinline', '');

  const startAutoplay = function () {
    const playPromise = video.play();
    if (playPromise !== undefined) {
      playPromise
        .then(function () {
          if (pulseDot) pulseDot.style.display = 'inline-block';
        })
        .catch(function () {
          // If browser policy prevented autoplay on page load, play upon first user interaction
          const unlockAutoplay = function () {
            video.play();
            document.removeEventListener('click', unlockAutoplay);
            document.removeEventListener('touchstart', unlockAutoplay);
            document.removeEventListener('scroll', unlockAutoplay);
          };
          document.addEventListener('click', unlockAutoplay, { once: true });
          document.addEventListener('touchstart', unlockAutoplay, { once: true });
          document.addEventListener('scroll', unlockAutoplay, { once: true });
        });
    }
  };

  startAutoplay();

  if (toggleBtn) {
    const pauseIcon = toggleBtn.querySelector('.toggle-pause-icon');
    const playIcon = toggleBtn.querySelector('.toggle-play-icon');

    toggleBtn.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();

      if (video.paused) {
        video.play();
        if (pauseIcon) pauseIcon.style.display = 'block';
        if (playIcon) playIcon.style.display = 'none';
        if (pulseDot) pulseDot.style.opacity = '1';
        toggleBtn.setAttribute('aria-label', 'Pause background video');
      } else {
        video.pause();
        if (pauseIcon) pauseIcon.style.display = 'none';
        if (playIcon) playIcon.style.display = 'block';
        if (pulseDot) pulseDot.style.opacity = '0.35';
        toggleBtn.setAttribute('aria-label', 'Play background video');
      }
    });
  }
});

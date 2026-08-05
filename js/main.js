// Mobile nav toggle (ready for later)
const navToggle = document.querySelector('.nav__toggle');
navToggle?.addEventListener('click', () => {
  const expanded = navToggle.getAttribute('aria-expanded') === 'true';
  navToggle.setAttribute('aria-expanded', String(!expanded));
  document.querySelector('.nav__links').classList.toggle('is-open');
});

// Simple reveal-on-scroll (IntersectionObserver — performant)
const reveals = document.querySelectorAll('.card, .blog-card, .topic-chip, .section__header');
if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) {
        e.target.classList.add('is-visible');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.1 });
  reveals.forEach((el) => io.observe(el));
}

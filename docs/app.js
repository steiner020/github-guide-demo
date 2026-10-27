(function () {
  const input = document.getElementById('doc-search');
  if (!input) return;
  const links = [...document.querySelectorAll('#doc-nav a')];
  const cards = [...document.querySelectorAll('.card[data-search]')];
  const sections = [...document.querySelectorAll('.article section')];

  input.addEventListener('input', () => {
    const q = input.value.trim().toLowerCase();
    links.forEach((a) => a.classList.toggle('hidden', Boolean(q) && !a.textContent.toLowerCase().includes(q)));
    cards.forEach((c) => {
      const haystack = (c.textContent + ' ' + c.dataset.search).toLowerCase();
      c.classList.toggle('hidden', Boolean(q) && !haystack.includes(q));
    });
    sections.forEach((s) => {
      s.classList.toggle('hidden', Boolean(q) && !s.textContent.toLowerCase().includes(q));
    });
  });
})();

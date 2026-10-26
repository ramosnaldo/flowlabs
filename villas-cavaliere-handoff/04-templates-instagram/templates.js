// Ajusta a escala das peças à tela, liga as guias e o modo ?exportar.
(function () {
  const raiz = document.documentElement;
  const params = new URLSearchParams(location.search);
  if (params.has('exportar')) raiz.classList.add('exportar');

  const grao =
    '<svg class="grao" aria-hidden="true"><filter id="vcg"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter><rect width="100%" height="100%" filter="url(#vcg)"/></svg>';
  document.querySelectorAll('.peca').forEach((p) => p.insertAdjacentHTML('beforeend', grao));

  function ajustar() {
    if (raiz.classList.contains('exportar')) {
      raiz.style.setProperty('--escala', 1);
      return;
    }
    document.querySelectorAll('.moldura').forEach((m) => {
      const w = Number(getComputedStyle(m).getPropertyValue('--w'));
      const h = Number(getComputedStyle(m).getPropertyValue('--h'));
      const porLargura = (window.innerWidth - 48) / w;
      const porAltura = (window.innerHeight - 140) / h;
      const alvo = Number(m.dataset.escala || 0.42);
      m.style.setProperty('--escala', Math.min(alvo, porLargura, Math.max(porAltura, 0.2)));
    });
  }
  ajustar();
  addEventListener('resize', ajustar);

  const guias = document.getElementById('guias');
  if (guias) {
    guias.addEventListener('change', () => raiz.classList.toggle('guias', guias.checked));
  }
})();

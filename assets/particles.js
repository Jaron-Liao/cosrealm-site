// ====== 龙奕学院 Universal Particle Engine ======
(function() {
  const canvas = document.createElement('canvas');
  canvas.className = 'particle-canvas';
  document.body.prepend(canvas);
  const ctx = canvas.getContext('2d');

  let W, H;
  let particles = [];
  let mouse = { x: -1000, y: -1000 };

  const PARTICLE_COUNT = 80;
  const CONNECTION_DIST = 150;

  function resize() {
    W = canvas.width = window.innerWidth;
    H = canvas.height = document.documentElement.scrollHeight;
  }

  function getComputedColors() {
    const style = getComputedStyle(document.documentElement);
    return [
      style.getPropertyValue('--particle-color-1').trim() || '#ffffff',
      style.getPropertyValue('--particle-color-2').trim() || '#aaaaaa',
      style.getPropertyValue('--particle-color-3').trim() || '#888888'
    ];
  }

  class Particle {
    constructor() {
      this.reset();
    }

    reset() {
      this.x = Math.random() * W;
      this.y = Math.random() * H;
      this.vx = (Math.random() - 0.5) * 0.8;
      this.vy = (Math.random() - 0.5) * 0.8;
      this.size = Math.random() * 3 + 1;
      const colors = getComputedColors();
      this.color = colors[Math.floor(Math.random() * colors.length)];
      this.opacity = Math.random() * 0.6 + 0.2;
    }

    update() {
      this.x += this.vx;
      this.y += this.vy;

      if (this.x < -20) this.x = W + 20;
      if (this.x > W + 20) this.x = -20;
      if (this.y < -20) this.y = H + 20;
      if (this.y > H + 20) this.y = -20;

      // Mouse interaction
      const dx = mouse.x - this.x;
      const dy = mouse.y - this.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      if (dist < 120) {
        const force = (120 - dist) / 120;
        this.x -= dx * force * 0.02;
        this.y -= dy * force * 0.02;
      }
    }

    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fillStyle = this.color;
      ctx.globalAlpha = this.opacity;
      ctx.fill();

      // Glow
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size * 3, 0, Math.PI * 2);
      ctx.fillStyle = this.color;
      ctx.globalAlpha = this.opacity * 0.15;
      ctx.fill();

      ctx.globalAlpha = 1;
    }
  }

  function init() {
    resize();
    particles = [];
    for (let i = 0; i < PARTICLE_COUNT; i++) {
      particles.push(new Particle());
    }
  }

  function drawConnections() {
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < CONNECTION_DIST) {
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.strokeStyle = particles[i].color;
          ctx.globalAlpha = (1 - dist / CONNECTION_DIST) * 0.15;
          ctx.lineWidth = 0.5;
          ctx.stroke();
          ctx.globalAlpha = 1;
        }
      }
    }
  }

  function animate() {
    ctx.clearRect(0, 0, W, H);
    drawConnections();
    particles.forEach(p => {
      p.update();
      p.draw();
    });
    requestAnimationFrame(animate);
  }

  // Scroll handler - update canvas height
  let scrollTimeout;
  window.addEventListener('scroll', () => {
    clearTimeout(scrollTimeout);
    scrollTimeout = setTimeout(() => {
      H = canvas.height = document.documentElement.scrollHeight;
    }, 200);
  });

  window.addEventListener('resize', init);
  window.addEventListener('mousemove', (e) => {
    mouse.x = e.clientX;
    mouse.y = e.clientY + window.scrollY;
  });

  // Re-init on color change
  const observer = new MutationObserver(() => {
    particles.forEach(p => {
      const colors = getComputedColors();
      p.color = colors[Math.floor(Math.random() * colors.length)];
    });
  });
  observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });

  init();
  animate();

  // Re-init when height changes significantly
  setInterval(() => {
    const newH = document.documentElement.scrollHeight;
    if (Math.abs(H - newH) > 100) {
      H = canvas.height = newH;
    }
  }, 1000);
})();

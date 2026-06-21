// ================================================================
// 龙奕学院 · 特效运行时 v4.0 — Effects Runtime    
// 粒子画布、光标光晕、点击爆炸、滚动显形、倾斜卡片、数字雨
// ================================================================
(function() {
  'use strict';

  // ===== 粒子画布 =====
  const canvas = document.createElement('canvas');
  canvas.id = 'fx-particle-canvas';
  document.body.prepend(canvas);
  const ctx = canvas.getContext('2d');

  let particles = [];
  let W, H;

  function resize() {
    W = canvas.width = window.innerWidth;
    H = canvas.height = Math.max(document.documentElement.scrollHeight, window.innerHeight);
  }
  resize();
  window.addEventListener('resize', () => {
    resize();
    initParticles();
  });
  window.addEventListener('scroll', () => {
    H = Math.max(document.documentElement.scrollHeight, window.innerHeight);
    canvas.height = H;
  });

  function initParticles() {
    particles = [];
    const count = Math.min(Math.floor((W * H) / 15000), 120);
    for (let i = 0; i < count; i++) {
      particles.push({
        x: Math.random() * W,
        y: Math.random() * H,
        r: Math.random() * 2 + 0.5,
        vx: (Math.random() - 0.5) * 0.3,
        vy: (Math.random() - 0.5) * 0.3,
        alpha: Math.random() * 0.4 + 0.1,
        pulse: Math.random() * Math.PI * 2,
        pulseSpeed: 0.005 + Math.random() * 0.02
      });
    }
  }
  initParticles();

  // 连线距离
  const linkDist = 120;

  function drawParticles() {
    ctx.clearRect(0, 0, W, H);

    const accent = getComputedStyle(document.documentElement).getPropertyValue('--accent').trim() || '#6366f1';

    particles.forEach((p, i) => {
      p.x += p.vx;
      p.y += p.vy;
      p.pulse += p.pulseSpeed;

      // 边缘环绕
      if (p.x < 0) p.x = W;
      if (p.x > W) p.x = 0;
      if (p.y < 0) p.y = H;
      if (p.y > H) p.y = 0;

      const currentAlpha = p.alpha * (0.6 + 0.4 * Math.sin(p.pulse));

      // 绘制粒子
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = accent;
      ctx.globalAlpha = currentAlpha;
      ctx.fill();

      // 连线
      for (let j = i + 1; j < particles.length; j++) {
        const q = particles[j];
        const dx = p.x - q.x;
        const dy = p.y - q.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < linkDist) {
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(q.x, q.y);
          ctx.strokeStyle = accent;
          ctx.globalAlpha = (1 - dist / linkDist) * 0.1 * currentAlpha;
          ctx.lineWidth = 0.5;
          ctx.stroke();
        }
      }
    });
    ctx.globalAlpha = 1;
    requestAnimationFrame(drawParticles);
  }
  drawParticles();

  // ===== 光标光晕 =====
  const cursorGlow = document.createElement('div');
  cursorGlow.className = 'cursor-glow';
  document.body.prepend(cursorGlow);

  let mouseX = -500, mouseY = -500;
  document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    cursorGlow.style.transform = `translate(${mouseX}px, ${mouseY}px) translate(-50%, -50%)`;
    cursorGlow.style.opacity = '0.15';
  });
  document.addEventListener('mouseleave', () => {
    cursorGlow.style.opacity = '0';
  });

  // ===== 点击粒子爆炸 =====
  document.addEventListener('click', (e) => {
    const container = document.createElement('div');
    container.className = 'particle-burst';
    container.style.left = e.clientX + 'px';
    container.style.top = e.clientY + 'px';
    document.body.appendChild(container);

    const accent = getComputedStyle(document.documentElement).getPropertyValue('--accent').trim() || '#6366f1';
    const count = 12;

    for (let i = 0; i < count; i++) {
      const particle = document.createElement('div');
      particle.className = 'explosion-particle';
      const angle = (Math.PI * 2 * i) / count;
      const distance = 30 + Math.random() * 50;
      const tx = Math.cos(angle) * distance;
      const ty = Math.sin(angle) * distance;
      particle.style.cssText = `
        width: ${4 + Math.random() * 4}px;
        height: ${4 + Math.random() * 4}px;
        background: ${accent};
        --tx: ${tx}px;
        --ty: ${ty}px;
        animation-delay: ${Math.random() * 0.15}s;
      `;
      container.appendChild(particle);
    }

    setTimeout(() => container.remove(), 1200);
  });

  // ===== 滚动显形 (Intersection Observer) =====
  const revealElements = document.querySelectorAll('.reveal');
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -50px 0px' });

  const existingReveals = document.querySelectorAll('.reveal');
  existingReveals.forEach(el => revealObserver.observe(el));

  // 为动态添加的元素建立 MutationObserver
  const revealMutObserver = new MutationObserver((mutations) => {
    mutations.forEach(mut => {
      mut.addedNodes.forEach(node => {
        if (node.nodeType === 1) {
          if (node.classList && node.classList.contains('reveal')) {
            revealObserver.observe(node);
          }
          if (node.querySelectorAll) {
            node.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));
          }
        }
      });
    });
  });
  revealMutObserver.observe(document.body, { childList: true, subtree: true });

  // ===== 3D 倾斜卡片 =====
  document.addEventListener('mousemove', (e) => {
    const tilts = document.querySelectorAll('.card-tilt');
    tilts.forEach(card => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      const rotateX = ((y - centerY) / centerY) * -8;
      const rotateY = ((x - centerX) / centerX) * 8;
      card.style.transform = `perspective(800px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    });
  });

  // ===== 按钮波纹 =====
  document.addEventListener('click', (e) => {
    const btn = e.target.closest('.btn-ripple');
    if (!btn) return;
    const rect = btn.getBoundingClientRect();
    const ripple = document.createElement('span');
    ripple.className = 'ripple-effect-inner';
    const size = Math.max(rect.width, rect.height);
    ripple.style.width = ripple.style.height = size + 'px';
    ripple.style.left = (e.clientX - rect.left - size / 2) + 'px';
    ripple.style.top = (e.clientY - rect.top - size / 2) + 'px';
    btn.appendChild(ripple);
    setTimeout(() => ripple.remove(), 600);
  });

  // ===== 滚动进度条 =====
  const progressBar = document.createElement('div');
  progressBar.className = 'scroll-progress-bar';
  document.body.appendChild(progressBar);
  window.addEventListener('scroll', () => {
    const h = document.documentElement.scrollHeight - window.innerHeight;
    const scrollPercent = h > 0 ? (window.scrollY / h) * 100 : 0;
    progressBar.style.width = scrollPercent + '%';
  });

  // ===== 数字增长计数器 =====
  function animateCounters() {
    const counters = document.querySelectorAll('.counter-up');
    counters.forEach(el => {
      if (el.dataset.counted) return;
      el.dataset.counted = '1';
      const target = parseInt(el.textContent.replace(/[^0-9]/g, ''), 10);
      if (isNaN(target)) return;
      const suffix = el.textContent.replace(/[0-9,.]/g, '').trim();
      const duration = 1500;
      const start = performance.now();

      function update(ts) {
        const elapsed = ts - start;
        const progress = Math.min(elapsed / duration, 1);
        // easeOutExpo
        const val = progress === 1 ? target : target * (1 - Math.pow(2, -10 * progress));
        el.textContent = Math.floor(val).toLocaleString() + suffix;
        if (progress < 1) requestAnimationFrame(update);
      }
      requestAnimationFrame(update);
    });
  }

  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounters();
        counterObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });

  document.querySelectorAll('.counter-up').forEach(el => counterObserver.observe(el));

  // ===== 交错入场（给 stagger-in 的子元素加延迟） =====
  function initStaggerIn() {
    document.querySelectorAll('.stagger-in').forEach(container => {
      if (container.dataset.staggered) return;
      container.dataset.staggered = '1';
      Array.from(container.children).forEach((child, i) => {
        child.style.animationDelay = (i * 0.08) + 's';
      });
    });
  }
  initStaggerIn();

  // ===== 数字雨效果(仅对 .digital-rain-container) =====
  function spawnDigitalRain(container) {
    const chars = '龙奕学院二次元宇宙アイウエオカキクケコサシスセソタチツテトナニヌネノ01';
    const width = container.offsetWidth;
    const cols = Math.floor(width / 20);
    
    function createRain() {
      for (let i = 0; i < cols; i++) {
        const drop = document.createElement('span');
        drop.className = 'digital-rain';
        drop.style.left = (i * 20 + Math.random() * 10) + 'px';
        drop.style.animationDelay = Math.random() * 2 + 's';
        drop.style.animationDuration = (1 + Math.random() * 2) + 's';
        drop.textContent = chars[Math.floor(Math.random() * chars.length)];
        container.appendChild(drop);
        setTimeout(() => drop.remove(), 3000);
      }
    }
    createRain();
    setInterval(createRain, 1500);
  }

  document.querySelectorAll('.digital-rain-container').forEach(spawnDigitalRain);

  // ===== 暴露全局API =====
  window.LongYiFX = {
    initStaggerIn,
    animateCounters,
    resize,
    revealObserver
  };

  // ===== 页面加载完成后的初始化 =====
  window.addEventListener('DOMContentLoaded', () => {
    initStaggerIn();
  });

  // ===== 磁吸悬停效果 (Magnetic Hover) =====
  document.querySelectorAll('.magnetic').forEach(el => {
    el.addEventListener('mousemove', (e) => {
      const rect = el.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      el.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px)`;
    });
    el.addEventListener('mouseleave', () => {
      el.style.transform = 'translate(0, 0)';
    });
  });

  // ===== 极光渐变球 =====
  document.querySelectorAll('.gradient-orb-container').forEach(container => {
    const orbs = [
      { color: 'rgba(255,107,157,0.15)', size: 300, x: 20, y: 30 },
      { color: 'rgba(99,102,241,0.12)', size: 250, x: 70, y: 50 },
      { color: 'rgba(34,211,238,0.1)', size: 200, x: 50, y: 20 }
    ];
    orbs.forEach(orb => {
      const div = document.createElement('div');
      div.className = 'gradient-orb';
      div.style.cssText = `width:${orb.size}px;height:${orb.size}px;background:${orb.color};left:${orb.x}%;top:${orb.y}%`;
      container.appendChild(div);
    });
  });

  // ===== 卡牌光扫 (Card Light Sweep) =====
  document.querySelectorAll('.card-light-sweep').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = ((e.clientX - rect.left) / rect.width) * 100;
      const y = ((e.clientY - rect.top) / rect.height) * 100;
      card.style.setProperty('--mx', x + '%');
      card.style.setProperty('--my', y + '%');
      card.style.background = `radial-gradient(circle at ${x}% ${y}%, rgba(255,255,255,0.08) 0%, transparent 50%), var(--bg-card, #fff)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.background = '';
    });
  });

  // ===== 背景流星 =====
  let shootingStars = [];
  function createShootingStar() {
    if (shootingStars.length > 3) return;
    const star = document.createElement('div');
    const startX = Math.random() * window.innerWidth;
    const startY = Math.random() * window.innerHeight * 0.5;
    const angle = -20 + Math.random() * 40;
    const dist = 200 + Math.random() * 300;
    star.style.cssText = `
      position: fixed; left: ${startX}px; top: ${startY}px; pointer-events: none; z-index: 1;
      width: ${60 + Math.random() * 100}px; height: 1px;
      background: linear-gradient(90deg, transparent, rgba(167,139,250,0.6), rgba(255,255,255,0.8));
      transform: rotate(${angle}deg); border-radius: 50%;
      animation: shootingStar ${1 + Math.random() * 1.5}s linear forwards;
      opacity: 0;
    `;
    document.body.appendChild(star);
    shootingStars.push(star);
    setTimeout(() => { star.remove(); shootingStars = shootingStars.filter(s => s !== star) }, 3000);
  }
  setInterval(() => { if (Math.random() < 0.3) createShootingStar() }, 4000);
  createShootingStar();

  // ===== 键盘音效视觉反馈 =====
  document.addEventListener('keydown', (e) => {
    const activeEl = document.activeElement;
    if (!activeEl || activeEl.tagName === 'INPUT' || activeEl.tagName === 'TEXTAREA') {
      // 在输入框时不做视觉反馈
      return;
    }
    if (e.key === 'Enter' || e.key === 'Escape' || e.key === ' ') {
      const dot = document.createElement('div');
      dot.style.cssText = `
        position: fixed; width: 8px; height: 8px; border-radius: 50%;
        background: var(--accent, #6366f1); pointer-events: none; z-index: 9999;
        left: ${50 + Math.random() * 20}%; top: ${50 + Math.random() * 20}%;
        opacity: 0.5; animation: explodeOut 0.8s ease-out forwards;
      `;
      document.body.appendChild(dot);
      setTimeout(() => dot.remove(), 800);
    }
  });

})();

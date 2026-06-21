/**
 * 量子全息动态背景 v5.0 - 确保显示版
 * 纯 Canvas2D 渲染，零依赖，100% 确保显示
 * 效果：粒子星海 + 量子光线 + 鼠标互动 + 震动感
 */
(function() {
  "use strict";

  const CONFIG = {
    particleCount: 180,
    lineDistance: 140,
    mouseRadius: 200,
    glowIntensity: 0.8,
    shakeIntensity: 2.5,
    shakeSpeed: 0.06,
    colors: [
      [0, 200, 255],    // 量子蓝
      [0, 255, 180],    // 全息绿
      [180, 0, 255],    // 虚空紫
      [255, 100, 0],     // 熔岩橙
      [255, 0, 120],     // 霓虹粉
      [0, 255, 255],     // 青色
    ]
  };

  let canvas, ctx, particles, mouse, animId;
  let w, h, dpr;
  let time = 0;
  let shakeX = 0, shakeY = 0;

  function init() {
    // 创建 canvas
    let old = document.getElementById("qbg-canvas");
    if (old) old.remove();

    canvas = document.createElement("canvas");
    canvas.id = "qbg-canvas";
    Object.assign(canvas.style, {
      position: "fixed",
      top: "0px",
      left: "0px",
      width: "100vw",
      height: "100vh",
      zIndex: "-1",
      pointerEvents: "none",
      display: "block",
    });
    // 插入到 body 最底层
    if (document.body) {
      document.body.insertBefore(canvas, document.body.firstChild);
    } else {
      document.addEventListener("DOMContentLoaded", () => {
        document.body.insertBefore(canvas, document.body.firstChild);
      });
    }

    ctx = canvas.getContext("2d");
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    resize();
    window.addEventListener("resize", resize);

    // 鼠标追踪
    mouse = { x: -9999, y: -9999 };
    window.addEventListener("mousemove", (e) => {
      mouse.x = e.clientX * dpr;
      mouse.y = e.clientY * dpr;
    });
    window.addEventListener("touchmove", (e) => {
      if (e.touches.length > 0) {
        mouse.x = e.touches[0].clientX * dpr;
        mouse.y = e.touches[0].clientY * dpr;
      }
    }, { passive: true });

    initParticles();
    animate();
  }

  function resize() {
    w = window.innerWidth;
    h = window.innerHeight;
    canvas.width = w * dpr;
    canvas.height = h * dpr;
    canvas.style.width = w + "px";
    canvas.style.height = h + "px";
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function initParticles() {
    particles = [];
    for (let i = 0; i < CONFIG.particleCount; i++) {
      particles.push({
        x: Math.random() * w,
        y: Math.random() * h,
        vx: (Math.random() - 0.5) * 0.5,
        vy: (Math.random() - 0.5) * 0.5,
        r: Math.random() * 2 + 0.5,
        color: CONFIG.colors[Math.floor(Math.random() * CONFIG.colors.length)],
        alpha: Math.random() * 0.6 + 0.3,
        phase: Math.random() * Math.PI * 2,
      });
    }
  }

  function animate() {
    time += CONFIG.shakeSpeed;

    // 震动效果
    shakeX = Math.sin(time * 1.7) * CONFIG.shakeIntensity * (0.5 + 0.5 * Math.sin(time * 0.3));
    shakeY = Math.cos(time * 2.3) * CONFIG.shakeIntensity * (0.5 + 0.5 * Math.cos(time * 0.4));

    ctx.save();
    ctx.translate(shakeX, shakeY);

    // 清除画布 - 深色半透明实现拖尾效果
    ctx.globalCompositeOperation = "source-over";
    ctx.fillStyle = "rgba(2, 2, 8, 0.25)";
    ctx.fillRect(-10, -10, w + 20, h + 20);

    // 绘制背景网格（全息扫描线）
    drawGrid();

    // 绘制量子光线
    drawQuantumRays();

    // 更新和绘制粒子
    updateAndDrawParticles();

    // 绘制粒子间连线
    drawParticleLines();

    // 绘制鼠标光晕
    drawMouseGlow();

    ctx.restore();
    animId = requestAnimationFrame(animate);
  }

  function drawGrid() {
    ctx.strokeStyle = "rgba(0, 200, 255, 0.04)";
    ctx.lineWidth = 0.5;
    const spacing = 60;
    const offsetX = (time * 0.5) % spacing;
    const offsetY = (time * 0.3) % spacing;

    for (let x = -spacing + offsetX; x < w + spacing; x += spacing) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, h);
      ctx.stroke();
    }
    for (let y = -spacing + offsetY; y < h + spacing; y += spacing) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(w, y);
      ctx.stroke();
    }

    // 扫描线
    const scanY = (time * 2.5) % (h + 100) - 50;
    const scanGrad = ctx.createLinearGradient(0, scanY - 40, 0, scanY + 40);
    scanGrad.addColorStop(0, "rgba(0, 200, 255, 0)");
    scanGrad.addColorStop(0.5, "rgba(0, 200, 255, 0.08)");
    scanGrad.addColorStop(1, "rgba(0, 200, 255, 0)");
    ctx.fillStyle = scanGrad;
    ctx.fillRect(0, scanY - 40, w, 80);
  }

  function drawQuantumRays() {
    const cx = w / 2 + Math.sin(time * 0.2) * w * 0.3;
    const cy = h / 2 + Math.cos(time * 0.15) * h * 0.2;

    for (let i = 0; i < 5; i++) {
      const angle = (i / 5) * Math.PI * 2 + time * 0.15;
      const len = 200 + Math.sin(time + i) * 150;
      const ex = cx + Math.cos(angle) * len;
      const ey = cy + Math.sin(angle) * len;

      const grad = ctx.createLinearGradient(cx, cy, ex, ey);
      const c = CONFIG.colors[i % CONFIG.colors.length];
      grad.addColorStop(0, "rgba(" + c[0] + "," + c[1] + "," + c[2] + ",0.15)");
      grad.addColorStop(1, "rgba(" + c[0] + "," + c[1] + "," + c[2] + ",0)");

      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(ex, ey);
      ctx.strokeStyle = grad;
      ctx.lineWidth = 1.5 + Math.sin(time + i) * 0.8;
      ctx.stroke();
    }

    // 中心光晕
    const glow = ctx.createRadialGradient(cx, cy, 0, cx, cy, 120);
    glow.addColorStop(0, "rgba(0, 200, 255, 0.12)");
    glow.addColorStop(0.5, "rgba(100, 0, 255, 0.04)");
    glow.addColorStop(1, "rgba(0, 0, 0, 0)");
    ctx.fillStyle = glow;
    ctx.fillRect(cx - 120, cy - 120, 240, 240);
  }

  function updateAndDrawParticles() {
    particles.forEach(p => {
      // 更新位置
      p.x += p.vx + Math.sin(time + p.phase) * 0.2;
      p.y += p.vy + Math.cos(time + p.phase) * 0.2;

      // 边界循环
      if (p.x < -20) p.x = w + 20;
      if (p.x > w + 20) p.x = -20;
      if (p.y < -20) p.y = h + 20;
      if (p.y > h + 20) p.y = -20;

      // 鼠标吸引
      const dx = mouse.x / dpr - p.x;
      const dy = mouse.y / dpr - p.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      if (dist < CONFIG.mouseRadius) {
        const force = (1 - dist / CONFIG.mouseRadius) * 0.03;
        p.vx += dx * force * 0.01;
        p.vy += dy * force * 0.01;
      }

      // 阻力
      p.vx *= 0.99;
      p.vy *= 0.99;

      // 绘制粒子光晕
      const pulse = 0.7 + 0.3 * Math.sin(time * 2 + p.phase);
      const [r, g, b] = p.color;
      const glowR = p.r * 3 * pulse;

      const grad = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, glowR);
      grad.addColorStop(0, "rgba(" + r + "," + g + "," + b + "," + (p.alpha * pulse) + ")");
      grad.addColorStop(0.5, "rgba(" + r + "," + g + "," + b + "," + (p.alpha * 0.3 * pulse) + ")");
      grad.addColorStop(1, "rgba(" + r + "," + g + "," + b + ",0)");
      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.arc(p.x, p.y, glowR, 0, Math.PI * 2);
      ctx.fill();

      // 绘制粒子核心
      ctx.fillStyle = "rgba(" + r + "," + g + "," + b + "," + p.alpha + ")";
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fill();
    });
  }

  function drawParticleLines() {
    ctx.lineWidth = 0.6;
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < CONFIG.lineDistance) {
          const alpha = (1 - dist / CONFIG.lineDistance) * 0.25;
          const [r, g, b] = particles[i].color;
          ctx.strokeStyle = "rgba(" + r + "," + g + "," + b + "," + alpha + ")";
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.stroke();
        }
      }
    }
  }

  function drawMouseGlow() {
    if (mouse.x < -999) return;
    const mx = mouse.x / dpr;
    const my = mouse.y / dpr;

    const grad = ctx.createRadialGradient(mx, my, 0, mx, my, CONFIG.mouseRadius);
    grad.addColorStop(0, "rgba(0, 200, 255, 0.08)");
    grad.addColorStop(0.5, "rgba(100, 0, 255, 0.03)");
    grad.addColorStop(1, "rgba(0, 0, 0, 0)");
    ctx.fillStyle = grad;
    ctx.fillRect(mx - CONFIG.mouseRadius, my - CONFIG.mouseRadius, CONFIG.mouseRadius * 2, CONFIG.mouseRadius * 2);
  }

  // 启动
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

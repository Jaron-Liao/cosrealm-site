/**
 * CosRealm 超炫3D动态背景引擎
 * Three.js 超现实主义风格
 * 流动粒子 + 体积光 + 霓虹网格 + 动态扭曲
 */
(function () {
  'use strict';

  // 已存在则跳过
  if (window.__cosrealmBg3D) return;
  window.__cosrealmBg3D = true;

  // 动态加载 Three.js
  function loadThreeJS(cb) {
    if (window.THREE) { cb(); return; }
    const s = document.createElement('script');
    s.src = 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js';
    s.onload = cb;
    s.onerror = function () {
      console.warn('[bg-3d] Three.js CDN failed, falling back to static gradient');
      initFallback();
    };
    document.head.appendChild(s);
  }

  // 降级方案：超渐变动态CSS背景
  function initFallback() {
    let canvas = document.getElementById('bg-canvas');
    if (!canvas) {
      canvas = document.createElement('canvas');
      canvas.id = 'bg-canvas';
      canvas.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;z-index:-2;pointer-events:none;';
      document.body.prepend(canvas);
    }
    // 用 CSS 动画渐变作为降级
    document.body.style.background = 'linear-gradient(135deg, #0a0a1a 0%, #1a0533 25%, #050520 50%, #0a0a1a 75%, #1a0533 100%)';
    document.body.style.backgroundSize = '400% 400%';
    document.body.style.animation = 'gradientShift 20s ease infinite';
    if (!document.getElementById('fallback-bg-style')) {
      const style = document.createElement('style');
      style.id = 'fallback-bg-style';
      style.textContent = `
        @keyframes gradientShift {
          0% { background-position: 0% 50%; }
          50% { background-position: 100% 50%; }
          100% { background-position: 0% 50%; }
        }
      `;
      document.head.appendChild(style);
    }
  }

  function initThree() {
    const THREE = window.THREE;
    if (!THREE) { initFallback(); return; }

    // 移除旧canvas
    const old = document.getElementById('bg-canvas');
    if (old) old.remove();

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 80;

    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setClearColor(0x000000, 0);
    renderer.domElement.id = 'bg-canvas';
    renderer.domElement.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;z-index:-2;pointer-events:none;';
    document.body.prepend(renderer.domElement);

    // 监听主题
    let isDark = !document.documentElement.classList.contains('theme-light');
    window.addEventListener('themeChange', function (e) {
      isDark = e.detail === 'dark';
    });

    // ========== 超现实主义粒子场 ==========
    const PARTICLE_COUNT = 5000;
    const particleGeo = new THREE.BufferGeometry();
    const positions = new Float32Array(PARTICLE_COUNT * 3);
    const colors = new Float32Array(PARTICLE_COUNT * 3);
    const sizes = new Float32Array(PARTICLE_COUNT);
    const phases = new Float32Array(PARTICLE_COUNT); // 相位

    const colorPalette = [
      new THREE.Color(0xFF6B35), // 活力橙
      new THREE.Color(0xff2d95), // 霓虹粉
      new THREE.Color(0x00f0ff), // 赛博青
      new THREE.Color(0x9d4dff), // 幻紫
      new THREE.Color(0xffd700), // 金
      new THREE.Color(0x00ff88), // 霓虹绿
    ];

    for (let i = 0; i < PARTICLE_COUNT; i++) {
      const i3 = i * 3;
      const r = 60 * Math.sqrt(Math.random());
      const theta = Math.random() * Math.PI * 2;
      const phi = Math.acos(2 * Math.random() - 1);

      positions[i3]     = r * Math.sin(phi) * Math.cos(theta);
      positions[i3 + 1] = r * Math.sin(phi) * Math.sin(theta);
      positions[i3 + 2] = r * Math.cos(phi);

      const c = colorPalette[Math.floor(Math.random() * colorPalette.length)];
      colors[i3]     = c.r;
      colors[i3 + 1] = c.g;
      colors[i3 + 2] = c.b;

      sizes[i] = Math.random() * 3 + 0.5;
      phases[i] = Math.random() * Math.PI * 2;
    }

    particleGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    particleGeo.setAttribute('color', new THREE.BufferAttribute(colors, 3));
    particleGeo.setAttribute('size', new THREE.BufferAttribute(sizes, 1));

    const particleMat = new THREE.ShaderMaterial({
      uniforms: {
        time: { value: 0 },
        pixelRatio: { value: renderer.getPixelRatio() },
      },
      vertexShader: `
        attribute float size;
        attribute vec3 color;
        varying vec3 vColor;
        varying float vAlpha;
        uniform float time;
        uniform float pixelRatio;
        void main() {
          vColor = color;
          vec3 pos = position;
          // 流动扭曲
          float wave1 = sin(pos.x * 0.02 + time * 0.5) * 3.0;
          float wave2 = cos(pos.y * 0.02 + time * 0.3) * 3.0;
          float wave3 = sin(pos.z * 0.02 + time * 0.7) * 2.0;
          pos.x += wave1 + wave3 * 0.5;
          pos.y += wave2;
          pos.z += wave1 * 0.3 - wave2 * 0.3;
          // 呼吸脉冲
          float pulse = sin(time * 0.8 + length(pos) * 0.05) * 0.5 + 0.5;
          vAlpha = 0.3 + pulse * 0.7;
          vec4 mvPosition = modelViewMatrix * vec4(pos, 1.0);
          gl_PointSize = size * pixelRatio * (120.0 / -mvPosition.z) * (0.5 + pulse * 0.5);
          gl_Position = projectionMatrix * mvPosition;
        }
      `,
      fragmentShader: `
        varying vec3 vColor;
        varying float vAlpha;
        void main() {
          // 圆形软粒子
          float d = length(gl_PointCoord - vec2(0.5));
          if (d > 0.5) discard;
          float alpha = (1.0 - d * 2.0) * vAlpha;
          gl_FragColor = vec4(vColor, alpha * 0.85);
        }
      `,
      transparent: true,
      depthWrite: false,
      blending: THREE.AdditiveBlending,
    });

    const particles = new THREE.Points(particleGeo, particleMat);
    scene.add(particles);

    // ========== 霓虹网格线框球体 ==========
    const gridGroup = new THREE.Group();
    const sphereGeo = new THREE.IcosahedronGeometry(35, 2);
    const wireframe = new THREE.WireframeGeometry(sphereGeo);
    const lineMat = new THREE.LineBasicMaterial({
      color: 0xFF6B35,
      transparent: true,
      opacity: 0.08,
      blending: THREE.AdditiveBlending,
    });
    const wireSphere = new THREE.LineSegments(wireframe, lineMat);
    gridGroup.add(wireSphere);

    // 第二层
    const sphereGeo2 = new THREE.IcosahedronGeometry(45, 1);
    const wireframe2 = new THREE.WireframeGeometry(sphereGeo2);
    const lineMat2 = new THREE.LineBasicMaterial({
      color: 0x9d4dff,
      transparent: true,
      opacity: 0.06,
      blending: THREE.AdditiveBlending,
    });
    const wireSphere2 = new THREE.LineSegments(wireframe2, lineMat2);
    gridGroup.add(wireSphere2);

    scene.add(gridGroup);

    // ========== 体积光射线 ==========
    const rayGroup = new THREE.Group();
    const rayCount = 8;
    for (let i = 0; i < rayCount; i++) {
      const angle = (i / rayCount) * Math.PI * 2;
      const rayGeo = new THREE.BufferGeometry();
      const rayLen = 80 + Math.random() * 40;
      const pts = new Float32Array(6);
      pts[0] = 0; pts[1] = 0; pts[2] = 0;
      pts[3] = Math.cos(angle) * rayLen;
      pts[4] = (Math.random() - 0.5) * 20;
      pts[5] = Math.sin(angle) * rayLen;

      rayGeo.setAttribute('position', new THREE.BufferAttribute(pts, 3));
      const rayMat = new THREE.LineBasicMaterial({
        color: colorPalette[i % colorPalette.length].getHex(),
        transparent: true,
        opacity: 0.04 + Math.random() * 0.04,
        blending: THREE.AdditiveBlending,
      });
      const ray = new THREE.Line(rayGeo, rayMat);
      ray.userData.baseOpacity = rayMat.opacity;
      rayGroup.add(ray);
    }
    scene.add(rayGroup);

    // ========== 漂浮几何碎片 ==========
    const debrisGroup = new THREE.Group();
    const debrisCount = 25;
    const debrisGeos = [
      new THREE.TetrahedronGeometry(0.8),
      new THREE.OctahedronGeometry(0.6),
      new THREE.IcosahedronGeometry(0.5),
      new THREE.TorusGeometry(0.5, 0.2, 8, 16),
    ];
    for (let i = 0; i < debrisCount; i++) {
      const geo = debrisGeos[Math.floor(Math.random() * debrisGeos.length)];
      const mat = new THREE.MeshBasicMaterial({
        color: colorPalette[Math.floor(Math.random() * colorPalette.length)].getHex(),
        transparent: true,
        opacity: 0.15 + Math.random() * 0.2,
        blending: THREE.AdditiveBlending,
        wireframe: Math.random() > 0.5,
      });
      const mesh = new THREE.Mesh(geo, mat);
      mesh.position.set(
        (Math.random() - 0.5) * 100,
        (Math.random() - 0.5) * 100,
        (Math.random() - 0.5) * 60,
      );
      mesh.userData = {
        rotSpeed: new THREE.Vector3(
          (Math.random() - 0.5) * 0.02,
          (Math.random() - 0.5) * 0.02,
          (Math.random() - 0.5) * 0.02,
        ),
        floatSpeed: Math.random() * 0.5 + 0.3,
        floatAmp: Math.random() * 5 + 2,
        phase: Math.random() * Math.PI * 2,
      };
      debrisGroup.add(mesh);
    }
    scene.add(debrisGroup);

    // ========== 中心光辉 ==========
    const glowGeo = new THREE.SphereGeometry(3, 32, 32);
    const glowMat = new THREE.MeshBasicMaterial({
      color: 0xFF6B35,
      transparent: true,
      opacity: 0.3,
      blending: THREE.AdditiveBlending,
    });
    const glow = new THREE.Mesh(glowGeo, glowMat);
    scene.add(glow);

    // 外层光晕
    const glow2Geo = new THREE.SphereGeometry(8, 32, 32);
    const glow2Mat = new THREE.MeshBasicMaterial({
      color: 0x9d4dff,
      transparent: true,
      opacity: 0.08,
      blending: THREE.AdditiveBlending,
      side: THREE.BackSide,
    });
    const glow2 = new THREE.Mesh(glow2Geo, glow2Mat);
    scene.add(glow2);

    // ========== 鼠标交互 ==========
    const mouse = { x: 0, y: 0, tx: 0, ty: 0 };
    window.addEventListener('mousemove', function (e) {
      mouse.tx = (e.clientX / window.innerWidth - 0.5) * 2;
      mouse.ty = -(e.clientY / window.innerHeight - 0.5) * 2;
    });

    // ========== 动画循环 ==========
    const clock = new THREE.Clock();
    let frame;

    function animate() {
      frame = requestAnimationFrame(animate);
      const t = clock.getElapsedTime();
      const dt = clock.getDelta();

      // 平滑鼠标
      mouse.x += (mouse.tx - mouse.x) * 0.05;
      mouse.y += (mouse.ty - mouse.y) * 0.05;

      // 粒子时间
      particleMat.uniforms.time.value = t;

      // 粒子场旋转
      particles.rotation.y = t * 0.03;
      particles.rotation.x = Math.sin(t * 0.02) * 0.1;

      // 网格球体旋转
      gridGroup.rotation.y = t * 0.05;
      gridGroup.rotation.x = Math.sin(t * 0.03) * 0.15;
      gridGroup.rotation.z = Math.cos(t * 0.02) * 0.05;

      // 体积光旋转
      rayGroup.rotation.y = t * 0.08;
      rayGroup.children.forEach(function (ray, i) {
        ray.material.opacity = ray.userData.baseOpacity *
          (0.5 + 0.5 * Math.sin(t * 0.5 + i * 0.8));
      });

      // 几何碎片
      debrisGroup.children.forEach(function (m) {
        m.rotation.x += m.userData.rotSpeed.x;
        m.rotation.y += m.userData.rotSpeed.y;
        m.rotation.z += m.userData.rotSpeed.z;
        m.position.y += Math.sin(t * m.userData.floatSpeed + m.userData.phase) * 0.02;
      });

      // 中心光辉脉冲
      const pulse = 0.2 + 0.15 * Math.sin(t * 1.5);
      glowMat.opacity = pulse;
      glow.scale.setScalar(1 + 0.2 * Math.sin(t * 1.5));
      glow2Mat.opacity = 0.05 + 0.05 * Math.cos(t * 0.8);

      // 相机跟随鼠标
      camera.position.x += (mouse.x * 10 - camera.position.x) * 0.03;
      camera.position.y += (mouse.y * 8 - camera.position.y) * 0.03;
      camera.lookAt(0, 0, 0);

      // 主题适配
      if (!isDark) {
        // 浅色模式降低强度
        renderer.domElement.style.opacity = '0.3';
      } else {
        renderer.domElement.style.opacity = '1';
      }

      renderer.render(scene, camera);
    }

    animate();

    // ========== 窗口resize ==========
    function onResize() {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
      particleMat.uniforms.pixelRatio.value = renderer.getPixelRatio();
    }
    window.addEventListener('resize', onResize);

    // ========== 公开停止方法 ==========
    window.__stopBg3D = function () {
      cancelAnimationFrame(frame);
      renderer.dispose();
      if (renderer.domElement.parentNode) {
        renderer.domElement.parentNode.removeChild(renderer.domElement);
      }
    };
  }

  // 启动
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { loadThreeJS(initThree); });
  } else {
    loadThreeJS(initThree);
  }
})();

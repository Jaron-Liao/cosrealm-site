/**
 * CosRealm 超现实3D动态背景引擎 v2.0
 * 技术栈：Three.js + 自定义Shader + 粒子系统 + 鼠标交互
 * 特性：火箭发射粒子流、霓虹网格、体积光、动态扭曲、PBR反射
 * 性能：LOD自适应 + requestAnimationFrame节流 + 滚动暂停
 */
(function () {
  'use strict';

  if (window.__cosrealmBgEngine) return;
  window.__cosrealmBgEngine = true;

  // ========== 配置 ==========
  const CONFIG = {
    particleCount: 6000,
    enableRocket: true,
    enableNeonGrid: true,
    enableVolumetricLight: true,
    enableDebris: true,
    enableMouseInteraction: true,
    pauseOnScroll: true,
    lodEnabled: true,
    maxFPS: 60,
    darkModeOnly: false,
  };

  // 检测低端设备
  const isLowEnd = navigator.hardwareConcurrency && navigator.hardwareConcurrency <= 4;
  if (isLowEnd) {
    CONFIG.particleCount = 2000;
    CONFIG.enableDebris = false;
  }

  // ========== 加载 Three.js ==========
  function loadThreeJS(cb) {
    if (window.THREE) { cb(); return; }
    const s = document.createElement('script');
    s.src = 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js';
    s.onload = cb;
    s.onerror = function () {
      console.warn('[bg-engine] Three.js CDN failed');
      initCSSFallback();
    };
    document.head.appendChild(s);
  }

  function initCSSFallback() {
    const style = document.createElement('style');
    style.id = 'bg-fallback-style';
    style.textContent = `
      body::before {
        content: '';
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        z-index: -2;
        background:
          radial-gradient(ellipse at 20% 50%, rgba(255,107,53,0.15) 0%, transparent 50%),
          radial-gradient(ellipse at 80% 20%, rgba(157,77,255,0.12) 0%, transparent 50%),
          radial-gradient(ellipse at 50% 80%, rgba(0,240,255,0.1) 0%, transparent 50%),
          linear-gradient(135deg, #0a0a1a 0%, #0d0d2a 25%, #050520 50%, #0a0a1a 75%, #0d0d2a 100%);
        background-size: 200% 200%;
        animation: gradientShift 25s ease infinite;
      }
      @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
      }
    `;
    document.head.appendChild(style);
  }

  // ========== 主初始化 ==========
  function init() {
    const THREE = window.THREE;
    if (!THREE) { initCSSFallback(); return; }

    // 移除旧canvas
    const old = document.getElementById('bg-canvas');
    if (old) old.remove();

    const scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x0a0a1a, 0.008);

    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 2000);
    camera.position.set(0, 0, 80);

    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'high-performance' });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setClearColor(0x000000, 0);
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.2;
    renderer.domElement.id = 'bg-canvas';
    renderer.domElement.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;z-index:-2;pointer-events:none;';
    document.body.prepend(renderer.domElement);

    // 主题监听
    let isDark = !document.documentElement.classList.contains('theme-light');
    window.addEventListener('themeChange', function (e) {
      isDark = e.detail === 'dark';
    });

    // ========== 灯光系统 ==========
    const ambientLight = new THREE.AmbientLight(0x222244, 0.5);
    scene.add(ambientLight);

    const pointLight1 = new THREE.PointLight(0xFF6B35, 2, 200);
    pointLight1.position.set(20, 30, 50);
    scene.add(pointLight1);

    const pointLight2 = new THREE.PointLight(0x9d4dff, 1.5, 200);
    pointLight2.position.set(-30, -20, 40);
    scene.add(pointLight2);

    const pointLight3 = new THREE.PointLight(0x00f0ff, 1, 150);
    pointLight3.position.set(0, 40, 30);
    scene.add(pointLight3);

    // ========== 超现实粒子场 ==========
    const PARTICLE_COUNT = CONFIG.particleCount;
    const particleGeo = new THREE.BufferGeometry();
    const positions = new Float32Array(PARTICLE_COUNT * 3);
    const colors = new Float32Array(PARTICLE_COUNT * 3);
    const sizes = new Float32Array(PARTICLE_COUNT);
    const velocities = new Float32Array(PARTICLE_COUNT * 3);
    const phases = new Float32Array(PARTICLE_COUNT);

    const palette = [
      new THREE.Color(0xFF6B35),
      new THREE.Color(0xff2d95),
      new THREE.Color(0x00f0ff),
      new THREE.Color(0x9d4dff),
      new THREE.Color(0xffd700),
      new THREE.Color(0x00ff88),
      new THREE.Color(0xff4466),
      new THREE.Color(0x44aaff),
    ];

    for (let i = 0; i < PARTICLE_COUNT; i++) {
      const i3 = i * 3;
      // 球面分布
      const r = 50 * Math.pow(Math.random(), 0.7);
      const theta = Math.random() * Math.PI * 2;
      const phi = Math.acos(2 * Math.random() - 1);

      positions[i3]     = r * Math.sin(phi) * Math.cos(theta);
      positions[i3 + 1] = r * Math.sin(phi) * Math.sin(theta);
      positions[i3 + 2] = r * Math.cos(phi);

      const c = palette[Math.floor(Math.random() * palette.length)];
      colors[i3]     = c.r;
      colors[i3 + 1] = c.g;
      colors[i3 + 2] = c.b;

      sizes[i] = Math.random() * 3.5 + 0.3;
      phases[i] = Math.random() * Math.PI * 2;

      velocities[i3]     = (Math.random() - 0.5) * 0.02;
      velocities[i3 + 1] = (Math.random() - 0.5) * 0.02;
      velocities[i3 + 2] = (Math.random() - 0.5) * 0.02;
    }

    particleGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    particleGeo.setAttribute('color', new THREE.BufferAttribute(colors, 3));
    particleGeo.setAttribute('size', new THREE.BufferAttribute(sizes, 1));
    particleGeo.setAttribute('velocity', new THREE.BufferAttribute(velocities, 3));

    // 自定义Shader - 超现实渲染
    const particleMat = new THREE.ShaderMaterial({
      uniforms: {
        time: { value: 0 },
        pixelRatio: { value: renderer.getPixelRatio() },
        isDark: { value: 1.0 },
      },
      vertexShader: `
        attribute float size;
        attribute vec3 color;
        attribute vec3 velocity;
        varying vec3 vColor;
        varying float vAlpha;
        varying float vDist;
        uniform float time;
        uniform float pixelRatio;
        uniform float isDark;

        void main() {
          vColor = color;
          vec3 pos = position;

          // 多维噪声扭曲
          float n1 = sin(pos.x * 0.015 + time * 0.4) * cos(pos.z * 0.012 + time * 0.3);
          float n2 = sin(pos.y * 0.018 + time * 0.5) * sin(pos.x * 0.01 + time * 0.2);
          float n3 = cos(pos.z * 0.02 + time * 0.6) * sin(pos.y * 0.014 + time * 0.35);

          pos.x += n1 * 4.0 + n3 * 2.0;
          pos.y += n2 * 4.0;
          pos.z += n1 * 2.0 - n2 * 2.0;

          // 呼吸脉冲
          float pulse = 0.5 + 0.5 * sin(time * 0.7 + length(pos) * 0.03);
          vAlpha = mix(0.15, 0.9, pulse);

          // 距离衰减
          vDist = length(pos);
          float distFade = smoothstep(100.0, 10.0, vDist);
          vAlpha *= distFade;

          vec4 mvPosition = modelViewMatrix * vec4(pos, 1.0);
          gl_PointSize = size * pixelRatio * (100.0 / -mvPosition.z) * (0.4 + 0.6 * pulse);
          gl_Position = projectionMatrix * mvPosition;
        }
      `,
      fragmentShader: `
        varying vec3 vColor;
        varying float vAlpha;
        varying float vDist;

        void main() {
          float d = length(gl_PointCoord - vec2(0.5));
          if (d > 0.5) discard;

          // 软粒子 - 高斯衰减
          float alpha = exp(-d * d * 6.0) * vAlpha;

          // 色晕效果
          vec3 col = vColor;
          col += 0.3 * exp(-d * d * 12.0) * vec3(1.0); // 白心

          gl_FragColor = vec4(col, alpha * 0.85);
        }
      `,
      transparent: true,
      depthWrite: false,
      blending: THREE.AdditiveBlending,
    });

    const particles = new THREE.Points(particleGeo, particleMat);
    scene.add(particles);

    // ========== 霓虹网格线框（超现实几何） ==========
    const gridGroup = new THREE.Group();

    // 主网格 - 二十面体
    const icoGeo = new THREE.IcosahedronGeometry(32, 1);
    const icoWire = new THREE.WireframeGeometry(icoGeo);
    const icoMat = new THREE.LineBasicMaterial({
      color: 0xFF6B35,
      transparent: true,
      opacity: 0.1,
      blending: THREE.AdditiveBlending,
    });
    const icoMesh = new THREE.LineSegments(icoWire, icoMat);
    gridGroup.add(icoMesh);

    // 次网格 - 八面体
    const octGeo = new THREE.OctahedronGeometry(42, 0);
    const octWire = new THREE.WireframeGeometry(octGeo);
    const octMat = new THREE.LineBasicMaterial({
      color: 0x9d4dff,
      transparent: true,
      opacity: 0.07,
      blending: THREE.AdditiveBlending,
    });
    const octMesh = new THREE.LineSegments(octWire, octMat);
    gridGroup.add(octMesh);

    // 第三层 -  torus
    const torusGeo = new THREE.TorusGeometry(38, 0.5, 8, 64);
    const torusMat = new THREE.LineBasicMaterial({
      color: 0x00f0ff,
      transparent: true,
      opacity: 0.08,
      blending: THREE.AdditiveBlending,
    });
    const torusLine = new THREE.Line(torusGeo, torusMat);
    torusLine.rotation.x = Math.PI / 2;
    gridGroup.add(torusLine);

    scene.add(gridGroup);

    // ========== 体积光射线 ==========
    const rayGroup = new THREE.Group();
    const rayCount = 12;
    for (let i = 0; i < rayCount; i++) {
      const angle = (i / rayCount) * Math.PI * 2;
      const tilt = (Math.random() - 0.5) * 0.6;
      const rayLen = 70 + Math.random() * 50;

      const rayGeo = new THREE.BufferGeometry();
      const pts = new Float32Array(6);
      pts[0] = 0; pts[1] = 0; pts[2] = 0;
      pts[3] = Math.cos(angle) * Math.cos(tilt) * rayLen;
      pts[4] = Math.sin(tilt) * rayLen * 0.5;
      pts[5] = Math.sin(angle) * Math.cos(tilt) * rayLen;

      rayGeo.setAttribute('position', new THREE.BufferAttribute(pts, 3));
      const c = palette[i % palette.length];
      const rayMat = new THREE.LineBasicMaterial({
        color: c.getHex(),
        transparent: true,
        opacity: 0.03 + Math.random() * 0.04,
        blending: THREE.AdditiveBlending,
      });
      const ray = new THREE.Line(rayGeo, rayMat);
      ray.userData = { baseOpacity: rayMat.opacity, speed: 0.3 + Math.random() * 0.5 };
      rayGroup.add(ray);
    }
    scene.add(rayGroup);

    // ========== 漂浮几何碎片（PBR风格） ==========
    const debrisGroup = new THREE.Group();
    if (CONFIG.enableDebris) {
      const debrisCount = 20;
      const geoTypes = [
        new THREE.TetrahedronGeometry(0.7),
        new THREE.OctahedronGeometry(0.5),
        new THREE.IcosahedronGeometry(0.4),
        new THREE.TorusGeometry(0.4, 0.15, 6, 12),
        new THREE.ConeGeometry(0.3, 0.8, 6),
      ];

      for (let i = 0; i < debrisCount; i++) {
        const geo = geoTypes[Math.floor(Math.random() * geoTypes.length)];
        const c = palette[Math.floor(Math.random() * palette.length)];
        const mat = new THREE.MeshBasicMaterial({
          color: c.getHex(),
          transparent: true,
          opacity: 0.12 + Math.random() * 0.18,
          blending: THREE.AdditiveBlending,
          wireframe: Math.random() > 0.4,
        });
        const mesh = new THREE.Mesh(geo, mat);
        mesh.position.set(
          (Math.random() - 0.5) * 90,
          (Math.random() - 0.5) * 90,
          (Math.random() - 0.5) * 50,
        );
        mesh.userData = {
          rotSpeed: new THREE.Vector3(
            (Math.random() - 0.5) * 0.015,
            (Math.random() - 0.5) * 0.015,
            (Math.random() - 0.5) * 0.015
          ),
          floatSpeed: 0.3 + Math.random() * 0.5,
          floatAmp: 2 + Math.random() * 5,
          phase: Math.random() * Math.PI * 2,
        };
        debrisGroup.add(mesh);
      }
      scene.add(debrisGroup);
    }

    // ========== 中心光辉（脉冲星） ==========
    const glowGroup = new THREE.Group();

    // 内核
    const coreGeo = new THREE.SphereGeometry(2.5, 32, 32);
    const coreMat = new THREE.MeshBasicMaterial({
      color: 0xFF6B35,
      transparent: true,
      opacity: 0.4,
      blending: THREE.AdditiveBlending,
    });
    const core = new THREE.Mesh(coreGeo, coreMat);
    glowGroup.add(core);

    // 光晕1
    const halo1Geo = new THREE.SphereGeometry(7, 32, 32);
    const halo1Mat = new THREE.MeshBasicMaterial({
      color: 0xFF6B35,
      transparent: true,
      opacity: 0.06,
      blending: THREE.AdditiveBlending,
      side: THREE.BackSide,
    });
    const halo1 = new THREE.Mesh(halo1Geo, halo1Mat);
    glowGroup.add(halo1);

    // 光晕2
    const halo2Geo = new THREE.SphereGeometry(12, 32, 32);
    const halo2Mat = new THREE.MeshBasicMaterial({
      color: 0x9d4dff,
      transparent: true,
      opacity: 0.03,
      blending: THREE.AdditiveBlending,
      side: THREE.BackSide,
    });
    const halo2 = new THREE.Mesh(halo2Geo, halo2Mat);
    glowGroup.add(halo2);

    scene.add(glowGroup);

    // ========== 火箭发射粒子流（特效） ==========
    let rocketParticles = null;
    let rocketActive = false;
    let rocketTime = 0;

    function launchRocket() {
      if (rocketActive) return;
      rocketActive = true;
      rocketTime = 0;

      const count = 500;
      const geo = new THREE.BufferGeometry();
      const pos = new Float32Array(count * 3);
      const col = new Float32Array(count * 3);
      const sz = new Float32Array(count);

      for (let i = 0; i < count; i++) {
        pos[i * 3] = (Math.random() - 0.5) * 2;
        pos[i * 3 + 1] = -60 + Math.random() * 5;
        pos[i * 3 + 2] = (Math.random() - 0.5) * 2;

        const c = new THREE.Color().setHSL(0.05 + Math.random() * 0.08, 1, 0.5 + Math.random() * 0.3);
        col[i * 3] = c.r;
        col[i * 3 + 1] = c.g;
        col[i * 3 + 2] = c.b;

        sz[i] = Math.random() * 2 + 0.5;
      }

      geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
      geo.setAttribute('color', new THREE.BufferAttribute(col, 3));
      geo.setAttribute('size', new THREE.BufferAttribute(sz, 1));

      const mat = new THREE.ShaderMaterial({
        uniforms: { time: { value: 0 } },
        vertexShader: `
          attribute float size;
          attribute vec3 color;
          varying vec3 vColor;
          varying float vAlpha;
          uniform float time;
          void main() {
            vColor = color;
            vec3 p = position;
            p.y += time * 20.0;
            p.x += sin(time * 3.0 + p.y * 0.1) * 2.0;
            p.z += cos(time * 3.0 + p.y * 0.1) * 2.0;
            vAlpha = smoothstep(80.0, 0.0, p.y);
            vec4 mv = modelViewMatrix * vec4(p, 1.0);
            gl_PointSize = size * (80.0 / -mv.z);
            gl_Position = projectionMatrix * mv;
          }
        `,
        fragmentShader: `
          varying vec3 vColor;
          varying float vAlpha;
          void main() {
            float d = length(gl_PointCoord - vec2(0.5));
            if (d > 0.5) discard;
            gl_FragColor = vec4(vColor, vAlpha * 0.8);
          }
        `,
        transparent: true,
        blending: THREE.AdditiveBlending,
        depthWrite: false,
      });

      rocketParticles = new THREE.Points(geo, mat);
      scene.add(rocketParticles);

      // 5秒后自动移除
      setTimeout(() => {
        if (rocketParticles) {
          scene.remove(rocketParticles);
          rocketParticles.geometry.dispose();
          rocketParticles.material.dispose();
          rocketParticles = null;
          rocketActive = false;
        }
      }, 5000);
    }

    // 点击背景触发火箭
    renderer.domElement.addEventListener('click', function (e) {
      if (e.target === renderer.domElement) launchRocket();
    });

    // ========== 鼠标交互 ==========
    const mouse = { x: 0, y: 0, tx: 0, ty: 0 };
    if (CONFIG.enableMouseInteraction) {
      window.addEventListener('mousemove', function (e) {
        mouse.tx = (e.clientX / window.innerWidth - 0.5) * 2;
        mouse.ty = -(e.clientY / window.innerHeight - 0.5) * 2;
      });
    }

    // ========== 滚动暂停 ==========
    let scrollPaused = false;
    if (CONFIG.pauseOnScroll) {
      let scrollTimeout;
      window.addEventListener('scroll', function () {
        scrollPaused = true;
        clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(() => { scrollPaused = false; }, 1000);
      }, { passive: true });
    }

    // ========== 动画循环 ==========
    const clock = new THREE.Clock();
    let frameId;
    let lastTime = 0;

    function animate() {
      frameId = requestAnimationFrame(animate);

      const now = performance.now();
      if (now - lastTime < 1000 / CONFIG.maxFPS) return;
      lastTime = now;

      if (scrollPaused) return;

      const t = clock.getElapsedTime();
      const dt = clock.getDelta();

      // 平滑鼠标
      mouse.x += (mouse.tx - mouse.x) * 0.04;
      mouse.y += (mouse.ty - mouse.y) * 0.04;

      // 粒子时间
      particleMat.uniforms.time.value = t;
      particleMat.uniforms.isDark.value = isDark ? 1.0 : 0.2;

      // 粒子场旋转
      particles.rotation.y = t * 0.025;
      particles.rotation.x = Math.sin(t * 0.015) * 0.08;

      // 更新粒子位置（JS端，降级兼容）
      const posArr = particleGeo.attributes.position.array;
      for (let i = 0; i < PARTICLE_COUNT; i++) {
        const i3 = i * 3;
        posArr[i3]     += velocities[i3]     * (1 + 0.5 * Math.sin(t * 0.3 + phases[i]));
        posArr[i3 + 1] += velocities[i3 + 1] * (1 + 0.5 * Math.cos(t * 0.4 + phases[i]));
        posArr[i3 + 2] += velocities[i3 + 2] * (1 + 0.5 * Math.sin(t * 0.35 + phases[i]));

        // 边界回绕
        if (posArr[i3] > 60) posArr[i3] = -60;
        if (posArr[i3] < -60) posArr[i3] = 60;
        if (posArr[i3 + 1] > 60) posArr[i3 + 1] = -60;
        if (posArr[i3 + 1] < -60) posArr[i3 + 1] = 60;
        if (posArr[i3 + 2] > 60) posArr[i3 + 2] = -60;
        if (posArr[i3 + 2] < -60) posArr[i3 + 2] = 60;
      }
      particleGeo.attributes.position.needsUpdate = true;

      // 网格旋转
      gridGroup.rotation.y = t * 0.04;
      gridGroup.rotation.x = Math.sin(t * 0.025) * 0.12;
      gridGroup.rotation.z = Math.cos(t * 0.018) * 0.04;

      // 体积光
      rayGroup.rotation.y = t * 0.06;
      rayGroup.children.forEach(function (ray, i) {
        ray.material.opacity = ray.userData.baseOpacity *
          (0.4 + 0.6 * Math.sin(t * ray.userData.speed + i * 0.7));
      });

      // 几何碎片
      debrisGroup.children.forEach(function (m) {
        m.rotation.x += m.userData.rotSpeed.x;
        m.rotation.y += m.userData.rotSpeed.y;
        m.rotation.z += m.userData.rotSpeed.z;
        m.position.y += Math.sin(t * m.userData.floatSpeed + m.userData.phase) * 0.015;
      });

      // 脉冲星
      const pulse = 0.25 + 0.2 * Math.sin(t * 1.2);
      coreMat.opacity = pulse;
      core.scale.setScalar(1 + 0.25 * Math.sin(t * 1.2));
      halo1Mat.opacity = 0.04 + 0.04 * Math.cos(t * 0.7);
      halo2Mat.opacity = 0.02 + 0.02 * Math.sin(t * 0.5);

      // 火箭粒子
      if (rocketParticles) {
        rocketTime += dt;
        rocketParticles.material.uniforms.time.value = rocketTime;
        rocketParticles.rotation.y = t * 0.1;
      }

      // 相机跟随
      camera.position.x += (mouse.x * 12 - camera.position.x) * 0.025;
      camera.position.y += (mouse.y * 10 - camera.position.y) * 0.025;
      camera.lookAt(0, 0, 0);

      // 浅色模式淡出
      if (!isDark) {
        renderer.domElement.style.opacity = '0.25';
      } else {
        renderer.domElement.style.opacity = '1';
      }

      renderer.render(scene, camera);
    }

    animate();

    // ========== Resize ==========
    function onResize() {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
      particleMat.uniforms.pixelRatio.value = renderer.getPixelRatio();
    }
    window.addEventListener('resize', onResize);

    // ========== LOD自适应 ==========
    if (CONFIG.lodEnabled) {
      function updateLOD() {
        const fps = renderer.info.render.frame;
        // 简化：根据设备内存调整
        if (navigator.deviceMemory && navigator.deviceMemory < 4) {
          particleMat.uniforms.pixelRatio.value = Math.min(renderer.getPixelRatio(), 1);
        }
        requestAnimationFrame(updateLOD);
      }
      updateLOD();
    }

    // ========== 公开API ==========
    window.__bgEngine = {
      launchRocket,
      setParticleCount: function (n) {
        CONFIG.particleCount = n;
        location.reload();
      },
      pause: function () { scrollPaused = true; },
      resume: function () { scrollPaused = false; },
      destroy: function () {
        cancelAnimationFrame(frameId);
        renderer.dispose();
        if (renderer.domElement.parentNode) {
          renderer.domElement.parentNode.removeChild(renderer.domElement);
        }
      },
    };

    // 暴露主题事件
    window.dispatchEvent(new CustomEvent('bgEngineReady', { detail: { version: '2.0' } }));
  }

  // 启动
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { loadThreeJS(init); });
  } else {
    loadThreeJS(init);
  }
})();

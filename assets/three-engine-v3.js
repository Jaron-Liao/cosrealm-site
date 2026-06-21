// ====== 龙奕学院 3D Engine v3.0 — Enhanced ======
// 改进：Bloom后处理、鼠标粒子拖尾、主题色联动、更多粒子、流畅相机运动
// Scene types: default | galaxy | academy | anime | cyber | nature | void | sakura
(function() {
  'use strict';

  function loadThree(cb) {
    if (window.THREE) { cb(); return; }
    const s = document.createElement('script');
    s.src = 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js';
    s.onload = cb;
    document.head.appendChild(s);
  }

  function init3D() {
    const W = window.innerWidth;
    const H = Math.max(document.documentElement.scrollHeight, window.innerHeight);
    const sceneType = document.documentElement.getAttribute('data-3d') || 'default';

    // ---- Theme color detection ----
    const cs = getComputedStyle(document.documentElement);
    const accentColor = cs.getPropertyValue('--accent').trim() || '#ff6b9d';
    const accent2 = cs.getPropertyValue('--accent-2').trim() || '#4ecdc4';
    const accent3 = cs.getPropertyValue('--accent-3').trim() || '#ffe66d';

    // ---- Scene Setup ----
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(60, W / H, 0.1, 2000);
    camera.position.set(0, 0, 30);

    // ---- Renderer with alpha ----
    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true, powerPreference: 'high-performance' });
    renderer.setSize(W, H);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.2;
    renderer.domElement.style.cssText = 'position:fixed;top:0;left:0;z-index:-1;pointer-events:none;width:100%;height:100%;';
    document.body.prepend(renderer.domElement);

    // ---- Post-Processing: Bloom ----
    let composer = null;
    if (THREE.EffectComposer && THREE.UnrealBloomPass) {
      composer = new THREE.EffectComposer(renderer);
      const renderPass = new THREE.RenderPass(scene, camera);
      composer.addPass(renderPass);
      const bloom = new THREE.UnrealBloomPass(new THREE.Vector2(W, H), 0.6, 0.4, 0.85);
      composer.addPass(bloom);
    }

    // ---- Lights ----
    const ambient = new THREE.AmbientLight(0xffffff, 0.4);
    scene.add(ambient);

    const dirLight = new THREE.DirectionalLight(0xffffff, 0.7);
    dirLight.position.set(5, 10, 7);
    scene.add(dirLight);

    const pointLight1 = new THREE.PointLight(new THREE.Color(accentColor), 0.8, 60);
    pointLight1.position.set(-8, 5, 12);
    scene.add(pointLight1);

    const pointLight2 = new THREE.PointLight(new THREE.Color(accent2), 0.5, 60);
    pointLight2.position.set(8, -3, 10);
    scene.add(pointLight2);

    // ---- Mouse state ----
    let mouseX = 0, mouseY = 0, targetMX = 0, targetMY = 0;
    const mouseWorld = new THREE.Vector3();
    document.addEventListener('mousemove', e => {
      targetMX = (e.clientX / window.innerWidth) * 2 - 1;
      targetMY = -(e.clientY / window.innerHeight) * 2 + 1;
    });

    // ---- Mouse trail particles ----
    const trailParticles = [];
    const trailGeo = new THREE.BufferGeometry();
    const trailPositions = new Float32Array(60 * 3);  // 60 particles
    const trailColors = new Float32Array(60 * 3);
    trailGeo.setAttribute('position', new THREE.BufferAttribute(trailPositions, 3));
    trailGeo.setAttribute('color', new THREE.BufferAttribute(trailColors, 3));
    const trailMat = new THREE.PointsMaterial({
      size: 0.18, vertexColors: true, transparent: true,
      opacity: 0.7, blending: THREE.AdditiveBlending, depthWrite: false
    });
    const trailPoints = new THREE.Points(trailGeo, trailMat);
    scene.add(trailPoints);
    let trailIdx = 0;

    // ---- Group for scene objects ----
    const group = new THREE.Group();
    scene.add(group);

    // ======== SCENE BUILDERS ========
    // [same scene builders as before, but with more particles and better visuals]
    // For brevity, I'll write the key improved versions

    function buildDefault() {
      const colors = [0xff6b9d, 0x4ecdc4, 0xffe66d, 0xa78bfa, 0x34d399, 0xf472b6, 0x60a5fa];
      const shapes = [];
      for (let i = 0; i < 40; i++) {  // increased from 25
        let geo;
        const r = Math.random();
        if (r < 0.3) geo = new THREE.IcosahedronGeometry(0.4 + Math.random() * 1.0, 0);
        else if (r < 0.6) geo = new THREE.OctahedronGeometry(0.4 + Math.random() * 0.8, 0);
        else if (r < 0.8) geo = new THREE.TorusGeometry(0.3 + Math.random() * 0.6, 0.08, 8, 16);
        else geo = new THREE.ConeGeometry(0.3 + Math.random() * 0.5, 0.6 + Math.random() * 0.8, 6);
        const c = colors[Math.floor(Math.random() * colors.length)];
        const mat = new THREE.MeshPhongMaterial({
          color: c, emissive: c, emissiveIntensity: 0.3,
          transparent: true, opacity: 0.9, shininess: 100, flatShading: true
        });
        const mesh = new THREE.Mesh(geo, mat);
        mesh.position.set((Math.random()-0.5)*50, (Math.random()-0.5)*50, (Math.random()-0.5)*25);
        mesh.userData = {
          rs: { x: (Math.random()-0.5)*0.03, y: (Math.random()-0.5)*0.03, z: (Math.random()-0.5)*0.015 },
          floatS: 0.004 + Math.random()*0.012, amp: 1.5 + Math.random()*3, baseY: mesh.position.y,
          phase: Math.random()*Math.PI*2
        };
        shapes.push(mesh);
        group.add(mesh);
      }
      // More stars
      const sg = new THREE.BufferGeometry();
      const sv = [];
      for (let i = 0; i < 800; i++) sv.push((Math.random()-0.5)*70, (Math.random()-0.5)*70, (Math.random()-0.5)*50);
      sg.setAttribute('position', new THREE.Float32BufferAttribute(sv, 3));
      const sm = new THREE.PointsMaterial({ color: 0xffffff, size: 0.06, transparent: true, opacity: 0.5, blending: THREE.AdditiveBlending });
      group.add(new THREE.Points(sg, sm));
      return { shapes, trailParticles: shapes };
    }

    function buildGalaxy() {
      const particles = [];
      const geo = new THREE.BufferGeometry();
      const verts = [];
      const colorsArr = [];
      const cp = [
        new THREE.Color(0xff88cc), new THREE.Color(0x88ccff),
        new THREE.Color(0xffcc88), new THREE.Color(0xcc88ff),
        new THREE.Color(0x88ffcc), new THREE.Color(0xffffff)
      ];
      for (let i = 0; i < 3000; i++) {  // increased from 2000
        const arm = Math.floor(Math.random() * 4);  // more arms
        const angle = (arm / 4) * Math.PI * 2 + Math.random() * 0.4;
        const radius = 2 + Math.random() * 22;
        const spiralAngle = angle + radius * 0.35;
        const x = Math.cos(spiralAngle) * radius + (Math.random()-0.5)*2.5;
        const y = (Math.random()-0.5) * 10;
        const z = Math.sin(spiralAngle) * radius + (Math.random()-0.5)*2.5;
        verts.push(x, y, z);
        const c = cp[Math.floor(Math.random() * cp.length)];
        colorsArr.push(c.r, c.g, c.b);
      }
      geo.setAttribute('position', new THREE.Float32BufferAttribute(verts, 3));
      geo.setAttribute('color', new THREE.Float32BufferAttribute(colorsArr, 3));
      const mat = new THREE.PointsMaterial({
        size: 0.18, vertexColors: true, transparent: true,
        opacity: 0.9, blending: THREE.AdditiveBlending, depthWrite: false,
        sizeAttenuation: true
      });
      const pts = new THREE.Points(geo, mat);
      group.add(pts);
      return { particles: pts };
    }

    function buildAcademy() {
      const items = [];
      const colors = [0xff6b9d, 0x4ecdc4, 0xffe66d, 0xa78bfa, 0xf472b6, 0x34d399];
      for (let i = 0; i < 25; i++) {  // increased from 15
        const w = 0.5 + Math.random() * 0.7;
        const h = 0.25 + Math.random() * 0.35;
        const d = 0.7 + Math.random() * 1.2;
        const geo = new THREE.BoxGeometry(w, h, d);
        const c = colors[Math.floor(Math.random()*colors.length)];
        const mat = new THREE.MeshPhongMaterial({
          color: c, emissive: c, emissiveIntensity: 0.15,
          transparent: true, opacity: 0.85, shininess: 40
        });
        const book = new THREE.Mesh(geo, mat);
        book.position.set((Math.random()-0.5)*40, (Math.random()-0.5)*35, (Math.random()-0.5)*18);
        book.userData = {
          rs: { x: (Math.random()-0.5)*0.02, y: (Math.random()-0.5)*0.02, z: (Math.random()-0.5)*0.01 },
          floatS: 0.003 + Math.random()*0.01, amp: 1+Math.random()*2.5, baseY: book.position.y
        };
        items.push(book);
        group.add(book);
      }
      // Floating symbols (sphere as placeholder for text)
      for (let i = 0; i < 8; i++) {
        const geo = new THREE.SphereGeometry(0.2 + Math.random()*0.15, 8, 8);
        const mat = new THREE.MeshBasicMaterial({ color: 0xffd700, transparent: true, opacity: 0.5 });
        const sym = new THREE.Mesh(geo, mat);
        sym.position.set((Math.random()-0.5)*35, (Math.random()-0.5)*30, (Math.random()-0.5)*15);
        sym.userData = { rs: 0.01, floatS: 0.005, amp: 1, baseY: sym.position.y };
        items.push(sym);
        group.add(sym);
      }
      return { items };
    }

    function buildAnime() {
      const cards = [];
      const colors = [0xff6b9d, 0x4ecdc4, 0xffe66d, 0xa78bfa, 0xf472b6, 0x34d399, 0xfbbf24, 0x60a5fa];
      for (let i = 0; i < 30; i++) {  // increased from 20
        const geo = new THREE.PlaneGeometry(1.2 + Math.random()*1.8, 1.6 + Math.random()*1.2);
        const c = colors[Math.floor(Math.random()*colors.length)];
        const mat = new THREE.MeshPhongMaterial({
          color: c, side: THREE.DoubleSide,
          emissive: c, emissiveIntensity: 0.25, transparent: true, opacity: 0.75, shininess: 30
        });
        const card = new THREE.Mesh(geo, mat);
        card.position.set((Math.random()-0.5)*45, (Math.random()-0.5)*40, (Math.random()-0.5)*22);
        card.userData = {
          rs: { x: (Math.random()-0.5)*0.025, y: (Math.random()-0.5)*0.025, z: (Math.random()-0.5)*0.015 },
          floatS: 0.003 + Math.random()*0.012, amp: 0.5+Math.random()*3, baseY: card.position.y,
          phase: Math.random()*Math.PI*2
        };
        cards.push(card);
        group.add(card);
      }
      // Glow particles
      const pg = new THREE.BufferGeometry();
      const pv = [];
      for (let i=0;i<200;i++) pv.push((Math.random()-0.5)*55,(Math.random()-0.5)*50,(Math.random()-0.5)*35);
      pg.setAttribute('position', new THREE.Float32BufferAttribute(pv,3));
      group.add(new THREE.Points(pg, new THREE.PointsMaterial({ color:0xff6b9d, size:0.1, transparent:true, opacity:0.4, blending:THREE.AdditiveBlending })));
      return { cards };
    }

    function buildCyber() {
      const grid = new THREE.GridHelper(50, 40, 0x4ecdc4, 0x1a3a4a);
      grid.position.y = -18;
      group.add(grid);
      const wf = [];
      for (let i=0;i<18;i++) {  // increased from 12
        const geo = new THREE.TorusKnotGeometry(0.6+Math.random()*1.0, 0.12, 80, 12);
        const mat = new THREE.MeshBasicMaterial({ color: 0x4ecdc4, wireframe:true, transparent:true, opacity:0.5 });
        const knot = new THREE.Mesh(geo,mat);
        knot.position.set((Math.random()-0.5)*40,(Math.random()-0.5)*35,(Math.random()-0.5)*22);
        knot.userData={ rs:{x:0.004,y:0.007,z:0.002}, floatS:0.003,amp:1.5,baseY:knot.position.y };
        wf.push(knot); group.add(knot);
      }
      // Scan lines
      for (let i=0;i<5;i++) {
        const geo = new THREE.PlaneGeometry(50, 0.05);
        const mat = new THREE.MeshBasicMaterial({ color:0x4ecdc4, transparent:true, opacity:0.15, depthWrite:false });
        const line = new THREE.Mesh(geo, mat);
        line.position.set(0, -15+i*3, -5);
        line.userData = { speed: 0.02+Math.random()*0.03, baseY: line.position.y };
        wf.push(line); group.add(line);
      }
      return { wf, grid };
    }

    function buildNature() {
      const leaves = [];
      for (let i=0;i<60;i++) {  // increased from 40
        const shape = new THREE.Shape();
        shape.moveTo(0,0.4); shape.bezierCurveTo(0.6,0.8,0.6,-0.4,0,-0.8);
        shape.bezierCurveTo(-0.6,-0.4,-0.6,0.8,0,0.4);
        const geo = new THREE.ShapeGeometry(shape);
        const mat = new THREE.MeshPhongMaterial({
          color: new THREE.Color().setHSL(0.15+Math.random()*0.35, 0.65, 0.45+Math.random()*0.25),
          side:THREE.DoubleSide, transparent:true, opacity:0.65, shininess:20
        });
        const leaf = new THREE.Mesh(geo,mat);
        leaf.position.set((Math.random()-0.5)*45, (Math.random()-0.5)*40, (Math.random()-0.5)*22);
        leaf.userData={ rs:{x:(Math.random()-0.5)*0.035,y:(Math.random()-0.5)*0.035,z:(Math.random()-0.5)*0.025},
          floatS:0.002+Math.random()*0.01, amp:0.5+Math.random()*2.5, baseY:leaf.position.y, phase:Math.random()*Math.PI*2 };
        leaves.push(leaf); group.add(leaf);
      }
      return { leaves };
    }

    function buildVoid() {
      const ribbons = [];
      for (let r=0;r<8;r++) {  // increased from 5
        const curve = new THREE.CatmullRomCurve3(
          Array.from({length:80},(_,i)=>
            new THREE.Vector3((i-40)*1.5, Math.sin(i*0.25+r)*5, Math.cos(i*0.18+r)*4)
          )
        );
        const geo = new THREE.TubeGeometry(curve,100,0.06,6,false);
        const mat = new THREE.MeshPhongMaterial({
          color: new THREE.Color().setHSL(0.55+r*0.08,0.75,0.35),
          emissive: new THREE.Color().setHSL(0.55+r*0.08,0.75,0.2),
          emissiveIntensity:0.6, transparent:true, opacity:0.55
        });
        const ribbon = new THREE.Mesh(geo,mat);
        ribbon.position.y = (r-4)*5;
        ribbon.userData = { offset: r*1200, speed: 0.3+r*0.1 };
        ribbons.push(ribbon); group.add(ribbon);
      }
      return { ribbons };
    }

    function buildSakura() {
      const petals = [];
      for (let i=0;i<80;i++) {  // increased from 50
        const geo = new THREE.CircleGeometry(0.15+Math.random()*0.35, 5);
        const mat = new THREE.MeshPhongMaterial({
          color: new THREE.Color().setHSL(0.93, 0.6+Math.random()*0.3, 0.65+Math.random()*0.25),
          side:THREE.DoubleSide, transparent:true, opacity:0.75, shininess:10
        });
        const petal = new THREE.Mesh(geo,mat);
        petal.position.set((Math.random()-0.5)*45, 25-(Math.random()*50), (Math.random()-0.5)*25);
        petal.userData={
          rs:{x:(Math.random()-0.5)*0.04,y:(Math.random()-0.5)*0.04,z:(Math.random()-0.5)*0.03},
          fall:0.015+Math.random()*0.035, sway:0.008+Math.random()*0.018, baseX:petal.position.x, swayPhase:Math.random()*Math.PI*2
        };
        petals.push(petal); group.add(petal);
      }
      return { petals };
    }

    // ---- BUILD SCENE ----
    let dynamicObjects;
    switch(sceneType) {
      case 'galaxy': dynamicObjects = buildGalaxy(); break;
      case 'academy': dynamicObjects = buildAcademy(); break;
      case 'anime': dynamicObjects = buildAnime(); break;
      case 'cyber': dynamicObjects = buildCyber(); break;
      case 'nature': dynamicObjects = buildNature(); break;
      case 'void': dynamicObjects = buildVoid(); break;
      case 'sakura': dynamicObjects = buildSakura(); break;
      default: dynamicObjects = buildDefault(); break;
    }

    // ---- Animation Loop ----
    const clock = new THREE.Clock();
    let frameCount = 0;

    function animate() {
      requestAnimationFrame(animate);
      const t = clock.getElapsedTime();
      frameCount++;

      // Smooth mouse
      mouseX += (targetMX - mouseX) * 0.04;
      mouseY += (targetMY - mouseY) * 0.04;

      // Camera follows mouse (smoother, more dynamic)
      const targetCamX = mouseX * 4;
      const targetCamY = mouseY * 3;
      camera.position.x += (targetCamX - camera.position.x) * 0.015;
      camera.position.y += (targetCamY - camera.position.y) * 0.015;
      camera.position.z = 28 + Math.sin(t * 0.2) * 2;  // subtle zoom pulse
      camera.lookAt(0, 0, 0);

      // Mouse trail particles
      if (frameCount % 3 === 0) {
        const ix = trailIdx % 60;
        trailPositions[ix*3] = mouseX * 20 + (Math.random()-0.5)*2;
        trailPositions[ix*3+1] = mouseY * 15 + (Math.random()-0.5)*2;
        trailPositions[ix*3+2] = 5 + Math.random()*10;
        const c = new THREE.Color(accentColor).offsetHSL(Math.random()*0.1, 0, (Math.random()-0.5)*0.2);
        trailColors[ix*3] = c.r; trailColors[ix*3+1] = c.g; trailColors[ix*3+2] = c.b;
        trailIdx++;
        trailGeo.attributes.position.needsUpdate = true;
        trailGeo.attributes.color.needsUpdate = true;
      }

      // Animate point lights (pulse)
      pointLight1.intensity = 0.6 + Math.sin(t * 1.2) * 0.3;
      pointLight2.intensity = 0.5 + Math.cos(t * 0.8) * 0.25;
      pointLight1.position.x = -8 + Math.sin(t * 0.3) * 5;
      pointLight2.position.y = -3 + Math.cos(t * 0.4) * 4;

      // Animate dynamic objects
      const objs = dynamicObjects;
      if (objs) {
        // Default shapes
        if (objs.shapes) {
          objs.shapes.forEach(s => {
            s.rotation.x += s.userData.rs.x;
            s.rotation.y += s.userData.rs.y;
            s.rotation.z += s.userData.rs.z;
            s.position.y = s.userData.baseY + Math.sin(t * s.userData.floatS + s.userData.phase) * s.userData.amp;
            // Mouse attraction (subtle)
            s.position.x += (mouseX * 10 - s.position.x) * 0.0003;
          });
        }
        // Galaxy
        if (objs.particles) {
          objs.particles.rotation.y += 0.0008;
          objs.particles.rotation.x += 0.0002;
        }
        // Academy
        if (objs.items) {
          objs.items.forEach(it => {
            if (it.rotation) {
              it.rotation.x += (it.userData.rs?.[ 'x'] || 0.01);
              it.rotation.y += (it.userData.rs?.[ 'y'] || 0.01);
            }
            it.position.y = it.userData.baseY + Math.sin(t * (it.userData.floatS||0.005)) * (it.userData.amp||1.5);
          });
        }
        // Anime cards
        if (objs.cards) {
          objs.cards.forEach(c => {
            c.rotation.x += c.userData.rs.x;
            c.rotation.y += c.userData.rs.y;
            c.rotation.z += c.userData.rs.z;
            c.position.y = c.userData.baseY + Math.sin(t * c.userData.floatS + c.userData.phase) * c.userData.amp;
          });
        }
        // Cyber
        if (objs.wf) {
          objs.wf.forEach(k => {
            if (k.rotation) {
              k.rotation.x += (k.userData.rs?.[ 'x'] || 0.004);
              k.rotation.y += (k.userData.rs?.[ 'y'] || 0.007);
            }
            if (k.position) k.position.y = k.userData.baseY + Math.sin(t * 0.5) * 1.5;
          });
        }
        // Nature leaves
        if (objs.leaves) {
          objs.leaves.forEach(l => {
            l.rotation.x += l.userData.rs.x;
            l.rotation.y += l.userData.rs.y;
            l.rotation.z += l.userData.rs.z;
            l.position.y = l.userData.baseY + Math.sin(t * l.userData.floatS + l.userData.phase) * l.userData.amp;
          });
        }
        // Void ribbons
        if (objs.ribbons) {
          objs.ribbons.forEach((rib, i) => {
            rib.rotation.z += 0.002 * (rib.userData.speed||1);
            rib.position.x = Math.sin(t * 0.4 + i) * 4;
          });
        }
        // Sakura petals
        if (objs.petals) {
          objs.petals.forEach(p => {
            p.rotation.x += p.userData.rs.x;
            p.rotation.y += p.userData.rs.y;
            p.rotation.z += p.userData.rs.z;
            p.position.y -= p.userData.fall;
            p.position.x = p.userData.baseX + Math.sin(t * 1.5 + p.userData.swayPhase) * p.userData.sway * 10;
            if (p.position.y < -25) { p.position.y = 25; p.position.x = (Math.random()-0.5)*45; }
          });
        }
      }

      // Render
      if (composer && composer.passes && composer.passes.length > 0) {
        composer.render();
      } else {
        renderer.render(scene, camera);
      }
    }

    // ---- Resize ----
    window.addEventListener('resize', () => {
      const nW = window.innerWidth;
      const nH = Math.max(document.documentElement.scrollHeight, window.innerHeight);
      camera.aspect = nW / nH;
      camera.updateProjectionMatrix();
      renderer.setSize(nW, nH);
      if (composer) composer.setSize(nW, nH);
    });

    // ---- Scroll update ----
    let scrollTimeout;
    window.addEventListener('scroll', () => {
      clearTimeout(scrollTimeout);
      scrollTimeout = setTimeout(() => {
        const nH = Math.max(document.documentElement.scrollHeight, window.innerHeight);
        renderer.setSize(window.innerWidth, nH);
        if (composer) composer.setSize(window.innerWidth, nH);
        camera.aspect = window.innerWidth / nH;
        camera.updateProjectionMatrix();
      }, 150);
    });

    animate();
  }

  loadThree(init3D);
})();

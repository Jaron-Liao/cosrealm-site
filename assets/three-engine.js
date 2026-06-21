// ====== 龙奕学院 3D Engine v2.0 — Three.js Powered ======
// Scene types: default | galaxy | academy | anime | cyber | nature | void | sakura
(function() {
  'use strict';

  // 动态加载Three.js CDN
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

    // ---- Scene Setup ----
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(60, W / H, 0.1, 1000);
    camera.position.z = 30;

    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    renderer.setSize(W, H);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.domElement.style.cssText = 'position:fixed;top:0;left:0;z-index:-1;pointer-events:none;';
    document.body.prepend(renderer.domElement);

    // ---- Lights ----
    const ambient = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(ambient);
    const dirLight = new THREE.DirectionalLight(0xffffff, 0.8);
    dirLight.position.set(5, 10, 7);
    scene.add(dirLight);
    const pointLight = new THREE.PointLight(0xff88aa, 0.6, 50);
    pointLight.position.set(-5, 0, 10);
    scene.add(pointLight);

    // ---- Common Objects ----
    const group = new THREE.Group();
    scene.add(group);

    // ======== SCENE BUILDERS ========

    function buildDefault() {
      // Floating colorful geometric shapes
      const shapes = [];
      const colors = [0xff6b9d, 0x4ecdc4, 0xffe66d, 0xa78bfa, 0x34d399, 0xf472b6];
      for (let i = 0; i < 25; i++) {
        let geo;
        const r = Math.random();
        if (r < 0.33) geo = new THREE.IcosahedronGeometry(0.5 + Math.random() * 1.2, 0);
        else if (r < 0.66) geo = new THREE.OctahedronGeometry(0.5 + Math.random() * 1.0, 0);
        else geo = new THREE.TorusGeometry(0.4 + Math.random() * 0.8, 0.1, 8, 16);
        const mat = new THREE.MeshPhongMaterial({
          color: colors[Math.floor(Math.random() * colors.length)],
          emissive: colors[Math.floor(Math.random() * colors.length)],
          emissiveIntensity: 0.2,
          transparent: true,
          opacity: 0.85,
          shininess: 80
        });
        const mesh = new THREE.Mesh(geo, mat);
        mesh.position.set(
          (Math.random() - 0.5) * 40,
          (Math.random() - 0.5) * 40,
          (Math.random() - 0.5) * 20
        );
        mesh.userData = {
          rotSpeed: { x: (Math.random()-0.5)*0.02, y: (Math.random()-0.5)*0.02, z: (Math.random()-0.5)*0.01 },
          floatSpeed: 0.005 + Math.random() * 0.015,
          floatAmp: 1 + Math.random() * 3,
          baseY: mesh.position.y
        };
        shapes.push(mesh);
        group.add(mesh);
      }
      // Starfield backdrop
      const starGeo = new THREE.BufferGeometry();
      const starVerts = [];
      for (let i = 0; i < 500; i++) {
        starVerts.push((Math.random()-0.5)*60, (Math.random()-0.5)*60, (Math.random()-0.5)*40);
      }
      starGeo.setAttribute('position', new THREE.Float32BufferAttribute(starVerts, 3));
      const starMat = new THREE.PointsMaterial({ color: 0xffffff, size: 0.08, transparent: true, opacity: 0.6 });
      const stars = new THREE.Points(starGeo, starMat);
      group.add(stars);
      return { shapes, stars };
    }

    function buildGalaxy() {
      // Spiral galaxy
      const particles = [];
      const geo = new THREE.BufferGeometry();
      const verts = [];
      const colorsArr = [];
      const colorPalette = [
        new THREE.Color(0xff88cc), new THREE.Color(0x88ccff),
        new THREE.Color(0xffcc88), new THREE.Color(0xcc88ff),
        new THREE.Color(0x88ffcc), new THREE.Color(0xffffff)
      ];
      for (let i = 0; i < 2000; i++) {
        const arm = Math.floor(Math.random() * 3);
        const angle = (arm / 3) * Math.PI * 2 + Math.random() * 0.5;
        const radius = 3 + Math.random() * 18;
        const spiralAngle = angle + radius * 0.4;
        const x = Math.cos(spiralAngle) * radius + (Math.random()-0.5)*2;
        const y = (Math.random()-0.5) * 8;
        const z = Math.sin(spiralAngle) * radius + (Math.random()-0.5)*2;
        verts.push(x, y, z);
        const c = colorPalette[Math.floor(Math.random() * colorPalette.length)];
        colorsArr.push(c.r, c.g, c.b);
      }
      geo.setAttribute('position', new THREE.Float32BufferAttribute(verts, 3));
      geo.setAttribute('color', new THREE.Float32BufferAttribute(colorsArr, 3));
      const mat = new THREE.PointsMaterial({
        size: 0.15, vertexColors: true, transparent: true,
        opacity: 0.8, blending: THREE.AdditiveBlending, depthWrite: false
      });
      const pts = new THREE.Points(geo, mat);
      group.add(pts);
      return { particles: pts };
    }

    function buildAcademy() {
      // Floating books & stars — academy vibes
      const items = [];
      const colors = [0xff6b9d, 0x4ecdc4, 0xffe66d, 0xa78bfa, 0xf472b6, 0x34d399];
      // Books (flat boxes)
      for (let i = 0; i < 15; i++) {
        const w = 0.6 + Math.random() * 0.8;
        const h = 0.3 + Math.random() * 0.3;
        const d = 0.8 + Math.random() * 1.0;
        const geo = new THREE.BoxGeometry(w, h, d);
        const mat = new THREE.MeshPhongMaterial({
          color: colors[Math.floor(Math.random()*colors.length)],
          transparent: true, opacity: 0.9, shininess: 60
        });
        const book = new THREE.Mesh(geo, mat);
        book.position.set((Math.random()-0.5)*35, (Math.random()-0.5)*30, (Math.random()-0.5)*15);
        book.userData = { rs: (Math.random()-0.5)*0.015, ry: (Math.random()-0.5)*0.01, float: 0.005+Math.random()*0.01, amp: 1+Math.random()*2, baseY: book.position.y };
        items.push(book);
        group.add(book);
      }
      // Stars
      const starGeo = new THREE.BufferGeometry();
      const sv = [];
      for (let i=0;i<400;i++) sv.push((Math.random()-0.5)*50,(Math.random()-0.5)*40,(Math.random()-0.5)*30);
      starGeo.setAttribute('position', new THREE.Float32BufferAttribute(sv,3));
      group.add(new THREE.Points(starGeo, new THREE.PointsMaterial({color:0xffd700,size:0.1,transparent:true,opacity:0.5})));
      return { items };
    }

    function buildAnime() {
      // Floating cards / posters
      const cards = [];
      const colors = [0xff6b9d, 0x4ecdc4, 0xffe66d, 0xa78bfa, 0xf472b6, 0xfbbf24, 0x34d399, 0x60a5fa];
      for (let i = 0; i < 20; i++) {
        const geo = new THREE.PlaneGeometry(1.5 + Math.random()*1.5, 2 + Math.random()*1.5);
        const mat = new THREE.MeshPhongMaterial({
          color: colors[Math.floor(Math.random()*colors.length)],
          side: THREE.DoubleSide, transparent: true, opacity: 0.8,
          emissive: colors[Math.floor(Math.random()*colors.length)], emissiveIntensity: 0.3,
          shininess: 40
        });
        const card = new THREE.Mesh(geo, mat);
        card.position.set((Math.random()-0.5)*40, (Math.random()-0.5)*35, (Math.random()-0.5)*20);
        card.userData = { rs: (Math.random()-0.5)*0.02, ry: (Math.random()-0.5)*0.02, rz: (Math.random()-0.5)*0.01, float: 0.003+Math.random()*0.012, amp: 0.5+Math.random()*2.5, baseY: card.position.y };
        cards.push(card);
        group.add(card);
      }
      const sg = new THREE.BufferGeometry(); const sv=[];
      for (let i=0;i<300;i++) sv.push((Math.random()-0.5)*55,(Math.random()-0.5)*45,(Math.random()-0.5)*30);
      sg.setAttribute('position',new THREE.Float32BufferAttribute(sv,3));
      group.add(new THREE.Points(sg,new THREE.PointsMaterial({color:0xff88cc,size:0.12,transparent:true,opacity:0.4,blending:THREE.AdditiveBlending})));
      return { cards };
    }

    function buildCyber() {
      // Wireframe grid
      const grid = new THREE.GridHelper(40, 30, 0x4ecdc4, 0x1a1a2e);
      grid.position.y = -15;
      group.add(grid);
      // Floating wireframe shapes
      const wf = [];
      for (let i=0;i<12;i++) {
        const geo = new THREE.TorusKnotGeometry(0.8+Math.random()*0.8, 0.15, 64, 8, 2, 3);
        const mat = new THREE.MeshBasicMaterial({color:0x4ecdc4,wireframe:true,transparent:true,opacity:0.4});
        const knot = new THREE.Mesh(geo,mat);
        knot.position.set((Math.random()-0.5)*35,(Math.random()-0.5)*30,(Math.random()-0.5)*20);
        knot.userData={rs:0.005,ry:0.008,rz:0.003,float:0.004,amp:1.5,baseY:knot.position.y};
        wf.push(knot); group.add(knot);
      }
      return { wf, grid };
    }

    function buildNature() {
      // Floating leaves
      const leaves = [];
      for (let i=0;i<40;i++) {
        const shape = new THREE.Shape();
        shape.moveTo(0,0.4); shape.bezierCurveTo(0.6,0.8,0.6,-0.4,0,-0.8);
        shape.bezierCurveTo(-0.6,-0.4,-0.6,0.8,0,0.4);
        const geo = new THREE.ShapeGeometry(shape);
        const mat = new THREE.MeshPhongMaterial({
          color: new THREE.Color().setHSL(0.15+Math.random()*0.35,0.7,0.5+Math.random()*0.3),
          side:THREE.DoubleSide,transparent:true,opacity:0.7,shininess:30
        });
        const leaf = new THREE.Mesh(geo,mat);
        leaf.position.set((Math.random()-0.5)*40, (Math.random()-0.5)*35, (Math.random()-0.5)*20);
        leaf.userData={rs:(Math.random()-0.5)*0.03,ry:(Math.random()-0.5)*0.03,rz:(Math.random()-0.5)*0.02,float:0.003+Math.random()*0.01,amp:0.5+Math.random()*2,baseY:leaf.position.y};
        leaves.push(leaf); group.add(leaf);
      }
      return { leaves };
    }

    function buildVoid() {
      // Abstract wave ribbons
      const ribbons = [];
      for (let r=0;r<5;r++) {
        const curve = new THREE.CatmullRomCurve3(
          Array.from({length:60},(_,i)=>
            new THREE.Vector3((i-30)*1.2, Math.sin(i*0.3+r)*4, Math.cos(i*0.2+r)*3)
          )
        );
        const geo = new THREE.TubeGeometry(curve,80,0.08,8,false);
        const mat = new THREE.MeshPhongMaterial({
          color: new THREE.Color().setHSL(0.55+r*0.1,0.8,0.6),
          emissive: new THREE.Color().setHSL(0.55+r*0.1,0.8,0.3),
          emissiveIntensity:0.5,transparent:true,opacity:0.6
        });
        const ribbon = new THREE.Mesh(geo,mat);
        ribbon.position.y = (r-2)*4;
        ribbon.userData = { offset: r * 1000 };
        ribbons.push(ribbon); group.add(ribbon);
      }
      return { ribbons };
    }

    function buildSakura() {
      // Cherry blossom petals
      const petals = [];
      for (let i=0;i<50;i++) {
        const geo = new THREE.CircleGeometry(0.2+Math.random()*0.3, 5);
        const mat = new THREE.MeshPhongMaterial({
          color: new THREE.Color().setHSL(0.93,0.7,0.7+Math.random()*0.3),
          side:THREE.DoubleSide,transparent:true,opacity:0.8
        });
        const petal = new THREE.Mesh(geo,mat);
        petal.position.set((Math.random()-0.5)*40, (Math.random()-0.5)*35, (Math.random()-0.5)*20);
        petal.userData={
          rs:(Math.random()-0.5)*0.04,ry:(Math.random()-0.5)*0.04,rz:(Math.random()-0.5)*0.03,
          fall:0.02+Math.random()*0.04, sway:0.01+Math.random()*0.02, baseY:petal.position.y, swayPhase:Math.random()*Math.PI*2
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

    // ---- Mouse Interaction ----
    let mouseX = 0, mouseY = 0, targetMX = 0, targetMY = 0;
    document.addEventListener('mousemove', e => {
      targetMX = (e.clientX / window.innerWidth) * 2 - 1;
      targetMY = -(e.clientY / window.innerHeight) * 2 + 1;
    });

    // ---- Animation Loop ----
    const clock = new THREE.Clock();
    function animate() {
      requestAnimationFrame(animate);
      const t = clock.getElapsedTime();

      // Smooth mouse
      mouseX += (targetMX - mouseX) * 0.05;
      mouseY += (targetMY - mouseY) * 0.05;

      // Camera follow mouse
      camera.position.x += (mouseX * 3 - camera.position.x) * 0.02;
      camera.position.y += (mouseY * 2 - camera.position.y) * 0.02;
      camera.lookAt(0, 0, 0);

      // Animate dynamic objects
      const objs = dynamicObjects;
      if (objs) {
        // Shapes (default)
        if (objs.shapes) {
          objs.shapes.forEach(s => {
            s.rotation.x += s.userData.rotSpeed.x;
            s.rotation.y += s.userData.rotSpeed.y;
            s.rotation.z += s.userData.rotSpeed.z;
            s.position.y = s.userData.baseY + Math.sin(t * s.userData.floatSpeed) * s.userData.floatAmp;
          });
          if (objs.stars) objs.stars.rotation.y += 0.0003;
        }
        // Galaxy
        if (objs.particles) {
          objs.particles.rotation.y += 0.001;
          objs.particles.rotation.x += 0.0003;
        }
        // Academy
        if (objs.items) {
          objs.items.forEach(it => {
            it.rotation.x += it.userData.rs;
            it.rotation.y += it.userData.ry;
            it.position.y = it.userData.baseY + Math.sin(t * it.userData.float) * it.userData.amp;
          });
        }
        // Anime
        if (objs.cards) {
          objs.cards.forEach(c => {
            c.rotation.x += c.userData.rs;
            c.rotation.y += c.userData.ry;
            c.rotation.z += c.userData.rz;
            c.position.y = c.userData.baseY + Math.sin(t * c.userData.float) * c.userData.amp;
          });
        }
        // Cyber
        if (objs.wf) {
          objs.wf.forEach(k => {
            k.rotation.x += k.userData.rs;
            k.rotation.y += k.userData.ry;
            k.position.y = k.userData.baseY + Math.sin(t * k.userData.float) * k.userData.amp;
          });
        }
        // Nature
        if (objs.leaves) {
          objs.leaves.forEach(l => {
            l.rotation.x += l.userData.rs;
            l.rotation.y += l.userData.ry;
            l.rotation.z += l.userData.rz;
            l.position.y = l.userData.baseY + Math.sin(t * l.userData.float) * l.userData.amp;
          });
        }
        // Void
        if (objs.ribbons) {
          objs.ribbons.forEach((rib, i) => {
            rib.rotation.z += 0.003;
            rib.position.x = Math.sin(t * 0.5 + i) * 3;
          });
        }
        // Sakura
        if (objs.petals) {
          objs.petals.forEach(p => {
            p.rotation.x += p.userData.rs;
            p.rotation.y += p.userData.ry;
            p.rotation.z += p.userData.rz;
            p.position.y -= p.userData.fall;
            p.position.x += Math.sin(t * 2 + p.userData.swayPhase) * p.userData.sway;
            if (p.position.y < -20) { p.position.y = 20; p.position.x = (Math.random()-0.5)*40; }
          });
        }
      }

      // Light animation
      pointLight.intensity = 0.5 + Math.sin(t * 1.5) * 0.2;

      renderer.render(scene, camera);
    }

    // ---- Resize ----
    window.addEventListener('resize', () => {
      const nW = window.innerWidth;
      const nH = Math.max(document.documentElement.scrollHeight, window.innerHeight);
      camera.aspect = nW / nH;
      camera.updateProjectionMatrix();
      renderer.setSize(nW, nH);
    });

    // Scroll update (for dynamic height pages)
    let scrollTimeout;
    window.addEventListener('scroll', () => {
      clearTimeout(scrollTimeout);
      scrollTimeout = setTimeout(() => {
        const nH = Math.max(document.documentElement.scrollHeight, window.innerHeight);
        renderer.setSize(window.innerWidth, nH);
        camera.aspect = window.innerWidth / nH;
        camera.updateProjectionMatrix();
      }, 150);
    });

    animate();
  }

  loadThree(init3D);
})();

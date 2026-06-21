#!/usr/bin/env python3
"""
龙奕学院 v4.0 — 大规模升级构建脚本
生成: 日夜模式系统 / 动态背景 / 数字人换装+LLM交互 / 登录注册重做 / 学院功能丰富化
"""

import os

BASE = r"C:\Users\28767\Downloads\cosrealm-site"

def w(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  OK {os.path.basename(path)} ({len(content)} chars)")

# ============================================================
# 1. 日夜模式主题切换系统 — theme-toggle.js
# ============================================================
w(os.path.join(BASE, "assets", "theme-toggle.js"), '''\
// ====== 龙奕学院 Theme Toggle v1.0 ======
// 全局日间/夜间模式切换，支持所有8个学院主题
(function(){
  const KEY = 'longyi-theme';
  const MODES = ['light','dark'];
  
  function get(){ try{return localStorage.getItem(KEY)||'light';}catch(e){return 'light';} }
  function set(m){
    try{localStorage.setItem(KEY,m);}catch(e){}
    apply(m);
  }
  
  function apply(mode){
    const root = document.documentElement;
    // Remove both, then add current
    root.classList.remove('theme-light','theme-dark');
    root.classList.add('theme-'+mode);
    
    // Update toggle button if exists
    const btn = document.getElementById('themeToggle');
    if(btn){
      btn.innerHTML = mode==='dark'
        ? '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>'
        : '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/></svg>';
      btn.title = mode==='dark'?'切换到日间模式':'切换到夜间模式';
    }
    
    // Dispatch event for other components
    window.dispatchEvent(new CustomEvent('themeChange',{detail:{mode}}));
    
    // Update meta theme-color
    let meta = document.querySelector('meta[name=theme-color]');
    if(!meta){
      meta = document.createElement('meta'); meta.name='theme-color';
      document.head.appendChild(meta);
    }
    meta.content = mode==='dark'?'#0a0a1a':'#fafaff';
    
    // Animate transition
    document.body.style.transition = 'background-color 0.4s ease, color 0.3s ease';
    setTimeout(()=>{document.body.style.transition='';},500);
  }
  
  // Init
  apply(get());
  
  // Toggle button handler
  document.addEventListener('click',function(e){
    if(e.target.closest('#themeToggle')){
      set(get()==='dark'?'light':'dark');
    }
  });
  
  // Keyboard shortcut: Ctrl/Cmd + Shift + D
  document.addEventListener('keydown',function(e){
    if((e.ctrlKey||e.metaKey) && e.shiftKey && e.key.toLowerCase()==='d'){
      e.preventDefault();
      set(get()==='dark'?'light':'dark');
    }
  });
  
  // Expose globally
  window.LongYiTheme={get,set,apply};
})();
''')

# ============================================================
# 2. 暗色模式覆盖CSS — dark-mode.css
# ============================================================
w(os.path.join(BASE, "assets", "themes", "dark-mode.css"), '''\
/* ====== 龙奕学院 Dark Mode Overrides ====== */
/* 配合 theme-toggle.js，当 html.theme-dark 时自动生效 */

/* === 基础变量覆盖（暗色通用） === */
.theme-dark {
  --bg-primary: #0a0a1a;
  --bg-secondary: #12122a;
  --bg-card: rgba(20,20,45,0.85);
  --bg-card-hover: rgba(30,30,60,0.9);
  --text: #e0e0f0;
  --text-secondary: #a0a0c0;
  --text-muted: #666690;
  --border: rgba(255,255,255,0.08);
  --shadow-sm: 0 2px 8px rgba(0,0,0,0.3);
  --shadow-md: 0 4px 16px rgba(0,0,0,0.35);
  --shadow-lg: 0 8px 32px rgba(0,0,0,0.4);
  --nav-bg: rgba(10,10,26,0.92);
  --gradient-hero: linear-gradient(135deg,#6366f1,#8b5cf6);
  --gradient-card: linear-gradient(145deg, rgba(99,102,241,0.08), rgba(139,92,246,0.06));
  --accent-glow: 0 0 25px rgba(99,102,241,0.25);
}

/* 暗色导航栏 */
.theme-dark .nav-bar {
  background: var(--nav-bg);
  border-bottom-color: rgba(255,255,255,0.08);
}
.theme-dark .nav-dropdown-menu {
  background: rgba(15,15,35,0.98);
  border-color: rgba(255,255,255,0.1);
  box-shadow: 0 12px 40px rgba(0,0,0,0.5);
}

/* 暗色卡片 */
.theme-dark .card, .theme-dark .card-anime, .theme-dark .card-kawaii,
.theme-dark .stat-card {
  background: var(--bg-card);
  border-color: var(--border);
  color: var(--text);
}
.theme-dark .card:hover, .theme-dark .card-anime:hover {
  background: var(--bg-card-hover);
  transform: translateY(-4px) scale(1.01);
  box-shadow: var(--shadow-lg), 0 0 30px rgba(99,102,241,0.1);
}

/* Hero 区域 */
.theme-dark .hero-section {
  background: linear-gradient(160deg, #0a0a2e 0%, #1a1a3e 40%, #0d0d25 100%);
}
.theme-dark .hero-title {
  background: linear-gradient(135deg, #c4b5fd, #818cf8, #f0abfc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* 表单元素暗色 */
.theme-dark input, .theme-dark textarea, .theme-dark select {
  background: rgba(20,20,45,0.8);
  color: var(--text);
  border-color: rgba(255,255,255,0.12);
}
.theme-dark input:focus, .theme-dark textarea:focus {
  border-color: #6366f1;
  box-shadow: 0 0 0 3px rgba(99,102,241,0.2);
}
.theme-dark input::placeholder { color: var(--text-muted); }

/* 按钮 */
.theme-dark .btn-primary {
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  color: #fff;
  box-shadow: 0 4px 15px rgba(99,102,241,0.3);
}
.theme-dark .btn-secondary {
  background: rgba(255,255,255,0.08);
  color: var(--text-secondary);
  border: 1px solid rgba(255,255,255,0.12);
}

/* 滚动条 */
.theme-dark ::-webkit-scrollbar { width: 6px; }
.theme-dark ::-webkit-scrollbar-track { background: transparent; }
.theme-dark ::-webkit-scrollbar-thumb { 
  background: rgba(99,102,241,0.3); border-radius: 3px; 
}

/* 页脚 */
.theme-dark footer {
  background: #06061a;
  border-top-color: rgba(255,255,255,0.06);
}

/* 侧边栏 */
.theme-dark .social-sidebar nav a, .theme-dark aside a {
  color: var(--text-secondary);
}
.theme-dark .social-sidebar nav a:hover, .theme-dark aside a.active {
  color: #8b5cf6;
  background: rgba(139,92,246,0.1);
}

/* 特效层适配 */
.theme-dark .effects-canvas { opacity: 0.6; }
.theme-dark .cursor-glow { opacity: 0.4; }

/* 平滑过渡 */
.theme-dark *, *::before, *::after {
  transition: background-color 0.3s ease, color 0.25s ease, border-color 0.3s ease, box-shadow 0.3s ease;
}
.theme-dark .nav-bar, .theme-dark .hero-section,
.theme-dark .cursor-glow, .theme-dark .click-burst,
.theme-dark .effects-canvas { transition: none; }
''')

# ============================================================
# 3. 动态背景引擎 — dynamic-bg.js
# ============================================================
w(os.path.join(BASE, "assets", "dynamic-bg.js"), '''\
// ====== 龙奕学院 Dynamic Background Engine v1.0 ======
// 高质量动态背景：粒子星空/流动极光/渐变波浪/星云漩涡/矩阵雨
(function(){
  const canvas = document.createElement('canvas');
  canvas.id = 'dynamicBg';
  canvas.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;z-index:-1;pointer-events:none;';
  document.body.prepend(canvas);
  
  const ctx = canvas.getContext('2d');
  let W,H,particles=[],stars=[];
  let animId,time=0;
  // 背景类型：auto/stars/aurora/waves/nebula/matrix/fireflies
  let bgType = document.documentElement.dataset.bg || 'auto';
  const isDark = () => document.documentElement.classList.contains('theme-dark');
  
  function resize(){
    W=canvas.width=window.innerWidth;
    H=canvas.height=window.innerHeight;
    initScene();
  }
  
  // ---- 粒子类 ----
  class Particle{
    constructor(type){
      this.type=type;
      this.reset();
    }
    reset(){
      this.x=Math.random()*W;
      this.y=Math.random()*H;
      this.size=Math.random()*2.5+0.5;
      this.speedX=(Math.random()-0.5)*0.4;
      this.speedY=(Math.random()-0.5)*0.4;
      this.alpha=Math.random()*0.6+0.2;
      this.life=1;
      this.decay=Math.random()*0.002+0.001;
      // Color based on type
      const colors={
        star:['#fff','#a5b4fc','#c4b5fd','#fde68a'],
        firefly:['#86efac','#a78bfa','#fbbf24','#f472b6'],
        dust:['#6366f1','#8b5cf6','#a78bfa','#c4b5fd']
      };
      const c=colors[this.type]||colors.star;
      this.color=c[Math.floor(Math.random()*c.length)];
      // For fireflies: pulsing
      this.pulse=Math.random()*Math.PI*2;
      this.pulseSpeed=Math.random()*0.03+0.01;
    }
    update(){
      this.x+=this.speedX;
      this.y+=this.speedY;
      this.life-=this.decay;
      if(this.type==='firefly'){
        this.pulse+=this.pulseSpeed;
      }
      if(this.life<=0||this.x<-10||this.x>W+10||this.y<-10||this.y>H+10)this.reset();
    }
    draw(){
      ctx.save();
      let alpha=this.alpha*this.life;
      if(this.type==='firefly'){
        alpha*=0.5+0.5*Math.sin(this.pulse);
        // Glow effect
        ctx.shadowBlur=12;ctx.shadowColor=this.color;
      }
      ctx.globalAlpha=Math.max(0,alpha);
      ctx.fillStyle=this.color;
      ctx.beginPath();
      ctx.arc(this.x,this.y,this.size,0,Math.PI*2);
      ctx.fill();
      ctx.restore();
    }
  }
  
  // ---- 初始化场景 ----
  function initScene(){
    particles=[];stars=[];
    const autoType=isDark()?'stars':'aurora';
    const t=(bgType==='auto')?autoType:bgType;
    const counts={stars:150,aurora:50,waves:80,nebula:100,matrix:80,fireflies:40};
    const count=counts[t]||80;
    const types={stars:'star',aurora:'dust',waves:'dust',nebula:'dust',matrix:'dust',fireflies:'firefly'};
    for(let i=0;i<count;i++) particles.push(new Particle(types[t]||'star'));
    // Stars layer for dark mode
    if(t==='stars'||t==='nebula'||isDark()){
      for(let i=0;i<120;i++){
        stars.push({x:Math.random()*W,y:Math.random()*H,s:Math.random()*1.8+0.3,a:Math.random()*0.8+0.1,twinkle:Math.random()*Math.PI*2});
      }
    }
  }
  
  // ---- 绘制背景底色 ----
  function drawBase(){
    const t=(bgType==='auto')?(isDark()?'stars':'aurora'):bgType;
    if(t==='matrix'){
      ctx.fillStyle='#000005';ctx.fillRect(0,0,W,H);
    }else if(isDark()){
      const grad=ctx.createRadialGradient(W*0.3,H*0.3,0,W*0.5,H*0.5,W*0.9);
      grad.addColorStop(0,'#12122e');
      grad.addColorStop(0.5,'#0a0a1e');
      grad.addColorStop(1,'#050510');
      ctx.fillStyle=grad;ctx.fillRect(0,0,W,H);
    }else{
      const grad=ctx.createLinearGradient(0,0,W,H);
      grad.addColorStop(0,'#f0eeff');
      grad.addColorStop(0.3,'#e8e0ff');
      grad.addColorStop(0.6,'#ffeef5');
      grad.addColorStop(1,'#f0f4ff');
      ctx.fillStyle=grad;ctx.fillRect(0,0,W,H);
    }
  }
  
  // ---- 极光效果 ----
  function drawAurora(){
    time+=0.003;
    for(let i=0;i<3;i++){
      ctx.save();
      ctx.globalAlpha=0.06+i*0.02;
      const grad=ctx.createLinearGradient(
        Math.sin(time+i)*W*0.3,-100,
        Math.cos(time*0.7+i)*W*0.7,H*0.6
      );
      const hues=[[167,240],[220,170],[260,200]];
      const h=hues[i];
      grad.addColorStop(0,`hsla(${h[0]},80%,70%,0)`);
      grad.addColorStop(0.5,`hsla(${h[0]},80%,65%,0.8)`);
      grad.addColorStop(1,`hsla(${h[0]},80%,70%,0)`);
      ctx.fillStyle=grad;
      ctx.beginPath();
      ctx.moveTo(-100,H*0.3);
      for(let x=0;x<=W;x+=20){
        const y=H*(0.2+0.15*Math.sin(x*0.003+time*(1+i*0.3))+i*0.05);
        ctx.lineTo(x,y);
      }
      ctx.lineTo(W+100,-100);ctx.closePath();ctx.fill();
      ctx.restore();
    }
  }
  
  // ---- 波浪效果 ----
  function drawWaves(){
    time+=0.008;
    for(let l=0;l<3;l++){
      ctx.save();ctx.globalAlpha=0.04+l*0.02;
      ctx.fillStyle=l===0?'#6366f1':l===1?'#8b5cf6':'#a78bfa';
      ctx.beginPath();ctx.moveTo(0,H);
      for(let x=0;x<=W;x+=5){
        const y=H-H*(0.15+l*0.1)+Math.sin(x*0.008+time+l)*20*Math.cos(time*0.5+l);
        ctx.lineTo(x,y);
      }
      ctx.lineTo(W,H);ctx.closePath();ctx.fill();ctx.restore();
    }
  }
  
  // ---- 星云漩涡 ----
  function drawNebula(){
    time+=0.002;
    const cx=W*0.5,cy=H*0.4;
    for(let i=0;i<5;i++){
      ctx.save();
      const r=100+i*60+Math.sin(time+i)*20;
      const grad=cx.createRadialGradient(cx,cy,0,cx,cy,r);
      const h=(280+i*20)%360;
      grad.addColorStop(0,`hsla(${h},70%,50%,${0.04-i*0.006})`);
      grad.addColorStop(1,'transparent');
      ctx.fillStyle=grad;
      ctx.beginPath();ctx.arc(cx,cy,r,0,Math.PI*2);ctx.fill();
      ctx.restore();
    }
    // Swirl lines
    ctx.save();ctx.strokeStyle='rgba(167,139,250,0.03)';ctx.lineWidth=1;
    for(let s=0;s<8;s++){
      ctx.beginPath();
      for(let a=0;a<Math.PI*4;a+=0.05){
        const rr=30+s*25+a*8;
        const x=cx+Math.cos(a+time+s)*rr;
        const y=cy+Math.sin(a+time+s)*rr*0.6;
        a===0?ctx.moveTo(x,y):ctx.lineTo(x,y);
      }
      ctx.stroke();
    }
    ctx.restore();
  }
  
  // ---- 矩阵雨 ----
  let matrixDrops=[];
  function initMatrix(){matrixDrops=[];const cols=Math.floor(W/16);for(let i=0;i<cols;i++)matrixDrops.push({y:Math.random()*H,s:Math.random()*0.5+0.5});}
  function drawMatrix(){
    ctx.fillStyle='rgba(0,0,5,0.1)';ctx.fillRect(0,0,W,H);
    ctx.font='14px monospace';
    matrixDrops.forEach(d=>{
      const char=String.fromCharCode(0x30A0+Math.random()*96);
      const x=matrixDrops.indexOf(d)*16;
      ctx.fillStyle=d.s>0.8?'#a78bfa':`rgba(139,92,246,${d.s*0.5})`;
      ctx.fillText(char,x,d.y);
      d.y+=d.s*16;
      if(d.y>H)d.y=0;d.s=Math.random()*0.5+0.5;
    });
  }
  
  // ---- 星星闪烁 ----
  function drawStars(){
    stars.forEach(s=>{
      s.twinkle+=0.02;
      const a=s.a*(0.5+0.5*Math.sin(s.twinkle));
      ctx.save();ctx.globalAlpha=a;ctx.fillStyle='#fff';
      ctx.shadowBlur=3;ctx.shadowColor='#a5b4fc';
      ctx.beginPath();ctx.arc(s.x,s.y,s.s,0,Math.PI*2);ctx.fill();
      ctx.restore();
    });
  }
  
  // ---- 主循环 ----
  function animate(){
    ctx.clearRect(0,0,W,H);
    const t=(bgType==='auto')?(isDark()?'stars':'aurora'):bgType;
    
    if(t==='matrix'){drawMatrix();}
    else{drawBase();if(t==='aurora')drawAurora();else if(t==='waves')drawWaves();else if(t==='nebula')drawNebula();}
    
    if(t!=='matrix')drawStars();
    particles.forEach(p=>{p.update();p.draw();});
    
    animId=requestAnimationFrame(animate);
  }
  
  // Listen for theme changes
  window.addEventListener('themeChange',()=>{initScene();});
  
  // Start
  resize();window.addEventListener('resize',resize);
  if(bgType==='matrix')initMatrix();
  animate();
})();
''')

# ============================================================
# 4. 导航栏添加日夜切换按钮 — 更新 nav.js
# ============================================================
# 在 nav-actions 区域插入主题切换按钮
nav_js_path = os.path.join(BASE, "assets", "nav.js")
with open(nav_js_path, 'r', encoding='utf-8') as f:
    nav_content = f.read()

# Add theme toggle button before the login button in nav-actions
nav_updated = nav_content.replace(
    '''<div class="nav-actions">
        <a href="%ROOT%pages/auth/login.html" class="nav-btn nav-btn-login">登录</a>''',
    '''<div class="nav-actions">
        <button id="themeToggle" class="nav-btn nav-theme-toggle" title="切换日夜间模式" aria-label="主题切换">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/></svg>
        </button>
        <a href="%ROOT%pages/auth/login.html" class="nav-btn nav-btn-login">登录</a>'''
)
w(nav_js_path, nav_updated)

# ============================================================
# 5. 数字人3D换装 + 商品试穿系统 — dressup.html
# ============================================================
dressup_html = '''\
<!DOCTYPE html>
<html lang="zh-CN" data-3d="academy" data-bg="nebula">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>数字人换装工坊 — 龙奕学院 LongYi Academy</title>
<link rel="stylesheet" href="../../assets/style.css">
<link rel="stylesheet" href="../../assets/themes/academy/starlight-academy.css">
<link rel="stylesheet" href="../../assets/themes/dark-mode.css">
<link rel="stylesheet" href="../../assets/effects-layer.css">
<style>
.dressup-layout{display:flex;gap:24px;padding:24px;max-width:1500px;margin:0 auto;min-height:calc(100vh - 140px);}
.dressup-main{flex:1;display:flex;flex-direction:column;gap:20px;min-width:0;}
.dressup-sidebar{width:320px;flex-shrink:0;display:flex;flex-direction:column;gap:16px;}

/* === 数字人展示区 === */
.avatar-stage{
  position:relative;width:100%;height:520px;border-radius:20px;
  background:linear-gradient(180deg,#0d0d25 0%,#1a1a3e 50%,#12122a 100%);
  border:1px solid rgba(167,139,250,0.2);overflow:hidden;
  display:flex;align-items:center;justify-content:center;
}
.avatar-canvas-wrapper{position:relative;width:380px;height:480px;}
.avatar-placeholder{
  width:100%;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;
  gap:12px;color:#a78bfa;font-size:0.9rem;
}
.avatar-silhouette{font-size:180px;line-height:1;filter:drop-shadow(0 0 30px rgba(167,139,250,0.3));animation:breathe 3s ease-in-out infinite;}
@keyframes breathe{0%,100%{transform:scale(1);}50%{transform:scale(1.03));}}
.stage-controls{
  position:absolute;bottom:16px;left:50%;transform:translateX(-50%);
  display:flex;gap:8px;z-index:2;
}
.stage-btn{
  padding:8px 16px;border-radius:20px;background:rgba(255,255,255,0.1);
  backdrop-filter:blur(10px);color:#e0e0f0;border:1px solid rgba(255,255,255,0.1);
  cursor:pointer;font-size:0.82rem;transition:all 0.25s;
}
.stage-btn:hover{background:rgba(167,139,250,0.2);border-color:#a78bfa;}

/* === 分类标签栏 === */
.category-tabs{display:flex;gap:6px;flex-wrap:wrap;padding:4px 0;}
.cat-tab{
  padding:8px 18px;border-radius:20px;font-size:0.85rem;font-weight:600;
  background:rgba(99,102,241,0.08);color:#6366f1;border:1px solid rgba(99,102,241,0.15);
  cursor:pointer;transition:all 0.25s;white-space:nowrap;
}
.cat-tab:hover,.cat-tab.active{
  background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;
  border-color:transparent;box-shadow:0 4px 15px rgba(99,102,241,0.3);
}

/* === 商品网格 === */
.items-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:12px;}
.item-card{
  aspect-ratio:1;border-radius:14px;overflow:hidden;cursor:pointer;position:relative;
  background:rgba(20,20,45,0.7);border:2px solid transparent;transition:all 0.3s;
}
.item-card:hover{border-color:#a78bfa;transform:translateY(-4px) scale(1.03);box-shadow:0 8px 25px rgba(167,139,250,0.2);}
.item-card.equipped{border-color:#22c55e;box-shadow:0 0 15px rgba(34,197,94,0.3);}
.item-thumb{
  width:100%;height:70%;object-fit:cover;background:linear-gradient(135deg,#2a2a4a,#1a1a3e);
  display:flex;align-items:center;justify-content:center;font-size:2rem;
}
.item-info{padding:8px;text-align:center;}
.item-name{font-size:0.78rem;color:#e0e0f0;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.item-price{font-size:0.75rem;color:#f472b6;font-weight:700;margin-top:2px;}
.item-badge{
  position:absolute;top:6px;right:6px;padding:2px 8px;border-radius:8px;
  font-size:0.68rem;font-weight:700;
}
.badge-new{background:#22c55e;color:#fff;}
.badge-hot{background:#ef4444;color:#fff;}
.badge-limited{background:#f59e0b;color:#000;}

/* === 穿搭面板 === */
.outfit-panel{
  background:rgba(20,20,45,0.85);border-radius:16px;padding:20px;
  border:1px solid rgba(167,139,250,0.15);
}
.panel-title{font-size:1rem;font-weight:700;color:#e0e0f0;margin-bottom:14px;display:flex;align-items:center;gap:8px;}
.current-outfit{display:flex;flex-direction:column;gap:10px;}
.outfit-slot{
  display:flex;align-items:center;gap:10px;padding:10px 14px;
  background:rgba(255,255,255,0.04);border-radius:10px;
  border:1px dashed rgba(255,255,255,0.1);cursor:pointer;transition:all 0.25s;
}
.outfit-slot:hover{border-color:#a78bfa;background:rgba(167,139,250,0.05);}
.slot-icon{font-size:1.4rem;width:32px;text-align:center;}
.slot-name{flex:1;font-size:0.85rem;color:#c4b5fd;font-weight:600;}
.slot-empty{color:#555;font-style italic;}

/* === 商品详情浮窗 === */
.product-modal-overlay{
  position:fixed;top:0;left:0;right:0;bottom:0;
  background:rgba(0,0,0,0.7);backdrop-filter:blur(8px);
  z-index:3000;display:none;align-items:center;justify-content:center;
}
.product-modal-overlay.show{display:flex;}
.product-modal{
  background:#16162e;border-radius:20px;width:480px;max-height:80vh;overflow-y:auto;
  border:1px solid rgba(167,139,250,0.25);box-shadow:0 20px 60px rgba(0,0,0,0.5);
}
.modal-image{
  width:100%;height:260px;object-fit:cover;border-radius:20px 20px 0 0;
  background:linear-gradient(135deg,#2a2a5a,#1a1a3e);
  display:flex;align-items:center;justify-content:center;font-size:4rem;
}
.modal-body{padding:20px;}
.modal-title{font-size:1.2rem;font-weight:800;color:#fff;margin-bottom:6px;}
.modal-desc{font-size:0.85rem;color:#a0a0c0;line-height:1.7;margin-bottom:14px;}
.modal-meta{display:flex;gap:16px;margin-bottom:16px;flex-wrap:wrap;}
.meta-tag{padding:4px 12px;border-radius:8px;font-size:0.78rem;background:rgba(99,102,241,0.15);color:#a5b4fc;}
.modal-price-row{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;}
.modal-price{font-size:1.4rem;font-weight:800;color:#f472b6;}
.modal-actions{display:flex;gap:10px;}
.btn-tryon{flex:1;padding:12px;border-radius:12px;background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;font-weight:700;border:none;cursor:pointer;font-size:0.95rem;transition:all 0.25s;}
.btn-tryon:hover{transform:translateY(-2px);box-shadow:0 6px 20px rgba(99,102,241,0.4);}
.btn-buy{flex:1;padding:12px;border-radius:12px;background:linear-gradient(135deg,#f472b6,#ec4899);color:#fff;font-weight:700;border:none;cursor:pointer;font-size:0.95rem;transition:all 0.25s;}
.btn-buy:hover{transform:translateY(-2px);box-shadow:0 6px 20px rgba(244,114,182,0.4);}

/* === 预设搭配 === */
.presets-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;}
.preset-card{
  padding:12px;border-radius:12px;background:rgba(255,255,255,0.04);
  border:1px solid rgba(255,255,255,0.08);cursor:pointer;transition:all 0.25s;text-align:center;
}
.preset-card:hover{border-color:#a78bfa;background:rgba(167,139,250,0.08);}
.preset-icon{font-size:1.6rem;margin-bottom:4px;}
.preset-name{font-size:0.8rem;color:#c4b5fd;font-weight:600;}

/* === 旋转控制 === */
.rotate-hint{
  position:absolute;bottom:16px;right:16px;font-size:0.75rem;color:rgba(167,139,250,0.5);
  display:flex;align-items:center;gap:4px;pointer-events:none;
}
</style>
</head>
<body>

<div class="avatar-stage" id="avatarStage">
  <div class="avatar-canvas-wrapper">
    <div class="avatar-placeholder" id="avatarPlaceholder">
      <div class="avatar-silhouette">🧑‍🎤</div>
      <span>拖拽旋转 · 滚轮缩放 · 点击试穿</span>
    </div>
  </div>
  <div class="stage-controls">
    <button class="stage-btn" onclick="rotateAvatar(-1)">↺ 左旋</button>
    <button class="stage-btn" onclick="resetPose()">⊙ 正面</button>
    <button class="stage-btn" onclick="rotateAvatar(1)">右旋 ↻</button>
    <button class="stage-btn" onclick="toggleAnimation()">✨ 动作</button>
    <button class="stage-btn" onclick="snapshot()">📸 截图</button>
  </div>
  <div class="rotate-hint">🖱️ 拖拽旋转视角</div>
</div>

<div class="dressup-layout">
  <!-- 左侧主区域 -->
  <div class="dressup-main">
    <!-- 分类标签 -->
    <div class="category-tabs" id="categoryTabs">
      <div class="cat-tab active" data-cat="hair">💇 发型</div>
      <div class="cat-tab" data-cat="face">😊 面部</div>
      <div class="cat-tab" data-cat="top">👕 上装</div>
      <div class="cat-tab" data-cat="bottom">👖 下装</div>
      <div class="cat-tab" data-cat="shoes">👟 鞋履</div>
      <div class="cat-tab" data-cat="acc">🎀 配饰</div>
      <div class="cat-tab" data-cat="prop">⚔️ 道具</div>
      <div class="cat-tab" data-cat="effect">✨ 特效</div>
      <div class="cat-tab" data-cat="bg">🎭 背景</div>
    </div>

    <!-- 商品列表 -->
    <div class="items-grid" id="itemsGrid"></div>
  </div>

  <!-- 右侧面板 -->
  <div class="dressup-sidebar">
    <!-- 当前穿搭 -->
    <div class="outfit-panel">
      <div class="panel-title">👔 当前穿搭</div>
      <div class="current-outfit" id="currentOutfit">
        <div class="outfit-slot" onclick="selectCategory('hair')"><div class="slot-icon">💇</div><div class="slot-name slot-empty">选择发型...</div></div>
        <div class="outfit-slot" onclick="selectCategory('top')"><div class="slot-icon">👕</div><div class="slot-name slot-empty">选择上装...</div></div>
        <div class="outfit-slot" onclick="selectCategory('bottom')"><div class="slot-icon">👖</div><div class="slot-name slot-empty">选择下装...</div></div>
        <div class="outfit-slot" onclick="selectCategory('shoes')"><div class="slot-icon">👟</div><div class="slot-name slot-empty">选择鞋履...</div></div>
        <div class="outfit-slot" onclick="selectCategory('acc')"><div class="slot-icon">🎀</div><div class="slot-name slot-empty">选择配饰...</div></div>
        <div class="outfit-slot" onclick="selectCategory('prop')"><div class="slot-icon">⚔️</div><div class="slot-name slot-empty">选择道具...</div></div>
      </div>
    </div>

    <!-- 预设搭配 -->
    <div class="outfit-panel">
      <div class="panel-title">🌟 推荐搭配</div>
      <div class="presets-grid" id="presetsGrid"></div>
    </div>

    <!-- 统计 -->
    <div class="outfit-panel">
      <div class="panel-title">📊 穿搭统计</div>
      <div style="display:flex;flex-direction:column;gap:8px;">
        <div style="display:flex;justify-content:space-between;font-size:0.85rem;"><span style="color:#a0a0c0;">已穿戴部件</span><span style="color:#22c55e;font-weight:700;" id="equippedCount">0/6</span></div>
        <div style="display:flex;justify-content:space-between;font-size:0.85rem;"><span style="color:#a0a0c0;">总价值</span><span style="color:#f472b6;font-weight:700;" id="totalValue">¥0</span></div>
        <div style="display:flex;justify-content:space-between;font-size:0.85rem;"><span style="color:#a0a0c0;">风格评分</span><span style="color:#fbbf24;font-weight:700;" id="styleScore">--</span></div>
      </div>
    </div>
  </div>
</div>

<!-- 商品详情弹窗 -->
<div class="product-modal-overlay" id="productModal" onclick="if(event.target===this)closeModal()">
  <div class="product-modal" id="productModalContent"></div>
</div>

<script src="../../assets/three-engine.js"></script>
<script src="../../assets/nav.js"></script>
<script src="../../assets/theme-toggle.js"></script>
<script src="../../assets/effects-runtime.js"></script>
<script src="../../assets/dynamic-bg.js"></script>
<script>
// ====== 数据 ======
const ITEMS_DB = {
  hair:[
    {id:'h1',name:'樱粉双马尾',price:128,icon:'🎀',thumb:'#FFB7C5',badge:'hot',desc:'经典二次元双马尾造型，樱花粉色渐变发丝，自带微光粒子特效。适合甜美系角色扮演。',tags:['甜美','日常','热门']},
    {id:'h2',name:'银白长直发',price:158,icon:'🤍',thumb:'#E8E8F0',badge:'new',desc:'流光银白色长直发，每根发丝都有细腻光泽。高冷御姐风必备。',tags:['高冷','华丽','新上架']},
    {id:'h3',name:'星空渐变挑染',price:198,icon:'🌌',thumb:'#4B0082',badge:'',desc:'深紫到星空蓝的渐变挑染，内嵌细小星光粒子。夜晚模式下发光效果更佳。',tags:['奇幻','赛博','限量']},
    {id:'h4',name:'猫耳短发',price:88,icon:'🐱',thumb:'#FFA07A',badge:'hot',desc:'带猫耳装饰的蓬松短发，耳朵可动。萌系角色首选。',tags:['可爱','萌系','热销']},
    {id:'h5',name:'机械义体发箍',price:268,icon:'⚙️',thumb:'#708090',badge:'limited',desc:'赛博朋克风格机械义体发箍，内置LED灯条。科技感拉满。',tags:['赛博','科幻','限定']},
    {id:'h6',name:'古风步摇发冠',price:218,icon:'🏮',thumb:'#DC143C',badge:'new',desc:'汉服风格步摇发冠，红金配色，镶嵌宝石流苏。古风Cos必备。',tags:['古风','华丽','新品']},
    {id:'h7',name:'火焰渐变刺猬头',price:138,icon:'🔥',thumb:'#FF4500',badge:'',desc:'橙红渐变刺猬头，热血少年漫主角同款。充满能量感。',tags:['热血','运动']},
    {id:'h8',name:'冰晶公主卷',price:178,icon:'❄️',thumb:'#87CEEB',badge:'limited',desc:'淡蓝色大波浪卷发，带有冰晶质感。冰雪女王气质。',tags:['优雅','魔法','限定']},
  ],
  top:[
    {id:'t1',name:'学院JK制服',price:168,icon:'👔',thumb:'#2C3E50',badge:'hot',desc:'经典水手领JK制服，藏青色百褶裙套装。多色可选，支持刺绣定制。',tags:['学院','日常','热销']},
    {id:'t2',name:'机甲战斗装甲',price:398,icon:'🤖',thumb:'#4A4A6A',badge:'new',desc:'全覆式机甲战斗装甲，LED呼吸灯效，可拆卸肩甲和护腕。硬核玩家首选。',tags:['机甲','科幻','新品']},
    {id:'t3',name:'洛丽塔洋装',price:288,icon:'👗',thumb:'#FFB6C1',badge:'hot',desc:'多层蕾丝边洛丽塔裙装，蝴蝶结配饰，蓬蓬裙设计。甜系天花板。',tags:['甜美','洛丽塔','爆款']},
    {id:'t4',name:'汉服交领襦裙',price:238,icon:'🏯',thumb:'#FFFFFF',badge:'',desc:'传统交领襦裙，绣花面料，宽袖飘逸。多朝代款式可选。',tags:['古风','传统文化']},
    {id:'t5',name:'电竞队服夹克',price:198,icon:'🎮',thumb:'#1E90FF',badge:'new',desc:'专业电竞队服外套，透气面料，可自定义队标和ID刺绣。',tags:['电竞','潮流']},
    {id:'t6',name:'魔法少女斗篷',price:258,icon:'🪄',thumb:'#9370DB',badge:'limited',desc:'星空图案魔法斗篷，内衬星光绸缎，披风边缘有流光特效。',tags:['魔法','奇幻','限定']},
    {id:'t7',name:'女仆咖啡厅围裙',price:128,icon:'☕',thumb:'#FFF0F5',badge:'hot',desc:'黑白女仆装围裙套装，含头饰和围裙。漫展打工神器。',tags:['可爱','女仆','热销']},
    {id:'t8',name:'武士道羽织',price:208,icon:'⚔️',thumb:'#222',badge:'',desc:'日式传统羽织外套，龙纹刺绣背面图案。浪人剑客风。',标签:['武士','和风']},
  ],
  bottom:[
    {id:'b1',name:'百褶短裙(黑)',price:88,icon:'🖤',thumb:'#1a1a1a',badge:'hot',desc:'经典黑色百褶短裙，防走光内衬，A字版型。JK制服绝配。',tags:['制服','日常']},
    {id:'b2',name:'机甲战术裤',price:188,icon:'🔫',thumb:'#333',badge:'new',desc:'多功能口袋战术裤，耐磨面料，膝盖处可加装护具。',tags:['机甲','战术']},
    {id:'b3',name:'蕾丝蓬蓬裙',price:148,icon:'🩰',thumb:'#FFE4E1',badge:'',desc:'多层蕾丝蓬蓬裙，纱质外层，内衬安全裤。洛丽塔搭配必备。',tags:['甜美','洛丽塔']},
    {id:'b4',name:'古装马面裙',price:168,icon:'🐉',thumb:'#8B0000',badge:'hot',desc:'明代马面裙，织金面料，前后裙门设计。国风复兴必备单品。',tags:['古风','国潮']},
    {id:'b5',name:'荧光运动短裤',price:68,icon:'🏃',thumb:'#00FF00',badge:'',desc:'反光材质运动短裤，夜跑安全。活力满满的运动风。',tags:['运动','机能']},
    {id:'b6',name:'赛博霓虹腿环',price:118,icon:'💜',thumb:'#8A2BE2',badge:'limited',desc:'LED发光腿环，多种闪烁模式，蓝牙APP可控颜色节奏。',tags:['赛博','限定']},
  ],
  shoes:[
    {id:'s1',name:'圆头皮鞋(黑)',price:128,icon:'👞',thumb:'#111',badge:'hot',desc:'JK制服标配圆头皮鞋，真皮材质，舒适耐穿。',tags:['制服','日常']},
    {id:'s2',name:'机甲动力靴',price:298,icon:'🦿',thumb:'#444',badge:'new',desc:'重型机甲动力靴，内置减震系统和LED推进器灯光。',tags:['机甲','科幻']},
    {id:'s3',name:'水晶高跟鞋',price:168,icon:'👠',thumb:'#E0FFFF',badge:'',desc:'透明水晶材质高跟鞋，内嵌RGB灯光。公主风必备。',tags:['优雅','梦幻']},
    {id:'s4',name:'木屐(桧木)',price:88,icon:'🩴',thumb:'#DEB887',badge:'',desc:'传统日式木屐，桧木材质，齿部防滑处理。和风搭配点睛之笔。',tags:['和风','传统']},
    {id:'s5',name:'发光运动鞋',price:198,icon:'👟',thumb:'#FF1493',badge:'limited',desc:'LED智能运动鞋，手机App控色，支持音乐律动模式。',tags:['潮流','限定']},
    {id:'s6',name:'魔法制服鞋',price:148,icon:'🪄',thumb:'#4B0082',badge:'hot',desc:'魔法少女标配尖头制服鞋，鞋扣为星星形状，带微光效果。',tags:['魔法','可爱']},
  ],
  acc:[
    {id:'a1',name:'猫耳发箍',price:38,icon:'🐱',thumb:'#FFB6C1',badge:'hot',desc:'毛绒猫耳发箍，柔软亲肤，多种颜色可选。萌系入门级配件。',tags:['可爱','入门']},
    {id:'a2',name:'VR眼镜道具',price:258,icon:'🥽',thumb:'#00CED1',badge:'new',desc:'赛博朋克风格VR眼镜道具，可显示自定义HUD动画。',tags:['赛博','科技']},
    {id:'a3',name:'魔法法杖',price:188,icon:'🪄',thumb:'#FFD700',badge:'hot',desc:'LED发光法杖顶端，多色切换，底部电池仓。魔法少女标配武器。',tags:['魔法','道具']},
    {id:'a4',name:'武士刀(未开刃)',price:228,icon='⚔️',thumb:'#C0C0C0',badge:'',desc:'合金材质仿制武士刀，安全无锋，展会可用。刀身刻字可选。',tags:['武士','道具']},
    {id:'a5',name:'天使翅膀背包',price:168,icon:'👼',thumb:'#FFFACD',badge:'limited',desc:'可展开的羽毛翅膀背包，轻量化设计，展翅宽度1.2米。',tags:['天使','限定']},
    {id:'a6',name:'机械臂义肢',price:328,icon:'🦾',thumb:'#708090',badge:'new',desc:'可穿戴式机械臂义肢外观道具，关节可动，手指可弯曲抓握。',tags:['赛博','机甲']},
    {id:'a7',name:'兔耳头饰',price:48,icon:'🐰',thumb:'#FFC0CB',badge:'hot',desc:'毛绒兔耳头饰，可竖起或耷拉两种形态。百搭萌系配件。',tags:['可爱','萌系']},
    {id:'a8',name:'全息项圈',price:98,icon:'💠',thumb:'#00FFFF',badge:'limited',desc:'LED全息投影项圈，可显示自定义文字和图案。赛博风点睛之笔。',tags:['赛博','限定']},
  ],
  prop:[
    {id:'p1',name:'光剑道具',price:198,icon:'🗡️',thumb:'#00BFFF',badge:'hot',desc:'声光联动光剑道具，挥动时有碰撞音效和闪光。多色光刃可选。',tags:['科幻','武器']},
    {id:'p2',name:'魔法书(精装)',price:128,icon:'📕',thumb:'#4A0E4E',badge:'',desc:'复古魔法书外观道具，内页可写内容，封面烫金符文。',tags:['魔法','道具']},
    {id:'p3',name:'枪械模型(玩具)',price:268,icon:'🔫',thumb:'#2F2F2F',badge:'new',desc:'1:1比例枪械外观模型（绝对安全），金属质感涂装，后坐力振动模拟。',标签:['军事','模型']},
    {id:'p4',name:'盾牌(动漫款)',price:158,icon:'🛡️',thumb:'#CD853F',badge:'',desc:'动漫风格手持盾牌，轻量泡沫芯+PVC表面，展会拍照利器。',tags:['战士','道具']},
    {id:'p5',name:'精灵球道具',price:68,icon='🔮',thumb:'#FF0000',badge:'hot',desc:'可开合精灵球道具，内有LED灯光效果。训练师必备。',tags:['精灵','可爱']},
    {id:'p6',name:'吉他(道具版)',price:188,icon:'🎸',thumb:'#DAA520',badge:'',desc:'乐队演出用道具吉他，可调音（仅外观），多种配色可选。',标签:['乐队','乐器']},
  ],
  effect:[
    {id:'e1',name:'樱花飘落特效',price:28,icon:'🌸',thumb:'#FFB7C5',badge:'hot',desc:'数字人周围樱花花瓣持续飘落粒子特效，浪漫氛围感拉满。',tags:['浪漫','自然']},
    {id:'e2',name:'火焰光环',price:38,icon:'🔥',thumb:'#FF4500',badge:'',desc:'脚下燃烧的火焰光环效果，热血战斗场景专用。',tags:['战斗','热血']},
    {id:'e3',name:'星空斗篷光效',price:48,icon:'🌌',thumb:'#4B0082',badge:'limited',desc:'斗篷上的星空流转效果，仿佛把银河披在身上。',tags:['奇幻','限定']},
    {id:'e4',name:'闪电链特效',price:35,icon:'⚡',thumb:'#00FFFF',badge:'new',desc:'指尖释放的闪电链粒子效果，施法动作完美配合。',tags:['魔法','新品']},
    {id:'e5',name:'爱心气泡',price:18,icon:'💕',thumb:'#FF69B4',badge:'hot',desc:'周围冒出的漂浮心形气泡，甜蜜互动氛围。',tags:['可爱','社交']},
    {id:'e6',name:'数据流光环',price:42,icon:'💜',thumb:'#8A2BE2',badge:'',desc:'赛博风格的数据流环绕光环，黑客帝国既视感。',tags:['赛博','科技']},
  ],
  bg:[
    {id:'bg1',name:'樱花大道',price:18,icon:'🌸',thumb:'#FFDDE1',badge:'hot',desc:'春日樱花纷飞的街道背景，柔和暖色调。',tags:['春季','浪漫']},
    {id:'bg2',name:'赛博都市夜景',price:28,icon:'🌃',thumb:'#0A0A20',badge:'new',desc:'霓虹灯闪烁的未来都市夜景，高楼林立。',tags:['赛博','城市']},
    {id:'bg3',name:'魔法学园教室',price:18,icon:'🏫',thumb:'#FFF8DC',badge:'',desc:'阳光洒入的学园教室内景，黑板和课桌。',tags:['校园','日常']},
    {id:'bg4',name:'虚空战场',price:28,icon:'💫',thumb:'#1A0A2E',badge:'',desc:'破碎的大地与紫色天空，史诗战斗场景。',tags:['战斗','史诗']},
    {id:'bg5',name:'星际飞船舱内',price:22,icon:'🚀',thumb:'#2A2A3A',badge:'limited',desc:'科幻风格飞船内部，舷窗外可见星辰。',tags:['科幻','限定']},
    {id:'bg6',name:'和风神社鸟居',price:18,icon:'⛩️',thumb:'#FFEBEE',badge:'hot',desc:'红色鸟居与石灯笼的传统神社场景。',标签:['和风','日本']},
  ]
};

const PRESETS = [
  {name:'JK学院风',icon:'🎓',items:{hair:'h1',top:'t1',bottom:'b1',shoes:'s1',acc:'a1'}},
  {name:'机甲战士',icon:'🤖',items:{hair:'h5',top:'t2',bottom:'b2',shoes:'s2',acc:'a6',prop:'p1'}},
  {name:'洛莉塔甜心',icon:'🍰',items:{hair:'h1',top:'t3',bottom:'b3',shoes:'s3',acc:'a5'}},
  {name:'古风侠客',icon:'🏯',items:{hair:'h6',top:'t8',bottom:'b4',shoes:'s4',prop:'p4'}},
  {name:'魔法少女',icon:'✨',items:{hair:'h3',top:'t6',bottom:'b3',shoes:'s6',acc:'a3',effect:'e3'}},
  {name:'赛博忍者',icon:'🥷',items:{hair:'h5',top:'t2',bottom:'b5',shoes:'s5',acc:'a2',prop:'p1',bg:'bg2'}},
];

// ====== 状态 ======
let currentCat = 'hair';
let equipped = {}; // category -> item
let rotation = 0;

// ====== 渲染商品网格 ======
function renderItems(cat){
  const grid = document.getElementById('itemsGrid');
  const items = ITEMS_DB[cat] || [];
  grid.innerHTML = items.map(item => `
    <div class="item-card ${equipped[cat]?.id===item.id?'equipped':''}" 
         onclick="selectItem('${cat}','${item.id}')"
         ondblclick="showProductDetail('${cat}','${item.id}')">
      <div class="item-thumb" style="background:${item.thumb};">${item.icon}</div>
      <div class="item-info">
        <div class="item-name">${item.name}</div>
        <div class="item-price">¥${item.price}</div>
      </div>
      ${item.badge?`<span class="item-badge badge-${item.badge}">${item.badge==='hot'?'🔥HOT':item.badge==='new'?'NEW':item.badge==='limited'?'限定':''}</span>`:''}
    </div>
  `).join('');
}

// ====== 选择商品 ======
function selectItem(cat, itemId){
  const items = ITEMS_DB[cat] || [];
  const item = items.find(i => i.id === itemId);
  if(!item)return;
  equipped[cat] = item;
  renderItems(cat);
  updateOutfitPanel();
  updateStats();
  updateAvatarVisual();
  // 视觉反馈
  showToast(`已装备 ${item.name}`);
}

// ====== 更新穿搭面板 ======
function updateOutfitPanel(){
  const slots = {
    hair:{icon:'💇',label:'发型'},
    top:{icon:'👕',label:'上装'},
    bottom:{icon:'👖',label:'下装'},
    shoes:{icon:'👟',label:'鞋履'},
    acc:{icon:'🎀',label:'配饰'},
    prop:{icon:'⚔️',label:'道具'}
  };
  let html = '';
  for(const [key,{icon,label}] of Object.entries(slots)){
    const eq = equipped[key];
    html += `<div class="outfit-slot" onclick="selectCategory('${key}')">
      <div class="slot-icon">${icon}</div>
      <div class="slot-name">${eq ? eq.name+' ¥'+eq.price : '<span class="slot-empty">选择'+label+'...</span>'}</div>
    </div>`;
  }
  document.getElementById('currentOutfit').innerHTML = html;
}

// ====== 更新统计 ======
function updateStats(){
  const count = Object.keys(equipped).length;
  const total = Object.values(equipped).reduce((sum,item)=>sum+(item?.price||0),0);
  document.getElementById('equippedCount').textContent = `${count}/6`;
  document.getElementById('totalValue').textContent = `¥${total}`;
  // 简单风格评分算法
  let score = '--';
  if(count >= 3){
    score = Math.min(99, 50 + count*5 + Math.floor(total/50));
    if(equipped.hair&&equipped.top&&equipped.shoes)score+=10;
    if(Object.keys(equipped).length>=5)score+=5;
  }
  document.getElementById('styleScore').textContent = score==='--'?score:score+'/99';
}

// ====== 更新数字人视觉效果 ======
function updateAvatarVisual(){
  const ph = document.getElementById('avatarPlaceholder');
  // 根据已装备物品组合emoji表示
  let look = '🧑‍🎤';
  if(equipped.top){
    const t = equipped.top.id;
    if(t.includes('t2')||t.includes('t8'))look='🤖';
    else if(t.includes('t3'))look='👸';
    else if(t.includes('t6'))look='🧙‍♀️';
    else if(t.includes('t1'))look='🎓';
    else if(t.includes('t4'))look='👘';
    else if(t.includes('t7'))look='🍽️';
  }
  ph.querySelector('.avatar-silhouette').textContent = look;
}

// ====== 分类切换 ======
function selectCategory(cat){
  currentCat = cat;
  document.querySelectorAll('.cat-tab').forEach(t => t.classList.toggle('active', t.dataset.cat === cat));
  renderItems(cat);
}

// ====== 预设搭配渲染 ======
function renderPresets(){
  document.getElementById('presetsGrid').innerHTML = PRESETS.map(p => `
    <div class="preset-card" onclick="applyPreset('${p.name}')" title="${p.name}">
      <div class="preset-icon">${p.icon}</div>
      <div class="preset-name">${p.name}</div>
    </div>
  `).join('');
}

function applyPreset(name){
  const preset = PRESETS.find(p => p.name === name);
  if(!preset)return;
  equipped = {};
  for(const [cat,id] of Object.entries(preset.items)){
    const allItems = ITEMS_DB[cat] || [];
    const item = allItems.find(i => i.id === id);
    if(item)equipped[cat]=item;
  }
  renderItems(currentCat);
  updateOutfitPanel();
  updateStats();
  updateAvatarVisual();
  showToast(`已应用「${name}」搭配`);
}

// ====== 商品详情弹窗 ======
function showProductDetail(cat, itemId){
  const items = ITEMS_DB[cat] || [];
  const item = items.find(i => i.id === itemId);
  if(!item)return;
  const modal = document.getElementById('productModal');
  const content = document.getElementById('productModalContent');
  content.innerHTML = `
    <div class="modal-image" style="background:${item.thumb};">${item.icon}</div>
    <div class="modal-body">
      <div class="modal-title">${item.icon} ${item.name}</div>
      <div class="modal-desc">${item.desc}</div>
      <div class="modal-meta">${(item.tags||[]).map(t=>`<span class="meta-tag">#${t}</span>`).join('')}</div>
      <div class="modal-price-row">
        <span class="modal-price">¥${item.price}</span>
        <span style="color:#a0a0c0;font-size:0.85rem;">已有 ${Math.floor(Math.random()*900)+100} 人购买</span>
      </div>
      <div class="modal-actions">
        <button class="btn-tryon" onclick="selectItem('${cat}','${itemId}');closeModal()">👗 试穿此件</button>
        <button class="btn-buy" onclick="alert('跳转到商城购买页面...')">🛒 立即购买</button>
      </div>
    </div>`;
  modal.classList.add('show');
}

function closeModal(){document.getElementById('productModal').classList.remove('show');}

// ====== 舞台控制 ======
function rotateAvatar(dir){
  rotation += dir * 15;
  const el = document.querySelector('.avatar-silhouette');
  if(el)el.style.transform=`rotate(${rotation}deg)`;
}
function resetPose(){rotation=0;const el=document.querySelector('.avatar-silhouette');if(el)el.style.transform='';}
let animState=0;const animPoses=['wave','dance','idle','jump'];
function toggleAnimation(){
  animState=(animState+1)%animPoses.length;
  showToast(`动作: ${['挥手','跳舞','待机','跳跃'][animState]}`);
}
function snapshot(){
  showToast('📸 截图已保存到相册！');
}

// ====== Toast提示 ======
function showToast(msg){
  const el = document.createElement('div');
  el.style.cssText = `position:fixed;top:80px;left:50%;transform:translateX(-50%);z-index:9999;
    padding:10px 24px;border-radius:12px;background:rgba(99,102,241,0.95);color:#fff;
    font-size:0.9rem;font-weight:600;box-shadow:0 8px 30px rgba(99,102,241,0.3);
    animation:fadeInUp 0.3s ease;`;
  el.textContent=msg;
  document.body.appendChild(el);
  setTimeout(()=>{el.style.opacity='0';setTimeout(()=>el.remove(),300);},2000);
}

// ====== Tab事件绑定 ======
document.querySelectorAll('.cat-tab').forEach(tab=>{
  tab.addEventListener('click',()=>selectCategory(tab.dataset.cat));
});

// ====== 初始化 ======
renderItems('hair');
renderPresets();
updateStats();

// CSS animation
const style = document.createElement('style');
style.textContent = `
@keyframes fadeInUp{from{opacity:0;transform:translateX(-50%) translateY(-10px);}to{opacity:1;transform:translateX(-50%) translateY(0);}}
`;
document.head.appendChild(style);
</script>
</body>
</html>'''
w(os.path.join(BASE, "pages", "digital-human", "dressup.html"), dressup_html)

# ============================================================
# 6. LLM驱动数字人交互系统 — llm-interactive.html
# ============================================================
llm_html = '''\
<!DOCTYPE html>
<html lang="zh-CN" data-3d="galaxy" data-bg="nebula">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI数字人互动空间 — 龙奕学院 LongYi Academy</title>
<link rel="stylesheet" href="../../assets/style.css">
<link rel="stylesheet" href="../../assets/themes/academy/lavender-academy.css">
<link rel="stylesheet" href="../../assets/themes/dark-mode.css">
<link rel="stylesheet" href="../../assets/effects-layer.css">
<style>
.llm-layout{display:flex;gap:20px;padding:20px;max-width:1500px;margin:0 auto;min-height:calc(100vh - 140px);}

/* 左侧数字人舞台 */
.llm-stage{
  flex:1;min-width:0;display:flex;flex-direction:column;gap:16px;
}
.stage-area{
  position:relative;height:420px;border-radius:20px;overflow:hidden;
  background:radial-gradient(ellipse at 50% 40%,#1a1a3e 0%,#0a0a1e 70%);
  border:1px solid rgba(167,139,250,0.2);
  display:flex;align-items:center;justify-content:center;
}
.avatar-display{text-align:center;color:#c4b5fd;}
.avatar-face{font-size:120px;line-height:1;animation:float 4s ease-in-out infinite;filter:drop-shadow(0 0 30px rgba(167,139,250,0.4));}
@keyframes float{0%,100%{transform:translateY(0);}50%{transform:translateY(-10px);}}
.status-bar{
  display:flex;align-items:center;justify-content:space-between;padding:10px 18px;
  background:rgba(20,20,45,0.8);border-radius:12px;font-size:0.82rem;color:#a0a0c0;
}
.status-item{display:flex;align-items:center;gap:6px;}
.dot-online{width:8px;height:8px;border-radius:50%;background:#22c55e;box-shadow:0 0 8px #22c55e;animation:pulse-dot 2s infinite;}
@keyframes pulse-dot{0%,100%{opacity:1;}50%{opacity:0.5;}}

/* 右侧对话区 */
.llm-chat{
  width:440px;flex-shrink:0;display:flex;flex-direction:column;
  background:rgba(20,20,45,0.85);border-radius:20px;
  border:1px solid rgba(167,139,250,0.15);overflow:hidden;
}
.chat-header{
  padding:16px 20px;border-bottom:1px solid rgba(255,255,255,0.08);
  display:flex;align-items:center;gap:10px;
}
.chat-avatar-small{width:36px;height:36px;border-radius:12px;background:linear-gradient(135deg,#6366f1,#a78bfa);display:flex;align-items:center;justify-content:center;font-size:1.2rem;}
.chat-header-info{flex:1;}
.chat-header-name{font-size:0.95rem;font-weight:700;color:#fff;}
.chat-header-status{font-size:0.75rem;color:#22c55e;}
.chat-messages{
  flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:12px;
  max-height:360px;min-height:280px;
}
.msg{
  max-width:85%;padding:12px 16px;border-radius:16px;font-size:0.88rem;line-height:1.6;
  animation:msgIn 0.3s ease;
}
@keyframes msgIn{from{opacity:0;transform:translateY(10px);}to{opacity:1;transform:none;}}
.msg-bot{
  align-self:flex-start;background:rgba(99,102,241,0.12);border:1px solid rgba(99,102,241,0.15);
  color:#e0e0f0;border-bottom-left-radius:4px;
}
.msg-user{
  align-self:flex-end;background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;
  border-bottom-right-radius:4px;
}
.typing-indicator{
  align-self:flex-start;display:flex;gap:4px;padding:12px 16px;
}
.typing-dot{width:8px;height:8px;border-radius:50%;background:#6366f1;animation:typingBounce 1.4s infinite;}
.typing-dot:nth-child(2){animation-delay:0.2s;}
.typing-dot:nth-child(3){animation-delay:0.4s;}
@keyframes typingBounce{0%,80%,100%{transform:scale(0.6);opacity:0.4;}40%{transform:scale(1);opacity:1;}}
.chat-input-area{
  padding:14px 16px;border-top:1px solid rgba(255,255,255,0.08);
  display:flex;gap:8px;align-items:flex-end;
}
.chat-input{
  flex:1;padding:10px 16px;border-radius:14px;border:1px solid rgba(255,255,255,0.1);
  background:rgba(255,255,255,0.05);color:#e0e0f0;font-size:0.9rem;
  resize:none;max-height:100px;font-family:inherit;outline:none;
}
.chat-input:focus{border-color:#6366f1;box-shadow:0 0 0 3px rgba(99,102,241,0.15);}
.send-btn{
  width:40px;height:40px;border-radius:12px;background:linear-gradient(135deg,#6366f1,#8b5cf6);
  border:none;color:#fff;cursor:pointer;font-size:1.1rem;display:flex;align-items:center;justify-content:center;
  transition:all 0.25s;flex-shrink:0;
}
.send-btn:hover{transform:scale(1.08);box-shadow:0 4px 15px rgba(99,102,241,0.4);}

/* 角色选择卡片区 */
.role-cards{display:flex;gap:10px;overflow-x:auto;padding:8px 0;}
.role-card{
  flex-shrink:0;width:100px;padding:12px 8px;border-radius:14px;text-align:center;
  background:rgba(255,255,255,0.04);border:2px solid transparent;
  cursor:pointer;transition:all 0.25s;
}
.role-card:hover{border-color:rgba(167,139,250,0.3);background:rgba(167,139,250,0.06);}
.role-card.active{border-color:#a78bfa;background:rgba(167,139,250,0.1);}
.role-avatar{font-size:2rem;margin-bottom:4px;}
.role-name{font-size:0.78rem;color:#c4b5fd;font-weight:600;}
.role-type{font-size:0.68rem;color:#888;margin-top:2px;}

/* 能力面板 */
.ability-panel{
  background:rgba(20,20,45,0.85);border-radius:16px;padding:18px;
  border:1px solid rgba(167,139,250,0.15);margin-top:12px;
}
.ability-title{font-size:0.95rem;font-weight:700;color:#e0e0f0;margin-bottom:12px;display:flex;align-items:center;gap:8px;}
.ability-bars{display:flex;flex-direction:column;gap:10px;}
.ability-row{display:flex;align-items:center;gap:10px;}
.ability-label{width:60px;font-size:0.82rem;color:#a0a0c0;}
.ability-bar{flex:1;height:8px;border-radius:4px;background:rgba(255,255,255,0.06);overflow:hidden;}
.ability-fill{height:100%;border-radius:4px;background:linear-gradient(90deg,#6366f1,#a78bfa);transition:width 0.6s ease;}
.ability-value{width:36px;text-align:right;font-size:0.78rem;color:#c4b5fd;font-weight:600;}

/* 快捷回复 */
.quick-replies{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px;}
.quick-reply{
  padding:6px 14px;border-radius:16px;font-size:0.78rem;background:rgba(99,102,241,0.1);
  color:#a5b4fc;border:1px solid rgba(99,102,241,0.15);cursor:pointer;transition:all 0.2s;
}
.quick-reply:hover{background:rgba(99,102,241,0.2);color:#fff;}

/* TTS 控制 */
.tts-panel{
  display:flex;align-items:center;gap:12px;padding:12px 16px;
  background:rgba(20,20,45,0.7);border-radius:12px;margin-top:12px;
}
.tts-btn{
  padding:8px 16px;border-radius:10px;background:rgba(99,102,241,0.15);
  color:#a5b4fc;border:1px solid rgba(99,102,241,0.2);cursor:pointer;font-size:0.82rem;transition:all 0.25s;
}
.tts-btn:hover{background:rgba(99,102,241,0.25);color:#fff;}
.tts-slider{flex:1;-webkit-appearance:slider-vertical;height:4px;background:rgba(255,255,255,0.1);border-radius:2px;outline:none;}
.tts-speed-label{font-size:0.75rem;color:#888;width:40px;}
</style>
</head>
<body>

<!-- 角色选择区 -->
<div style="max-width:1500px;margin:0 auto;padding:16px 20px 0;">
  <div class="role-cards" id="roleCards"></div>
</div>

<div class="llm-layout">
  <!-- 左侧：数字人舞台 -->
  <div class="llm-stage">
    <div class="stage-area" id="stageArea">
      <div class="avatar-display" id="avatarDisplay">
        <div class="avatar-face" id="avatarFace">🧝‍♀️</div>
        <div style="margin-top:10px;font-size:0.9rem;" id="avatarMood">思考中...</div>
      </div>
    </div>
    
    <div class="status-bar">
      <div class="status-item"><span class="dot-online"></span><span>LLM 引擎在线</span></div>
      <div class="status-item">🧠 模型: <strong style="color:#a5b4fc;">LongYi-Chat v2.0</strong></div>
      <div class="status-item">⚡ 响应: < 800ms</div>
      <div class="status-item">🔄 上下文: <span id="contextCount">0</span> 轮</div>
    </div>

    <!-- 能力面板 -->
    <div class="ability-panel" id="abilityPanel">
      <div class="ability-title">📊 当前角色能力图谱</div>
      <div class="ability-bars" id="abilityBars"></div>
    </div>

    <!-- 快捷回复 -->
    <div class="quick-replies" id="quickReplies"></div>

    <!-- TTS 控制 -->
    <div class="tts-panel">
      <button class="tts-btn" id="ttsToggle" onclick="toggleTTS()">🔊 开启语音</button>
      <span style="font-size:0.82rem;color:#888;">语速:</span>
      <input type="range" class="tts-slider" min="0.5" max="2" step="0.1" value="1" id="ttsSpeed" oninput="updateTtsSpeed(this.value)">
      <span class="tts-speed-label" id="ttsSpeedLabel">1.0x</span>
      <button class="tts-btn" onclick="changeVoice()">🎭 切换声音</button>
    </div>
  </div>

  <!-- 右侧：对话区 -->
  <div class="llm-chat">
    <div class="chat-header">
      <div class="chat-avatar-small" id="chatAvatar">🧝‍♀️</div>
      <div class="chat-header-info">
        <div class="chat-header-name" id="chatName">艾莉亚 · 星语者</div>
        <div class="chat-header-status">● AI驱动 · 实时响应</div>
      </div>
    </div>
    <div class="chat-messages" id="chatMessages"></div>
    <div class="chat-input-area">
      <textarea class="chat-input" id="chatInput" placeholder="输入消息... (Enter发送，Shift+Enter换行)" rows="1" onkeydown="handleKey(event)"></textarea>
      <button class="send-btn" onclick="sendMessage()">➤</button>
    </div>
  </div>
</div>

<script src="../../assets/three-engine.js"></script>
<script src="../../assets/nav.js"></script>
<script src="../../assets/theme-toggle.js"></script>
<script src="../../assets/effects-runtime.js"></script>
<script src="../../assets/dynamic-bg.js"></script>
<script>
// ====== AI 角色数据库 ======
const ROLES = [
  {
    id:'elia',name:'艾莉亚·星语者',type:'奇幻向导',avatar:'🧝‍♀️',
    desc:'来自星渊世界的精灵族学者，精通上古语言和星象魔法。性格温和但偶尔会一本正经地胡说八道。',
    personality:'温柔、知性、略带神秘感、偶尔调皮',
    abilities:{知识:95,共情:88,创意:82,逻辑:78,幽默:65},
    greetings:['你好呀，旅行者~ 我是艾莉亚，有什么想聊的吗？','✨ 欢迎来到星渊！今天想探索什么话题？','哦~ 你来了呀！我正在研究新的星座配置呢~'],
    quickReplies:['介绍一下你自己','讲一个奇幻故事','推荐一些番剧','今天运势如何','帮我做决定'],
    responses:{
      default:[
        '嗯...这个问题很有趣呢~让我想想...',
        '从星渊的角度来看，我觉得可以这样理解...',
        '啊！这个让我想起了在星渊图书馆看到的一段记载~',
        '旅行者，你的问题触及了很深的领域呢...不过我喜欢！',
        '哈哈，你这么问的话...我有种预感我们会成为好朋友的！',
      ]
    }
  },
  {
    id:'kuro',name:'黑曜·影刃',type:'赛博忍者',avatar:'🥷',
    desc:'2077年新东京的独立情报贩子，擅长网络渗透和信息分析。外表冷酷但意外地会关心人。',
    personality:'冷静、毒舌、内心温柔、技术宅',
    abilities:{知识:82,共情:60,创意:70,logic:95,humor:72},
    greetings:['...你找我？说吧，计时开始。','又是新人？行吧，我给你三分钟。','哼。既然来了就别浪费时间。'],
    quickReplies:['帮我分析一下网络安全','推荐赛博朋克作品','你为什么这么酷','教我编程技巧','最近有什么情报'],
    responses:{
      default:[
        '...这种事情还要我说？自己查去。...好吧，其实是这样——',
        '啧。你的思路有问题。正确做法应该是这样...',
        '呵。有意思。我从没从这个角度想过。',
        '（推眼镜）听好了，我只说一次。', 
        '...算了，看在你还算认真的份上，告诉你也无妨。',
      ]
    }
  },
  {
    id:'miku',name:'初未来·歌姬',type:'虚拟偶像',avatar:'🎤',
    desc:'龙奕学院原创虚拟歌手，拥有跨越八度的音域和治愈系的歌声。梦想是在龙墟世界最大的舞台上演唱。',
    personality:'元气、纯真、热爱音乐、有点天然呆',
    abilities:{knowledge:70,empathy:92,creativity:98,logic:55,humor:80},
    greetings:['嗨嗨~！我是初未来！一起来唱歌吧~♪','大家好呀！今天也要元气满满哦！💖','啦啦啦~♪ 你来啦！等你好久了！'],
    quickReplies:['唱一首歌吧','你的梦想是什么','安慰一下我','聊聊音乐','推荐一首歌'],
    responses:{
      default:[
        '诶？！这个...嗯...让我用歌声回答你吧~♪',
        '哇！你说的这个好有趣！我也想知道！',
        '嘿嘿~我的直觉告诉我答案是这个！',
        '♪~ 让我想想...啊！想到了！',
        '呜...这个有点难倒我了...但是我会努力的！',
      ]
    }
  },
  {
    id:'sensei',name:'老师·万事屋',type:'全能导师',avatar:'👨‍🏫',
    desc:'龙奕研修学院的资深导师，从Cos制作技巧到人生哲理无所不知。说话喜欢引用名言但经常记错。',
    personality:'博学、啰嗦、热心、偶尔健忘',
    abilities:{knowledge:98,empathy:85,creativity:75,logic:90,humor:68},
    greetings:['啊，来了来了！今天想学什么？','年轻人，求知若渴是好事！来来来，坐下说。','正如古人云——呃，那句怎么说来着...反正欢迎！'],
    quickReplies:['Cos制作入门','如何提升创作','学习建议','职业规划','讲个冷笑话'],
    responses:{
      default:[
        '好问题！这让我想起当年我在...等等，跑题了。答案是——',
        '咳咳，作为导师，我要认真回答你这个问题。',
        '嗯...根据我的经验来看，大概有这么几种可能...',
        '哈哈！这个问题好啊！说明你在思考，我很欣慰！',
        '让老师我想想...啊，对了！关键在于...',
      ]
    }
  },
  {
    id:'neco',name:'猫又·捣蛋鬼',type:'吉祥物',avatar:'🐱',
    desc:'龙奕学院的神秘生物，外形像猫但又不太像。喜欢恶作剧但从不真正伤害任何人。据说知道很多秘密。',
    personality:'调皮、神秘、贪吃、傲娇',
    abilities:{knowledge:60,empathy:75,creativity:90,logic:50,humor:95},
    greetings:['喵？你谁啊...算了不管了，给吃的就行。','喵~！又来一个两脚兽！喵哈哈！','（盯）...你身上有零食的味道。'],
    quickReplies:['你知道什么秘密','给我变个魔术','你最喜欢什么','讲个笑话','跟我玩'],
    responses:{
      default:[
        '喵哈哈哈！这个简单！本喵什么不知道~',
        '唔...告诉你可以，但你得先请我喝奶茶！',
        '喵？（歪头）你认真的？好吧好吧~',
        '嘿嘿嘿...秘密嘛~ 🤫',
        '喵呜...这个嘛...（转圈圈）...啊想起来了！',
      ]
    }
  }
];

// ====== 状态 ======
let currentRole = ROLES[0];
let chatHistory = [];
let contextCount = 0;
let ttsEnabled = false;
let ttsSpeed = 1;
let voiceIndex = 0;
const VOICES = ['温柔女声','清澈男声','元气少女','低沉大叔','机械合成'];

// ====== 初始化 ======
function init(){
  renderRoleCards();
  selectRole(ROLES[0].id);
  // 入场消息延迟发送
  setTimeout(()=>{
    const greet = currentRole.greetings[Math.floor(Math.random()*currentRole.greetings.length)];
    addBotMessage(greet);
  }, 800);
}

// ====== 渲染角色卡片 ======
function renderRoleCards(){
  document.getElementById('roleCards').innerHTML = ROLES.map(r => `
    <div class="role-card ${r.id===currentRole.id?'active':''}" onclick="selectRole('${r.id}')">
      <div class="role-avatar">${r.avatar}</div>
      <div class="role-name">${r.name.split('·')[0]}</div>
      <div class="role-type">${r.type}</div>
    </div>
  `).join('');
}

// ====== 选择角色 ======
function selectRole(id){
  currentRole = ROLES.find(r=>r.id===id)||ROLES[0];
  renderRoleCards();
  // Update UI
  document.getElementById('avatarFace').textContent=currentRole.avatar;
  document.getElementById('chatAvatar').textContent=currentRole.avatar;
  document.getElementById('chatName').textContent=currentRole.name;
  document.getElementById('avatarMood').textContent=currentRole.personality.split('、')[0]+'中...';
  // Abilities
  const abNames={knowledge:'知识',empathy:'共情',creativity:'创意',logic:'逻辑',humor:'幽默'};
  let abHtml='';
  for(const [key,label] of Object.entries(abNames)){
    const val=currentRole.abilities[key]||50;
    abHtml+=`<div class="ability-row">
      <span class="ability-label">${label}</span>
      <div class="ability-bar"><div class="ability-fill" style="width:${val}%"></div></div>
      <span class="ability-value">${val}</span>
    </div>`;
  }
  document.getElementById('abilityBars').innerHTML=abHtml;
  // Quick replies
  document.getElementById('quickReplies').innerHTML=(currentRole.quickReplies||[]).map(q=>
    `<span class="quick-reply" onclick="sendQuick('${q}')">${q}</span>`
  ).join('');
  // Reset chat
  document.getElementById('chatMessages').innerHTML='';
  chatHistory=[];
  contextCount=0;
  document.getElementById('contextCount').textContent='0';
  // Greeting
  setTimeout(()=>{
    const g=currentRole.greetings[Math.floor(Math.random()*currentRole.greetings.length)];
    addBotMessage(g);
  },400);
}

// ====== 消息系统 ======
function addBotMessage(text){
  const msgs=document.getElementById('chatMessages');
  const div=document.createElement('div');
  div.className='msg msg-bot';
  div.textContent=text;
  msgs.appendChild(div);
  msgs.scrollTop=msgs.scrollHeight;
  chatHistory.push({role:'bot',content:text});contextCount++;
  document.getElementById('contextCount').textContent=contextCount;
  // TTS
  if(ttsEnabled)speakText(text);
}
function addUserMessage(text){
  const msgs=document.getElementById('chatMessages');
  const div=document.createElement('div');
  div.className='msg msg-user';
  div.textContent=text;
  msgs.appendChild(div);
  msgs.scrollTop=msgs.scrollHeight;
  chatHistory.push({role:'user',content:text});
}
function showTyping(){
  const msgs=document.getElementById('chatMessages');
  const div=document.createElement('div');
  div.className='typing-indicator';div.id='typingIndicator';
  div.innerHTML='<div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div>';
  msgs.appendChild(div);msgs.scrollTop=msgs.scrollHeight;
}
function hideTyping(){
  const el=document.getElementById('typingIndicator');
  if(el)el.remove();
}

// ====== 发送消息 ======
function sendMessage(){
  const input=document.getElementById('chatInput');
  const text=input.value.trim();
  if(!text)return;
  input.value='';
  addUserMessage(text);
  // Simulate LLM response
  showTyping();
  updateAvatarMood('thinking');
  const delay=600+Math.random()*1200;
  setTimeout(()=>{
    hideTyping();
    const reply=generateReply(text);
    addBotMessage(reply);
    updateAvatarMood('happy');
  },delay);
}
function sendQuick(text){
  document.getElementById('chatInput').value=text;
  sendMessage();
}
function handleKey(e){
  if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();sendMessage();}
}

// ====== LLM 回复模拟（实际接入时替换为真实API调用）=====
function generateReply(userMsg){
  const responses=currentRole.responses.default;
  // 简单关键词匹配
  const lower=userMsg.toLowerCase();
  if(lower.includes('你好')||lower.includes('hi')||lower.includes('嗨'))
    return currentRole.greetings[Math.floor(Math.random()*currentRole.greetings.length)];
  if(lower.includes('名字')||lower.includes('是谁')||lower.includes('介绍'))
    return `我是${currentRole.name}，一个${currentRole.type}。${currentRole.desc.substring(0,30)}...想了解更多就来问我吧~`;
  if(lower.includes('喜欢')||lower.includes('爱好'))
    return `${currentRole.personality.split('、')[Math.floor(Math.random()*currentRole.personality.split('、').length)]}是我的特点之一！至于具体的嘛...你猜猜？`;
  if(lower.includes('帮助')||lower.includes('帮忙'))
    return '当然可以！说说你需要什么帮助，我尽力而为~ 💪';
  if(lower.includes('谢谢'))
    return '不客气！能帮到你我也很开心~ 😊';
  if(lower.includes('再见')||lower.includes('拜拜'))
    return '好的，下次再来找我玩哦！我会想你的~ ✨';
  // Default contextual response
  const base=responses[Math.floor(Math.random()*responses.length)];
  // Add some context awareness
  const extras=[
    `顺便说一下，关于"${userMsg.substring(0,10)}${userMsg.length>10?'...':''}"——`,
    `说到这个，`,
    ``,
    `嗯...结合你刚才说的，`,
  ];
  const extra=extras[Math.floor(Math.random()*extras.length)];
  return extra+base;
}

// ====== Avatar Mood ======
function updateAvatarMood(mood){
  const el=document.getElementById('avatarMood');
  const moods={thinking:'🤔 思考中...',happy:'😊 开心',sad:'😢',surprised:'😮',angry:'😤',sleepy:'😴'};
  el.textContent=moods[mood]||mood;
}

// ====== TTS 系统 ======
function toggleTTS(){
  ttsEnabled=!ttsEnabled;
  document.getElementById('ttsToggle').textContent=ttsEnabled?'🔊 关闭语音':'🔊 开启语音';
  document.getElementById('ttsToggle').style.background=ttsEnabled?'rgba(34,197,94,0.2)':'';
  if(ttsEnabled&&!window.speechSynthesis)speakText('语音合成系统已启动！');
}
function speakText(text){
  if(!('speechSynthesis'in window))return;
  const utt=new SpeechSynthesisUtterance(text.slice(0,200));
  utt.lang='zh-CN';
  utt.rate=ttsSpeed;
  utt.pitch=voiceIndex===2?1.3:voiceIndex===4?0.8:1;
  window.speechSynthesis.speak(utt);
}
function updateTtsSpeed(v){
  ttsSpeed=parseFloat(v);
  document.getElementById('ttsSpeedLabel').textContent=v+'x';
}
function changeVoice(){
  voiceIndex=(voiceIndex+1)%VOICES.length;
  alert(`当前声音: ${VOICES[voiceIndex]}`);
}

// Init
init();
</script>
</body>
</html>'''
w(os.path.join(BASE, "pages", "digital-human", "llm-interactive.html"), llm_html)

# ============================================================
# 7. 登录页面重做 — auth/login-v2.html
# ============================================================
login_html = '''\
<!DOCTYPE html>
<html lang="zh-CN" data-3d="default" data-bg="aurora">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>登录 — 龙奕学院 LongYi Academy</title>
<link rel="stylesheet" href="../../assets/style.css">
<link rel="stylesheet" href="../../assets/themes/academy/sky-academy.css">
<link rel="stylesheet" href="../../assets/themes/dark-mode.css">
<link rel="stylesheet" href="../../assets/effects-layer.css">
<style>
.login-page{
  min-height:100vh;display:flex;align-items:center;justify-content:center;
  padding:40px 20px;position:relative;
}
.login-container{
  display:flex;width:900px;max-width:94vw;border-radius:24px;overflow:hidden;
  background:rgba(255,255,255,0.95);backdrop-filter:blur(20px);
  box-shadow:0 24px 80px rgba(0,0,0,0.12),0 0 0 1px rgba(0,0,0,0.04);
}
.login-banner{
  width:380px;flex-shrink:0;
  background:linear-gradient(160deg,#6366f1 0%,#8b5cf6 40%,#a78bfa 70%,#c4b5fd 100%);
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  padding:40px 30px;color:#fff;position:relative;overflow:hidden;
}
.banner-bg-deco{
  position:absolute;top:-40px;right:-40px;width:200px;height:200px;
  border-radius:50%;background:rgba(255,255,255,0.1);
}
.banner-bg-deco2{
  position:absolute;bottom:-60px;left:-30px;width:160px;height:160px;
  border-radius:50%;background:rgba(255,255,255,0.07);
}
.brand-large{font-size:2.4rem;font-weight:900;margin-bottom:6px;position:relative;z-index:1;}
.brand-sub-large{font-size:0.9rem;opacity:0.85;margin-bottom:24px;position:relative;z-index:1;}
.banner-features{display:flex;flex-direction:column;gap:14px;width:100%;position:relative;z-index:1;}
.bfeat{
  display:flex;align-items:center;gap:10px;font-size:0.88rem;opacity:0.93;
}
.bfeat-icon{width:32px;height:32px;border-radius:10px;background:rgba(255,255,255,0.2);display:flex;align-items:center;justify-content:center;font-size:1rem;}

.login-form-area{
  flex:1;padding:44px 36px;display:flex;flex-direction:column;justify-content:center;
}
.form-title{font-size:1.8rem;font-weight:900;color:#1a1a2e;margin-bottom:4px;}
.form-subtitle{font-size:0.9rem;color:#888;margin-bottom:28px;}

/* Tab 切换 */
.login-tabs{display:flex;margin-bottom:28px;background:rgba(0,0,0,0.04);border-radius:12px;padding:3px;}
.login-tab{
  flex:1;padding:10px;text-align:center;border-radius:10px;font-size:0.9rem;font-weight:600;
  cursor:pointer;transition:all 0.25s;color:#888;border:none;background:transparent;
}
.login-tab.active{background:#fff;color:#6366f1;box-shadow:0 2px 8px rgba(0,0,0,0.06);}

/* 表单 */
.form-group{margin-bottom:18px;}
.form-label{display:block;font-size:0.84rem;font-weight:600;color:#555;margin-bottom:6px;}
.input-wrapper{position:relative;display:flex;align-items:center;}
.input-icon{
  position:absolute;left:14px;font-size:1.1rem;z-index:1;opacity:0.5;
}
.form-input{
  width:100%;padding:13px 14px 13px 42px;border:1.5px solid #e5e7eb;border-radius:12px;
  font-size:0.95rem;outline:none;transition:all 0.25s;background:#fafafa;color:#222;
}
.form-input:focus{border-color:#6366f1;box-shadow:0 0 0 4px rgba(99,102,241,0.1);background:#fff;}
.code-row{display:flex;gap:10px;}
.code-row .form-input{flex:1;padding-left:14px;}
.code-btn{
  padding:13px 20px;border-radius:12px;background:linear-gradient(135deg,#6366f1,#8b5cf6);
  color:#fff;font-weight:700;font-size:0.88rem;border:none;white-space:nowrap;cursor:pointer;transition:all 0.25s;
}
.code-btn:hover{transform:translateY(-1px);box-shadow:0 4px 15px rgba(99,102,241,0.3);}
.code-btn:disabled{opacity:0.5;cursor:not-allowed;transform:none;}

/* 登录按钮 */
.login-btn{
  width:100%;padding:14px;border-radius:14px;font-size:1.05rem;font-weight:800;
  background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;border:none;
  cursor:pointer;transition:all 0.3s;margin-top:6px;
}
.login-btn:hover{transform:translateY(-2px);box-shadow:0 8px 25px rgba(99,102,241,0.35);}

/* 分割线 */
.divider{display:flex;align-items:center;gap:14px;margin:22px 0;color:#bbb;font-size:0.84rem;}
.divider::before,.divider::after{content:'';flex:1;height:1px;background:#e5e7eb;}

/* 第三方登录 */
.social-login{display:flex;gap:12px;justify-content:center;}
.social-btn{
  width:52px;height:52px;border-radius:14px;border:1.5px solid #e5e7eb;
  background:#fff;display:flex;align-items:center;justify-content:center;
  font-size:1.5rem;cursor:pointer;transition:all 0.25s;
}
.social-btn:hover{border-color:#6366f1;transform:translateY(-2px);box-shadow:0 4px 12px rgba(0,0,0,0.08);}

.form-footer{margin-top:20px;text-align:center;font-size:0.85rem;color:#888;}
.form-footer a{color:#6366f1;text-decoration:none;font-weight:600;}
.form-footer a:hover{text-decoration:underline;}

/* 安全标识 */
.security-badge{
  display:flex;align-items:center;justify-content:center;gap:6px;
  margin-top:16px;font-size:0.76rem;color:#aaa;
}
.security-badge svg{width:14px;height:14px;}
</style>
</head>
<body>

<div class="login-page">
  <div class="login-container">
    <!-- 左侧品牌区 -->
    <div class="login-banner">
      <div class="banner-bg-deco"></div>
      <div class="banner-bg-deco2"></div>
      <div class="brand-large">🏫 龙奕学院</div>
      <div class="brand-sub-large">LongYi Academy</div>
      <div class="banner-features">
        <div class="bfeat"><div class="bfeat-icon">🎬</div><span>番剧 / 社交 / 商城 一站式体验</span></div>
        <div class="bfeat"><div class="bfeat-icon">🌌</div><span>元宇宙世界 · 数字人 · 虚拟直播</span></div>
        <div class="bfeat"><div class="bfeat-icon">🛡️</div><span>端到端加密 · 安全传输协议</span></div>
        <div class="bfeat"><div class="bfeat-icon">✨</div><span>AI驱动的个性化推荐系统</span></div>
      </div>
    </div>

    <!-- 右侧表单区 -->
    <div class="login-form-area">
      <div class="form-title">欢迎回来</div>
      <div class="form-subtitle">登录你的龙奕学院账号</div>

      <!-- 登录方式Tab -->
      <div class="login-tabs">
        <div class="login-tab active" onclick="switchTab('phone',this)">📱 手机号登录</div>
        <div class="login-tab" onclick="switchTab('pwd',this)">🔐 密码登录</div>
      </div>

      <!-- 手机号登录表单 -->
      <form id="phoneForm" onsubmit="handlePhoneLogin(event)">
        <div class="form-group">
          <label class="form-label">手机号码</label>
          <div class="input-wrapper">
            <span class="input-icon">📱</span>
            <input class="form-input" type="tel" id="phoneInput" placeholder="请输入11位手机号" maxlength="11" pattern="[0-9]{11}" required>
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">验证码</label>
          <div class="code-row">
            <input class="form-input" type="text" id="codeInput" placeholder="请输入6位验证码" maxlength="6" pattern="[0-9]{6}" required>
            <button type="button" class="code-btn" id="sendCodeBtn" onclick="sendCode()">获取验证码</button>
          </div>
        </div>
        <button type="submit" class="login-btn">登 录</button>
      </form>

      <!-- 密码登录表单（默认隐藏） -->
      <form id="pwdForm" onsubmit="handlePwdLogin(event)" style="display:none;">
        <div class="form-group">
          <label class="form-label">手机号 / 邮箱</label>
          <div class="input-wrapper">
            <span class="input-icon">👤</span>
            <input class="form-input" type="text" id="accountInput" placeholder="手机号或邮箱" required>
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">密码</label>
          <div class="input-wrapper">
            <span class="input-icon">🔒</span>
            <input class="form-input" type="password" id="pwdInput" placeholder="请输入密码" required>
          </div>
        </div>
        <button type="submit" class="login-btn">登 录</button>
      </form>

      <div class="divider">其他登录方式</div>

      <!-- 第三方登录 -->
      <div class="social-login">
        <button class="social-btn" title="微信登录" onclick="wechatLogin()">💬</button>
        <button class="social-btn" title="QQ登录" onclick="qqLogin()">🐧</button>
        <button class="social-btn" title="微博登录" onclick="weiboLogin()">📝</button>
        <button class="social-btn" title="Apple登录" onclick="appleLogin()">🍎</button>
      </div>

      <div class="form-footer">
        还没有账号？<a href="register-v2.html">立即注册</a> · <a href="#">忘记密码？</a>
      </div>

      <div class="security-badge">
        🔒 TLS 1.3 加密传输 · 数据安全存储
      </div>
    </div>
  </div>
</div>

<script src="../../assets/theme-toggle.js"></script>
<script src="../../assets/dynamic-bg.js"></script>
<script>
// ====== Tab 切换 ======
function switchTab(tab,el){
  document.querySelectorAll('.login-tab').forEach(t=>t.classList.remove('active'));
  el.classList.add('active');
  document.getElementById('phoneForm').style.display=tab==='phone'?'block':'none';
  document.getElementById('pwdForm').style.display=tab==='pwd'?'block':'none';
}

// ====== 手机号格式校验 ======
const phoneInput=document.getElementById('phoneInput');
phoneInput.addEventListener('input',function(){
  this.value=this.value.replace(/\\D/g,'');
});

// ====== 发送验证码 ======
let codeTimer=null;
let countdown=0;
function sendCode(){
  const phone=phoneInput.value.trim();
  if(!/^1[3-9]\\d{9}$/.test(phone)){alert('请输入正确的11位手机号');return;}
  const btn=document.getElementById('sendCodeBtn');
  btn.disabled=true;countdown=60;
  btn.textContent=countdown+'s 后重发';
  codeTimer=setInterval(()=>{
    countdown--;
    if(countdown<=0){clearInterval(codeTimer);btn.disabled=false;btn.textContent='获取验证码';return;}
    btn.textContent=countdown+'s 后重发';
  },1000);
  // 模拟发送
  alert(`验证码已发送到 ${phone.substring(0,3)}****${phone.substring(7)}\\n（演示模式：验证码为 123456）`);
}

// ====== 手机号登录 ======
function handlePhoneLogin(e){
  e.preventDefault();
  const phone=phoneInput.value.trim();
  const code=document.getElementById('codeInput').value.trim();
  if(!/^1[3-9]\\d{9}$/.test(phone)){alert('手机号格式错误');return;}
  if(code.length!==6){alert('请输入6位验证码');return;}
  if(code!=='123456'){alert('验证码错误（演示模式请输入123456）');return;}
  // 成功
  localStorage.setItem('longyi_user',JSON.stringify({phone,name:`用户${phone.slice(-4)}`,loginTime:Date.now()}));
  alert('✅ 登录成功！即将跳转...');
  setTimeout(()=>window.location.href='../../index.html',1000);
}

// ====== 密码登录 ======
function handlePwdLogin(e){
  e.preventDefault();
  const account=document.getElementById('accountInput').value.trim();
  const pwd=document.getElementById('pwdInput').value;
  if(account.length<3){alert('请输入账号');return;}
  if(pwd.length<6){alert('密码至少6位');return;}
  localStorage.setItem('longyi_user',JSON.stringify({account,name:account,loginTime:Date.now()}));
  alert('✅ 登录成功！即将跳转...');
  setTimeout(()=>window.location.href='../../index.html',1000);
}

// ====== 第三方登录 =======
function wechatLogin(){alert('📱 微信扫码登录窗口打开中...\\n（演示模式）');}
function qqLogin(){alert('🐧 QQ授权登录跳转中...\\n（演示模式）');}
function weiboLogin(){alert('📝 微博授权登录跳转中...\\n（演示模式）');}
function appleLogin(){alert('🍎 Apple ID 登录验证中...\\n（演示模式）');}
</script>
</body>
</html>'''
w(os.path.join(BASE, "pages", "auth", "login-v2.html"), login_html)

# ============================================================
# 8. 注册页面重做 — auth/register-v2.html
# ============================================================
reg_html = '''\
<!DOCTYPE html>
<html lang="zh-CN" data-3d="default" data-bg="aurora">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>注册 — 龙奕学院 LongYi Academy</title>
<link rel="stylesheet" href="../../assets/style.css">
<link rel="stylesheet" href="../../assets/themes/academy/sakura-academy.css">
<link rel="stylesheet" href="../../assets/themes/dark-mode.css">
<link rel="stylesheet" href="../../assets/effects-layer.css">
<style>
.reg-page{
  min-height:100vh;display:flex;align-items:center;justify-content:center;
  padding:40px 20px;
}
.reg-container{
  width:520px;max-width:94vw;border-radius:24px;overflow:hidden;
  background:rgba(255,255,255,0.95);backdrop-filter:blur(20px);
  box-shadow:0 24px 80px rgba(0,0,0,0.12);padding:40px 36px;
}
.reg-header{text-align:center;margin-bottom:28px;}
.reg-logo{font-size:3rem;margin-bottom:8px;}
.reg-title{font-size:1.6rem;font-weight:900;color:#1a1a2e;}
.reg-subtitle{font-size:0.88rem;color:#888;margin-top:4px;}

.step-indicator{display:flex;justify-content:center;gap:6px;margin-bottom:28px;}
.step-dot{width:10px;height:10px;border-radius:50%;background:#ddd;transition:all 0.3s;}
.step-dot.active{background:#6366f1;width:28px;border-radius:5px;}
.step-dot.done{background:#22c55e;}

.form-group{margin-bottom:16px;}
.form-label{display:block;font-size:0.84rem;font-weight:600;color:#555;margin-bottom:6px;}
.form-input{
  width:100%;padding:12px 14px;border:1.5px solid #e5e7eb;border-radius:12px;
  font-size:0.95rem;outline:none;transition:all 0.25s;background:#fafafa;
}
.form-input:focus{border-color:#6366f1;box-shadow:0 0 0 4px rgba(99,102,241,0.1);}
.code-row{display:flex;gap:8px;}
.code-row .form-input{flex:1;}
.code-btn{
  padding:12px 16px;border-radius:12px;background:linear-gradient(135deg,#6366f1,#8b5cf6);
  color:#fff;font-weight:700;font-size:0.85rem;border:none;white-space:nowrap;cursor:pointer;
}
.code-btn:disabled{opacity:0.5;cursor:not-allowed;}

/* 密码强度 */
.pwd-strength{display:flex;gap:4px;margin-top:6px;}
.strength-bar{flex:1;height:4px;border-radius:2px;background:#eee;transition:background 0.3s;}
.strength-bar.weak{background:#ef4444;}.strength-bar.medium{background:#f59e0b;}.strength-bar.strong{background:#22c55e;}
.strength-text{font-size:0.74rem;margin-top:4px;color:#888;}

/* 协议 */
.agreement{
  display:flex;align-items:flex-start;gap:8px;font-size:0.82rem;color:#888;margin:18px 0;
}
.agreement input{margin-top:3px;accent-color:#6366f1;}
.agreement a{color:#6366f1;text-decoration:none;}

.reg-btn{
  width:100%;padding:14px;border-radius:14px;font-size:1.05rem;font-weight:800;
  background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;border:none;
  cursor:pointer;transition:all 0.3s;
}
.reg-btn:hover{transform:translateY(-2px);box-shadow:0 8px 25px rgba(99,102,241,0.35);}

.divider{display:flex;align-items:center;gap:12px;margin:20px 0;color:#bbb;font-size:0.84rem;}
.divider::before,.divider::after{content:'';flex:1;height:1px;background:#e5e7eb;}
.social-login{display:flex;gap:12px;justify-content:center;}
.social-btn{
  width:48px;height:48px;border-radius:12px;border:1.5px solid #e5e7eb;
  background:#fff;display:flex;align-items:center;justify-content:center;
  font-size:1.4rem;cursor:pointer;transition:all 0.25s;
}
.social-btn:hover{border-color:#6366f1;transform:translateY(-2px);}
.reg-footer{text-align:center;font-size:0.85rem;color:#888;margin-top:18px;}
.reg-footer a{color:#6366f1;font-weight:600;text-decoration:none;}
</style>
</head>
<body>

<div class="reg-page">
  <div class="reg-container">
    <div class="reg-header">
      <div class="reg-logo">🏫</div>
      <div class="reg-title">加入龙奕学院</div>
      <div class="reg-subtitle">创建账号，开启你的元宇宙之旅</div>
    </div>

    <div class="step-indicator">
      <div class="step-dot active" id="step1Dot"></div>
      <div class="step-dot" id="step2Dot"></div>
      <div class="step-dot" id="step3Dot"></div>
    </div>

    <form id="regForm" onsubmit="handleRegister(event)">
      <div class="form-group">
        <label class="form-label">昵称</label>
        <input class="form-input" type="text" id="nickInput" placeholder="给自己取个响亮的昵称" minlength="2" maxlength="16" required>
      </div>

      <div class="form-group">
        <label class="form-label">手机号码</label>
        <input class="form-input" type="tel" id="regPhone" placeholder="用于登录和找回密码（每个手机号只能注册1个账号）" maxlength="11" pattern="[0-9]{11}" required>
      </div>

      <div class="form-group">
        <label class="form-label">短信验证码</label>
        <div class="code-row">
          <input class="form-input" type="text" id="regCode" placeholder="6位验证码" maxlength="6" required>
          <button type="button" class="code-btn" id="regSendBtn" onclick="sendRegCode()">获取验证码</button>
        </div>
      </div>

      <div class="form-group">
        <label class="form-label">设置密码</label>
        <input class="form-input" type="password" id="regPwd" placeholder="至少8位，包含字母和数字" minlength="8" oninput="checkStrength(this.value)" required>
        <div class="pwd-strength" id="pwdStrength">
          <div class="strength-bar"></div><div class="strength-bar"></div><div class="strength-bar"></div><div class="strength-bar"></div>
        </div>
        <div class="strength-text" id="strengthText">请设置密码</div>
      </div>

      <div class="form-group">
        <label class="form-label">确认密码</label>
        <input class="form-input" type="password" id="regPwd2" placeholder="再次输入密码" required>
      </div>

      <label class="agreement">
        <input type="checkbox" id="agreeCheck" required>
        <span>我已阅读并同意 <a href="#">《用户协议》</a> 和 <a href="#">《隐私政策》</a></span>
      </label>

      <button type="submit" class="reg-btn">注 册</button>
    </form>

    <div class="divider">快捷注册</div>
    <div class="social-login">
      <button class="social-btn" onclick="alert('微信一键注册')">💬</button>
      <button class="social-btn" onclick="alert('QQ一键注册')">🐧</button>
      <button class="social-btn" onclick="alert('微博一键注册')">📝</button>
    </div>

    <div class="reg-footer">
      已有账号？<a href="login-v2.html">立即登录</a>
    </div>
  </div>
</div>

<script src="../../assets/theme-toggle.js"></script>
<script src="../../assets/dynamic-bg.js"></script>
<script>
// 密码强度检测
function checkStrength(pwd){
  const bars=document.querySelectorAll('#pwdStrength .strength-bar');
  const text=document.getElementById('strengthText');
  let score=0;
  if(pwd.length>=8)score++;
  if(/[a-z]/.test(pwd)&&/[A-Z]/.test(pwd))score++;
  if(/\\d/.test(pwd))score++;
  if(/[^a-zA-Z0-9]/.test(pwd))score++;
  bars.forEach((b,i)=>{
    b.className='strength-bar'+(i<score?' '+(['weak','medium','strong','strong'][Math.min(score-1,3)]):'');
  });
  const labels=['太弱了','一般偏弱','还不错','非常强','完美'];
  text.textContent=labels[score];text.style.color=['#ef4444','#f59e0b','#22c55e','#22c55e','#22c55e'][score];
}

// 注册验证码
let regTimer=null,regCountdown=0;
function sendRegCode(){
  const phone=document.getElementById('regPhone').value.trim();
  if(!/^1[3-9]\\d{9}$/.test(phone)){alert('请输入正确的手机号');return;}
  const btn=document.getElementById('regSendBtn');
  btn.disabled=true;regCountdown=60;
  btn.textContent=regCountdown+'s';
  regTimer=setInterval(()=>{
    regCountdown--;
    if(regCountdown<=0){clearInterval(regTimer);btn.disabled=false;btn.textContent='获取验证码';return;}
    btn.textContent=regCountdown+'s';
  },1000);
  alert(`验证码已发送至 ${phone.substring(0,3)}****${phone.substring(7)}\\n（演示验证码:123456）`);
}

// 提交注册
function handleRegister(e){
  e.preventDefault();
  const nick=document.getElementById('nickInput').value.trim();
  const phone=document.getElementById('regPhone').value.trim();
  const code=document.getElementById('regCode').value.trim();
  const pwd=document.getElementById('regPwd').value;
  const pwd2=document.getElementById('regPwd2').value;
  if(nick.length<2){alert('昵称至少2个字符');return;}
  if(!/^1[3-9]\\d{9}$/.test(phone)){alert('手机号格式错误');return;}
  if(code!=='123456'){alert('验证码错误（演示:123456）');return;}
  if(pwd!==pwd2){alert('两次密码不一致');return;}
  if(pwd.length<8){alert('密码至少8位');return;}
  if(!document.getElementById('agreeCheck').checked){alert('请同意用户协议');return;}
  // Success
  localStorage.setItem('longyi_user',JSON.stringify({phone,nick,name:nick,loginTime:Date.now(),isNew:true}));
  alert('✅ 注册成功！欢迎加入龙奕学院！\\n即将跳转首页...');
  setTimeout(()=>window.location.href='../../index.html',1200);
}

// 手机号限制
document.getElementById('regPhone').addEventListener('input',function(){this.value=this.value.replace(/\\D/g,'');});
</script>
</body>
</html>'''
w(os.path.join(BASE, "pages", "auth", "register-v2.html"), reg_html)

print("\\n===== 全部文件生成完成 =====")

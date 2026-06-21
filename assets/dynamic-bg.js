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

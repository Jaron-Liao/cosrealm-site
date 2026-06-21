// ========== 龙奕学院 Academy Enrichment Part 2: shop, metaverse, creator, digital-human, academy ==========
const fs = require('fs');
const path = require('path');
const base = 'C:\\Users\\28767\\Downloads\\cosrealm-site';

const headTpl = (title, theme, extraCSS) =>
`<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${title} | 龙奕学院 LongYi Academy</title>
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="assets/themes/academy/${theme}">
<link rel="stylesheet" href="assets/themes/dark-mode.css">
<link rel="stylesheet" href="assets/effects-layer.css">
<style>*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}body{overflow-x:overlay}
.page-wrap{position:relative;z-index:1;padding-top:72px;max-width:1340px;margin:0 auto;padding-bottom:50px}
.hero-section{position:relative;padding:56px 32px 32px;text-align:center;overflow:hidden}
.hero-section::before{content:'';position:absolute;inset:0;pointer-events:none}
.hero-section h1{font-size:clamp(2rem,5vw,3.2rem);font-weight:900;position:relative;z-index:1;margin-bottom:8px}
.hero-section .hero-sub{font-size:1.05rem;max-width:640px;margin:0 auto 20px;position:relative;z-index:1;opacity:.82;line-height:1.7}
.hero-stats{display:flex;justify-content:center;gap:32px;flex-wrap:wrap;margin-top:16px;position:relative;z-index:1}
.hero-stat{text-align:center;min-width:72px}
.hero-stat .hs-val{font-size:1.8rem;font-weight:900;display:block;line-height:1.1}
.hero-stat .hs-lbl{font-size:.74rem;opacity:.65;margin-top:2px}
.sec-header{display:flex;align-items:center;gap:10px;padding:0 30px;margin-bottom:14px}
.sec-header .sh-icon{font-size:1.5rem}
.sec-header h2{font-size:1.3rem;font-weight:800}
.sec-header .sh-more{margin-left:auto;font-size:.8rem;opacity:.6;text-decoration:none;color:inherit;transition:opacity .2s}
.sec-header .sh-more:hover{opacity:1}
${extraCSS || ''}
@media(max-width:768px){.hero-stats{gap:16px}.hero-section{padding:40px 16px 24px}}
</style>
</head>
<body>
<div id="nav-placeholder"></div>
<div class="page-wrap">`;

const footTpl = `</div>
<script src="assets/nav.js"></script>
<script src="assets/theme-toggle.js"></script>
<script src="assets/dynamic-bg.js"></script>
<script src="assets/effects-runtime.js"></script>
</body>
</html>`;

function write(name, html) {
  fs.writeFileSync(path.join(base, name), html, 'utf8');
  console.log('OK: ' + name + ' (' + html.length + ' chars)');
}

// ===== 3. 商贸学院 shop.html =====
function buildShop() {
  const css = `
.shop-layout{display:flex;gap:20px;padding:0 30px 20px}
.shop-side{width:230px;flex-shrink:0}.shop-main{flex:1;min-width:0}
.fcard{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:16px;margin-bottom:14px}
.fcard h3{font-size:.82rem;opacity:.5;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px}
.fgroup{margin-bottom:12px}.fgroup label{display:flex;align-items:center;gap:6px;padding:5px 0;cursor:pointer;font-size:.82rem}
.fgroup input[type=checkbox]{accent-color:var(--accent)}
.price-rng{display:flex;gap:6px;align-items:center}.price-rng input{width:80px;padding:5px 8px;background:rgba(255,255,255,.04);border:1px solid var(--border);border-radius:6px;color:var(--text);font-size:.78rem}
.shop-search{display:flex;gap:8px;margin-bottom:16px}
.shop-search input{flex:1;padding:11px 16px;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;color:var(--text);font-size:.9rem}
.shop-search input:focus{outline:none;border-color:var(--accent)}
.shop-search select{padding:11px 14px;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;color:var(--text);font-size:.85rem}
.product-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px}
.product-card{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;overflow:hidden;transition:all .3s;cursor:pointer}
.product-card:hover{transform:translateY(-4px);box-shadow:0 12px 36px rgba(0,0,0,.25);border-color:var(--accent)}
.pc-img{height:200px;display:flex;align-items:center;justify-content:center;font-size:3.5rem;position:relative}
.pc-badge{position:absolute;top:10px;left:10px;padding:3px 10px;border-radius:6px;font-size:.66rem;font-weight:700;color:#fff}
.pc-info{padding:14px}.pc-name{font-weight:700;font-size:.92rem;margin-bottom:2px}
.pc-role{font-size:.76rem;opacity:.55;margin-bottom:8px}
.pc-footer{display:flex;align-items:center;justify-content:space-between}
.pc-price{font-size:1.2rem;font-weight:800;color:var(--accent)}.pc-price .orig{font-size:.75rem;opacity:.4;text-decoration:line-through;margin-left:6px}
.pc-cart{padding:7px 14px;border-radius:8px;border:none;background:var(--accent);color:#fff;font-size:.78rem;font-weight:600;cursor:pointer;transition:all .2s}
.pc-cart:hover{transform:scale(1.05)}
.cart-fab{position:fixed;bottom:24px;right:24px;z-index:900;width:54px;height:54px;border-radius:50%;background:var(--accent);border:none;color:#fff;font-size:1.3rem;cursor:pointer;box-shadow:0 4px 24px rgba(0,0,0,.4);transition:all .3s;display:flex;align-items:center;justify-content:center}
.cart-fab:hover{transform:scale(1.12)}
.cart-count{position:absolute;top:-5px;right:-5px;width:22px;height:22px;border-radius:50%;background:#ff4081;font-size:.65rem;font-weight:700;display:flex;align-items:center;justify-content:center}
.cart-panel{position:fixed;top:0;right:-400px;width:360px;height:100vh;z-index:9000;background:var(--bg-deep,var(--bg-card));border-left:1px solid var(--border);transition:right .35s ease;display:flex;flex-direction:column;box-shadow:-4px 0 30px rgba(0,0,0,.5)}
.cart-panel.open{right:0}
.cart-overlay{position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:8999;opacity:0;pointer-events:none;transition:opacity .3s}
.cart-overlay.show{opacity:1;pointer-events:auto}
.cart-hd{padding:18px;border-bottom:1px solid var(--border);display:flex;justify-content:space-between;align-items:center}
.cart-items{flex:1;overflow-y:auto;padding:18px}
.ci-row{display:flex;gap:10px;padding:10px 0;border-bottom:1px solid var(--border)}
.ci-img{width:56px;height:56px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.5rem;flex-shrink:0}
.ci-info{flex:1}.ci-name{font-size:.85rem;font-weight:600}.ci-price{color:var(--accent);font-weight:700;font-size:.82rem;margin-top:2px}
.ci-qty{display:flex;align-items:center;gap:8px;margin-top:4px}
.ci-qty button{width:24px;height:24px;border-radius:50%;border:1px solid var(--border);background:rgba(255,255,255,.04);color:var(--text);cursor:pointer;font-size:.9rem;display:flex;align-items:center;justify-content:center}
.cart-ft{padding:18px;border-top:1px solid var(--border)}
.cart-total{display:flex;justify-content:space-between;font-weight:700;margin-bottom:12px}
.cta-banner{margin:0 30px 20px;padding:24px;border-radius:14px;background:linear-gradient(135deg,rgba(196,77,255,.12),rgba(0,229,255,.08));border:1px solid rgba(196,77,255,.2);display:flex;align-items:center;gap:16px;cursor:pointer;transition:all .3s}
.cta-banner:hover{background:linear-gradient(135deg,rgba(196,77,255,.2),rgba(0,229,255,.14))}
.cta-banner .cta-icon{font-size:2.5rem;flex-shrink:0}
.cta-banner .cta-txt{flex:1}.cta-banner .cta-title{font-weight:700;font-size:1rem;margin-bottom:2px}
.cta-banner .cta-desc{font-size:.78rem;opacity:.6}
.deal-strip{display:flex;gap:12px;overflow-x:auto;padding:0 30px 18px}.deal-strip::-webkit-scrollbar{height:4px}.deal-strip::-webkit-scrollbar-thumb{background:var(--accent);border-radius:4px}
.deal-card{flex:0 0 280px;background:var(--bg-card);border:1px solid var(--border);border-radius:14px;overflow:hidden;cursor:pointer;transition:all .3s}
.deal-card:hover{transform:translateY(-3px);box-shadow:0 10px 30px rgba(0,0,0,.2)}
.deal-card .dc-img{height:140px;display:flex;align-items:center;justify-content:center;font-size:3rem;position:relative}
.deal-card .dc-timer{position:absolute;bottom:8px;right:8px;background:rgba(0,0,0,.7);color:#fff;padding:3px 10px;border-radius:8px;font-size:.68rem;font-weight:700}
.deal-card .dc-info{padding:12px}
.deal-card .dc-price{font-size:1.1rem;font-weight:800;color:#ff4081}
.deal-card .dc-orig{font-size:.72rem;opacity:.4;text-decoration:line-through;margin-left:6px}
@media(max-width:1024px){.shop-layout{flex-direction:column;padding:0 14px 14px}.shop-side{width:100%}.cart-panel{width:100%;right:-100%}}`;

  const body = `
  <div class="hero-section" style="background:radial-gradient(ellipse at 50% 30%,rgba(0,229,255,.1),transparent 70%)">
    <h1 style="background:linear-gradient(135deg,#06b6d4,#22d3ee,#6366f1);-webkit-background-clip:text;-webkit-text-fill-color:transparent">商贸学院</h1>
    <p class="hero-sub">二次元好物一站式购齐——Cos服装、道具、假发、配件，正版授权、品质保障、AI穿搭推荐。立刻开启你的Cos购物之旅。</p>
    <div class="hero-stats"><div class="hero-stat"><span class="hs-val">12,800+</span><span class="hs-lbl">商品SKU</span></div><div class="hero-stat"><span class="hs-val">98.6%</span><span class="hs-lbl">好评率</span></div><div class="hero-stat"><span class="hs-val">24h</span><span class="hs-lbl">极速发货</span></div><div class="hero-stat"><span class="hs-val">7天</span><span class="hs-lbl">无忧退换</span></div></div>
  </div>
  <div class="cta-banner" onclick="location.href='pages/digital-human/dressup.html'">
    <span class="cta-icon">👗</span><div class="cta-txt"><div class="cta-title">AI 3D虚拟试装</div><div class="cta-desc">上传你的照片，用数字人预览服装上身效果。支持360°旋转查看，搭配推荐一键生成。</div></div><span style="font-size:1.5rem">→</span>
  </div>
  <div class="sec-header"><span class="sh-icon">⏰</span><h2>限时特惠</h2><a href="pages/shop/flash.html" class="sh-more">更多 →</a></div>
  <div class="deal-strip" id="dealStrip"></div>
  <div class="shop-layout">
    <aside class="shop-side">
      <div class="fcard"><h3>角色分类</h3><div class="fgroup"><label><input type="checkbox" checked onchange="F()"> 全部</label><label><input type="checkbox" onchange="F()" data-r="genshin"> 原神</label><label><input type="checkbox" onchange="F()" data-r="starrail"> 崩坏：星穹铁道</label><label><input type="checkbox" onchange="F()" data-r="arknights"> 明日方舟</label><label><input type="checkbox" onchange="F()" data-r="spyfamily"> 间谍过家家</label><label><input type="checkbox" onchange="F()" data-r="vocaloid"> VOCALOID</label></div></div>
      <div class="fcard"><h3>商品类型</h3><div class="fgroup"><label><input type="checkbox" onchange="F()" data-t="costume"> 全套服装</label><label><input type="checkbox" onchange="F()" data-t="wig"> 假发/造型</label><label><input type="checkbox" onchange="F()" data-t="prop"> 道具/武器</label><label><input type="checkbox" onchange="F()" data-t="accessory"> 饰品配件</label><label><input type="checkbox" onchange="F()" data-t="shoe"> 鞋子/袜子</label></div></div>
      <div class="fcard"><h3>价格区间</h3><div class="price-rng"><input type="number" placeholder="最低" id="pMin" onchange="F()"><span>—</span><input type="number" placeholder="最高" id="pMax" onchange="F()"></div></div>
    </aside>
    <main class="shop-main">
      <div class="shop-search"><input type="text" placeholder="搜索角色服装、道具... 如 雷电将军 银狼" id="shopQ" oninput="F()"><select id="shopSort" onchange="F()"><option value="default">默认排序</option><option value="price-asc">价格 ↑</option><option value="price-desc">价格 ↓</option><option value="sales">销量优先</option><option value="new">最新上架</option></select></div>
      <div class="product-grid" id="productGrid"></div>
    </main>
  </div>
  <button class="cart-fab" onclick="T()">🛒<span class="cart-count" id="cartCnt">0</span></button>
  <div class="cart-overlay" id="cartOv" onclick="T()"></div>
  <div class="cart-panel" id="cartPn"><div class="cart-hd"><h3>🛒 购物车</h3><button onclick="T()" style="background:none;border:none;color:var(--text);font-size:1.2rem;cursor:pointer">✕</button></div><div class="cart-items" id="cartItems"><p style="text-align:center;opacity:.4;padding:40px 0">购物车空空如也~</p></div><div class="cart-ft"><div class="cart-total"><span>合计</span><span style="color:var(--accent)" id="cartTotal">¥0</span></div><button class="btn btn-primary" style="width:100%;justify-content:center" onclick="K()">💳 立即结算</button></div></div>
<script>
!function(){var ps=[{id:1,n:"雷电将军全套cos服",r:"原神 雷电将军",t:"costume",g:"genshin",p:599,op:799,i:"⚡",bg:"linear-gradient(135deg,#4a148c,#7b1fa2)",b:"hot",s:3200},{id:2,n:"银狼限定cos套装",r:"崩坏：星穹铁道 银狼",t:"costume",g:"starrail",p:489,op:599,i:"🎮",bg:"linear-gradient(135deg,#01579b,#0277bd)",b:"new",s:1800},{id:3,n:"阿米娅兔耳cos假发",r:"明日方舟 阿米娅",t:"wig",g:"arknights",p:128,op:168,i:"🐰",bg:"linear-gradient(135deg,#311b92,#4527a0)",b:"sale",s:5600},{id:4,n:"无想的一刀道具刀",r:"原神 雷电将军",t:"prop",g:"genshin",p:358,op:458,i:"🗡️",bg:"linear-gradient(135deg,#827717,#9e9d24)",b:"hot",s:2400},{id:5,n:"阿尼亚校服cos套装",r:"间谍过家家 阿尼亚",t:"costume",g:"spyfamily",p:268,op:328,i:"🥜",bg:"linear-gradient(135deg,#1b5e20,#2e7d32)",b:"new",s:4100},{id:6,n:"初音未来双马尾假发",r:"VOCALOID 初音未来",t:"wig",g:"vocaloid",p:98,op:128,i:"🎤",bg:"linear-gradient(135deg,#006064,#00838f)",b:"hot",s:8900},{id:7,n:"星穹铁道通票项链",r:"崩坏：星穹铁道",t:"accessory",g:"starrail",p:58,op:78,i:"🎫",bg:"linear-gradient(135deg,#1a237e,#283593)",b:"sale",s:7200},{id:8,n:"银狼cos高跟靴",r:"崩坏：星穹铁道 银狼",t:"shoe",g:"starrail",p:328,op:398,i:"👢",bg:"linear-gradient(135deg,#212121,#424242)",b:"",s:1500},{id:9,n:"班尼特冒险家套装",r:"原神 班尼特",t:"costume",g:"genshin",p:428,op:528,i:"🔥",bg:"linear-gradient(135deg,#bf360c,#e64a19)",b:"",s:980},{id:10,n:"德克萨斯cos剑",r:"明日方舟 德克萨斯",t:"prop",g:"arknights",p:198,op:258,i:"⚔️",bg:"linear-gradient(135deg,#37474f,#546e7a)",b:"new",s:2100},{id:11,n:"约尔荆棘公主cos装",r:"间谍过家家 约尔",t:"costume",g:"spyfamily",p:688,op:888,i:"🌹",bg:"linear-gradient(135deg,#880e4f,#ad1457)",b:"hot",s:760},{id:12,n:"镜音双子假发套装",r:"VOCALOID 镜音双子",t:"wig",g:"vocaloid",p:158,op:198,i:"🎵",bg:"linear-gradient(135deg,#f57f17,#fbc02d)",b:"sale",s:3400}],cart=[];
window.F=function(){var q=(document.getElementById('shopQ').value||'').toLowerCase(),sr=document.getElementById('shopSort').value,mn=parseFloat(document.getElementById('pMin').value)||0,mx=parseFloat(document.getElementById('pMax').value)||Infinity,rs=Array.from(document.querySelectorAll('.fgroup input[data-r]:checked')).map(function(c){return c.dataset.r}),ts=Array.from(document.querySelectorAll('.fgroup input[data-t]:checked')).map(function(c){return c.dataset.t}),f=ps.filter(function(p){if(rs.length>0&&rs.indexOf(p.g)===-1)return false;if(ts.length>0&&ts.indexOf(p.t)===-1)return false;if(p.p<mn||p.p>mx)return false;if(q&&p.n.toLowerCase().indexOf(q)===-1&&p.r.toLowerCase().indexOf(q)===-1)return false;return true});
if(sr==='price-asc')f.sort(function(a,b){return a.p-b.p});else if(sr==='price-desc')f.sort(function(a,b){return b.p-a.p});else if(sr==='sales')f.sort(function(a,b){return b.s-a.s});else if(sr==='new')f.sort(function(a,b){return b.id-a.id});
document.getElementById('productGrid').innerHTML=f.map(function(p){return'<div class="product-card" onclick="alert(\\''+p.n+' 详情 (模拟)\\')"><div class="pc-img" style="background:'+p.bg+'">'+p.i+(p.b?'<span class="pc-badge" style="background:'+(p.b==='hot'?'#ff4081':p.b==='new'?'#00e5ff':'#ffd740')+';color:'+(p.b==='sale'?'#000':'#fff')+'">'+(p.b==='hot'?'热卖':p.b==='new'?'新品':'特价')+'</span>':'')+'</div><div class="pc-info"><div class="pc-name">'+p.n+'</div><div class="pc-role">'+p.r+'</div><div class="pc-footer"><div class="pc-price">¥'+p.p+'<span class="orig">¥'+p.op+'</span></div><button class="pc-cart" onclick="event.stopPropagation();A('+p.id+')">🛒 加入</button></div></div></div>'}).join('')};
window.A=function(id){var p=ps.find(function(x){return x.id===id}),c=cart.find(function(x){return x.id===id});c?c.q++:cart.push({id:p.id,n:p.n,p:p.p,i:p.i,bg:p.bg,q:1});U()};
window.U=function(){var cnt=cart.reduce(function(s,c){return s+c.q},0),tot=cart.reduce(function(s,c){return s+c.p*c.q},0);document.getElementById('cartCnt').textContent=cnt;document.getElementById('cartTotal').textContent='¥'+tot.toLocaleString();var el=document.getElementById('cartItems');el.innerHTML=cart.length===0?'<p style="text-align:center;opacity:.4;padding:40px 0">购物车空空如也~</p>':cart.map(function(c){return'<div class="ci-row"><div class="ci-img" style="background:'+c.bg+'">'+c.i+'</div><div class="ci-info"><div class="ci-name">'+c.n+'</div><div class="ci-price">¥'+c.p+'</div><div class="ci-qty"><button onclick="Q('+c.id+',-1)">−</button><span>'+c.q+'</span><button onclick="Q('+c.id+',1)">+</button></div></div></div>'}).join('')};
window.Q=function(id,d){var c=cart.find(function(x){return x.id===id});if(!c)return;c.q+=d;if(c.q<=0){cart=cart.filter(function(x){return x.id!==id})}U()};
window.T=function(){document.getElementById('cartPn').classList.toggle('open');document.getElementById('cartOv').classList.toggle('show')};
window.K=function(){if(cart.length===0){alert('购物车是空的!');return}var t=cart.reduce(function(s,c){return s+c.p*c.q},0);cart=[];U();T();alert('订单已提交! 共 ¥'+t.toLocaleString())};
document.getElementById('dealStrip').innerHTML=[{n:"雷电将军套装 限时7折",p:419,op:599,i:"⚡",bg:"linear-gradient(135deg,#4a148c,#7b1fa2)",t:"23:59:48"},{n:"初音假发 5折秒杀",p:49,op:98,i:"🎤",bg:"linear-gradient(135deg,#006064,#00838f)",t:"12:30:15"},{n:"星穹铁道通票项链",p:29,op:58,i:"🎫",bg:"linear-gradient(135deg,#1a237e,#283593)",t:"06:15:33"},{n:"银狼限定套装",p:389,op:599,i:"🎮",bg:"linear-gradient(135deg,#01579b,#0277bd)",t:"18:45:02"}].map(function(d){return'<div class="deal-card"><div class="dc-img" style="background:'+d.bg+'">'+d.i+'<span class="dc-timer">⏰ '+d.t+'</span></div><div class="dc-info"><div style="font-weight:600;font-size:.85rem;margin-bottom:4px">'+d.n+'</div><span class="dc-price">¥'+d.p+'</span><span class="dc-orig">¥'+d.op+'</span></div></div>'}).join('');
F()}();
</script>` + footTpl;
  return headTpl('商贸学院', 'mint-academy.css', css) + body;
}

// ===== 4. 虚空学院 metaverse.html =====
function buildMeta() {
  const css = `
.meta-hero h1{background:linear-gradient(135deg,#a78bfa,#7c3aed,#6366f1);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.meta-online{display:inline-flex;align-items:center;gap:6px;padding:6px 18px;background:rgba(34,197,94,.08);border:1px solid rgba(34,197,94,.2);border-radius:20px;color:#22c55e;font-size:.82rem;margin-bottom:16px}
.meta-online .dot{width:8px;height:8px;border-radius:50%;background:#22c55e;animation:pulse 1.5s infinite}@keyframes pulse{50%{opacity:.4}}
.cube-stage{padding:40px 30px;text-align:center}.cube-box{perspective:800px;width:260px;height:260px;margin:0 auto 30px}
.cube{width:100%;height:100%;position:relative;transform-style:preserve-3d;animation:rcube 12s linear infinite}
@keyframes rcube{0%{transform:rotateX(-10deg) rotateY(0)}100%{transform:rotateX(-10deg) rotateY(360deg)}}
.cf{position:absolute;width:260px;height:260px;border:2px solid var(--accent);border-radius:18px;display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:700;gap:8px;backdrop-filter:blur(8px)}
.cf .cemoji{font-size:2.5rem}.cf-front{transform:translateZ(130px);background:rgba(196,77,255,.1)}.cf-back{transform:rotateY(180deg) translateZ(130px);background:rgba(0,229,255,.1)}.cf-right{transform:rotateY(90deg) translateZ(130px);background:rgba(255,64,129,.1)}.cf-left{transform:rotateY(-90deg) translateZ(130px);background:rgba(255,215,64,.1)}.cf-top{transform:rotateX(90deg) translateZ(130px);background:rgba(124,77,255,.1)}.cf-bottom{transform:rotateX(-90deg) translateZ(130px);background:rgba(105,240,174,.1)}
.zone-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px;padding:0 30px 30px}
.zone-card{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:24px;transition:all .35s;cursor:pointer;position:relative;overflow:hidden}
.zone-card:hover{transform:translateY(-4px);box-shadow:0 14px 40px rgba(0,0,0,.25);border-color:var(--accent)}
.zone-card::after{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--accent),transparent);transform:scaleX(0);transition:transform .4s}
.zone-card:hover::after{transform:scaleX(1)}
.zone-card .zi{font-size:2.5rem;display:block;margin-bottom:10px}.zone-card .zn{font-size:1.1rem;font-weight:700;margin-bottom:4px}.zone-card .zd{font-size:.82rem;opacity:.6;margin-bottom:10px;line-height:1.5}.zone-card .zs{display:flex;gap:16px;font-size:.75rem;opacity:.5}
.act-feed{padding:0 30px 30px;max-width:800px;margin:0 auto}
.act-item{display:flex;gap:12px;padding:14px;margin-bottom:8px;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;transition:all .25s}
.act-item:hover{border-color:rgba(255,255,255,.1)}
.act-av{width:42px;height:42px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.1rem;flex-shrink:0}
.act-body{flex:1}.act-body .at{font-size:.85rem}.act-body .at strong{color:var(--accent)}.act-body .atm{font-size:.7rem;opacity:.4;margin-top:2px}
.event-row{display:flex;gap:16px;margin-bottom:12px;background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:18px;cursor:pointer;transition:all .3s}
.event-row:hover{border-color:var(--accent)}
.ev-date{width:62px;height:62px;border-radius:12px;background:var(--accent);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;flex-shrink:0;font-weight:700}.ev-date .day{font-size:1.3rem;line-height:1}.ev-date .mon{font-size:.7rem;opacity:.8}
.ev-info{flex:1}.ev-info h4{font-size:.95rem;margin-bottom:2px}.ev-info p{font-size:.78rem;opacity:.6;line-height:1.4}.ev-tags{display:flex;gap:6px;margin-top:6px;flex-wrap:wrap}
@media(max-width:768px){.cube-box{width:180px;height:180px}.cf{width:180px;height:180px;font-size:.8rem}.cf-front{transform:translateZ(90px)}.cf-back{transform:rotateY(180deg) translateZ(90px)}.cf-right{transform:rotateY(90deg) translateZ(90px)}.cf-left{transform:rotateY(-90deg) translateZ(90px)}.cf-top{transform:rotateX(90deg) translateZ(90px)}.cf-bottom{transform:rotateX(-90deg) translateZ(90px)}.event-row{flex-direction:column}}`;

  return headTpl('虚空学院', 'starlight-academy.css', css) + `
  <div class="hero-section meta-hero">
    <div class="meta-online"><span class="dot"></span>当前在线：<strong id="onlineCnt">1,247</strong> 位Coser</div>
    <h1>虚空学院</h1>
    <p class="hero-sub">进入属于Cosplay爱好者的数字奇点。3D虚拟空间、数字分身交互、实时语音社交——不止于元宇宙，这是第二人生。</p>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;position:relative;z-index:1">
      <button class="btn btn-primary btn-lg" onclick="alert('正在连接3D引擎...🚀')">🌐 进入虚空学院世界</button>
      <button class="btn btn-outline btn-lg" onclick="alert('创建数字分身...')">👤 创建数字分身</button>
    </div>
  </div>
  <div class="cube-stage"><div class="cube-box"><div class="cube" id="mcube">
    <div class="cf cf-front"><span class="cemoji">🐉</span>虚空主城</div><div class="cf cf-back"><span class="cemoji">🎪</span>展览大厅</div><div class="cf cf-right"><span class="cemoji">🛒</span>虚拟商城</div><div class="cf cf-left"><span class="cemoji">🎤</span>演播舞台</div><div class="cf cf-top"><span class="cemoji">🎮</span>游戏广场</div><div class="cf cf-bottom"><span class="cemoji">🏠</span>个人空间</div>
  </div></div><p style="opacity:.5">拖拽旋转 | 6大主题空间</p></div>
  <div class="sec-header"><span class="sh-icon">🏙️</span><h2>主题空间</h2></div>
  <div class="zone-grid">
    <div class="zone-card" onclick="alert('进入虚空主城...')"><span class="zi">🏰</span><div class="zn">虚空主城 · Singularity Hub</div><div class="zd">龙奕学院中心枢纽，龙形雕塑矗立广场，LED粒子瀑布环绕。Coser社交主战场。</div><div class="zs"><span>👥 623在线</span><span>🏛️ 12入口</span></div></div>
    <div class="zone-card" onclick="alert('进入展览大厅...')"><span class="zi">🎨</span><div class="zn">Cosplay虚拟展览厅</div><div class="zd">3D全景展厅展示精选Cos作品。VR沉浸观展，每件作品附制作花絮和Coser语音讲解。</div><div class="zs"><span>🖼️ 286展品</span><span>🏆 本月大赛中</span></div></div>
    <div class="zone-card" onclick="alert('进入虚拟商城...')"><span class="zi">💎</span><div class="zn">虚拟试装商城</div><div class="zd">上传照片或用数字人试穿Cos服装。AI实时渲染，360°查看。连接实体商城一键下单。</div><div class="zs"><span>👘 3200+可试</span><span>🤖 AI试装</span></div></div>
    <div class="zone-card" onclick="alert('进入演播舞台...')"><span class="zi">🎬</span><div class="zn">全息演播舞台</div><div class="zd">数字人驱动虚拟演出空间。Cos走秀、舞台剧、嘉宾访谈——用数字分身上舞台。</div><div class="zs"><span>🎤 本月18场</span><span>📺 直播</span></div></div>
    <div class="zone-card" onclick="alert('进入游戏广场...')"><span class="zi">🎮</span><div class="zn">互动游戏广场</div><div class="zd">Cos主题小游戏大厅。角色问答、摄影挑战、虚拟合影——用游戏连接同好赢积分。</div><div class="zs"><span>🎯 24款游戏</span><span>🏅 积分奖励</span></div></div>
    <div class="zone-card" onclick="alert('进入个人空间...')"><span class="zi">🏠</span><div class="zn">个人元宇宙空间</div><div class="zd">私人领地。自定义装修、展示Cos作品集、邀请好友参观。你的数字分身之家。</div><div class="zs"><span>🏠 52,380空间</span><span>🔒 隐私保护</span></div></div>
  </div>
  <div class="sec-header"><span class="sh-icon">📡</span><h2>实时动态</h2></div>
  <div class="act-feed">
    <div class="act-item"><div class="act-av" style="background:linear-gradient(135deg,#ff4081,#ff80ab)">🌸</div><div class="act-body"><div class="at"><strong>樱落Cos</strong> 进入了展览大厅</div><div class="atm">刚刚</div></div></div>
    <div class="act-item"><div class="act-av" style="background:linear-gradient(135deg,#7c4dff,#b388ff)">⚔️</div><div class="act-body"><div class="at"><strong>SwordArt_Cos</strong> 试穿了 <strong>雷电将军</strong> 服装</div><div class="atm">2分钟前</div></div></div>
    <div class="act-item"><div class="act-av" style="background:linear-gradient(135deg,#00e5ff,#80deea)">💎</div><div class="act-body"><div class="at"><strong>星穹铁道Cos社</strong> 举办了虚拟Cos大赛</div><div class="atm">5分钟前</div></div></div>
    <div class="act-item"><div class="act-av" style="background:linear-gradient(135deg,#69f0ae,#b9f6ca)">🐱</div><div class="act-body"><div class="at"><strong>小透明Coser</strong> 完成了一次AI试装体验</div><div class="atm">8分钟前</div></div></div>
  </div>
  <div class="sec-header"><span class="sh-icon">📅</span><h2>活动日历</h2></div>
  <div style="padding:0 30px 30px;max-width:900px;margin:0 auto">
    <div class="event-row"><div class="ev-date"><span class="day">28</span><span class="mon">6月</span></div><div class="ev-info"><h4>龙奕学院首届虚拟Cos大赛 · 决赛</h4><p>20位Coser在全息舞台最终对决，评审团+观众投票。总奖金池20万元。</p><div class="ev-tags"><span class="tag">Cos大赛</span><span class="tag">线上</span><span class="tag">有奖</span></div></div></div>
    <div class="event-row"><div class="ev-date"><span class="day">15</span><span class="mon">7月</span></div><div class="ev-info"><h4>崩坏：星穹铁道 主题展览周</h4><p>龙奕学院展览厅举办星穹铁道专题展，限定虚拟空间+官方联动道具+Coser交流会。</p><div class="ev-tags"><span class="tag">主题展</span><span class="tag">联动</span><span class="tag">限定</span></div></div></div>
    <div class="event-row"><div class="ev-date"><span class="day">1</span><span class="mon">8月</span></div><div class="ev-info"><h4>龙奕学院夏日祭 · 元宇宙庆典</h4><p>年度最大活动！烟花大会+虚拟庙会+Cos游行+限定商品，连续3天72小时不间断。</p><div class="ev-tags"><span class="tag">年度盛典</span><span class="tag">夏日祭</span><span class="tag">限定</span></div></div></div>
  </div>
<script>
!function(){setInterval(function(){var e=document.getElementById('onlineCnt');if(e)e.textContent=(1200+Math.random()*100|0).toLocaleString()},5000);
var c=document.getElementById('mcube'),d=false,sx,sy,rx=-10,ry=0;c.addEventListener('mousedown',function(e){d=true;sx=e.clientX;sy=e.clientY;c.style.animation='none';c.style.transform='rotateX('+rx+'deg) rotateY('+ry+'deg)'});
window.addEventListener('mousemove',function(e){if(!d)return;ry+=(e.clientX-sx)*.5;rx-=(e.clientY-sy)*.5;c.style.transform='rotateX('+rx+'deg) rotateY('+ry+'deg)';sx=e.clientX;sy=e.clientY});
window.addEventListener('mouseup',function(){if(d){d=false;setTimeout(function(){c.style.transform='rotateX(-10deg) rotateY(0deg)';c.style.transition='transform 1s ease';setTimeout(function(){c.style.animation='rcube 12s linear infinite';c.style.transition=''},1000)},2000)}})}();
</script>` + footTpl;
}

// ===== 5. 创作学院 creator.html =====
function buildCreator() {
  const css = `
.cr-hero{background:radial-gradient(ellipse at 40% 30%,rgba(59,130,246,.12),transparent 60%),radial-gradient(ellipse at 60% 70%,rgba(6,182,212,.08),transparent 60%)}
.cr-hero h1{background:linear-gradient(135deg,#3b82f6,#06b6d4,#6366f1);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.dash-grid{display:grid;grid-template-columns:2fr 1fr;gap:16px;padding:0 30px 30px}
.dash-main{display:flex;flex-direction:column;gap:16px}
.stat-row{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.stat-box{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:20px;text-align:center;transition:all .3s}
.stat-box:hover{border-color:var(--accent);transform:translateY(-2px)}
.stat-box .sn{font-size:1.8rem;font-weight:900;color:var(--accent);display:block}
.stat-box .sl{font-size:.74rem;opacity:.5;margin-top:2px}
.stat-box .st{font-size:.68rem;margin-top:2px}.st.up{color:#22c55e}.st.down{color:#ef4444}
.tools-card{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:22px}
.tools-card h2{font-size:1.05rem;margin-bottom:14px}
.tool-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.tool-item{text-align:center;padding:16px 10px;border-radius:12px;border:1px solid var(--border);transition:all .3s;cursor:pointer;text-decoration:none;color:inherit}
.tool-item:hover{transform:translateY(-3px);box-shadow:0 8px 28px rgba(59,130,246,.15);border-color:var(--accent)}
.tool-item .ti{font-size:2rem;display:block;margin-bottom:4px}.tool-item .tn{font-weight:600;font-size:.78rem}
.dash-side{display:flex;flex-direction:column;gap:16px}
.side-card{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:20px}
.side-card h3{font-size:.9rem;margin-bottom:12px}
.trend-row2{display:flex;align-items:center;gap:8px;padding:8px 0;border-bottom:1px solid var(--border);cursor:pointer;transition:all .2s}
.trend-row2:last-child{border-bottom:none}.trend-row2:hover{color:var(--accent)}
.tr-rank{font-weight:900;font-size:.9rem;color:var(--accent);width:24px}
.tr-info{flex:1}.tr-name{font-size:.8rem;font-weight:500}.tr-meta{font-size:.68rem;opacity:.5}
.collab-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;padding:0 30px 30px}
.collab-card{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:20px;text-align:center;transition:all .3s;cursor:pointer;text-decoration:none;color:inherit}
.collab-card:hover{transform:translateY(-4px);box-shadow:0 10px 28px rgba(59,130,246,.15)}
.collab-card .ci{font-size:2.2rem;display:block;margin-bottom:8px}.collab-card .cn{font-weight:700;font-size:.9rem;margin-bottom:2px}.collab-card .cd{font-size:.74rem;opacity:.6}
.rev-row{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;padding:0 30px 30px}
.rev-card{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:20px;text-decoration:none;color:inherit;transition:all .3s}
.rev-card:hover{transform:translateY(-3px);box-shadow:0 10px 28px rgba(59,130,246,.12)}
.rev-card .ri{font-size:2rem;display:block;margin-bottom:8px}.rev-card .rn{font-weight:700;font-size:.9rem}
@media(max-width:768px){.dash-grid,.stat-row{grid-template-columns:1fr}.tool-grid,.collab-grid,.rev-row{grid-template-columns:repeat(2,1fr)}}`;

  return headTpl('创作学院', 'sky-academy.css', css) + `
  <div class="hero-section cr-hero"><h1>创作学院</h1><p class="hero-sub">一站式创作平台——AI辅助创作工具、版权管理、收益变现、粉丝互动、协作广场，让你的创作才华绽放光芒。</p></div>
  <div class="dash-grid">
    <div class="dash-main">
      <div class="stat-row">
        <div class="stat-box"><span class="sn">128</span><span class="sl">我的作品</span><span class="st up">↑ 12% 本月</span></div>
        <div class="stat-box"><span class="sn">8.9万</span><span class="sl">累计播放</span><span class="st up">↑ 23% 本月</span></div>
        <div class="stat-box"><span class="sn">¥4,280</span><span class="sl">创作收益</span><span class="st up">↑ 15% 本月</span></div>
        <div class="stat-box"><span class="sn">3,456</span><span class="sl">粉丝数</span><span class="st up">↑ 8% 本月</span></div>
      </div>
      <div class="tools-card"><h2>🛠️ AI创作工具套件</h2><div class="tool-grid">
        <a href="pages/creator/workshop.html" class="tool-item"><span class="ti">🎨</span><span class="tn">AI绘画</span></a>
        <a href="pages/creator/workshop.html" class="tool-item"><span class="ti">✂️</span><span class="tn">视频剪辑</span></a>
        <a href="pages/creator/workshop.html" class="tool-item"><span class="ti">🎵</span><span class="tn">音频处理</span></a>
        <a href="pages/creator/workshop.html" class="tool-item"><span class="ti">🎬</span><span class="tn">3D建模</span></a>
        <a href="pages/creator/tools.html" class="tool-item"><span class="ti">📝</span><span class="tn">剧本助手</span></a>
        <a href="pages/creator/tools.html" class="tool-item"><span class="ti">🖼️</span><span class="tn">AI修图</span></a>
        <a href="pages/creator/tools.html" class="tool-item"><span class="ti">🎭</span><span class="tn">角色设计</span></a>
        <a href="pages/creator/tools.html" class="tool-item"><span class="ti">📊</span><span class="tn">数据分析</span></a>
      </div></div>
    </div>
    <div class="dash-side">
      <div class="side-card"><h3>🔥 创作趋势</h3>
        <div class="trend-row2"><span class="tr-rank">01</span><div class="tr-info"><div class="tr-name">AI生成Cosplay写真</div><div class="tr-meta">↑ 280%</div></div></div>
        <div class="trend-row2"><span class="tr-rank">02</span><div class="tr-info"><div class="tr-name">数字人虚拟偶像出道</div><div class="tr-meta">↑ 195%</div></div></div>
        <div class="trend-row2"><span class="tr-rank">03</span><div class="tr-info"><div class="tr-name">元宇宙Cos短剧</div><div class="tr-meta">↑ 167%</div></div></div>
        <div class="trend-row2"><span class="tr-rank">04</span><div class="tr-info"><div class="tr-name">3D打印道具制作</div><div class="tr-meta">↑ 140%</div></div></div>
        <div class="trend-row2"><span class="tr-rank">05</span><div class="tr-info"><div class="tr-name">AR实时Cos滤镜</div><div class="tr-meta">↑ 122%</div></div></div>
      </div>
      <div class="side-card"><h3>📢 公告</h3><div style="font-size:.78rem;opacity:.7;line-height:1.7">• 夏季创作激励计划开启，奖金池100万<br>• AI配音工具上线，支持50+语言<br>• 版权保护系统v3.0<br>• 创作者等级体系上线</div></div>
    </div>
  </div>
  <div class="sec-header"><span class="sh-icon">🤝</span><h2>协作广场</h2></div>
  <div class="collab-grid">
    <a href="pages/creator/collab.html" class="collab-card"><span class="ci">🎬</span><div class="cn">寻找摄影师</div><div class="cd">找专业Cos摄影师</div></a>
    <a href="pages/creator/collab.html" class="collab-card"><span class="ci">👗</span><div class="cn">服装定制师</div><div class="cd">专属Cos服装定制</div></a>
    <a href="pages/creator/collab.html" class="collab-card"><span class="ci">🖌️</span><div class="cn">后期修图师</div><div class="cd">专业后期特效合成</div></a>
    <a href="pages/creator/collab.html" class="collab-card"><span class="ci">🗡️</span><div class="cn">道具工作室</div><div class="cd">3D打印+手工锻造</div></a>
    <a href="pages/creator/collab.html" class="collab-card"><span class="ci">💄</span><div class="cn">特效化妆师</div><div class="cd">伤妆/科幻妆/奇幻妆</div></a>
    <a href="pages/creator/collab.html" class="collab-card"><span class="ci">🎤</span><div class="cn">配音工作室</div><div class="cd">角色配音+音效</div></a>
  </div>
  <div class="sec-header"><span class="sh-icon">💎</span><h2>收益管理</h2></div>
  <div class="rev-row">
    <a href="pages/creator/income.html" class="rev-card"><span class="ri">💰</span><div class="rn">创作收益</div><div style="font-size:.72rem;opacity:.5;margin-top:2px">打赏 · 分成 · 广告</div></a>
    <a href="pages/creator/fans.html" class="rev-card"><span class="ri">👥</span><div class="rn">粉丝管理</div><div style="font-size:.72rem;opacity:.5;margin-top:2px">数据分析 · 粉丝画像</div></a>
    <a href="pages/creator/dashboard.html" class="rev-card"><span class="ri">📊</span><div class="rn">创作仪表盘</div><div style="font-size:.72rem;opacity:.5;margin-top:2px">全维度数据总览</div></a>
  </div>` + footTpl;
}

// ===== 6. 幻影学院 digital-human.html =====
function buildDH() {
  const css = `
.dh-layout{display:grid;grid-template-columns:350px 1fr;gap:20px;padding:0 30px 30px}
.dh-controls{display:flex;flex-direction:column;gap:14px}
.ctrl-card{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:18px}
.ctrl-card h3{font-size:.88rem;margin-bottom:10px}
.style-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.style-opt{padding:14px 8px;border-radius:10px;border:2px solid transparent;background:rgba(255,255,255,.03);text-align:center;cursor:pointer;transition:all .25s;font-size:.76rem}
.style-opt:hover{background:rgba(255,255,255,.06)}
.style-opt.selected{border-color:var(--accent);background:rgba(196,77,255,.1)}
.style-opt .se{font-size:1.8rem;display:block;margin-bottom:4px}
.slider-group{margin-bottom:12px}.slider-group label{display:flex;justify-content:space-between;font-size:.78rem;opacity:.6;margin-bottom:4px}.slider-group label span{color:var(--accent)}
.slider-group input[type=range]{width:100%;-webkit-appearance:none;height:5px;background:rgba(255,255,255,.08);border-radius:3px;outline:none}
.slider-group input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:18px;height:18px;border-radius:50%;background:var(--accent);cursor:pointer;box-shadow:0 0 10px var(--accent)}
.color-grid{display:flex;gap:8px;flex-wrap:wrap}.color-dot{width:26px;height:26px;border-radius:50%;cursor:pointer;border:2px solid transparent;transition:all .2s}.color-dot:hover{transform:scale(1.15)}.color-dot.selected{border-color:#fff;box-shadow:0 0 12px currentColor}
.preview-stage{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;min-height:500px;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden}
.preview-stage::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(196,77,255,.08),transparent 60%)}
.pv-avatar{position:relative;z-index:1;text-align:center;transition:all .5s}
.pv-avatar .face{font-size:7rem;display:block;margin-bottom:6px;transition:all .5s}
.pv-avatar .pv-name{font-size:1.1rem;font-weight:700}
.pv-avatar .pv-info{font-size:.8rem;opacity:.5}
.voice-wave{display:flex;gap:3px;justify-content:center;height:20px;margin-top:6px;opacity:0;transition:opacity .3s}
.voice-wave.show{opacity:1}.voice-wave .bar{width:4px;border-radius:2px;background:var(--accent);animation:vwAnim .6s ease-in-out infinite alternate}@keyframes vwAnim{to{height:16px}}.voice-wave .bar:nth-child(2){animation-delay:.1s}.voice-wave .bar:nth-child(3){animation-delay:.2s}.voice-wave .bar:nth-child(4){animation-delay:.3s}.voice-wave .bar:nth-child(5){animation-delay:.4s}
.quick-links{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;padding:0 30px 30px}
.ql-card{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:20px;text-align:center;transition:all .3s;cursor:pointer;text-decoration:none;color:inherit}
.ql-card:hover{transform:translateY(-4px);box-shadow:0 10px 30px rgba(196,77,255,.15);border-color:var(--accent)}
.ql-card .qi{font-size:2.2rem;display:block;margin-bottom:8px}.ql-card .qn{font-weight:700;font-size:.85rem}
.feature-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;padding:0 30px 30px}
.feat-card{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:22px;transition:all .3s;cursor:pointer;text-decoration:none;color:inherit}
.feat-card:hover{transform:translateY(-3px);box-shadow:0 10px 28px rgba(0,0,0,.15);border-color:var(--accent)}
.feat-card .fi{font-size:2rem;display:block;margin-bottom:8px}.feat-card .fn{font-weight:700;font-size:.92rem;margin-bottom:4px}.feat-card .fd{font-size:.76rem;opacity:.6;line-height:1.4}
@media(max-width:768px){.dh-layout{grid-template-columns:1fr}.quick-links,.feature-grid{grid-template-columns:repeat(2,1fr)}}`;

  return headTpl('幻影学院', 'sunset-academy.css', css) + `
  <div class="hero-section" style="background:radial-gradient(ellipse at 50% 30%,rgba(196,77,255,.1),transparent 70%)"><h1 style="background:linear-gradient(135deg,#c44dff,#ec4899,#6366f1);-webkit-background-clip:text;-webkit-text-fill-color:transparent">幻影学院</h1><p class="hero-sub">创造属于你的数字分身——3D捏脸、AI驱动交互、语音合成、动作捕捉。接入大模型，让你的数字人活起来。</p><div class="hero-stats"><div class="hero-stat"><span class="hs-val">156,820</span><span class="hs-lbl">已创建数字人</span></div><div class="hero-stat"><span class="hs-val">98.7%</span><span class="hs-lbl">AI识别准确率</span></div><div class="hero-stat"><span class="hs-val">&lt;50ms</span><span class="hs-lbl">语音合成延迟</span></div><div class="hero-stat"><span class="hs-val">24/7</span><span class="hs-lbl">在线运行</span></div></div></div>
  <div class="quick-links">
    <a href="pages/digital-human/dressup.html" class="ql-card"><span class="qi">👗</span><div class="qn">3D换装工坊</div></a>
    <a href="pages/digital-human/llm-interactive.html" class="ql-card"><span class="qi">🤖</span><div class="qn">LLM智能互动</div></a>
    <a href="pages/digital-human/studio.html" class="ql-card"><span class="qi">🎨</span><div class="qn">数字人Studio</div></a>
    <a href="pages/digital-human/livecast.html" class="ql-card"><span class="qi">📺</span><div class="qn">虚拟直播</div></a>
  </div>
  <div class="dh-layout">
    <div class="dh-controls">
      <div class="ctrl-card"><h3>🎨 风格预设</h3><div class="style-grid">
        <div class="style-opt selected" onclick="document.querySelectorAll('.style-opt').forEach(function(e){e.classList.remove('selected')});this.classList.add('selected');document.querySelector('.face').textContent='🧝'"><span class="se">🧝</span>奇幻</div>
        <div class="style-opt" onclick="document.querySelectorAll('.style-opt').forEach(function(e){e.classList.remove('selected')});this.classList.add('selected');document.querySelector('.face').textContent='🤖'"><span class="se">🤖</span>科幻</div>
        <div class="style-opt" onclick="document.querySelectorAll('.style-opt').forEach(function(e){e.classList.remove('selected')});this.classList.add('selected');document.querySelector('.face').textContent='🦸'"><span class="se">🦸</span>英雄</div>
        <div class="style-opt" onclick="document.querySelectorAll('.style-opt').forEach(function(e){e.classList.remove('selected')});this.classList.add('selected');document.querySelector('.face').textContent='👻'"><span class="se">👻</span>幽灵</div>
        <div class="style-opt" onclick="document.querySelectorAll('.style-opt').forEach(function(e){e.classList.remove('selected')});this.classList.add('selected');document.querySelector('.face').textContent='🐉'"><span class="se">🐉</span>龙族</div>
        <div class="style-opt" onclick="document.querySelectorAll('.style-opt').forEach(function(e){e.classList.remove('selected')});this.classList.add('selected');document.querySelector('.face').textContent='😺'"><span class="se">😺</span>猫耳</div>
      </div></div>
      <div class="ctrl-card"><h3>⚙️ 参数调节</h3>
        <div class="slider-group"><label>身高 <span id="hv">170</span>cm</label><input type="range" min="140" max="200" value="170" oninput="document.getElementById('hv').textContent=this.value;var s=1+(this.value-170)/200;document.getElementById('pvStage').style.transform='scaleY('+s+')'"></div>
        <div class="slider-group"><label>体型 <span id="bv">50</span></label><input type="range" min="20" max="100" value="50" oninput="document.getElementById('bv').textContent=this.value;var w=0.7+(this.value/100)*0.6;document.getElementById('pvStage').style.transform=document.getElementById('pvStage').style.transform.replace(/scaleX\\([^)]*\\)/,'')+' scaleX('+w+')'"></div>
        <div class="slider-group"><label>表情强度 <span id="ev">60</span>%</label><input type="range" min="0" max="100" value="60" oninput="document.getElementById('ev').textContent=this.value;document.querySelector('.face').style.filter='brightness('+(0.5+this.value/200)+')'"></div>
      </div>
      <div class="ctrl-card"><h3>🎨 主题色</h3><div class="color-grid"><div class="color-dot selected" style="background:#c44dff" onclick="pickColor(this,'#c44dff')"></div><div class="color-dot" style="background:#00e5ff" onclick="pickColor(this,'#00e5ff')"></div><div class="color-dot" style="background:#ff4081" onclick="pickColor(this,'#ff4081')"></div><div class="color-dot" style="background:#ffd740" onclick="pickColor(this,'#ffd740')"></div><div class="color-dot" style="background:#69f0ae" onclick="pickColor(this,'#69f0ae')"></div><div class="color-dot" style="background:#ff6b9d" onclick="pickColor(this,'#ff6b9d')"></div></div></div>
    </div>
    <div class="preview-stage" id="pvStage">
      <div class="pv-avatar"><span class="face">🧝</span><div class="pv-name">数字人预览</div><div class="pv-info" style="margin-top:2px">调整左侧参数实时查看效果</div><div class="voice-wave show"><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div></div></div>
    </div>
  </div>
  <div class="sec-header"><span class="sh-icon">✨</span><h2>核心功能</h2></div>
  <div class="feature-grid">
    <a href="pages/digital-human/studio.html" class="feat-card"><span class="fi">🎨</span><div class="fn">3D捏脸系统</div><div class="fd">200+可调节参数，从脸型到瞳孔细节。AI辅助生成，一键匹配真人照片。</div></a>
    <a href="pages/digital-human/animate.html" class="feat-card"><span class="fi">🕺</span><div class="fn">动作捕捉</div><div class="fd">支持摄像头实时动捕，无需专业设备。AI补全遮挡部位，动作流畅自然。</div></a>
    <a href="pages/digital-human/voice.html" class="feat-card"><span class="fi">🎙️</span><div class="fn">语音合成</div><div class="fd">50+角色声线，支持情绪调节、语速控制。TTS延迟低于50ms，几乎零等待。</div></a>
    <a href="pages/digital-human/ai-chat.html" class="feat-card"><span class="fi">💬</span><div class="fn">AI角色对话</div><div class="fd">接入GPT/Claude等大模型，角色人格化设定。记忆上下文，自然流畅对话。</div></a>
    <a href="pages/digital-human/emotion.html" class="feat-card"><span class="fi">😊</span><div class="fn">情感引擎</div><div class="fd">识别用户输入情绪，自动匹配面部表情和肢体语言。喜怒哀乐，栩栩如生。</div></a>
    <a href="pages/digital-human/scene.html" class="feat-card"><span class="fi">🌆</span><div class="fn">场景工坊</div><div class="fd">100+虚拟场景模板，支持自定义背景和光影。一键切换，实时渲染。</div></a>
  </div>
<script>function pickColor(el,c){document.querySelectorAll('.color-dot').forEach(function(e){e.classList.remove('selected')});el.classList.add('selected');document.querySelector('.voice-wave .bar').forEach?Array.from(document.querySelectorAll('.voice-wave .bar')).forEach(function(b){b.style.background=c}):null}</script>` + footTpl;
}

// Write them
write('shop.html', buildShop());
write('metaverse.html', buildMeta());
write('creator.html', buildCreator());
write('digital-human.html', buildDH());

console.log('Part 2 done - shop, metaverse, creator, digital-human');

// gen_enriched.js — Generate enriched academy homepage HTML files
// Uses Node.js template literals to avoid Python's curly-brace escaping issues
const fs = require('fs');
const path = require('path');

const SITE = 'C:/Users/28767/Downloads/cosrealm-site';

// ============================================================
// 1. 研修学院 (academy.html) — 完全重写为标准模板
// ============================================================
const academyHTML = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>研修学院 | 龙奕学院 LongYi Academy</title>
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="assets/themes/academy/sky-academy.css">
<link rel="stylesheet" href="assets/themes/dark-mode.css">
<link rel="stylesheet" href="assets/effects-layer.css">
<style>*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}body{overflow-x:overlay}
.page-wrap{position:relative;z-index:1;padding-top:72px;max-width:1340px;margin:0 auto;padding-bottom:50px}
.hero-section{position:relative;padding:56px 32px 32px;text-align:center;overflow:hidden}
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

.academy-hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 30%,rgba(59,130,246,.1),transparent 70%),radial-gradient(ellipse at 80% 70%,rgba(6,182,212,.08),transparent 60%);pointer-events:none}
.academy-hero h1{background:linear-gradient(135deg,#3b82f6,#06b6d4,#6366f1);-webkit-background-clip:text;-webkit-text-fill-color:transparent}

.learning-path{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-bottom:20px;position:relative;z-index:1}
.path-step{padding:14px 24px;background:var(--bg-card);border:1px solid var(--border);border-radius:14px;text-align:center;transition:all .3s;cursor:pointer;min-width:120px;text-decoration:none;color:inherit}
.path-step:hover{border-color:var(--accent);transform:translateY(-2px);box-shadow:0 8px 24px rgba(59,130,246,.12)}
.path-step .num{width:32px;height:32px;border-radius:50%;margin:0 auto 8px;background:var(--accent);color:#fff;font-weight:800;font-size:.9rem;display:flex;align-items:center;justify-content:center}
.path-step .label{font-size:.85rem;font-weight:600}
.path-step .sub{font-size:.7rem;opacity:.5}
.path-arrow{display:flex;align-items:center;color:var(--accent);font-size:1.2rem;flex-shrink:0;padding:0 4px}

.feat-banner{position:relative;margin:0 30px 20px;border-radius:18px;overflow:hidden;height:260px;cursor:pointer;background:linear-gradient(135deg,#1e3a5f,#0f2b46,#1a4a6e)}
.feat-banner .fb-overlay{position:absolute;bottom:0;left:0;right:0;padding:36px;background:linear-gradient(transparent,rgba(0,0,0,.88))}
.feat-banner .fb-tag{display:inline-block;background:var(--accent);color:#fff;padding:4px 14px;border-radius:12px;font-size:.72rem;font-weight:700;margin-bottom:8px}
.feat-banner .fb-title{font-size:1.7rem;font-weight:900;color:#fff;margin-bottom:4px}
.feat-banner .fb-desc{font-size:.85rem;color:rgba(255,255,255,.65);max-width:500px;line-height:1.5}

.quick-row{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;padding:0 30px 20px}
.qcard{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:20px;text-align:center;transition:all .3s;cursor:pointer;text-decoration:none;color:inherit}
.qcard:hover{transform:translateY(-4px);box-shadow:0 12px 36px rgba(0,0,0,.2);border-color:var(--accent)}
.qcard .qi{font-size:2.2rem;display:block;margin-bottom:6px}
.qcard .qt{font-weight:700;font-size:.9rem;margin-bottom:2px}
.qcard .qd{font-size:.74rem;opacity:.6}

.tutorial-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:18px;padding:0 30px 20px}
.tcard{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:26px;transition:all .35s;cursor:pointer;position:relative;overflow:hidden;text-decoration:none;color:inherit}
.tcard:hover{transform:translateY(-4px);box-shadow:0 14px 40px rgba(59,130,246,.2);border-color:var(--accent)}
.tcard .diff{position:absolute;top:14px;right:14px;padding:3px 10px;border-radius:6px;font-size:.7rem;font-weight:700}
.diff.beginner{background:rgba(105,240,174,.15);color:#69f0ae}
.diff.intermediate{background:rgba(255,215,64,.15);color:#ffd740}
.diff.advanced{background:rgba(255,64,129,.15);color:#ff4081}
.tcard .ti{font-size:2.5rem;margin-bottom:10px;display:block}
.tcard .tt{font-size:1.1rem;font-weight:700;margin-bottom:8px;padding-right:70px}
.tcard .td{font-size:.82rem;opacity:.6;margin-bottom:12px;line-height:1.6}
.tcard .tm{display:flex;gap:14px;font-size:.76rem;opacity:.45}

.gear-section{padding:0 30px 30px}
.gear-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}
.gcard{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:22px;transition:all .3s;cursor:pointer;text-decoration:none;color:inherit}
.gcard:hover{border-color:var(--accent);transform:translateY(-2px)}
.gcard .gi{font-size:2rem;display:block;margin-bottom:8px}
.gcard .gn{font-weight:700;font-size:.92rem;margin-bottom:4px}
.gcard .gd{font-size:.78rem;opacity:.6;line-height:1.5;margin-bottom:10px}
.gcard .gtags{display:flex;gap:6px;flex-wrap:wrap}
.gtag{padding:3px 10px;border-radius:8px;font-size:.68rem;background:rgba(255,255,255,.04);border:1px solid var(--border)}

.faq-section{padding:0 30px 30px;max-width:900px;margin:0 auto}
.faq-item{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;margin-bottom:10px;overflow:hidden;transition:all .3s}
.faq-item:hover{border-color:rgba(255,255,255,.12)}
.faq-q{padding:16px 22px;display:flex;align-items:center;justify-content:space-between;cursor:pointer;font-weight:600;font-size:.92rem}
.faq-q .arrow{transition:transform .3s;color:var(--accent)}
.faq-item.open .faq-q .arrow{transform:rotate(180deg)}
.faq-a{max-height:0;overflow:hidden;transition:max-height .4s ease;padding:0 22px;color:var(--text-secondary);font-size:.85rem;line-height:1.7}
.faq-item.open .faq-a{max-height:300px;padding-bottom:18px}

.live-class-strip{display:flex;gap:12px;overflow-x:auto;padding:0 30px 20px;scroll-snap-type:x mandatory}
.live-class-strip::-webkit-scrollbar{height:4px}
.live-class-strip::-webkit-scrollbar-thumb{background:var(--accent);border-radius:4px}
.lc-item{flex:0 0 220px;background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:18px;scroll-snap-align:start;transition:all .3s;cursor:pointer;text-decoration:none;color:inherit}
.lc-item:hover{border-color:var(--accent);transform:translateY(-2px)}
.lc-item .lci{font-size:2rem;display:block;margin-bottom:8px}
.lc-item .lct{font-weight:600;font-size:.85rem;margin-bottom:4px}
.lc-item .lcm{font-size:.72rem;opacity:.5}
.lc-item .lcbadge{display:inline-block;margin-top:8px;padding:2px 8px;border-radius:6px;font-size:.66rem;font-weight:700}

.student-showcase{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px;padding:0 30px 20px}
.scard{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;overflow:hidden;transition:all .3s;cursor:pointer;text-decoration:none;color:inherit;text-align:center}
.scard:hover{transform:translateY(-4px);box-shadow:0 10px 30px rgba(59,130,246,.15);border-color:var(--accent)}
.scard .sc-thumb{height:160px;display:flex;align-items:center;justify-content:center;font-size:4rem}
.scard .sc-info{padding:14px}
.scard .sc-name{font-weight:700;font-size:.85rem;margin-bottom:2px}
.scard .sc-meta{font-size:.72rem;opacity:.5}

@media(max-width:768px){
  .quick-row,.tutorial-grid,.gear-grid,.student-showcase{grid-template-columns:repeat(2,1fr)}
  .learning-path{flex-direction:column;align-items:center}.path-arrow{transform:rotate(90deg)}
  .feat-banner{height:200px;margin:0 14px 16px}
  .hero-stats{gap:16px}.hero-section{padding:40px 16px 24px}
}
</style>
</head>
<body>
<div id="nav-placeholder"></div>
<div class="page-wrap">
  <div class="hero-section academy-hero">
    <h1>研修学院</h1>
    <p class="hero-sub">从零基础到专业Coser的系统化学习路径。AI驱动个性化推荐，覆盖化妆、道具、摄影、后期等全流程，千万Coser的成长基地。</p>
    <div class="hero-stats">
      <div class="hero-stat"><span class="hs-val" id="courseCount">2,847</span><span class="hs-lbl">精品课程</span></div>
      <div class="hero-stat"><span class="hs-val" id="studentCount">89.6万</span><span class="hs-lbl">在学学员</span></div>
      <div class="hero-stat"><span class="hs-val">98.2%</span><span class="hs-lbl">好评率</span></div>
      <div class="hero-stat"><span class="hs-val">1,247</span><span class="hs-lbl">导师入驻</span></div>
    </div>
    <div class="learning-path">
      <a href="pages/academy/courses.html" class="path-step"><div class="num">1</div><div class="label">了解Cosplay</div><div class="sub">基础知识入门</div></a>
      <span class="path-arrow">→</span>
      <a href="pages/academy/courses.html" class="path-step"><div class="num">2</div><div class="label">选择角色</div><div class="sub">AI智能推荐</div></a>
      <span class="path-arrow">→</span>
      <a href="pages/academy/courses.html" class="path-step"><div class="num">3</div><div class="label">服装道具</div><div class="sub">采购与制作</div></a>
      <span class="path-arrow">→</span>
      <a href="pages/academy/courses.html" class="path-step"><div class="num">4</div><div class="label">化妆造型</div><div class="sub">技巧入门</div></a>
      <span class="path-arrow">→</span>
      <a href="pages/academy/courses.html" class="path-step"><div class="num">5</div><div class="label">拍摄后期</div><div class="sub">出片全流程</div></a>
      <span class="path-arrow">→</span>
      <a href="pages/academy/courses.html" class="path-step"><div class="num">6</div><div class="label">发布分享</div><div class="sub">社区互动</div></a>
    </div>
  </div>

  <div class="feat-banner" onclick="location.href='pages/academy/path.html'">
    <div class="fb-overlay">
      <span class="fb-tag">🌟 推荐学习路径</span>
      <div class="fb-title">AI智能学习规划 — 你的专属Cos成长之路</div>
      <div class="fb-desc">上传你的照片和目标，AI分析你的体型、肤色、预算和偏好，生成个性化学习计划。从选角到出片，AI全程陪伴。</div>
    </div>
  </div>

  <div class="quick-row">
    <a href="pages/academy/courses.html" class="qcard"><span class="qi">📚</span><div class="qt">课程中心</div><div class="qd">系统化学习路径</div></a>
    <a href="pages/academy/videos.html" class="qcard"><span class="qi">🎬</span><div class="qt">视频教程</div><div class="qd">免费高清教学</div></a>
    <a href="pages/academy/challenge.html" class="qcard"><span class="qi">🎯</span><div class="qt">挑战任务</div><div class="qd">实战检验技能</div></a>
    <a href="pages/academy/ranking.html" class="qcard"><span class="qi">🏆</span><div class="qt">学霸排行</div><div class="qd">学习PK竞技</div></a>
  </div>

  <div class="sec-header"><span class="sh-icon">📺</span><h2>直播课堂 · 即将开讲</h2><a href="pages/academy/live-class.html" class="sh-more">全部课程 →</a></div>
  <div class="live-class-strip" id="liveStrip"></div>

  <div class="sec-header"><span class="sh-icon">📚</span><h2>系统化教程</h2><a href="pages/academy/courses.html" class="sh-more">课程中心 →</a></div>
  <div class="tutorial-grid" id="tutorialGrid"></div>

  <div class="sec-header"><span class="sh-icon">🛠️</span><h2>新手必备装备</h2><a href="pages/academy/library.html" class="sh-more">装备库 →</a></div>
  <div class="gear-section"><div class="gear-grid" id="gearGrid"></div></div>

  <div class="sec-header"><span class="sh-icon">🎓</span><h2>优秀学员作品展</h2><a href="pages/academy/ranking.html" class="sh-more">排行榜 →</a></div>
  <div class="student-showcase" id="studentShow"></div>

  <div class="sec-header"><span class="sh-icon">🏅</span><h2>证书认证</h2></div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px;padding:0 30px 20px">
    <a href="pages/academy/cert.html" class="gcard" style="text-align:center"><span class="gi">🥇</span><div class="gn">初级Coser认证</div><div class="gd">完成6门基础课程+1次实战考核</div></a>
    <a href="pages/academy/cert.html" class="gcard" style="text-align:center"><span class="gi">🥈</span><div class="gn">中级Coser认证</div><div class="gd">完成12门进阶课程+3次作品评审</div></a>
    <a href="pages/academy/cert.html" class="gcard" style="text-align:center"><span class="gi">🥉</span><div class="gn">高级Coser认证</div><div class="gd">完成18门高级课程+社区贡献评审</div></a>
  </div>

  <div class="sec-header"><span class="sh-icon">❓</span><h2>新手常见问题</h2></div>
  <div class="faq-section" id="faqSection"></div>
</div>

<script>
!function(){
var tutorials=[{t:"Cosplay入门完全指南",d:"什么是Cosplay？如何选择第一个角色？从零开始系统了解Cosplay文化、圈内术语和基础流程。",l:"beginner",i:"📖",m:["📚 12课时","⏱️ 2小时","👥 3.2万人"]},
{t:"AI智能角色推荐与选择",d:"根据你的体型、肤色、预算和喜好，AI推荐最适合新手的入门角色。匹配率高达92%，降低翻车风险。",l:"beginner",i:"🎯",m:["📚 6课时","⏱️ 1小时","👥 4.8万人"]},
{t:"Cosplay化妆基础入门",d:"底妆、眼妆、修容、唇妆四大板块。包含原神/星穹铁道等热门角色的妆容分解教程。",l:"beginner",i:"💄",m:["📚 15课时","⏱️ 3小时","👥 6.1万人"]},
{t:"Cos服装选购与尺寸指南",d:"如何测量身体尺寸？各平台服装质量对比、性价比分析。淘宝/拼多多/定制工作室选购技巧。",l:"beginner",i:"👘",m:["📚 8课时","⏱️ 1.5小时","👥 5.4万人"]},
{t:"Cosplay摄影与后期处理",d:"手机也能出大片！构图技巧、光线运用、LR+PS后期调色修图全流程。",l:"intermediate",i:"📷",m:["📚 20课时","⏱️ 4小时","👥 3.8万人"]},
{t:"道具制作与3D打印入门",d:"EVA泡沫板、热塑材料、3D打印三种主流技术详解。包含雷电将军薙刀等实战案例。",l:"advanced",i:"🔧",m:["📚 18课时","⏱️ 4小时","👥 2.1万人"]},
{t:"假发造型基础与进阶",d:"从基础梳理到复杂造型，真人假发与化纤假发的区别及护理技巧。",l:"intermediate",i:"💇",m:["📚 10课时","⏱️ 2小时","👥 3.5万人"]},
{t:"特效化妆与伤妆制作",d:"液态乳胶、明胶、硅胶——三种材料在特效化妆中的应用。科幻/奇幻/伤妆全覆盖。",l:"advanced",i:"🎭",m:["📚 14课时","⏱️ 3小时","👥 1.8万人"]}];

document.getElementById('tutorialGrid').innerHTML=tutorials.map(function(t,i){return'<a href="pages/academy/courses.html" class="tcard"><span class="diff '+t.l+'">'+(t.l==='beginner'?'入门':t.l==='intermediate'?'进阶':'高级')+'</span><span class="ti">'+t.i+'</span><div class="tt">'+t.t+'</div><div class="td">'+t.d+'</div><div class="tm">'+t.m.map(function(x){return'<span>'+x+'</span>'}).join('')+'</div></a>'}).join('');

var gear=[{i:"💄",n:"化妆入门套装",d:"新手友好，包含底妆、眼影、修容等基础产品，附赠教程视频",t:["粉底液","眼影盘","修容棒","定妆喷雾"]},
{i:"📸",n:"摄影入门设备",d:"手机也能拍！环形补光灯+手机三脚架+反光板，总预算300元以内",t:["补光灯","三脚架","反光板"]},
{i:"🧵",n:"服装护理工具",d:"假发护理液、服装熨烫、防皱喷雾——保持服装最佳状态的必备品",t:["假发护理","蒸汽熨斗","防皱喷雾"]},
{i:"🎒",n:"漫展出征包",d:"化妆包、针线包、备用丝袜、创可贴、充电宝——漫展现场应急必备",t:["应急包","针线包","充电宝"]}];

document.getElementById('gearGrid').innerHTML=gear.map(function(g){return'<a href="pages/academy/library.html" class="gcard"><span class="gi">'+g.i+'</span><div class="gn">'+g.n+'</div><div class="gd">'+g.d+'</div><div class="gtags">'+g.t.map(function(x){return'<span class="gtag">'+x+'</span>'}).join('')+'</div></a>'}).join('');

var students=[{n:"小樱Cos",r:"入门3个月",s:"从零到出片！",bg:"linear-gradient(135deg,#ff4081,#ff80ab)",i:"🌸"},
{n:"摄影新手小王",r:"入门1个月",s:"手机也能拍大片",bg:"linear-gradient(135deg,#37474f,#607d8b)",i:"📷"},
{n:"道具学徒阿强",r:"入门6个月",s:"第一把EVA剑",bg:"linear-gradient(135deg,#ff6f00,#ffa000)",i:"🗡️"},
{n:"化妆爱好者",r:"入门2个月",s:"还原雷电将军妆容",bg:"linear-gradient(135deg,#4a148c,#7b1fa2)",i:"💄"},
{n:"cos新手小美",r:"入门4个月",s:"完成阿尼亚cos",bg:"linear-gradient(135deg,#1b5e20,#43a047)",i:"🥜"}];

document.getElementById('studentShow').innerHTML=students.map(function(s){return'<a href="pages/academy/ranking.html" class="scard"><div class="sc-thumb" style="background:'+s.bg+'">'+s.i+'</div><div class="sc-info"><div class="sc-name">'+s.n+'</div><div class="sc-meta">'+s.r+' · '+s.s+'</div></div></a>'}).join('');

var live=[{t:"雷电将军cos妆容教学",d:"今晚20:00",bg:"#ef4444",i:"💄",n:"妆娘小雨"},
{t:"EVA道具刀制作直播",d:"明晚19:30",bg:"#f97316",i:"🔧",n:"道具大师K"},
{t:"摄影布光实战",d:"周三14:00",bg:"#6366f1",i:"📸",n:"摄影师A"},
{t:"假发造型入门",d:"周四20:00",bg:"#ec4899",i:"💇",n:"发型师CC"},
{t:"3D打印道具全流程",d:"周六15:00",bg:"#8b5cf6",i:"🖨️",n:"3D打印工坊"}];

document.getElementById('liveStrip').innerHTML=live.map(function(l){return'<a href="pages/academy/live-class.html" class="lc-item"><span class="lci">'+l.i+'</span><div class="lct">'+l.t+'</div><div class="lcm">'+l.d+'</div><span class="lcbadge" style="background:'+l.bg+';color:#fff">'+l.n+'</span></a>'}).join('');

var faqs=[{q:"Cosplay需要花很多钱吗？",a:"不一定！入门级Cosplay预算可以从300元起步。选择简单角色、购买二手服装、自己动手做道具都是省钱的好方法。龙奕学院商城专门有新手专区，提供高性价比Cos服装。"},
{q:"完全0基础，第一个角色选什么？",a:"建议选择服装结构简单、妆容要求不高的角色。推荐：阿尼亚（间谍过家家）、旅行者（原神）、现代风格角色。使用龙奕学院AI推荐功能匹配最佳角色。"},
{q:"男生可以Cos女性角色吗？",a:"当然可以！跨性别Cosplay（Crossplay）是Cosplay文化中非常普遍和受尊重的形式。关键在于妆容技巧和服装合身度。学院有专门的Crossplay化妆教程。"},
{q:"Cos服装在哪里买最靠谱？",a:"首选龙奕学院自营商城（品质保证+退换无忧），其次是淘宝认证的Cos服装店，定制服装建议选口碑好的工作室。商城所有商品都有Coser真实评价和实拍图。"},
{q:"学到什么程度可以参加比赛？",a:"没有硬性门槛！学院每月举办新人挑战赛，专门为零基础学员设计。完成6门基础课程后，就可以参加初级认证考核。比赛更看重创意和进步，不只是技术。"}];

document.getElementById('faqSection').innerHTML=faqs.map(function(f,i){return'<div class="faq-item'+(i===0?' open':'')+'"><div class="faq-q" onclick="this.parentElement.classList.toggle(\'open\')">'+f.q+'<span class="arrow">▼</span></div><div class="faq-a">'+f.a+'</div></div>'}).join('');
}();
</script>

<script src="assets/nav.js"></script>
<script src="assets/theme-toggle.js"></script>
<script src="assets/dynamic-bg.js"></script>
<script src="assets/effects-runtime.js"></script>
</body>
</html>`;

// ============================================================
// 2. 祭典学院 (events.html) — 增强版
// ============================================================
const eventsHTML = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>祭典学院 | 龙奕学院 LongYi Academy</title>
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="assets/themes/academy/sunset-academy.css">
<link rel="stylesheet" href="assets/themes/dark-mode.css">
<link rel="stylesheet" href="assets/effects-layer.css">
<style>*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}body{overflow-x:overlay}
.page-wrap{position:relative;z-index:1;padding-top:72px;max-width:1340px;margin:0 auto;padding-bottom:50px}
.hero-section{position:relative;padding:56px 32px 32px;text-align:center;overflow:hidden}
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

.events-hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 30% 20%,rgba(249,115,22,.13),transparent 60%),radial-gradient(ellipse at 70% 80%,rgba(236,72,153,.1),transparent 60%);pointer-events:none}
.events-hero h1{background:linear-gradient(135deg,#f97316,#ec4899,#f59e0b);-webkit-background-clip:text;-webkit-text-fill-color:transparent}

.event-countdown{display:flex;justify-content:center;gap:20px;margin-top:20px;position:relative;z-index:1;flex-wrap:wrap}
.cd-item{text-align:center;background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:16px 24px;min-width:80px}
.cd-num{font-size:2.2rem;font-weight:900;color:var(--accent);display:block;line-height:1}
.cd-label{font-size:.72rem;opacity:.6;margin-top:4px}

.feat-banner{position:relative;margin:0 30px 20px;border-radius:18px;overflow:hidden;height:260px;cursor:pointer}
.feat-banner .fb-overlay{position:absolute;bottom:0;left:0;right:0;padding:36px;background:linear-gradient(transparent,rgba(0,0,0,.88))}
.feat-banner .fb-tag{display:inline-block;background:#f97316;color:#fff;padding:4px 14px;border-radius:12px;font-size:.72rem;font-weight:700;margin-bottom:8px}
.feat-banner .fb-title{font-size:1.7rem;font-weight:900;color:#fff;margin-bottom:4px}
.feat-banner .fb-desc{font-size:.85rem;color:rgba(255,255,255,.65);max-width:500px;line-height:1.5}

.quick-row{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;padding:0 30px 20px}
.qcard{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:20px;text-align:center;transition:all .3s;cursor:pointer;text-decoration:none;color:inherit}
.qcard:hover{transform:translateY(-4px);box-shadow:0 12px 36px rgba(249,115,22,.15);border-color:var(--accent)}
.qcard .qi{font-size:2.2rem;display:block;margin-bottom:6px}
.qcard .qt{font-weight:700;font-size:.9rem;margin-bottom:2px}
.qcard .qd{font-size:.74rem;opacity:.6}

.ev-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:18px;padding:0 30px 20px}
.ev-card{background:var(--bg-card);border-radius:18px;overflow:hidden;border:1px solid var(--border);transition:all .35s;cursor:pointer;text-decoration:none;color:inherit;position:relative}
.ev-card:hover{transform:translateY(-6px);box-shadow:0 16px 48px rgba(249,115,22,.2)}
.ev-card .evh{height:160px;display:flex;align-items:center;justify-content:center;font-size:4rem;position:relative}
.ev-card .ev-date-badge{position:absolute;top:12px;right:12px;background:rgba(0,0,0,.7);color:#fff;padding:4px 12px;border-radius:10px;font-size:.7rem;font-weight:700;backdrop-filter:blur(6px)}
.ev-card .ev-status{position:absolute;top:12px;left:12px;padding:4px 12px;border-radius:10px;font-size:.7rem;font-weight:700;color:#fff}
.ev-status.upcoming{background:#f59e0b}.ev-status.ongoing{background:#22c55e}.ev-status.past{background:#6b7280}
.ev-card .ev-body{padding:18px}
.ev-card .ev-title{font-weight:700;font-size:1rem;margin-bottom:6px}
.ev-card .ev-desc{font-size:.82rem;opacity:.6;line-height:1.5;margin-bottom:10px}
.ev-card .ev-footer{display:flex;justify-content:space-between;font-size:.78rem;opacity:.5}

.activity-feed{padding:0 30px 20px;max-width:700px;margin:0 auto}
.act-item{display:flex;gap:12px;padding:14px;margin-bottom:8px;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;transition:all .25s}
.act-item:hover{border-color:rgba(255,255,255,.1)}
.act-item .act-av{width:42px;height:42px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.1rem;flex-shrink:0}
.act-item .act-body{flex:1}.act-body .at{font-size:.85rem}.act-body .at strong{color:var(--accent)}.act-body .atm{font-size:.7rem;opacity:.4;margin-top:2px}

.cta-section{margin:0 30px 20px;padding:26px;border-radius:16px;background:linear-gradient(135deg,rgba(249,115,22,.1),rgba(236,72,153,.08));border:1px solid rgba(249,115,22,.2);display:flex;align-items:center;gap:18px;cursor:pointer;transition:all .3s}
.cta-section:hover{background:linear-gradient(135deg,rgba(249,115,22,.18),rgba(236,72,153,.12))}
.cta-section .cta-icon{font-size:2.5rem;flex-shrink:0}
.cta-section .cta-text{flex:1}.cta-section .cta-title{font-weight:700;font-size:1rem;margin-bottom:2px}
.cta-section .cta-desc{font-size:.78rem;opacity:.6}

@media(max-width:768px){
  .quick-row{grid-template-columns:repeat(2,1fr)}
  .ev-grid,.activity-feed{padding:0 14px 14px}
  .feat-banner{height:200px;margin:0 14px 16px}
  .hero-stats{gap:16px}.hero-section{padding:40px 16px 24px}
  .event-countdown{flex-wrap:wrap;gap:10px}
}
</style>
</head>
<body>
<div id="nav-placeholder"></div>
<div class="page-wrap">
  <div class="hero-section events-hero">
    <h1>祭典学院</h1>
    <p class="hero-sub">线上元宇宙活动 + 线下真实聚会 — Cos大赛 · 漫展 · 虚拟演唱会 · 学园祭 · 年度评选。让每一次活动都成为难忘的回忆。</p>
    <div class="hero-stats">
      <div class="hero-stat"><span class="hs-val">128</span><span class="hs-lbl">年度活动</span></div>
      <div class="hero-stat"><span class="hs-val">56.8万</span><span class="hs-lbl">累计参与</span></div>
      <div class="hero-stat"><span class="hs-val">¥500万</span><span class="hs-lbl">总奖金池</span></div>
      <div class="hero-stat"><span class="hs-val">98%</span><span class="hs-lbl">满意度</span></div>
    </div>
    <div class="event-countdown">
      <div class="cd-item"><span class="cd-num">15</span><span class="cd-label">天后</span></div>
      <div class="cd-item"><span class="cd-num">夏季Cos大赛</span><span class="cd-label">¥50万奖金</span></div>
      <div class="cd-item"><span class="cd-num">32</span><span class="cd-label">天后</span></div>
      <div class="cd-item"><span class="cd-num">龙奕学园祭</span><span class="cd-label">年度盛典</span></div>
    </div>
  </div>

  <div class="feat-banner" onclick="location.href='pages/events/contest.html'" style="background:linear-gradient(135deg,#7c2d12,#9a3412,#c2410c)">
    <div class="fb-overlay">
      <span class="fb-tag">🏆 年度重磅</span>
      <div class="fb-title">2024夏季Cosplay大赛 · 报名火热进行中</div>
      <div class="fb-desc">全国最大Cosplay线上+线下联动赛事，总奖金池50万元。Cos走秀、道具制作、数字人Cos三大赛道，等你来战！</div>
    </div>
  </div>

  <div class="quick-row">
    <a href="pages/events/contest.html" class="qcard"><span class="qi">🏆</span><div class="qt">Cos大赛</div><div class="qd">年度竞技舞台</div></a>
    <a href="pages/events/calendar.html" class="qcard"><span class="qi">📅</span><div class="qt">活动日历</div><div class="qd">不错过每一场</div></a>
    <a href="pages/events/con.html" class="qcard"><span class="qi">🌐</span><div class="qt">虚拟漫展</div><div class="qd">元宇宙逛展</div></a>
    <a href="pages/events/festival.html" class="qcard"><span class="qi">🎆</span><div class="qt">学园祭</div><div class="qd">夏日盛典</div></a>
  </div>

  <div class="cta-section" onclick="location.href='pages/events/live-show.html'">
    <span class="cta-icon">🎤</span>
    <div class="cta-text"><div class="cta-title">虚拟演唱会 · 星海之约 进行中！</div><div class="cta-desc">与知名Vtuber和虚拟偶像同台，AI实时驱动、AR特效渲染、360°自由视角沉浸式观看。</div></div>
    <span style="font-size:1.5rem">→</span>
  </div>

  <div class="sec-header"><span class="sh-icon">🔥</span><h2>即将举行的活动</h2><a href="pages/events/calendar.html" class="sh-more">活动日历 →</a></div>
  <div class="ev-grid" id="upcomingGrid"></div>

  <div class="sec-header"><span class="sh-icon">⏳</span><h2>进行中的活动</h2></div>
  <div class="ev-grid" id="ongoingGrid"></div>

  <div class="sec-header"><span class="sh-icon">📡</span><h2>最新参与动态</h2></div>
  <div class="activity-feed" id="actFeed"></div>

  <div class="sec-header"><span class="sh-icon">🏅</span><h2>往期精彩回顾</h2><a href="pages/events/award.html" class="sh-more">年度评选 →</a></div>
  <div class="ev-grid" id="pastGrid"></div>
</div>

<script>
var events=[
{t:"2024夏季Cosplay大赛",d:"全国最大Cosplay线上+线下联动赛事，总奖金池50万元。Cos走秀、道具制作、数字人Cos三大赛道。",s:"upcoming",dt:"2024.07.15 - 08.30",bg:"linear-gradient(135deg,#f97316,#ec4899)",i:"🏆",m:"2,341人已报名"},
{t:"龙奕学园祭 · 夏日盛典",d:"元宇宙虚拟学园祭！在龙墟世界中畅游摊贩、游戏、表演、烟花大会。无需出门就能体验最纯正的学园祭。",s:"upcoming",dt:"2024.08.01 - 08.03",bg:"linear-gradient(135deg,#8b5cf6,#ec4899)",i:"🎆",m:"5,892人预约"},
{t:"Cos道具制作研习营",d:"线下+线上混合工作坊，由资深道具师教授锻造、3D打印、涂装全流程。限额200人，先到先得。",s:"upcoming",dt:"2024.07.20 - 07.22",bg:"linear-gradient(135deg,#22c55e,#14b8a6)",i:"🔧",m:"168人已报名"},
{t:"声优见面会 · 龙奕专场",d:"人气声优线上见面会，AI实时翻译，全球粉丝同步参与Q&A互动和签名环节。",s:"upcoming",dt:"2024.08.10",bg:"linear-gradient(135deg,#f59e0b,#ef4444)",i:"🎙️",m:"3,456人预约"},
{t:"虚拟演唱会 · 星海之约",d:"与知名Vtuber和虚拟偶像同台！AI实时驱动、AR特效渲染、360°自由视角沉浸式观看。",s:"ongoing",dt:"2024.06.20 - 07.05",bg:"linear-gradient(135deg,#06b6d4,#6366f1)",i:"🎤",m:"演出中"},
{t:"线上ACG艺术展",d:"元宇宙虚拟画廊展示原创插画、同人漫画、3D建模作品。观众可在虚拟空间中漫步观赏。",s:"ongoing",dt:"2024.06.15 - 07.15",bg:"linear-gradient(135deg,#a78bfa,#ec4899)",i:"🎨",m:"展出中"},
{t:"2024元旦烟花大会",d:"元宇宙跨年烟花大会，数千架数字烟花同步绽放，3D环绕声景，万人同时在线狂欢。",s:"past",dt:"2024.01.01",bg:"linear-gradient(135deg,#1e1b4b,#312e81)",i:"🎇",m:"12万人参与"},
{t:"年度Cosplay大赏",d:"2023年度最佳Cos作品评选，专业评审团+全民投票。最佳还原、最佳创意、最佳数字人等多个奖项。",s:"past",dt:"2023.12.30",bg:"linear-gradient(135deg,#fbbf24,#d97706)",i:"🥇",m:"8万人投票"},
{t:"万圣节Cos狂欢夜",d:"元宇宙万圣节主题派对，鬼怪Cos大赛+恐怖密室逃脱+不给糖就捣蛋虚拟寻宝。",s:"past",dt:"2023.10.31",bg:"linear-gradient(135deg,#4a148c,#7b1fa2)",i:"🎃",m:"6.5万人参与"}
];

function renderGrid(id,status){
  var el=document.getElementById(id);
  if(!el)return;
  var list=events.filter(function(e){return e.s===status});
  el.innerHTML=list.map(function(e){return'<a href="pages/events/'+(e.s==='upcoming'?'contest':e.s==='ongoing'?'live-show':'award')+'.html" class="ev-card"><div class="evh" style="background:'+e.bg+'">'+e.i+'<span class="ev-date-badge">'+e.dt+'</span><span class="ev-status '+e.s+'">'+(e.s==='upcoming'?'即将开始':e.s==='ongoing'?'进行中':'已结束')+'</span></div><div class="ev-body"><div class="ev-title">'+e.t+'</div><div class="ev-desc">'+e.d+'</div><div class="ev-footer"><span>'+e.m+'</span><span style="color:var(--accent)">查看详情 →</span></div></div></a>'}).join('');
}
renderGrid('upcomingGrid','upcoming');
renderGrid('ongoingGrid','ongoing');
renderGrid('pastGrid','past');

var acts=[{u:"樱落Cos",a:"报名了 夏季Cos大赛",t:"刚刚",av:"🌸",bg:"linear-gradient(135deg,#ff4081,#ff80ab)"},
{u:"SwordArt_Cos",a:"加入了 虚拟演唱会",t:"2分钟前",av:"⚔️",bg:"linear-gradient(135deg,#7c4dff,#b388ff)"},
{u:"星穹铁道Cos社",a:"发布了 学园祭摊贩申请",t:"5分钟前",av:"💎",bg:"linear-gradient(135deg,#00e5ff,#80deea)"},
{u:"摄影师A",a:"报名了 cos道具研习营",t:"8分钟前",av:"📷",bg:"linear-gradient(135deg,#37474f,#607d8b)"},
{u:"小透明Coser",a:"预约了 声优见面会",t:"12分钟前",av:"🐱",bg:"linear-gradient(135deg,#69f0ae,#b9f6ca)"}];

document.getElementById('actFeed').innerHTML=acts.map(function(x){return'<div class="act-item"><div class="act-av" style="background:'+x.bg+'">'+x.av+'</div><div class="act-body"><div class="at"><strong>'+x.u+'</strong> '+x.a+'</div><div class="atm">'+x.t+'</div></div></div>'}).join('');
</script>

<script src="assets/nav.js"></script>
<script src="assets/theme-toggle.js"></script>
<script src="assets/dynamic-bg.js"></script>
<script src="assets/effects-runtime.js"></script>
</body>
</html>`;

// ============================================================
// 3. 百科书院 (wiki.html) — 增强版
// ============================================================
const wikiHTML = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>百科书院 | 龙奕学院 LongYi Academy</title>
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="assets/themes/academy/lavender-academy.css">
<link rel="stylesheet" href="assets/themes/dark-mode.css">
<link rel="stylesheet" href="assets/effects-layer.css">
<style>*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}body{overflow-x:overlay}
.page-wrap{position:relative;z-index:1;padding-top:72px;max-width:1340px;margin:0 auto;padding-bottom:50px}
.hero-section{position:relative;padding:56px 32px 32px;text-align:center;overflow:hidden}
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

.wiki-hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 30%,rgba(167,139,250,.12),transparent 70%),radial-gradient(ellipse at 30% 70%,rgba(99,102,241,.08),transparent 60%);pointer-events:none}
.wiki-hero h1{background:linear-gradient(135deg,#a78bfa,#7c3aed,#6366f1);-webkit-background-clip:text;-webkit-text-fill-color:transparent}

.wiki-search{max-width:500px;margin:20px auto;display:flex;gap:8px;position:relative;z-index:1}
.wiki-search input{flex:1;padding:14px 20px;border:2px solid var(--border);border-radius:28px;background:var(--bg-card);color:var(--text);font-size:.95rem;outline:none;transition:all .3s}
.wiki-search input:focus{border-color:var(--accent);box-shadow:0 0 24px rgba(167,139,250,.25)}
.wiki-search button{padding:14px 24px;background:linear-gradient(135deg,#a78bfa,#7c3aed);border:none;border-radius:28px;color:#fff;font-weight:700;cursor:pointer;font-size:.95rem;transition:all .3s}
.wiki-search button:hover{transform:scale(1.05);box-shadow:0 6px 24px rgba(167,139,250,.4)}

.cat-row{display:grid;grid-template-columns:repeat(7,1fr);gap:12px;padding:0 30px 20px}
.cat-card{background:var(--bg-card);border-radius:16px;padding:20px 12px;text-align:center;border:1px solid var(--border);transition:all .3s;cursor:pointer;text-decoration:none;color:inherit}
.cat-card:hover{transform:translateY(-4px);box-shadow:0 10px 32px rgba(167,139,250,.2);border-color:var(--accent)}
.cat-card .cci{font-size:2rem;display:block;margin-bottom:6px}
.cat-card .ccn{font-weight:700;font-size:.85rem}

.feat-banner{position:relative;margin:0 30px 20px;border-radius:18px;overflow:hidden;height:240px;cursor:pointer;background:linear-gradient(135deg,#2e1065,#3b0764,#4c1d95)}
.feat-banner .fb-overlay{position:absolute;bottom:0;left:0;right:0;padding:36px;background:linear-gradient(transparent,rgba(0,0,0,.88))}
.feat-banner .fb-tag{display:inline-block;background:#a78bfa;color:#fff;padding:4px 14px;border-radius:12px;font-size:.72rem;font-weight:700;margin-bottom:8px}
.feat-banner .fb-title{font-size:1.6rem;font-weight:900;color:#fff;margin-bottom:4px}
.feat-banner .fb-desc{font-size:.82rem;color:rgba(255,255,255,.6);max-width:500px;line-height:1.5}

.wiki-article-list{padding:0 30px 20px;display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
.wiki-article{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:20px;transition:all .3s;cursor:pointer;text-decoration:none;color:inherit;display:flex;gap:16px}
.wiki-article:hover{transform:translateX(4px);border-color:var(--accent);box-shadow:0 6px 24px rgba(167,139,250,.15)}
.wiki-article .wa-thumb{width:80px;height:80px;border-radius:12px;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:2.5rem}
.wiki-article .wa-info{flex:1;min-width:0}
.wiki-article .wa-title{font-weight:700;font-size:.95rem;margin-bottom:4px}
.wiki-article .wa-desc{font-size:.78rem;opacity:.6;line-height:1.5;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.wiki-article .wa-meta{font-size:.72rem;opacity:.45;margin-top:8px}

.timeline-strip{display:flex;gap:0;overflow-x:auto;padding:0 30px 20px;scroll-snap-type:x mandatory}
.timeline-strip::-webkit-scrollbar{height:4px}.timeline-strip::-webkit-scrollbar-thumb{background:var(--accent);border-radius:4px}
.tl-item{flex:0 0 170px;background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:18px;text-align:center;transition:all .3s;cursor:pointer;text-decoration:none;color:inherit;margin-right:14px;scroll-snap-align:start}
.tl-item:hover{transform:translateY(-4px);box-shadow:0 10px 30px rgba(167,139,250,.2);border-color:var(--accent)}
.tl-year{font-size:1.4rem;font-weight:900;color:var(--accent)}
.tl-title{font-size:.82rem;font-weight:600;margin:8px 0}
.tl-desc{font-size:.72rem;opacity:.5}

.trend-section{padding:0 30px 20px;display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.trend-card{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:20px;transition:all .3s;cursor:pointer;text-decoration:none;color:inherit}
.trend-card:hover{transform:translateY(-3px);box-shadow:0 10px 28px rgba(167,139,250,.12);border-color:var(--accent)}
.trend-card .tri{font-size:2rem;display:block;margin-bottom:8px}
.trend-card .trn{font-weight:700;font-size:.92rem;margin-bottom:4px}
.trend-card .trd{font-size:.76rem;opacity:.6;line-height:1.4}

@media(max-width:768px){
  .cat-row{grid-template-columns:repeat(4,1fr)}
  .wiki-article-list,.trend-section{grid-template-columns:1fr}
  .feat-banner{height:200px;margin:0 14px 16px}
  .hero-stats{gap:16px}.hero-section{padding:40px 16px 24px}
}
</style>
</head>
<body>
<div id="nav-placeholder"></div>
<div class="page-wrap">
  <div class="hero-section wiki-hero">
    <h1>百科书院</h1>
    <p class="hero-sub">二次元知识中枢 — Cos维基、动画编年史、角色图鉴、声优资料、术语词典。一站式知识探索平台。</p>
    <div class="hero-stats">
      <div class="hero-stat"><span class="hs-val">28,647</span><span class="hs-lbl">百科条目</span></div>
      <div class="hero-stat"><span class="hs-val">12,480</span><span class="hs-lbl">角色图鉴</span></div>
      <div class="hero-stat"><span class="hs-val">5,230</span><span class="hs-lbl">声优资料</span></div>
      <div class="hero-stat"><span class="hs-val">189万</span><span class="hs-lbl">月访问量</span></div>
    </div>
    <div class="wiki-search"><input type="text" id="wikiQ" placeholder="搜索百科内容... 角色/声优/动画/术语"><button onclick="searchWiki()">🔍 搜索</button></div>
  </div>

  <div class="cat-row">
    <a href="pages/wiki/index.html" class="cat-card"><span class="cci">📚</span><span class="ccn">Cos维基</span></a>
    <a href="pages/wiki/timeline.html" class="cat-card"><span class="cci">📅</span><span class="ccn">编年史</span></a>
    <a href="pages/wiki/characters.html" class="cat-card"><span class="cci">🎭</span><span class="ccn">角色图鉴</span></a>
    <a href="pages/wiki/studios.html" class="cat-card"><span class="cci">🏢</span><span class="ccn">动画公司</span></a>
    <a href="pages/wiki/seiyuu.html" class="cat-card"><span class="cci">🎙️</span><span class="ccn">声优图鉴</span></a>
    <a href="pages/wiki/glossary.html" class="cat-card"><span class="cci">📝</span><span class="ccn">术语词典</span></a>
    <a href="pages/wiki/article.html" class="cat-card"><span class="cci">📄</span><span class="ccn">知识文章</span></a>
  </div>

  <div class="feat-banner" onclick="location.href='pages/wiki/article.html'">
    <div class="fb-overlay">
      <span class="fb-tag">⭐ 精选百科</span>
      <div class="fb-title">数字人Cosplay革命：AI如何改变Cos圈</div>
      <div class="fb-desc">深度解析AI生成、动作捕捉、实时渲染三大技术如何赋能Cosplay，让虚拟与现实完美融合。超过9000人阅读，4.8星好评。</div>
    </div>
  </div>

  <div class="sec-header"><span class="sh-icon">🔥</span><h2>热门百科文章</h2><a href="pages/wiki/article.html" class="sh-more">更多文章 →</a></div>
  <div class="wiki-article-list">
    <a href="pages/wiki/article.html" class="wiki-article">
      <div class="wa-thumb" style="background:linear-gradient(135deg,#7c3aed,#a78bfa)">🎭</div>
      <div class="wa-info"><div class="wa-title">Cosplay入门完全指南：从选角到出片</div><div class="wa-desc">覆盖角色选择、服装制作、道具打造、化妆技巧、摄影构图、后期修图的完整Cosplay流程指南。</div><div class="wa-meta">📖 12,847阅读 · ⭐ 4.9 · 2024.06.15更新</div></div>
    </a>
    <a href="pages/wiki/article.html" class="wiki-article">
      <div class="wa-thumb" style="background:linear-gradient(135deg,#6366f1,#22d3ee)">🌟</div>
      <div class="wa-info"><div class="wa-title">数字人Cosplay革命：AI如何改变Cos圈</div><div class="wa-desc">深度解析AI生成、动作捕捉、实时渲染三大技术如何赋能Cosplay，让虚拟与现实完美融合。</div><div class="wa-meta">📖 9,234阅读 · ⭐ 4.8 · 2024.06.10更新</div></div>
    </a>
    <a href="pages/wiki/article.html" class="wiki-article">
      <div class="wa-thumb" style="background:linear-gradient(135deg,#ec4899,#f97316)">⚔️</div>
      <div class="wa-info"><div class="wa-title">武器道具制作终极教程：从设计图到成品</div><div class="wa-desc">EVA发泡板、PVC管、3D打印——详细对比各种材料优劣，附完整制作流程和涂装技巧。</div><div class="wa-meta">📖 7,891阅读 · ⭐ 4.7 · 2024.05.28更新</div></div>
    </a>
    <a href="pages/wiki/article.html" class="wiki-article">
      <div class="wa-thumb" style="background:linear-gradient(135deg,#22c55e,#14b8a6)">📸</div>
      <div class="wa-info"><div class="wa-title">Cos摄影布光圣经：从单灯到多灯全攻略</div><div class="wa-desc">自然光VS棚拍、Rembrandt光、蝴蝶光、边缘光——手把手教你用光线塑造角色氛围。</div><div class="wa-meta">📖 6,543阅读 · ⭐ 4.6 · 2024.05.20更新</div></div>
    </a>
  </div>

  <div class="sec-header"><span class="sh-icon">📅</span><h2>动画编年史</h2><a href="pages/wiki/timeline.html" class="sh-more">完整编年史 →</a></div>
  <div class="timeline-strip">
    <a href="pages/wiki/timeline.html" class="tl-item"><div class="tl-year">1963</div><div class="tl-title">铁臂阿童木</div><div class="tl-desc">日本TV动画元年</div></a>
    <a href="pages/wiki/timeline.html" class="tl-item"><div class="tl-year">1979</div><div class="tl-title">机动战士高达</div><div class="tl-desc">真实系机器人开山</div></a>
    <a href="pages/wiki/timeline.html" class="tl-item"><div class="tl-year">1995</div><div class="tl-title">EVA</div><div class="tl-desc">颠覆性叙事革命</div></a>
    <a href="pages/wiki/timeline.html" class="tl-item"><div class="tl-year">1998</div><div class="tl-title">星际牛仔</div><div class="tl-desc">太空爵士诗篇</div></a>
    <a href="pages/wiki/timeline.html" class="tl-item"><div class="tl-year">2006</div><div class="tl-title">凉宫春日</div><div class="tl-desc">轻改动画浪潮</div></a>
    <a href="pages/wiki/timeline.html" class="tl-item"><div class="tl-year">2011</div><div class="tl-title">魔法少女小圆</div><div class="tl-desc">颠覆魔法少女</div></a>
    <a href="pages/wiki/timeline.html" class="tl-item"><div class="tl-year">2016</div><div class="tl-title">你的名字。</div><div class="tl-desc">新海诚现象级</div></a>
    <a href="pages/wiki/timeline.html" class="tl-item"><div class="tl-year">2020</div><div class="tl-title">鬼灭之刃</div><div class="tl-desc">剧场版历史纪录</div></a>
    <a href="pages/wiki/timeline.html" class="tl-item" style="background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center">
      <div><span style="font-size:2rem">→</span><div style="font-weight:700;font-size:.82rem">查看完整编年史</div></div>
    </a>
  </div>

  <div class="sec-header"><span class="sh-icon">🎙️</span><h2>本周热门声优</h2><a href="pages/wiki/seiyuu.html" class="sh-more">声优图鉴 →</a></div>
  <div style="padding:0 30px 20px;display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px">
    <a href="pages/wiki/seiyuu.html" class="cat-card"><span class="cci">🌸</span><span class="ccn">花泽香菜</span><div style="font-size:.7rem;opacity:.5;margin-top:4px">五更琉璃 · 千石抚子</div></a>
    <a href="pages/wiki/seiyuu.html" class="cat-card"><span class="cci">🎭</span><span class="ccn">松冈祯丞</span><div style="font-size:.7rem;opacity:.5;margin-top:4px">桐谷和人 · 培提尔其乌斯</div></a>
    <a href="pages/wiki/seiyuu.html" class="cat-card"><span class="cci">💎</span><span class="ccn">钉宫理惠</span><div style="font-size:.7rem;opacity:.5;margin-top:4px">夏娜 · 露易丝 · 神乐</div></a>
    <a href="pages/wiki/seiyuu.html" class="cat-card"><span class="cci">🌟</span><span class="ccn">宫野真守</span><div style="font-size:.7rem;opacity:.5;margin-top:4px">夜神月 · 冈部伦太郎</div></a>
    <a href="pages/wiki/seiyuu.html" class="cat-card"><span class="cci">🎤</span><span class="ccn">泽城美雪</span><div style="font-size:.7rem;opacity:.5;margin-top:4px">赛尔提 · 镰池和马</div></a>
  </div>

  <div class="sec-header"><span class="sh-icon">📈</span><h2>知识探索</h2></div>
  <div class="trend-section">
    <a href="pages/wiki/glossary.html" class="trend-card"><span class="tri">📝</span><div class="trn">术语词典</div><div class="trd">Cosplay圈常用术语、黑话、缩写大全。从「出c」到「场照」，不再一脸茫然。</div></a>
    <a href="pages/wiki/characters.html" class="trend-card"><span class="tri">🎭</span><div class="trn">角色图鉴</div><div class="trd">收录12,000+ACG角色详细信息，支持按作品/属性/人气多维度检索。</div></a>
    <a href="pages/wiki/studios.html" class="trend-card"><span class="tri">🏢</span><div class="trn">动画公司档案</div><div class="trd">京都动画、WIT STUDIO、MAPPA、ufotable...深度了解你喜爱的动画背后的创作者。</div></a>
  </div>
</div>

<script>
function searchWiki(){var q=document.getElementById('wikiQ').value.trim();if(!q)return;alert('正在搜索百科：「'+q+'」...\\n\\n(模拟结果)\\n• Cosplay入门指南\\n• '+q+'相关角色图鉴\\n• '+q+'术语解析')}
</script>

<script src="assets/nav.js"></script>
<script src="assets/theme-toggle.js"></script>
<script src="assets/dynamic-bg.js"></script>
<script src="assets/effects-runtime.js"></script>
</body>
</html>`;

// ============================================================
// Write all files
// ============================================================
const files = [
  { path: path.join(SITE, 'academy.html'), content: academyHTML, name: '研修学院' },
  { path: path.join(SITE, 'events.html'), content: eventsHTML, name: '祭典学院' },
  { path: path.join(SITE, 'wiki.html'), content: wikiHTML, name: '百科书院' },
];

files.forEach(f => {
  fs.writeFileSync(f.path, f.content, 'utf8');
  console.log('OK: ' + f.name + ' (' + f.path + ')');
});

console.log('\\nDone! Generated 3 enriched academy homepages.');

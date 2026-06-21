// ========== 龙奕学院 Academy Enrichment Part 3: academy, events, wiki ==========
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

// ===== 7. 研修学院 academy.html =====
function buildAcademy() {
  const css = `
.acd-hero{background:linear-gradient(180deg,rgba(255,215,64,.04),transparent)}
.acd-hero h1{background:linear-gradient(135deg,#f59e0b,#f97316,#ef4444);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.path-row{display:flex;justify-content:center;gap:10px;flex-wrap:wrap;margin-bottom:16px;position:relative;z-index:1}
.path-step{padding:14px 22px;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;text-align:center;transition:all .3s;cursor:pointer;min-width:120px}
.path-step:hover{border-color:var(--accent);transform:translateY(-2px)}
.path-step .ps-num{width:30px;height:30px;border-radius:50%;margin:0 auto 6px;background:linear-gradient(135deg,var(--accent),#f97316);color:#fff;font-weight:800;font-size:.82rem;display:flex;align-items:center;justify-content:center}
.path-step .ps-lbl{font-size:.82rem;font-weight:600}.path-step .ps-sub{font-size:.7rem;opacity:.5}
.path-arrow{display:flex;align-items:center;color:var(--accent);font-size:1.1rem;flex-shrink:0}
.tut-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:16px;padding:0 30px 30px}
.tut-card{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:24px;transition:all .3s;cursor:pointer;position:relative;overflow:hidden}
.tut-card:hover{transform:translateY(-4px);box-shadow:0 10px 32px rgba(0,0,0,.2);border-color:var(--accent)}
.tut-card .diff{position:absolute;top:14px;right:14px;padding:3px 10px;border-radius:6px;font-size:.66rem;font-weight:700}
.diff.beginner{background:rgba(105,240,174,.12);color:#69f0ae}
.diff.intermediate{background:rgba(255,215,64,.12);color:#ffd740}
.diff.advanced{background:rgba(255,64,129,.12);color:#ff4081}
.tut-card .ti{font-size:2.2rem;display:block;margin-bottom:10px}
.tut-card .tt{font-size:1.05rem;font-weight:700;margin-bottom:6px;padding-right:60px}
.tut-card .td{font-size:.82rem;opacity:.6;margin-bottom:12px;line-height:1.5}
.tut-card .tm{display:flex;gap:14px;font-size:.74rem;opacity:.4}
.gear-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;padding:0 30px 30px}
.gear-card{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:22px;transition:all .3s}
.gear-card:hover{border-color:var(--accent)}
.gear-card .gi{font-size:2rem;display:block;margin-bottom:8px}.gear-card h4{font-size:.98rem;margin-bottom:4px}.gear-card p{font-size:.78rem;opacity:.6;margin-bottom:10px;line-height:1.4}
.gi-tags{display:flex;gap:5px;flex-wrap:wrap}.gi-tags span{padding:3px 10px;border-radius:6px;font-size:.68rem;background:rgba(255,255,255,.05)}
.faq-wrap{padding:0 30px 30px;max-width:800px;margin:0 auto}
.faq-item{background:var(--bg-card);border:1px solid var(--border);border-radius:12px;margin-bottom:10px;overflow:hidden;transition:all .3s}
.faq-item:hover{border-color:rgba(255,255,255,.12)}
.faq-q{padding:16px 20px;display:flex;justify-content:space-between;align-items:center;cursor:pointer;font-weight:600;font-size:.9rem}
.faq-q .arrow{transition:transform .3s;opacity:.5}.faq-item.open .faq-q .arrow{transform:rotate(180deg)}
.faq-a{max-height:0;overflow:hidden;transition:max-height .4s ease;padding:0 20px;font-size:.82rem;opacity:.65;line-height:1.7}
.faq-item.open .faq-a{max-height:300px;padding-bottom:16px}
.progress-bar{height:8px;border-radius:4px;background:rgba(255,255,255,.06);overflow:hidden;margin-top:8px}
.progress-fill{height:100%;border-radius:4px;background:linear-gradient(90deg,var(--accent),#f97316);transition:width .6s ease}
@media(max-width:768px){.path-row{flex-direction:column;align-items:center}.path-arrow{transform:rotate(90deg)}.tut-grid{grid-template-columns:1fr}}`;

  return headTpl('研修学院', 'sky-academy.css', css) + `
  <div class="hero-section acd-hero"><h1>研修学院</h1><p class="hero-sub">从完全新手到熟练Coser，AI辅助系统化学习路径。7大能力维度、60+精品课程、导师一对一指导——你的成长，我们有谱。</p><div class="hero-stats"><div class="hero-stat"><span class="hs-val">60+</span><span class="hs-lbl">精品课程</span></div><div class="hero-stat"><span class="hs-val">8.2万</span><span class="hs-lbl">学员总数</span></div><div class="hero-stat"><span class="hs-val">98%</span><span class="hs-lbl">好评率</span></div><div class="hero-stat"><span class="hs-val">30天</span><span class="hs-lbl">退款保障</span></div></div>
    <div class="path-row">
      <div class="path-step"><div class="ps-num">1</div><div class="ps-lbl">了解Cosplay</div><div class="ps-sub">基础知识</div></div><div class="path-arrow">→</div>
      <div class="path-step"><div class="ps-num">2</div><div class="ps-lbl">选择角色</div><div class="ps-sub">AI辅助推荐</div></div><div class="path-arrow">→</div>
      <div class="path-step"><div class="ps-num">3</div><div class="ps-lbl">服装道具</div><div class="ps-sub">采购/制作</div></div><div class="path-arrow">→</div>
      <div class="path-step"><div class="ps-num">4</div><div class="ps-lbl">化妆造型</div><div class="ps-sub">技巧入门</div></div><div class="path-arrow">→</div>
      <div class="path-step"><div class="ps-num">5</div><div class="ps-lbl">拍摄后期</div><div class="ps-sub">出片全流程</div></div><div class="path-arrow">→</div>
      <div class="path-step"><div class="ps-num">6</div><div class="ps-lbl">发布分享</div><div class="ps-sub">社区互动</div></div>
    </div>
    <button class="btn btn-primary btn-lg" style="position:relative;z-index:1" onclick="alert('AI正在为你生成个性化学习路径...')">🤖 AI帮我规划学习路径</button>
  </div>
  <div class="sec-header"><span class="sh-icon">📚</span><h2>系统化教程</h2><a href="pages/academy/courses.html" class="sh-more">全部课程 →</a></div>
  <div class="tut-grid">
    <div class="tut-card" onclick="alert('打开：Cosplay入门完全指南')"><span class="diff beginner">入门</span><span class="ti">📖</span><div class="tt">Cosplay入门完全指南</div><div class="td">什么是Cosplay？如何选择第一个角色？从零开始系统了解Cosplay文化、圈内术语和基础流程。匹配率高达92%。</div><div class="tm"><span>📚 12课时</span><span>⏱️ 2小时</span><span>👥 3.2万人</span></div><div class="progress-bar"><div class="progress-fill" style="width:0%"></div></div></div>
    <div class="tut-card" onclick="alert('打开：AI智能角色推荐')"><span class="diff beginner">入门</span><span class="ti">🎯</span><div class="tt">AI智能角色推荐与选择</div><div class="td">根据体型、肤色、预算和喜好，AI推荐最适合新手的入门角色。降低翻车风险。</div><div class="tm"><span>📚 6课时</span><span>⏱️ 1小时</span><span>👥 4.8万人</span></div></div>
    <div class="tut-card" onclick="alert('打开：Cosplay化妆基础')"><span class="diff beginner">入门</span><span class="ti">💄</span><div class="tt">Cosplay化妆基础入门</div><div class="td">底妆、眼妆、修容、唇妆四大板块。包含原神/星穹铁道热门角色妆容分解教程。</div><div class="tm"><span>📚 15课时</span><span>⏱️ 3小时</span><span>👥 6.1万人</span></div></div>
    <div class="tut-card" onclick="alert('打开：Cos服装选购指南')"><span class="diff beginner">入门</span><span class="ti">👘</span><div class="tt">Cos服装选购与尺寸指南</div><div class="td">身体尺寸测量、各平台质量对比、性价比分析。淘宝/拼多多/定制工作室选购技巧大公开。</div><div class="tm"><span>📚 8课时</span><span>⏱️ 1.5小时</span><span>👥 5.4万人</span></div></div>
    <div class="tut-card" onclick="alert('打开：Cos摄影与后期')"><span class="diff intermediate">进阶</span><span class="ti">📷</span><div class="tt">Cosplay摄影与后期处理</div><div class="td">手机也能出大片！构图、光线、参数设置。LR+PS后期调色修图全流程。</div><div class="tm"><span>📚 20课时</span><span>⏱️ 4小时</span><span>👥 3.8万人</span></div></div>
    <div class="tut-card" onclick="alert('打开：道具制作与3D打印')"><span class="diff advanced">高级</span><span class="ti">🔧</span><div class="tt">道具制作与3D打印入门</div><div class="td">EVA泡沫板、热塑材料、3D打印——三种主流材料与技术详解。雷电将军薙刀等案例。</div><div class="tm"><span>📚 18课时</span><span>⏱️ 4小时</span><span>👥 2.1万人</span></div></div>
  </div>
  <div class="sec-header"><span class="sh-icon">🛠️</span><h2>新手必备装备推荐</h2></div>
  <div class="gear-grid">
    <div class="gear-card"><span class="gi">💄</span><h4>化妆入门套装</h4><p>新手友好，底妆+眼影+修容+定妆，附赠教程视频</p><div class="gi-tags"><span>粉底液</span><span>眼影盘</span><span>修容棒</span><span>定妆喷雾</span></div></div>
    <div class="gear-card"><span class="gi">📸</span><h4>摄影入门设备</h4><p>手机也能拍！环形补光灯+三脚架+反光板，总预算300元以内</p><div class="gi-tags"><span>补光灯</span><span>三脚架</span><span>反光板</span></div></div>
    <div class="gear-card"><span class="gi">🧵</span><h4>服装护理工具</h4><p>假发护理液+熨烫+防皱喷雾——保持最佳状态</p><div class="gi-tags"><span>假发护理</span><span>蒸汽熨斗</span><span>防皱喷雾</span></div></div>
    <div class="gear-card"><span class="gi">🎒</span><h4>漫展出征包</h4><p>化妆包+针线包+创可贴+充电宝，漫展现场应急必备</p><div class="gi-tags"><span>应急包</span><span>针线包</span><span>充电宝</span></div></div>
  </div>
  <div class="sec-header"><span class="sh-icon">❓</span><h2>新手常见问题</h2></div>
  <div class="faq-wrap">
    <div class="faq-item open"><div class="faq-q" onclick="this.parentElement.classList.toggle('open')">Cosplay需要花很多钱吗？<span class="arrow">▼</span></div><div class="faq-a">不一定！入门级预算可从300元起步。选择简单角色、买二手、自己做道具都是省钱方法。龙奕学院商城有新手专区，提供高性价比服装。很多知名Coser都是从低成本开始的。</div></div>
    <div class="faq-item"><div class="faq-q" onclick="this.parentElement.classList.toggle('open')">完全0基础，第一个角色选什么？<span class="arrow">▼</span></div><div class="faq-a">建议选服装简单、妆容要求不高的角色。推荐：阿尼亚（间谍过家家）—校服+假发；旅行者（原神）—服装不复杂；或用AI推荐功能，根据预算/体型/喜好匹配最佳角色。</div></div>
    <div class="faq-item"><div class="faq-q" onclick="this.parentElement.classList.toggle('open')">男生可以Cos女性角色吗？<span class="arrow">▼</span></div><div class="faq-a">当然可以！Crossplay是Cosplay文化中非常普遍和受尊重的形式。很多著名男Coser也常出女性角色。关键在于妆容技巧和服装合身度。有专门的Crossplay化妆教程。</div></div>
    <div class="faq-item"><div class="faq-q" onclick="this.parentElement.classList.toggle('open')">Cos服装在哪里买最靠谱？<span class="arrow">▼</span></div><div class="faq-a">首选龙奕学院自营商城（品质保证+退换无忧），其次是淘宝认证店。定制服装选口碑好的工作室。所有商品有Coser真实评价和实拍图。</div></div>
  </div>` + footTpl;
}

// ===== 8. 祭典学院 events.html =====
function buildEvents() {
  const css = `
.events-hero{background:radial-gradient(ellipse at 30% 20%,rgba(249,115,22,.12),transparent 60%),radial-gradient(ellipse at 70% 80%,rgba(236,72,153,.08),transparent 60%)}
.events-hero h1{background:linear-gradient(135deg,#f97316,#ec4899,#f59e0b);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.cd-row{display:flex;justify-content:center;gap:16px;flex-wrap:wrap;margin-top:14px;position:relative;z-index:1}
.cd-item{text-align:center;background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:14px 20px;min-width:72px}
.cd-item .cdn{font-size:2rem;font-weight:900;color:var(--accent);display:block;line-height:1}.cd-item .cdl{font-size:.68rem;opacity:.5;margin-top:2px}
.event-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px;padding:0 30px 20px}
.ev-card{background:var(--bg-card);border-radius:16px;overflow:hidden;border:1px solid var(--border);transition:all .35s;cursor:pointer;text-decoration:none;color:inherit}
.ev-card:hover{transform:translateY(-6px);box-shadow:0 16px 48px rgba(249,115,22,.15)}
.ev-card .eh{height:150px;position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center;font-size:3.5rem}
.ev-card .edb{position:absolute;top:10px;right:10px;background:rgba(0,0,0,.7);color:#fff;padding:3px 10px;border-radius:8px;font-size:.66rem;font-weight:700;backdrop-filter:blur(6px)}
.ev-card .est{position:absolute;top:10px;left:10px;padding:3px 10px;border-radius:8px;font-size:.66rem;font-weight:700;color:#fff}
.est.upcoming{background:#f59e0b}.est.ongoing{background:#22c55e}.est.past{background:#6b7280}
.ev-card .eb{padding:16px}.ev-card .ebt{font-weight:700;font-size:.92rem;margin-bottom:6px}.ev-card .ebd{font-size:.78rem;opacity:.6;line-height:1.5;margin-bottom:8px}.ev-card .ebf{display:flex;justify-content:space-between;font-size:.72rem;opacity:.4}
.cal-hint{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;padding:0 30px 20px;max-width:700px;margin:0 auto}
.cal-day{text-align:center;padding:10px 6px;border-radius:10px;font-size:.78rem;cursor:pointer;transition:all .2s;border:1px solid transparent}
.cal-day:hover{border-color:var(--accent)}.cal-day.has-event{background:rgba(249,115,22,.08);border-color:rgba(249,115,22,.2);font-weight:700;color:var(--accent)}
.cal-day.today{background:var(--accent);color:#fff;font-weight:700}
.cal-hdr{font-size:.7rem;opacity:.4;text-align:center;padding:6px}
@media(max-width:768px){.event-grid{grid-template-columns:1fr}.cal-hint{max-width:100%}}`;

  return headTpl('祭典学院', 'coral-academy.css', css) + `
  <div class="hero-section events-hero"><h1>祭典学院</h1><p class="hero-sub">线上元宇宙活动 + 线下真实聚会——Cos大赛、虚拟漫展、学园祭、演唱会、烟花大会，与千万同好共赴盛宴。</p><div class="cd-row"><div class="cd-item"><span class="cdn">15</span><span class="cdl">天后 · 夏季Cos大赛</span></div><div class="cd-item"><span class="cdn">32</span><span class="cdl">天后 · 龙奕学园祭</span></div><div class="cd-item"><span class="cdn">58</span><span class="cdl">天后 · 夏日祭</span></div></div></div>
  <div class="sec-header"><span class="sh-icon">📅</span><h2>活动日历预览</h2><a href="pages/events/calendar.html" class="sh-more">完整日历 →</a></div>
  <div class="cal-hint" id="calWidget"></div>
  <div class="sec-header"><span class="sh-icon">🔥</span><h2>即将举行</h2><a href="pages/events/calendar.html" class="sh-more">全部 →</a></div>
  <div class="event-grid" id="upEvents"></div>
  <div class="sec-header"><span class="sh-icon">⏳</span><h2>进行中</h2></div>
  <div class="event-grid" id="onEvents"></div>
  <div class="sec-header"><span class="sh-icon">🏆</span><h2>往期精彩</h2></div>
  <div class="event-grid" id="pastEvents"></div>
<script>
!function(){var e=[{t:"2024夏季Cosplay大赛",d:"全国最大Cos线上+线下联动赛事，总奖金池50万元。三大赛道：Cos走秀、道具制作、数字人Cos。",s:"upcoming",dt:"2024.07.15 - 08.30",l:"pages/events/contest.html",c:"linear-gradient(135deg,#f97316,#ec4899)",i:"🏆",p:"2,341人报名"},{t:"龙奕学园祭 · 夏日盛典",d:"元宇宙虚拟学园祭！在虚空学院中畅游摊贩、游戏、表演、烟花大会。无需出门体验最纯正学园祭。",s:"upcoming",dt:"2024.08.01 - 08.03",l:"pages/events/festival.html",c:"linear-gradient(135deg,#8b5cf6,#ec4899)",i:"🎆",p:"5,892人预约"},{t:"虚拟演唱会 · 星海之约",d:"与知名Vtuber和虚拟偶像同台！AI实时驱动、AR特效渲染、360°自由视角沉浸观看。",s:"ongoing",dt:"2024.06.20 - 07.05",l:"pages/events/live-show.html",c:"linear-gradient(135deg,#06b6d4,#6366f1)",i:"🎤",p:"演出中"},{t:"Cos道具制作研习营",d:"线下+线上混合工作坊，资深道具师教授锻造、3D打印、涂装全流程。限额200人。",s:"upcoming",dt:"2024.07.20 - 07.22",l:"pages/events/meetup.html",c:"linear-gradient(135deg,#22c55e,#14b8a6)",i:"🔧",p:"168人报名"},{t:"线上ACG艺术展",d:"元宇宙虚拟画廊·展出原创插画、同人漫画、3D建模。观众可在虚拟空间漫步观赏。",s:"ongoing",dt:"2024.06.15 - 07.15",l:"pages/events/exhibition.html",c:"linear-gradient(135deg,#a78bfa,#ec4899)",i:"🎨",p:"展出中"},{t:"声优见面会 · 龙奕专场",d:"人气声优线上见面会，AI实时翻译，全球粉丝同步参与Q&A和签名环节。",s:"upcoming",dt:"2024.08.10",l:"pages/events/con.html",c:"linear-gradient(135deg,#f59e0b,#ef4444)",i:"🎙️",p:"3,456人预约"},{t:"2024元旦烟花大会",d:"元宇宙跨年烟花大会，数千架数字烟花同步绽放，3D环绕声景，万人同时在线狂欢。",s:"past",dt:"2024.01.01",l:"pages/events/fireworks.html",c:"linear-gradient(135deg,#1e1b4b,#312e81)",i:"🎇",p:"12万人参与"},{t:"年度Cosplay大赏",d:"最佳Cos作品评选，专业评审团+全民投票，涵盖最佳还原、最佳创意、最佳数字人等奖项。",s:"past",dt:"2023.12.30",l:"pages/events/award.html",c:"linear-gradient(135deg,#fbbf24,#d97706)",i:"🥇",p:"8万人投票"}];
["upEvents","onEvents","pastEvents"].forEach(function(id){var el=document.getElementById(id);if(!el)return;var list=e.filter(function(x){return id==="upEvents"?x.s==="upcoming":id==="onEvents"?x.s==="ongoing":x.s==="past"});el.innerHTML=list.map(function(x){return'<a href="'+x.l+'" class="ev-card"><div class="eh" style="background:'+x.c+'">'+x.i+'<span class="edb">'+x.dt+'</span><span class="est '+x.s+'">'+(x.s==="upcoming"?"即将开始":x.s==="ongoing"?"进行中":"已结束")+'</span></div><div class="eb"><div class="ebt">'+x.t+'</div><div class="ebd">'+x.d+'</div><div class="ebf"><span>'+x.p+'</span><span style="color:var(--accent)">详情 →</span></div></div></a>'}).join("")});
var cal=document.getElementById("calWidget"),now=new Date(),tDay=now.getDate(),tMon=now.getMonth(),daysInMon=new Date(now.getFullYear(),tMon+1,0).getDate(),hds=["日","一","二","三","四","五","六"],evDays=[5,12,15,20,22,28];cal.innerHTML=hds.map(function(d){return'<div class="cal-hdr">'+d+'</div>'}).join("")+Array.from({length:daysInMon},function(_,i){var dn=i+1,cls="cal-day";if(dn===tDay)cls+=" today";else if(evDays.indexOf(dn)>-1)cls+=" has-event";return'<div class="'+cls+'"'+(evDays.indexOf(dn)>-1?' onclick="alert(\\'此日有活动\\')"':'')+'>'+dn+'</div>'}).join("")}();
</script>` + footTpl;
}

// ===== 9. 百科书院 wiki.html =====
function buildWiki() {
  const css = `
.wiki-hero h1{background:linear-gradient(135deg,#a78bfa,#7c3aed,#6366f1);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.wiki-search{max-width:520px;margin:18px auto 0;display:flex;gap:8px;position:relative;z-index:1}
.wiki-search input{flex:1;padding:13px 18px;border:2px solid var(--border);border-radius:26px;background:var(--bg-card);color:var(--text);font-size:.9rem;outline:none;transition:all .3s}
.wiki-search input:focus{border-color:var(--accent);box-shadow:0 0 20px rgba(167,139,250,.2)}
.wiki-search button{padding:13px 24px;border-radius:26px;border:none;background:linear-gradient(135deg,#7c3aed,#6366f1);color:#fff;font-weight:700;cursor:pointer;transition:all .3s;font-size:.9rem}
.wiki-search button:hover{transform:scale(1.05);box-shadow:0 6px 24px rgba(124,58,237,.4)}
.cat-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:10px;padding:0 30px 20px}
.cat-card{background:var(--bg-card);border-radius:14px;padding:18px 10px;text-align:center;border:1px solid var(--border);transition:all .3s;cursor:pointer;text-decoration:none;color:inherit}
.cat-card:hover{transform:translateY(-4px);box-shadow:0 10px 28px rgba(167,139,250,.18);border-color:var(--accent)}
.cat-card .ci{font-size:1.8rem;display:block;margin-bottom:4px}.cat-card .cn{font-weight:700;font-size:.8rem}
.wiki-articles{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;padding:0 30px 20px}
.wa-card{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:18px;transition:all .3s;cursor:pointer;text-decoration:none;color:inherit;display:flex;gap:14px}
.wa-card:hover{transform:translateX(3px);border-color:var(--accent);box-shadow:0 6px 24px rgba(167,139,250,.12)}
.wa-card .wathumb{width:70px;height:70px;border-radius:10px;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:2rem}
.wa-card .wainfo{flex:1;min-width:0}.wa-card .watitle{font-weight:700;font-size:.88rem;margin-bottom:4px}.wa-card .wadesc{font-size:.74rem;opacity:.6;line-height:1.5;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}.wa-card .wameta{font-size:.68rem;opacity:.35;margin-top:6px}
.timeline-strip{display:flex;gap:0;overflow-x:auto;padding:0 30px 20px}.timeline-strip::-webkit-scrollbar{height:4px}.timeline-strip::-webkit-scrollbar-thumb{background:var(--accent);border-radius:4px}
.tl-item{flex:0 0 170px;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:16px;text-align:center;transition:all .3s;cursor:pointer;text-decoration:none;color:inherit;margin-right:12px}
.tl-item:hover{transform:translateY(-4px);box-shadow:0 10px 24px rgba(167,139,250,.18)}
.tl-item .tly{font-size:1.3rem;font-weight:900;color:var(--accent)}.tl-item .tlt{font-size:.78rem;font-weight:600;margin:6px 0}.tl-item .tld{font-size:.68rem;opacity:.5}
.feat-char{display:grid;grid-template-columns:repeat(6,1fr);gap:10px;padding:0 30px 20px}
.char-card{background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:14px 8px;text-align:center;transition:all .3s;cursor:pointer;text-decoration:none;color:inherit}
.char-card:hover{transform:translateY(-3px);box-shadow:0 8px 24px rgba(167,139,250,.12)}
.char-card .ch{font-size:2rem;display:block;margin-bottom:4px}.char-card .chn{font-weight:600;font-size:.78rem}
@media(max-width:768px){.cat-grid{grid-template-columns:repeat(4,1fr)}.wiki-articles{grid-template-columns:1fr}.feat-char{grid-template-columns:repeat(3,1fr)}}`;

  return headTpl('百科书院', 'lavender-academy.css', css) + `
  <div class="hero-section wiki-hero"><h1>百科书院</h1><p class="hero-sub">二次元世界的知识中枢——从Cos维基到动画编年史，从角色图鉴到声优资料，从术语词典到创作指南，一切尽在其中。</p><div class="wiki-search"><input type="text" placeholder="搜索百科... 角色/声优/动画/术语" id="wikiQ"><button onclick="var q=document.getElementById('wikiQ').value.trim();if(q)alert('搜索结果(模拟): 找到关于 '+q+' 的 128 篇百科文章')">🔍 搜索</button></div></div>
  <div class="cat-grid">
    <a href="pages/wiki/index.html" class="cat-card"><span class="ci">📚</span><span class="cn">Cos维基</span></a>
    <a href="pages/wiki/timeline.html" class="cat-card"><span class="ci">📅</span><span class="cn">编年史</span></a>
    <a href="pages/wiki/characters.html" class="cat-card"><span class="ci">🎭</span><span class="cn">角色图鉴</span></a>
    <a href="pages/wiki/studios.html" class="cat-card"><span class="ci">🏢</span><span class="cn">动画公司</span></a>
    <a href="pages/wiki/seiyuu.html" class="cat-card"><span class="ci">🎙️</span><span class="cn">声优图鉴</span></a>
    <a href="pages/wiki/glossary.html" class="cat-card"><span class="ci">📝</span><span class="cn">术语词典</span></a>
    <a href="pages/wiki/article.html" class="cat-card"><span class="ci">📄</span><span class="cn">知识文章</span></a>
  </div>
  <div class="sec-header"><span class="sh-icon">🔥</span><h2>热门百科文章</h2><a href="pages/wiki/article.html" class="sh-more">更多 →</a></div>
  <div class="wiki-articles">
    <a href="pages/wiki/article.html" class="wa-card"><div class="wathumb" style="background:linear-gradient(135deg,#7c3aed,#a78bfa)">🎭</div><div class="wainfo"><div class="watitle">Cosplay入门完全指南：从选角到出片</div><div class="wadesc">覆盖角色选择、服装制作、道具打造、化妆技巧、摄影构图、后期修图的完整流程指南。</div><div class="wameta">📖 12,847阅读 · ⭐ 4.9 · 2024.06.15更新</div></div></a>
    <a href="pages/wiki/article.html" class="wa-card"><div class="wathumb" style="background:linear-gradient(135deg,#6366f1,#22d3ee)">🌟</div><div class="wainfo"><div class="watitle">数字人Cosplay革命：AI如何改变Cos圈</div><div class="wadesc">深度解析AI生成、动作捕捉、实时渲染三大技术赋能Cosplay，让虚拟与现实完美融合。</div><div class="wameta">📖 9,234阅读 · ⭐ 4.8 · 2024.06.10更新</div></div></a>
    <a href="pages/wiki/article.html" class="wa-card"><div class="wathumb" style="background:linear-gradient(135deg,#ec4899,#f97316)">⚔️</div><div class="wainfo"><div class="watitle">武器道具制作终极教程：从设计图到成品</div><div class="wadesc">EVA发泡板、PVC管、3D打印——详细对比各种材料优劣，附完整制作流程和涂装技巧。</div><div class="wameta">📖 7,891阅读 · ⭐ 4.7 · 2024.05.28更新</div></div></a>
    <a href="pages/wiki/article.html" class="wa-card"><div class="wathumb" style="background:linear-gradient(135deg,#22c55e,#14b8a6)">📸</div><div class="wainfo"><div class="watitle">Cos摄影布光圣经：从单灯到多灯全攻略</div><div class="wadesc">自然光VS棚拍、Rembrandt光、蝴蝶光、边缘光——手把手教你用光线塑造角色氛围。</div><div class="wameta">📖 6,543阅读 · ⭐ 4.6 · 2024.05.20更新</div></div></a>
  </div>
  <div class="sec-header"><span class="sh-icon">🎭</span><h2>精选角色图鉴</h2></div>
  <div class="feat-char">
    <a href="pages/wiki/characters.html" class="char-card"><span class="ch">⚡</span><span class="chn">雷电将军</span></a>
    <a href="pages/wiki/characters.html" class="char-card"><span class="ch">🎮</span><span class="chn">银狼</span></a>
    <a href="pages/wiki/characters.html" class="char-card"><span class="ch">🐰</span><span class="chn">阿米娅</span></a>
    <a href="pages/wiki/characters.html" class="char-card"><span class="ch">🥜</span><span class="chn">阿尼亚</span></a>
    <a href="pages/wiki/characters.html" class="char-card"><span class="ch">🎤</span><span class="chn">初音未来</span></a>
    <a href="pages/wiki/characters.html" class="char-card"><span class="ch">⚔️</span><span class="chn">银灰</span></a>
  </div>
  <div class="sec-header"><span class="sh-icon">📅</span><h2>动画编年史</h2></div>
  <div class="timeline-strip">
    <a href="pages/wiki/timeline.html" class="tl-item"><div class="tly">1963</div><div class="tlt">铁臂阿童木</div><div class="tld">日本TV动画元年</div></a>
    <div class="tl-item"><div class="tly">1979</div><div class="tlt">机动战士高达</div><div class="tld">真实系机器人开山</div></div>
    <div class="tl-item"><div class="tly">1995</div><div class="tlt">EVA</div><div class="tld">颠覆性叙事革命</div></div>
    <div class="tl-item"><div class="tly">1998</div><div class="tlt">星际牛仔</div><div class="tld">太空爵士诗篇</div></div>
    <div class="tl-item"><div class="tly">2006</div><div class="tlt">凉宫春日</div><div class="tld">轻改动画浪潮</div></div>
    <div class="tl-item"><div class="tly">2011</div><div class="tlt">魔法少女小圆</div><div class="tld">颠覆魔法少女</div></div>
    <div class="tl-item"><div class="tly">2016</div><div class="tlt">你的名字。</div><div class="tld">新海诚现象级</div></div>
    <div class="tl-item"><div class="tly">2020</div><div class="tlt">鬼灭之刃</div><div class="tld">剧场版历史纪录</div></div>
    <a href="pages/wiki/timeline.html" class="tl-item" style="background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center"><div><span style="font-size:1.8rem">→</span><div style="font-weight:700;font-size:.82rem">查看完整编年史</div></div></a>
  </div>` + footTpl;
}

// Write them
write('academy.html', buildAcademy());
write('events.html', buildEvents());
write('wiki.html', buildWiki());

console.log('Part 3 done - academy, events, wiki');

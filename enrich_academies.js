// ========== 龙奕学院 9大学院页面丰富化脚本 (Node.js) ==========
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

// ===== 1. 番剧学院 =====
function buildAnime() {
  const css = `
.anime-hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 30%,rgba(255,107,157,.15),transparent 70%),radial-gradient(ellipse at 80% 70%,rgba(139,92,246,.1),transparent 60%);pointer-events:none}
.anime-hero h1{background:linear-gradient(135deg,#ff6b9d,#a855f7,#6366f1);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.feat-banner{position:relative;margin:0 30px 20px;border-radius:18px;overflow:hidden;height:340px;cursor:pointer;background:linear-gradient(135deg,#1a1a2e,#16213e,#0f3460)}
.feat-banner .fb-overlay{position:absolute;bottom:0;left:0;right:0;padding:36px;background:linear-gradient(transparent,rgba(0,0,0,.88))}
.feat-banner .fb-tag{display:inline-block;background:var(--accent);color:#fff;padding:4px 14px;border-radius:12px;font-size:.72rem;font-weight:700;margin-bottom:8px}
.feat-banner .fb-title{font-size:1.7rem;font-weight:900;color:#fff;margin-bottom:4px}
.feat-banner .fb-desc{font-size:.85rem;color:rgba(255,255,255,.65);max-width:500px;line-height:1.5}
.quick-row{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;padding:0 30px 20px}
.qcard{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:20px;text-align:center;transition:all .3s;cursor:pointer;text-decoration:none;color:inherit;position:relative;overflow:hidden}
.qcard:hover{transform:translateY(-4px);box-shadow:0 12px 36px rgba(0,0,0,.2);border-color:var(--accent)}
.qcard .qi{font-size:2.2rem;display:block;margin-bottom:6px}
.qcard .qt{font-weight:700;font-size:.9rem;margin-bottom:2px}
.qcard .qd{font-size:.74rem;opacity:.6}
.anime-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(175px,1fr));gap:14px;padding:0 30px 20px}
.anime-card{background:var(--bg-card);border-radius:12px;overflow:hidden;border:1px solid var(--border);transition:all .3s;cursor:pointer;text-decoration:none;color:inherit}
.anime-card:hover{transform:translateY(-5px);box-shadow:0 14px 40px rgba(255,107,157,.2);border-color:var(--accent)}
.anime-card .ac-thumb{height:220px;position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center;font-size:3.5rem}
.anime-card .ac-badge{position:absolute;top:8px;left:8px;padding:3px 10px;border-radius:8px;font-size:.66rem;font-weight:700;color:#fff}
.anime-card .ac-info{padding:12px}
.anime-card .ac-title{font-weight:600;font-size:.85rem;line-height:1.35;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;margin-bottom:4px}
.anime-card .ac-meta{font-size:.72rem;opacity:.6;display:flex;justify-content:space-between}
.schedule-strip{display:flex;gap:12px;overflow-x:auto;padding:0 30px 20px;scroll-snap-type:x mandatory}
.schedule-strip::-webkit-scrollbar{height:4px}.schedule-strip::-webkit-scrollbar-thumb{background:var(--accent);border-radius:4px}
.sched-item{flex:0 0 190px;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:16px;scroll-snap-align:start;transition:all .3s;cursor:pointer;text-decoration:none;color:inherit}
.sched-item:hover{border-color:var(--accent);transform:translateY(-2px)}
.sched-item .si-day{font-size:.7rem;font-weight:700;opacity:.5}
.sched-item .si-title{font-weight:600;font-size:.85rem;margin:6px 0}
.sched-item .si-ep{font-size:.7rem;opacity:.5}
.genre-scroll{display:flex;gap:8px;overflow-x:auto;padding:0 30px 6px}.genre-scroll::-webkit-scrollbar{display:none}
.genre-tag{padding:6px 16px;border-radius:20px;border:1px solid var(--border);font-size:.78rem;white-space:nowrap;cursor:pointer;transition:all .2s;background:var(--bg-card)}
.genre-tag:hover,.genre-tag.active{background:var(--accent);color:#fff;border-color:var(--accent)}
@media(max-width:768px){.anime-grid{grid-template-columns:repeat(2,1fr)}.quick-row{grid-template-columns:repeat(2,1fr)}.feat-banner{height:220px;margin:0 14px 16px}}`;

  return headTpl('番剧学院', 'sakura-academy.css', css) + `
  <div class="hero-section anime-hero">
    <h1>番剧学院</h1>
    <p class="hero-sub">AI驱动的沉浸式番剧宇宙——追番、看番、聊番，与千万同好共享二次元盛宴。不只是观看，更是参与。</p>
    <div class="hero-stats"><div class="hero-stat"><span class="hs-val">12,847</span><span class="hs-lbl">收录番剧</span></div><div class="hero-stat"><span class="hs-val">3.2亿</span><span class="hs-lbl">弹幕总数</span></div><div class="hero-stat"><span class="hs-val">8,493</span><span class="hs-lbl">本周更新</span></div><div class="hero-stat"><span class="hs-val">189万</span><span class="hs-lbl">在线观看</span></div></div>
  </div>
  <div class="feat-banner" onclick="location.href='pages/anime/player.html'"><div class="fb-overlay"><span class="fb-tag">热播推荐</span><div class="fb-title">《虚空歌姬 Re:Void》第二季</div><div class="fb-desc">AI驱动叙事的革新番剧。每集由百万观众实时情感数据动态调整剧情走向——你不再是被动的观众，你是故事的共创者。</div></div></div>
  <div class="quick-row">
    <a href="pages/anime/index.html" class="qcard"><span class="qi">🎭</span><div class="qt">番剧大厅</div><div class="qd">浏览全部番剧</div></a>
    <a href="pages/anime/player.html" class="qcard"><span class="qi">▶️</span><div class="qt">在线播放</div><div class="qd">沉浸观影体验</div></a>
    <a href="pages/anime/bangumi.html" class="qcard"><span class="qi">📅</span><div class="qt">新番时间表</div><div class="qd">追番不迷路</div></a>
    <a href="pages/anime/ranking.html" class="qcard"><span class="qi">🏆</span><div class="qt">番剧排行</div><div class="qd">实时热门榜单</div></a>
  </div>
  <div class="sec-header"><span class="sh-icon">🔥</span><h2>今日热播番剧</h2><a href="pages/anime/ranking.html" class="sh-more">查看全部 →</a></div>
  <div class="anime-grid" id="hotGrid"></div>
  <div class="sec-header"><span class="sh-icon">🆕</span><h2>7月新番速递</h2><a href="pages/anime/bangumi.html" class="sh-more">时间表 →</a></div>
  <div class="anime-grid" id="newGrid"></div>
  <div class="sec-header"><span class="sh-icon">📺</span><h2>今日放送日程</h2><a href="pages/anime/live.html" class="sh-more">直播 →</a></div>
  <div class="schedule-strip" id="scheduleStrip"></div>
  <div class="sec-header"><span class="sh-icon">🏷️</span><h2>分类探索</h2></div>
  <div class="genre-scroll" id="genreBar"></div>
  <div class="sec-header"><span class="sh-icon">🎨</span><h2>MAD/AMV 二创精选</h2><a href="pages/anime/mad.html" class="sh-more">创作工坊 →</a></div>
  <div class="anime-grid" id="madGrid"></div>
<script>
!function(){var n=[{t:"虚空歌姬 Re:Void S2",m:"12话 9.8分 1.2亿播放",b:"热播",c:"linear-gradient(135deg,#ff6b9d,#a855f7)",i:"🎤"},{t:"星海纪元 Chronos Edge",m:"24话 9.7分 2.8亿播放",b:"霸榜",c:"linear-gradient(135deg,#6366f1,#22d3ee)",i:"🌟"},{t:"刀剑圣域 Alicization",m:"47话 9.6分 5.6亿播放",b:"经典",c:"linear-gradient(135deg,#f59e0b,#ef4444)",i:"⚔️"},{t:"辉夜大小姐 S4",m:"13话 9.5分 3.1亿播放",b:"热播",c:"linear-gradient(135deg,#ec4899,#8b5cf6)",i:"💕"},{t:"剑风传奇 黄金时代",m:"剧场版 9.9分 8900万播放",b:"神作",c:"linear-gradient(135deg,#fbbf24,#d97706)",i:"🗡️"},{t:"孤独摇滚 S2",m:"12话 9.4分 2.3亿播放",b:"热播",c:"linear-gradient(135deg,#14b8a6,#06b6d4)",i:"🎸"}],
o=[{t:"轮回第7次的恶役千金",m:"独家 每周六更新",b:"独家",c:"linear-gradient(135deg,#ec4899,#db2777)",i:"👑"},{t:"青梅竹马是宇宙人？",m:"轻改 每周三更新",b:"新番",c:"linear-gradient(135deg,#8b5cf6,#7c3aed)",i:"👽"},{t:"灵能百分百 最终章",m:"剧场版上映中",b:"话题",c:"linear-gradient(135deg,#f97316,#ea580c)",i:"👻"},{t:"REVENGER 复仇者",m:"虚渊玄原案 每周五",b:"大作",c:"linear-gradient(135deg,#dc2626,#b91c1c)",i:"🔪"},{t:"僵尸百分百 S2",m:"Netflix同步 每周日",b:"热追",c:"linear-gradient(135deg,#84cc16,#65a30d)",i:"🧟"},{t:"间谍过家家 S3",m:"WIT STUDIO 秋季档",b:"期待",c:"linear-gradient(135deg,#06b6d4,#0891b2)",i:"🥜"}],
m=[{t:"虚空歌姬 × Unravel",m:"播放892万 硬币12万",b:"神剪辑",c:"linear-gradient(135deg,#7c3aed,#6366f1)",i:"✂️"},{t:"星海纪元 这就是神作",m:"播放567万 硬币8万",b:"燃向",c:"linear-gradient(135deg,#ef4444,#dc2626)",i:"🔥"},{t:"那些年我们追过的番",m:"播放1203万 硬币21万",b:"情怀",c:"linear-gradient(135deg,#f59e0b,#d97706)",i:"😭"},{t:"2024年度MAD大赏",m:"播放445万 硬币6万",b:"年度",c:"linear-gradient(135deg,#22c55e,#16a34a)",i:"🏅"},{t:"全角色混剪 龙奕学院",m:"播放234万 硬币5万",b:"官方",c:"linear-gradient(135deg,#ec4899,#be185d)",i:"🎬"},{t:"静止画MAD叙事",m:"播放178万 硬币9万",b:"艺术",c:"linear-gradient(135deg,#a78bfa,#8b5cf6)",i:"🖼️"}],
s=[{d:"周一",t:"星海纪元",e:"第18话",c:"linear-gradient(135deg,#6366f1,#22d3ee)",i:"🌟"},{d:"周三",t:"轮回第7次恶役千金",e:"第5话",c:"linear-gradient(135deg,#ec4899,#db2777)",i:"👑"},{d:"周五",t:"REVENGER 复仇者",e:"第3话",c:"linear-gradient(135deg,#dc2626,#b91c1c)",i:"🔪"},{d:"周六",t:"虚空歌姬 Re:Void S2",e:"第9话",c:"linear-gradient(135deg,#ff6b9d,#a855f7)",i:"🎤"},{d:"周日",t:"僵尸百分百 S2",e:"第12话 完结",c:"linear-gradient(135deg,#84cc16,#65a30d)",i:"🧟"},{d:"周日",t:"孤独摇滚 S2",e:"第7话",c:"linear-gradient(135deg,#14b8a6,#06b6d4)",i:"🎸"}],
g=["全部","热血","恋爱","搞笑","科幻","奇幻","悬疑","日常","机战","异世界","偶像","运动"];
function C(a){var bc=a.b==='热播'?'#ff6b9d':a.b==='霸榜'?'#f59e0b':a.b==='神作'?'#fbbf24':'#8b5cf6';return'<a href="pages/anime/detail-'+((Math.random()*8|0)+1)+'.html" class="anime-card"><div class="ac-thumb" style="background:'+a.c+'">'+a.i+'</div><span class="ac-badge" style="background:'+bc+'">'+a.b+'</span><div class="ac-info"><div class="ac-title">'+a.t+'</div><div class="ac-meta">'+a.m+'</div></div></a>'}
document.getElementById('hotGrid').innerHTML=n.map(C).join('');
document.getElementById('newGrid').innerHTML=o.map(C).join('');
document.getElementById('madGrid').innerHTML=m.map(C).join('');
document.getElementById('scheduleStrip').innerHTML=s.map(function(x){return'<a href="pages/anime/bangumi.html" class="sched-item"><div class="si-day">'+x.d+'</div><div style="font-size:2.5rem;text-align:center;margin:8px 0">'+x.i+'</div><div class="si-title">'+x.t+'</div><div class="si-ep">'+x.e+'</div></a>'}).join('');
document.getElementById('genreBar').innerHTML=g.map(function(x,i){return'<span class="genre-tag'+(i===0?' active':'')+'" onclick="var t=this;document.querySelectorAll(\'.genre-tag\').forEach(function(e){e.classList.remove(\'active\')});t.classList.add(\'active\')">'+x+'</span>'}).join('')}();
</script>` + footTpl;
}

// ===== 2. 羁绊学院 =====
function buildSocial() {
  const css = `
.social-layout{display:flex;gap:20px;padding:0 30px 20px}
.social-side{width:240px;flex-shrink:0}.social-main{flex:1;min-width:0}.social-right{width:280px;flex-shrink:0}
.side-menu{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:14px;position:sticky;top:80px}
.side-menu h3{font-size:.82rem;opacity:.5;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px}
.side-menu a{display:flex;align-items:center;gap:8px;padding:9px 10px;border-radius:10px;color:inherit;text-decoration:none;font-size:.85rem;transition:all .2s;margin-bottom:1px}
.side-menu a:hover,.side-menu a.active{background:rgba(255,255,255,.05);color:var(--accent)}
.side-menu a .badge{margin-left:auto;font-size:.7rem;padding:2px 8px;border-radius:10px;background:rgba(255,255,255,.06)}
.ai-zone{background:linear-gradient(135deg,rgba(196,77,255,.06),rgba(0,229,255,.06));border:2px dashed rgba(196,77,255,.25);border-radius:14px;padding:32px 20px;text-align:center;margin-bottom:18px;transition:all .3s;cursor:pointer;position:relative;overflow:hidden}
.ai-zone:hover{border-color:var(--accent);background:rgba(196,77,255,.1)}
.ai-zone input[type=file]{position:absolute;inset:0;opacity:0;cursor:pointer}
.ai-zone .az-icon{font-size:2.5rem;display:block;margin-bottom:8px}
.ai-zone h3{font-size:1.05rem;margin-bottom:4px}.ai-zone p{font-size:.78rem;opacity:.6}
.post-composer{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:18px;margin-bottom:18px}
.post-composer textarea{width:100%;min-height:72px;background:rgba(255,255,255,.03);border:1px solid var(--border);border-radius:10px;padding:12px;color:var(--text);resize:vertical;font:inherit;font-size:.9rem}
.post-composer textarea:focus{outline:none;border-color:var(--accent)}
.pc-actions{display:flex;gap:8px;margin-top:10px;align-items:center}
.feed-post{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:18px;margin-bottom:14px;transition:all .25s}
.feed-post:hover{border-color:rgba(255,255,255,.15)}
.post-hd{display:flex;align-items:center;gap:10px;margin-bottom:12px}
.post-av{width:40px;height:40px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.1rem;flex-shrink:0}
.post-user{flex:1}.post-user .uname{font-weight:700;font-size:.88rem}.post-user .utime{font-size:.72rem;opacity:.5}
.post-body{font-size:.9rem;line-height:1.65;margin-bottom:10px}
.post-media{width:100%;border-radius:10px;min-height:160px;display:flex;align-items:center;justify-content:center;font-size:3.5rem;margin-bottom:10px}
.post-tags{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:10px}
.tag{font-size:.7rem;padding:3px 10px;border-radius:8px;background:rgba(255,255,255,.05)}
.post-acts{display:flex;gap:16px;flex-wrap:wrap}
.post-acts button{background:none;border:none;color:inherit;opacity:.6;display:flex;align-items:center;gap:4px;font-size:.82rem;cursor:pointer;padding:4px 8px;border-radius:6px;transition:all .2s;font:inherit}
.post-acts button:hover{opacity:1;background:rgba(255,255,255,.04)}
.post-acts button.liked{color:#ff4081;opacity:1}
.right-card{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:16px;margin-bottom:14px}
.right-card h3{font-size:.9rem;margin-bottom:12px}
.trend-row{display:flex;align-items:center;gap:8px;padding:7px 0;border-bottom:1px solid var(--border);cursor:pointer;transition:all .2s}
.trend-row:last-child{border-bottom:none}.trend-row:hover{color:var(--accent)}
.trend-rank{font-weight:800;font-size:.82rem;color:var(--accent);width:22px}
.trend-info{flex:1}.trend-info .tn{font-size:.82rem}.trend-info .tc{font-size:.7rem;opacity:.5}
.live-dots{display:flex;gap:6px;overflow-x:auto;padding-bottom:4px}.live-dots::-webkit-scrollbar{display:none}
.live-dot{width:44px;height:44px;border-radius:50%;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:1.2rem;position:relative;cursor:pointer;border:2px solid transparent;transition:all .2s}
.live-dot:hover{border-color:var(--accent)}.live-dot::after{content:'';position:absolute;bottom:2px;right:2px;width:10px;height:10px;border-radius:50%;background:#22c55e;border:2px solid var(--bg-card)}
@media(max-width:1024px){.social-layout{flex-direction:column;padding:0 14px 14px}.social-side,.social-right{width:100%}.side-menu{display:flex;overflow-x:auto;gap:4px;position:static}.side-menu a{white-space:nowrap;flex-shrink:0}.side-menu .badge{display:none}.right-card{position:static}}`;

  return headTpl('羁绊学院', 'coral-academy.css', css) + `
  <div class="hero-section" style="background:radial-gradient(ellipse at 50% 30%,rgba(255,107,157,.12),transparent 70%)">
    <h1 style="background:linear-gradient(135deg,#ff6b9d,#f97316,#ef4444);-webkit-background-clip:text;-webkit-text-fill-color:transparent">羁绊学院</h1>
    <p class="hero-sub">以Cos为纽带，连接千万同好。AI角色识别、社区动态、社团活动——这里不只是一个社交平台，是二次元的家。</p>
    <div class="hero-stats"><div class="hero-stat"><span class="hs-val">52.8万</span><span class="hs-lbl">注册Coser</span></div><div class="hero-stat"><span class="hs-val">890万</span><span class="hs-lbl">累计动态</span></div><div class="hero-stat"><span class="hs-val">1,247</span><span class="hs-lbl">当前在线</span></div></div>
  </div>
  <div class="social-layout">
    <aside class="social-side"><div class="side-menu"><h3>板块导航</h3><a href="#" class="active">🔥 推荐动态</a><a href="#">🆕 最新发布</a><a href="#">🎯 关注动态<span class="badge">23</span></a><a href="#">🏷️ 角色专区</a><a href="#">📸 摄影作品</a><a href="#">🎨 化妆教程</a><a href="#">🛠️ 道具制作</a><a href="#">🎪 漫展活动</a><a href="#">💬 聊天室</a></div></aside>
    <main class="social-main">
      <div class="ai-zone"><input type="file" accept="image/*" onchange="H(this)" id="aiFile"><span class="az-icon">🤖</span><h3>AI Cosplay 角色识别</h3><p>拖拽或点击上传Cosplay照片 · JPG/PNG/WebP · 最大20MB</p></div>
      <div id="aiResult" style="display:none;background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:18px;margin-bottom:18px"></div>
      <div class="post-composer"><textarea placeholder="分享你的Cosplay日常... 支持 @提及用户 和 #话题标签" id="postText"></textarea><div class="pc-actions"><button class="btn btn-ghost btn-sm">📷</button><button class="btn btn-ghost btn-sm">🎬</button><button class="btn btn-ghost btn-sm">🏷️</button><button class="btn btn-ghost btn-sm" style="margin-left:auto" onclick="P()">发布动态</button></div></div>
      <div style="padding:0 0 14px"><div style="font-size:.82rem;font-weight:700;margin-bottom:8px">🔴 好友正在直播</div><div class="live-dots" id="liveDots"></div></div>
      <div id="feedContainer"></div>
      <div style="text-align:center;padding:16px"><button class="btn btn-outline" onclick="alert('没有更多动态了~')">📥 加载更多</button></div>
    </main>
    <aside class="social-right">
      <div class="right-card"><h3>🔥 热门话题</h3><div id="trendList"></div></div>
      <div class="right-card"><h3>👥 推荐关注</h3><div id="suggestedUsers"></div></div>
    </aside>
  </div>
<script>
!function(){var p=[{u:"樱落Cos",av:"🌸",abg:"linear-gradient(135deg,#ff4081,#ff80ab)",t:"2小时前",v:true,tx:"新出的雷电将军cos正片来啦！这次特意选了稻妻城的实景拍摄，无想的一刀特效是后期加的~大家觉得还原度怎么样？",img:"⚡",ibg:"linear-gradient(135deg,#4a148c,#7b1fa2)",ta:["#雷电将军","#原神cos","#正片"],li:2847,cm:356,sa:892,ld:false},{u:"道具大师K",av:"🔧",abg:"linear-gradient(135deg,#ff6f00,#ffa000)",t:"5小时前",v:true,tx:"分享一下最近做的银狼专属武器星海巡航的3D建模过程。从草图到成品花了整整两周~",img:"🎨",ibg:"linear-gradient(135deg,#01579b,#0288d1)",ta:["#银狼","#道具制作","#3D建模"],li:1523,cm:201,sa:567,ld:false},{u:"小透明Coser",av:"🐱",abg:"linear-gradient(135deg,#00c853,#69f0ae)",t:"8小时前",v:false,tx:"入坑3个月的成果！虽然还有很多不足，但是真的很喜欢cosplay。感谢龙奕学院社区的大佬们！",img:"🌟",ibg:"linear-gradient(135deg,#1b5e20,#43a047)",ta:["#新人cos","#成长记录"],li:487,cm:102,sa:56,ld:false},{u:"摄影师大A",av:"📷",abg:"linear-gradient(135deg,#37474f,#607d8b)",t:"12小时前",v:true,tx:"漫展现场返图！今天拍了20多组Coser。器材：Sony A7M4 + 85mm F1.4 GM，后期LR调色。",img:"📸",ibg:"linear-gradient(135deg,#212121,#424242)",ta:["#漫展","#返图","#摄影"],li:3201,cm:489,sa:1203,ld:false}];
document.getElementById('liveDots').innerHTML="🌸,⚔️,💎,🎤,📷,🎨,🎮,🐰".split(",").map(function(a,i){var bgs=["linear-gradient(135deg,#ff4081,#ff80ab)","linear-gradient(135deg,#7c4dff,#b388ff)","linear-gradient(135deg,#00e5ff,#80deea)","linear-gradient(135deg,#ff6b9d,#a855f7)","linear-gradient(135deg,#37474f,#607d8b)","linear-gradient(135deg,#f97316,#ea580c)","linear-gradient(135deg,#6366f1,#22d3ee)","linear-gradient(135deg,#22c55e,#16a34a)"];return'<div class="live-dot" style="background:'+bgs[i]+'" title="直播中">'+a+'</div>'}).join("");
document.getElementById('trendList').innerHTML=[{r:1,n:"#崩坏星穹铁道cos",c:"12.8万动态"},{r:2,n:"#原神cos正片",c:"9.6万动态"},{r:3,n:"#明日方舟cos",c:"8.2万动态"},{r:4,n:"#碧蓝航线cos",c:"6.5万动态"},{r:5,n:"#间谍过家家cos",c:"5.3万动态"}].map(function(t){return'<div class="trend-row"><span class="trend-rank">#'+t.r+'</span><div class="trend-info"><div class="tn">'+t.n+'</div><div class="tc">'+t.c+'</div></div></div>'}).join("");
document.getElementById('suggestedUsers').innerHTML=[{n:"樱落Cos",b:"专业Coser 12.3万粉",bg:"linear-gradient(135deg,#ff4081,#ff80ab)",av:"🌸"},{n:"SwordArt_Cos",b:"武器道具师 8.7万粉",bg:"linear-gradient(135deg,#7c4dff,#b388ff)",av:"⚔️"},{n:"星穹铁道Cos社",b:"社团官方 15.1万粉",bg:"linear-gradient(135deg,#00e5ff,#80deea)",av:"💎"}].map(function(u){return'<div style="display:flex;align-items:center;gap:8px;padding:8px 0;border-bottom:1px solid var(--border)"><div style="width:34px;height:34px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:.9rem;background:'+u.bg+'">'+u.av+'</div><div style="flex:1"><div style="font-size:.82rem;font-weight:500">'+u.n+'</div><div style="font-size:.7rem;opacity:.5">'+u.b+'</div></div><button class="btn btn-outline btn-sm" onclick="this.textContent=\\'已关注\\'">+关注</button></div>'}).join("");
document.getElementById('feedContainer').innerHTML=p.map(function(x,i){return'<div class="feed-post"><div class="post-hd"><div class="post-av" style="background:'+x.abg+'">'+x.av+'</div><div class="post-user"><div class="uname">'+x.u+(x.v?' <span style="font-size:.66rem;padding:2px 8px;border-radius:8px;background:rgba(0,229,255,.15);color:#00e5ff">认证</span>':'')+'</div><div class="utime">'+x.t+'</div></div></div><div class="post-body">'+x.tx+'</div><div class="post-media" style="background:'+x.ibg+'">'+x.img+'</div><div class="post-tags">'+x.ta.map(function(t){return'<span class="tag">'+t+'</span>'}).join("")+'</div><div class="post-acts"><button onclick="L(this,'+i+')">❤️ <span>'+x.li.toLocaleString()+'</span></button><button>💬 <span>'+x.cm+'</span></button><button>⭐ <span>'+x.sa+'</span></button><button>🔗 分享</button></div></div>'}).join("")})();
function L(b,i){var x=p[i];x.ld=!x.ld;x.li+=x.ld?1:-1;b.classList.toggle('liked',x.ld);b.querySelector('span').textContent=x.li.toLocaleString()}
function P(){var t=document.getElementById('postText').value.trim();if(!t)return;alert('动态发布成功!');document.getElementById('postText').value=''}
function H(input){var f=input.files[0];if(!f)return;var r=document.getElementById('aiResult');r.style.display='block';r.innerHTML='<div style="display:flex;align-items:center;gap:12px"><div style="font-size:3rem">🧝</div><div><h4>识别中...</h4><p style="opacity:.5">分析特征...</p></div><div style="margin-left:auto;text-align:center"><div style="font-size:1.5rem;font-weight:800;color:#22c55e">--%</div><div style="font-size:.7rem;opacity:.5">置信度</div></div></div>';var chars=[{n:"雷电将军",s:"原神",c:92.7},{n:"银狼",s:"崩坏：星穹铁道",c:88.4},{n:"阿米娅",s:"明日方舟",c:95.1},{n:"阿尼亚",s:"间谍过家家",c:86.3},{n:"初音未来",s:"VOCALOID",c:97.8}];var pk=chars[Math.random()*chars.length|0];setTimeout(function(){r.innerHTML='<div style="display:flex;align-items:center;gap:12px"><div style="font-size:3rem">🧝</div><div><h4>'+pk.n+'</h4><p style="opacity:.5">'+pk.s+'</p></div><div style="margin-left:auto;text-align:center"><div style="font-size:1.5rem;font-weight:800;color:#22c55e">'+pk.c+'%</div><div style="font-size:.7rem;opacity:.5">置信度</div></div></div>'},1800)}
</script>` + footTpl;
}

// ===== Write =====
function write(name, builder) {
  const html = builder();
  fs.writeFileSync(path.join(base, name), html, 'utf8');
  console.log('OK: ' + name + ' (' + html.length + ' chars)');
}

write('anime.html', buildAnime);
write('social.html', buildSocial);

console.log('Part 1 done - anime + social');

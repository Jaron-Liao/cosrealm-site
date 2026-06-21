# -*- coding: utf-8 -*-
"""生成4个缺失模块首页 + 深度重写数字人子页面"""
import os

BASE = r"C:\Users\28767\Downloads\cosrealm-site"

# ======================================================================
# 1. anime.html — 番剧大厅 (3D: anime, theme: sakura-academy)
# ======================================================================
anime_html = '''<!DOCTYPE html>
<html lang="zh-CN" data-3d="anime">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>番剧学院 | 龙奕学院 LongYi Academy</title>
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="assets/themes/academy/sakura-academy.css">
<link rel="stylesheet" href="assets/effects-layer.css">
<style>
.page-container{position:relative;z-index:1;padding-top:80px;max-width:1300px;margin:0 auto}
/* Hero */
.anime-hero{position:relative;padding:60px 30px 40px;text-align:center;overflow:hidden}
.anime-hero::before{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:radial-gradient(ellipse at 50% 30%,rgba(255,107,157,.15),transparent 70%),radial-gradient(ellipse at 80% 70%,rgba(139,92,246,.1),transparent 60%);pointer-events:none}
.anime-hero h1{font-size:3rem;font-weight:900;background:linear-gradient(135deg,#ff6b9d,#a855f7,#6366f1);-webkit-background-clip:text;-webkit-text-fill-color:transparent;position:relative;z-index:1}
.anime-hero p{font-size:1.1rem;color:var(--text-secondary);max-width:600px;margin:12px auto 0;position:relative;z-index:1}
.hero-stats-row{display:flex;justify-content:center;gap:40px;margin-top:24px;position:relative;z-index:1}
.hs-item{text-align:center}
.hs-num{font-size:2rem;font-weight:900;background:linear-gradient(135deg,var(--accent),var(--accent-secondary,#a78bfa));-webkit-background-clip:text;-webkit-text-fill-color:transparent;display:block}
.hs-label{font-size:.82rem;color:var(--text-dim);margin-top:4px}

/* Featured banner */
.featured-banner{position:relative;margin:20px 30px;border-radius:20px;overflow:hidden;height:360px;background:linear-gradient(135deg,#1a1a2e,#16213e,#0f3460);cursor:pointer}
.featured-banner .fb-img{width:100%;height:100%;object-fit:cover;opacity:.7;transition:transform 8s,opacity .5s}
.featured-banner:hover .fb-img{transform:scale(1.05);opacity:.85}
.featured-banner .fb-overlay{position:absolute;bottom:0;left:0;right:0;padding:40px;background:linear-gradient(transparent,rgba(0,0,0,.85))}
.featured-banner .fb-tag{display:inline-block;background:var(--accent);color:#fff;padding:4px 14px;border-radius:12px;font-size:.75rem;font-weight:700;margin-bottom:10px}
.featured-banner .fb-title{font-size:1.8rem;font-weight:900;color:#fff;margin-bottom:6px}
.featured-banner .fb-desc{font-size:.9rem;color:rgba(255,255,255,.7);max-width:500px}

/* Hot section */
.section-wrap{padding:20px 30px}
.sec-title{font-size:1.4rem;font-weight:800;margin-bottom:16px;display:flex;align-items:center;gap:10px}
.sec-title .st-icon{font-size:1.6rem}
.sec-title .st-more{margin-left:auto;font-size:.82rem;color:var(--text-dim);text-decoration:none}
.anime-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:16px}
.anime-item{background:var(--bg-card);border-radius:14px;overflow:hidden;border:1px solid var(--border);transition:all .35s;cursor:pointer;text-decoration:none;color:inherit}
.anime-item:hover{transform:translateY(-6px);box-shadow:0 14px 40px rgba(255,107,157,.25);border-color:var(--accent)}
.anime-item .ai-thumb{width:100%;height:240px;position:relative;overflow:hidden;background:var(--bg-secondary)}
.anime-item .ai-thumb .ai-cover{width:100%;height:100%;object-fit:cover;transition:transform .5s}
.anime-item:hover .ai-cover{transform:scale(1.08)}
.anime-item .ai-badge{position:absolute;top:8px;left:8px;background:var(--accent);color:#fff;font-size:.68rem;padding:2px 8px;border-radius:8px;font-weight:700}
.anime-item .ai-info{padding:12px}
.anime-item .ai-title{font-weight:600;font-size:.88rem;line-height:1.4;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;margin-bottom:6px}
.anime-item .ai-meta{font-size:.74rem;color:var(--text-dim);display:flex;justify-content:space-between}
/* Rainbow card rows */
.rainbow-row{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;padding:0 30px 30px}
.rainbow-card{background:var(--bg-card);border-radius:16px;padding:24px;border:1px solid var(--border);text-align:center;transition:all .35s;cursor:pointer;text-decoration:none;color:inherit;position:relative;overflow:hidden}
.rainbow-card::before{content:'';position:absolute;top:-50%;left:-50%;width:200%;height:200%;background:conic-gradient(var(--card-accent,var(--accent)),transparent,var(--card-accent,var(--accent)));animation:rcSpin 8s linear infinite;opacity:.06}
@keyframes rcSpin{to{transform:rotate(360deg)}}
.rainbow-card:hover{transform:translateY(-4px);box-shadow:0 12px 36px rgba(0,0,0,.2)}
.rainbow-card .rc-icon{font-size:2.5rem;margin-bottom:8px;display:block}
.rainbow-card .rc-title{font-weight:700;font-size:.95rem;margin-bottom:4px}
.rainbow-card .rc-desc{font-size:.78rem;color:var(--text-dim)}
@media(max-width:768px){.anime-grid{grid-template-columns:repeat(2,1fr)}.rainbow-row{grid-template-columns:repeat(2,1fr)}.anime-hero h1{font-size:2rem}.featured-banner{height:240px}}
</style>
</head>
<body>
<div id="nav-placeholder"></div>
<div class="page-container">
  <div class="anime-hero">
    <h1>🎬 番剧学院</h1>
    <p>追番、看番、聊番——AI驱动的沉浸式番剧宇宙。与B站并肩，我们提供更深度的元宇宙番剧体验。</p>
    <div class="hero-stats-row">
      <div class="hs-item"><span class="hs-num">12,847</span><span class="hs-label">收录番剧</span></div>
      <div class="hs-item"><span class="hs-num">3.2亿</span><span class="hs-label">弹幕总数</span></div>
      <div class="hs-item"><span class="hs-num">8,493</span><span class="hs-label">本周更新</span></div>
      <div class="hs-item"><span class="hs-num">189万</span><span class="hs-label">在线观看</span></div>
    </div>
  </div>

  <div class="featured-banner hologram">
    <div class="fb-overlay">
      <span class="fb-tag">🔥 热播推荐</span>
      <div class="fb-title">《虚空歌姬 Re:Void》第二季</div>
      <div class="fb-desc">AI 驱动叙事的革新番剧。每集由百万观众的实时情感数据动态调整剧情走向——你不再是被动的观众，你是故事的共同创作者。</div>
    </div>
  </div>

  <div class="rainbow-row">
    <a href="pages/anime/index.html" class="rainbow-card" style="--card-accent:#ff6b9d"><span class="rc-icon">🎭</span><div class="rc-title">番剧大厅</div><div class="rc-desc">浏览全部番剧</div></a>
    <a href="pages/anime/player.html" class="rainbow-card" style="--card-accent:#6366f1"><span class="rc-icon">▶️</span><div class="rc-title">在线播放</div><div class="rc-desc">沉浸式观影体验</div></a>
    <a href="pages/anime/bangumi.html" class="rainbow-card" style="--card-accent:#22d3ee"><span class="rc-icon">📅</span><div class="rc-title">新番时间表</div><div class="rc-desc">追番不迷路</div></a>
    <a href="pages/anime/ranking.html" class="rainbow-card" style="--card-accent:#f59e0b"><span class="rc-icon">🏆</span><div class="rc-title">番剧排行</div><div class="rc-desc">热门榜单实时更新</div></a>
  </div>

  <div class="section-wrap">
    <div class="sec-title"><span class="st-icon">🔥</span> 今日热播番剧<a href="pages/anime/ranking.html" class="st-more">查看全部 →</a></div>
    <div class="anime-grid" id="hotAnime"></div>
  </div>

  <div class="section-wrap">
    <div class="sec-title"><span class="st-icon">🆕</span> 4月新番速递<a href="pages/anime/bangumi.html" class="st-more">查看全部 →</a></div>
    <div class="anime-grid" id="newAnime"></div>
  </div>

  <div class="section-wrap">
    <div class="sec-title"><span class="st-icon">🎨</span> MAD / AMV / 二创精选<a href="pages/anime/mad.html" class="st-more">进入创作工坊 →</a></div>
    <div class="anime-grid" id="madWorks"></div>
  </div>
</div>
<script src="assets/particles.js"></script>
<script src="assets/three-engine-v3.js"></script>
<script src="assets/effects-runtime.js"></script>
<script src="assets/nav.js"></script>
<script>
const animeList=[{t:'虚空歌姬 Re:Void S2',m:'12话 · 9.8分 · 1.2亿播放',b:'热播',c:'linear-gradient(135deg,#ff6b9d,#a855f7)'},{t:'星海纪元 Chronos Edge',m:'24话 · 9.7分 · 2.8亿播放',b:'霸榜',c:'linear-gradient(135deg,#6366f1,#22d3ee)'},{t:'刀剑圣域 Alicization',m:'47话 · 9.6分 · 5.6亿播放',b:'经典',c:'linear-gradient(135deg,#f59e0b,#ef4444)'},{t:'辉夜大小姐想让我告白 S4',m:'13话 · 9.5分 · 3.1亿播放',b:'热播',c:'linear-gradient(135deg,#ec4899,#8b5cf6)'},{t:'剑风传奇 黄金时代',m:'剧场版 · 9.9分 · 8900万播放',b:'神作',c:'linear-gradient(135deg,#fbbf24,#d97706)'},{t:'孤独摇滚 S2',m:'12话 · 9.4分 · 2.3亿播放',b:'热播',c:'linear-gradient(135deg,#14b8a6,#06b6d4)'}];
const newList=[{t:'轮回第7次的恶役千金',m:'全网独播 · 每周六更新',b:'独家'},{t:'青梅竹马是宇宙人？',m:'每周三更新 · 轻改',b:'新番'},{t:'灵能百分百 最终章',m:'剧场版上映中',b:'话题'},{t:'REVENGER 复仇者',m:'虚渊玄原案 · 每周五更新',b:'大作'},{t:'僵尸百分百 S2',m:'Netflix同步 · 每周日',b:'热追'},{t:'间谍过家家 S3',m:'WIT STUDIO · 秋季档',b:'期待'}];
const madList=[{t:'【MAD/AMV】虚空歌姬 × Unravel',m:'播放: 892万 · 硬币: 12万',b:'神剪辑'},{t:'【误解系】星海纪元 — 这就是神作',m:'播放: 567万 · 硬币: 8万',b:'燃向'},{t:'【催泪向】那些年我们追过的番',m:'播放: 1203万 · 硬币: 21万',b:'情怀'},{t:'【踩点向】2024年度MAD大赏',m:'播放: 445万 · 硬币: 6万',b:'年度'},{t:'【AMV】全角色混剪 — 龙奕学院',m:'播放: 234万 · 硬币: 5万',b:'官方'},{t:'【静止画MAD】你从未见过的叙事',m:'播放: 178万 · 硬币: 9万',b:'艺术'}];
function renderCards(list,container,isMad){container.innerHTML=list.map((a,i)=>`<a href="pages/anime/detail-${(i%8)+1}.html" class="anime-item"><div class="ai-thumb"><div style="width:100%;height:100%;${a.c||'background:var(--bg-secondary)'};display:flex;align-items:center;justify-content:center;font-size:3rem">${isMad?'🎬':['🎭','🌟','⚔️','💕','🗡️','🎸','♾️','🛸'][i%8]}</div><span class="ai-badge">${a.b}</span></div><div class="ai-info"><div class="ai-title">${a.t}</div><div class="ai-meta">${a.m}</div></div></a>`).join('')}
renderCards(animeList,'hotAnime');renderCards(newList,'newAnime');renderCards(madList,'madWorks',true);
</script>
</body>
</html>'''

# ======================================================================
# 2. events.html — 祭典活动中心 (3D: galaxy, theme: sunset-academy)
# ======================================================================
events_html = '''<!DOCTYPE html>
<html lang="zh-CN" data-3d="galaxy">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>祭典学院 | 龙奕学院 LongYi Academy</title>
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="assets/themes/academy/sunset-academy.css">
<link rel="stylesheet" href="assets/effects-layer.css">
<style>
.page-container{position:relative;z-index:1;padding-top:80px;max-width:1300px;margin:0 auto}
.events-hero{position:relative;padding:60px 30px 40px;text-align:center;overflow:hidden}
.events-hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 30% 20%,rgba(249,115,22,.13),transparent 60%),radial-gradient(ellipse at 70% 80%,rgba(236,72,153,.1),transparent 60%);pointer-events:none}
.events-hero h1{font-size:3rem;font-weight:900;background:linear-gradient(135deg,#f97316,#ec4899,#f59e0b);-webkit-background-clip:text;-webkit-text-fill-color:transparent;position:relative;z-index:1}
.events-hero p{font-size:1.1rem;color:var(--text-secondary);max-width:600px;margin:12px auto 0;position:relative;z-index:1}
.event-countdown{display:flex;justify-content:center;gap:20px;margin-top:20px;position:relative;z-index:1}
.cd-item{text-align:center;background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:16px 24px;min-width:80px}
.cd-num{font-size:2.2rem;font-weight:900;color:var(--accent);display:block;line-height:1}
.cd-label{font-size:.72rem;color:var(--text-dim);margin-top:4px}
.card-grid2{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:18px;padding:20px 30px 30px}
.ev-card{background:var(--bg-card);border-radius:18px;overflow:hidden;border:1px solid var(--border);transition:all .35s;cursor:pointer;text-decoration:none;color:inherit;position:relative}
.ev-card:hover{transform:translateY(-6px);box-shadow:0 16px 48px rgba(249,115,22,.2)}
.ev-card .ev-header{height:160px;position:relative;overflow:hidden}
.ev-card .ev-header-inner{width:100%;height:100%;display:flex;align-items:center;justify-content:center;font-size:4rem;position:relative}
.ev-card .ev-date-badge{position:absolute;top:12px;right:12px;background:rgba(0,0,0,.7);color:#fff;padding:4px 12px;border-radius:10px;font-size:.7rem;font-weight:700;backdrop-filter:blur(6px)}
.ev-card .ev-status{position:absolute;top:12px;left:12px;padding:4px 12px;border-radius:10px;font-size:.7rem;font-weight:700;color:#fff}
.ev-card .ev-status.upcoming{background:#f59e0b}.ev-card .ev-status.ongoing{background:#22c55e}.ev-card .ev-status.past{background:#6b7280}
.ev-card .ev-body{padding:18px}
.ev-card .ev-title{font-weight:700;font-size:1rem;margin-bottom:6px}
.ev-card .ev-desc{font-size:.82rem;color:var(--text-secondary);line-height:1.5;margin-bottom:10px}
.ev-card .ev-footer{display:flex;justify-content:space-between;font-size:.78rem;color:var(--text-dim)}
@media(max-width:768px){.events-hero h1{font-size:2rem}.card-grid2{grid-template-columns:1fr}.event-countdown{flex-wrap:wrap}}
</style>
</head>
<body>
<div id="nav-placeholder"></div>
<div class="page-container">
  <div class="events-hero">
    <h1>🎪 祭典学院</h1>
    <p>线上元宇宙活动 + 线下真实聚会 · Cos大赛 · 漫展 · 虚拟演唱会 · 学园祭 · 年度评选</p>
    <div class="event-countdown">
      <div class="cd-item"><span class="cd-num">15</span><span class="cd-label">天后</span></div>
      <div class="cd-item"><span class="cd-num">—</span><span class="cd-label">夏季 Cos 大赛</span></div>
      <div class="cd-item"><span class="cd-num">32</span><span class="cd-label">天后</span></div>
      <div class="cd-item"><span class="cd-num">—</span><span class="cd-label">龙奕学园祭</span></div>
    </div>
  </div>

  <div style="padding:0 30px 20px"><div class="sec-title"><span class="st-icon" style="font-size:1.6rem">📅</span> 即将举行的活动</div></div>
  <div class="card-grid2" id="upcomingEvents"></div>

  <div style="padding:0 30px"><div class="sec-title"><span class="st-icon" style="font-size:1.6rem">🔥</span> 进行中的活动</div></div>
  <div class="card-grid2" id="ongoingEvents"></div>

  <div style="padding:0 30px"><div class="sec-title"><span class="st-icon" style="font-size:1.6rem">🏆</span> 往期精彩回顾</div></div>
  <div class="card-grid2" id="pastEvents"></div>
</div>
<script src="assets/particles.js"></script>
<script src="assets/three-engine-v3.js"></script>
<script src="assets/effects-runtime.js"></script>
<script src="assets/nav.js"></script>
<script>
const events=[{t:'2024夏季Cosplay大赛',d:'全国最大的Cosplay线上+线下联动赛事，总奖金池50万元。分设Cos走秀、道具制作、数字人Cos三大赛道。',s:'upcoming',dt:'2024.07.15 - 08.30',l:'pages/events/contest.html',c:'linear-gradient(135deg,#f97316,#ec4899)',icon:'🏆',p:'2,341人已报名'},{t:'龙奕学园祭 · 夏日盛典',d:'元宇宙虚拟学园祭！在龙墟世界中畅游摊贩、游戏、表演、烟花大会。无需出门即可体验最纯正的学园祭氛围。',s:'upcoming',dt:'2024.08.01 - 08.03',l:'pages/events/festival.html',c:'linear-gradient(135deg,#8b5cf6,#ec4899)',icon:'🎆',p:'5,892人预约'},{t:'虚拟演唱会 · 星海之约',d:'与知名Vtuber和虚拟偶像同台！AI实时驱动、AR特效渲染、360°自由视角沉浸式观看。',s:'ongoing',dt:'2024.06.20 - 07.05',l:'pages/events/live-show.html',c:'linear-gradient(135deg,#06b6d4,#6366f1)',icon:'🎤',p:'演出中'},{t:'Cos道具制作研习营',d:'线下+线上混合工作坊，由资深道具师教授锻造、3D打印、涂装全流程。限额200人。',s:'upcoming',dt:'2024.07.20 - 07.22',l:'pages/events/meetup.html',c:'linear-gradient(135deg,#22c55e,#14b8a6)',icon:'🔧',p:'168人已报名'},{t:'线上ACG艺术展',d:'元宇宙虚拟画廊 · 展出原创插画、同人漫画、3D建模作品。观众可在虚拟空间中漫步观赏。',s:'ongoing',dt:'2024.06.15 - 07.15',l:'pages/events/exhibition.html',c:'linear-gradient(135deg,#a78bfa,#ec4899)',icon:'🎨',p:'展出中'},{t:'声优见面会 · 龙奕专场',d:'邀请人气声优进行线上见面会，AI实时翻译，全球粉丝同步参与Q&A互动和签名环节。',s:'upcoming',dt:'2024.08.10',l:'pages/events/con.html',c:'linear-gradient(135deg,#f59e0b,#ef4444)',icon:'🎙️',p:'3,456人预约'},{t:'2024元旦烟花大会',d:'元宇宙跨年烟花大会，数千架数字烟花同步绽放，3D环绕声景，万人同时在线狂欢。',s:'past',dt:'2024.01.01',l:'pages/events/fireworks.html',c:'linear-gradient(135deg,#1e1b4b,#312e81)',icon:'🎇',p:'12万人参与'},{t:'年度Cosplay大赏',d:'2023年度最佳Cos作品评选，专业评审团+全民投票，涵盖最佳还原、最佳创意、最佳数字人等多个奖项。',s:'past',dt:'2023.12.30',l:'pages/events/award.html',c:'linear-gradient(135deg,#fbbf24,#d97706)',icon:'🥇',p:'8万人投票'}];
['upcomingEvents','ongoingEvents','pastEvents'].forEach(id=>{const el=document.getElementById(id);if(!el)return;const list=events.filter(e=>id==='upcomingEvents'?e.s==='upcoming':id==='ongoingEvents'?e.s==='ongoing':e.s==='past');el.innerHTML=list.map(e=>`<a href="${e.l}" class="ev-card"><div class="ev-header"><div class="ev-header-inner" style="background:${e.c}">${e.icon}</div><span class="ev-date-badge">${e.dt}</span><span class="ev-status ${e.s}">${e.s==='upcoming'?'即将开始':e.s==='ongoing'?'进行中':'已结束'}</span></div><div class="ev-body"><div class="ev-title">${e.t}</div><div class="ev-desc">${e.d}</div><div class="ev-footer"><span>${e.p}</span><span style="color:var(--accent)">查看详情 →</span></div></div></a>`).join('')});
</script>
</body>
</html>'''

# ======================================================================
# 3. wiki.html — 百科书院 (3D: academy, theme: lavender-academy)
# ======================================================================
wiki_html = '''<!DOCTYPE html>
<html lang="zh-CN" data-3d="academy">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>百科书院 | 龙奕学院 LongYi Academy</title>
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="assets/themes/academy/lavender-academy.css">
<link rel="stylesheet" href="assets/effects-layer.css">
<style>
.page-container{position:relative;z-index:1;padding-top:80px;max-width:1300px;margin:0 auto}
.wiki-hero{position:relative;padding:50px 30px 30px;text-align:center}
.wiki-hero h1{font-size:2.8rem;font-weight:900;background:linear-gradient(135deg,#a78bfa,#7c3aed,#6366f1);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.wiki-hero p{font-size:1.05rem;color:var(--text-secondary);max-width:550px;margin:10px auto 0}
.wiki-search{max-width:500px;margin:20px auto;display:flex;gap:8px;position:relative;z-index:1}
.wiki-search input{flex:1;padding:14px 20px;border:2px solid var(--border);border-radius:28px;background:var(--bg-card);color:var(--text);font-size:.95rem;outline:none;transition:all .3s}
.wiki-search input:focus{border-color:var(--accent);box-shadow:0 0 24px rgba(167,139,250,.25)}
.wiki-search button{padding:14px 28px;background:var(--gradient-btn);border:none;border-radius:28px;color:#fff;font-weight:700;cursor:pointer;font-size:.95rem;transition:all .3s}
.wiki-search button:hover{transform:scale(1.05);box-shadow:0 6px 24px rgba(167,139,250,.4)}
.cat-row{display:grid;grid-template-columns:repeat(7,1fr);gap:12px;padding:0 30px 30px}
.cat-card{background:var(--bg-card);border-radius:16px;padding:20px 12px;text-align:center;border:1px solid var(--border);transition:all .3s;cursor:pointer;text-decoration:none;color:inherit}
.cat-card:hover{transform:translateY(-4px);box-shadow:0 10px 32px rgba(167,139,250,.2);border-color:var(--accent)}
.cat-card .cc-icon{font-size:2rem;display:block;margin-bottom:6px}
.cat-card .cc-name{font-weight:700;font-size:.85rem}
.wiki-list{padding:0 30px 20px;display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
.wiki-article{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:20px;transition:all .3s;cursor:pointer;text-decoration:none;color:inherit;display:flex;gap:16px}
.wiki-article:hover{transform:translateX(4px);border-color:var(--accent);box-shadow:0 6px 24px rgba(167,139,250,.15)}
.wiki-article .wa-thumb{width:80px;height:80px;border-radius:12px;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:2.5rem}
.wiki-article .wa-info{flex:1;min-width:0}
.wiki-article .wa-title{font-weight:700;font-size:.95rem;margin-bottom:4px}
.wiki-article .wa-desc{font-size:.78rem;color:var(--text-secondary);line-height:1.5;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.wiki-article .wa-meta{font-size:.72rem;color:var(--text-dim);margin-top:8px}
.timeline-strip{display:flex;gap:0;overflow-x:auto;padding:0 30px 30px}
.tl-item{flex:0 0 180px;background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:18px;text-align:center;transition:all .3s;cursor:pointer;text-decoration:none;color:inherit;margin-right:14px}
.tl-item:hover{transform:translateY(-4px);box-shadow:0 10px 30px rgba(167,139,250,.2)}
.tl-year{font-size:1.4rem;font-weight:900;color:var(--accent)}
.tl-title{font-size:.82rem;font-weight:600;margin:8px 0}
.tl-desc{font-size:.72rem;color:var(--text-dim)}
@media(max-width:768px){.cat-row{grid-template-columns:repeat(4,1fr)}.wiki-list{grid-template-columns:1fr}.wiki-hero h1{font-size:2rem}}
</style>
</head>
<body>
<div id="nav-placeholder"></div>
<div class="page-container">
  <div class="wiki-hero">
    <h1>📖 百科书院</h1>
    <p>这里是二次元世界的知识中枢——从Cos维基到动画编年史，从角色图鉴到声优资料，一切尽在其中。</p>
    <div class="wiki-search"><input type="text" placeholder="搜索百科内容... 角色/声优/动画/术语"><button>🔍 搜索</button></div>
  </div>

  <div class="cat-row">
    <a href="pages/wiki/index.html" class="cat-card"><span class="cc-icon">📚</span><span class="cc-name">Cos维基</span></a>
    <a href="pages/wiki/timeline.html" class="cat-card"><span class="cc-icon">📅</span><span class="cc-name">编年史</span></a>
    <a href="pages/wiki/characters.html" class="cat-card"><span class="cc-icon">🎭</span><span class="cc-name">角色图鉴</span></a>
    <a href="pages/wiki/studios.html" class="cat-card"><span class="cc-icon">🏢</span><span class="cc-name">动画公司</span></a>
    <a href="pages/wiki/seiyuu.html" class="cat-card"><span class="cc-icon">🎙️</span><span class="cc-name">声优图鉴</span></a>
    <a href="pages/wiki/glossary.html" class="cat-card"><span class="cc-icon">📝</span><span class="cc-name">术语词典</span></a>
    <a href="pages/wiki/article.html" class="cat-card"><span class="cc-icon">📄</span><span class="cc-name">知识文章</span></a>
  </div>

  <div style="padding:0 30px"><div class="sec-title"><span style="font-size:1.6rem">🔥</span> 热门百科文章</div></div>
  <div class="wiki-list">
    <a href="pages/wiki/article.html" class="wiki-article"><div class="wa-thumb" style="background:linear-gradient(135deg,#7c3aed,#a78bfa)">🎭</div><div class="wa-info"><div class="wa-title">Cosplay入门完全指南：从选角到出片</div><div class="wa-desc">覆盖角色选择、服装制作、道具打造、化妆技巧、摄影构图、后期修图的完整Cosplay流程指南。</div><div class="wa-meta">📖 12,847阅读 · ⭐ 4.9 · 2024.06.15更新</div></div></a>
    <a href="pages/wiki/article.html" class="wiki-article"><div class="wa-thumb" style="background:linear-gradient(135deg,#6366f1,#22d3ee)">🌟</div><div class="wa-info"><div class="wa-title">数字人Cosplay革命：AI如何改变Cos圈</div><div class="wa-desc">深度解析AI生成、动作捕捉、实时渲染三大技术如何赋能Cosplay，让虚拟与现实完美融合。</div><div class="wa-meta">📖 9,234阅读 · ⭐ 4.8 · 2024.06.10更新</div></div></a>
    <a href="pages/wiki/article.html" class="wiki-article"><div class="wa-thumb" style="background:linear-gradient(135deg,#ec4899,#f97316)">⚔️</div><div class="wa-info"><div class="wa-title">武器道具制作终极教程：从设计图到成品</div><div class="wa-desc">EVA发泡板、PVC管、3D打印——详细对比各种材料优劣，附完整制作流程和涂装技巧。</div><div class="wa-meta">📖 7,891阅读 · ⭐ 4.7 · 2024.05.28更新</div></div></a>
    <a href="pages/wiki/article.html" class="wiki-article"><div class="wa-thumb" style="background:linear-gradient(135deg,#22c55e,#14b8a6)">📸</div><div class="wa-info"><div class="wa-title">Cos摄影布光圣经：从单灯到多灯全攻略</div><div class="wa-desc">自然光VS棚拍、Rembrandt光、蝴蝶光、边缘光——手把手教你用光线塑造角色氛围。</div><div class="wa-meta">📖 6,543阅读 · ⭐ 4.6 · 2024.05.20更新</div></div></a>
  </div>

  <div style="padding:0 30px"><div class="sec-title" style="margin-bottom:14px"><span style="font-size:1.6rem">📅</span> 动画编年史</div></div>
  <div class="timeline-strip">
    <a href="pages/wiki/timeline.html" class="tl-item"><div class="tl-year">1963</div><div class="tl-title">铁臂阿童木</div><div class="tl-desc">日本TV动画元年</div></a>
    <div class="tl-item"><div class="tl-year">1979</div><div class="tl-title">机动战士高达</div><div class="tl-desc">真实系机器人开山</div></div>
    <div class="tl-item"><div class="tl-year">1995</div><div class="tl-title">EVA</div><div class="tl-desc">颠覆性叙事革命</div></div>
    <div class="tl-item"><div class="tl-year">1998</div><div class="tl-title">星际牛仔</div><div class="tl-desc">太空爵士诗篇</div></div>
    <div class="tl-item"><div class="tl-year">2006</div><div class="tl-title">凉宫春日</div><div class="tl-desc">轻改动画浪潮</div></div>
    <div class="tl-item"><div class="tl-year">2011</div><div class="tl-title">魔法少女小圆</div><div class="tl-desc">颠覆魔法少女</div></div>
    <div class="tl-item"><div class="tl-year">2016</div><div class="tl-title">你的名字。</div><div class="tl-desc">新海诚现象级</div></div>
    <div class="tl-item"><div class="tl-year">2020</div><div class="tl-title">鬼灭之刃</div><div class="tl-desc">剧场版历史纪录</div></div>
    <a href="pages/wiki/timeline.html" class="tl-item" style="background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center"><div><span style="font-size:2rem">→</span><div style="font-weight:700">查看完整编年史</div></div></a>
  </div>
</div>
<script src="assets/particles.js"></script>
<script src="assets/three-engine-v3.js"></script>
<script src="assets/effects-runtime.js"></script>
<script src="assets/nav.js"></script>
</body>
</html>'''

# ======================================================================
# 4. creator.html — 创作学院 (3D: default, theme: sky-academy)
# ======================================================================
creator_html = '''<!DOCTYPE html>
<html lang="zh-CN" data-3d="default">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>创作学院 | 龙奕学院 LongYi Academy</title>
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="assets/themes/academy/sky-academy.css">
<link rel="stylesheet" href="assets/effects-layer.css">
<style>
.page-container{position:relative;z-index:1;padding-top:80px;max-width:1300px;margin:0 auto}
.cr-hero{position:relative;padding:60px 30px 40px;text-align:center;overflow:hidden}
.cr-hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 40% 30%,rgba(59,130,246,.12),transparent 60%),radial-gradient(ellipse at 60% 70%,rgba(6,182,212,.08),transparent 60%);pointer-events:none}
.cr-hero h1{font-size:3rem;font-weight:900;background:linear-gradient(135deg,#3b82f6,#06b6d4,#6366f1);-webkit-background-clip:text;-webkit-text-fill-color:transparent;position:relative;z-index:1}
.cr-hero p{font-size:1.1rem;color:var(--text-secondary);max-width:650px;margin:12px auto 0;position:relative;z-index:1}
.creator-dashboard{display:grid;grid-template-columns:2fr 1fr;gap:18px;padding:0 30px 30px}
.cd-main{display:flex;flex-direction:column;gap:18px}
.cd-stat-row{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.cd-stat{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:22px;text-align:center}
.cd-stat .cds-num{font-size:2rem;font-weight:900;color:var(--accent);display:block}
.cd-stat .cds-label{font-size:.78rem;color:var(--text-dim);margin-top:4px}
.cd-stat .cds-trend{font-size:.72rem;margin-top:4px}
.cd-stat .cds-trend.up{color:#22c55e}.cd-stat .cds-trend.down{color:#ef4444}
.cd-tools{background:var(--bg-card);border:1px solid var(--border);border-radius:18px;padding:24px}
.cd-tools h2{font-size:1.1rem;margin-bottom:16px}
.tool-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.tool-item{text-align:center;padding:16px 10px;border-radius:14px;border:1px solid var(--border);transition:all .3s;cursor:pointer;text-decoration:none;color:inherit}
.tool-item:hover{transform:translateY(-3px);box-shadow:0 8px 28px rgba(59,130,246,.15);border-color:var(--accent)}
.tool-item .ti-icon{font-size:2rem;display:block;margin-bottom:6px}
.tool-item .ti-name{font-weight:600;font-size:.82rem}
.cd-side{display:flex;flex-direction:column;gap:18px}
.cd-side-card{background:var(--bg-card);border:1px solid var(--border);border-radius:18px;padding:24px}
.cd-side-card h3{font-size:.95rem;margin-bottom:14px}
.trend-list{display:flex;flex-direction:column;gap:10px}
.trend-item{display:flex;align-items:center;gap:10px;padding:10px;border-radius:12px;transition:all .3s;cursor:pointer;text-decoration:none;color:inherit}
.trend-item:hover{background:var(--bg-secondary)}
.trend-item .tr-rank{font-weight:900;font-size:1rem;width:24px;text-align:center;color:var(--accent)}
.trend-item .tr-info{flex:1;min-width:0}
.trend-item .tr-name{font-weight:600;font-size:.82rem}
.trend-item .tr-meta{font-size:.72rem;color:var(--text-dim)}
.collab-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;padding:0 30px 30px}
.collab-card{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:20px;text-align:center;transition:all .3s;cursor:pointer;text-decoration:none;color:inherit}
.collab-card:hover{transform:translateY(-4px);box-shadow:0 12px 32px rgba(59,130,246,.15)}
.collab-card .cb-icon{font-size:2.5rem;display:block;margin-bottom:10px}
.collab-card .cb-title{font-weight:700;font-size:.95rem;margin-bottom:4px}
.collab-card .cb-desc{font-size:.78rem;color:var(--text-dim);line-height:1.5}
@media(max-width:768px){.cr-hero h1{font-size:2rem}.creator-dashboard,.cd-stat-row{grid-template-columns:1fr}.tool-grid{grid-template-columns:repeat(2,1fr)}.collab-grid{grid-template-columns:1fr}}
</style>
</head>
<body>
<div id="nav-placeholder"></div>
<div class="page-container">
  <div class="cr-hero">
    <h1>🎨 创作学院</h1>
    <p>一站式创作平台——AI辅助创作工具、版权管理、收益变现、粉丝互动、协作广场，让你的创作才华绽放光芒。</p>
  </div>

  <div class="creator-dashboard">
    <div class="cd-main">
      <div class="cd-stat-row">
        <div class="cd-stat"><span class="cds-num">128</span><span class="cds-label">我的作品</span><span class="cds-trend up">↑ 12% 本月</span></div>
        <div class="cd-stat"><span class="cds-num">8.9万</span><span class="cds-label">累计播放</span><span class="cds-trend up">↑ 23% 本月</span></div>
        <div class="cd-stat"><span class="cds-num">¥4,280</span><span class="cds-label">创作收益</span><span class="cds-trend up">↑ 15% 本月</span></div>
        <div class="cd-stat"><span class="cds-num">3,456</span><span class="cds-label">粉丝数</span><span class="cds-trend up">↑ 8% 本月</span></div>
      </div>
      <div class="cd-tools"><h2>🛠️ AI创作工具套件</h2><div class="tool-grid"><a href="pages/creator/workshop.html" class="tool-item"><span class="ti-icon">🎨</span><span class="ti-name">AI绘画</span></a><a href="pages/creator/workshop.html" class="tool-item"><span class="ti-icon">✂️</span><span class="ti-name">视频剪辑</span></a><a href="pages/creator/workshop.html" class="tool-item"><span class="ti-icon">🎵</span><span class="ti-name">音频处理</span></a><a href="pages/creator/workshop.html" class="tool-item"><span class="ti-icon">🎬</span><span class="ti-name">3D建模</span></a><a href="pages/creator/tools.html" class="tool-item"><span class="ti-icon">📝</span><span class="ti-name">剧本助手</span></a><a href="pages/creator/tools.html" class="tool-item"><span class="ti-icon">🖼️</span><span class="ti-name">AI修图</span></a><a href="pages/creator/tools.html" class="tool-item"><span class="ti-icon">🎭</span><span class="ti-name">角色设计</span></a><a href="pages/creator/tools.html" class="tool-item"><span class="ti-icon">📊</span><span class="ti-name">数据分析</span></a></div></div>
    </div>
    <div class="cd-side">
      <div class="cd-side-card"><h3>🔥 创作趋势</h3><div class="trend-list"><a href="#" class="trend-item"><span class="tr-rank">01</span><div class="tr-info"><div class="tr-name">AI生成Cosplay写真</div><div class="tr-meta">↑ 趋势飙升 280%</div></div></a><a href="#" class="trend-item"><span class="tr-rank">02</span><div class="tr-info"><div class="tr-name">数字人虚拟偶像出道</div><div class="tr-meta">↑ 趋势上升 195%</div></div></a><a href="#" class="trend-item"><span class="tr-rank">03</span><div class="tr-info"><div class="tr-name">元宇宙Cos短剧</div><div class="tr-meta">↑ 趋势上升 167%</div></div></a><a href="#" class="trend-item"><span class="tr-rank">04</span><div class="tr-info"><div class="tr-name">3D打印道具制作</div><div class="tr-meta">↑ 趋势上升 140%</div></div></a><a href="#" class="trend-item"><span class="tr-rank">05</span><div class="tr-info"><div class="tr-name">AR实时Cos滤镜</div><div class="tr-meta">↑ 趋势上升 122%</div></div></a></div></div>
      <div class="cd-side-card"><h3>📢 创作者公告</h3><div style="font-size:.82rem;color:var(--text-secondary);line-height:1.6">• 夏季创作激励计划开启，总奖金池100万元<br>• 新上线AI配音工具，支持50+语言<br>• 版权保护系统升级至v3.0<br>• 创作者等级体系上线，解锁更多权益</div></div>
    </div>
  </div>

  <div style="padding:0 30px"><div class="sec-title"><span style="font-size:1.6rem">🤝</span> 协作广场</div></div>
  <div class="collab-grid">
    <a href="pages/creator/collab.html" class="collab-card"><span class="cb-icon">🎬</span><div class="cb-title">寻找摄影师</div><div class="cb-desc">在你的城市找到专业Cos摄影师</div></a>
    <a href="pages/creator/collab.html" class="collab-card"><span class="cb-icon">👗</span><div class="cb-title">服装定制师</div><div class="cb-desc">一对一专属Cos服装定制</div></a>
    <a href="pages/creator/collab.html" class="collab-card"><span class="cb-icon">🖌️</span><div class="cb-title">后期修图师</div><div class="cb-desc">专业后期处理与特效合成</div></a>
    <a href="pages/creator/collab.html" class="collab-card"><span class="cb-icon">🗡️</span><div class="cb-title">道具工作室</div><div class="cb-desc">3D打印与手工锻造道具</div></a>
    <a href="pages/creator/collab.html" class="collab-card"><span class="cb-icon">💄</span><div class="cb-title">特效化妆师</div><div class="cb-desc">伤妆、科幻妆、奇幻妆</div></a>
    <a href="pages/creator/collab.html" class="collab-card"><span class="cb-icon">🎤</span><div class="cb-title">配音工作室</div><div class="cb-desc">角色配音与音效制作</div></a>
  </div>

  <div style="padding:0 30px 30px"><div class="sec-title"><span style="font-size:1.6rem">💎</span> 收益管理</div><div style="display:flex;gap:18px;flex-wrap:wrap"><a href="pages/creator/income.html" style="flex:1;min-width:200px;background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:24px;text-decoration:none;color:inherit;transition:all .3s" onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 12px 32px rgba(59,130,246,.15)'" onmouseout="this.style.transform='';this.style.boxShadow=''"><div style="font-size:2rem;margin-bottom:8px">💰</div><div style="font-weight:700;margin-bottom:4px">创作收益</div><div style="font-size:.78rem;color:var(--text-dim)">打赏 · 分成 · 广告</div></a><a href="pages/creator/fans.html" style="flex:1;min-width:200px;background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:24px;text-decoration:none;color:inherit;transition:all .3s" onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 12px 32px rgba(59,130,246,.15)'" onmouseout="this.style.transform='';this.style.boxShadow=''"><div style="font-size:2rem;margin-bottom:8px">👥</div><div style="font-weight:700;margin-bottom:4px">粉丝管理</div><div style="font-size:.78rem;color:var(--text-dim)">数据分析 · 粉丝画像</div></a><a href="pages/creator/dashboard.html" style="flex:1;min-width:200px;background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:24px;text-decoration:none;color:inherit;transition:all .3s" onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 12px 32px rgba(59,130,246,.15)'" onmouseout="this.style.transform='';this.style.boxShadow=''"><div style="font-size:2rem;margin-bottom:8px">📊</div><div style="font-weight:700;margin-bottom:4px">创作仪表盘</div><div style="font-size:.78rem;color:var(--text-dim)">全维度数据总览</div></a></div></div>
</div>
<script src="assets/particles.js"></script>
<script src="assets/three-engine-v3.js"></script>
<script src="assets/effects-runtime.js"></script>
<script src="assets/nav.js"></script>
</body>
</html>'''

# Write all 4 files
pages = {
    'anime.html': anime_html,
    'events.html': events_html,
    'wiki.html': wiki_html,
    'creator.html': creator_html,
}

for filename, content in pages.items():
    path = os.path.join(BASE, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'✓ {filename} ({len(content)} chars)')

print(f'\nDone! 4 module homepages created.')

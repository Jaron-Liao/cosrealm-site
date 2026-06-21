// ===== Nav Injector v7.0 — 内联 HTML + CSS 到每个页面 =====
// 将导航栏的 HTML 和 CSS 直接写入每个 .html 文件的 </head> 前
// 不再依赖 JS 动态生成，确保 100% 可见

const fs = require('fs');
const path = require('path');

// ===== 导航内联 CSS =====
const NAV_CSS = `
/* === LongYi Nav v7 — 嵌入式 === */
.ly-nav-wrap { position: fixed; top: 0; left: 0; right: 0; z-index: 99999; }
.ly-nav {
  background: rgba(10,10,26,0.95); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(255,107,53,0.3); box-shadow: 0 2px 20px rgba(0,0,0,0.6);
  font-family: -apple-system, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
}
.ly-nav-inner { max-width: 1300px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; padding: 0 16px; height: 52px; }
.ly-brand { display: flex; align-items: center; gap: 6px; text-decoration: none; flex-shrink: 0; margin-right: 16px; }
.ly-brand-icon { font-size: 1.3rem; }
.ly-brand-text { color: #FF6B35; font-weight: 800; font-size: 1rem; letter-spacing: 1px; }
.ly-brand-sub { color: #555; font-size: 0.6rem; margin-left: 4px; }

/* 九宫格导航 */
.ly-menu { display: flex; align-items: center; gap: 2px; flex: 1; justify-content: center; overflow-x: auto; }
.ly-menu::-webkit-scrollbar { display: none; }
.ly-acc { position: relative; /* dropdown container */ }
.ly-acc-head {
  display: flex; align-items: center; gap: 4px;
  padding: 8px 13px; border-radius: 8px;
  color: #ccc; font-size: 0.85rem; font-weight: 600; cursor: pointer;
  text-decoration: none; white-space: nowrap; transition: all 0.2s;
  user-select: none; border: none; background: transparent;
}
.ly-acc-head:hover { color: #FF6B35; background: rgba(255,107,53,0.12); transform: translateY(-1px); }
.ly-acc:hover > .ly-acc-head { color: #FF6B35; }

/* 下拉菜单 */
.ly-drop {
  display: none; position: absolute; top: 100%; left: 50%; transform: translateX(-50%);
  min-width: 200px; background: rgba(14,14,35,0.98);
  border: 1px solid rgba(255,107,53,0.25); border-radius: 12px;
  padding: 8px; margin-top: 4px;
  box-shadow: 0 12px 48px rgba(0,0,0,0.7), 0 0 30px rgba(255,107,53,0.08);
  z-index: 100000;
}
.ly-acc:hover > .ly-drop { display: block !important; animation: lyFadeIn 0.15s ease; }
@keyframes lyFadeIn { from{opacity:0;transform:translateX(-50%) translateY(-8px)} to{opacity:1;transform:translateX(-50%) translateY(0)} }

.ly-drop a {
  display: block; padding: 9px 14px; border-radius: 8px;
  color: #aaa; text-decoration: none; font-size: 0.82rem;
  transition: all 0.15s; white-space: nowrap;
}
.ly-drop a:hover { background: rgba(255,107,53,0.15); color: #FF6B35; padding-left: 18px; }
.ly-drop a.ly-cur { color: #FF6B35; background: rgba(255,107,53,0.08); font-weight: 600; }
.ly-drop-sep { height: 1px; background: rgba(255,255,255,0.06); margin: 4px 8px; }

/* 右侧按钮 */
.ly-actions { display: flex; align-items: center; gap: 6px; flex-shrink: 0; }
.ly-btn {
  padding: 5px 12px; border-radius: 8px; font-size: 0.8rem;
  color: #ccc; text-decoration: none; border: 1px solid rgba(255,255,255,0.12);
  background: rgba(255,255,255,0.04); cursor: pointer; transition: all 0.2s;
}
.ly-btn:hover { border-color: #FF6B35; color: #FF6B35; }
.ly-tbtn {
  width: 34px; height: 34px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.1);
  color: #ccc; font-size: 1rem; cursor: pointer; transition: all 0.2s;
}
.ly-tbtn:hover { background: rgba(255,107,53,0.2); color: #FF6B35; transform: rotate(15deg); }
.ly-spacer { height: 52px; }

/* 移动端 */
@media(max-width:900px){
  .ly-menu{display:none;position:fixed;top:52px;left:0;right:0;flex-direction:column;background:rgba(10,10,26,0.99);border-bottom:1px solid rgba(255,107,53,0.2);padding:12px;gap:2px;z-index:99998;max-height:calc(100vh-52px);overflow-y:auto}
  .ly-menu.ly-open{display:flex}
  .ly-drop{position:static;transform:none;display:none!important;box-shadow:none;border:none;background:rgba(255,255,255,0.03);margin-top:0;padding-left:16px;border-radius:0}
  .ly-acc.ly-open>.ly-drop{display:block!important}
  .ly-ham{display:block;background:none;border:none;color:#ccc;font-size:1.4rem;cursor:pointer;padding:4px 8px}
}
@media(min-width:901px){.ly-ham{display:none}}
`;

// ===== 导航 HTML 模板（用 __PREFIX__ 占位符） =====
function getNavHTML(prefix) {
  return `<div class="ly-nav-wrap"><nav class="ly-nav" id="mainNav">
<div class="ly-nav-inner">
<a href="${prefix}index.html" class="ly-brand">
<span class="ly-brand-icon">🐉</span><span class="ly-brand-text">龙墟</span><span class="ly-brand-sub">CosRealm</span>
</a>
<div class="ly-menu" id="lyMenu">

<!-- 番剧 -->
<div class="ly-acc">
<button class="ly-acc-head">📺 番剧</button>
<div class="ly-drop">
<a href="${prefix}anime.html">🏠 番剧首页</a><a href="${prefix}pages/anime/index.html">番剧大厅</a><div class="ly-drop-sep"></div>
<a href="${prefix}pages/anime/player.html">▶ 播放器</a><a href="${prefix}pages/anime/bangumi.html">📅 新番时间表</a><a href="${prefix}pages/anime/ranking.html">🏆 排行榜</a><div class="ly-drop-sep"></div>
<a href="${prefix}pages/anime/mad.html">🎬 MAD创作</a><a href="${prefix}pages/anime/library.html">📚 动画图书馆</a><a href="${prefix}pages/anime/live.html">📡 直播</a><a href="${prefix}pages/anime/upload.html">📤 投稿上传</a></div></div>

<!-- 羁绊 -->
<div class="ly-acc">
<button class="ly-acc-head">💬 羁绊</button>
<div class="ly-drop">
<a href="${prefix}social.html">🏠 社交首页</a><a href="${prefix}pages/social/feed.html">📜 社区动态</a><div class="ly-drop-sep"></div>
<a href="${prefix}pages/social/create.html">✏️ 发布创作</a><a href="${prefix}pages/social/profile.html">👤 个人主页</a><a href="${prefix}pages/social/gallery.html">🖼️ Cos画廊</a><div class="ly-drop-sep"></div>
<a href="${prefix}pages/social/messages.html">💬 私信</a><a href="${prefix}pages/social/club.html">🏛️ 社团圈子</a><a href="${prefix}pages/social/bbs.html">📋 论坛BBS</a><a href="${prefix}pages/social/match.html">💕 同好匹配</a><a href="${prefix}pages/social/live-room.html">📡 虚拟直播</a><a href="${prefix}pages/social/ai-identify.html">🔍 AI识图</a></div></div>

<!-- 商贸 -->
<div class="ly-acc">
<button class="ly-acc-head">🛒 商贸</button>
<div class="ly-drop">
<a href="${prefix}shop.html">🏠 商城首页</a><a href="${prefix}pages/shop/browse.html">🛍️ 商品浏览</a><div class="ly-drop-sep"></div>
<a href="${prefix}pages/shop/detail.html">📋 商品详情</a><a href="${prefix}pages/shop/cart.html">🛒 购物车</a><a href="${prefix}pages/shop/seller.html">🏪 卖家中心</a><div class="ly-drop-sep"></div>
<a href="${prefix}pages/shop/recommend.html">🤖 AI推荐</a><a href="${prefix}pages/shop/flash.html">⚡ 限时抢购</a><a href="${prefix}pages/shop/secondhand.html">♻️ 二手交易</a><a href="${prefix}pages/shop/custom.html">🔧 定制工坊</a><a href="${prefix}pages/shop/rental.html">👗 Cos租赁</a><a href="${prefix}pages/shop/points.html">💎 积分商城</a></div></div>

<!-- 虚空 -->
<div class="ly-acc">
<button class="ly-acc-head">🌌 虚空</button>
<div class="ly-drop">
<a href="${prefix}metaverse.html">🏠 世界入口</a><a href="${prefix}pages/metaverse/explore.html">🔭 空间探索</a><div class="ly-drop-sep"></div>
<a href="${prefix}pages/metaverse/avatar.html">🧘 虚拟化身</a><a href="${prefix}pages/metaverse/worlds.html">🌍 主题世界</a><a href="${prefix}pages/metaverse/realm.html">🚪 异世界门</a><div class="ly-drop-sep"></div>
<a href="${prefix}pages/metaverse/live.html">🎵 现场活动</a><a href="${prefix}pages/metaverse/social.html">👥 元宇宙社交</a><a href="${prefix}pages/metaverse/builder.html">🏗️ 世界建造</a><a href="${prefix}pages/metaverse/city.html">🏙️ 虚拟城市</a><a href="${prefix}pages/metaverse/combat.html">⚔️ 竞技场</a><a href="${prefix}pages/metaverse/guild.html">⚔️ 公会</a><a href="${prefix}pages/metaverse/trade.html">💰 交易所</a><a href="${prefix}pages/metaverse/pets.html">🐾 使魔养成</a><a href="${prefix}pages/metaverse/fashion.html">👗 时装秀</a><a href="${prefix}pages/metaverse/airship.html">✈️ 飞空艇</a></div></div>

<!-- 创作 -->
<div class="ly-acc">
<button class="ly-acc-head">🎨 创作</button>
<div class="ly-drop">
<a href="${prefix}creator.html">🏠 创作首页</a><a href="${prefix}pages/creator/dashboard.html">📊 创作仪表盘</a><div class="ly-drop-sep"></div>
<a href="${prefix}pages/creator/workshop.html">🔨 创作工坊</a><a href="${prefix}pages/creator/collab.html">🤝 协作广场</a><a href="${prefix}pages/creator/income.html">💰 创作收益</a><a href="${prefix}pages/creator/fans.html">❤️ 粉丝管理</a><a href="${prefix}pages/creator/tools.html">🛠️ 创作工具箱</a></div></div>

<!-- 幻影/数字人 -->
<div class="ly-acc">
<button class="ly-acc-head">🤖 幻影</button>
<div class="ly-drop">
<a href="${prefix}digital-human.html">🏠 数字人首页</a><a href="${prefix}pages/digital-human/showroom.html">🎭 数字人展馆</a><div class="ly-drop-sep"></div>
<a href="${prefix}pages/digital-human/studio.html">🎬 Studio影棚</a><a href="${prefix}pages/digital-human/animate.html">🎬 动画实验室</a><a href="${prefix}pages/digital-human/livecast.html">📡 虚拟直播</a><a href="${prefix}pages/digital-human/voice.html">🎙️ 语音合成</a><div class="ly-drop-sep"></div>
<a href="${prefix}pages/digital-human/ai-chat.html">💬 AI角色对话</a><a href="${prefix}pages/digital-human/motion.html">🎯 动作捕捉</a><a href="${prefix}pages/digital-human/clone.html">👤 数字分身</a><a href="${prefix}pages/digital-human/scene.html">🎬 场景工坊</a><a href="${prefix}pages/digital-human/emotion.html">😊 情感引擎</a><div class="ly-drop-sep"></div>
<a href="${prefix}pages/digital-human/dressup.html">👗 3D换装工坊 ⭐</a><a href="${prefix}pages/digital-human/llm-interactive.html">🤖 LLM互动 ⭐</a></div></div>

<!-- 研修 -->
<div class="ly-acc">
<button class="ly-acc-head">🎓 研修</button>
<div class="ly-drop">
<a href="${prefix}academy.html">🏠 学院首页</a><a href="${prefix}pages/academy/courses.html">📖 课程中心</a><div class="ly-drop-sep"></div>
<a href="${prefix}pages/academy/videos.html">🎥 视频教程</a><a href="${prefix}pages/academy/path.html">🛤️ 成长之路</a><a href="${prefix}pages/academy/mentor.html">👨‍🏫 导师发现</a><a href="${prefix}pages/academy/challenge.html">🎯 挑战任务</a><div class="ly-drop-sep"></div>
<a href="${prefix}pages/academy/exam.html">📝 考试系统</a><a href="${prefix}pages/academy/cert.html">🎓 证书认证</a><a href="${prefix}pages/academy/live-class.html">📡 直播课堂</a><a href="${prefix}pages/academy/ranking.html">🏆 学霸排行</a><a href="${prefix}pages/academy/library.html">📚 资料馆</a></div></div>

<!-- 祭典 -->
<div class="ly-acc">
<button class="ly-acc-head">🎪 祭典</button>
<div class="ly-drop">
<a href="${prefix}events.html">🏠 活动首页</a><a href="${prefix}pages/events/calendar.html">📅 活动日历</a><div class="ly-drop-sep"></div>
<a href="${prefix}events/contest.html">🏆 Cos大赛</a><a href="${prefix}pages/events/con.html">🎪 虚拟漫展</a><a href="${prefix}pages/events/meetup.html">🤝 线下聚会</a><a href="${prefix}pages/events/live-show.html">🎤 虚拟演唱会</a><div class="ly-drop-sep"></div>
<a href="${prefix}pages/events/exhibition.html">🖼️ 线上展览</a><a href="${prefix}pages/events/festival.html">🎊 学园祭</a><a href="${prefix}pages/events/award.html">🏅 年度评选</a><a href="${prefix}pages/events/fireworks.html">🎆 烟花大会</a></div></div>

<!-- 百科 -->
<div class="ly-acc">
<button class="ly-acc-head">📖 百科</button>
<div class="ly-drop">
<a href="${prefix}wiki.html">🏠 百科首页</a><a href="${prefix}pages/wiki/index.html">📚 Cos维基</a><div class="ly-drop-sep"></div>
<a href="${prefix}pages/wiki/article.html">📄 知识文章</a><a href="${prefix}pages/wiki/glossary.html">📖 术语词典</a><a href="${prefix}pages/wiki/timeline.html">⏳ 动漫编年史</a><a href="${prefix}pages/wiki/characters.html">🎭 角色图鉴</a><a href="${prefix}pages/wiki/studios.html">🏢 动画公司</a><a href="${prefix}pages/wiki/seiyuu.html">🎤 声优图鉴</a></div></div>

</div><!-- end lyMenu -->
<div class="ly-actions">
<button class="ly-tbtn" id="lyThemeBtn" title="日/夜间切换">🌓</button>
<a href="${prefix}pages/auth/login-v2.html" class="ly-btn">登录</a>
<a href="${prefix}pages/user/settings.html" class="ly-btn" title="设置">⚙️</a>
<button class="ly-ham" id="lyHam">☰</button>
</div>
</div></nav></div>
<div class="ly-spacer"></div>`;
}

// ===== 导航交互 JS（精简版，只管交互） =====
const NAV_JS = `(function(){
var t=document.getElementById('lyThemeBtn');
if(t)t.addEventListener('click',function(){var r=document.documentElement,d=r.classList.contains('theme-dark');r.classList.remove(d?'theme-dark':'theme-light');r.classList.add(d?'theme-light':'theme-dark');localStorage.setItem('cosrealm-theme',d?'light':'dark')});
var s=localStorage.getItem('cosrealm-theme')||'dark';document.documentElement.classList.add('theme-'+s);
var h=document.getElementById('lyHam');var m=document.getElementById('lyMenu');
if(h&&m){h.addEventListener('click',function(){m.classList.toggle('ly-open');h.textContent=m.classList.contains('ly-open')?'✕':'☰'})}
document.querySelectorAll('.ly-acc-head').forEach(function(el){el.addEventListener('click',function(e){if(window.innerWidth<=900){e.preventDefault();this.parentElement.classList.toggle('ly-open')}})});
document.addEventListener('click',function(e){if(window.innerWidth<=900&&!e.target.closest('.ly-acc')&&!e.target.closest('.ly-ham')){document.querySelectorAll('.ly-acc').forEach(function(a){a.classList.remove('ly-open')});if(m)m.classList.remove('ly-open');if(h)h.textContent='☰'}});
})();`;

// ===== 扫描所有 HTML 文件 =====
function getAllHtmlFiles(dir) {
  let results = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    if (entry.name === 'node_modules' || entry.name === '.git' || entry.name.startsWith('.') || entry.name === 'index-backup') continue;
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      results = results.concat(getAllHtmlFiles(fullPath));
    } else if (entry.name.endsWith('.html')) {
      results.push(fullPath);
    }
  }
  return results;
}

const rootDir = path.resolve(__dirname);
const files = getAllHtmlFiles(rootDir);

let updated = 0;
let skipped = 0;

files.forEach(filePath => {
  const relPath = path.relative(rootDir, filePath).replace(/\\/g, '/');
  
  // 计算前缀路径
  let prefix = '';
  // pages/xxx/yyy.html → ../../
  if (/^pages\/[^\/]+\/.+\.html$/.test(relPath)) {
    prefix = '../../';
  } 
  // extra/xxx.html → ../
  else if (/^extra\/.+\.html$/.test(relPath)) {
    prefix = '../';
  }
  
  let html = fs.readFileSync(filePath, 'utf8');
  
  // 检查是否已有嵌入标记（避免重复注入）
  if (html.includes('<!-- LYNAV_EMBEDDED -->')) {
    skipped++;
    return;
  }
  
  // 生成带正确路径的导航 HTML + CSS + JS
  const cssBlock = '<style>\n/* == LongYi Navigation Embedded == */\n' + NAV_CSS + '\n</style>';
  const navBlock = '<!-- LYNAV_EMBEDDED -->\n' + getNavHTML(prefix);
  const jsBlock = '<script>\n/* == LongYi Nav Interact == */\n' + NAV_JS + '\n</script>';
  
  // 在 </head> 前插入 CSS
  if (html.includes('</head>')) {
    html = html.replace('</head>', cssBlock + '\n</head>');
  } else {
    // 没有 </head> 就在 <body> 或 <html> 后插入
    html = cssBlock + '\n' + html;
  }
  
  // 在 <body> 开头后插入导航 HTML
  if (html.includes('<body')) {
    html = html.replace(/(<body[^>]*>)/, '$1\n' + navBlock);
  } else {
    html = navBlock + '\n' + html;
  }
  
  // 在 </body> 前插入交互 JS（如果没有已有）
  if (!html.includes('lyThemeBtn')) {
    html = html.replace('</body>', jsBlock + '\n</body>');
  }
  
  fs.writeFileSync(filePath, html, 'utf8');
  updated++;
});

console.log(`Done: ${updated} files updated, ${skipped} skipped (already embedded)`);
console.log(`Total HTML files: ${files.length}`);

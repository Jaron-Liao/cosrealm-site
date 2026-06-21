const fs = require('fs');
const path = require('path');

const ROOT = 'C:/Users/28767/Downloads/cosrealm-site';

// 导航 CSS —— 纯 CSS hover 下拉，零 JS 依赖
const NAV_CSS = `<style id="lynav-css">
/* === LongYi Nav v8 — 纯CSS下拉，零JS === */
.lyn-wrap { position: fixed; top: 0; left: 0; right: 0; z-index: 99999; }
.lyn-bar {
  background: rgba(10,10,26,0.96); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(255,107,53,0.3); box-shadow: 0 2px 20px rgba(0,0,0,0.6);
  font-family: -apple-system, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
}
.lyn-inner { max-width: 1300px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; padding: 0 12px; height: 50px; }
.lyn-brand { display: flex; align-items: center; gap: 6px; text-decoration: none; flex-shrink: 0; margin-right: 10px; }
.lyn-brand-icon { font-size: 1.3rem; }
.lyn-brand-text { color: #FF6B35; font-weight: 800; font-size: 0.95rem; letter-spacing: 1px; }
.lyn-brand-sub { color: #555; font-size: 0.6rem; margin-left: 3px; }
.lyn-menu { display: flex; align-items: center; gap: 1px; flex: 1; justify-content: center; overflow-x: auto; }
.lyn-menu::-webkit-scrollbar { display: none; }
/* 下拉容器 */
.lyn-dd { position: relative; }
.lyn-dd-btn {
  display: flex; align-items: center; gap: 4px;
  padding: 7px 11px; border-radius: 8px;
  color: #ccc; font-size: 0.83rem; font-weight: 600; cursor: pointer;
  text-decoration: none; white-space: nowrap; transition: all 0.2s;
  user-select: none; border: none; background: transparent; font-family: inherit;
}
.lyn-dd-btn:hover { color: #FF6B35; background: rgba(255,107,53,0.12); }
.lyn-dd:hover > .lyn-dd-btn { color: #FF6B35; }
/* 下拉菜单 —— 纯 CSS hover 显示 */
.lyn-dd-menu {
  display: none;
  position: absolute; top: 100%; left: 50%; transform: translateX(-50%);
  min-width: 195px; background: rgba(14,14,35,0.99);
  border: 1px solid rgba(255,107,53,0.25); border-radius: 12px;
  padding: 7px; margin-top: 4px;
  box-shadow: 0 12px 48px rgba(0,0,0,0.7), 0 0 30px rgba(255,107,53,0.08);
  z-index: 100000;
}
/* 核心：hover 显示下拉 */
.lyn-dd:hover > .lyn-dd-menu { display: block; animation: lynFadeIn 0.15s ease; }
@keyframes lynFadeIn { from{opacity:0;transform:translateX(-50%) translateY(-6px)} to{opacity:1;transform:translateX(-50%) translateY(0)} }
.lyn-dd-menu a {
  display: block; padding: 8px 13px; border-radius: 8px;
  color: #aaa; text-decoration: none; font-size: 0.81rem; transition: all 0.15s; white-space: nowrap;
}
.lyn-dd-menu a:hover { background: rgba(255,107,53,0.15); color: #FF6B35; padding-left: 17px; }
.lyn-dd-menu a.lyn-cur { color: #FF6B35; background: rgba(255,107,53,0.08); font-weight: 600; }
.lyn-sep { height: 1px; background: rgba(255,255,255,0.06); margin: 4px 8px; }
/* 右侧 */
.lyn-actions { display: flex; align-items: center; gap: 5px; flex-shrink: 0; }
.lyn-btn { padding: 5px 10px; border-radius: 8px; font-size: 0.78rem; color: #ccc; text-decoration: none; border: 1px solid rgba(255,255,255,0.12); background: rgba(255,255,255,0.04); cursor: pointer; transition: all 0.2s; }
.lyn-btn:hover { border-color: #FF6B35; color: #FF6B35; }
.lyn-tbtn { width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.1); color: #ccc; font-size: 0.95rem; cursor: pointer; transition: all 0.2s; }
.lyn-tbtn:hover { background: rgba(255,107,53,0.2); color: #FF6B35; }
.lyn-spacer { height: 50px; }
/* 汉堡菜单按钮 */
.lyn-ham { display: none; background: none; border: none; color: #ccc; font-size: 1.4rem; cursor: pointer; padding: 4px 8px; }
/* 移动端 */
@media(max-width:880px){
  .lyn-menu { display: none; position: fixed; top: 50px; left: 0; right: 0; flex-direction: column; background: rgba(10,10,26,0.995); border-bottom: 1px solid rgba(255,107,53,0.2); padding: 10px; gap: 2px; z-index: 99998; max-height: calc(100vh - 50px); overflow-y: auto; }
  .lyn-menu.lyn-open { display: flex; }
  .lyn-dd-menu { position: static; transform: none; display: none !important; box-shadow: none; border: none; background: rgba(255,255,255,0.03); margin-top: 0; padding-left: 14px; border-radius: 0; }
  .lyn-dd.lyn-open > .lyn-dd-menu { display: block !important; }
  .lyn-ham { display: block; }
}
@media(min-width:881px){ .lyn-ham { display: none; } }
</style>`;

// 导航 HTML —— 根据文件所处目录深度自动计算路径
function makeNavHTML(depth) {
  const p = (rel) => (depth > 0 ? '../'.repeat(depth) + rel : rel);
  return `<div class="lyn-wrap"><nav class="lyn-bar" id="mainNav">
<div class="lyn-inner">
<a href="${p('index.html')}" class="lyn-brand">
<span class="lyn-brand-icon">🐉</span><span class="lyn-brand-text">龙墟</span><span class="lyn-brand-sub">CosRealm</span>
</a>
<button class="lyn-ham" onclick="document.getElementById('lynMenu').classList.toggle('lyn-open')">☰</button>
<div class="lyn-menu" id="lynMenu">

<!-- 番剧 -->
<div class="lyn-dd">
<button class="lyn-dd-btn">📺 番剧 ▾</button>
<div class="lyn-dd-menu">
<a href="${p('anime.html')}">🏠 番剧首页</a>
<a href="${p('pages/anime/index.html')}">番剧大厅</a>
<div class="lyn-sep"></div>
<a href="${p('pages/anime/player.html')}">▶ 播放器</a>
<a href="${p('pages/anime/bangumi.html')}">📅 新番时间表</a>
<a href="${p('pages/anime/ranking.html')}">🏆 排行榜</a>
<div class="lyn-sep"></div>
<a href="${p('pages/anime/mad.html')}">🎬 MAD创作</a>
<a href="${p('pages/anime/library.html')}">📚 动画图书馆</a>
<a href="${p('pages/anime/live.html')}">📡 直播</a>
<a href="${p('pages/anime/upload.html')}">📤 投稿上传</a>
</div></div>

<!-- 羁绊 -->
<div class="lyn-dd">
<button class="lyn-dd-btn">💬 羁绊 ▾</button>
<div class="lyn-dd-menu">
<a href="${p('social.html')}">🏠 社交首页</a>
<a href="${p('pages/social/feed.html')}">📰 社区动态</a>
<div class="lyn-sep"></div>
<a href="${p('pages/social/create.html')}">✏️ 发布创作</a>
<a href="${p('pages/social/profile.html')}">👤 个人主页</a>
<a href="${p('pages/social/gallery.html')}">🖼️ Cos画廊</a>
<div class="lyn-sep"></div>
<a href="${p('pages/social/messages.html')}">💬 私信</a>
<a href="${p('pages/social/club.html')}">🏛️ 社团圈子</a>
<a href="${p('pages/social/bbs.html')}">📋 论坛BBS</a>
<a href="${p('pages/social/match.html')}">💕 同好匹配</a>
<a href="${p('pages/social/live-room.html')}">📡 虚拟直播</a>
<a href="${p('pages/social/ai-identify.html')}">🔍 AI识图</a>
</div></div>

<!-- 商贸 -->
<div class="lyn-dd">
<button class="lyn-dd-btn">🛒 商贸 ▾</button>
<div class="lyn-dd-menu">
<a href="${p('shop.html')}">🏠 商城首页</a>
<a href="${p('pages/shop/index.html')}">商品大厅</a>
<div class="lyn-sep"></div>
<a href="${p('pages/shop/product.html')}">📦 商品详情</a>
<a href="${p('pages/shop/cart.html')}">🛒 购物车</a>
<a href="${p('pages/shop/checkout.html')}">💳 结算</a>
<div class="lyn-sep"></div>
<a href="${p('pages/shop/seller.html')}">🏪 卖家中心</a>
<a href="${p('pages/shop/order.html')}">📋 我的订单</a>
</div></div>

<!-- 书院 -->
<div class="lyn-dd">
<button class="lyn-dd-btn">🏛️ 书院 ▾</button>
<div class="lyn-dd-menu">
<a href="${p('academy.html')}">🏠 书院首页</a>
<a href="${p('pages/academy/index.html')}">全部课程</a>
<div class="lyn-sep"></div>
<a href="${p('pages/academy/course.html')}">📖 课程详情</a>
<a href="${p('pages/academy/player.html')}">▶ 课程播放</a>
<a href="${p('pages/academy/exercise.html')}">📝 练习</a>
<div class="lyn-sep"></div>
<a href="${p('pages/academy/creator.html')}">✏️ 创作中心</a>
<a href="${p('pages/academy/dashboard.html')}">📊 学习仪表盘</a>
</div></div>

<!-- 创作者 -->
<div class="lyn-dd">
<button class="lyn-dd-btn">🎨 创作者 ▾</button>
<div class="lyn-dd-menu">
<a href="${p('creator.html')}">🏠 创作者首页</a>
<a href="${p('pages/creator/index.html')}">作品大厅</a>
<div class="lyn-sep"></div>
<a href="${p('pages/creator/upload.html')}">📤 发布作品</a>
<a href="${p('pages/creator/studio.html')}">🎬 创作工作室</a>
<a href="${p('pages/creator/collaborate.html')}">🤝 协同创作</a>
<div class="lyn-sep"></div>
<a href="${p('pages/creator/monetize.html')}">💰 变现中心</a>
<a href="${p('pages/creator/analytics.html')}">📊 数据分析</a>
</div></div>

<!-- 数字人 -->
<div class="lyn-dd">
<button class="lyn-dd-btn">🤖 数字人 ▾</button>
<div class="lyn-dd-menu">
<a href="${p('digital-human.html')}">🏠 数字人首页</a>
<a href="${p('pages/digital-human/index.html')}">全息大厅</a>
<div class="lyn-sep"></div>
<a href="${p('pages/digital-human/create.html')}">✨ 创造数字人</a>
<a href="${p('pages/digital-human/wardrobe.html')}">👗 衣橱</a>
<a href="${p('pages/digital-human/interact.html')}">💬 交互</a>
<div class="lyn-sep"></div>
<a href="${p('pages/digital-human/market.html')}">🏪 市场</a>
<a href="${p('pages/digital-human/ai.html')}">🧠 AI核心</a>
</div></div>

<!-- 元宇宙 -->
<div class="lyn-dd">
<button class="lyn-dd-btn">🌐 元宇宙 ▾</button>
<div class="lyn-dd-menu">
<a href="${p('metaverse.html')}">🏠 元宇宙首页</a>
<a href="${p('pages/metaverse/index.html')}">世界大厅</a>
<div class="lyn-sep"></div>
<a href="${p('pages/metaverse/land.html')}">🗺️ 土地</a>
<a href="${p('pages/metaverse/avatar.html')}">🧑 虚拟形象</a>
<a href="${p('pages/metaverse/nft.html')}">🖼️ NFT画廊</a>
<div class="lyn-sep"></div>
<a href="${p('pages/metaverse/explore.html')}">🔮 探索</a>
<a href="${p('pages/metaverse/asset.html')}">📦 资产</a>
</div></div>

<!-- 活动 -->
<div class="lyn-dd">
<button class="lyn-dd-btn">🎉 活动 ▾</button>
<div class="lyn-dd-menu">
<a href="${p('pages/events/index.html')}">🏠 活动首页</a>
<a href="${p('pages/events/detail.html')}">📋 活动详情</a>
<div class="lyn-sep"></div>
<a href="${p('pages/events/create.html')}">✏️ 发布活动</a>
<a href="${p('pages/events/signup.html')}">📝 报名</a>
<div class="lyn-sep"></div>
<a href="${p('pages/events/live.html')}">📡 直播活动</a>
<a href="${p('pages/events/plugin.html')}">🔌 插件</a>
</div></div>

</div><!-- /lyn-menu -->
<div class="lyn-actions">
<button class="lyn-tbtn" title="切换主题">🎨</button>
<a href="${p('pages/auth/login.html')}" class="lyn-btn">登录</a>
<a href="${p('pages/auth/register.html')}" class="lyn-btn" style="border-color:#FF6B35;color:#FF6B35;">注册</a>
</div>
</div><!-- /lyn-inner -->
</nav></div>`;
}

// 移动端点击展开下拉（仅移动端需要JS，桌面端纯CSS）
const NAV_JS = `<script id="lynav-js">
(function(){
  if(window.innerWidth > 880) return;
  document.querySelectorAll('.lyn-dd-btn').forEach(function(btn){
    btn.addEventListener('click', function(e){
      e.preventDefault();
      var dd = this.parentElement;
      document.querySelectorAll('.lyn-dd.lyn-open').forEach(function(d){ if(d!==dd) d.classList.remove('lyn-open'); });
      dd.classList.toggle('lyn-open');
    });
  });
  // 点击其他地方关闭
  document.addEventListener('click', function(e){
    if(!e.target.closest('.lyn-dd')) document.querySelectorAll('.lyn-dd.lyn-open').forEach(function(d){ d.classList.remove('lyn-open'); });
  });
})();
</script>`;

// 收集所有HTML文件
function walkDir(dir, base) {
  let results = [];
  const list = fs.readdirSync(dir);
  list.forEach(function(file) {
    const full = path.join(dir, file);
    const rel = base ? path.join(base, file) : file;
    const stat = fs.statSync(full);
    if (stat && stat.isDirectory()) {
      if (file !== 'assets') results = results.concat(walkDir(full, rel));
    } else if (file.endsWith('.html')) {
      results.push(rel);
    }
  });
  return results;
}

const files = walkDir(ROOT, '');
console.log('[v8] Found ' + files.length + ' HTML files');

let ok = 0, skip = 0;
files.forEach(function(rel) {
  const full = path.join(ROOT, rel);
  let html = fs.readFileSync(full, 'utf8');

  // 计算深度
  const depth = rel.split(/[\\/]/).length - 1;

  // 1. 删除旧导航 CSS（lynav-css / ly-nav / nav-bar / ly-nav-wrap 等）
  html = html.replace(/<style[^>]*id=["']?lynav-css["']?[^>]*>[\s\S]*?<\/style>/gi, '');
  html = html.replace(/<style[^>]*>[\s\S]*?ly-nav-wrap[\s\S]*?<\/style>/gi, '');
  html = html.replace(/<style[^>]*>[\s\S]*?\.nav-bar[\s\S]*?<\/style>/gi, '');
  // 删除旧导航 HTML 注释和容器
  html = html.replace(/<!--\s*LYNAV_EMBEDDED\s*-->/gi, '');
  html = html.replace(/<!--\s*导航栏由 nav\.js[\s\S]*?-->/gi, '');
  html = html.replace(/<div class="ly-nav-wrap">[\s\S]*?<\/div>\s*<\/nav>\s*<\/div>/gi, '');
  html = html.replace(/<div class="lyn-wrap">[\s\S]*?<\/nav>\s*<\/div>/gi, '');
  // 删除旧 nav.js 引用
  html = html.replace(/<script[^>]*src=["'][^"']*nav\.js["'][^>]*><\/script>/gi, '');
  html = html.replace(/<script[^>]*id=["']?lynav-js["']?[^>]*>[\s\S]*?<\/script>/gi, '');

  // 2. 注入新导航 CSS（在 </head> 前）
  const newCSS = NAV_CSS;
  if (html.includes('</head>')) {
    html = html.replace('</head>', newCSS + '\n</head>');
  }

  // 3. 注入导航 HTML（在 <body> 后）
  const navHTML = makeNavHTML(depth);
  if (html.includes('<body')) {
    html = html.replace(/(<body[^>]*>)/, '$1\n' + navHTML + '\n<div class="lyn-spacer"></div>');
  }

  // 4. 注入移动端 JS（在 </body> 前）
  if (html.includes('</body>')) {
    html = html.replace('</body>', NAV_JS + '\n</body>');
  }

  fs.writeFileSync(full, html, 'utf8');
  ok++;
  if (ok % 50 === 0) console.log('[v8] Processed ' + ok + '/' + files.length);
});

console.log('[v8] Done! ' + ok + ' files updated, ' + skip + ' skipped.');

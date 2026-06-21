// ===== LongYi Academy Universal Nav v6.0 (Inline CSS + Smart Path) =====
(function() {
  'use strict';

  // ===== 内联 CSS =====
  const navCSS = `
/* === 导航栏核心样式 === */
.nav-bar {
  position: fixed; top: 0; left: 0; right: 0; z-index: 99999;
  background: rgba(10,10,26,0.92); backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px);
  border-bottom: 1px solid rgba(255,107,53,0.25);
  box-shadow: 0 2px 24px rgba(0,0,0,0.5);
  transition: background 0.3s, box-shadow 0.3s;
}
.nav-bar.nav-scrolled { background: rgba(10,10,26,0.98); box-shadow: 0 2px 32px rgba(255,107,53,0.15); }
.nav-inner {
  max-width: 1400px; margin: 0 auto;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 18px; height: 54px;
}
/* 品牌 */
.nav-brand {
  display: flex; align-items: center; gap: 8px;
  color: #FF6B35; text-decoration: none; font-weight: 700; font-size: 1.05rem;
  white-space: nowrap; flex-shrink: 0;
}
.brand-icon { font-size: 1.4rem; }
.brand-text { background: linear-gradient(135deg,#FF6B35,#ff9a56); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.brand-sub { color: #666; font-size: 0.65rem; font-weight: 400; }

/* 导航链接区 */
.nav-links { display: flex; align-items: center; gap: 2px; overflow-x: auto; flex: 1; justify-content: center; }
.nav-links::-webkit-scrollbar { display: none; }

/* 下拉容器 */
.nav-dropdown { position: relative; }
.nav-group-label {
  display: flex; align-items: center; gap: 4px;
  padding: 8px 12px; border-radius: 8px;
  color: #ccc; font-size: 0.82rem; font-weight: 500;
  cursor: pointer; white-space: nowrap;
  transition: all 0.2s; user-select: none;
}
.nav-group-label:hover { color: #FF6B35; background: rgba(255,107,53,0.1); }
.nav-dropdown:hover .nav-group-label { color: #FF6B35; }

/* 下拉菜单 */
.nav-dropdown-menu {
  display: none;
  position: absolute; top: 100%; left: 50%; transform: translateX(-50%);
  min-width: 180px; max-height: 80vh; overflow-y: auto;
  background: rgba(18,18,40,0.98); backdrop-filter: blur(24px);
  border: 1px solid rgba(255,107,53,0.2); border-radius: 12px;
  padding: 6px; margin-top: 4px;
  box-shadow: 0 12px 48px rgba(0,0,0,0.6);
  z-index: 100000;
}
.nav-dropdown:hover .nav-dropdown-menu { display: block; }
.nav-dropdown-menu a {
  display: block; padding: 8px 14px; border-radius: 8px;
  color: #bbb; text-decoration: none; font-size: 0.8rem;
  transition: all 0.15s; white-space: nowrap;
}
.nav-dropdown-menu a:hover { background: rgba(255,107,53,0.12); color: #FF6B35; }
.nav-dropdown-menu a.nav-active { color: #FF6B35; background: rgba(255,107,53,0.08); }

/* 右侧操作区 */
.nav-actions { display: flex; align-items: center; gap: 8px; flex-shrink: 0; }
.nav-btn {
  padding: 6px 14px; border-radius: 8px;
  color: #ccc; text-decoration: none; font-size: 0.82rem;
  border: 1px solid rgba(255,255,255,0.1);
  background: rgba(255,255,255,0.04);
  transition: all 0.2s; cursor: pointer;
}
.nav-btn:hover { border-color: rgba(255,107,53,0.4); color: #FF6B35; }
.nav-theme-toggle {
  width: 36px; height: 36px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.1);
  color: #ccc; cursor: pointer; transition: all 0.2s;
}
.nav-theme-toggle:hover { background: rgba(255,107,53,0.15); color: #FF6B35; }
.nav-hamburger { display: none; }

/* 占位 */
.nav-spacer { height: 54px; }

/* ===== 移动端 ===== */
@media (max-width: 900px) {
  .nav-links { display: none; position: fixed; top: 54px; left: 0; right: 0;
    flex-direction: column; background: rgba(10,10,26,0.99);
    border-bottom: 1px solid rgba(255,107,53,0.2);
    padding: 12px; gap: 4px; z-index: 99998;
    max-height: calc(100vh - 54px); overflow-y: auto;
  }
  .nav-links.nav-open { display: flex; }
  .nav-dropdown-menu { position: static; transform: none; display: none; box-shadow: none; border: none; background: rgba(255,255,255,0.03); margin-top: 0; padding-left: 12px; }
  .nav-dropdown.nav-dd-open .nav-dropdown-menu { display: block; }
  .nav-hamburger { display: block; background: none; border: none; color: #ccc; font-size: 1.4rem; cursor: pointer; }
}
`;

  // 注入 CSS
  const style = document.createElement('style');
  style.textContent = navCSS;
  document.head.appendChild(style);

  // ===== 路径计算 =====
  function getPrefix() {
    const path = window.location.pathname;
    // pages/xxx/ 或 extra/xxx → ../../  (2层)
    if (/\/pages\/[^\/]+\//.test(path) || /\/extra\//.test(path)) return '../../';
    // pages/ 或 extra/ → ../  (1层)  — 实际不存在此结构
    if (/\/pages\/[^\/]+$/.test(path)) return '../';
    return '';
  }
  const p = getPrefix();

  // ===== 导航 HTML =====
  const navHTML = `
  <nav class="nav-bar" id="mainNav">
    <div class="nav-inner">
      <a href="${p}index.html" class="nav-brand">
        <span class="brand-icon">🏫</span>
        <span class="brand-text">龙奕学院</span>
        <span class="brand-sub">LongYi</span>
      </a>
      <div class="nav-links" id="navLinks">
        <div class="nav-dropdown">
          <span class="nav-group-label">📺 番剧</span>
          <div class="nav-dropdown-menu">
            <a href="${p}anime.html">🏠 番剧首页</a>
            <a href="${p}pages/anime/index.html">番剧大厅</a>
            <a href="${p}pages/anime/player.html">播放器</a>
            <a href="${p}pages/anime/bangumi.html">新番时间表</a>
            <a href="${p}pages/anime/ranking.html">排行榜</a>
            <a href="${p}pages/anime/mad.html">MAD创作</a>
            <a href="${p}pages/anime/library.html">动画图书馆</a>
            <a href="${p}pages/anime/live.html">动画直播</a>
            <a href="${p}pages/anime/upload.html">上传投稿</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <span class="nav-group-label">💬 羁绊</span>
          <div class="nav-dropdown-menu">
            <a href="${p}social.html">🏠 社交首页</a>
            <a href="${p}pages/social/feed.html">社区动态</a>
            <a href="${p}pages/social/create.html">发布创作</a>
            <a href="${p}pages/social/ai-identify.html">AI识图</a>
            <a href="${p}pages/social/profile.html">个人主页</a>
            <a href="${p}pages/social/gallery.html">Cos画廊</a>
            <a href="${p}pages/social/messages.html">私信</a>
            <a href="${p}pages/social/club.html">社团/圈子</a>
            <a href="${p}pages/social/bbs.html">论坛BBS</a>
            <a href="${p}pages/social/match.html">同好匹配</a>
            <a href="${p}pages/social/live-room.html">虚拟直播</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <span class="nav-group-label">🛒 商贸</span>
          <div class="nav-dropdown-menu">
            <a href="${p}shop.html">🏠 商城首页</a>
            <a href="${p}pages/shop/browse.html">商品浏览</a>
            <a href="${p}pages/shop/detail.html">商品详情</a>
            <a href="${p}pages/shop/cart.html">购物车</a>
            <a href="${p}pages/shop/seller.html">卖家中心</a>
            <a href="${p}pages/shop/recommend.html">AI推荐</a>
            <a href="${p}pages/shop/flash.html">限时抢购</a>
            <a href="${p}pages/shop/secondhand.html">二手交易</a>
            <a href="${p}pages/shop/custom.html">定制工坊</a>
            <a href="${p}pages/shop/rental.html">Cos租赁</a>
            <a href="${p}pages/shop/points.html">积分商城</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <span class="nav-group-label">🌌 虚空</span>
          <div class="nav-dropdown-menu">
            <a href="${p}metaverse.html">🏠 世界入口</a>
            <a href="${p}pages/metaverse/explore.html">空间探索</a>
            <a href="${p}pages/metaverse/avatar.html">虚拟化身</a>
            <a href="${p}pages/metaverse/worlds.html">主题世界</a>
            <a href="${p}pages/metaverse/live.html">现场活动</a>
            <a href="${p}pages/metaverse/social.html">元宇宙社交</a>
            <a href="${p}pages/metaverse/builder.html">世界建造</a>
            <a href="${p}pages/metaverse/city.html">虚拟城市</a>
            <a href="${p}pages/metaverse/combat.html">竞技场</a>
            <a href="${p}pages/metaverse/guild.html">公会</a>
            <a href="${p}pages/metaverse/trade.html">交易所</a>
            <a href="${p}pages/metaverse/pets.html">使魔养成</a>
            <a href="${p}pages/metaverse/fashion.html">时装秀</a>
            <a href="${p}pages/metaverse/realm.html">异世界门</a>
            <a href="${p}pages/metaverse/airship.html">飞空艇</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <span class="nav-group-label">🎨 创作</span>
          <div class="nav-dropdown-menu">
            <a href="${p}creator.html">🏠 创作首页</a>
            <a href="${p}pages/creator/dashboard.html">创作仪表盘</a>
            <a href="${p}pages/creator/workshop.html">创作工坊</a>
            <a href="${p}pages/creator/collab.html">协作广场</a>
            <a href="${p}pages/creator/income.html">创作收益</a>
            <a href="${p}pages/creator/fans.html">粉丝管理</a>
            <a href="${p}pages/creator/tools.html">创作工具</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <span class="nav-group-label">🤖 幻影</span>
          <div class="nav-dropdown-menu">
            <a href="${p}digital-human.html">🏠 数字人首页</a>
            <a href="${p}pages/digital-human/studio.html">Studio影棚</a>
            <a href="${p}pages/digital-human/animate.html">动画实验室</a>
            <a href="${p}pages/digital-human/livecast.html">虚拟直播</a>
            <a href="${p}pages/digital-human/showroom.html">数字人展馆</a>
            <a href="${p}pages/digital-human/voice.html">语音合成</a>
            <a href="${p}pages/digital-human/ai-chat.html">AI角色对话</a>
            <a href="${p}pages/digital-human/motion.html">动作捕捉</a>
            <a href="${p}pages/digital-human/clone.html">数字分身</a>
            <a href="${p}pages/digital-human/scene.html">场景工坊</a>
            <a href="${p}pages/digital-human/emotion.html">情感引擎</a>
            <a href="${p}pages/digital-human/dressup.html">👗 3D换装工坊</a>
            <a href="${p}pages/digital-human/llm-interactive.html">🤖 LLM互动</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <span class="nav-group-label">🎓 研修</span>
          <div class="nav-dropdown-menu">
            <a href="${p}academy.html">🏠 学院首页</a>
            <a href="${p}pages/academy/courses.html">课程中心</a>
            <a href="${p}pages/academy/videos.html">视频教程</a>
            <a href="${p}pages/academy/path.html">成长之路</a>
            <a href="${p}pages/academy/mentor.html">导师发现</a>
            <a href="${p}pages/academy/challenge.html">挑战任务</a>
            <a href="${p}pages/academy/exam.html">考试系统</a>
            <a href="${p}pages/academy/cert.html">证书认证</a>
            <a href="${p}pages/academy/live-class.html">直播课堂</a>
            <a href="${p}pages/academy/ranking.html">学霸排行</a>
            <a href="${p}pages/academy/library.html">资料馆</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <span class="nav-group-label">🎪 祭典</span>
          <div class="nav-dropdown-menu">
            <a href="${p}events.html">🏠 活动首页</a>
            <a href="${p}pages/events/calendar.html">活动日历</a>
            <a href="${p}pages/events/contest.html">Cos大赛</a>
            <a href="${p}pages/events/con.html">虚拟漫展</a>
            <a href="${p}pages/events/meetup.html">线下聚会</a>
            <a href="${p}pages/events/live-show.html">虚拟演唱会</a>
            <a href="${p}pages/events/exhibition.html">线上展览</a>
            <a href="${p}pages/events/festival.html">学园祭</a>
            <a href="${p}pages/events/award.html">年度评选</a>
            <a href="${p}pages/events/fireworks.html">烟花大会</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <span class="nav-group-label">📖 百科</span>
          <div class="nav-dropdown-menu">
            <a href="${p}wiki.html">🏠 百科首页</a>
            <a href="${p}pages/wiki/index.html">Cos维基</a>
            <a href="${p}pages/wiki/article.html">知识文章</a>
            <a href="${p}pages/wiki/glossary.html">术语词典</a>
            <a href="${p}pages/wiki/timeline.html">动漫编年史</a>
            <a href="${p}pages/wiki/characters.html">角色图鉴</a>
            <a href="${p}pages/wiki/studios.html">动画公司</a>
            <a href="${p}pages/wiki/seiyuu.html">声优图鉴</a>
          </div>
        </div>
      </div>
      <div class="nav-actions">
        <button id="themeToggle" class="nav-theme-toggle" title="切换日/夜间">🌓</button>
        <a href="${p}pages/auth/login-v2.html" class="nav-btn">登录</a>
        <a href="${p}pages/user/settings.html" class="nav-btn" title="设置">⚙️</a>
        <button class="nav-hamburger" id="navHamburger" aria-label="菜单">☰</button>
      </div>
    </div>
  </nav>
  <div class="nav-spacer"></div>`;

  // 插入导航
  document.body.insertAdjacentHTML('afterbegin', navHTML);

  // ===== 主题切换 =====
  const themeToggle = document.getElementById('themeToggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', function() {
      const root = document.documentElement;
      const isDark = root.classList.contains('theme-dark');
      root.classList.remove(isDark ? 'theme-dark' : 'theme-light');
      root.classList.add(isDark ? 'theme-light' : 'theme-dark');
      localStorage.setItem('cosrealm-theme', isDark ? 'light' : 'dark');
    });
  }

  // 应用保存的主题
  const saved = localStorage.getItem('cosrealm-theme') || 'dark';
  document.documentElement.classList.add('theme-' + saved);

  // ===== 高亮当前页面 =====
  const currentPath = window.location.pathname;
  document.querySelectorAll('.nav-dropdown-menu a').forEach(a => {
    const href = a.getAttribute('href');
    if (!href) return;
    // 匹配最后一段路径
    const linkPath = href.replace(/^\.\.\//, '').replace(/^\.\//, '');
    const curFile = currentPath.split('/').pop();
    if (href.endsWith(curFile) || currentPath.endsWith(href)) {
      a.classList.add('nav-active');
    }
  });

  // ===== 移动端汉堡菜单 =====
  const hamburger = document.getElementById('navHamburger');
  const navLinks = document.getElementById('navLinks');
  if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => {
      navLinks.classList.toggle('nav-open');
      hamburger.textContent = navLinks.classList.contains('nav-open') ? '✕' : '☰';
    });
  }

  // ===== 移动端点击展开下拉 =====
  document.querySelectorAll('.nav-group-label').forEach(label => {
    label.addEventListener('click', function(e) {
      if (window.innerWidth <= 900) {
        e.preventDefault();
        this.closest('.nav-dropdown').classList.toggle('nav-dd-open');
      }
    });
  });

  // ===== 滚动效果 =====
  const nav = document.getElementById('mainNav');
  if (nav) {
    window.addEventListener('scroll', () => {
      nav.classList.toggle('nav-scrolled', window.scrollY > 50);
    }, { passive: true });
  }

  // ===== 点击页面其他地方关闭下拉（移动端）=====
  document.addEventListener('click', (e) => {
    if (window.innerWidth <= 900) {
      if (!e.target.closest('.nav-dropdown') && !e.target.closest('.nav-hamburger')) {
        document.querySelectorAll('.nav-dropdown').forEach(dd => dd.classList.remove('nav-dd-open'));
        if (navLinks) navLinks.classList.remove('nav-open');
        if (hamburger) hamburger.textContent = '☰';
      }
    }
  });

})();

// ===== LongYi Academy Universal Nav v4.0 (Absolute Path) =====
(function() {
  // Use absolute path from site root
  const root = '/';

  const navHTML = `
  <nav class="nav-bar" id="mainNav">
    <div class="nav-inner">
      <a href="${root}index.html" class="nav-brand">
        <span class="brand-icon">🏫</span>
        <span class="brand-text">龙奕学院</span>
        <span class="brand-sub">LongYi Academy</span>
      </a>
      <div class="nav-links" id="navLinks">
        <div class="nav-dropdown">
          <span class="nav-group-label">📺 番剧学院</span>
          <div class="nav-dropdown-menu">
            <a href="${root}anime.html" data-nav="anime-home">🔥 番剧首页</a>
            <a href="${root}pages/anime/index.html" data-nav="anime-index">番剧大厅</a>
            <a href="${root}pages/anime/player.html" data-nav="anime-player">动画播放器</a>
            <a href="${root}pages/anime/bangumi.html" data-nav="anime-bangumi">新番时间表</a>
            <a href="${root}pages/anime/ranking.html" data-nav="anime-ranking">番剧排行</a>
            <a href="${root}pages/anime/mad.html" data-nav="anime-mad">MAD创作</a>
            <a href="${root}pages/anime/library.html" data-nav="anime-library">动画图书馆</a>
            <a href="${root}pages/anime/live.html" data-nav="anime-live">动画直播</a>
            <a href="${root}pages/anime/upload.html" data-nav="anime-upload">上传投稿</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <span class="nav-group-label">💬 羁绊学院</span>
          <div class="nav-dropdown-menu">
            <a href="${root}social.html" data-nav="social">社交大厅</a>
            <a href="${root}pages/social/feed.html" data-nav="social-feed">社区动态</a>
            <a href="${root}pages/social/create.html" data-nav="social-create">发布创作</a>
            <a href="${root}pages/social/ai-identify.html" data-nav="social-ai">AI识别</a>
            <a href="${root}pages/social/profile.html" data-nav="social-profile">个人主页</a>
            <a href="${root}pages/social/gallery.html" data-nav="social-gallery">Cos画廊</a>
            <a href="${root}pages/social/messages.html" data-nav="social-msg">消息</a>
            <a href="${root}pages/social/club.html" data-nav="social-club">社团</a>
            <a href="${root}pages/social/bbs.html" data-nav="social-bbs">论坛</a>
            <a href="${root}pages/social/match.html" data-nav="social-match">同好匹配</a>
            <a href="${root}pages/social/live-room.html" data-nav="social-liveroom">虚拟直播</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <span class="nav-group-label">🛒 商贸学院</span>
          <div class="nav-dropdown-menu">
            <a href="${root}shop.html" data-nav="shop">商城首页</a>
            <a href="${root}pages/shop/browse.html" data-nav="shop-browse">商品浏览</a>
            <a href="${root}pages/shop/detail.html" data-nav="shop-detail">商品详情</a>
            <a href="${root}pages/shop/cart.html" data-nav="shop-cart">购物车</a>
            <a href="${root}pages/shop/seller.html" data-nav="shop-seller">卖家中心</a>
            <a href="${root}pages/shop/recommend.html" data-nav="shop-recommend">AI推荐</a>
            <a href="${root}pages/shop/flash.html" data-nav="shop-flash">限时抢购</a>
            <a href="${root}pages/shop/secondhand.html" data-nav="shop-secondhand">二手交易</a>
            <a href="${root}pages/shop/custom.html" data-nav="shop-custom">定制工坊</a>
            <a href="${root}pages/shop/rental.html" data-nav="shop-rental">Cos租赁</a>
            <a href="${root}pages/shop/points.html" data-nav="shop-points">积分商城</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <span class="nav-group-label">🌌 虚空学院</span>
          <div class="nav-dropdown-menu">
            <a href="${root}metaverse.html" data-nav="metaverse">世界入口</a>
            <a href="${root}pages/metaverse/explore.html" data-nav="meta-explore">空间探索</a>
            <a href="${root}pages/metaverse/avatar.html" data-nav="meta-avatar">虚拟化身</a>
            <a href="${root}pages/metaverse/worlds.html" data-nav="meta-worlds">主题世界</a>
            <a href="${root}pages/metaverse/live.html" data-nav="meta-live">现场活动</a>
            <a href="${root}pages/metaverse/social.html" data-nav="meta-social">元宇宙社交</a>
            <a href="${root}pages/metaverse/builder.html" data-nav="meta-builder">世界建造</a>
            <a href="${root}pages/metaverse/city.html" data-nav="meta-city">虚拟城市</a>
            <a href="${root}pages/metaverse/combat.html" data-nav="meta-combat">竞技场</a>
            <a href="${root}pages/metaverse/guild.html" data-nav="meta-guild">公会</a>
            <a href="${root}pages/metaverse/trade.html" data-nav="meta-trade">交易所</a>
            <a href="${root}pages/metaverse/pets.html" data-nav="meta-pets">使魔养成</a>
            <a href="${root}pages/metaverse/fashion.html" data-nav="meta-fashion">时装秀</a>
            <a href="${root}pages/metaverse/realm.html" data-nav="meta-realm">异世界门</a>
            <a href="${root}pages/metaverse/airship.html" data-nav="meta-airship">飞空艇</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <span class="nav-group-label">🎨 创作学院</span>
          <div class="nav-dropdown-menu">
            <a href="${root}creator.html" data-nav="creator-home">🔥 创作首页</a>
            <a href="${root}pages/creator/dashboard.html" data-nav="creator-dash">创作仪表盘</a>
            <a href="${root}pages/creator/workshop.html" data-nav="creator-workshop">创作工坊</a>
            <a href="${root}pages/creator/collab.html" data-nav="creator-collab">协作广场</a>
            <a href="${root}pages/creator/income.html" data-nav="creator-income">创作收益</a>
            <a href="${root}pages/creator/fans.html" data-nav="creator-fans">粉丝管理</a>
            <a href="${root}pages/creator/tools.html" data-nav="creator-tools">创作工具</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <span class="nav-group-label">✨ 幻影学院</span>
          <div class="nav-dropdown-menu">
            <a href="${root}digital-human.html" data-nav="dh">数字人首页</a>
            <a href="${root}pages/digital-human/studio.html" data-nav="dh-studio">Studio</a>
            <a href="${root}pages/digital-human/animate.html" data-nav="dh-animate">动画实验室</a>
            <a href="${root}pages/digital-human/livecast.html" data-nav="dh-livecast">虚拟直播</a>
            <a href="${root}pages/digital-human/showroom.html" data-nav="dh-showroom">数字人展馆</a>
            <a href="${root}pages/digital-human/voice.html" data-nav="dh-voice">语音合成</a>
            <a href="${root}pages/digital-human/ai-chat.html" data-nav="dh-aichat">AI角色对话</a>
            <a href="${root}pages/digital-human/motion.html" data-nav="dh-motion">动作捕捉</a>
            <a href="${root}pages/digital-human/clone.html" data-nav="dh-clone">数字分身</a>
            <a href="${root}pages/digital-human/scene.html" data-nav="dh-scene">场景工坊</a>
            <a href="${root}pages/digital-human/emotion.html" data-nav="dh-emotion">情感引擎</a>
            <a href="${root}pages/digital-human/dressup.html" data-nav="dh-dressup">👗 3D换装工坊</a>
            <a href="${root}pages/digital-human/llm-interactive.html" data-nav="dh-llm">🤖 LLM互动</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <span class="nav-group-label">🎓 研修学院</span>
          <div class="nav-dropdown-menu">
            <a href="${root}academy.html" data-nav="academy">学院首页</a>
            <a href="${root}pages/academy/courses.html" data-nav="academy-courses">课程中心</a>
            <a href="${root}pages/academy/videos.html" data-nav="academy-videos">视频教程</a>
            <a href="${root}pages/academy/path.html" data-nav="academy-path">成长之路</a>
            <a href="${root}pages/academy/mentor.html" data-nav="academy-mentor">导师发现</a>
            <a href="${root}pages/academy/challenge.html" data-nav="academy-challenge">挑战任务</a>
            <a href="${root}pages/academy/exam.html" data-nav="academy-exam">考试系统</a>
            <a href="${root}pages/academy/cert.html" data-nav="academy-cert">证书认证</a>
            <a href="${root}pages/academy/live-class.html" data-nav="academy-live">直播课堂</a>
            <a href="${root}pages/academy/ranking.html" data-nav="academy-rank">学霸排行</a>
            <a href="${root}pages/academy/library.html" data-nav="academy-lib">资料馆</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <span class="nav-group-label">🎪 祭典学院</span>
          <div class="nav-dropdown-menu">
            <a href="${root}events.html" data-nav="events-home">🔥 活动首页</a>
            <a href="${root}pages/events/calendar.html" data-nav="events-cal">活动日历</a>
            <a href="${root}pages/events/contest.html" data-nav="events-contest">Cos大赛</a>
            <a href="${root}pages/events/con.html" data-nav="events-con">虚拟漫展</a>
            <a href="${root}pages/events/meetup.html" data-nav="events-meetup">线下聚会</a>
            <a href="${root}pages/events/live-show.html" data-nav="events-liveshow">虚拟演唱会</a>
            <a href="${root}pages/events/exhibition.html" data-nav="events-exhibition">线上展览</a>
            <a href="${root}pages/events/festival.html" data-nav="events-festival">学园祭</a>
            <a href="${root}pages/events/award.html" data-nav="events-award">年度评选</a>
            <a href="${root}pages/events/fireworks.html" data-nav="events-fireworks">烟花大会</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <span class="nav-group-label">📖 百科书院</span>
          <div class="nav-dropdown-menu">
            <a href="${root}wiki.html" data-nav="wiki-home">🔥 百科首页</a>
            <a href="${root}pages/wiki/index.html" data-nav="wiki">Cos维基</a>
            <a href="${root}pages/wiki/article.html" data-nav="wiki-article">知识文章</a>
            <a href="${root}pages/wiki/glossary.html" data-nav="wiki-glossary">术语词典</a>
            <a href="${root}pages/wiki/timeline.html" data-nav="wiki-timeline">动漫编年史</a>
            <a href="${root}pages/wiki/characters.html" data-nav="wiki-chars">角色图鉴</a>
            <a href="${root}pages/wiki/studios.html" data-nav="wiki-studios">动画公司</a>
            <a href="${root}pages/wiki/seiyuu.html" data-nav="wiki-seiyuu">声优图鉴</a>
          </div>
        </div>
      </div>
      <div class="nav-actions">
        <button id="themeToggle" class="nav-btn nav-theme-toggle" title="切换日夜间模式" aria-label="主题切换">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
        </button>
        <a href="${root}pages/auth/login-v2.html" class="nav-btn nav-btn-login">登录</a>
        <a href="${root}pages/user/settings.html" class="nav-btn nav-btn-settings">⚙️</a>
        <button class="nav-hamburger" id="navHamburger" aria-label="菜单">☰</button>
      </div>
    </div>
  </nav>
  <div class="nav-spacer"></div>
  `;

  // Insert nav at top of body
  document.body.insertAdjacentHTML('afterbegin', navHTML);

  // Theme toggle
  const themeToggle = document.getElementById('themeToggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', function() {
      const root = document.documentElement;
      const isDark = root.classList.contains('theme-dark');
      if (isDark) {
        root.classList.remove('theme-dark');
        root.classList.add('theme-light');
        localStorage.setItem('cosrealm-theme', 'light');
      } else {
        root.classList.remove('theme-light');
        root.classList.add('theme-dark');
        localStorage.setItem('cosrealm-theme', 'dark');
      }
    });
  }

  // Apply saved theme
  const saved = localStorage.getItem('cosrealm-theme') || 'dark';
  document.documentElement.classList.add('theme-' + saved);

  // Mobile hamburger
  const hamburger = document.getElementById('navHamburger');
  const navLinks = document.getElementById('navLinks');
  if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => {
      navLinks.classList.toggle('nav-open');
      hamburger.textContent = navLinks.classList.contains('nav-open') ? '✕' : '☰';
    });
  }

  // Dropdown toggle on mobile
  document.querySelectorAll('.nav-group-label').forEach(label => {
    label.addEventListener('click', function(e) {
      if (window.innerWidth <= 768) {
        e.preventDefault();
        this.closest('.nav-dropdown').classList.toggle('nav-dd-open');
      }
    });
  });

  // Scroll effects
  const nav = document.getElementById('mainNav');
  if (nav) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) nav.classList.add('nav-scrolled');
      else nav.classList.remove('nav-scrolled');
    });
  }
})();

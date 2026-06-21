#!/usr/bin/env python3
"""
龙奕学院 v4.1 — 9大学院栏目功能丰富化 (安全版)
使用字符串拼接避免f-string大括号嵌套问题
"""
import os

BASE = r"C:\Users\28767\Downloads\cosrealm-site"

def w(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  OK {os.path.basename(path)} ({len(content)} chars)")

# 共享CSS（所有学院首页共用）
SHARED_CSS = """
.hero-box{{background: linear-gradient(160deg, {{CP}}22 0%, {{CS}}18 50%, {{CP}}10 100%);
  border-radius:24px;padding:48px 36px;margin-bottom:28px;
  position:relative;overflow:hidden;border:1px solid rgba(255,255,255,0.08);}}
.hero-box::before{{content:'';position:absolute;top:-40%;right:-20%;width:300px;height:300px;border-radius:50%;background:{{CP}}30;filter:blur(80px);}}
.hero-box::after{{content:'';position:absolute;bottom:-30%;left:-10%;width:250px;height:250px;border-radius:50%;background:{{CS}}20;filter:blur(60px);}}
.hero-inner{{position:relative;z-index:1;}}
.icon-row{{display:flex;gap:12px;margin-bottom:16px;font-size:1.8rem;}}
.htitle{{font-size:2.4rem;font-weight:900;color:#fff;line-height:1.2;margin-bottom:8px;
  background:linear-gradient(135deg,#fff,#c4b5fd);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}}
.hdesc{{font-size:1rem;color:rgba(255,255,255,0.75);max-width:560px;line-height:1.7;}}
.stats-bar{{display:flex;gap:16px;margin-bottom:28px;flex-wrap:wrap;}}
.stat-card{{flex:1;min-width:130px;padding:20px;border-radius:16px;text-align:center;
  background:rgba(20,20,45,0.7);border:1px solid rgba(255,255,255,0.06);transition:all 0.3s;}}
.stat-card:hover{{transform:translateY(-3px);box-shadow:0 8px 25px rgba(99,102,241,0.12);}}
.sctitle{{font-size:1.35rem;font-weight:800;color:#fff;margin-bottom:16px;display:flex;align-items:center;gap:8px;}}
.fgrid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px;margin-bottom:28px;}}
.fcard{{padding:22px;border-radius:18px;background:rgba(20,20,45,0.65);
  border:1px solid rgba(255,255,255,0.06);transition:all 0.3s;cursor:pointer;border-left:4px solid #6366f1;}}
.fcard:hover{{transform:translateY(-5px);box-shadow:0 12px 30px rgba(0,0,0,0.2);border-color:rgba(167,139,250,0.25);}}
.twocol{{display:flex;gap:20px;margin-bottom:28px;}}
.colmain{{flex:1;min-width:0;}}.colside{{width:340px;flex-shrink:0;}}
.spanel{{background:rgba(20,20,45,0.7);border-radius:18px;padding:20px;border:1px solid rgba(255,255,255,0.06);}}
.qgrid{{display:grid;grid-template-columns:repeat(auto-fill,minwidth(120px,1fr));gap:10px;margin-bottom:28px;}}
.qentry{{padding:16px 10px;border-radius:14px;text-align:center;background:rgba(20,20,45,0.55);
  border:1px solid rgba(255,255,255,0.05);cursor:pointer;transition:all 0.25s;text-decoration:none;color:inherit;}}
.qentry:hover{{background:rgba(99,102,241,0.12);border-color:rgba(99,102,241,0.25);transform:translateY(-2px);}}
.nlist{{list-style:none;padding:0;margin:0;}}
.nlist li{{padding:10px 0;border-bottom:1px solid rgba(255,255,255,0.06);display:flex;align-items:center;justify-content:space-between;}}
.nlist li strong{{margin-left:8px;color:#e0e0f0;font-size:0.9rem;}}
.nlist li strong:hover{{color:#a78bfa;}}
.ntime{{color:#666;font-size:0.78rem;white-space:nowrap;}}
.cdown{{display:flex;gap:8px;justify-content:center;margin:16px 0;}}
.cdu{{background:rgba(99,102,241,0.15);border-radius:10px;padding:10px 14px;text-align:center;min-width:52px;}}
.cdnum{{font-size:1.5rem;font-weight:900;color:#fff;}}.cdlab{{font-size:0.68rem;color:#888;margin-top:2px;}}
.twrap{{overflow:hidden;border-radius:12px;background:rgba(20,20,45,0.5);margin-bottom:20px;}}
.ttrack{{display:flex;animation:tscrl 30s linear infinite;width:max-content;padding:8px 0;}}
@keyframes tscrl{{0%{{transform:translateX(0)}}100%{{transform:translateX(-50%)}}}}
.titem{{padding:0 20px;white-space:nowrap;font-size:0.84rem;color:#a0a0c0;shrink:0;}}
.chartph{{height:180px;border-radius:14px;background:rgba(20,20,45,0.4);display:flex;align-items:center;justify-content:center;
  color:#666;font-size:0.9rem;border:1px dashed rgba(255,255,255,0.08);margin:14px 0;}}
"""

def make_home(name_cn, icon, emojis, desc, stats, feats, news, cp, cs, subpgs, d3d='academy', theme='sakura-academy.css', extra=''):
    css = SHARED_CSS.format(CP=cp, CS=cs)
    
    # Stats
    sh = ''
    for ic,nm,lb in stats:
        sh += '<div class="stat-card"><div style="font-size:1.6rem;">'+ic+'</div><div class="cdnum" data-target="'+str(nm)+'">0</div><div style="font-size:0.82rem;color:#888;margin-top:2px;">'+lb+'</div></div>'
    
    # Features  
    fh = ''
    for ic,t,d,c in feats:
        fh += '<div class="fcard" style="border-left-color:'+c+';"><div style="font-size:2rem;margin-bottom:8px;">'+ic+'</div><h3 style="font-size:1.05rem;color:#fff;font-weight:700;margin-bottom:6px;">'+t+'</h3><p style="font-size:0.85rem;color:#a0a0c0;line-height:1.6;">'+d+'</p></div>'

    # News
    nh = ''
    colors_bg = ['rgba(99,102,241,0.15)','rgba(34,197,94,0.15)','rgba(245,158,11,0.15)','rgba(244,114,182,0.15)']
    colors_fg = ['#a5b4fc','#86efac','#fbbf24','#f472b6']
    for i,(ti,tg,tm,_) in enumerate(news):
        nh += '<li><span style="flex:1;"><span style="padding:2px 8px;border-radius:6px;font-size:0.72rem;font-weight:600;background:'+colors_bg[i%4]+';color:'+colors_fg[i%4]+';">'+tg+'</span><strong>'+ti+'</strong></span><span class="ntime">'+tm+'</span></li>'

    # Ticker
    tk = ' '.join(['<span class="titem">&#x1F525; '+n[0]+' |</span>' for n in news]) * 2
    
    # Sub pages nav
    sp = ''
    for n,u,ic in subpgs:
        sp += '<a href="'+u+'" class="qentry"><span style="font-size:1.8rem;display:block;">'+ic+'</span><span style="font-size:0.82rem;color:#d0d0e8;font-weight:600;">'+n+'</span></a>'

    return '''<!DOCTYPE html>
<html lang="zh-CN" data-3d="'''+d3d+'''">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>'''+name_cn+''' &mdash; &#x9F99&#x5959;&#x5B66;&#x9662; LongYi Academy</title>
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="assets/themes/academy/'''+theme+'''">
<link rel="stylesheet" href="assets/themes/dark-mode.css">
<link rel="stylesheet" href="assets/effects-layer.css">
<style>'''+css+'''</style>
</head>
<body>

<div class="hero-box"><div class="hero-inner">
  <div class="icon-row">'''+emojis+'''</div>
  <h1 class="htitle">'''+icon+' '''+name_cn+'''</h1>
  <p class="hdesc">'''+desc+'''</p>
  <div style="display:flex;gap:10px;margin-top:20px;flex-wrap:wrap;">
    <a href="#features" style="display:inline-block;padding:12px 28px;border-radius:14px;background:linear-gradient(135deg,'''+cp+''','''+cs+''');color:#fff;font-weight:700;text-decoration:none;font-size:0.95rem;">&#x63A2;&#x7D22;&#x529F;&#x80FD; &rarr;</a>
    <a href="'''+subpgs[0][1]+'''" style="display:inline-block;padding:12px 28px;border-radius:14px;background:rgba(255,255,255,0.08);color:#e0e0f0;font-weight:600;text-decoration:none;font-size:0.95rem;border:1px solid rgba(255,255,255,0.12);">&#x8FDB;&#x5165;&#x5B66;&#x9662; &uarr;</a>
  </div>
</div></div>

<div style="max-width:1400px;margin:0 auto;padding:0 24px;">
<div class="stats-bar">'''+sh+'''</div>

<div class="twrap"><div class="ttrack">'''+tk+'''</div></div>

<h2 class="sctitle">&#x1F3AF; &#x5FEB;&#x6377;&#x5165;&#x53E3;</h2>
<div class="qgrid">'''+sp+'''</div>

<h2 class="sctitle" id="features">&#x26A1; &#x6838;&#x5FC3;&#x529F;&#x80FD;</h2>
<div class="fgrid">'''+fh+'''</div>

'''+extra+'''

<div class="twocol">
<div class="colmain"><div class="spanel" style="height:100%;">
<h3 class="sctitle">&#x1F4E2; &#x6700;&#x65B0;&#x52A8;&#x6001;</h3>
<ul class="nlist">'''+nh+'''</ul>
</div></div>
<div class="colside">
<div class="spanel" style="margin-bottom:16px;">
<h3 class="sctitle" style="font-size:1.05rem;">&#x23F0; &#x8FD1;&#x671F;&#x6D3B;&#x52A8;&#x5012;&#x8BA1;</h3>
<div class="cdown" id="cbox"></div>
</div>
<div class="spanel">
<h3 class="sctitle" style="font-size:1.05rem;">&#x1F4C8; &#x70ED;&#x5EA6;&#x8D8B;&#x52BF;</h3>
<div class="chartph" id="chartArea">&#x1F4CA; &#x52A8;&#x6001;&#x56FE;&#8868;&#x52A0;&#x8F7D;&#x4E2D;...</div>
</div>
</div></div>

</div>
<script src="assets/three-engine.js"></script>
<script src="assets/nav.js"></script>
<script src="assets/theme-toggle.js"></script>
<script src="assets/effects-runtime.js"></script>
<script src="assets/dynamic-bg.js"></script>
<script>
document.querySelectorAll('.stat-num[data-target]').forEach(function(el){var t=+el.dataset.target;var d=1500;var s=performance.now();function st(n){var p=Math.min((n-s)/d,1);el.textContent=Math.floor(t*p).toLocaleString();if(p<1)requestAnimationFrame(st);}requestAnimationFrame(st);});
(function(){var b=document.getElementById('cbox');if(!b)return;var th=new Date(Date.now()+7*86400000);function tk(){var df=Math.max(0,th-new Date());var d=Math.floor(df/86400000),h=Math.floor((df%86400000)/3600000),m=Math.floor((df%3600000)/60000),sec=Math.floor((df%60000)/1000);b.innerHTML='<div class="cdu"><div class="cdnum">'+d+'</div><div class="cdlab">&#x5929;</div></div><div class="cdu"><div class="cdnum">'+String(h).padStart(2,'0')+'</div><div class="cdlab">&#x65F6;</div></div><div class="cdu"><div class="cdnum">'+String(m).padStart(2,'0')+'</div><div class="cdlab">&#x5206;</div></div><div class="cdu"><div class="cdnum">'+String(sec).padStart(2,'0')+'</div><div class="cdlab">&#x79D2;</div></div>';}tk();setInterval(tk,1000);})();
(function(){var a=document.getElementById('chartArea');if(!a)return;var c=document.createElement('canvas');c.width=a.offsetWidth-20;c.height=160;c.style.borderRadius='12px';a.innerHTML='';a.appendChild(c);var x=c.getContext('2d');var dt=Array.from({length:14},function(){return Math.random()*60+30});var mx=Math.max.apply(null,dt)+10;x.strokeStyle='#6366f1';x.lineWidth=2.5;x.lineCap='round';x.lineJoin='round';var sx=(c.width-20)/(dt.length-1);x.beginPath();dt.forEach(function(v,i){var px=10+i*sx,py=c.height-(v/mx)*(c.height-20)-10;i===0?x.moveTo(px,py):x.lineTo(px,py);});x.stroke();x.lineTo(c.width-10,c.height-10);x.lineTo(10,c.height-10);x.closePath();var g=x.createLinearGradient(0,0,0,c.height);g.addColorStop(0,'rgba(99,102,241,0.2)');g.addColorStop(1,'rgba(99,102,241,0)');x.fillStyle=g;x.fill();})();
</script>
</body>
</html>'''

# ====== 9个学院数据定义 ======
ACADEMIES = [
    {
        'name':'番剧学院','icon':'🎬',
        'emojis':'🎬 📺 ✨ 🌟 🔥 💜 🎭 🎪',
        'desc':'追番、看番、聊番的一站式番剧殿堂。从新番速递到经典回顾，从MAD创作到弹幕狂欢——这里是二次元爱好者的终极聚集地。支持1080P高清播放、实时弹幕、智能推荐。',
        'stats':[('📺',12847,'部番剧'),('👁️',2300000,'日均播放'),('💬',89000000,'弹幕总量'),('⭐',49,'用户评分')],
        'feats':[
            ('🔥','番剧大厅','全站番剧分类浏览，按季度/类型/标签筛选，智能个性化推荐引擎'),
            ('▶️','动画播放器','1080P自适应播放器，支持弹幕发送/遮挡/A-B循环/播放速度调节'),
            ('📅','新番时间表','每季新番追踪，开播提醒，放送时间线可视化日历'),
            ('🏆','番剧排行榜','实时热度榜、评分榜、追番人数榜、弹幕数榜多维度排名'),
            ('🎬','MAD·AMV工坊','视频剪辑工具链，素材库，特效模板，一键渲染发布'),
            ('📚','动画图书馆','动画制作百科、声优数据库、制作公司档案、角色关系图谱'),
        ],
        'news':[('2026年7月新番「星渊编年史」今日首播！','HOT','10分钟前','#'),('MAD创作大赛第三季作品征集开始','NEW','2小时前','#'),('「魔法少女初未来」剧场版定档8月','NEW','5小时前','#'),('本周弹幕热梗TOP10出炉','热门','1天前','#'),('番剧学院年度盛典投票开启','活动','2天前','#')],
        'cp':'rgba(99,102,241,','cs':'rgba(167,139,250,',
        'subpgs':[('番剧大厅','pages/anime/index.html','🏛️'),('播放器','pages/anime/player.html','▶️'),('新番表','pages/anime/bangumi.html','📅'),('排行榜','pages/anime/ranking.html','🏆'),('MAD工坊','pages/anime/mad.html','🎬'),('图书馆','pages/anime/library.html','📚'),('直播','pages/anime/live.html','📡'),('投稿','pages/anime/upload.html','📤')],
        'file':'anime.html','d3d':'anime','theme':'sakura-academy.css'
    },
    {
        'name':'羁绊学院','icon':'🌐',
        'emojis':'💬 👥 💕 🎉 🌟 💜 🔗 🎪',
        'desc':'以Cosplay为纽带的社交生态。动态分享、社团组队、同好匹配、虚拟直播、私信互动——在这里找到志同道合的伙伴，建立跨越次元的羁绊。',
        'stats':[('👥',386000,'活跃用户'),('📝',1200000,'每日动态'),('🏰',2847,'活跃社团'),('💕',12000000,'匹配成功')],
        'feats':[
            ('📱','社区动态','图文/视频/长文动态流，点赞评论转发，话题标签系统'),
            ('👥','社团系统','创建/加入社团，社团活动管理，等级和贡献值体系'),
            ('❤️','同好匹配','AI驱动的兴趣匹配算法，找到你的灵魂搭档'),
            ('📸','Cos画廊','专业级Cos照片展示区，打光/后期技巧交流'),
            ('💬','消息系统','即时通讯，群组聊天，文件共享，已读回执'),
            ('📡','虚拟直播间','3D虚拟形象直播，礼物打榜，连麦PK系统'),
        ],
        'news':[('「春日祭典」大型线下聚会报名开启！','HOT','30分钟前','#'),('新功能上线：AI自动识别Cos角色！','NEW','3小时前','#'),('月度最佳社团：「星穹骑士团」','热门','6小时前','#'),('匹配成功率创新高：本周突破5000对','数据','1天前','#'),('虚拟直播大赛海选进行中','活动','2天前','#')],
        'cp':'rgba(59,130,246,','cs':'rgba(96,165,250,',
        'subpgs':[('社交大厅','social.html','🌐'),('社区动态','pages/social/feed.html','📝'),('发布创作','pages/social/create.html','✍️'),('AI识别','pages/social/ai-identify.html','🤖'),('个人主页','pages/social/profile.html','👤'),('Cos画廊','pages/social/gallery.html','📸'),('消息','pages/social/messages.html','💬'),('社团','pages/social/club.html','🏰'),('论坛','pages/social/bbs.html','📋'),('同好匹配','pages/social/match.html','❤️'),('虚拟直播','pages/social/live-room.html','📡')],
        'file':'social.html','d3d':'default','theme':'sky-academy.css'
    },
    {
        'name':'商贸学院','icon':'🏪',
        'emojis':'🛍️ 💎 ⭐ 🎁 💰 🏷️ ✨ 🎯',
        'desc':'龙奕学院官方商城与C2C交易平台。Cos道具服装、动漫周边、数字商品、定制工坊——正品保障，假一赔十。支持3D商品预览和数字人试穿功能。',
        'stats':[('🛍️',58000,'在售商品'),('🏪',3200,'入驻商家'),('💰',28000000,'GMV/月'),('⭐',487,'平均评分')],
        'feats':[
            ('🔍','商品浏览','多维度筛选搜索，3D模型预览，AR试穿（开发中）'),
            ('📋','商品详情','多图展示/规格选择/评价问答/卖家信用评级'),
            ('🛒','智能购物车','一键加购/批量操作/优惠券抵扣/满减计算'),
            ('🤖','AI推荐','基于浏览历史的个性化推荐，相似商品发现'),
            ('⚡','限时抢购','每日秒杀时段，库存实时同步，排队公平机制'),
            ('♻️','二手交易','个人闲置流转，平台担保交易，验货后放款'),
            ('🎨','定制工坊','提交需求→设计师接单→样品确认→生产发货'),
            ('👗','Cos租赁','短期租赁服务，高端装备低门槛体验'),
        ],
        'news':[('618年中大促正式开启！全场5折起','HOT','刚刚','#'),('新品上架：机甲系列战斗装甲全套','NEW','1小时前','#'),('积分商城更新：限定款猫耳发箍返场','热门','4小时前','#'),('商家入驻优惠政策延期至月底','公告','1天前','#'),('买家秀精选第42期发布','社区','2天前','#')],
        'cp':'rgba(245,158,11,','cs':'rgba(251,191,36,',
        'subpgs':[('商城首页','shop.html','🏪'),('商品浏览','pages/shop/browse.html','🔍'),('商品详情','pages/shop/detail.html','📋'),('购物车','pages/shop/cart.html','🛒'),('卖家中心','pages/shop/seller.html','🏭'),('AI推荐','pages/shop/recommend.html','🤖'),('限时抢购','pages/shop/flash.html','⚡'),('二手交易','pages/shop/secondhand.html','♻️'),('定制工坊','pages/shop/custom.html','🎨'),('Cos租赁','pages/shop/rental.html','👗'),('积分商城','pages/shop/points.html','⭐')],
        'file':'shop.html','d3d':'default','theme':'lemon-academy.css'
    },
    {
        'name':'虚空学院','icon':'🌌',
        'emojis':'🌌 🪐 ⚔️ 🏰 🚀 ✨ 🐉 🔮',
        'desc:'龙墟元宇宙世界的核心入口。虚拟城市探索、PVP竞技场、公会系统、使魔养成、时装秀场、飞空艇航行——一个完全由用户创造的异世界正在等待你。',
        'stats':[('🌍',128,'个主题世界'),('👥',56000,'在线冒险者'),('⚔️',1200000,'场竞技对战'),('🏰',847,'个活跃公会')],
        'feats':[
            ('🏙️','虚拟城市','全3D开放式城市探索，NPC交互，隐藏任务触发'),
            ('⚔️','PVP竞技场','1v1 / 3v3 / 团战模式，赛季排位，段位奖励'),
            ('🏰','公会系统','公会建设/战争/领地争夺，公会技能树'),
            ('💱','交易所','跨服交易市场，虚拟货币兑换，拍卖行'),
            ('🐾','使魔养成','捕捉/进化/合成宠物，战斗伙伴培养路线'),
            ('👗','时装秀场','全服时装展示舞台，T台走秀，投票评选'),
            ('🌀','异世界门','传送至不同规则的主题世界，独特玩法'),
            ('🚀','飞空艇舰队','建造并驾驶飞空艇，空战系统，航线贸易'),
        ],
        'news':[('第五季「虚空之战」公测开启！','HOT','刚刚','#'),('新世界「机械纪元」地图开放','NEW','2小时前','#'),('全服公会争霸赛八强诞生','热门','5小时前','#'),('使魔进化系统重大更新公告','更新','1天前','#'),('飞空艇竞速锦标赛报名开始','活动','2天前','#')],
        'cp':'rgba(139,92,246,','cs':'rgba(167,139,250,',
        'subpgs':[('世界入口','metaverse.html','🌌'),('空间探索','pages/metaverse/explore.html','🔭'),('虚拟化身','pages/metaverse/avatar.html','🧑‍🎤'),('主题世界','pages/metaverse/worlds.html','🌍'),('现场活动','pages/metaverse/live.html','🎪'),('元宇宙社交','pages/metaverse/social.html','💬'),('世界建造','pages/metaverse/builder.html','🏗️'),('虚拟城市','pages/metaverse/city.html','🏙️'),('竞技场','pages/metaverse/combat.html','⚔️'),('公会','pages/metaverse/guild.html','🏰'),('交易所','pages/metaverse/trade.html','💱'),('使魔','pages/metaverse/pets.html','🐾'),('时装秀','pages/metaverse/fashion.html','👗'),('异世界门','pages/metaverse/realm.html','🌀'),('飞空艇','pages/metaverse/airship.html','🚀')],
        'file':'metaverse.html','d3d':'cyber','theme':'starlight-academy.css'
    },
    {
        'name':'创作学院','icon':'🎨',
        'emojis':'🎨 ✍️ 📸 🎬 🎵 💡 🖌️ 🎭',
        'desc':'创作者的成长摇篮和变现平台。从投稿发布、版权保护到收益提现的全链路支持。内置AI辅助创作工具集，让每一个创意都能发光发热。',
        'stats':[('👩‍🎨',28000,'认证创作者'),('📦',186000,'原创作品'),('💰',4200000,'月度分成'),('📈',37,'月增长率%')],
        'feats':[
            ('📊','创作仪表盘','作品数据总览，粉丝增长曲线，收益明细一目了然'),
            ('🛠️','创作工坊','在线编辑器，模板库，素材市场，版本管理'),
            ('🤝','协作广场','跨领域组队，项目招募，远程协作文档'),
            ('💰','收益中心','多渠道收入统计，提现管理，税务协助'),
            ('👥','粉丝管理','粉丝画像分析，互动频率追踪，分层运营'),
            ('🔧','工具箱','AI绘图/文案/配音/视频，一站式创作辅助套件'),
        ],
        'news':[('创作者激励计划Q3升级：分成比例上调至70%！','HOT','1小时前','#'),('AI绘画工具「幻笔」正式接入创作工坊','NEW','4小时前','#'),('本周优秀创作者：「樱坂月华」专访上线','热门','1天前','#'),('版权保护系统新增侵权自动检测','功能','2天前','#'),('跨领域协作挑战赛报名中','活动','3天前','#')],
        'cp':'rgba(236,72,153,','cs':'rgba(244,114,182,',
        'subpgs':[('创作首页','creator.html','🔥'),('仪表盘','pages/creator/dashboard.html','📊'),('创作工坊','pages/creator/workshop.html','🛠️'),('协作广场','pages/creator/collab.html','🤝'),('创作收益','pages/creator/income.html','💰'),('粉丝管理','pages/creator/fans.html','👥'),('创作工具','pages/creator/tools.html','🔧')],
        'file':'creator.html','d3d':'academy','theme':'sunset-academy.css'
    },
    {
        'name':'幻影学院','icon':'✨',
        'emojis':'✨ 🤖 🧝 🎤 🧙‍♀️ 👻 🥷 🧑‍🎤',
        'desc:'下一代AI数字人技术平台。从建模、驱动到交互的完整链路。支持3D换装试穿、LLM大模型驱动行为对话、TTS语音合成、动作捕捉、情感表达——打造属于你的虚拟分身。',
        'stats':[('🤖',1280,'数字人模型'),('🧠','GPT-4o级','LLM驱动'),('🗣️',48,'种语音风格'),('👗',8600,'服装配饰')],
        'feats':[
            ('🎨','Studio建模','参数化捏脸系统，100+可调部位，实时预览渲染'),
            ('👗','3D换装工坊','服装/配饰拖拽试穿，商品3D导入即穿，搭配评分'),
            ('🤖','LLM交互','大模型驱动的自然对话、动作决策、情感响应'),
            ('🎤','语音合成','48种声音风格，语速/音调/情感可调，TTS实时输出'),
            ('📹','虚拟直播','数字人驱动直播，实时表情捕捉，弹幕互动联动'),
            ('🎬','动画实验室','动作预设库，动画混合器，AI文本生成动画'),
            ('📷','动作捕捉','WebCam/专业设备双模式，骨骼绑定，数据导出'),
            ('😊','情感引擎','情绪混合矩阵，微表情控制，情境感知情感切换'),
        ],
        'news':[('数字人换装工坊v2.0上线：支持3D商品导入！','HOT','刚刚','#'),('LLM交互系统升级：上下文记忆增强至50轮','NEW','2小时前','#'),('新语音包「御姐系」正式发布','热门','6小时前','#'),('动作捕捉精度提升至亚毫米级别','技术','1天前','#'),('虚拟直播月活突破10万主播里程碑','数据','2天前','#')],
        'cp':'rgba(167,139,250,','cs':'rgba(196,181,253,',
        'subpgs':[('数字人首页','digital-human.html','✨'),('Studio建模','pages/digital-human/studio.html','🎨'),('动画实验室','pages/digital-human/animate.html','🎬'),('虚拟直播','pages/digital-human/livecast.html','📹'),('展馆','pages/digital-human/showroom.html','🏛️'),('语音合成','pages/digital-human/voice.html','🎤'),('AI对话','pages/digital-human/ai-chat.html','💬'),('LLM互动','pages/digital-human/llm-interactive.html','🤖'),('动作捕捉','pages/digital-human/motion.html','📷'),('数字分身','pages/digital-human/clone.html','🪞'),('场景工坊','pages/digital-human/scene.html','🎭'),('情感引擎','pages/digital-human/emotion.html','😊'),('3D换装','pages/digital-human/dressup.html','👗')],
        'file':'digital-human.html','d3d':'galaxy','theme':'lavender-academy.css'
    },
    {
        'name':'研修学院','icon':'📚',
        'emojis':'📚 🎓 📝 ✏️ 🏆 💡 🔬 🎯',
        'desc:'龙奕学院的知识中枢。系统化的课程体系、权威导师团队、证书认证、学霸排行——从零基础到行业专家的成长之路都在这里。',
        'stats':[('📚',368,'精品课程'),('🎓',86000,'在读学员'),('👨‍🏫',320,'认证导师'),('🏆',12000,'证书颁发')],
        'feats':[
            ('📖','课程中心','分类课程库（Cos/摄影/插画/声优/服装/AI等），进度追踪'),
            ('🎬','视频教程','高清录播+直播回放，倍速/字幕/笔记同步'),
            ('🛤️','成长之路','技能树可视化，学习路径推荐，成就解锁系统'),
            ('👨‍🏫','导师发现','行业大咖入驻，1对1预约辅导，经验传承'),
            ('⚔️','挑战任务','阶段性实践任务，完成获得经验和徽章奖励'),
            ('📝','考试系统','在线考试，防作弊监控，自动批阅，成绩分析'),
            ('🎓','证书认证','完成课程获得区块链存证证书，简历加分项'),
            ('📡','直播课堂','实时互动教学，举手发言，屏幕共享，录制回放'),
            ('🏆','学霸排行','学习时长/成绩/贡献多维排行，奖学金激励机制'),
            ('📂','资料馆','课件下载，素材共享，笔记导出，知识库检索'),
        ],
        'news':[('「AI绘画大师」认证课程限时免费！','HOT','30分钟前','#'),('新晋导师：知名Coser「星野爱丽丝」入驻','NEW','3小时前','#'),('Q2学霸榜单公布：恭喜Top100学员！','热门','1天前','#'),('《Cos服装制作》教材第二版发布','资源','2天前','#'),('研修学院年度学术研讨会征稿中','活动','3天前','#')],
        'cp':'rgba(34,197,94,','cs':'rgba(74,222,128,',
        'subpgs':[('学院首页','academy.html','📚'),('课程中心','pages/academy/courses.html','📖'),('视频教程','pages/academy/videos.html','🎬'),('成长之路','pages/academy/path.html','🛤️'),('导师发现','pages/academy/mentor.html','👨‍🏫'),('挑战任务','pages/academy/challenge.html','⚔️'),('考试系统','pages/academy/exam.html','📝'),('证书认证','pages/academy/cert.html','🎓'),('直播课堂','pages/academy/live-class.html','📡'),('学霸排行','pages/academy/ranking.html','🏆'),('资料馆','pages/academy/library.html','📂')],
        'file':'academy.html','d3d':'academy','theme':'mint-academy.css'
    },
    {
        'name':'祭典学院','icon':'🎪',
        'emojis':'🎪 🎆 🎵 🎭 🎇 🎉 🎊 ✨',
        'desc:'龙奕学院的节日与活动中心。虚拟演唱会、线上漫展、学园祭、Cosplay大赛、烟花大会——全年无休的狂欢盛宴，让每一次相聚都成为难忘回忆。',
        'stats':[('🎪',156,'年度活动'),('👥',2800000,'参与人次'),('🎆',42,'品牌合作'),('⭐',495,'活动评分')],
        'feats':[
            ('📅','活动日历','全年活动一览，订阅提醒，日/周/月视图切换'),
            ('👘','Cos大赛','线上投稿评审+线下总决赛，多赛道角逐，丰厚奖金'),
            ('🌐','虚拟漫展','3D展厅漫游，VR视角，摊位互动，数字周边掉落'),
            ('🤝','线下聚会','同城面基活动组织，场地预订，安全保障'),
            ('🎵','虚拟演唱会','全息投影级数字人演唱会，实时弹幕点歌，礼物打榜'),
            ('🖼️','线上展览','画廊/手办/同人志多展区，创作者直售通道'),
            ('🎏','学园祭','校园风主题活动，摊位文化，美食街，舞台表演'),
            ('🏆','年度评选','人气/作品/社团/新人四大奖项，全民投票+评委评审'),
            ('🎆','烟花大会','龙墟世界内3D烟花秀，多人同时观赏，拍照打卡'),
        ],
        'news':[('夏日祭2026完整日程公布！','HOT','刚刚','#'),('虚拟演唱会门票预售开启 — 前100名获限定头像框','NEW','1小时前','#'),('Cos大赛华南赛区入围名单公示','热门','5小时前','#'),('烟花大会新增3种全新烟火样式','活动','1天前','#'),('年度评选提名阶段进入最后3天','紧急','2天前','#')],
        'cp':'rgba(245,158,11,','cs':'rgba(251,191,36,',
        'subpgs':[('活动首页','events.html','🔥'),('活动日历','pages/events/calendar.html','📅'),('Cos大赛','pages/events/contest.html','👘'),('虚拟漫展','pages/events/con.html','🌐'),('线下聚会','pages/events/meetup.html','🤝'),('虚拟演唱会','pages/events/live-show.html','🎵'),('线上展览','pages/events/exhibition.html','🖼️'),('学园祭','pages/events/festival.html','🎏'),('年度评选','pages/events/award.html','🏆'),('烟花大会','pages/events/fireworks.html','🎆')],
        'file':'events.html','d3d':'default','theme':'coral-academy.css'
    },
    {
        'name':'百科书院','icon':'📖',
        'emotis':'📖 📚 ✏️ 🔍 📝 📜 📋 🎓',
        'desc:'龙奕学院的知识宝库。动画编年史、角色图鉴、声优档案、术语词典、制作公司名录——由社区共建的权威二次元百科全书，每一条词条都经过严格审核。',
        'stats':[('📄',128000,'篇词条'),('👥',18000,'位贡献者'),('📖',2100000,'日访问量'),('✅',99.2,'准确率%')],
        'feats':[
            ('📖','Cos维基','全站核心百科，A-Z索引，交叉引用，版本历史'),
            ('📝','知识文章','深度专题文章，幕后揭秘，技术解析，访谈翻译'),
            ('📋','术语词典','二次元专业术语解释，中日英三语对照'),
            ('📅','动漫编年史','按年份/季度检索的历史事件时间线'),
            ('👤','角色图鉴','详细的角色资料库：设定/声优/登场作品/名台词'),
            ('🎤','声优图鉴','声优个人信息/代表作品/获奖记录/社交链接'),
            ('🏢','动画公司','制作公司档案：历史/代表作/员工/合作关系'),
        ],
        'news':[('「星渊编年史」词条突破10万编辑量！','HOT','2小时前','#'),('新词条批量入库：7月新番全角色档案','NEW','5小时前','#'),('本周优质贡献者：「墨染青书」（32条）','热门','1天前','#'),('术语词典新增AI相关词条120条','更新','2天前','#'),('编年史1990-2026完整版上线','里程碑','3天前','#')],
        'cp':'rgba(99,102,241,','cs':'rgba(167,139,250,',
        'subpgs':[('百科首页','wiki.html','🔥'),('Cos维基','pages/wiki/index.html','📖'),('知识文章','pages/wiki/article.html','📝'),('术语词典','pages/wiki/glossary.html','📋'),('编年史','pages/wiki/timeline.html','📅'),('角色图鉴','pages/wiki/characters.html','👤'),('动画公司','pages/wiki/studios.html','🏢'),('声优图鉴','pages/wiki/seiyuu.html','🎤')],
        'file':'wiki.html','d3d':'academy','theme':'sky-academy.css'
    }
]

# ====== 生成全部 ======
for ac in ACADEMIES:
    html = make_home(
        name_cn=ac['name'], icon=ac['icon'], emojis=ac.get('emotis',ac['emojis']),
        desc=ac['desc'], stats=ac['stats'], feats=ac['feats'],
        news=ac['news'], cp=ac['cp'], cs=ac['cs'],
        subpgs=ac['subpgs'], d3d=ac['d3d'], theme=ac['theme']
    )
    w(os.path.join(BASE, ac['file']), html)

print("\n===== 9大学院首页重写完成 =====")

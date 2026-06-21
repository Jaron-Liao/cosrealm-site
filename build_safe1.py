# -*- coding: utf-8 -*-
"""龙奕学院 批量生成器 v4.0 — ALL IN ONE (Safe Edition)"""
import os

BASE = r'C:\Users\28767\Downloads\cosrealm-site'
PAGES = os.path.join(BASE, 'pages')

HEAD = '<!DOCTYPE html><html lang="zh-CN" data-3d="{scene}" data-nav="{nav}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>{title} — 龙奕学院</title><link id="themeCss" rel="stylesheet" href="{root}assets/themes/academy/{theme}.css"><link rel="stylesheet" href="{root}assets/style.css"><link rel="stylesheet" href="{root}assets/effects-layer.css"></head><body><nav class="nav-bar" id="mainNav"><div class="nav-inner"><div class="nav-brand"><a href="{root}index.html" style="text-decoration:none;display:flex;align-items:center;gap:6px"><span class="brand-icon">🏯</span><div><span class="brand-text">龙奕学院</span><span class="brand-sub">LongYi Academy</span></div></a></div><div class="nav-links" id="navLinks"></div><div class="nav-actions"><a href="{root}pages/auth/login.html" class="btn btn-sm btn-kawaii">登录</a></div><button class="nav-hamburger" id="navHamburger">☰</button></div></nav><div class="nav-spacer"></div><div class="page-wrap">'
FOOT = '</div><footer class="footer"><div class="footer-inner"><div class="footer-brand">© 2026 <strong>龙奕学院 LongYi Academy</strong> · 广州龙奕无形科技文化有限公司</div><div class="footer-links"><a href="{root}pages/help/faq.html">帮助</a><a href="{root}pages/meta/privacy.html">隐私</a><a href="{root}pages/meta/join.html">加入</a></div></div></footer><script src="{root}assets/theme-init.js"></script><script src="{root}assets/three-engine-v3.js"></script><script src="{root}assets/nav.js"></script><script src="{root}assets/effects-runtime.js"></script></body></html>'

def H(e,t,d,extra=''):
    return f'<section class="page-hero"><div class="gradient-orb" style="width:300px;height:300px;top:-50px;left:20%;background:var(--accent)"></div><div class="gradient-orb" style="width:200px;height:200px;bottom:-30px;right:15%;background:var(--accent-2)"></div><span class="hero-emoji anim-float">{e}</span><h1 class="gravity-title">{t}</h1><p>{d}</p>{extra}</section>'

def S(stats):
    n=len(stats)
    c=''.join(f'<div class="stat-card reveal"><div class="stat-value counter-up">{v}</div><div class="stat-label">{l}</div></div>' for v,l in stats)
    return f'<section class="section"><div class="grid-{n}">{c}</div></section>'

def AC(c1,c2,e,n,d,extra=''):
    return f'<div class="card-anime card-shimmer reveal"><div class="card-anime-img" style="background:linear-gradient(135deg,{c1},{c2});display:flex;align-items:center;justify-content:center;font-size:3rem">{e}</div><div class="card-anime-body"><h4>{n}</h4><p style="color:var(--text-muted);font-size:0.8rem">{d}</p>{extra}</div></div>'

def make_page(path,nav,scene,theme,title,body):
    r='../'*len(path.strip('/').split('/'))
    root=r if r else './'
    h=HEAD.format(scene=scene,nav=nav,title=title,root=root,theme=theme)
    f=FOOT.format(root=root)
    fp=os.path.join(PAGES,path)
    os.makedirs(os.path.dirname(fp),exist_ok=True)
    with open(fp,'w',encoding='utf-8') as fh:fh.write(h+body+f)

# ============================================================
# 各学院页面 - 使用列表+join避免嵌套问题
# ============================================================

def anime_doujin():
    P='anime/doujin.html'
    body=[H('🎨','同人创作社区','画出你的热爱，分享你的二次元创作'),
          S([('12,847','作品总数'),('3,201','活跃画师'),('856','本周新作'),('98.7%','好评率')]),
          '<section class="section"><div class="tabs"><button class="tab active">热门作品</button><button class="tab">新晋画师</button><button class="tab">同人小说</button><button class="tab">MMD动画</button></div><div class="grid-4">']
    cards=[
        ('#ff6b9d','#ff8fab','🌸','樱花下的誓言','插画·星野梦','<div style="display:flex;gap:8px;margin-top:8px"><span class="tag tag-pink">❤️ 2.3k</span><span class="tag tag-purple">💬 428</span></div>'),
        ('#4ecdc4','#44a08d','⚔️','剑与魔法的终章','漫画·黑羽凛','<div style="display:flex;gap:8px;margin-top:8px"><span class="tag tag-pink">❤️ 1.8k</span><span class="tag tag-purple">💬 312</span></div>'),
        ('#a78bfa','#7c3aed','🎵','电音天使MMD','MMD·镜音控','<div style="display:flex;gap:8px;margin-top:8px"><span class="tag tag-pink">❤️ 4.1k</span><span class="tag tag-purple">💬 856</span></div>'),
        ('#fbbf24','#f59e0b','📖','异世界转生录','小说·龙奕书院','<div style="display:flex;gap:8px;margin-top:8px"><span class="tag tag-pink">❤️ 3.2k</span><span class="tag tag-purple">💬 621</span></div>'),
    ]
    body.append(''.join(AC(*c) for c in cards))
    body.append('</div></section>')
    body.append('<section class="section"><div class="section-title">🎯 创作挑战 <span class="tag tag-accent tag-glow">进行中</span></div><div class="grid-3">')
    challenges=[('🌙「月下幻想」插画大赛','主题:月光魔法少女·一等奖¥5000',65,'已投稿328幅·剩余7天'),
        ('🎤「声动二次元」音乐祭','原创/翻唱·评委阵容豪华',42,'已投稿156首·剩余14天'),
        ('✍️「异世界狂想」小说大赛','短篇/中篇·出版机会',28,'已投稿89篇·剩余21天')]
    for t,d,p,s in challenges:
        body.append(f'<div class="card-academy-premium reveal"><h3>{t}</h3><p style="color:var(--text-muted)">{d}</p><div class="progress-bar" style="margin:12px 0"><div class="progress-fill" style="width:{p}%"></div></div><span style="font-size:0.75rem;color:var(--text-muted)">{s}</span></div>')
    body.append('</div></section>')
    make_page(P,'anime','sakura','sakura-academy','同人创作',''.join(body))

def anime_radio():
    P='anime/radio.html'
    bars=''.join(f'<div class="audio-bar" style="height:{10+30*j}px;animation-delay:{j*0.08}s"></div>' for j in range(8))
    body=[H('🎵','动漫音乐电台24/7','二次元歌曲不间断',f'<div class="audio-bars" style="justify-content:center;margin-top:16px">{bars}</div>'),
    '<section class="section"><div style="background:var(--bg-card);border-radius:20px;padding:32px;border:1px solid var(--border);max-width:800px;margin:0 auto"><div style="display:flex;align-items:center;gap:16px;margin-bottom:20px"><div style="width:80px;height:80px;border-radius:16px;background:linear-gradient(135deg,#ff6b9d,#a78bfa);display:flex;align-items:center;justify-content:center;font-size:2.5rem">🎶</div><div style="flex:1"><h3>现在播放: Unravel</h3><p style="color:var(--text-muted)">東京喰種OP·TK</p><div class="progress-bar" style="margin-top:8px"><div class="progress-fill progress-glow" style="width:43%"></div></div></div></div><div style="display:flex;gap:12px;justify-content:center"><button class="btn btn-ghost btn-sm">⏮️</button><button class="btn btn-kawaii btn-sm">⏯️</button><button class="btn btn-ghost btn-sm">⏭️</button><button class="btn btn-ghost btn-sm">❤️</button></div></div></section>',
    '<section class="section"><div class="section-title">🎧 热门歌单</div><div class="grid-3">']
    playlists=[('🔥','2025最燃OP TOP50','50首·3小时12分','tag-orange','128万播放'),
        ('💧','催泪神曲治愈特辑','30首·2小时05分','tag-blue','96万播放'),
        ('⚡','作业/工作纯音乐集','60首·4小时30分','tag-green','215万播放')]
    for e,t,d,tc,v in playlists:
        body.append(f'<div class="card card-shimmer reveal"><div style="font-size:2rem;margin-bottom:8px">{e}</div><h4>{t}</h4><p style="color:var(--text-muted);font-size:0.85rem">{d}</p><span class="tag {tc}">{v}</span></div>')
    body.append('</div></section>')
    make_page(P,'anime','galaxy','starlight-academy','动漫音乐电台',''.join(body))

def anime_seiyuu():
    P='anime/seiyuu.html'
    s=[('#ff6b9d','#ff8fab','🎤','花江夏树','鬼灭·炭治郎、东京喰种·金木研','<span class="tag tag-pink">人气TOP</span><span class="tag tag-blue">82角色</span>'),
       ('#4ecdc4','#44a08d','🎤','悠木碧','小圆·鹿目圆、Fate·冲田总司','<span class="tag tag-purple">实力派</span><span class="tag tag-blue">156角色</span>'),
       ('#a78bfa','#7c3aed','🎤','梶裕贵','巨人·艾伦、七大罪·梅利','<span class="tag tag-orange">老牌</span><span class="tag tag-blue">210角色</span>'),
       ('#fbbf24','#f59e0b','🎤','早见沙织','鬼灭·蝴蝶忍、春物·雪乃','<span class="tag tag-green">新锐</span><span class="tag tag-blue">128角色</span>'),
       ('#34d399','#059669','🎤','松冈祯丞','SAO·桐人、ReZero·昴','<span class="tag tag-pink">人气TOP</span><span class="tag tag-blue">89角色</span>'),
       ('#60a5fa','#3b82f6','🎤','水濑祈','ReZero·蕾姆、五等分·五月','<span class="tag tag-accent">声优奖</span><span class="tag tag-blue">67角色</span>')]
    body=[H('🎙️','声优图鉴','声音的魔法师们'),S([('4,832','收录声优'),('12,450','代表角色'),('156','本月新增')]),
    '<section class="section"><div class="input-group-glass" style="max-width:500px;margin:0 auto 32px"><input type="text" placeholder="搜索声优或角色名..."><button>🔍</button></div><div class="grid-3">']
    for c1,c2,e,n,ch,t in s:
        body.append(f'<div class="card-academy-premium reveal" style="text-align:center"><div style="width:72px;height:72px;border-radius:50%;margin:0 auto 16px;background:linear-gradient(135deg,{c1},{c2});display:flex;align-items:center;justify-content:center;font-size:2rem">{e}</div><h3>{n}</h3><p style="color:var(--text-muted);font-size:0.85rem">{ch}</p><div style="margin-top:8px;display:flex;gap:4px;justify-content:center;flex-wrap:wrap">{t}</div></div>')
    body.append('</div></section>')
    make_page(P,'anime','academy','sakura-academy','声优图鉴',''.join(body))

def anime_news():
    P='anime/news.html'
    items=[('tag-pink','新番速递','咒术回战第三季制作决定！','MAPPA官方宣布·2026夏季开播','2小时前'),
           ('tag-blue','剧场版','鬼灭无限城篇票房突破500亿','日本影史新纪录','5小时前'),
           ('tag-purple','业界新闻','京都动画紫罗兰续篇公布','暌违5年全新企划','1天前'),
           ('tag-orange','声优情报','松冈祯丞×茅野爱衣再度合作','粉丝期待黄金搭档回归','1天前'),
           ('tag-green','展会活动','Comic Market 105突破3万作品','史上最大同人志即卖会','2天前'),
           ('tag-accent','海外动态','Crunchyroll全球收视排行出炉','龙奕学院作品登顶','2天前')]
    body=[H('📰','动漫资讯站','最新番剧情报·票房速报·业界动态','<div style="margin-top:12px"><span class="online-badge"><span class="live-dot"></span>实时更新中</span></div>'),
    '<section class="section"><div class="grid-2">']
    for tc,tg,t,d,dt in items:
        body.append(f'<div class="card-academy-premium reveal"><span class="tag {tc}">{tg}</span><h4 style="margin:8px 0">{t}</h4><p style="color:var(--text-muted);font-size:0.82rem">{d}</p><span style="font-size:0.7rem;color:var(--text-muted)">{dt}</span></div>')
    body.append('</div></section>')
    make_page(P,'anime','academy','mint-academy','动漫资讯',''.join(body))

def anime_community():
    P='anime/community.html'
    topics=[('咒术最终章·五条悟回归?','漫画太虐了但预感...','咒术研究部','428','3.2k','2小时前'),
            ('盘点2025年10部冷门神作','质量很高却没人看','鉴番团','315','2.8k','5小时前'),
            ('谏山创叙事结构分析','巨人至今的叙事为何独特','学术派','892','5.4k','8小时前'),
            ('新海诚新作风格分析','预告片透露了什么','电影社','234','1.8k','12小时前'),
            ('AI动画是未来吗?','传统手绘会被取代吗','技术前瞻','567','4.2k','1天前'),
            ('[投票]年度最佳动画','来给你的心头好投票','龙奕官方','1.2k','8.9k','1天前')]
    body=[H('💬','番剧讨论社区','和同好一起追番讨论吐槽'),
    '<section class="section"><div class="tabs"><button class="tab active">热议</button><button class="tab">新番</button><button class="tab">经典</button><button class="tab">制作</button></div><div class="grid-2">']
    for t,d,a,c,l,tm in topics:
        body.append(f'<div class="card card-shimmer reveal"><h4>{t}</h4><p style="color:var(--text-muted);font-size:0.85rem;margin:8px 0">{d}</p><div style="display:flex;gap:12px;font-size:0.8rem;color:var(--text-muted)"><span>👤{a}</span><span>💬{c}</span><span>❤️{l}</span><span>🕐{tm}</span></div></div>')
    body.append('</div></section>')
    make_page(P,'anime','sakura','sakura-academy','番剧讨论',''.join(body))

def anime_gallery():
    P='anime/gallery.html'
    imgs=[('#ff6b9d','#ff8fab','🌸','樱花纷飞校园','3840×2160','4.2万'),('#4ecdc4','#44a08d','🌊','夏日海边约定','3840×2160','3.8万'),
          ('#a78bfa','#7c3aed','🌌','星空下魔法阵','3840×2160','6.1万'),('#fbbf24','#f59e0b','🏯','赛博神社','2560×1440','2.9万'),
          ('#34d399','#059669','🗡️','剑士与龙','3840×2160','5.4万'),('#60a5fa','#3b82f6','❄️','冬日温暖','2560×1440','3.1万'),
          ('#f472b6','#ec4899','💖','魔法变身','1080×2340','7.8万'),('#fb923c','#f97316','🔥','炎之意志','3840×2160','4.5万')]
    body=[H('🖼️','二次元壁纸画廊','高清动漫壁纸每日更新'),
    '<section class="section"><div class="tabs"><button class="tab active">精选</button><button class="tab">4K</button><button class="tab">竖屏</button><button class="tab">横屏</button></div><div class="grid-4">']
    for c1,c2,e,n,r,v in imgs:
        body.append(AC(c1,c2,e,n,f'分辨率:{r}',f'<div style="display:flex;gap:6px;margin-top:6px"><button class="btn btn-sm btn-ghost">⬇️</button><span class="tag tag-accent">{v}</span></div>'))
    body.append('</div></section>')
    make_page(P,'anime','sakura','sakura-academy','壁纸画廊',''.join(body))

def social_cosplay():
    P='social/cosplay.html'
    items=[('#ff6b9d','#ff8fab','🌸','鬼灭·甘露寺蜜璃','摄影:星尘·服装:手工','5.2k','628'),
           ('#4ecdc4','#44a08d','⚔️','Fate·Saber蓝','摄影:光影·3D打印','4.8k','512'),
           ('#a78bfa','#7c3aed','🌙','美战·月野兔','摄影:月影·定制','3.8k','445'),
           ('#fbbf24','#f59e0b','🐉','原神·钟离','摄影:龙摄·手工','6.1k','789'),
           ('#34d399','#059669','🔥','咒术·五条悟','摄影:闪灵·定制','7.2k','1k'),
           ('#60a5fa','#3b82f6','💎','冰雪·艾莎','摄影:冰晶·定制','4.5k','356'),
           ('#f472b6','#ec4899','🎀','小圆·鹿目圆','摄影:星海·制作','3.2k','298'),
           ('#fb923c','#f97316','🦊','火影·鸣人','摄影:忍摄·自绘','5.6k','634')]
    body=[H('📸','Cosplay相册广场','展示你的Cosplay作品'),S([('15,230','作品'),('4,891','Coser'),('892','本周新作')]),
    '<section class="section"><div class="tabs"><button class="tab active">热门</button><button class="tab">最新</button><button class="tab">还原</button><button class="tab">原创</button></div><div class="grid-4">']
    for c1,c2,e,n,d,l,cm in items:
        body.append(AC(c1,c2,e,n,d,f'<div style="display:flex;gap:8px;margin-top:8px"><span>❤️{l}</span><span>💬{cm}</span></div>'))
    body.append('</div></section>')
    make_page(P,'social','anime','sakura-academy','Cosplay相册',''.join(body))

def social_timeline():
    P='social/timeline.html'
    posts=[('#ff6b9d','#ff8fab','🌸','星野梦','发布新同人插画','樱花下的誓言完成了！','<div style="height:120px;border-radius:12px;background:linear-gradient(135deg,#ff6b9d,#ff8fab);margin-top:8px;display:flex;align-items:center;justify-content:center;font-size:3rem">🌸</div>','2.3k','428','18分钟前'),
           ('#4ecdc4','#44a08d','⚔️','黑羽凛','更新漫画24话','剑与魔法终章24话已更新！','<div style="height:120px;border-radius:12px;background:linear-gradient(135deg,#4ecdc4,#44a08d);margin-top:8px"></div>','1.8k','312','38分钟前'),
           ('#a78bfa','#7c3aed','🎵','镜音控','上传新MMD','电音天使新作来啦','','4.1k','856','1小时前'),
           ('#fbbf24','#f59e0b','📖','龙奕书院','开新小说','异世界转生录新篇章','','3.2k','621','2小时前')]
    body=[H('🌊','好友动态','关注好友最新动态'),'<section class="section" style="max-width:640px;margin:0 auto">']
    for c1,c2,e,u,a,c,m,l,cm,t in posts:
        body.append(f'<div class="card card-shimmer reveal" style="margin-bottom:16px"><div style="display:flex;align-items:center;gap:12px;margin-bottom:12px"><div style="width:40px;height:40px;border-radius:50%;background:linear-gradient(135deg,{c1},{c2});display:flex;align-items:center;justify-content:center;font-size:1.2rem">{e}</div><div><strong>{u}</strong> <span style="color:var(--text-muted);font-size:0.8rem">{a}</span></div></div><p>{c}</p>{m}<div style="display:flex;gap:16px;margin-top:12px;font-size:0.8rem;color:var(--text-muted)"><span>❤️{l}</span><span>💬{cm}</span><span>🕐{t}</span></div></div>')
    body.append('</section>')
    make_page(P,'social','default','mint-academy','好友动态',''.join(body))

def social_danmaku():
    P='social/danmaku.html'
    danmakus=[(20,40,'rgba(255,107,157,0.15)','🔥咒术第三季快来！',0),(60,250,'rgba(78,205,196,0.15)','高能预警！！！',0.5),
              (100,60,'rgba(167,139,250,0.15)','欢迎来到龙奕学院~',1),(140,320,'rgba(251,191,36,0.15)','前方高能！',1.5),
              (180,30,'rgba(96,165,250,0.15)','空降成功打卡！',2),(220,300,'rgba(244,114,182,0.15)','我永远喜欢蕾姆！',2.5)]
    body=[H('💭','弹幕广场','让全站看到你的吐槽'),
    '<section class="section"><div style="text-align:center;margin-bottom:24px"><div class="input-group-glass" style="max-width:600px;margin:0 auto"><input type="text" id="dIn" placeholder="输入弹幕...Enter发送"><button onclick="sendDanmaku()">发送▸</button></div></div><div id="dWall" style="max-width:800px;margin:0 auto;padding:24px;background:var(--bg-card);border-radius:20px;border:1px solid var(--border);min-height:300px;position:relative;overflow:hidden">']
    for y,x,bg,t,d in danmakus:
        body.append(f'<div style="position:absolute;top:{y}px;left:{x}px;background:{bg};padding:4px 12px;border-radius:8px;font-size:0.8rem;animation:float 4s infinite;animation-delay:{d}s">{t}</div>')
    body.append('</div></section><script>function sendDanmaku(){var i=document.getElementById("dIn");var w=document.getElementById("dWall");if(!i.value.trim())return;var d=document.createElement("div");d.style.cssText="position:absolute;background:rgba(99,102,241,0.15);padding:4px 12px;border-radius:8px;font-size:0.8rem;animation:float 4s infinite;z-index:1";d.style.left=(20+Math.random()*60)+"%";d.style.top=(10+Math.random()*80)+"%";d.style.animationDelay=Math.random()*3+"s";d.textContent=i.value;w.appendChild(d);i.value="";setTimeout(function(){d.remove()},8000)}</script>')
    make_page(P,'social','anime','sky-academy','弹幕广场',''.join(body))

def social_avatar():
    P='social/avatar-social.html'
    users=[('#ff6b9d','#ff8fab','🌸','樱花少女','在线·听音乐'),('#4ecdc4','#44a08d','⚔️','剑士Kirito','在线·副本中'),
           ('#a78bfa','#7c3aed','🧙','魔法师露娜','离线·1小时前'),('#fbbf24','#f59e0b','🐉','龙骑士雷恩','在线·翱翔中'),
           ('#34d399','#059669','🎸','吉他手音音','忙碌·创作中'),('#60a5fa','#3b82f6','🐱','猫耳娘小雪','在线·求组队'),
           ('#f472b6','#ec4899','💃','舞者美咲','在线·排练中'),('#fb923c','#f97316','🔥','炎术师炎真','离线·3天前')]
    body=[H('🧑‍💻','3D虚拟形象社交','在元宇宙中交友'),
    '<section class="section"><div style="text-align:center;margin-bottom:32px"><div class="glass-crystal" style="display:inline-block;padding:32px 48px;border-radius:24px"><div style="width:120px;height:120px;border-radius:50%;background:linear-gradient(135deg,#6366f1,#a78bfa);margin:0 auto 16px;display:flex;align-items:center;justify-content:center;font-size:3rem">🧑‍🎤</div><h3>你的虚拟形象</h3><p style="color:var(--text-muted)">Lv.1·0位好友</p><button class="btn btn-kawaii neon-btn" style="margin-top:12px">🎨自定义形象</button></div></div><div class="grid-4">']
    for c1,c2,e,n,s in users:
        body.append(f'<div class="card-academy-premium reveal" style="text-align:center"><div style="width:64px;height:64px;border-radius:50%;background:linear-gradient(135deg,{c1},{c2});margin:0 auto 12px;display:flex;align-items:center;justify-content:center;font-size:1.8rem">{e}</div><h4>{n}</h4><p style="color:var(--text-muted);font-size:0.8rem">{s}</p><button class="btn btn-sm btn-ghost" style="margin-top:8px">+加好友</button></div>')
    body.append('</div></section>')
    make_page(P,'social','cyber','starlight-academy','虚拟形象社交',''.join(body))

def social_voice():
    P='social/voice-room.html'
    rooms=[('#ff6b9d','#ff8fab','🌸','二次元深夜电台','328','闲聊','<span class="tag tag-pink">闲聊</span><span class="tag tag-purple">音乐</span>'),
           ('#4ecdc4','#44a08d','⚔️','咒术最终话讨论','892','最新话','<span class="tag tag-blue">番剧</span><span class="tag tag-orange">剧透</span>'),
           ('#a78bfa','#7c3aed','🎮','原神联机开黑','456','锄大地','<span class="tag tag-green">游戏</span><span class="tag tag-purple">组队</span>'),
           ('#fbbf24','#f59e0b','🎤','翻唱比赛海选','234','评审中','<span class="tag tag-pink">比赛</span><span class="tag tag-accent">音乐</span>'),
           ('#34d399','#059669','📚','异世界小说接龙','178','创作中','<span class="tag tag-green">创作</span><span class="tag tag-blue">文字</span>'),
           ('#60a5fa','#3b82f6','🗣️','日语学习角','312','N2备考','<span class="tag tag-purple">学习</span><span class="tag tag-accent">日语</span>')]
    body=[H('🎙️','实时语音房间','和同好语音聊天游戏开黑'),'<section class="section"><div class="grid-2">']
    for c1,c2,e,n,cnt,tp,tg in rooms:
        body.append(f'<div class="card-academy-premium card-shimmer reveal" style="display:flex;align-items:center;justify-content:space-between"><div style="display:flex;align-items:center;gap:12px"><div style="width:48px;height:48px;border-radius:12px;background:linear-gradient(135deg,{c1},{c2});display:flex;align-items:center;justify-content:center;font-size:1.5rem">{e}</div><div><h4>{n}</h4><p style="color:var(--text-muted);font-size:0.8rem"><span class="status-online">●</span>{cnt}人在线·{tp}</p></div></div><div style="display:flex;gap:8px">{tg}</div><button class="btn btn-accent btn-sm btn-ripple">🎧加入</button></div>')
    body.append('</div></section>')
    make_page(P,'social','cyber','sunset-academy','语音房间',''.join(body))

# ===== 商城 =====
def shop_goods():
    P='shop/goods.html'
    items=[('#ff6b9d','#ff8fab','🌸','炭治郎手办','1/7PVC完成品','699'),('#4ecdc4','#44a08d','⚔️','立体机动装置','1:1金属可穿戴','1299'),
           ('#a78bfa','#7c3aed','🎭','蕾姆抱枕','等身大160cm','299'),('#fbbf24','#f59e0b','🐉','钟离键帽','PBT137键','199'),
           ('#34d399','#059669','🔥','宿傩手指','1:1树脂收藏','159'),('#60a5fa','#3b82f6','🗡️','阐释者','1:1刀模展示架','499'),
           ('#f472b6','#ec4899','💎','灵魂宝石','发光款旋转底座','89'),('#fb923c','#f97316','🎴','忍术卷轴','全12款随机','39')]
    body=[H('🛍️','正版周边商城','手办模型抱枕COS道具'),S([('12,450','商品'),('98.6%','好评'),('24h','发货'),('7天','退换')]),
    '<section class="section"><div class="tabs"><button class="tab active">🔥热销</button><button class="tab">🆕新品</button><button class="tab">💰特价</button></div><div class="grid-4">']
    for c1,c2,e,n,d,p in items:
        body.append(AC(c1,c2,e,n,f'官方正版·{d}',f'<div style="display:flex;justify-content:space-between;align-items:center;margin-top:8px"><span style="font-size:1.1rem;font-weight:800;color:var(--accent)">¥{p}</span><button class="btn btn-sm btn-kawaii btn-ripple">🛒</button></div>'))
    body.append('</div></section>')
    make_page(P,'shop','default','coral-academy','正版周边',''.join(body))

def shop_cosprops():
    P='shop/cos-props.html'
    cards=[('🖨️','3D打印定制','上传模型或参考图','<span class="tag tag-blue">SLA</span><span class="tag tag-green">FDM</span><span class="tag tag-purple">尼龙</span>',85,'产能85%·3-5天出货','开始定制▸'),
           ('🎨','手工上色','专业美术团队涂装','<span class="tag tag-pink">喷枪</span><span class="tag tag-orange">手涂</span><span class="tag tag-accent">旧化</span>',60,'画师档期60%·5-7天','预约画师▸'),
           ('⚒️','金属加工','CNC精密加工','<span class="tag tag-blue">CNC</span><span class="tag tag-green">激光切割</span><span class="tag tag-purple">镀层</span>',45,'工坊产能45%·7-14天','询价定制▸')]
    body=[H('🔧','COS道具定制工坊','3D打印·手工制作·还原细节'),'<section class="section"><div class="grid-3">']
    for e,n,d,tg,pg,inf,btn in cards:
        body.append(f'<div class="card-academy-premium reveal"><div style="font-size:3rem;margin-bottom:12px;text-align:center">{e}</div><h3 style="text-align:center">{n}</h3><p style="color:var(--text-muted);text-align:center">{d}</p><div style="text-align:center;margin-top:12px">{tg}</div><div class="progress-bar" style="margin:12px 0"><div class="progress-fill" style="width:{pg}%"></div></div><p style="text-align:center;color:var(--text-muted);font-size:0.8rem">{inf}</p><div style="text-align:center"><button class="btn btn-accent btn-sm btn-ripple" style="margin-top:8px">{btn}</button></div></div>')
    body.append('</div></section>')
    make_page(P,'shop','cyber','lavender-academy','COS道具定制',''.join(body))

def shop_flash():
    P='shop/flash-sale.html'
    items=[('#ff6b9d','#ff8fab','🌸','鬼灭T恤炭治郎款','89','199',55,72),('#4ecdc4','#44a08d','📱','过家家手机壳','39','89',56,88),
           ('#a78bfa','#7c3aed','🧸','五条悟趴趴','59','129',54,63),('#fbbf24','#f59e0b','🎒','原神元素背包','99','249',60,45)]
    body=[H('⚡','限时闪购','每2小时更新·手慢无','<div style="text-align:center;margin-top:12px"><span class="badge" style="font-size:1rem;padding:8px 20px">⏱️下一波:<span id="cd">01:45:32</span></span></div>'),
    '<section class="section"><div class="grid-4">']
    for c1,c2,e,n,p,o,dc,s in items:
        body.append(f'<div class="card-anime card-shimmer reveal" style="position:relative"><div style="position:absolute;top:8px;left:8px;background:#ef4444;color:#fff;padding:4px 10px;border-radius:8px;font-size:0.7rem;font-weight:800;z-index:2">-{dc}%</div><div class="card-anime-img" style="background:linear-gradient(135deg,{c1},{c2});display:flex;align-items:center;justify-content:center;font-size:3rem">{e}</div><div class="card-anime-body"><h4>{n}</h4><div style="display:flex;align-items:center;gap:8px;margin-top:4px"><span style="font-size:1.1rem;font-weight:800;color:#ef4444">¥{p}</span><span style="text-decoration:line-through;color:var(--text-muted);font-size:0.8rem">¥{o}</span></div><div class="progress-bar" style="margin:8px 0"><div class="progress-fill" style="width:{s}%"></div></div><span style="font-size:0.7rem;color:var(--text-muted)">已售{s}%</span><button class="btn btn-sm btn-kawaii btn-ripple" style="margin-top:8px;width:100%">⚡抢购</button></div></div>')
    body.append('</div></section><script>setInterval(function(){var m=document.getElementById("cd");if(!m)return;var t=m.textContent.split(":");var h=parseInt(t[0]),mi=parseInt(t[1]),s=parseInt(t[2]);if(s>0)s--;else if(mi>0){mi--;s=59}else if(h>0){h--;mi=59;s=59}m.textContent=String(h).padStart(2,"0")+":"+String(mi).padStart(2,"0")+":"+String(s).padStart(2,"0")},1000)</script>')
    make_page(P,'shop','default','sunset-academy','限时闪购',''.join(body))

def shop_secondhand():
    P='shop/secondhand.html'
    items=[('#ff6b9d','#ff8fab','📦','誓约胜利之剑','1:1金属复刻','剑士收藏家','899','tag-green','几乎全新'),
           ('#4ecdc4','#44a08d','📦','日轮刀全套','限定版7把','鬼灭粉','2499','tag-blue','9成新'),
           ('#a78bfa','#7c3aed','📦','雪初音手办','2018限定','V家死忠','1299','tag-orange','良好'),
           ('#fbbf24','#f59e0b','📦','初号机模型','RG未拼装','胶佬清仓','399','tag-green','全新')]
    body=[H('🔄','二手交易市场','闲置周边绝版手办自由交易'),S([('8,540','在线商品'),('98.2%','成功率'),('¥236','均价')]),
    '<section class="section"><div class="input-group-glass" style="max-width:500px;margin:0 auto 24px"><input type="text" placeholder="搜索二手商品..."><button>搜索</button></div><div class="grid-4">']
    for c1,c2,e,n,d,sl,p,tc,c in items:
        body.append(AC(c1,c2,e,n,f'{d}·{sl}',f'<div style="display:flex;justify-content:space-between;align-items:center;margin-top:8px"><span style="font-weight:800;color:var(--accent)">¥{p}</span><span class="tag {tc}">{c}</span></div>'))
    body.append('</div></section>')
    make_page(P,'shop','default','lemon-academy','二手交易',''.join(body))

def shop_rental():
    P='shop/rental.html'
    items=[('#ff6b9d','#ff8fab','👘','炭治郎全套','刀+制服+羽织','89','S-XXL'),('#4ecdc4','#44a08d','👘','Saber蓝裙','铠甲+裙+剑','129','S-L'),
           ('#a78bfa','#7c3aed','👘','小樱粉裙','杖+假发+裙','79','S-M'),('#fbbf24','#f59e0b','👘','鸣人橙衣','护额+外套+裤子','69','S-XXL'),
           ('#34d399','#059669','👘','五条悟校服','眼罩+校服+假发','99','M-XXL'),('#60a5fa','#3b82f6','👘','初音公式服','假发+耳机+裙','59','均码')]
    body=[H('👘','COS服装租赁','三天起租·正版·消毒'),'<section class="section"><div class="grid-3">']
    for c1,c2,e,n,d,p,s in items:
        body.append(f'<div class="card-academy-premium card-shimmer reveal"><div style="display:flex;align-items:center;gap:16px"><div style="width:80px;height:100px;border-radius:12px;background:linear-gradient(135deg,{c1},{c2});flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:2.5rem">{e}</div><div><h4>{n}</h4><p style="color:var(--text-muted);font-size:0.8rem">{d}</p><div style="margin-top:8px"><span style="font-weight:800;color:var(--accent)">¥{p}/天</span>·<span style="font-size:0.8rem;color:var(--text-muted)">{s}</span></div><button class="btn btn-sm btn-accent btn-ripple" style="margin-top:8px">立即租赁</button></div></div></div>')
    body.append('</div></section>')
    make_page(P,'shop','default','coral-academy','COS服装租赁',''.join(body))

# ============================================================
print('='*60)
print('龙奕学院 批量生成器 v4.0 SAFE EDITION')
print('='*60)

print('🎬 动漫学院...')
anime_doujin(); anime_radio(); anime_seiyuu(); anime_news(); anime_community(); anime_gallery()
print('  ✅ 动漫学院 6页完成')

print('👥 社交学院...')
social_cosplay(); social_timeline(); social_danmaku(); social_avatar(); social_voice()
print('  ✅ 社交学院 5页完成')

print('🛍️ 商城学院...')
shop_goods(); shop_cosprops(); shop_flash(); shop_secondhand(); shop_rental()
print('  ✅ 商城学院 5页完成')

print('='*60)
print('第一批完成！总计 16 个新页面')
print('='*60)

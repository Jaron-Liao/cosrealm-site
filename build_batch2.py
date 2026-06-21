# -*- coding: utf-8 -*-
"""龙奕学院 批量生成器 v4.0 — 第二批: 龙墟世界/数字人/创作者/学院/活动/Wiki"""
import os

BASE = r'C:\Users\28767\Downloads\cosrealm-site'
PAGES = os.path.join(BASE, 'pages')

HEAD = '<!DOCTYPE html><html lang="zh-CN" data-3d="{scene}" data-nav="{nav}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>{title} — 龙奕学院</title><link id="themeCss" rel="stylesheet" href="{root}assets/themes/academy/{theme}.css"><link rel="stylesheet" href="{root}assets/style.css"><link rel="stylesheet" href="{root}assets/effects-layer.css"></head><body><nav class="nav-bar" id="mainNav"><div class="nav-inner"><div class="nav-brand"><a href="{root}index.html" style="text-decoration:none;display:flex;align-items:center;gap:6px"><span class="brand-icon">🏯</span><div><span class="brand-text">龙奕学院</span><span class="brand-sub">LongYi Academy</span></div></a></div><div class="nav-links" id="navLinks"></div><div class="nav-actions"><a href="{root}pages/auth/login.html" class="btn btn-sm btn-kawaii">登录</a></div><button class="nav-hamburger" id="navHamburger">☰</button></div></nav><div class="nav-spacer"></div><div class="page-wrap">'
FOOT = '</div><footer class="footer"><div class="footer-inner"><div class="footer-brand">© 2026 <strong>龙奕学院 LongYi Academy</strong> · 广州龙奕无形科技文化有限公司</div><div class="footer-links"><a href="{root}pages/help/faq.html">帮助</a><a href="{root}pages/meta/privacy.html">隐私</a><a href="{root}pages/meta/join.html">加入</a></div></div></footer><script src="{root}assets/theme-init.js"></script><script src="{root}assets/three-engine-v3.js"></script><script src="{root}assets/nav.js"></script><script src="{root}assets/effects-runtime.js"></script></body></html>'

def hero(e,t,d,extra=''):
    return f'<section class="page-hero"><div class="gradient-orb" style="width:300px;height:300px;top:-50px;left:20%;background:var(--accent)"></div><div class="gradient-orb" style="width:200px;height:200px;bottom:-30px;right:15%;background:var(--accent-2)"></div><span class="hero-emoji anim-float">{e}</span><h1 class="gravity-title">{t}</h1><p>{d}</p>{extra}</section>'
def stat_row(stats):
    return '<section class="section"><div class="grid-{}">'.format(len(stats))+''.join(f'<div class="stat-card reveal"><div class="stat-value counter-up">{v}</div><div class="stat-label">{l}</div></div>' for v,l in stats)+'</div></section>'
def make_page(path,nav,scene,theme,title,body):
    r='../'*len(path.strip('/').split('/'))
    root=r if r else './'
    h=HEAD.format(scene=scene,nav=nav,title=title,root=root,theme=theme)
    f=FOOT.format(root=root)
    fp=os.path.join(PAGES,path)
    os.makedirs(os.path.dirname(fp),exist_ok=True)
    with open(fp,'w',encoding='utf-8') as fh:fh.write(h+body+f)

# ===== 龙墟世界 METAVERSE (7页) =====
def build_metaverse():
    P='metaverse'
    # 世界地图
    make_page(f'{P}/world-map.html','metaverse','cyber','starlight-academy','龙墟世界地图',
        hero('🗺️','龙墟世界全地图','七大区域等待探索')+
        '<section class="section"><div style="background:var(--bg-card);border-radius:24px;padding:32px;border:1px solid var(--border);max-width:900px;margin:0 auto"><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px;text-align:center">'+
        ''.join([f'<div class="card-academy-premium card-shimmer reveal" style="text-align:center"><div style="font-size:2.5rem;margin-bottom:8px">{e}</div><h4>{n}</h4><p style="color:var(--text-muted);font-size:0.75rem">{d}</p><span class="tag tag-accent">{p}在线</span></div>'
        for e,n,d,p in [('🏰','浮空皇城','主城·集会中心','12,450'),('🌲','翠绿森域','精灵领地·采集','6,780'),('🗻','铁脊山脉','矮人锻造·矿石','4,230'),
        ('🌊','星落海岸','美人鱼海·贸易','3,890'),('🌋','熔火深渊','龙族巢穴·副本','2,150'),('❄️','永冻冰原','冰霜巨人·材料','1,980'),
        ('🌌','虚空裂隙','未知领域·BOSS','890'),('🕳️','深渊裂谷','新版图·挑战','1,240')]])+'</div></div></section>')
    
    # 使魔
    make_page(f'{P}/pets-breed.html','metaverse','nature','mint-academy','使魔孵化',
        hero('🥚','使魔孵化与培育','从蛋开始培育专属战斗伙伴')+
        '<section class="section"><div class="section-title">🥚可孵化使魔蛋</div><div class="grid-4">'+
        ''.join([f'<div class="card-academy-premium card-shimmer reveal" style="text-align:center"><div style="font-size:3rem;margin-bottom:8px">{e}</div><h4>{n}</h4><p style="color:var(--text-muted);font-size:0.8rem">{d}</p><div style="margin:8px 0"><span class="tag tag-pink">稀有度:{"⭐"*s}</span></div><div class="progress-bar"><div class="progress-fill" style="width:{h}%"></div></div><span style="font-size:0.7rem;color:var(--text-muted)">孵化{h}%</span><button class="btn btn-sm btn-accent btn-ripple" style="margin-top:8px;width:100%">🔮加速</button></div>'
        for e,n,d,s,h in [('🐉','幼龙蛋','火属性远程攻击',5,78),('🦊','九尾狐幼崽','幻术高闪避暴击',4,45),('🐺','霜狼幼崽','冰属性近战坦克',3,92),
        ('🦅','雷鹰蛋','风属性飞行侦查',4,63),('🐍','蛇妖之卵','毒属性持续伤害',3,34),('🦄','独角兽幼驹','光属性治疗',5,15),
        ('🐢','玄武幼崽','水属性防御',4,51),('🦇','影蝠幼体','暗属性偷袭',3,89)]])+'</div></section>')

    # 异世界门
    make_page(f'{P}/realm-gate.html','metaverse','void','lavender-academy','异世界之门',
        hero('🌀','异世界之门','穿梭不同次元探索无限可能')+
        '<section class="section"><div class="grid-3">'+''.join([f'<div class="card-academy-premium hologram card-shimmer reveal" style="text-align:center"><div style="font-size:4rem;margin-bottom:12px">{e}</div><h3>{n}</h3><p style="color:var(--text-muted);margin:8px 0">{d}</p><div style="margin:12px 0"><span class="tag tag-accent">Lv.{l}</span><span class="tag tag-orange">难度{dif}/10</span></div><button class="btn btn-accent btn-ripple neon-btn">🌌穿越</button><p style="color:var(--text-muted);font-size:0.7rem;margin-top:8px">{p}人探索</p></div>'
        for e,n,d,l,dif,p in [('🏯','战国妖狐传','妖魔横行·你是猎魔人',50,6,'3,240'),('🚀','星际迷航纪元','探索银河系边缘',80,8,'1,890'),
        ('🧙','魔法学院霍格莫德','古老魔法学校',30,4,'5,670'),('🤖','机械纪元2099','赛博朋克义体大战',70,7,'2,340'),
        ('🏴‍☠️','大海贼时代','寻找ONE PIECE',40,5,'4,120'),('🦖','恐龙纪元','史前生存挑战',60,7,'1,560')]])+'</div></section>')

    # 飞空艇
    make_page(f'{P}/airship-routes.html','metaverse','galaxy','sky-academy','飞空艇航线',
        hero('🛸','飞空艇航线','龙墟世界空中交通系统')+
        '<section class="section"><div style="background:var(--bg-card);border-radius:20px;padding:32px;border:1px solid var(--border);max-width:800px;margin:0 auto">'+
        ''.join([f'<div class="card card-shimmer reveal" style="display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;padding:12px"><div style="display:flex;align-items:center;gap:12px"><span>🏰</span><span style="font-weight:600">浮空皇城</span><span style="color:var(--text-muted)">→</span><span style="font-size:1.5rem">{e}</span><span style="font-weight:600">{d}</span></div><div style="text-align:right"><span style="color:var(--accent)">¥{p}</span><br><span style="font-size:0.7rem;color:var(--text-muted)">{t}</span></div><button class="btn btn-sm btn-ghost">购票</button></div>'
        for e,d,p,t in [('🌲','翠绿森域','50','约5分钟'),('🗻','铁脊山脉','50','约5分钟'),('🌊','星落海岸','80','约8分钟'),
        ('🌋','熔火深渊','100','约12分钟'),('❄️','永冻冰原','120','约15分钟'),('🌌','虚空裂隙','200','约20分钟'),('🕳️','深渊裂谷','250','约25分钟')]])+'</div></section>')

    # 公会战+拍卖行+时装
    make_page(f'{P}/guild-war.html','metaverse','cyber','sunset-academy','公会战争',
        hero('⚔️','公会战争','公会间荣耀之战')+stat_row([('256','活跃公会'),('18,450','参战玩家'),('3','进行中战役')])+
        '<section class="section"><div class="section-title">🏆公会战力排行</div>'+''.join([f'<div class="card card-shimmer reveal" style="display:flex;align-items:center;gap:16px;margin-bottom:12px;padding:12px"><div style="font-size:1.5rem;font-weight:900;width:40px;text-align:center;color:{c}">#{r}</div><div style="width:44px;height:44px;border-radius:12px;background:linear-gradient(135deg,{c1},{c2});display:flex;align-items:center;justify-content:center;font-size:1.3rem">{e}</div><div style="flex:1"><h4>{n}</h4><p style="color:var(--text-muted);font-size:0.8rem">{l}·{m}人</p></div><div style="text-align:right"><span style="font-weight:800;font-size:1.1rem;color:var(--accent)">{s}</span><br><span style="font-size:0.75rem;color:var(--text-muted)">战斗值</span></div></div>'
        for r,c,c1,c2,e,n,l,m,s in [(1,'#fbbf24','#fbbf24','#f59e0b','🐉','龙奕骑士团','团长:雷恩',158,'9,999,999'),
        (2,'#94a3b8','#94a3b8','#c0c0c0','⚔️','星辰之剑','团长:星落',142,'8,765,432'),
        (3,'#cd7f32','#cd7f32','#8b5a2b','🔥','炼狱之火','团长:焚天',135,'7,654,321'),
        (4,'#6366f1','#6366f1','#8b5cf6','🌙','月下同盟','团长:月影',128,'6,543,210'),
        (5,'#10b981','#34d399','#059669','🌿','翠绿守护','团长:叶风',120,'5,432,109')]])+'</section>')

    make_page(f'{P}/auction.html','metaverse','cyber','lemon-academy','拍卖行',
        hero('💰','龙墟拍卖行','稀有装备·限定道具·传说使魔')+
        '<section class="section"><div class="tabs"><button class="tab active">🔥热门</button><button class="tab">⚔️装备</button><button class="tab">🧪药水</button><button class="tab">📜卷轴</button></div><div class="grid-3">'+
        ''.join([f'<div class="card-academy-premium card-shimmer reveal"><div style="display:flex;align-items:center;gap:12px"><div style="width:60px;height:60px;border-radius:12px;background:linear-gradient(135deg,{c1},{c2});display:flex;align-items:center;justify-content:center;font-size:2rem">{e}</div><div><h4>{n}</h4><p style="color:var(--text-muted);font-size:0.8rem">{r}</p></div></div><div style="display:flex;justify-content:space-between;align-items:center;margin-top:12px"><div><span style="font-weight:800;color:var(--accent)">¥{b}</span><br><span style="font-size:0.7rem;color:var(--text-muted)">{bc}次·⏱️{t}</span></div><button class="btn btn-sm btn-accent btn-ripple">出价</button></div></div>'
        for c1,c2,e,n,r,b,bc,t in [('#fbbf24','#f59e0b','⚔️','龙渊之剑','传说·攻击+999','8,500','128','2分'),
        ('#a78bfa','#7c3aed','🛡️','不灭之盾','史诗·防御+666','5,200','89','15分'),
        ('#ff6b9d','#ff8fab','🧪','不死鸟之泪','传说·全回复','3,800','234','45分'),
        ('#4ecdc4','#44a08d','📜','时空禁咒卷轴','传说·暂停5秒','6,400','67','1时'),
        ('#34d399','#059669','💍','龙语者戒指','史诗·龙语+50','2,900','156','2时'),
        ('#60a5fa','#3b82f6','👑','浮空城冠冕','限定·全属性+10%','9,999','312','3时')]])+'</div></section>')

    # 时装秀
    make_page(f'{P}/fashion-show.html','metaverse','anime','sakura-academy','时装秀场',
        hero('✨','龙墟时装秀场','每季更新的虚拟时装')+
        '<section class="section"><div class="tabs"><button class="tab active">🌸春</button><button class="tab">☀️夏</button><button class="tab">🍂秋</button><button class="tab">❄️冬</button></div><div class="grid-4">'+
        ''.join([f'<div class="card-anime card-shimmer reveal"><div class="card-anime-img" style="background:linear-gradient(135deg,{c1},{c2});display:flex;align-items:center;justify-content:center;font-size:3.5rem">{e}</div><div class="card-anime-body"><h4>{n}</h4><p style="color:var(--text-muted);font-size:0.8rem">{d}</p><div style="display:flex;justify-content:space-between;align-items:center;margin-top:8px"><span style="font-weight:800;color:var(--accent)">¥{p}</span><span class="tag {tg}">{l}</span></div><button class="btn btn-sm btn-kawaii btn-ripple" style="margin-top:8px;width:100%">🛍️购买</button></div></div>'
        for c1,c2,e,n,d,p,tg,l in [('#ff6b9d','#ff8fab','🌸','樱花和风套装','含专属动作','128','tag-pink','限定'),
        ('#4ecdc4','#44a08d','🧜','深海人鱼尾裙','绝美渐变特效','198','tag-blue','稀有'),
        ('#a78bfa','#7c3aed','🌙','月下蝶舞长裙','黑夜发光魔法裙','268','tag-purple','传说'),
        ('#fbbf24','#f59e0b','⚡','雷神战甲','特效拉满酷炫','168','tag-orange','史诗'),
        ('#34d399','#059669','🧝','精灵森林绿裙','自然之力','138','tag-green','套装'),
        ('#60a5fa','#3b82f6','❄️','冰晶女王礼服','雪花飘落特效','228','tag-blue','传说'),
        ('#f472b6','#ec4899','🎀','魔法少女变身服','含变身动画','158','tag-pink','限定'),
        ('#fb923c','#f97316','🔥','炎之礼服','烈焰环绕','188','tag-orange','史诗')]])+'</div></section>')
    print('  [OK] 龙墟世界 7页')

# ===== 数字人学院 DIGITAL-HUMAN (8页) =====
def build_digital_human():
    P='digital-human'
    # 建模工坊
    make_page(f'{P}/modeling.html','digital-human','cyber','starlight-academy','数字人建模',
        hero('🧬','数字人建模工坊','从零创建专属数字人形象','<div style="margin-top:12px"><span class="online-badge"><span class="live-dot"></span>在线建模:1,245人</span></div>')+
        '<section class="section"><div class="section-title">🔧建模工作流</div><div class="grid-3">'+
        ''.join([f'<div class="card-academy-premium reveal"><div style="font-size:3rem;text-align:center;margin-bottom:12px">{e}</div><h3 style="text-align:center">{n}</h3><p style="color:var(--text-muted);font-size:0.85rem;text-align:center">{d}</p><div class="progress-bar" style="margin:12px 0"><div class="progress-fill" style="width:{p}%"></div></div><span style="font-size:0.7rem;color:var(--text-muted)">{inf}</span><div style="text-align:center"><button class="btn btn-sm btn-accent btn-ripple" style="margin-top:8px">{b}</button></div></div>'
        for e,n,d,p,inf,b in [('📷','Step1:照片采集','上传3张照片AI提取特征',100,'128特征点·精度0.1mm','开始采集'),
        ('🧬','Step2:3D重建','NeRF/Gaussian Splatting',0,'约30秒·50K-200K面片','开始重建'),
        ('🎨','Step3:精修定制','调整发型/服装/肤色/表情',0,'200+可调参数·实时预览','开始精修')]])+
        '</section><section class="section"><div class="section-title">🏗️技术架构</div><div class="grid-2"><div class="card card-shimmer reveal"><h4>🧠AI驱动技术栈</h4><div style="margin-top:12px">'+
        ''.join([f'<div style="display:flex;justify-content:space-between;margin-bottom:8px"><span>{t}</span><span style="color:var(--accent)">{v}</span></div>' 
        for t,v in [('NeRF神经辐射场','v3.2'),('3DGaussianSplatting','latest'),('StableDiffusionInpainting','XL'),('Metahuman兼容','UE5.4'),('BlendShape表情','52维')]])+
        '</div></div><div class="card card-shimmer reveal"><h4>🎯输出格式</h4><div style="display:flex;gap:6px;flex-wrap:wrap;margin-top:12px"><span class="tag tag-blue">.fbx</span><span class="tag tag-green">.glb</span><span class="tag tag-purple">.vrm</span><span class="tag tag-pink">.usd</span><span class="tag tag-orange">.obj</span><span class="tag tag-accent">.blend</span></div><p style="color:var(--text-muted);font-size:0.8rem;margin-top:12px">支持导出Unity/UE/Blender/VRoid/VRChat</p></div></div></section>')

    # VTuber
    make_page(f'{P}/vtuber.html','digital-human','anime','sakura-academy','虚拟主播',
        hero('🎬','虚拟主播工作室','面部捕捉·表情驱动·直播')+
        '<section class="section"><div class="glass-crystal" style="padding:32px;border-radius:24px;text-align:center;max-width:600px;margin:0 auto"><div style="width:100px;height:100px;border-radius:50%;background:linear-gradient(135deg,#ff6b9d,#a78bfa);margin:0 auto 16px;display:flex;align-items:center;justify-content:center;font-size:3rem">🎤</div><h3>你的虚拟主播形象</h3><p style="color:var(--text-muted)">未配置摄像头</p><div style="display:flex;gap:12px;justify-content:center;margin-top:16px;flex-wrap:wrap"><button class="btn btn-kawaii btn-ripple">📷摄像头</button><button class="btn btn-accent btn-ripple">🎙️麦克风</button><button class="btn btn-outline btn-ripple">🎭换形象</button></div><div style="margin-top:16px"><span class="tag tag-accent">FaceMesh478点</span><span class="tag tag-blue">52维BlendShape</span><span class="tag tag-green">60FPS</span></div></div></section>'+
        '<section class="section"><div class="section-title">🌟推荐虚拟主播</div><div class="grid-4">'+''.join([f'<div class="card-anime card-shimmer reveal" style="text-align:center"><div style="width:72px;height:72px;border-radius:50%;background:linear-gradient(135deg,{c1},{c2});margin:0 auto 12px;font-size:2rem;display:flex;align-items:center;justify-content:center">{e}</div><h4>{n}</h4><p style="color:var(--text-muted);font-size:0.8rem">{d}</p><div style="margin:8px 0"><span class="online-badge"><span class="live-dot"></span>{s}</span></div><div><span style="font-size:0.75rem;color:var(--text-muted)">👥{f}</span></div><button class="btn btn-sm btn-kawaii btn-ripple" style="margin-top:8px">进入直播间</button></div>'
        for c1,c2,e,n,d,s,f in [('#ff6b9d','#ff8fab','🌸','樱月奈奈','治愈系歌势','直播中','125K'),('#4ecdc4','#44a08d','⚔️','剑持雷电','高燃操作','直播中','89K'),
        ('#a78bfa','#7c3aed','📚','星野文学','深夜电台','即将开播','234K'),('#fbbf24','#f59e0b','🎮','VR KING','高技术力','休息中','456K'),
        ('#34d399','#059669','🎨','画师小绿','绘画直播','直播中','67K'),('#60a5fa','#3b82f6','🎵','冰晶歌姬','原创曲','准备中','198K'),
        ('#f472b6','#ec4899','💃','舞动美咲','3D动捕','直播中','312K'),('#fb923c','#f97316','🧪','科学少女Atom','科普实验','直播中','78K')]])+'</div></section>')

    # 动捕技术
    make_page(f'{P}/mocap-tech.html','digital-human','cyber','starlight-academy','动作捕捉技术',
        hero('🎯','动作捕捉技术','从摄像头到全身动捕')+
        '<section class="section"><div class="table-wrap"><table><tr><th>方案</th><th>精度</th><th>成本</th><th>延迟</th><th>场景</th><th>状态</th></tr>'+
        ''.join([f'<tr><td><strong>{n}</strong></td><td>{"⭐"*a}</td><td>{c}</td><td>{l}</td><td>{s}</td><td><span class="tag {tc}">{st}</span></td></tr>'
        for n,a,c,l,s,tc,st in [('MediaPipe单摄',3,'免费','~15ms','半身/面部','tag-green','已上线'),('MoveNet姿态',4,'免费','~10ms','全身33点','tag-green','已上线'),
        ('iPhoneARKit',5,'设备成本','~5ms','面部52维','tag-green','已上线'),('Kinectv2',4,'¥800','~20ms','全身25点','tag-blue','测试中'),
        ('XSens惯性',5,'¥50K+','~5ms','专业全身','tag-purple','支持'),('OptiTrack光学',5,'¥100K+','~2ms','影视级','tag-purple','支持'),
        ('RokokoSmartsuit',4,'¥20K+','~10ms','全身IMU','tag-blue','测试中')]])+'</table></div></section>'+
        '<section class="section"><div class="section-title">🎓从零开始教程</div><div class="grid-2"><div class="card-academy-premium reveal"><h4>📹单摄像头方案</h4><p style="color:var(--text-muted)">普通摄像头实现上半身姿态+表情追踪</p><div class="progress-bar" style="margin:12px 0"><div class="progress-fill" style="width:100%"></div></div><span style="font-size:0.75rem;color:var(--text-muted)">难度⭐⭐·89%完成</span><button class="btn btn-sm btn-accent btn-ripple" style="margin-top:8px">开始学习▸</button></div><div class="card-academy-premium reveal"><h4>📱iPhoneTrueDepth</h4><p style="color:var(--text-muted)">FaceID模组影视级面部捕捉</p><div class="progress-bar" style="margin:12px 0"><div class="progress-fill" style="width:72%"></div></div><span style="font-size:0.75rem;color:var(--text-muted)">难度⭐⭐⭐·72%完成</span><button class="btn btn-sm btn-accent btn-ripple" style="margin-top:8px">开始学习▸</button></div></div></section>')

    # 情感AI
    make_page(f'{P}/emotion-ai.html','digital-human','void','lavender-academy','情感AI引擎',
        hero('💗','情感AI引擎','让数字人理解并表达情感')+
        '<section class="section"><div class="section-title">🎭情感维度</div><div class="grid-3">'+''.join([f'<div class="card-academy-premium reveal" style="text-align:center"><div style="font-size:3rem;margin-bottom:12px">{e}</div><h3>{n}</h3><div style="display:flex;gap:4px;justify-content:center;flex-wrap:wrap;margin:8px 0">{tg}</div><p style="color:var(--text-muted);font-size:0.8rem">{d}</p></div>'
        for e,n,tg,d in [('😊','基础情绪','<span class="tag tag-pink">开心</span><span class="tag tag-blue">悲伤</span><span class="tag tag-orange">愤怒</span><span class="tag tag-purple">惊讶</span><span class="tag tag-green">恐惧</span><span class="tag tag-accent">厌恶</span>','7种·Ekman模型'),
        ('🎯','复合情绪','<span class="tag tag-pink">泪笑</span><span class="tag tag-orange">羡慕嫉妒</span><span class="tag tag-purple">紧张期待</span><span class="tag tag-blue">怀旧感动</span>','24种·Plutchik模型'),
        ('🤖','AI情绪识别','<span class="tag tag-green">语音语调</span><span class="tag tag-accent">文本情感</span><span class="tag tag-blue">微表情</span><span class="tag tag-pink">肢体语言</span>','多模态融合·93.7%')]])+
        '</section><section class="section"><div class="section-title">📊情感表达系统</div><div class="grid-2"><div class="card card-shimmer reveal"><h4>🎙️语音情绪分析</h4><p style="color:var(--text-muted)">Wav2Vec2模型实时分析语调语速停顿</p><span class="tag tag-accent">延迟50ms·准确率91%</span></div><div class="card card-shimmer reveal"><h4>📝文本情感计算</h4><p style="color:var(--text-muted)">BERT中文情感模型识别8类情感</p><span class="tag tag-accent">延迟20ms·准确率95%</span></div></div></section>')

    # 场景工坊
    make_page(f'{P}/scene-studio.html','digital-human','cyber','sunset-academy','场景工坊',
        hero('🎬','数字人场景工坊','创建专属舞台/直播间/互动场景')+
        '<section class="section"><div class="section-title">🏗️预置场景模板</div><div class="grid-3">'+''.join([f'<div class="card-academy-premium card-shimmer reveal"><div style="height:120px;border-radius:12px;background:linear-gradient(135deg,{c1},{c2});display:flex;align-items:center;justify-content:center;font-size:3rem;margin-bottom:12px">{e}</div><h4>{n}</h4><p style="color:var(--text-muted);font-size:0.8rem">{d}</p><div style="margin-top:8px"><span class="tag tag-accent">{s}</span><span class="tag tag-blue">{i}道具</span></div><button class="btn btn-sm btn-accent btn-ripple" style="margin-top:8px">使用▸</button></div>'
        for c1,c2,e,n,d,s,i in [('#ff6b9d','#ff8fab','🌸','樱花教室','日本高中教室场景','中型','45'),('#4ecdc4','#44a08d','🎤','专业直播间','灯光/绿幕/提词器','大型','78'),
        ('#a78bfa','#7c3aed','🌌','星空舞台','360°全景粒子特效','大型','92'),('#fbbf24','#f59e0b','🏯','赛博神社','赛博朋克和风','中型','56'),
        ('#34d399','#059669','🌿','魔法森林','发光植物·漂浮粒子','大型','64'),('#60a5fa','#3b82f6','🚀','太空舱','科幻未来空间','小型','28')]])+'</div></section>')

    # 数字人社区
    make_page(f'{P}/community.html','digital-human','cyber','starlight-academy','数字人社区',
        hero('👥','数字人创作者社区','交流建模·分享动捕·展示作品')+stat_row([('15,430','创作者'),('89,200','已创建'),('3,456','本月新增')])+
        '<section class="section"><div class="grid-2">'+''.join([f'<div class="card card-shimmer reveal"><h4>💡{t}</h4><p style="color:var(--text-muted);margin:8px 0">{d}</p><div style="display:flex;gap:12px;font-size:0.8rem;color:var(--text-muted)"><span>👤{a}</span><span>💬{c}</span><span>❤️{l}</span></div></div>'
        for t,d,a,c,l in [('Blender做日系二次元角色','从建模到材质到渲染完整流程','CG小达人','256','1.2k'),
        ('VRM格式数字人表情优化','52个BlendShape调教心得','技术宅','189','890'),
        ('动作捕捉装备选购指南2025','入门到专业各价位推荐','动捕研究员','412','2.1k'),
        ('数字人直播经验踩坑分享','设备配置·网络优化·互动','Vtuber前线','534','3.4k'),
        ('UE5实时数字人渲染','Nanite+Lumen全流程','引擎开发','328','1.8k'),
        ('StyleGAN生成二次元形象','AI辅助角色设计','AI设计','267','1.5k')]])+'</div></section>')
    print('  [OK] 数字人学院 8页')

# ===== 创作者学院 (3页) =====
def build_creator():
    P='creator'
    make_page(f'{P}/studio.html','creator','academy','sky-academy','创作者工作室',
        hero('🎬','创作者工作室','发布动画·漫画·小说·音乐')+stat_row([('89,200','创作者'),('256万','作品'),('¥1.2亿','收入')])+
        '<section class="section"><div class="glass-crystal" style="padding:32px;border-radius:24px;max-width:700px;margin:0 auto"><div class="grid-3" style="text-align:center">'+
        ''.join([f'<div class="reveal" style="padding:16px;cursor:pointer"><div style="font-size:3rem;margin-bottom:8px">{e}</div><h4>{n}</h4><p style="color:var(--text-muted);font-size:0.8rem">{d}</p><button class="btn btn-sm btn-accent btn-ripple" style="margin-top:8px">上传</button></div>'
        for e,n,d in [('🎬','视频','动画/MAD/AMV'),('📖','漫画','页漫/条漫/四格'),('📝','小说','轻小说/同人'),('🎵','音乐','原创/翻唱/编曲'),('🎨','插画','壁纸/角色设计'),('🎮','游戏','独立游戏/MOD')]])+
        '</div></div></section>')

    make_page(f'{P}/revenue.html','creator','academy','mint-academy','创作收益',
        hero('💰','创作收益中心','你的创作我们帮你变现')+stat_row([('¥12,580','本月收入'),('4,230','付费粉丝'),('89','本月作品'),('¥2.96','千次播放')])+
        '<section class="section"><div class="section-title">📊收益来源</div><div class="grid-3">'+''.join([f'<div class="card-academy-premium reveal"><div style="font-size:2.5rem;margin-bottom:8px">{e}</div><h4>{n}</h4><p style="color:var(--text-muted)">{d}</p><div style="margin-top:8px"><span style="font-size:1.2rem;font-weight:800;color:var(--accent)">{a}</span></div></div>'
        for e,n,d,a in [('🎬','视频播放收益','播放量+互动率','¥5,680'),('⭐','会员订阅','付费粉丝分成','¥3,420'),('🎁','打赏','观众直接打赏','¥2,180'),
        ('🛍️','周边分成','联名周边','¥890'),('📢','广告合作','品牌推广','¥1,200'),('🎫','活动收入','线上线下','¥1,210')]])+'</div></section>')
    print('  [OK] 创作者学院 2页')

# ===== 学科学院 (4页) =====
def build_academy():
    P='academy'
    make_page(f'{P}/courses.html','academy','academy','sakura-academy','课程中心',
        hero('📚','课程中心','从绘画到编程·培养全能创作者')+stat_row([('856','课程'),('12,450','学员'),('96.8%','好评'),('38','讲师')])+
        '<section class="section"><div class="section-title">🔥热门课程</div><div class="grid-4">'+''.join([f'<div class="card-academy-premium card-shimmer reveal"><div style="font-size:2.5rem;margin-bottom:8px">{e}</div><h4>{n}</h4><p style="color:var(--text-muted);font-size:0.8rem">{d}</p><div style="margin:8px 0"><span class="tag tag-accent">{l}课时</span><span class="tag tag-pink">{s}人</span></div><div style="display:flex;justify-content:space-between;align-items:center"><span style="font-weight:800;color:var(--accent)">{p}</span><button class="btn btn-sm btn-accent btn-ripple">报名</button></div></div>'
        for e,n,d,l,s,p in [('🎨','二次元角色设计','线条到色彩系统教程','24','8,920','免费'),('🎬','动画制作基础','原画·动画·后期','36','6,450','¥299'),
        ('🎤','声优配音特训营','发声·情感·角色配音','18','4,230','¥599'),('🎵','动漫配乐作曲','和弦到编曲','30','3,120','¥399'),
        ('🎮','Unity游戏开发','C#开发第一个游戏','48','9,870','¥499'),('✍️','轻小说写作指南','世界观·角色·情节','20','5,670','¥199'),
        ('🤖','AI绘画入门','SD+Midjourney','16','12,340','免费'),('💻','Python编程基础','零基础数据分析','40','15,670','免费')]])+'</div></section>')

    make_page(f'{P}/projects.html','academy','academy','mint-academy','实战项目',
        hero('🔬','实战项目','边学边做完整实践')+
        '<section class="section"><div class="section-title">🚀进行中项目</div><div class="grid-3">'+''.join([f'<div class="card-academy-premium card-shimmer reveal"><div style="font-size:2rem;margin-bottom:8px">{e}</div><h4>{n}</h4><p style="color:var(--text-muted);font-size:0.85rem">{d}</p><div style="margin-top:8px"><span class="tag tag-accent">{t}团队</span><span class="tag tag-blue">{m}人</span></div><div class="progress-bar" style="margin:8px 0"><div class="progress-fill" style="width:{pg}%"></div></div><span style="font-size:0.75rem;color:var(--text-muted)">{pg}%·截止:{dl}</span><button class="btn btn-sm btn-accent btn-ripple" style="margin-top:8px;width:100%">加入</button></div>'
        for e,n,d,t,m,pg,dl in [('🎬','制作3分钟原创动画','脚本到成片全流程','12','156','78','8.15'),('🎮','开发同人视觉小说','分支剧情+配音+Live2D','8','89','45','9.30'),
        ('🎵','创作动画OST专辑','10首曲目+编曲+混音','5','42','62','8.1'),('📖','合著异世界轻小说','多人协作+插画配图','6','67','35','10.15'),
        ('🎨','绘制100张角色卡','统一世界观角色设计','15','234','23','12.1'),('🤖','训练动漫AI模型','LoRA微调专属模型','4','28','56','7.20')]])+'</div></section>')

    make_page(f'{P}/mentors.html','academy','academy','lavender-academy','导师团队',
        hero('👨‍🏫','导师团队','行业资深专家护航')+stat_row([('38','签约导师'),('15年','平均经验'),('156','合作企业'),('92%','就业率')])+
        '<section class="section"><div class="grid-3">'+''.join([f'<div class="card-academy-premium reveal" style="text-align:center"><div style="width:80px;height:80px;border-radius:50%;background:linear-gradient(135deg,{c1},{c2});margin:0 auto 16px;display:flex;align-items:center;justify-content:center;font-size:2.2rem">{e}</div><h3>{n}</h3><p style="color:var(--accent);font-size:0.9rem">{t}</p><p style="color:var(--text-muted);font-size:0.8rem;margin:8px 0">{d}</p><div style="margin-top:8px">{tg}</div><button class="btn btn-sm btn-ghost btn-ripple" style="margin-top:12px">查看课程▸</button></div>'
        for c1,c2,e,n,t,d,tg in [('#ff6b9d','#ff8fab','🎨','陈樱花','资深角色设计师','前吉卜力·千与千寻/哈尔','<span class="tag tag-pink">25年</span><span class="tag tag-blue">3门课</span>'),
        ('#4ecdc4','#44a08d','🎬','李动画','动画导演','执导3部动画电影','<span class="tag tag-green">15年</span><span class="tag tag-blue">2门课</span>'),
        ('#a78bfa','#7c3aed','🎤','王声优','资深配音演员','配音200+角色','<span class="tag tag-purple">18年</span><span class="tag tag-blue">4门课</span>'),
        ('#fbbf24','#f59e0b','🎵','林作曲','动漫配乐作曲家','50+部动画配乐','<span class="tag tag-orange">20年</span><span class="tag tag-blue">3门课</span>'),
        ('#34d399','#059669','💻','张编程','Unity技术专家','独立游戏开发者','<span class="tag tag-green">12年</span><span class="tag tag-blue">5门课</span>'),
        ('#60a5fa','#3b82f6','🤖','赵智能','AI技术研究员','多模态生成技术','<span class="tag tag-accent">8年</span><span class="tag tag-blue">3门课</span>')]])+'</div></section>')
    print('  [OK] 学科学院 3页')

# ===== 活动学院 (3页) =====
def build_events():
    P='events'
    make_page(f'{P}/convention.html','events','anime','sakura-academy','漫展大全',
        hero('🎪','漫展大全','全国动漫展会一站式查询')+
        '<section class="section"><div class="grid-3">'+''.join([f'<div class="card-academy-premium card-shimmer reveal"><div style="height:100px;border-radius:12px;background:linear-gradient(135deg,{c1},{c2});display:flex;align-items:center;justify-content:center;font-size:3rem;margin-bottom:12px">{e}</div><div style="display:flex;gap:8px;margin-bottom:8px"><span class="tag tag-pink">{dt}</span><span class="tag tag-blue">{ct}</span></div><h4>{n}</h4><p style="color:var(--text-muted);font-size:0.8rem">{d}</p><div style="margin-top:8px"><span style="font-weight:800;color:var(--accent)">{p}</span><span style="font-size:0.75rem;color:var(--text-muted)">·{s}</span></div><button class="btn btn-sm btn-kawaii btn-ripple" style="margin-top:8px;width:100%">🎫购票</button></div>'
        for c1,c2,e,dt,ct,n,d,p,s in [('#ff6b9d','#ff8fab','🎌','7.15-17','广州','CP45魔都同人祭','年度最大·2000+摊位','¥128起','已售68%'),
        ('#4ecdc4','#44a08d','🎭','8.2-4','上海','ChinaJoy2025','全球数字娱乐博览会','¥180起','已售42%'),
        ('#a78bfa','#7c3aed','🎪','7.22-24','成都','成都CD27','西南最大同人展','¥88起','已售55%'),
        ('#fbbf24','#f59e0b','🗼','8.12-14','北京','北京IDO39','北方最大嘉年华','¥128起','已售36%'),
        ('#34d399','#059669','🌸','9.1-3','杭州','杭州CP14','江浙沪年度聚会','¥98起','已售28%'),
        ('#60a5fa','#3b82f6','🌏','8.18-20','深圳','深圳动漫节','大湾区最大','¥88起','已售31%')]])+'</div></section>')

    make_page(f'{P}/tournament.html','events','cyber','sunset-academy','赛事中心',
        hero('🏆','赛事中心','各类创作/电竞/Cosplay大赛')+
        '<section class="section"><div class="section-title">🏅进行中比赛</div><div class="grid-2">'+''.join([f'<div class="card-academy-premium card-shimmer reveal" style="display:flex;align-items:center;gap:16px"><div style="width:60px;height:60px;border-radius:14px;background:linear-gradient(135deg,{c1},{c2});display:flex;align-items:center;justify-content:center;font-size:1.8rem;flex-shrink:0">{e}</div><div style="flex:1"><h4>{n}</h4><p style="color:var(--text-muted);font-size:0.8rem">{d}</p><div style="margin-top:4px"><span class="tag tag-accent">🥇¥{p}</span><span class="tag tag-blue">{en}人</span><span style="font-size:0.7rem;color:var(--text-muted);margin-left:8px">⏱️{dl}</span></div><button class="btn btn-sm btn-accent btn-ripple" style="margin-top:8px">报名</button></div></div>'
        for c1,c2,e,n,d,p,en,dl in [('#ff6b9d','#ff8fab','🎨','龙奕原创插画大赛','主题:龙与少女','50,000','1,245','7.30截止'),
        ('#4ecdc4','#44a08d','🎬','最佳动画短片奖','5分钟原创/同人','30,000','328','8.15截止'),
        ('#a78bfa','#7c3aed','🎤','声优之王配音大赛','自选片段表演','20,000','567','8.1截止'),
        ('#fbbf24','#f59e0b','📖','异世界小说大赛','短篇/中篇异世界','15,000','423','8.30截止'),
        ('#34d399','#059669','🎮','龙奕电竞杯Summer','LOL/原神/APEX','100,000','2,340','7.25截止'),
        ('#60a5fa','#3b82f6','🎵','原创动漫音乐大赛','OP/ED/BGM原创','25,000','189','8.10截止')]])+'</div></section>')
    print('  [OK] 活动学院 2页')

# ===== Wiki学院 (3页) =====
def build_wiki():
    P='wiki'
    make_page(f'{P}/anime-list.html','wiki','academy','lavender-academy','番剧大全',
        hero('📺','番剧大全','完整动漫数据库')+stat_row([('28,450','收录番剧'),('4,832','角色条目'),('+300','月新增')])+
        '<section class="section"><div class="input-group-glass" style="max-width:500px;margin:0 auto 24px"><input type="text" placeholder="搜索番剧..."><button>搜索</button></div><div class="grid-4">'+
        ''.join([f'<div class="card-anime card-shimmer reveal"><div class="card-anime-img" style="background:linear-gradient(135deg,{c1},{c2});display:flex;align-items:center;justify-content:center;font-size:3rem">{e}</div><div class="card-anime-body"><h4>{n}</h4><p style="color:var(--text-muted);font-size:0.8rem">{y}·{ep}·评分<span style="color:#fbbf24">{sc}</span></p><div style="margin-top:6px">{tg}</div></div></div>'
        for c1,c2,e,n,y,ep,sc,tg in [('#ff6b9d','#ff8fab','🌸','鬼灭之刃','2019-2024','63话','9.2','<span class="tag tag-pink">热血</span><span class="tag tag-blue">战斗</span>'),
        ('#4ecdc4','#44a08d','⚔️','进击的巨人','2013-2023','94话','9.1','<span class="tag tag-orange">黑暗</span><span class="tag tag-purple">悬疑</span>'),
        ('#a78bfa','#7c3aed','🌀','命运石之门','2011','24话','9.3','<span class="tag tag-green">科幻</span><span class="tag tag-accent">时间</span>'),
        ('#fbbf24','#f59e0b','🔥','咒术回战','2020-','48话','8.9','<span class="tag tag-pink">热血</span><span class="tag tag-purple">超自然</span>'),
        ('#34d399','#059669','⭐','紫罗兰永恒花园','2018','14话','8.8','<span class="tag tag-blue">治愈</span><span class="tag tag-pink">文艺</span>'),
        ('#60a5fa','#3b82f6','🎸','孤独摇滚!','2022','12话','8.7','<span class="tag tag-green">音乐</span><span class="tag tag-orange">日常</span>'),
        ('#f472b6','#ec4899','👻','ReZero','2016-','50话','8.6','<span class="tag tag-purple">奇幻</span><span class="tag tag-pink">悬疑</span>'),
        ('#fb923c','#f97316','🎭','间谍过家家','2022-','37话','8.8','<span class="tag tag-accent">喜剧</span><span class="tag tag-blue">家庭</span>')]])+'</div></section>')

    make_page(f'{P}/genre.html','wiki','academy','sunset-academy','动漫类型学',
        hero('📚','动漫类型学','了解各种动漫类型特点')+
        '<section class="section"><div class="tag-cloud" style="justify-content:center;margin-bottom:32px">'+''.join(f'<span class="tag-cloud-item">{t}</span>' for t in ['热血','治愈','科幻','奇幻','悬疑','日常','恋爱','搞笑','机战','运动','美食','音乐','历史','恐怖','异世界','校园','魔法少女'])+
        '</div><div class="grid-3">'+''.join([f'<div class="card-academy-premium card-shimmer reveal"><h4>{n}</h4><p style="color:var(--text-muted);font-size:0.85rem;margin:8px 0">{d}</p><div style="margin-top:8px"><span class="tag tag-blue">{c}部番剧</span></div><div style="margin-top:4px;font-size:0.75rem;color:var(--text-muted)">代表作:{e}</div></div>'
        for n,d,c,e in [('🔥热血','战斗·友情·成长',3200,'龙珠/火影/海贼/鬼灭/咒术'),('🌸治愈','温馨感人·心灵慰藉',1800,'紫罗兰/夏目/虫师'),
        ('🚀科幻','科学技术未来想象',890,'攻壳/石头门/PP'),('🏰奇幻','魔法·龙·异世界',2450,'Fate/ReZero/小圆'),
        ('🔍悬疑','层层谜题·推理',560,'死亡笔记/怪物'),('💕恋爱','青春爱情·甜蜜',2100,'你的名字/辉夜/月色真美'),
        ('😂搞笑','纯粹欢笑·喜剧',1600,'银魂/齐木楠雄/过家家'),('🌍异世界','转生/穿越',1200,'ReZero/史莱姆/无职'),
        ('🤖机战','巨型机器人',450,'高达/EVA/天元突破')]])+'</div></section>')

    make_page(f'{P}/industry.html','wiki','academy','coral-academy','动画产业研究',
        hero('🏭','动画产业研究','产业链·商业模式·趋势')+stat_row([('¥2.8万亿','全球市场'),('¥2,200亿','中国市场'),('35%','年增长'),('520','中国公司')])+
        '<section class="section"><div class="section-title">🏗️动画产业链</div><div style="display:flex;justify-content:center;flex-wrap:wrap;gap:16px;margin-bottom:32px">'+
        ''.join([f'<div class="card card-shimmer" style="text-align:center;padding:20px 24px"><div style="font-size:2rem">{e}</div><h4>{n}</h4><p style="color:var(--text-muted);font-size:0.75rem">{d}</p></div>'
        for e,n,d in [('📝','原作/IP','漫画·轻小说·游戏'),('💰','企划/投资','制作委员会'),('🎬','制作','原画·动画·CG'),('📺','播出/发行','TV·流媒体·影院'),('🛍️','衍生品','周边·BD·游戏'),('🌏','海外','出口·授权')]])+
        '</div><div class="grid-2"><div class="card card-shimmer reveal"><h4>📈行业趋势</h4><ul style="margin:12px 0 0 20px;line-height:2;font-size:0.9rem;color:var(--text-secondary)"><li>AI辅助制作渗透率→2026达60%</li><li>流媒体成主要播出渠道</li><li>中国动画出海加速·年均增40%</li><li>3DCG动画占比持续上升</li><li>虚拟制作技术普及</li></ul></div><div class="card card-shimmer reveal"><h4>💼就业方向</h4><ul style="margin:12px 0 0 20px;line-height:2;font-size:0.9rem;color:var(--text-secondary)"><li>原画师·¥12K-25K/月</li><li>3D建模师·¥15K-30K/月</li><li>动画导演·¥300K-800K/年</li><li>配音演员·按集/时计费</li><li>制片管理·¥200K-500K/年</li></ul></div></div></section>')
    print('  [OK] Wiki学院 3页')

print('='*50)
print('第二批: 生成龙墟世界/数字人/创作者/学院/活动/Wiki')
print('='*50)
build_metaverse()
build_digital_human()
build_creator()
build_academy()
build_events()
build_wiki()
print('='*50)
print('全部完成!')

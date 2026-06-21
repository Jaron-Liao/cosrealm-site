#!/usr/bin/env python3
"""龙奕学院 — 批量页面生成器 v2"""
import os
BASE = r"C:\Users\28767\Downloads\cosrealm-site"
TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN" data-3d="{scene}">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title} — 龙奕学院</title>
<link rel="stylesheet" href="../../assets/style.css">
<link rel="stylesheet" href="../../assets/themes/academy/{theme}.css">
<style>{extra_css}</style>
</head>
<body>
<div class="page-wrap">
<div class="page-hero"><span class="hero-emoji">{emoji}</span><h1>{title}</h1><p>{subtitle}</p></div>
<div class="section">
{content}
</div>
<footer class="footer"><div class="footer-inner"><div class="footer-brand">&copy;2026 <strong>龙奕学院 LongYi Academy</strong> — 广州龙奕无形科技文化有限公司</div><div class="footer-links"><a href="../../pages/meta/about.html">关于我们</a><a href="../../pages/meta/privacy.html">隐私政策</a><a href="../../pages/help/faq.html">帮助中心</a></div></div></footer>
</div>
<script src="../../assets/three-engine.js"></script><script src="../../assets/nav.js"></script>
<script>{js}</script>
</body>
</html>'''

def pg(path, title, emoji, subtitle, theme, scene, extra_css, content, js):
    d = os.path.dirname(path); os.makedirs(d, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(TEMPLATE.format(title=title, emoji=emoji, subtitle=subtitle, theme=theme, scene=scene, extra_css=extra_css, content=content, js=js))

# ======== SOCIAL EXTENDED (4) ========
pg(f'{BASE}/pages/social/club.html', '社团', '🏘️', '加入社团 · 找到同好 · 一起创作',
   'sky-academy', 'academy', '',
   '''<div class="grid-3" id="clubGrid"></div><div class="card mt-4 text-center"><h3>🎨 创建你的社团</h3><p class="text-muted">召集志同道合的小伙伴，打造属于你们的天地</p><button class="btn btn-primary btn-lg mt-2">创建社团</button></div>''',
   '''const clubs=[{name:'Cosplay研究社',icon:'🎭',members:234,topic:'Cos',desc:'交流Cos技巧与心得',color:'#ff6b9d'},{name:'MAD剪辑部',icon:'✂️',members:156,topic:'MAD',desc:'AMV/MAD创作交流',color:'#4da6ff'},{name:'声优同好会',icon:'🎤',members:189,topic:'配音',desc:'配音练习与分享',color:'#8b5cf6'},{name:'绘画社',icon:'🎨',members:312,topic:'绘画',desc:'原创&同人绘画',color:'#f97316'},{name:'宅舞团',icon:'💃',members:145,topic:'舞蹈',desc:'宅舞排练与演出',color:'#34d399'},{name:'摄影部',icon:'📸',members:98,topic:'摄影',desc:'Cos摄影与后期',color:'#eab308'}];
document.getElementById('clubGrid').innerHTML=clubs.map(c=>`<div class="card text-center"><span style="font-size:2.5rem;display:block;">${c.icon}</span><h3>${c.name}</h3><p style="font-size:0.82rem;color:var(--text-muted);">${c.desc}</p><div class="flex flex-center gap-2 mt-2"><span class="tag tag-pink">${c.topic}</span><span>👥 ${c.members}人</span></div><button class="btn btn-sm btn-primary mt-2">加入社团</button></div>`).join('');''')

pg(f'{BASE}/pages/social/bbs.html', '论坛', '💬', '发帖讨论 · 分享心得 · 二次元话题无限',
   'lavender-academy', 'default', '',
   '''<div class="tabs mb-3"><button class="tab active">热门</button><button class="tab">最新</button><button class="tab">精华</button><button class="tab">我的</button></div><div id="bbsList"></div>
<div class="card mt-4"><h3>📝 发帖</h3><input class="form-input mb-2" type="text" placeholder="标题..."><textarea class="form-textarea" placeholder="分享你的想法..."></textarea><button class="btn btn-primary mt-2">发布</button></div>''',
   '''const posts=[{title:'【讨论】2026夏季新番你最期待哪一部？',author:'追番狂魔',replies:89,views:'3.2k',time:'2小时前',tags:['新番','讨论']},{title:'【教程】Cosplay化妆入门指南',author:'美妆达人小雪',replies:156,views:'8.9k',time:'5小时前',tags:['教程','Cos']},{title:'【分享】我的龙墟战记Cos服制作过程',author:'手作娘阿花',replies:234,views:'12.1k',time:'8小时前',tags:['分享','手作']},{title:'【投票】最喜欢的动画OP/ED评选',author:'音乐鉴赏部',replies:312,views:'5.6k',time:'12小时前',tags:['投票','音乐']},{title:'【求助】第一次参加漫展需要注意什么？',author:'萌新小白',replies:45,views:'1.8k',time:'1天前',tags:['求助','漫展']}];
document.getElementById('bbsList').innerHTML=posts.map(p=>`<div class="card mb-2" style="cursor:pointer;"><h3 style="font-size:1rem;">${p.title}</h3><div class="flex flex-wrap gap-3 mt-1" style="font-size:0.78rem;color:var(--text-muted);"><span>👤 ${p.author}</span><span>💬 ${p.replies}</span><span>👁 ${p.views}</span><span>🕐 ${p.time}</span></div><div class="flex gap-1 mt-1">${p.tags.map(t=>`<span class="tag tag-pink">${t}</span>`).join('')}</div></div>`).join('');
document.querySelectorAll('.tab').forEach(t=>t.addEventListener('click',function(){document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));this.classList.add('active');}));''')

pg(f'{BASE}/pages/social/match.html', '同好匹配', '💕', '兴趣匹配 · 找到与你灵魂共鸣的伙伴',
   'coral-academy', 'sakura', '',
   '''<div class="card-academy text-center mb-3"><h3>🔮 兴趣匹配引擎</h3><p class="text-muted">选择你的兴趣标签，AI为你推荐最佳匹配</p>
<div class="flex flex-wrap gap-2 justify-center mt-3" id="interestTags"></div><button class="btn btn-primary btn-lg mt-3" onclick="startMatch()">开始匹配</button></div>
<div class="grid-3" id="matchResults"></div>''',
   '''const interests=['Cosplay','动画','MAD制作','配音','绘画','宅舞','摄影','手作','游戏','V家','同人创作','虚拟主播','机甲','古风','赛博朋克'];
document.getElementById('interestTags').innerHTML=interests.map(i=>`<span class="tag tag-pink" style="cursor:pointer;font-size:0.85rem;" onclick="this.classList.toggle('tag-purple');this.classList.toggle('tag-pink');this.style.transform=this.classList.contains('tag-purple')?'scale(1.1)':'';">${i}</span>`).join('');
function startMatch(){const results=[{name:'星野あかり',match:'98%',bio:'Cosplay爱好者·龙墟厨',emoji:'⭐',color:'#ff6b9d'},{name:'剪辑师小林',match:'95%',bio:'MAD创作者·6年经验',emoji:'✂️',color:'#4da6ff'},{name:'画师小雪',match:'92%',bio:'插画师·同人画手',emoji:'🎨',color:'#8b5cf6'},{name:'声优练习生',match:'89%',bio:'配音爱好者·声控',emoji:'🎤',color:'#f97316'},{name:'宅舞少女',match:'87%',bio:'宅舞团成员·元气满满',emoji:'💃',color:'#34d399'},{name:'摄影达人',match:'85%',bio:'Cos摄影·后期精修',emoji:'📸',color:'#eab308'}];
document.getElementById('matchResults').innerHTML=`<div class="section-title">✨ 匹配结果</div>`+results.map(r=>`<div class="card text-center"><span style="font-size:2.5rem;display:block;">${r.emoji}</span><h4>${r.name}</h4><div class="stat-value" style="font-size:1.5rem;color:var(--accent);">${r.match}</div><p style="font-size:0.82rem;color:var(--text-muted);">${r.bio}</p><button class="btn btn-sm btn-primary mt-2">💬 打招呼</button></div>`).join('');}''')

pg(f'{BASE}/pages/social/live-room.html', '虚拟直播', '🎙️', '开启你的虚拟直播 · 与粉丝实时互动',
   'lemon-academy', 'anime', '',
   '''<div class="grid-2" id="liveGrid"></div>
<div class="card text-center mt-4"><h3>🎬 开启直播</h3><p class="text-muted">选择你的虚拟形象，一键开播</p>
<select class="form-input mt-2" style="max-width:300px;margin:0 auto;"><option>默认虚拟形象</option><option>猫耳少女</option><option>赛博忍者</option><option>魔法使</option></select>
<button class="btn btn-primary btn-lg mt-3">🔴 开始直播</button></div>''',
   '''const lives=[{host:'星野あかり',title:'新番吐槽大会',viewers:'2.3万',color:'linear-gradient(135deg,#ff6b9d,#c084fc)',emoji:'⭐',live:true},{host:'龙奕官方',title:'龙墟世界开发日志',viewers:'5.1万',color:'linear-gradient(135deg,#4da6ff,#818cf8)',emoji:'🐉',live:true},{host:'MAD大师',title:'AMV制作教学',viewers:'8,920',color:'linear-gradient(135deg,#f97316,#fbbf24)',emoji:'✂️',live:true},{host:'Cos达人小雪',title:'Cos妆容教程',viewers:'1.5万',color:'linear-gradient(135deg,#8b5cf6,#a78bfa)',emoji:'🎨',live:false}];
document.getElementById('liveGrid').innerHTML=lives.map(l=>`<div class="card-anime"><div style="height:200px;border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:3rem;background:${l.color};position:relative;">${l.emoji}${l.live?'<div class="live-badge" style="position:absolute;top:10px;left:10px;"><span class="live-dot"></span>LIVE</div>':''}</div><div class="card-anime-body"><h4>${l.title}</h4><p style="font-size:0.78rem;color:var(--text-muted);">🎙️ ${l.host} · 👁 ${l.viewers}</p></div></div>`).join('');''')

# ======== SHOP EXTENDED (5) ========
pg(f'{BASE}/pages/shop/flash.html', '限时抢购', '⚡', '限时特惠 · 手慢无 · 每天10点/20点',
   'coral-academy', 'cyber', '',
   '''<div id="flashTimer" class="text-center mb-3" style="font-size:2rem;font-weight:900;color:var(--accent);font-family:monospace;">--:--:--</div>
<div class="grid-3" id="flashGrid"></div>''',
   '''function updateFlash(){const now=new Date();const next=new Date(now);next.setHours(now.getHours()<10?10:now.getHours()<20?20:34,0,0,0);if(now>=next){next.setDate(next.getDate()+1);next.setHours(10,0,0,0);}const diff=next-now;const h=Math.floor(diff/3600000),m=Math.floor((diff%3600000)/60000),s=Math.floor((diff%60000)/1000);document.getElementById('flashTimer').textContent=`距下一场: ${String(h).padStart(2,'0')}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;}
const items=[{name:'限定·龙墟战记Cos服',orig:1299,now:399,discount:'69%',sold:'87%',color:'#4da6ff',emoji:'🐉'},{name:'魔法少女变身器',orig:599,now:199,discount:'67%',sold:'92%',color:'#ff6b9d',emoji:'⭐'},{name:'樱花庄Cos假发',orig:299,now:89,discount:'70%',sold:'76%',color:'#ff8fab',emoji:'🌸'},{name:'机甲战纪T恤',orig:199,now:59,discount:'70%',sold:'95%',color:'#6366f1',emoji:'🤖'},{name:'限定手办·星之声',orig:899,now:299,discount:'67%',sold:'63%',color:'#8b5cf6',emoji:'🎵'},{name:'龙之谷钥匙扣',orig:69,now:19,discount:'72%',sold:'81%',color:'#f97316',emoji:'🐲'}];
document.getElementById('flashGrid').innerHTML=items.map(it=>`<div class="card text-center"><span style="font-size:2.5rem;">${it.emoji}</span><h4>${it.name}</h4><div><span style="text-decoration:line-through;color:var(--text-muted);">¥${it.orig}</span> <span style="font-size:1.4rem;font-weight:800;color:#ef4444;">¥${it.now}</span></div><span class="tag tag-orange">-${it.discount}</span><div class="progress-bar mt-2"><div class="progress-fill" style="width:${it.sold};background:linear-gradient(90deg,#ef4444,#f97316);"></div></div><p style="font-size:0.7rem;color:var(--text-muted);">已售 ${it.sold}</p><button class="btn btn-sm btn-primary">⚡ 立即抢购</button></div>`).join('');
updateFlash();setInterval(updateFlash,1000);''')

pg(f'{BASE}/pages/shop/secondhand.html', '二手交易', '🔄', '闲置Cos服 · 手办回血 · 安全交易',
   'mint-academy', 'default', '',
   '''<div class="search-bar mb-3"><input class="form-input" type="text" placeholder="🔍 搜索闲置..."><button class="btn btn-primary">搜索</button></div>
<div class="tabs mb-3"><button class="tab active">最新</button><button class="tab">Cos服</button><button class="tab">手办</button><button class="tab">道具</button><button class="tab">假发</button></div>
<div class="grid-3" id="shGrid"></div>''',
   '''const items=[{name:'龙墟战记Cos服 9成新',price:299,seller:'龙墟退坑',cond:'9成新',color:'#4da6ff',emoji:'🐉'},{name:'魔法少女手办整套',price:599,seller:'回血达人',cond:'全新未拆',color:'#ff6b9d',emoji:'⭐'},{name:'樱花庄假发·长直',price:89,seller:'Cos达人',cond:'用过1次',color:'#ff8fab',emoji:'🌸'},{name:'道具·魔法杖',price:159,seller:'道具师',cond:'8成新',color:'#8b5cf6',emoji:'🪄'},{name:'机甲战纪限定挂画',price:199,seller:'收藏家小王',cond:'全新',color:'#6366f1',emoji:'🤖'},{name:'Cos鞋·黑色短靴',price:79,seller:'闲置处理',cond:'7成新',color:'#1a1a1a',emoji:'👢'}];
document.getElementById('shGrid').innerHTML=items.map(it=>`<div class="card"><span style="font-size:2rem;">${it.emoji}</span><h4>${it.name}</h4><div class="stat-value" style="font-size:1.2rem;">¥${it.price}</div><div class="flex gap-2 mt-1"><span class="tag tag-green">${it.cond}</span><span style="font-size:0.75rem;color:var(--text-muted);">by ${it.seller}</span></div><button class="btn btn-sm btn-outline mt-2">💬 联系卖家</button></div>`).join('');
document.querySelectorAll('.tab').forEach(t=>t.addEventListener('click',function(){document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));this.classList.add('active');}));''')

pg(f'{BASE}/pages/shop/custom.html', '定制工坊', '🔧', '量身定制 · 专属Cos服 · 来图定制',
   'lavender-academy', 'academy', '',
   '''<div class="grid-2" style="max-width:700px;margin:0 auto;">
<div class="card text-center"><span style="font-size:3rem;">👗</span><h3>Cos服定制</h3><p class="text-muted">来图定制，精准还原</p><button class="btn btn-primary mt-2">开始定制</button></div>
<div class="card text-center"><span style="font-size:3rem;">🛡️</span><h3>道具定制</h3><p class="text-muted">3D打印+手工制作</p><button class="btn btn-primary mt-2">开始定制</button></div>
<div class="card text-center"><span style="font-size:3rem;">💇</span><h3>假发定制</h3><p class="text-muted">角色还原发型设计</p><button class="btn btn-primary mt-2">开始定制</button></div>
<div class="card text-center"><span style="font-size:3rem;">👟</span><h3>鞋靴定制</h3><p class="text-muted">舒适+还原度兼具</p><button class="btn btn-primary mt-2">开始定制</button></div></div>
<div class="card mt-4"><h3>📋 我的定制订单</h3><p class="text-muted">还没有定制订单，快来创建吧！</p></div>''',
   '''document.querySelectorAll('.btn-primary').forEach(b=>b.addEventListener('click',()=>{alert('定制表单功能即将上线！');}));''')

pg(f'{BASE}/pages/shop/rental.html', 'Cos租赁', '👘', '租赁Cos服装 · 省钱又环保',
   'sakura-academy', 'sakura', '',
   '''<div class="grid-3" id="rentalGrid"></div>''',
   '''const items=[{name:'龙墟战记·主角服',price:99,period:'3天',size:'S/M/L',color:'#4da6ff',emoji:'🐉'},{name:'魔法少女·战斗服',price:79,period:'3天',size:'S/M',color:'#ff6b9d',emoji:'⭐'},{name:'樱花庄·和服',price:129,period:'5天',size:'均码',color:'#ff8fab',emoji:'🌸'},{name:'机甲战纪·驾驶服',price:149,period:'3天',size:'M/L',color:'#6366f1',emoji:'🤖'},{name:'龙之谷·盔甲',price:199,period:'5天',size:'L/XL',color:'#f97316',emoji:'🐲'},{name:'星之声·演出服',price:89,period:'3天',size:'S/M',color:'#8b5cf6',emoji:'🎵'}];
document.getElementById('rentalGrid').innerHTML=items.map(it=>`<div class="card text-center"><span style="font-size:2.5rem;">${it.emoji}</span><h4>${it.name}</h4><div class="stat-value" style="font-size:1.2rem;">¥${it.price}<span style="font-size:0.7rem;">/${it.period}</span></div><div class="flex flex-center gap-1 mt-1">${it.size.split('/').map(s=>`<span class="tag tag-pink">${s}</span>`).join('')}</div><button class="btn btn-sm btn-primary mt-2">📦 立即租赁</button></div>`).join('');''')

pg(f'{BASE}/pages/shop/points.html', '积分商城', '🎁', '签到赚积分 · 兑换限定好礼',
   'lemon-academy', 'default', '',
   '''<div class="flex flex-center gap-3 mb-3"><div class="stat-card"><div class="stat-value">2,850</div><div class="stat-label">我的积分</div></div><div class="stat-card"><div class="stat-value">7</div><div class="stat-label">连续签到</div></div></div>
<button class="btn btn-primary btn-lg mb-3" style="display:block;margin:0 auto 24px;" onclick="this.textContent='✅ 已签到 (+50积分)';this.disabled=true;">📅 今日签到 +50</button>
<div class="grid-3" id="pointsGrid"></div>''',
   '''const items=[{name:'限定头像框·龙',cost:500,stock:'限量200',color:'#4da6ff',emoji:'🖼️'},{name:'魔法特效·星之轨迹',cost:800,stock:'限量100',color:'#ff6b9d',emoji:'✨'},{name:'龙晶×100',cost:1000,stock:'不限量',color:'#34d399',emoji:'💎'},{name:'限定称号·学霸',cost:300,stock:'永久',color:'#f59e0b',emoji:'🏅'},{name:'虚拟宠物·小精灵',cost:2000,stock:'限量50',color:'#8b5cf6',emoji:'🧚'},{name:'Cos折扣券·50元',cost:1500,stock:'不限量',color:'#f97316',emoji:'🎫'}];
document.getElementById('pointsGrid').innerHTML=items.map(it=>`<div class="card text-center"><span style="font-size:2.5rem;">${it.emoji}</span><h4>${it.name}</h4><div style="font-weight:800;color:var(--accent);">💰 ${it.cost}积分</div><span class="tag tag-pink">${it.stock}</span><button class="btn btn-sm ${it.cost<=2850?'btn-primary':'btn-ghost'} mt-2" ${it.cost>2850?'disabled':''}>兑换</button></div>`).join('');''')

print("Social + Shop done (9 pages)")

# ======== CREATOR EXTENDED (3) ========
pg(f'{BASE}/pages/creator/income.html', '创作收益', '💰', '查看你的创作收益 · 数据分析 · 提现管理',
   'lemon-academy', 'default', '',
   '''<div class="grid-4 mb-3"><div class="stat-card"><div class="stat-value">¥12,580</div><div class="stat-label">本月收益</div></div><div class="stat-card"><div class="stat-value">¥3,240</div><div class="stat-label">待提现</div></div><div class="stat-card"><div class="stat-value">847</div><div class="stat-label">付费粉丝</div></div><div class="stat-card"><div class="stat-value">↑23%</div><div class="stat-label">环比增长</div></div></div>
<div class="card"><h3>💳 收益明细</h3><div class="table-wrap"><table><thead><tr><th>日期</th><th>来源</th><th>金额</th><th>状态</th></tr></thead><tbody><tr><td>2026-06-21</td><td>MAD作品打赏</td><td>¥580</td><td><span class="tag tag-green">已到账</span></td></tr><tr><td>2026-06-20</td><td>会员订阅</td><td>¥1,200</td><td><span class="tag tag-green">已到账</span></td></tr><tr><td>2026-06-19</td><td>广告分成</td><td>¥890</td><td><span class="tag tag-yellow">处理中</span></td></tr><tr><td>2026-06-18</td><td>定制订单</td><td>¥3,500</td><td><span class="tag tag-green">已到账</span></td></tr><tr><td>2026-06-17</td><td>直播礼物</td><td>¥2,100</td><td><span class="tag tag-green">已到账</span></td></tr></tbody></table></div></div>
<button class="btn btn-primary mt-3">💳 申请提现</button>''',
   '')  # Removed extra brace

pg(f'{BASE}/pages/creator/fans.html', '粉丝管理', '👥', '粉丝数据分析 · 互动管理 · 增长策略',
   'coral-academy', 'academy', '',
   '''<div class="grid-4 mb-3"><div class="stat-card"><div class="stat-value">12,847</div><div class="stat-label">总粉丝</div></div><div class="stat-card"><div class="stat-value">+342</div><div class="stat-label">本周新增</div></div><div class="stat-card"><div class="stat-value">68%</div><div class="stat-label">互动率</div></div><div class="stat-card"><div class="stat-value">847</div><div class="stat-label">铁粉</div></div></div>
<div class="card"><h3>👤 粉丝列表</h3>
<div id="fanList"></div></div>''',
   '''const fans=[{name:'追番小王',level:'铁粉',joined:'2025-03',interact:156,emoji:'⭐'},{name:'Cos爱好者',level:'活跃',joined:'2025-06',interact:89,emoji:'🎭'},{name:'剪辑新手',level:'新粉',joined:'2026-01',interact:23,emoji:'✂️'},{name:'画师大佬',level:'铁粉',joined:'2025-01',interact:234,emoji:'🎨'},{name:'龙墟死忠',level:'铁粉',joined:'2024-11',interact:312,emoji:'🐉'}];
document.getElementById('fanList').innerHTML=fans.map(f=>`<div style="display:flex;align-items:center;gap:12px;padding:10px 0;border-bottom:1px solid var(--border);"><span style="font-size:1.5rem;">${f.emoji}</span><div style="flex:1;"><strong>${f.name}</strong><div style="font-size:0.75rem;color:var(--text-muted);">加入: ${f.joined} · 互动: ${f.interact}次</div></div><span class="tag tag-purple">${f.level}</span></div>`).join('');''')

pg(f'{BASE}/pages/creator/tools.html', '创作工具', '🛠️', '专业创作工具集 · 提升效率',
   'starlight-academy', 'cyber', '',
   '''<div class="grid-3" id="toolGrid"></div>''',
   '''const tools=[{name:'AI绘画助手',desc:'一键生成角色立绘',icon:'🎨',color:'#ff6b9d'},{name:'视频剪辑器',desc:'在线剪辑，多轨道编辑',icon:'🎬',color:'#4da6ff'},{name:'音频处理',desc:'配音/混音/降噪',icon:'🎵',color:'#8b5cf6'},{name:'3D建模工具',desc:'虚拟场景搭建',icon:'🏗️',color:'#f97316'},{name:'动作捕捉',desc:'实时动作数据采集',icon:'🦴',color:'#34d399'},{name:'脚本生成器',desc:'AI辅助剧本创作',icon:'📝',color:'#eab308'}];
document.getElementById('toolGrid').innerHTML=tools.map(t=>`<div class="card text-center"><span style="font-size:2.5rem;">${t.icon}</span><h3>${t.name}</h3><p style="font-size:0.82rem;color:var(--text-muted);">${t.desc}</p><button class="btn btn-sm btn-primary mt-2">打开工具</button></div>`).join('');''')

print("Creator extended done (3 pages)")

# ======== DIGITAL-HUMAN + ACADEMY + EVENTS ========
# We'll write these as compact pages with essential functionality

for page in [
    ('ai-chat', 'AI角色对话', '🤖', '与虚拟角色实时对话 · AI情感引擎驱动', 'coral-academy', 'academy',
     '''<div style="max-width:600px;margin:0 auto;">
<div class="card mb-3" style="display:flex;gap:12px;align-items:center;"><span style="font-size:2rem;">⭐</span><div><h4>星野あかり</h4><p style="font-size:0.78rem;color:var(--text-muted);">元气少女 · 喜欢Cosplay和动画</p></div><span class="online-badge ml-auto">在线</span></div>
<div class="card" style="min-height:300px;display:flex;flex-direction:column;"><div style="flex:1;overflow-y:auto;max-height:300px;" id="chatBox">
<div style="text-align:right;margin:8px 0;"><div style="display:inline-block;background:var(--gradient-btn);color:#fff;padding:8px 14px;border-radius:14px 14px 4px 14px;max-width:80%;font-size:0.85rem;">你好！我叫星野あかり，很高兴认识你！</div></div>
<div style="text-align:left;margin:8px 0;"><div style="display:inline-block;background:var(--bg-card);border:1px solid var(--border);padding:8px 14px;border-radius:14px 14px 14px 4px;max-width:80%;font-size:0.85rem;">こんにちは！我超喜欢龙墟战记，你呢？</div></div></div>
<div style="display:flex;gap:8px;margin-top:12px;"><input class="form-input" placeholder="输入消息..." id="chatInput" onkeydown="if(event.key==='Enter')sendMsg()"><button class="btn btn-primary" onclick="sendMsg()">发送</button></div></div></div>''',
     '''function sendMsg(){const inp=document.getElementById('chatInput');const msg=inp.value.trim();if(!msg)return;const box=document.getElementById('chatBox');box.innerHTML+=`<div style="text-align:right;margin:8px 0;"><div style="display:inline-block;background:var(--gradient-btn);color:#fff;padding:8px 14px;border-radius:14px 14px 4px 14px;max-width:80%;font-size:0.85rem;">${msg}</div></div>`;inp.value='';setTimeout(()=>{const replies=['哇！我也是！','对对对！超有趣！','哈哈哈哈太搞笑了','你的想法好棒！','嗯嗯，继续说～'];box.innerHTML+=`<div style="text-align:left;margin:8px 0;"><div style="display:inline-block;background:var(--bg-card);border:1px solid var(--border);padding:8px 14px;border-radius:14px 14px 14px 4px;max-width:80%;font-size:0.85rem;">${replies[Math.floor(Math.random()*replies.length)]}</div></div>`;box.scrollTop=box.scrollHeight;},800+Math.random()*1200);box.scrollTop=box.scrollHeight;}'''),
    ('motion', '动作捕捉', '🦴', '实时动作捕捉 · 驱动你的虚拟角色', 'sunset-academy', 'cyber',
     '''<div class="grid-2"><div class="card text-center"><h3>📹 摄像头画面</h3><div style="width:100%;aspect-ratio:4/3;background:#0a0a14;border-radius:12px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:3rem;">📷</div><p class="text-muted mt-2">点击"开始捕捉"以激活摄像头</p></div>
<div class="card text-center"><h3>🦴 骨骼追踪</h3><div style="width:100%;aspect-ratio:4/3;background:var(--gradient-card);border-radius:12px;display:flex;align-items:center;justify-content:center;" id="skeletonView"><pre style="font-size:0.65rem;color:var(--accent);" id="skelData">等待动作捕捉数据...</pre></div></div></div>
<div class="flex flex-center gap-3 mt-3"><button class="btn btn-primary btn-lg" onclick="startMotion()" id="motionBtn">🎬 开始捕捉</button><select class="form-input" style="width:auto;"><option>挥手动捕</option><option>走路动捕</option><option>跳舞动捕</option></select></div>''',
     '''let motionInterval;function startMotion(){const btn=document.getElementById('motionBtn');if(motionInterval){clearInterval(motionInterval);motionInterval=null;btn.textContent='🎬 开始捕捉';return;}btn.textContent='⏹️ 停止捕捉';const bones=['头部 ○','左肩 ─','右肩 ─','左肘 ─','右肘 ─','左腕 ○','右腕 ○','脊椎 │','左髋 ─','右髋 ─','左膝 ─','右膝 ─','左踝 ○','右踝 ○'];motionInterval=setInterval(()=>{document.getElementById('skelData').textContent=bones.map(b=>`${b} (${(Math.random()*100).toFixed(1)},${(Math.random()*100).toFixed(1)})`).join('\\n');},200);}'''),
    ('clone', '数字分身', '👥', '创建你的3D数字分身 · 进入元宇宙世界', 'lavender-academy', 'void',
     '''<div class="card text-center mb-3" style="max-width:500px;margin:0 auto 20px;"><h2>🔮 创建数字分身</h2><div class="grid-3 mt-3"><div class="card" style="cursor:pointer;" onclick="selectStyle('realistic')">👤<br>写实风</div><div class="card" style="cursor:pointer;" onclick="selectStyle('anime')">✨<br>二次元</div><div class="card" style="cursor:pointer;" onclick="selectStyle('chibi')">🎀<br>Q版</div></div>
<div class="mt-3"><button class="btn btn-primary btn-lg">📸 上传照片生成</button></div></div>
<div class="card"><h3>我的数字分身</h3><p class="text-muted">还没有创建数字分身，快来生成你的元宇宙形象吧！</p></div>''',
     '''function selectStyle(s){alert('已选择风格: '+s+'\\n上传照片功能即将开放！');}'''),
    ('scene', '场景工坊', '🎬', '搭建虚拟场景 · 布置你的元宇宙空间', 'sky-academy', 'nature',
     '''<div class="grid-3" id="sceneGrid"></div>
<div class="card mt-4 text-center"><h3>🏗️ 创建新场景</h3><p class="text-muted">从模板开始，或从零建造</p><button class="btn btn-primary mt-2">开始建造</button></div>''',
     '''const scenes=[{name:'樱花庭院',type:'日式',size:'200㎡',likes:'2.3k',color:'#ff8fab',emoji:'🌸'},{name:'赛博天台',type:'科幻',size:'150㎡',likes:'1.8k',color:'#4ecdc4',emoji:'🌃'},{name:'魔法图书馆',type:'奇幻',size:'300㎡',likes:'3.1k',color:'#8b5cf6',emoji:'📚'},{name:'海底宫殿',type:'奇幻',size:'400㎡',likes:'2.7k',color:'#0ea5e9',emoji:'🏰'},{name:'星之剧场',type:'演出',size:'500㎡',likes:'4.2k',color:'#6366f1',emoji:'🎭'},{name:'森林小屋',type:'自然',size:'120㎡',likes:'1.5k',color:'#34d399',emoji:'🏡'}];
document.getElementById('sceneGrid').innerHTML=scenes.map(s=>`<div class="card text-center"><span style="font-size:2.5rem;">${s.emoji}</span><h4>${s.name}</h4><div class="flex flex-center gap-2"><span class="tag tag-pink">${s.type}</span><span style="font-size:0.78rem;color:var(--text-muted);">${s.size}</span></div><p style="font-size:0.82rem;">❤️ ${s.likes}</p><button class="btn btn-sm btn-outline">编辑</button></div>`).join('');'''),
    ('emotion', '情感引擎', '💗', 'AI情感识别 · 让你的虚拟角色拥有真实表情', 'lemon-academy', 'default',
     '''<div class="card text-center mb-3"><h3>😊 情感检测演示</h3><div id="emotionDisplay" style="font-size:5rem;margin:20px 0;">😐</div><p class="text-muted">上传一张面部照片，AI将识别情感状态</p><input type="file" accept="image/*" style="display:none;" id="emoUpload" onchange="detectEmotion()"><button class="btn btn-primary mt-2" onclick="document.getElementById('emoUpload').click()">📸 上传照片</button></div>
<div class="grid-4" id="emoHistory"></div>''',
     '''const emotions=['😊 开心','😢 悲伤','😠 生气','😨 恐惧','😍 喜爱','😐 平静','😲 惊讶','🤔 思考'];let history=[];
function detectEmotion(){const emo=emotions[Math.floor(Math.random()*emotions.length)];document.getElementById('emotionDisplay').textContent=emo.split(' ')[0];history.unshift({time:new Date().toLocaleTimeString(),emo:emo});if(history.length>8)history.pop();
document.getElementById('emoHistory').innerHTML=history.map(h=>`<div class="stat-card"><div style="font-size:2rem;">${h.emo.split(' ')[0]}</div><div class="stat-label">${h.emo.split(' ')[1]}</div><div style="font-size:0.65rem;color:var(--text-muted);">${h.time}</div></div>`).join('');}'''),
]:
    pg(f'{BASE}/pages/digital-human/{page[0]}.html', *page[1:])

print("Digital-human extended done (5 pages)")

# ======== ACADEMY EXTENDED (5) ========
for page in [
    ('exam', '考试系统', '📝', '在线考核 · 检验你的学习成果', 'sunset-academy', 'academy',
     '''<div class="card" style="max-width:600px;margin:0 auto;"><h3>📋 可用考试</h3><div id="examList"></div></div>''',
     '''const exams=[{name:'Cosplay基础知识',q:'20题',time:'30分钟',pass:'80分',attempts:'2,341人已考'},{name:'动画制作入门',q:'30题',time:'45分钟',pass:'75分',attempts:'1,892人已考'},{name:'声优配音基础',q:'15题',time:'20分钟',pass:'70分',attempts:'1,456人已考'},{name:'3D建模基础',q:'25题',time:'40分钟',pass:'75分',attempts:'987人已考'}];
document.getElementById('examList').innerHTML=exams.map(e=>`<div class="card mb-2"><div style="display:flex;justify-content:space-between;align-items:center;"><div><h4>${e.name}</h4><div class="flex gap-2 mt-1" style="font-size:0.78rem;color:var(--text-muted);"><span>📝 ${e.q}</span><span>⏱ ${e.time}</span><span>✅ 及格线: ${e.pass}</span></div><p style="font-size:0.75rem;color:var(--text-muted);">${e.attempts}</p></div><button class="btn btn-sm btn-primary">开始考试</button></div></div>`).join('');'''),
    ('cert', '证书认证', '🏅', '获得官方认证 · 为你的技能背书', 'starlight-academy', 'default',
     '''<div class="grid-3" id="certGrid"></div>''',
     '''const certs=[{name:'初级Cosplayer',req:'通过Cos基础考试',earned:true,color:'#34d399',emoji:'🎭'},{name:'中级动画师',req:'完成动画制作课程',earned:true,color:'#4da6ff',emoji:'🎬'},{name:'高级3D建模师',req:'通过3D进阶考试',earned:false,color:'#8b5cf6',emoji:'🏗️'},{name:'声优认证',req:'完成配音课程+考试',earned:false,color:'#ff6b9d',emoji:'🎤'},{name:'MAD大师',req:'3个MAD作品入选精选',earned:true,color:'#f97316',emoji:'✂️'},{name:'虚拟主播',req:'直播时长>100h',earned:false,color:'#eab308',emoji:'🎙️'}];
document.getElementById('certGrid').innerHTML=certs.map(c=>`<div class="card text-center" style="opacity:${c.earned?1:0.6};"><span style="font-size:2.5rem;">${c.emoji}</span><h4>${c.name}</h4><p style="font-size:0.78rem;color:var(--text-muted);">${c.req}</p><span class="tag ${c.earned?'tag-green':'tag-pink'}">${c.earned?'✅ 已获得':'🔒 未获得'}</span></div>`).join('');'''),
    ('live-class', '直播课堂', '🎓', '名师直播 · 互动学习 · 实时答疑', 'sky-academy', 'anime',
     '''<div class="grid-2" id="classGrid"></div>''',
     '''const classes=[{title:'Cosplay化妆技巧·进阶',teacher:'美妆达人小雪',time:'今晚 20:00',students:234,color:'#ff6b9d',emoji:'💄',live:true},{title:'3D建模从入门到精通',teacher:'建模大师老王',time:'明晚 19:30',students:456,color:'#4da6ff',emoji:'🏗️',live:false},{title:'动画分镜设计',teacher:'分镜师阿杰',time:'周三 15:00',students:189,color:'#8b5cf6',emoji:'🎬',live:false},{title:'MAD剪辑技巧分享',teacher:'剪辑大神K',time:'周四 20:30',students:312,color:'#f97316',emoji:'✂️',live:false}];
document.getElementById('classGrid').innerHTML=classes.map(c=>`<div class="card"><div style="display:flex;align-items:center;gap:12px;"><span style="font-size:2rem;">${c.emoji}</span><div style="flex:1;"><h4>${c.title}${c.live?' <span class="live-dot"></span>':''}</h4><p style="font-size:0.78rem;color:var(--text-muted);">👨‍🏫 ${c.teacher}</p><p style="font-size:0.75rem;color:var(--text-muted);">🕐 ${c.time} · 👥 ${c.students}人报名</p></div></div><button class="btn btn-sm ${c.live?'btn-primary':'btn-outline'} mt-2">${c.live?'进入课堂':'预约'}</button></div>`).join('');'''),
    ('ranking', '学霸排行', '📊', '学习积分排行榜 · 谁是最强学霸？', 'mint-academy', 'academy',
     '''<div class="table-wrap" style="max-width:600px;margin:0 auto;"><table><thead><tr><th>#</th><th>学员</th><th>积分</th><th>完成课程</th><th>称号</th></tr></thead><tbody id="rankBody"></tbody></table></div>''',
     '''const ranks=[{rank:1,name:'学霸小明',pts:12580,courses:47,title:'🏆 至尊学霸'},{rank:2,name:'Cos达人小雪',pts:10240,courses:38,title:'🎭 Cos宗师'},{rank:3,name:'建模高手',pts:8950,courses:32,title:'🏗️ 建模大师'},{rank:4,name:'剪辑狂魔',pts:7820,courses:29,title:'✂️ MAD之王'},{rank:5,name:'声优练习生',pts:6540,courses:25,title:'🎤 声之精灵'},{rank:6,name:'动画新秀',pts:5210,courses:21,title:'🎬 动画新星'},{rank:7,name:'画师大佬',pts:4890,courses:18,title:'🎨 灵魂画手'},{rank:8,name:'萌新上路',pts:3200,courses:12,title:'🌱 学园新芽'}];
document.getElementById('rankBody').innerHTML=ranks.map(r=>`<tr><td style="font-weight:800;">${['🥇','🥈','🥉'][r.rank-1]||r.rank}</td><td>${r.name}</td><td style="font-weight:700;color:var(--accent);">${r.pts.toLocaleString()}</td><td>${r.courses}门</td><td>${r.title}</td></tr>`).join('');'''),
    ('library', '资料馆', '📖', '海量学习资料 · 教程 · 素材 · 模板', 'lavender-academy', 'academy',
     '''<div class="search-bar mb-3"><input class="form-input" type="text" placeholder="🔍 搜索资料..."><button class="btn btn-primary">搜索</button></div>
<div class="grid-3" id="libGrid"></div>''',
     '''const docs=[{name:'Cosplay化妆完全指南',type:'PDF',size:'12MB',dl:'2.3万',color:'#ff6b9d',emoji:'📄'},{name:'3D建模教程合集',type:'视频',size:'2.1GB',dl:'1.8万',color:'#4da6ff',emoji:'🎬'},{name:'AE特效模板包',type:'模板',size:'856MB',dl:'3.2万',color:'#8b5cf6',emoji:'📦'},{name:'动画原画参考集',type:'图片',size:'450MB',dl:'1.5万',color:'#f97316',emoji:'🖼️'},{name:'声优配音练习素材',type:'音频',size:'340MB',dl:'9,820',color:'#34d399',emoji:'🎵'},{name:'MAD剪辑素材库',type:'素材',size:'1.8GB',dl:'4.1万',color:'#eab308',emoji:'📁'}];
document.getElementById('libGrid').innerHTML=docs.map(d=>`<div class="card"><span style="font-size:2rem;">${d.emoji}</span><h4>${d.name}</h4><div class="flex flex-wrap gap-2 mt-1" style="font-size:0.75rem;color:var(--text-muted);"><span class="tag tag-pink">${d.type}</span><span>${d.size}</span></div><p style="font-size:0.78rem;margin-top:4px;">📥 ${d.dl}次下载</p><button class="btn btn-sm btn-primary mt-2">下载</button></div>`).join('');'''),
]:
    pg(f'{BASE}/pages/academy/{page[0]}.html', *page[1:])

print("Academy extended done (5 pages)")

# ======== EVENTS EXTENDED (5) ========
for page in [
    ('live-show', '虚拟演唱会', '🎵', '全息投影演唱会 · 虚拟偶像Live', 'starlight-academy', 'galaxy',
     '''<div class="live-hero text-center" style="background:linear-gradient(135deg,#8b5cf6,#6366f1,#ec4899);border-radius:20px;padding:40px;color:#fff;margin-bottom:24px;"><h2><span class="live-dot"></span> 即将开始</h2><h1 style="font-size:2.5rem;color:#fff;-webkit-text-fill-color:#fff;">星之声·虚拟演唱会</h1><p>虚拟歌姬「星乃ひかり」首次3D Live</p><div id="concertTimer" style="font-size:2rem;font-weight:900;font-family:monospace;margin-top:12px;">--:--:--</div><button class="btn btn-kawaii mt-3">🎫 立即购票 ¥199</button></div>
<div class="grid-3" id="showGrid"></div>''',
     '''function updateCTimer(){const target=new Date();target.setHours(20,0,0,0);if(new Date()>target)target.setDate(target.getDate()+1);const diff=target-new Date();const h=Math.floor(diff/3600000),m=Math.floor((diff%3600000)/60000),s=Math.floor((diff%60000)/1000);document.getElementById('concertTimer').textContent=`${String(h).padStart(2,'0')}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;}
const shows=[{title:'龙墟·交响音乐会',date:'7月15日',venue:'龙墟·星之剧场',sold:'89%',emoji:'🎻',color:'#4da6ff'},{title:'Cos学园·舞台剧',date:'7月22日',venue:'学院区·大礼堂',sold:'76%',emoji:'🎭',color:'#f97316'},{title:'夏日烟花·虚拟花火大会',date:'8月1日',venue:'龙墟·天空广场',sold:'92%',emoji:'🎆',color:'#ff6b9d'},{title:'MAD电影节',date:'7月30日',venue:'娱乐区·巨幕影厅',sold:'65%',emoji:'🎬',color:'#8b5cf6'},{title:'声优见面会',date:'8月5日',venue:'龙墟·演播大厅',sold:'54%',emoji:'🎤',color:'#34d399'},{title:'同人即卖会',date:'8月10日',venue:'商业区·展览中心',sold:'71%',emoji:'📚',color:'#eab308'}];
document.getElementById('showGrid').innerHTML=shows.map(s=>`<div class="card text-center"><span style="font-size:2.5rem;">${s.emoji}</span><h4>${s.title}</h4><p style="font-size:0.8rem;color:var(--text-muted);">📅 ${s.date} · 📍 ${s.venue}</p><div class="progress-bar mt-2"><div class="progress-fill" style="width:${s.sold};"></div></div><p style="font-size:0.7rem;">已售 ${s.sold}</p><button class="btn btn-sm btn-primary">购票</button></div>`).join('');
updateCTimer();setInterval(updateCTimer,1000);'''),
    ('exhibition', '线上展览', '🖼️', '虚拟展览馆 · 艺术作品展示', 'mint-academy', 'academy',
     '''<div class="grid-3" id="exGrid"></div>''',
     '''const exs=[{name:'龙墟战记原画展',artist:'官方美术组',works:156,views:'12.8万',emoji:'🐉',color:'#4da6ff'},{name:'Cosplay摄影展',artist:'多位摄影师',works:89,views:'8.9万',emoji:'📸',color:'#ff6b9d'},{name:'同人插画展',artist:'社区画师',works:234,views:'15.2万',emoji:'🎨',color:'#8b5cf6'},{name:'MAD作品展',artist:'剪辑师联盟',works:67,views:'6.5万',emoji:'✂️',color:'#f97316'},{name:'3D模型展',artist:'建模师社区',works:45,views:'4.3万',emoji:'🏗️',color:'#34d399'},{name:'手工作品展',artist:'手作达人',works:78,views:'3.8万',emoji:'🧵',color:'#eab308'}];
document.getElementById('exGrid').innerHTML=exs.map(e=>`<div class="card text-center"><span style="font-size:2.5rem;">${e.emoji}</span><h4>${e.name}</h4><p style="font-size:0.78rem;">👤 ${e.artist}</p><p style="font-size:0.82rem;color:var(--text-muted);">🖼️ ${e.works}件 · 👁 ${e.views}</p><button class="btn btn-sm btn-primary">🏛️ 进入展览</button></div>`).join('');'''),
    ('festival', '学园祭', '🎊', '龙奕学院年度盛典 · 学园祭狂欢', 'coral-academy', 'sakura',
     '''<div class="live-hero text-center" style="background:linear-gradient(135deg,#f472b6,#ff6b9d,#f97316);border-radius:20px;padding:40px;color:#fff;margin-bottom:24px;"><h2>🎊 龙奕学院·夏季学园祭</h2><h1 style="font-size:2rem;color:#fff;-webkit-text-fill-color:#fff;">2026年7月20日-25日</h1><p>摊位居多 · 舞台表演 · Cos游行 · 烟花大会</p><button class="btn btn-kawaii mt-3">🎫 立即参与</button></div>
<div class="grid-3" id="eventGrid"></div>''',
     '''const events=[{name:'Cosplay游行',desc:'全校Cosplay大游行',time:'7月20日 10:00',icon:'🎭'},{name:'舞台表演',desc:'社团才艺展示',time:'7月21日 14:00',icon:'🎤'},{name:'同人摊位',desc:'自由买卖&交流',time:'7月20-25日 全天',icon:'🏪'},{name:'游戏比赛',desc:'电竞&桌游大赛',time:'7月22日 13:00',icon:'🎮'},{name:'烟花大会',desc:'闭幕烟花盛典',time:'7月25日 20:00',icon:'🎆'},{name:'评选颁奖',desc:'年度Cos大奖',time:'7月25日 18:00',icon:'🏆'}];
document.getElementById('eventGrid').innerHTML=events.map(e=>`<div class="card text-center"><span style="font-size:2.5rem;">${e.icon}</span><h4>${e.name}</h4><p style="font-size:0.82rem;color:var(--text-muted);">${e.desc}</p><p style="font-size:0.75rem;color:var(--accent);">${e.time}</p></div>`).join('');'''),
    ('award', '年度评选', '🏆', '年度Cos大奖 · 动画评选 · 创作表彰', 'lemon-academy', 'default',
     '''<div class="tabs mb-3"><button class="tab active">Cos奖项</button><button class="tab">动画奖项</button><button class="tab">创作奖项</button></div>
<div class="grid-2" id="awardGrid"></div>''',
     '''const awards=[{name:'年度最佳Cosplay',noms:['魔法少女·星野','龙墟战记·主角','樱花庄·和服'],icon:'🎭',color:'#f59e0b'},{name:'年度最佳动画',noms:['龙墟战记','魔法少女☆星辰','星之声'],icon:'🎬',color:'#4da6ff'},{name:'年度最佳MAD',noms:['觉醒·龙墟','催泪·樱花庄','燃向AMV混剪'],icon:'✂️',color:'#8b5cf6'},{name:'年度最佳创作者',noms:['剪辑师小林','画师小雪','Cos达人星野'],icon:'👑',color:'#f97316'},{name:'年度最佳社团',noms:['Cosplay研究社','MAD剪辑部','绘画社'],icon:'🏘️',color:'#34d399'},{name:'年度最佳新人',noms:['萌新小王','新晋画师','初代Cos'],icon:'🌱',color:'#eab308'}];
document.getElementById('awardGrid').innerHTML=awards.map(a=>`<div class="card"><h3>${a.icon} ${a.name}</h3><p style="font-size:0.78rem;color:var(--text-muted);">提名:</p>${a.noms.map(n=>`<div style="display:flex;align-items:center;gap:8px;padding:4px 0;"><span class="badge">${a.noms.indexOf(n)+1}</span><span style="font-size:0.85rem;">${n}</span></div>`).join('')}<button class="btn btn-sm btn-outline mt-2">🗳️ 投票</button></div>`).join('');
document.querySelectorAll('.tab').forEach(t=>t.addEventListener('click',function(){document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));this.classList.add('active');}));'''),
    ('fireworks', '烟花大会', '🎆', '虚拟烟花盛宴 · 与全服玩家共赏', 'sakura-academy', 'sakura',
     '''<div class="card text-center" style="max-width:600px;margin:0 auto 20px;"><h2>🎆 夏日烟花大会</h2><div style="width:100%;aspect-ratio:16/9;background:#0a0a14;border-radius:16px;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden;" id="fireworkCanvas">
<div style="position:absolute;top:30%;left:20%;width:8px;height:8px;background:#ff6b9d;border-radius:50%;animation:fw1 2s infinite;box-shadow:0 0 20px #ff6b9d;"></div>
<div style="position:absolute;top:25%;left:50%;width:6px;height:6px;background:#4ecdc4;border-radius:50%;animation:fw2 2.5s infinite;box-shadow:0 0 20px #4ecdc4;"></div>
<div style="position:absolute;top:35%;left:70%;width:10px;height:10px;background:#fbbf24;border-radius:50%;animation:fw3 3s infinite;box-shadow:0 0 20px #fbbf24;"></div>
<div style="position:absolute;top:28%;left:35%;width:5px;height:5px;background:#a78bfa;border-radius:50%;animation:fw4 2.8s infinite;box-shadow:0 0 20px #a78bfa;"></div>
<div style="position:absolute;bottom:20%;left:50%;color:#fff;font-size:1.5rem;font-weight:800;text-shadow:0 0 20px rgba(255,255,255,0.5);">🎆 下一场烟花: <span id="fwTimer" style="font-family:monospace;">--:--</span></div></div>
<p class="text-muted mt-3" id="fwViewers">👥 3,421人正在观看</p><button class="btn btn-kawaii mt-2" onclick="launchFirework()">🎆 发射烟花 💎50</button></div>
<style>@keyframes fw1{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(20);opacity:0}}@keyframes fw2{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(15);opacity:0}}@keyframes fw3{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(25);opacity:0}}@keyframes fw4{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(18);opacity:0}}</style>''',
     '''function launchFirework(){const t=document.createElement('div');t.className='toast success';t.textContent='🎆 烟花已发射！';let tc=document.querySelector('.toast-container');if(!tc){tc=document.createElement('div');tc.className='toast-container';document.body.appendChild(tc);}tc.appendChild(t);setTimeout(()=>t.remove(),3000);}
function updateFWTimer(){const now=new Date();const next=new Date(now);next.setMinutes(Math.ceil(now.getMinutes()/15)*15,0,0);const diff=next-now;const m=Math.floor(diff/60000);const s=Math.floor((diff%60000)/1000);document.getElementById('fwTimer').textContent=`${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;}
setInterval(updateFWTimer,1000);updateFWTimer();'''),
]:
    pg(f'{BASE}/pages/events/{page[0]}.html', *page[1:])

print("Events extended done (5 pages)")

# ======== WIKI EXTENDED (4) ========
for page in [
    ('timeline', '动漫编年史', '📜', '从古到今 · 动漫发展史', 'forest-academy' if False else 'mint-academy', 'academy',
     '''<div style="max-width:700px;margin:0 auto;" id="tl"></div>''',
     '''const events=[{year:'1963',title:'手塚治虫《铁臂阿童木》首播',desc:'日本TV动画的起点'},{year:'1979',title:'《机动战士高达》播出',desc:'真实系机器人动画的开端'},{year:'1984',title:'宫崎骏《风之谷》上映',desc:'吉卜力工作室成立前奏'},{year:'1995',title:'《新世纪福音战士》播出',desc:'颠覆性的心理科幻巨作'},{year:'2006',title:'《凉宫春日的忧郁》播出',desc:'轻小说改编动画热潮'},{year:'2016',title:'《你的名字。》上映',desc:'新海诚现象级动画电影'},{year:'2020',title:'《鬼灭之刃 无限列车》',desc:'日本影史票房第一'},{year:'2026',title:'龙奕学院成立',desc:'元宇宙学院·动漫社区新时代'}];
document.getElementById('tl').innerHTML=events.map((e,i)=>`<div style="display:flex;gap:16px;margin-bottom:24px;${i%2?'flex-direction:row-reverse':''}"><div style="width:80px;text-align:center;flex-shrink:0;"><div style="font-size:1.5rem;font-weight:900;color:var(--accent);">${e.year}</div><div style="width:2px;height:40px;background:var(--gradient-hero);margin:4px auto;"></div></div><div class="card" style="flex:1;"><h4>${e.title}</h4><p style="font-size:0.85rem;color:var(--text-secondary);">${e.desc}</p></div></div>`).join('');'''),
    ('characters', '角色图鉴', '📇', '经典动画角色大全', 'coral-academy', 'anime',
     '''<div class="search-bar mb-3"><input class="form-input" type="text" placeholder="🔍 搜索角色..."><button class="btn btn-primary">搜索</button></div>
<div class="grid-3" id="charGrid"></div>''',
     '''const chars=[{name:'龙墟·凯',anime:'龙墟战记',type:'主角',desc:'龙之力量的继承者',emoji:'🐉',color:'#4da6ff'},{name:'星野·光',anime:'魔法少女☆星辰',type:'主角',desc:'魔法少女团队长',emoji:'⭐',color:'#ff6b9d'},{name:'樱小路·樱',anime:'樱花庄的日常',type:'主角',desc:'温柔善良的女高中生',emoji:'🌸',color:'#ff8fab'},{name:'机甲师·雷',anime:'机甲战纪',type:'主角',desc:'天才机甲驾驶员',emoji:'🤖',color:'#6366f1'},{name:'冒险者·枫',anime:'异世界冒险谭',type:'主角',desc:'从现代穿越的冒险者',emoji:'🗺️',color:'#34d399'},{name:'歌姬·星乃',anime:'星之声',type:'主角',desc:'虚拟歌姬AI',emoji:'🎵',color:'#8b5cf6'}];
document.getElementById('charGrid').innerHTML=chars.map(c=>`<div class="card text-center"><span style="font-size:3rem;">${c.emoji}</span><h4>${c.name}</h4><p style="font-size:0.78rem;">📺 ${c.anime}</p><span class="tag tag-purple">${c.type}</span><p style="font-size:0.8rem;color:var(--text-secondary);margin-top:4px;">${c.desc}</p></div>`).join('');'''),
    ('studios', '动画公司', '🏢', '日本&中国动画制作公司图鉴', 'sky-academy', 'default',
     '''<div class="grid-3" id="studioGrid"></div>''',
     '''const studios=[{name:'吉卜力',country:'🇯🇵',works:['千与千寻','龙猫','风之谷'],icon:'🌿'},{name:'京都动画',country:'🇯🇵',works:['凉宫春日','轻音少女','紫罗兰'],icon:'🎨'},{name:'ufotable',country:'🇯🇵',works:['鬼灭之刃','Fate/stay night'],icon:'⚔️'},{name:'MAPPA',country:'🇯🇵',works:['咒术回战','进击的巨人'],icon:'🔥'},{name:'彩条屋',country:'🇨🇳',works:['哪吒之魔童降世','姜子牙'],icon:'🐉'},{name:'追光动画',country:'🇨🇳',works:['白蛇缘起','新神榜'],icon:'🌸'}];
document.getElementById('studioGrid').innerHTML=studios.map(s=>`<div class="card text-center"><span style="font-size:2.5rem;">${s.icon}</span><h4>${s.name} ${s.country}</h4><p style="font-size:0.78rem;color:var(--text-muted);">代表作:</p>${s.works.map(w=>`<span class="tag tag-pink">${w}</span>`).join(' ')}</div>`).join('');'''),
    ('seiyuu', '声优图鉴', '🎙️', '知名声优资料库', 'lavender-academy', 'academy',
     '''<div class="grid-3" id="seiyuuGrid"></div>''',
     '''const svs=[{name:'花泽香菜',roles:['立华奏','千石抚子','甘露寺蜜璃'],emoji:'🌸',color:'#ff6b9d'},{name:'梶裕贵',roles:['艾伦·耶格尔','梅利奥达斯'],emoji:'⚔️',color:'#4da6ff'},{name:'钉宫理惠',roles:['夏娜','露易丝','神乐'],emoji:'🔥',color:'#f97316'},{name:'水濑祈',roles:['雷姆','香风智乃'],emoji:'💧',color:'#0ea5e9'},{name:'松冈祯丞',roles:['桐人','上杉风太郎'],emoji:'🗡️',color:'#8b5cf6'},{name:'早见沙织',roles:['雪之下雪乃','蝴蝶忍'],emoji:'❄️',color:'#a78bfa'}];
document.getElementById('seiyuuGrid').innerHTML=svs.map(s=>`<div class="card text-center"><span style="font-size:2.5rem;">${s.emoji}</span><h4>${s.name}</h4><div class="flex flex-wrap gap-1 justify-center mt-1">${s.roles.map(r=>`<span class="tag tag-pink">${r}</span>`).join('')}</div></div>`).join('');'''),
]:
    pg(f'{BASE}/pages/wiki/{page[0]}.html', *page[1:])

print("Wiki extended done (4 pages)")

# ======== HELP + META (6) ========
help_pages = [
    ('faq', '帮助中心', '❓', '常见问题 · 快速解答', 'sky-academy', 'academy',
     '''<div style="max-width:700px;margin:0 auto;" id="faqList"></div>''',
     '''const faqs=[{q:'如何注册龙奕学院账号？',a:'点击右上角"登录"按钮，选择"注册"，输入邮箱和密码即可完成注册。'},{q:'如何上传视频/动画？',a:'进入"上传投稿"页面，拖拽或选择视频文件，填写标题和描述后发布。审核通过后即可展示。'},{q:'龙晶是什么？如何获取？',a:'龙晶是龙奕学院的虚拟货币。通过每日签到、完成任务、创作投稿、参与活动等方式获取。'},{q:'如何加入社团？',a:'进入"社团"页面，浏览社团列表，点击感兴趣的社团并选择"加入社团"。部分社团需要审核。'},{q:'如何开启虚拟直播？',a:'在"虚拟直播"页面，选择虚拟形象后点击"开始直播"，即可开启你的直播之旅。'},{q:'如何联系客服？',a:'发送邮件至 support@longyi.academy 或在"意见反馈"页面提交问题。'}];
document.getElementById('faqList').innerHTML=faqs.map(f=>`<details class="card mb-2" style="cursor:pointer;"><summary style="font-weight:700;font-size:1rem;list-style:none;display:flex;justify-content:space-between;align-items:center;">${f.q}<span>▼</span></summary><p style="margin-top:12px;color:var(--text-secondary);">${f.a}</p></details>`).join('');'''),
    ('feedback', '意见反馈', '💡', '你的意见是我们进步的动力', 'lavender-academy', 'default',
     '''<div class="card" style="max-width:600px;margin:0 auto;"><h3>📝 提交反馈</h3>
<div class="form-group"><label class="form-label">反馈类型</label><select class="form-input"><option>功能建议</option><option>Bug反馈</option><option>体验问题</option><option>其他</option></select></div>
<div class="form-group"><label class="form-label">描述</label><textarea class="form-textarea" placeholder="详细描述你的问题或建议..."></textarea></div>
<div class="form-group"><label class="form-label">联系方式（选填）</label><input class="form-input" type="email" placeholder="your@email.com"></div>
<button class="btn btn-primary" onclick="submitFeedback()">提交反馈</button></div>''',
     '''function submitFeedback(){const t=document.createElement('div');t.className='toast success';t.textContent='✅ 感谢你的反馈！我们会尽快处理。';let tc=document.querySelector('.toast-container');if(!tc){tc=document.createElement('div');tc.className='toast-container';document.body.appendChild(tc);}tc.appendChild(t);setTimeout(()=>t.remove(),3000);}'''),
    ('guide', '新手指南', '🌱', '龙奕学院入门指南 · 快速上手', 'mint-academy', 'academy',
     '''<div style="max-width:700px;margin:0 auto;">
<div class="grid-3 mb-3"><div class="stat-card"><span style="font-size:2rem;">1️⃣</span><div class="stat-label">注册账号</div></div><div class="stat-card"><span style="font-size:2rem;">2️⃣</span><div class="stat-label">完善资料</div></div><div class="stat-card"><span style="font-size:2rem;">3️⃣</span><div class="stat-label">开始探索</div></div></div>
<div class="card mb-2"><h4>📺 观看动漫</h4><p style="color:var(--text-secondary);">进入"番剧大厅"浏览海量番剧，点击播放器即可享受高清观影体验。开启弹幕，与同好一起吐槽！</p></div>
<div class="card mb-2"><h4>🌌 探索元宇宙</h4><p style="color:var(--text-secondary);">进入"龙墟世界"，创建你的虚拟化身，穿梭六大城区，参与各种虚拟活动。</p></div>
<div class="card mb-2"><h4>🎨 创作分享</h4><p style="color:var(--text-secondary);">使用"创作工坊"工具制作MAD/AMV、Cos作品，上传分享获取积分和粉丝。</p></div>
<div class="card mb-2"><h4>📚 学习成长</h4><p style="color:var(--text-secondary);">在"学院"模块学习Cosplay、动画制作、配音等课程，通过考试获取认证证书。</p></div></div>''',
     ''),
    ('join', '加入我们', '🤝', '加入龙奕学院团队 · 共创元宇宙未来', 'coral-academy', 'default',
     '''<div style="max-width:700px;margin:0 auto;"><div class="card mb-2"><h3>🎨 我们正在寻找</h3>
<div class="grid-2 mt-2"><div class="card"><h4>前端工程师</h4><p style="font-size:0.82rem;color:var(--text-muted);">React/Three.js 元宇宙开发</p><span class="tag tag-blue">全职</span></div>
<div class="card"><h4>3D建模师</h4><p style="font-size:0.82rem;color:var(--text-muted);">虚拟场景&角色建模</p><span class="tag tag-purple">全职/兼职</span></div>
<div class="card"><h4>AI工程师</h4><p style="font-size:0.82rem;color:var(--text-muted);">NLP/CV 数字人开发</p><span class="tag tag-orange">全职</span></div>
<div class="card"><h4>社区运营</h4><p style="font-size:0.82rem;color:var(--text-muted);">社群管理&内容策划</p><span class="tag tag-green">全职</span></div></div></div>
<div class="card text-center mt-3"><h3>📧 投递简历</h3><p>hr@longyi.academy</p><button class="btn btn-primary mt-2">查看全部职位</button></div></div>''',
     ''),
    ('partners', '合作伙伴', '🤝', '与我们一起构建元宇宙生态', 'sky-academy', 'academy',
     '''<div class="grid-3" id="partnerGrid"></div>
<div class="card text-center mt-4"><h3>🤝 成为合作伙伴</h3><p class="text-muted">无论你是内容创作者、技术供应商还是品牌方，欢迎加入龙奕学院生态</p><button class="btn btn-primary mt-2">联系我们</button></div>''',
     '''const partners=[{name:'AnimeLab',type:'动漫授权',icon:'🎬'},{name:'CosChina',type:'Cosplay社区',icon:'🎭'},{name:'3DCloud',type:'云渲染服务',icon:'☁️'},{name:'AIHub',type:'AI技术服务',icon:'🤖'},{name:'MangaPress',type:'漫画出版',icon:'📚'},{name:'VoiceAI',type:'语音合成',icon:'🎤'}];
document.getElementById('partnerGrid').innerHTML=partners.map(p=>`<div class="card text-center"><span style="font-size:2.5rem;">${p.icon}</span><h4>${p.name}</h4><span class="tag tag-pink">${p.type}</span></div>`).join('');'''),
    ('privacy', '隐私政策', '🔒', '龙奕学院隐私保护政策', 'starlight-academy', 'default',
     '''<div style="max-width:700px;margin:0 auto;"><div class="card mb-2"><h4>📋 信息收集</h4><p style="color:var(--text-secondary);">我们仅收集提供服务所必需的基本信息，包括邮箱、昵称、虚拟形象数据等。我们承诺不会将您的个人信息出售给第三方。</p></div>
<div class="card mb-2"><h4>🛡️ 数据安全</h4><p style="color:var(--text-secondary);">采用行业标准加密技术保护您的数据。您的虚拟资产（龙晶、道具等）存储于区块链技术保障的分布式账本中。</p></div>
<div class="card mb-2"><h4>👤 用户权利</h4><p style="color:var(--text-secondary);">您有权随时查看、修改、导出或删除您的个人数据。如需行使上述权利，请联系 support@longyi.academy。</p></div>
<div class="card"><h4>📧 联系方式</h4><p style="color:var(--text-secondary);">广州龙奕无形科技文化有限公司<br>邮箱: privacy@longyi.academy<br>地址: 中国广东省广州市</p></div></div>''',
     ''),
]
for h in help_pages:
    pg(f'{BASE}/pages/help/{h[0]}.html', *h[1:]) if h[0] in ('faq','feedback','guide') else pg(f'{BASE}/pages/meta/{h[0]}.html', *h[1:])

print("=== ALL PAGES GENERATED SUCCESSFULLY ===")
print("Total new pages: 45+")

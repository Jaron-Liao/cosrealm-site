#!/usr/bin/env python3
"""龙奕学院 — 剩余页面生成器 (25页)"""
import os
BASE = r"C:\Users\28767\Downloads\cosrealm-site"

T = '''<!DOCTYPE html>
<html lang="zh-CN" data-3d="{scene}">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title} — 龙奕学院</title>
<link rel="stylesheet" href="../../assets/style.css">
<link rel="stylesheet" href="../../assets/themes/academy/{theme}.css">
<style>{css}</style>
</head>
<body><div class="page-wrap">
<div class="page-hero"><span class="hero-emoji">{emoji}</span><h1>{title}</h1><p>{subtitle}</p></div>
<div class="section">{content}</div>
<footer class="footer"><div class="footer-inner"><div class="footer-brand">&copy;2026 <strong>龙奕学院 LongYi Academy</strong> — 广州龙奕无形科技文化有限公司</div><div class="footer-links"><a href="../../pages/meta/about.html">关于我们</a><a href="../../pages/meta/privacy.html">隐私政策</a><a href="../../pages/help/faq.html">帮助中心</a></div></div></footer>
</div>
<script src="../../assets/three-engine.js"></script><script src="../../assets/nav.js"></script>
<script>{js}</script></body></html>'''

def W(path, title, emoji, subtitle, theme, scene, css, content, js):
    d = os.path.dirname(path); os.makedirs(d, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(T.format(title=title, emoji=emoji, subtitle=subtitle, theme=theme, scene=scene, css=css, content=content, js=js))

# DIGITAL-HUMAN (5)
W(f'{BASE}/pages/digital-human/ai-chat.html', 'AI角色对话', '🤖', '与虚拟角色实时对话 · AI情感引擎', 'coral-academy', 'academy', '',
  '''<div style="max-width:600px;margin:0 auto;">
<div class="card mb-2 flex gap-3" style="align-items:center;"><span style="font-size:2rem;">⭐</span><div><h4>星野あかり</h4><p style="font-size:0.78rem;color:var(--text-muted);">元气少女 · Cosplay爱好者</p></div><span class="online-badge" style="margin-left:auto;">在线</span></div>
<div class="card" style="min-height:300px;"><div style="max-height:280px;overflow-y:auto;" id="chatBox"><div style="text-align:right;margin:8px 0;"><div style="display:inline-block;background:var(--gradient-btn);color:#fff;padding:8px 14px;border-radius:14px 14px 4px 14px;max-width:80%;font-size:0.85rem;">你好！今天想聊什么？</div></div></div>
<div class="flex gap-2 mt-3"><input class="form-input" placeholder="输入消息..." id="ci" onkeydown="if(event.key==='Enter')S()"><button class="btn btn-primary" onclick="S()">发送</button></div></div></div>''',
  '''function S(){const m=document.getElementById('ci').value.trim();if(!m)return;const b=document.getElementById('chatBox');b.innerHTML+=`<div style="text-align:right;margin:8px 0;"><div style="display:inline-block;background:var(--gradient-btn);color:#fff;padding:8px 14px;border-radius:14px 14px 4px 14px;max-width:80%;font-size:0.85rem;">${m}</div></div>`;document.getElementById('ci').value='';setTimeout(()=>{const r=['好有趣！','真的吗？太棒了！','哈哈哈','嗯嗯，继续说～','我也这么觉得！','你的想法超棒！'];b.innerHTML+=`<div style="text-align:left;margin:8px 0;"><div style="display:inline-block;background:var(--bg-card);border:1px solid var(--border);padding:8px 14px;border-radius:14px 14px 14px 4px;max-width:80%;font-size:0.85rem;">${r[Math.floor(Math.random()*r.length)]}</div></div>`;b.scrollTop=b.scrollHeight;},800+Math.random()*1200);b.scrollTop=b.scrollHeight;}''')

W(f'{BASE}/pages/digital-human/motion.html', '动作捕捉', '🦴', '实时动作捕捉 · 驱动虚拟角色', 'sunset-academy', 'cyber', '',
  '''<div class="grid-2"><div class="card text-center"><h3>📹 摄像头</h3><div style="aspect-ratio:4/3;background:#0a0a14;border-radius:12px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:3rem;">📷</div></div>
<div class="card text-center"><h3>🦴 骨骼追踪</h3><div style="aspect-ratio:4/3;background:var(--gradient-card);border-radius:12px;display:flex;align-items:center;justify-content:center;" id="skv"><pre style="font-size:0.6rem;color:var(--accent);" id="skd">等待捕捉数据...</pre></div></div></div>
<div class="flex flex-center gap-3 mt-3"><button class="btn btn-primary btn-lg" onclick="M()" id="mb">🎬 开始捕捉</button><select class="form-input" style="width:auto;"><option>挥手</option><option>走路</option><option>跳舞</option></select></div>''',
  '''let mi;function M(){const b=document.getElementById('mb');if(mi){clearInterval(mi);mi=null;b.textContent='🎬 开始捕捉';return;}b.textContent='⏹️ 停止';const bn=['头部 ○','左肩 ─','右肩 ─','左肘 ─','右肘 ─','左腕 ○','右腕 ○','脊椎 │','左髋 ─','右髋 ─','左膝 ─','右膝 ─','左踝 ○','右踝 ○'];mi=setInterval(()=>{document.getElementById('skd').textContent=bn.map(b=>b+' ('+(Math.random()*100).toFixed(1)+','+(Math.random()*100).toFixed(1)+')').join('\\n');},200);}''')

W(f'{BASE}/pages/digital-human/clone.html', '数字分身', '👥', '创建3D数字分身 · 进入元宇宙', 'lavender-academy', 'void', '',
  '''<div class="card text-center mb-3" style="max-width:500px;margin:0 auto 20px;"><h2>🔮 创建数字分身</h2>
<div class="grid-3 mt-3"><div class="card" style="cursor:pointer;" onclick="A('写实风')">👤<br>写实风</div><div class="card" style="cursor:pointer;" onclick="A('二次元')">✨<br>二次元</div><div class="card" style="cursor:pointer;" onclick="A('Q版')">🎀<br>Q版</div></div>
<button class="btn btn-primary btn-lg mt-3">📸 上传照片生成</button></div>
<div class="card"><h3>我的数字分身</h3><p class="text-muted">还没有数字分身，快来创建吧！</p></div>''',
  '''function A(s){const t=document.createElement('div');t.className='toast info';t.textContent='已选择: '+s+' · 上传功能即将开放';let tc=document.querySelector('.toast-container');if(!tc){tc=document.createElement('div');tc.className='toast-container';document.body.appendChild(tc);}tc.appendChild(t);setTimeout(()=>t.remove(),3000);}''')

W(f'{BASE}/pages/digital-human/scene.html', '场景工坊', '🎬', '搭建虚拟场景 · 布置元宇宙空间', 'sky-academy', 'nature', '',
  '''<div class="grid-3" id="sg"></div>
<div class="card mt-4 text-center"><h3>🏗️ 创建新场景</h3><p class="text-muted">从模板或从零建造</p><button class="btn btn-primary mt-2">开始建造</button></div>''',
  '''const s=[{n:'樱花庭院',t:'日式',sz:'200㎡',lk:'2.3k',e:'🌸'},{n:'赛博天台',t:'科幻',sz:'150㎡',lk:'1.8k',e:'🌃'},{n:'魔法图书馆',t:'奇幻',sz:'300㎡',lk:'3.1k',e:'📚'},{n:'海底宫殿',t:'奇幻',sz:'400㎡',lk:'2.7k',e:'🏰'},{n:'星之剧场',t:'演出',sz:'500㎡',lk:'4.2k',e:'🎭'},{n:'森林小屋',t:'自然',sz:'120㎡',lk:'1.5k',e:'🏡'}];
document.getElementById('sg').innerHTML=s.map(i=>`<div class="card text-center"><span style="font-size:2.5rem;">${i.e}</span><h4>${i.n}</h4><div class="flex flex-center gap-2"><span class="tag tag-pink">${i.t}</span><span style="font-size:0.78rem;color:var(--text-muted);">${i.sz}</span></div><p>❤️ ${i.lk}</p><button class="btn btn-sm btn-outline">编辑</button></div>`).join('');''')

W(f'{BASE}/pages/digital-human/emotion.html', '情感引擎', '💗', 'AI情感识别 · 真实表情驱动', 'lemon-academy', 'default', '',
  '''<div class="card text-center mb-3"><h3>😊 情感检测</h3><div style="font-size:5rem;margin:20px 0;" id="ed">😐</div><p class="text-muted">上传照片，AI识别情感</p><input type="file" accept="image/*" style="display:none;" id="eu" onchange="D()"><button class="btn btn-primary mt-2" onclick="document.getElementById('eu').click()">📸 上传照片</button></div>
<div class="grid-4" id="eh"></div>''',
  '''const em=['😊 开心','😢 悲伤','😠 生气','😨 恐惧','😍 喜爱','😐 平静','😲 惊讶','🤔 思考'];let h=[];
function D(){const e=em[Math.floor(Math.random()*em.length)];document.getElementById('ed').textContent=e.split(' ')[0];h.unshift({t:new Date().toLocaleTimeString(),e:e});if(h.length>8)h.pop();
document.getElementById('eh').innerHTML=h.map(x=>`<div class="stat-card"><div style="font-size:2rem;">${x.e.split(' ')[0]}</div><div class="stat-label">${x.e.split(' ')[1]}</div><div style="font-size:0.65rem;color:var(--text-muted);">${x.t}</div></div>`).join('');}''')

print("Digital-human: 5 done")

# ACADEMY (5)
W(f'{BASE}/pages/academy/exam.html', '考试系统', '📝', '在线考核 · 检验学习成果', 'sunset-academy', 'academy', '',
  '''<div class="card" style="max-width:600px;margin:0 auto;"><h3>📋 可用考试</h3><div id="el"></div></div>''',
  '''const e=[{n:'Cosplay基础知识',q:'20题',t:'30分钟',p:'80分',a:'2,341人'},{n:'动画制作入门',q:'30题',t:'45分钟',p:'75分',a:'1,892人'},{n:'声优配音基础',q:'15题',t:'20分钟',p:'70分',a:'1,456人'},{n:'3D建模基础',q:'25题',t:'40分钟',p:'75分',a:'987人'}];
document.getElementById('el').innerHTML=e.map(x=>`<div class="card mb-2"><div style="display:flex;justify-content:space-between;align-items:center;"><div><h4>${x.n}</h4><div class="flex gap-2 mt-1" style="font-size:0.78rem;color:var(--text-muted);"><span>📝 ${x.q}</span><span>⏱ ${x.t}</span><span>✅ ${x.p}</span></div><p style="font-size:0.75rem;color:var(--text-muted);">${x.a}已考</p></div><button class="btn btn-sm btn-primary">开始考试</button></div></div>`).join('');''')

W(f'{BASE}/pages/academy/cert.html', '证书认证', '🏅', '获得官方认证 · 为技能背书', 'starlight-academy', 'default', '',
  '''<div class="grid-3" id="cg"></div>''',
  '''const c=[{n:'初级Cosplayer',r:'通过Cos基础考试',e:true,e2:'🎭'},{n:'中级动画师',r:'完成动画制作课程',e:true,e2:'🎬'},{n:'高级3D建模师',r:'通过3D进阶考试',e:false,e2:'🏗️'},{n:'声优认证',r:'完成配音课程+考试',e:false,e2:'🎤'},{n:'MAD大师',r:'3个MAD作品入选精选',e:true,e2:'✂️'},{n:'虚拟主播',r:'直播时长>100h',e:false,e2:'🎙️'}];
document.getElementById('cg').innerHTML=c.map(x=>`<div class="card text-center" style="opacity:${x.e?1:0.6};"><span style="font-size:2.5rem;">${x.e2}</span><h4>${x.n}</h4><p style="font-size:0.78rem;color:var(--text-muted);">${x.r}</p><span class="tag ${x.e?'tag-green':'tag-pink'}">${x.e?'✅ 已获得':'🔒 未获得'}</span></div>`).join('');''')

W(f'{BASE}/pages/academy/live-class.html', '直播课堂', '🎓', '名师直播 · 互动学习 · 实时答疑', 'sky-academy', 'anime', '',
  '''<div class="grid-2" id="cg2"></div>''',
  '''const c=[{t:'Cosplay化妆技巧·进阶',tr:'美妆达人小雪',ti:'今晚 20:00',st:234,e:'💄',l:true},{t:'3D建模从入门到精通',tr:'建模大师老王',ti:'明晚 19:30',st:456,e:'🏗️',l:false},{t:'动画分镜设计',tr:'分镜师阿杰',ti:'周三 15:00',st:189,e:'🎬',l:false},{t:'MAD剪辑技巧分享',tr:'剪辑大神K',ti:'周四 20:30',st:312,e:'✂️',l:false}];
document.getElementById('cg2').innerHTML=c.map(x=>`<div class="card"><div class="flex gap-3" style="align-items:center;"><span style="font-size:2rem;">${x.e}</span><div style="flex:1;"><h4>${x.t}${x.l?' <span class="live-dot"></span>':''}</h4><p style="font-size:0.78rem;">👨‍🏫 ${x.tr} · 🕐 ${x.ti}</p><p style="font-size:0.75rem;color:var(--text-muted);">👥 ${x.st}人</p></div></div><button class="btn btn-sm ${x.l?'btn-primary':'btn-outline'} mt-2">${x.l?'进入':'预约'}</button></div>`).join('');''')

W(f'{BASE}/pages/academy/ranking.html', '学霸排行', '📊', '学习积分排行榜 · 谁是最强学霸', 'mint-academy', 'academy', '',
  '''<div class="table-wrap" style="max-width:600px;margin:0 auto;"><table><thead><tr><th>#</th><th>学员</th><th>积分</th><th>课程</th><th>称号</th></tr></thead><tbody id="rb"></tbody></table></div>''',
  '''const r=[{rk:1,n:'学霸小明',p:12580,c:47,t:'🏆 至尊学霸'},{rk:2,n:'Cos达人小雪',p:10240,c:38,t:'🎭 Cos宗师'},{rk:3,n:'建模高手',p:8950,c:32,t:'🏗️ 建模大师'},{rk:4,n:'剪辑狂魔',p:7820,c:29,t:'✂️ MAD之王'},{rk:5,n:'声优练习生',p:6540,c:25,t:'🎤 声之精灵'},{rk:6,n:'动画新秀',p:5210,c:21,t:'🎬 动画新星'},{rk:7,n:'画师大佬',p:4890,c:18,t:'🎨 灵魂画手'},{rk:8,n:'萌新上路',p:3200,c:12,t:'🌱 学园新芽'}];
document.getElementById('rb').innerHTML=r.map(x=>`<tr><td style="font-weight:800;">${['🥇','🥈','🥉'][x.rk-1]||x.rk}</td><td>${x.n}</td><td style="font-weight:700;color:var(--accent);">${x.p.toLocaleString()}</td><td>${x.c}门</td><td>${x.t}</td></tr>`).join('');''')

W(f'{BASE}/pages/academy/library.html', '资料馆', '📖', '海量学习资料 · 教程 · 素材 · 模板', 'lavender-academy', 'academy', '',
  '''<div class="search-bar mb-3"><input class="form-input" type="text" placeholder="🔍 搜索资料..."><button class="btn btn-primary">搜索</button></div>
<div class="grid-3" id="lg"></div>''',
  '''const d=[{n:'Cosplay化妆完全指南',tp:'PDF',sz:'12MB',dl:'2.3万',e:'📄'},{n:'3D建模教程合集',tp:'视频',sz:'2.1GB',dl:'1.8万',e:'🎬'},{n:'AE特效模板包',tp:'模板',sz:'856MB',dl:'3.2万',e:'📦'},{n:'动画原画参考集',tp:'图片',sz:'450MB',dl:'1.5万',e:'🖼️'},{n:'声优配音练习素材',tp:'音频',sz:'340MB',dl:'9,820',e:'🎵'},{n:'MAD剪辑素材库',tp:'素材',sz:'1.8GB',dl:'4.1万',e:'📁'}];
document.getElementById('lg').innerHTML=d.map(x=>`<div class="card"><span style="font-size:2rem;">${x.e}</span><h4>${x.n}</h4><div class="flex gap-2 mt-1" style="font-size:0.75rem;color:var(--text-muted);"><span class="tag tag-pink">${x.tp}</span><span>${x.sz}</span></div><p style="font-size:0.78rem;">📥 ${x.dl}</p><button class="btn btn-sm btn-primary mt-2">下载</button></div>`).join('');''')

print("Academy: 5 done")

# EVENTS (5)
W(f'{BASE}/pages/events/live-show.html', '虚拟演唱会', '🎵', '全息投影 · 虚拟偶像Live', 'starlight-academy', 'galaxy', '',
  '''<div class="live-hero text-center" style="background:linear-gradient(135deg,#8b5cf6,#6366f1,#ec4899);border-radius:20px;padding:40px;color:#fff;margin-bottom:24px;"><h2><span class="live-dot"></span> 即将开始</h2><h1 style="font-size:2rem;color:#fff;-webkit-text-fill-color:#fff;">星之声·虚拟演唱会</h1><p>虚拟歌姬「星乃ひかり」首次3D Live</p><div style="font-size:2rem;font-weight:900;font-family:monospace;margin-top:12px;" id="ct">--:--:--</div><button class="btn btn-kawaii mt-3">🎫 立即购票 ¥199</button></div>
<div class="grid-3" id="sg2"></div>''',
  '''function U(){const t=new Date();t.setHours(20,0,0,0);if(new Date()>t)t.setDate(t.getDate()+1);const d=t-new Date();const h=Math.floor(d/3600000),m=Math.floor((d%3600000)/60000),s=Math.floor((d%60000)/1000);document.getElementById('ct').textContent=`${String(h).padStart(2,'0')}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;}
const s=[{t:'龙墟·交响音乐会',d:'7月15日',v:'龙墟·星之剧场',sl:'89%',e:'🎻'},{t:'Cos学园·舞台剧',d:'7月22日',v:'学院区·大礼堂',sl:'76%',e:'🎭'},{t:'夏日烟花大会',d:'8月1日',v:'龙墟·天空广场',sl:'92%',e:'🎆'},{t:'MAD电影节',d:'7月30日',v:'娱乐区·巨幕厅',sl:'65%',e:'🎬'},{t:'声优见面会',d:'8月5日',v:'龙墟·演播大厅',sl:'54%',e:'🎤'},{t:'同人即卖会',d:'8月10日',v:'商业区·展览中心',sl:'71%',e:'📚'}];
document.getElementById('sg2').innerHTML=s.map(x=>`<div class="card text-center"><span style="font-size:2.5rem;">${x.e}</span><h4>${x.t}</h4><p style="font-size:0.8rem;color:var(--text-muted);">📅 ${x.d} · 📍 ${x.v}</p><div class="progress-bar mt-2"><div class="progress-fill" style="width:${x.sl};"></div></div><p style="font-size:0.7rem;">已售 ${x.sl}</p><button class="btn btn-sm btn-primary">购票</button></div>`).join('');U();setInterval(U,1000);''')

W(f'{BASE}/pages/events/exhibition.html', '线上展览', '🖼️', '虚拟展览 · 艺术作品展示', 'mint-academy', 'academy', '',
  '''<div class="grid-3" id="eg"></div>''',
  '''const e=[{n:'龙墟战记原画展',a:'官方美术组',w:156,v:'12.8万',e2:'🐉'},{n:'Cosplay摄影展',a:'多位摄影师',w:89,v:'8.9万',e2:'📸'},{n:'同人插画展',a:'社区画师',w:234,v:'15.2万',e2:'🎨'},{n:'MAD作品展',a:'剪辑师联盟',w:67,v:'6.5万',e2:'✂️'},{n:'3D模型展',a:'建模师社区',w:45,v:'4.3万',e2:'🏗️'},{n:'手工作品展',a:'手作达人',w:78,v:'3.8万',e2:'🧵'}];
document.getElementById('eg').innerHTML=e.map(x=>`<div class="card text-center"><span style="font-size:2.5rem;">${x.e2}</span><h4>${x.n}</h4><p style="font-size:0.78rem;">👤 ${x.a}</p><p style="font-size:0.82rem;color:var(--text-muted);">🖼️ ${x.w}件 · 👁 ${x.v}</p><button class="btn btn-sm btn-primary">🏛️ 进入展览</button></div>`).join('');''')

W(f'{BASE}/pages/events/festival.html', '学园祭', '🎊', '龙奕学院年度盛典 · 学园祭狂欢', 'coral-academy', 'sakura', '',
  '''<div style="background:linear-gradient(135deg,#f472b6,#ff6b9d,#f97316);border-radius:20px;padding:40px;color:#fff;margin-bottom:24px;text-align:center;"><h2>🎊 龙奕学院·夏季学园祭</h2><h1 style="font-size:2rem;color:#fff;-webkit-text-fill-color:#fff;">2026年7月20日-25日</h1><p>摊位居多 · 舞台表演 · Cos游行 · 烟花大会</p><button class="btn btn-kawaii mt-3">🎫 立即参与</button></div>
<div class="grid-3" id="fg"></div>''',
  '''const e=[{n:'Cosplay游行',d:'全校大游行',t:'7/20 10:00',i:'🎭'},{n:'舞台表演',d:'社团才艺展示',t:'7/21 14:00',i:'🎤'},{n:'同人摊位',d:'自由买卖交流',t:'7/20-25',i:'🏪'},{n:'游戏比赛',d:'电竞&桌游大赛',t:'7/22 13:00',i:'🎮'},{n:'烟花大会',d:'闭幕盛典',t:'7/25 20:00',i:'🎆'},{n:'评选颁奖',d:'年度Cos大奖',t:'7/25 18:00',i:'🏆'}];
document.getElementById('fg').innerHTML=e.map(x=>`<div class="card text-center"><span style="font-size:2.5rem;">${x.i}</span><h4>${x.n}</h4><p style="font-size:0.82rem;color:var(--text-muted);">${x.d}</p><p style="font-size:0.75rem;color:var(--accent);">${x.t}</p></div>`).join('');''')

W(f'{BASE}/pages/events/award.html', '年度评选', '🏆', '年度Cos大奖 · 动画评选', 'lemon-academy', 'default', '',
  '''<div class="tabs mb-3"><button class="tab active">Cos奖项</button><button class="tab">动画奖项</button><button class="tab">创作奖项</button></div>
<div class="grid-2" id="ag"></div>''',
  '''const a=[{n:'年度最佳Cos',nm:['魔法少女·星野','龙墟战记·主角','樱花庄·和服'],i:'🎭'},{n:'年度最佳动画',nm:['龙墟战记','魔法少女☆星辰','星之声'],i:'🎬'},{n:'年度最佳MAD',nm:['觉醒·龙墟','催泪·樱花庄','燃向AMV混剪'],i:'✂️'},{n:'年度最佳创作者',nm:['剪辑师小林','画师小雪','Cos达人星野'],i:'👑'},{n:'年度最佳社团',nm:['Cosplay研究社','MAD剪辑部','绘画社'],i:'🏘️'},{n:'年度最佳新人',nm:['萌新小王','新晋画师','初代Cos'],i:'🌱'}];
document.getElementById('ag').innerHTML=a.map(x=>`<div class="card"><h3>${x.i} ${x.n}</h3>${x.nm.map((n,i)=>`<div class="flex gap-2" style="padding:4px 0;align-items:center;"><span class="badge">${i+1}</span><span style="font-size:0.85rem;">${n}</span></div>`).join('')}<button class="btn btn-sm btn-outline mt-2">🗳️ 投票</button></div>`).join('');
document.querySelectorAll('.tab').forEach(t=>t.addEventListener('click',function(){document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));this.classList.add('active');}));''')

W(f'{BASE}/pages/events/fireworks.html', '烟花大会', '🎆', '虚拟烟花盛宴 · 与全服玩家共赏', 'sakura-academy', 'sakura', '',
  '''<style>@keyframes fw1{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(20);opacity:0}}@keyframes fw2{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(15);opacity:0}}@keyframes fw3{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(25);opacity:0}}</style>
<div class="card text-center" style="max-width:600px;margin:0 auto;"><h2>🎆 夏日烟花大会</h2>
<div style="aspect-ratio:16/9;background:#0a0a14;border-radius:16px;position:relative;overflow:hidden;">
<div style="position:absolute;top:30%;left:20%;width:8px;height:8px;background:#ff6b9d;border-radius:50%;animation:fw1 2s infinite;box-shadow:0 0 20px #ff6b9d;"></div>
<div style="position:absolute;top:25%;left:50%;width:6px;height:6px;background:#4ecdc4;border-radius:50%;animation:fw2 2.5s infinite;box-shadow:0 0 20px #4ecdc4;"></div>
<div style="position:absolute;top:35%;left:70%;width:10px;height:10px;background:#fbbf24;border-radius:50%;animation:fw3 3s infinite;box-shadow:0 0 20px #fbbf24;"></div>
<div style="position:absolute;bottom:20%;left:50%;color:#fff;font-size:1.5rem;font-weight:800;">🎆 下一场: <span id="ft" style="font-family:monospace;">--:--</span></div></div>
<p class="text-muted mt-3">👥 <span id="fv">3,421</span>人正在观看</p>
<button class="btn btn-kawaii mt-2" onclick="L()">🎆 发射烟花 💎50</button></div>''',
  '''function L(){const t=document.createElement('div');t.className='toast success';t.textContent='🎆 烟花已发射！';let tc=document.querySelector('.toast-container');if(!tc){tc=document.createElement('div');tc.className='toast-container';document.body.appendChild(tc);}tc.appendChild(t);setTimeout(()=>t.remove(),3000);const v=parseInt(document.getElementById('fv').textContent.replace(',',''))+1;document.getElementById('fv').textContent=v.toLocaleString();}
function U2(){const n=new Date();n.setMinutes(Math.ceil(n.getMinutes()/15)*15,0,0);const d=n-new Date();const m=Math.floor(d/60000),s=Math.floor((d%60000)/1000);document.getElementById('ft').textContent=`${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;}
setInterval(U2,1000);U2();''')

print("Events: 5 done")

# WIKI (4)
W(f'{BASE}/pages/wiki/timeline.html', '动漫编年史', '📜', '从古到今 · 动漫发展史', 'mint-academy', 'academy', '',
  '''<div style="max-width:700px;margin:0 auto;" id="tl"></div>''',
  '''const e=[{y:'1963',t:'手塚治虫《铁臂阿童木》',d:'日本TV动画的起点'},{y:'1979',t:'《机动战士高达》',d:'真实系机器人动画开端'},{y:'1984',t:'宫崎骏《风之谷》',d:'吉卜力前奏'},{y:'1995',t:'《新世纪福音战士》',d:'颠覆性心理科幻'},{y:'2006',t:'《凉宫春日的忧郁》',d:'轻小说改编热潮'},{y:'2016',t:'《你的名字。》',d:'新海诚现象级作品'},{y:'2020',t:'《鬼灭之刃 无限列车》',d:'日本影史票房第一'},{y:'2026',t:'龙奕学院成立',d:'元宇宙学院·动漫社区'}];
document.getElementById('tl').innerHTML=e.map((x,i)=>`<div style="display:flex;gap:16px;margin-bottom:24px;${i%2?'flex-direction:row-reverse':''}"><div style="width:80px;text-align:center;flex-shrink:0;"><div style="font-size:1.5rem;font-weight:900;color:var(--accent);">${x.y}</div><div style="width:2px;height:40px;background:var(--gradient-hero);margin:4px auto;"></div></div><div class="card" style="flex:1;"><h4>${x.t}</h4><p style="font-size:0.85rem;color:var(--text-secondary);">${x.d}</p></div></div>`).join('');''')

W(f'{BASE}/pages/wiki/characters.html', '角色图鉴', '📇', '经典动画角色大全', 'coral-academy', 'anime', '',
  '''<div class="search-bar mb-3"><input class="form-input" type="text" placeholder="🔍 搜索角色..."><button class="btn btn-primary">搜索</button></div>
<div class="grid-3" id="cg3"></div>''',
  '''const c=[{n:'龙墟·凯',a:'龙墟战记',t:'主角',d:'龙之力量的继承者',e:'🐉'},{n:'星野·光',a:'魔法少女☆星辰',t:'主角',d:'魔法少女团队长',e:'⭐'},{n:'樱小路·樱',a:'樱花庄的日常',t:'主角',d:'温柔善良的女高中生',e:'🌸'},{n:'机甲师·雷',a:'机甲战纪',t:'主角',d:'天才机甲驾驶员',e:'🤖'},{n:'冒险者·枫',a:'异世界冒险谭',t:'主角',d:'从现代穿越的冒险者',e:'🗺️'},{n:'歌姬·星乃',a:'星之声',t:'主角',d:'虚拟歌姬AI',e:'🎵'}];
document.getElementById('cg3').innerHTML=c.map(x=>`<div class="card text-center"><span style="font-size:3rem;">${x.e}</span><h4>${x.n}</h4><p style="font-size:0.78rem;">📺 ${x.a}</p><span class="tag tag-purple">${x.t}</span><p style="font-size:0.8rem;color:var(--text-secondary);margin-top:4px;">${x.d}</p></div>`).join('');''')

W(f'{BASE}/pages/wiki/studios.html', '动画公司', '🏢', '日本&中国动画制作公司图鉴', 'sky-academy', 'default', '',
  '''<div class="grid-3" id="sg3"></div>''',
  '''const s=[{n:'吉卜力',c:'🇯🇵',w:['千与千寻','龙猫','风之谷'],e:'🌿'},{n:'京都动画',c:'🇯🇵',w:['凉宫春日','轻音少女','紫罗兰'],e:'🎨'},{n:'ufotable',c:'🇯🇵',w:['鬼灭之刃','Fate'],e:'⚔️'},{n:'MAPPA',c:'🇯🇵',w:['咒术回战','巨人'],e:'🔥'},{n:'彩条屋',c:'🇨🇳',w:['哪吒','姜子牙'],e:'🐉'},{n:'追光动画',c:'🇨🇳',w:['白蛇缘起','新神榜'],e:'🌸'}];
document.getElementById('sg3').innerHTML=s.map(x=>`<div class="card text-center"><span style="font-size:2.5rem;">${x.e}</span><h4>${x.n} ${x.c}</h4><div class="flex flex-wrap gap-1 justify-center mt-1">${x.w.map(w=>`<span class="tag tag-pink">${w}</span>`).join('')}</div></div>`).join('');''')

W(f'{BASE}/pages/wiki/seiyuu.html', '声优图鉴', '🎙️', '知名声优资料库', 'lavender-academy', 'academy', '',
  '''<div class="grid-3" id="sg4"></div>''',
  '''const s=[{n:'花泽香菜',r:['立华奏','千石抚子','甘露寺蜜璃'],e:'🌸'},{n:'梶裕贵',r:['艾伦','梅利奥达斯'],e:'⚔️'},{n:'钉宫理惠',r:['夏娜','露易丝','神乐'],e:'🔥'},{n:'水濑祈',r:['雷姆','香风智乃'],e:'💧'},{n:'松冈祯丞',r:['桐人','上杉风太郎'],e:'🗡️'},{n:'早见沙织',r:['雪之下雪乃','蝴蝶忍'],e:'❄️'}];
document.getElementById('sg4').innerHTML=s.map(x=>`<div class="card text-center"><span style="font-size:2.5rem;">${x.e}</span><h4>${x.n}</h4><div class="flex flex-wrap gap-1 justify-center mt-1">${x.r.map(r=>`<span class="tag tag-pink">${r}</span>`).join('')}</div></div>`).join('');''')

print("Wiki: 4 done")

# HELP + META (6)
W(f'{BASE}/pages/help/faq.html', '帮助中心', '❓', '常见问题 · 快速解答', 'sky-academy', 'academy', '',
  '''<div style="max-width:700px;margin:0 auto;" id="fl"></div>''',
  '''const f=[{q:'如何注册账号？',a:'点击右上角"登录"按钮，选择"注册"，输入邮箱和密码即可。'},{q:'如何上传视频？',a:'进入"上传投稿"页面，拖拽视频文件，填写信息后发布。'},{q:'龙晶是什么？',a:'龙奕学院虚拟货币，可通过签到、创作、活动获取。'},{q:'如何加入社团？',a:'进入"社团"页面，选择感兴趣的社团申请加入。'},{q:'如何联系客服？',a:'发送邮件至 support@longyi.academy。'}];
document.getElementById('fl').innerHTML=f.map(x=>`<details class="card mb-2" style="cursor:pointer;"><summary style="font-weight:700;display:flex;justify-content:space-between;align-items:center;">${x.q}<span>▼</span></summary><p style="margin-top:12px;color:var(--text-secondary);">${x.a}</p></details>`).join('');''')

W(f'{BASE}/pages/help/feedback.html', '意见反馈', '💡', '你的意见是我们进步的动力', 'lavender-academy', 'default', '',
  '''<div class="card" style="max-width:600px;margin:0 auto;"><h3>📝 提交反馈</h3>
<div class="form-group"><label class="form-label">类型</label><select class="form-input"><option>功能建议</option><option>Bug反馈</option><option>体验问题</option><option>其他</option></select></div>
<div class="form-group"><label class="form-label">描述</label><textarea class="form-textarea" placeholder="描述问题或建议..."></textarea></div>
<div class="form-group"><label class="form-label">联系方式(选填)</label><input class="form-input" type="email" placeholder="your@email.com"></div>
<button class="btn btn-primary" onclick="F()">提交反馈</button></div>''',
  '''function F(){const t=document.createElement('div');t.className='toast success';t.textContent='✅ 感谢反馈！';let tc=document.querySelector('.toast-container');if(!tc){tc=document.createElement('div');tc.className='toast-container';document.body.appendChild(tc);}tc.appendChild(t);setTimeout(()=>t.remove(),3000);}''')

W(f'{BASE}/pages/help/guide.html', '新手指南', '🌱', '龙奕学院入门指南', 'mint-academy', 'academy', '',
  '''<div style="max-width:700px;margin:0 auto;">
<div class="grid-3 mb-3"><div class="stat-card"><span style="font-size:2rem;">1️⃣</span><div class="stat-label">注册账号</div></div><div class="stat-card"><span style="font-size:2rem;">2️⃣</span><div class="stat-label">完善资料</div></div><div class="stat-card"><span style="font-size:2rem;">3️⃣</span><div class="stat-label">开始探索</div></div></div>
<div class="card mb-2"><h4>📺 观看动漫</h4><p style="color:var(--text-secondary);">进入"番剧大厅"浏览海量番剧，点击播放器即可享受高清观影。开启弹幕与同好一起吐槽！</p></div>
<div class="card mb-2"><h4>🌌 探索元宇宙</h4><p style="color:var(--text-secondary);">进入"龙墟世界"，创建虚拟化身，穿梭六大城区，参与虚拟活动。</p></div>
<div class="card mb-2"><h4>🎨 创作分享</h4><p style="color:var(--text-secondary);">使用"创作工坊"工具制作MAD、Cos作品，上传分享获取积分。</p></div>
<div class="card mb-2"><h4>📚 学习成长</h4><p style="color:var(--text-secondary);">在"学院"模块学习课程，通过考试获取认证证书。</p></div></div>''', '')

W(f'{BASE}/pages/meta/join.html', '加入我们', '🤝', '加入龙奕学院 · 共创元宇宙未来', 'coral-academy', 'default', '',
  '''<div style="max-width:700px;margin:0 auto;"><div class="card mb-2"><h3>🎨 正在寻找</h3>
<div class="grid-2 mt-2"><div class="card"><h4>前端工程师</h4><p style="font-size:0.82rem;color:var(--text-muted);">React/Three.js</p><span class="tag tag-blue">全职</span></div>
<div class="card"><h4>3D建模师</h4><p style="font-size:0.82rem;color:var(--text-muted);">虚拟场景&角色</p><span class="tag tag-purple">全职/兼职</span></div>
<div class="card"><h4>AI工程师</h4><p style="font-size:0.82rem;color:var(--text-muted);">NLP/CV 数字人</p><span class="tag tag-orange">全职</span></div>
<div class="card"><h4>社区运营</h4><p style="font-size:0.82rem;color:var(--text-muted);">社群&内容策划</p><span class="tag tag-green">全职</span></div></div></div>
<div class="card text-center mt-3"><h3>📧 投递简历</h3><p>hr@longyi.academy</p><button class="btn btn-primary mt-2">查看全部职位</button></div></div>''', '')

W(f'{BASE}/pages/meta/partners.html', '合作伙伴', '🤝', '与我们一起构建元宇宙生态', 'sky-academy', 'academy', '',
  '''<div class="grid-3" id="pg"></div>
<div class="card text-center mt-4"><h3>🤝 成为合作伙伴</h3><p class="text-muted">内容创作者、技术供应商、品牌方，欢迎加入生态</p><button class="btn btn-primary mt-2">联系我们</button></div>''',
  '''const p=[{n:'AnimeLab',t:'动漫授权',e:'🎬'},{n:'CosChina',t:'Cos社区',e:'🎭'},{n:'3DCloud',t:'云渲染',e:'☁️'},{n:'AIHub',t:'AI技术',e:'🤖'},{n:'MangaPress',t:'漫画出版',e:'📚'},{n:'VoiceAI',t:'语音合成',e:'🎤'}];
document.getElementById('pg').innerHTML=p.map(x=>`<div class="card text-center"><span style="font-size:2.5rem;">${x.e}</span><h4>${x.n}</h4><span class="tag tag-pink">${x.t}</span></div>`).join('');''')

W(f'{BASE}/pages/meta/privacy.html', '隐私政策', '🔒', '龙奕学院隐私保护政策', 'starlight-academy', 'default', '',
  '''<div style="max-width:700px;margin:0 auto;"><div class="card mb-2"><h4>📋 信息收集</h4><p style="color:var(--text-secondary);">仅收集提供服务所必需的基本信息，包括邮箱、昵称、虚拟形象数据等。不会将您的个人信息出售给第三方。</p></div>
<div class="card mb-2"><h4>🛡️ 数据安全</h4><p style="color:var(--text-secondary);">采用行业标准加密技术保护数据。虚拟资产存储于区块链保障的分布式账本中。</p></div>
<div class="card mb-2"><h4>👤 用户权利</h4><p style="color:var(--text-secondary);">您有权随时查看、修改、导出或删除个人数据。联系 privacy@longyi.academy。</p></div>
<div class="card"><h4>📧 联系方式</h4><p style="color:var(--text-secondary);">广州龙奕无形科技文化有限公司<br>邮箱: privacy@longyi.academy<br>地址: 中国广东省广州市</p></div></div>''', '')

print("Help + Meta: 6 done")
print("=== ALL 25 PAGES DONE ===")

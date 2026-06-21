# -*- coding: utf-8 -*-
"""Digital-Human pages batch 2: clone, scene, emotion, ai-chat"""
import os

BASE = r"C:\Users\28767\Downloads\cosrealm-site\pages\digital-human"

DH_HEAD = '''<!DOCTYPE html>
<html lang="zh-CN" data-3d="cyber">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | 龙奕学院 LongYi Academy</title>
<link rel="stylesheet" href="../../assets/style.css">
<link rel="stylesheet" href="../../assets/themes/academy/{theme}.css">
<link rel="stylesheet" href="../../assets/effects-layer.css">'''

DH_FOOT = '''
<script src="../../assets/particles.js"></script>
<script src="../../assets/three-engine-v3.js"></script>
<script src="../../assets/effects-runtime.js"></script>
<script src="../../assets/nav.js"></script>
</body>
</html>'''

def w(fn, c):
    with open(os.path.join(BASE, fn), 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'  OK {fn} ({len(c)} chars)')

# ======================================================================
# 7. clone.html — 数字分身
# ======================================================================
w('clone.html', DH_HEAD.format(title='数字分身 · 虚拟替身', theme='lemon-academy') + '''
<style>
.page-container{position:relative;z-index:1;padding-top:80px;max-width:1200px;margin:0 auto}
.hero{text-align:center;padding:40px 20px}
.hero h1{font-size:2.4rem;font-weight:900;background:linear-gradient(135deg,#f59e0b,#fbbf24,#ec4899);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero p{color:var(--text-secondary);margin-top:6px;max-width:650px;margin-left:auto;margin-right:auto}
.clone-layout{display:flex;gap:20px;padding:0 20px 30px}
.clone-sidebar{width:340px;display:flex;flex-direction:column;gap:14px}
.cs-card{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:18px}
.cs-card h3{font-size:.88rem;margin-bottom:12px}
.clone-methods{display:flex;flex-direction:column;gap:8px}
.cm-item{padding:14px;border:2px solid var(--border);border-radius:12px;cursor:pointer;transition:all .3s;display:flex;align-items:center;gap:12px}
.cm-item:hover,.cm-item.active{border-color:var(--accent);background:rgba(245,158,11,.05)}
.cm-item .cmi-icon{font-size:1.8rem}
.cm-item .cmi-info{flex:1}
.cm-item .cmi-name{font-weight:600;font-size:.85rem}
.cm-item .cmi-desc{font-size:.72rem;color:var(--text-dim)}
.upload-area{border:2px dashed var(--border);border-radius:14px;padding:30px;text-align:center;cursor:pointer;transition:all .3s}
.upload-area:hover{border-color:var(--accent);background:rgba(245,158,11,.05)}
.upload-area .ua-icon{font-size:2.5rem;margin-bottom:6px}
.clone-preview{flex:1;background:var(--bg-card);border:1px solid var(--border);border-radius:20px;display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:420px;gap:16px}
.clone-progress{width:80%;max-width:300px}
.progress-bar{height:8px;background:var(--bg-secondary);border-radius:4px;overflow:hidden;margin-top:8px}
.progress-fill{height:100%;background:linear-gradient(90deg,var(--accent),#fbbf24);border-radius:4px;width:0%;transition:width .3s}
.clone-steps{display:flex;flex-direction:column;gap:4px;width:80%;max-width:300px;margin-top:8px}
.clone-step{display:flex;align-items:center;gap:8px;font-size:.78rem;color:var(--text-dim)}
.clone-step.done{color:#22c55e}.clone-step.active{color:var(--accent)}
.clone-step .cstep-dot{width:8px;height:8px;border-radius:50%;background:var(--text-dim);flex-shrink:0}
.clone-step.done .cstep-dot{background:#22c55e}
.clone-step.active .cstep-dot{background:var(--accent);animation:pulse 1s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}
.cases-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;padding:0 20px 40px}
.case-card{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:20px;text-align:center;transition:all .3s}
.case-card:hover{transform:translateY(-4px)}
.case-card .cc-icon{font-size:2.5rem;margin-bottom:8px}
.case-card .cc-title{font-weight:700;font-size:.9rem;margin-bottom:4px}
.case-card .cc-desc{font-size:.78rem;color:var(--text-dim);line-height:1.5}
@media(max-width:768px){.clone-layout{flex-direction:column}.clone-sidebar{width:100%}.cases-grid{grid-template-columns:1fr}.hero h1{font-size:1.8rem}}
</style>
</head>
<body>
<div id="nav-placeholder"></div>
<div class="page-container">
  <div class="hero"><h1>🪞 数字分身 · 虚拟替身</h1><p>通过照片、视频或3D扫描，为真人创建高度还原的数字分身。用于元宇宙社交、远程会议、虚拟演出——你不再需要亲自到场。</p></div>
  <div class="clone-layout">
    <div class="clone-sidebar">
      <div class="cs-card"><h3>📸 采集方式</h3><div class="clone-methods"><div class="cm-item active" onclick="selectMethod('photo',this)"><span class="cmi-icon">📸</span><div class="cmi-info"><div class="cmi-name">照片建模</div><div class="cmi-desc">3-5张不同角度照片</div></div></div><div class="cm-item" onclick="selectMethod('video',this)"><span class="cmi-icon">🎥</span><div class="cmi-info"><div class="cmi-name">视频建模</div><div class="cmi-desc">10秒自拍旋转视频</div></div></div><div class="cm-item" onclick="selectMethod('scan',this)"><span class="cmi-icon">📐</span><div class="cmi-info"><div class="cmi-name">3D扫描</div><div class="cmi-desc">LiDAR/结构光扫描</div></div></div></div></div>
      <div class="cs-card"><h3>📤 上传素材</h3><div class="upload-area" onclick="alert('📤 上传素材\\n\\n支持格式: JPG/PNG/MP4/MOV/OBJ\\n单文件最大: 500MB\\n\\n(演示模式)')"><div class="ua-icon">📁</div><div style="font-size:.85rem;font-weight:600">点击或拖拽上传</div><div style="font-size:.72rem;color:var(--text-dim)">照片/视频/3D扫描</div></div></div>
      <button class="btn-primary" style="width:100%;padding:14px;background:linear-gradient(135deg,#f59e0b,#ec4899);border:none;border-radius:14px;color:#fff;font-weight:700;cursor:pointer;font-size:1rem" onclick="startCloning()">✨ 开始生成数字分身</button>
    </div>
    <div class="clone-preview" id="clonePreview">
      <div style="font-size:5rem">🪞</div>
      <div style="color:var(--text-secondary)">选择采集方式并上传素材开始</div>
      <div class="clone-progress" id="cloneProgress" style="display:none">
        <div style="display:flex;justify-content:space-between;font-size:.75rem;color:var(--text-dim)"><span>生成进度</span><span id="progressPct">0%</span></div>
        <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
      </div>
      <div class="clone-steps" id="cloneSteps" style="display:none"></div>
    </div>
  </div>
  <div style="padding:0 20px"><h2 style="font-size:1.3rem;margin-bottom:14px">🎯 应用场景</h2></div>
  <div class="cases-grid">
    <div class="case-card"><div class="cc-icon">🌐</div><div class="cc-title">元宇宙社交</div><div class="cc-desc">用自己的数字分身在龙墟世界中交友、参加活动、探索虚拟城市。表情和动作实时同步。</div></div>
    <div class="case-card"><div class="cc-icon">💼</div><div class="cc-title">远程办公</div><div class="cc-desc">数字分身代替视频会议——更生动、更省带宽、支持VR/AR沉浸式协作。</div></div>
    <div class="case-card"><div class="cc-icon">🎤</div><div class="cc-title">虚拟演出</div><div class="cc-desc">用你的数字分身在虚拟舞台上表演。动作捕捉驱动，AI实时渲染，全球粉丝同步观看。</div></div>
    <div class="case-card"><div class="cc-icon">🎓</div><div class="cc-title">在线教育</div><div class="cc-desc">教师的数字分身可以同时给多个班级上课，提供个性化辅导和互动问答。</div></div>
    <div class="case-card"><div class="cc-icon">🏪</div><div class="cc-title">虚拟导购</div><div class="cc-desc">品牌代言人的数字分身为顾客提供24/7的虚拟导购服务，支持多语言和个性化推荐。</div></div>
    <div class="case-card"><div class="cc-icon">🩺</div><div class="cc-title">数字孪生</div><div class="cc-desc">医疗健康领域——创建患者的数字孪生体，用于手术模拟、康复训练和远程会诊。</div></div>
  </div>
</div>
''' + DH_FOOT + '''
<script>
function selectMethod(m,btn){document.querySelectorAll('.cm-item').forEach(b=>b.classList.remove('active'));btn.classList.add('active')}
function startCloning(){const steps=[{t:'照片特征提取',d:80},{t:'3D网格重建',d:40},{t:'纹理映射烘焙',d:30},{t:'骨骼自动绑定',d:25},{t:'BlendShape生成',d:20},{t:'质量优化',d:15}];document.getElementById('cloneProgress').style.display='block';document.getElementById('cloneSteps').style.display='flex';const stepsEl=document.getElementById('cloneSteps');steps.forEach(s=>{const d=document.createElement('div');d.className='clone-step';d.innerHTML='<span class="cstep-dot"></span><span>'+s.t+'</span>';stepsEl.appendChild(d)});let totalTime=0;steps.forEach((s,i)=>{totalTime+=s.d;setTimeout(()=>{const pct=Math.round((totalTime/210)*100);document.getElementById('progressPct').textContent=pct+'%';document.getElementById('progressFill').style.width=pct+'%';stepsEl.children[i].classList.remove('active');stepsEl.children[i].classList.add('done');if(i<steps.length-1)stepsEl.children[i+1].classList.add('active');if(i===steps.length-1){setTimeout(()=>{document.querySelector('.clone-preview').innerHTML='<div style="font-size:5rem">✅</div><div style="font-weight:700;color:#22c55e;font-size:1.1rem">数字分身创建成功！</div><div style="color:var(--text-secondary)">模型ID: DC-'+Date.now().toString(36).toUpperCase()+'</div><div style="margin-top:10px"><button class="btn-primary" style="padding:10px 24px;background:var(--accent);border:none;border-radius:10px;color:#fff;cursor:pointer" onclick="alert(\'📤 导出数字分身\\n\\n格式: VRM / GLB / FBX\\n包含: 全身模型+骨骼+52 BlendShape+8K贴图\\n\\n可用于: VRChat, 龙墟元宇宙, Unreal, Unity\')">📤 导出模型</button></div>'},500)}},s.d*10)});stepsEl.children[0].classList.add('active')}
</script>''')

# ======================================================================
# 8. scene.html — 场景工坊
# ======================================================================
w('scene.html', DH_HEAD.format(title='场景工坊 · 虚拟舞台', theme='starlight-academy') + '''
<style>
.page-container{position:relative;z-index:1;padding-top:80px;max-width:1200px;margin:0 auto}
.hero{text-align:center;padding:40px 20px}
.hero h1{font-size:2.4rem;font-weight:900;background:linear-gradient(135deg,#6366f1,#a855f7,#ec4899);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero p{color:var(--text-secondary);margin-top:6px;max-width:600px;margin-left:auto;margin-right:auto}
.scene-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:18px;padding:0 20px 30px}
.scene-card{background:var(--bg-card);border-radius:18px;overflow:hidden;border:1px solid var(--border);transition:all .35s;cursor:pointer}
.scene-card:hover{transform:translateY(-6px);box-shadow:0 14px 40px rgba(99,102,241,.25)}
.scene-card .sc-cover{height:200px;position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center;font-size:4.5rem}
.scene-card .sc-badge{position:absolute;top:10px;right:10px;padding:4px 10px;border-radius:8px;font-size:.68rem;font-weight:700;color:#fff}
.scene-card .sc-body{padding:16px}
.scene-card .sc-name{font-weight:700;font-size:.95rem;margin-bottom:4px}
.scene-card .sc-desc{font-size:.78rem;color:var(--text-dim);line-height:1.5;margin-bottom:10px}
.scene-card .sc-meta{display:flex;justify-content:space-between;font-size:.72rem;color:var(--text-secondary)}
.builder-section{background:var(--bg-card);border:1px solid var(--border);border-radius:20px;margin:0 20px 40px;padding:30px;text-align:center}
.builder-section h2{font-size:1.2rem;margin-bottom:8px}
.builder-tools{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-top:16px}
.bt-tool{padding:10px 20px;border:1px solid var(--border);border-radius:10px;cursor:pointer;font-size:.82rem;color:var(--text-secondary);background:none;transition:all .3s}
.bt-tool:hover{border-color:var(--accent);color:var(--accent)}
@media(max-width:768px){.scene-grid{grid-template-columns:1fr}.hero h1{font-size:1.8rem}}
</style>
</head>
<body>
<div id="nav-placeholder"></div>
<div class="page-container">
  <div class="hero"><h1>🎬 场景工坊 · 虚拟舞台</h1><p>为你的数字人打造专属表演场景。从赛博都市到樱花庭院，从教室到星空舞台——50+预制场景，支持自定义搭建。</p></div>
  <div class="scene-grid">
    <div class="scene-card" onclick="selectScene('赛博都市夜景')"><div class="sc-cover" style="background:linear-gradient(135deg,#0f172a,#1e1b4b,#312e81)">🌃</div><span class="sc-badge" style="background:#6366f1">热门</span><div class="sc-body"><div class="sc-name">赛博都市夜景</div><div class="sc-desc">霓虹闪烁的未来都市，适合科技感Vtuber直播和赛博朋克主题Cos。</div><div class="sc-meta"><span>4K · 动态光照</span><span>12.4K使用</span></div></div></div>
    <div class="scene-card" onclick="selectScene('樱花庭院')"><div class="sc-cover" style="background:linear-gradient(135deg,#fce7f3,#fbcfe8,#f9a8d4)">🌸</div><span class="sc-badge" style="background:#ec4899">唯美</span><div class="sc-body"><div class="sc-name">日式樱花庭院</div><div class="sc-desc">飘落樱花、木质回廊、池塘锦鲤——完美的和风Cos背景。</div><div class="sc-meta"><span>4K · 粒子樱花</span><span>8.9K使用</span></div></div></div>
    <div class="scene-card" onclick="selectScene('星空舞台')"><div class="sc-cover" style="background:linear-gradient(135deg,#020617,#0f172a,#1e1b4b)">🌟</div><span class="sc-badge" style="background:#7c3aed">梦幻</span><div class="sc-body"><div class="sc-name">星空演唱会舞台</div><div class="sc-desc">流星划过、星云流转——虚拟偶像演唱会的终极舞台。</div><div class="sc-meta"><span>8K · 动态星空</span><span>15.2K使用</span></div></div></div>
    <div class="scene-card" onclick="selectScene('学院教室')"><div class="sc-cover" style="background:linear-gradient(135deg,#fef3c7,#fde68a)">🏫</div><span class="sc-badge" style="background:#f59e0b">日常</span><div class="sc-body"><div class="sc-name">龙奕学院教室</div><div class="sc-desc">还原龙奕学院的教室场景——黑板、课桌、窗外校园风景。</div><div class="sc-meta"><span>4K · 学院主题</span><span>6.7K使用</span></div></div></div>
    <div class="scene-card" onclick="selectScene('海底龙宫')"><div class="sc-cover" style="background:linear-gradient(135deg,#0c4a6e,#0369a1,#0284c7)">🐉</div><span class="sc-badge" style="background:#06b6d4">幻想</span><div class="sc-body"><div class="sc-name">海底龙宫</div><div class="sc-desc">珊瑚礁、发光水母、水晶宫殿——龙族角色专属场景。</div><div class="sc-meta"><span>4K · 水下光效</span><span>5.3K使用</span></div></div></div>
    <div class="scene-card" onclick="selectScene('废墟战场')"><div class="sc-cover" style="background:linear-gradient(135deg,#451a03,#78350f,#92400e)">⚔️</div><span class="sc-badge" style="background:#ef4444">战斗</span><div class="sc-body"><div class="sc-name">废墟战场</div><div class="sc-desc">断壁残垣、硝烟弥漫——适合动作类Cos和战斗场景展示。</div><div class="sc-meta"><span>4K · 粒子特效</span><span>4.8K使用</span></div></div></div>
  </div>
  <div class="builder-section"><h2>🛠️ 搭建你的专属场景</h2><p style="color:var(--text-secondary)">拖拽式场景编辑器：添加3D模型、调整光照、设置粒子特效、保存模板</p><div class="builder-tools"><button class="bt-tool">🏗️ 添加建筑</button><button class="bt-tool">🌳 添加植被</button><button class="bt-tool">💡 调整光照</button><button class="bt-tool">✨ 粒子特效</button><button class="bt-tool">📷 设置相机</button><button class="bt-tool">💾 保存场景</button></div><button class="btn-primary" style="margin-top:16px;padding:14px 32px;background:linear-gradient(135deg,#6366f1,#a855f7);border:none;border-radius:14px;color:#fff;font-weight:700;cursor:pointer;font-size:1rem" onclick="alert('🏗️ 场景编辑器\\n\\n即将开放！\\n\\n功能包括:\\n• 拖拽放置3D模型\\n• 实时PBR光照预览\\n• 天空盒自定义\\n• 反射探针烘焙\\n• 多人协作编辑\\n• 场景模板市场')">🚀 进入场景编辑器</button></div>
</div>
''' + DH_FOOT + '''
<script>
function selectScene(name){alert('🎬 场景: '+name+'\\n\\n已选择此场景作为默认背景。\\n\\n在完整版本中:\\n• 支持360° 自由旋转预览\\n• 实时加载3D场景\\n• 一键应用到直播/录像\\n• 导出为GLB场景文件')}
</script>''')

# ======================================================================
# 9. emotion.html — 情感引擎
# ======================================================================
w('emotion.html', DH_HEAD.format(title='情感引擎 · AI表情系统', theme='coral-academy') + '''
<style>
.page-container{position:relative;z-index:1;padding-top:80px;max-width:1200px;margin:0 auto}
.hero{text-align:center;padding:40px 20px}
.hero h1{font-size:2.4rem;font-weight:900;background:linear-gradient(135deg,#ef4444,#f97316,#ec4899);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero p{color:var(--text-secondary);margin-top:6px;max-width:650px;margin-left:auto;margin-right:auto}
.emotion-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:12px;padding:0 20px 20px}
.em-card{background:var(--bg-card);border:2px solid var(--border);border-radius:16px;padding:20px 12px;text-align:center;cursor:pointer;transition:all .3s}
.em-card:hover{transform:translateY(-4px);box-shadow:0 10px 32px rgba(239,68,68,.2)}
.em-card .em-icon{font-size:3rem;display:block;margin-bottom:8px;transition:transform .3s}
.em-card:hover .em-icon{transform:scale(1.2)}
.em-card .em-name{font-weight:700;font-size:.85rem}
.em-card .em-intensity{font-size:.68rem;color:var(--text-dim);margin-top:4px}
.emotion-preview{display:flex;gap:20px;padding:0 20px 30px}
.em-preview-main{flex:1;background:var(--bg-card);border:1px solid var(--border);border-radius:20px;min-height:350px;display:flex;align-items:center;justify-content:center}
.em-face{font-size:10rem;transition:all .5s cubic-bezier(.34,1.56,.64,1)}
.em-preview-info{width:300px;display:flex;flex-direction:column;gap:14px}
.epi-card{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:18px}
.epi-card h4{font-size:.85rem;margin-bottom:10px}
.epi-slider label{display:flex;justify-content:space-between;font-size:.75rem;color:var(--text-secondary);margin-bottom:4px}
.epi-slider input[type=range]{width:100%;accent-color:var(--accent);margin-bottom:10px}
.blend-matrix{display:grid;grid-template-columns:repeat(2,1fr);gap:8px;padding:0 20px 30px}
.bm-item{padding:12px;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;display:flex;align-items:center;gap:12px;cursor:pointer;transition:all .3s}
.bm-item:hover{border-color:var(--accent)}
.bm-item .bmi-icon{font-size:2rem}
.bm-item .bmi-info{flex:1}.bm-item .bmi-name{font-weight:600;font-size:.82rem}.bm-item .bmi-val{font-size:.72rem;color:var(--text-dim)}
@media(max-width:768px){.emotion-grid{grid-template-columns:repeat(3,1fr)}.emotion-preview{flex-direction:column}.em-preview-info{width:100%}.hero h1{font-size:1.8rem}}
</style>
</head>
<body>
<div id="nav-placeholder"></div>
<div class="page-container">
  <div class="hero"><h1>💓 情感引擎 · AI表情系统</h1><p>让数字人拥有真实的情感表达。基于心理学情感模型，支持7种基本情绪 + 24种微妙表情混合——AI根据对话内容和上下文自动调节。</p></div>
  <div class="emotion-grid">
    <div class="em-card" onclick="setEmotion('happy')"><span class="em-icon">😊</span><div class="em-name">开心</div><div class="em-intensity">Joy · 愉悦</div></div>
    <div class="em-card" onclick="setEmotion('sad')"><span class="em-icon">😢</span><div class="em-name">悲伤</div><div class="em-intensity">Sadness · 哀伤</div></div>
    <div class="em-card" onclick="setEmotion('angry')"><span class="em-icon">😠</span><div class="em-name">愤怒</div><div class="em-intensity">Anger · 愤怒</div></div>
    <div class="em-card" onclick="setEmotion('surprised')"><span class="em-icon">😲</span><div class="em-name">惊讶</div><div class="em-intensity">Surprise · 诧异</div></div>
    <div class="em-card" onclick="setEmotion('fear')"><span class="em-icon">😨</span><div class="em-name">恐惧</div><div class="em-intensity">Fear · 害怕</div></div>
    <div class="em-card" onclick="setEmotion('disgust')"><span class="em-icon">😖</span><div class="em-name">厌恶</div><div class="em-intensity">Disgust · 反感</div></div>
  </div>
  <div class="emotion-preview">
    <div class="em-preview-main"><span class="em-face" id="emFace">😊</span></div>
    <div class="em-preview-info">
      <div class="epi-card"><h4>🎭 情绪强度</h4><div class="epi-slider"><label><span>整体强度</span><span id="ev1">70%</span></label><input type="range" min="0" max="100" value="70" oninput="updateEmotion('ev1',this.value+'%')"></div></div>
      <div class="epi-card"><h4>🧠 混合表情</h4><div class="epi-slider"><label><span>开心成分</span><span id="ev2">60%</span></label><input type="range" min="0" max="100" value="60" oninput="updateEmotion('ev2',this.value+'%')"></div><div class="epi-slider"><label><span>惊讶成分</span><span id="ev3">20%</span></label><input type="range" min="0" max="100" value="20" oninput="updateEmotion('ev3',this.value+'%')"></div></div>
    </div>
  </div>
  <div style="padding:0 20px"><h2 style="font-size:1.3rem;margin-bottom:14px">🧬 情感混合矩阵</h2></div>
  <div class="blend-matrix">
    <div class="bm-item" onclick="setEmotion('happy')"><span class="bmi-icon">😊</span><div class="bmi-info"><div class="bmi-name">开心 + 惊讶</div><div class="bmi-val">惊喜表情 · 适用于收到礼物</div></div></div>
    <div class="bm-item" onclick="setEmotion('sad')"><span class="bmi-icon">😢</span><div class="bmi-info"><div class="bmi-name">悲伤 + 愤怒</div><div class="bmi-val">委屈表情 · 适用于被误解</div></div></div>
    <div class="bm-item" onclick="setEmotion('happy')"><span class="bmi-icon">😊</span><div class="bmi-info"><div class="bmi-name">开心 + 害羞</div><div class="bmi-val">羞涩微笑 · 适用于被夸奖</div></div></div>
    <div class="bm-item" onclick="setEmotion('surprised')"><span class="bmi-icon">😲</span><div class="bmi-info"><div class="bmi-name">惊讶 + 恐惧</div><div class="bmi-val">惊恐表情 · 适用于突发惊吓</div></div></div>
  </div>
</div>
''' + DH_FOOT + '''
<script>
const emotions={happy:'😊',sad:'😢',angry:'😠',surprised:'😲',fear:'😨',disgust:'😖'};
function setEmotion(e){const face=document.getElementById('emFace');face.textContent=emotions[e];face.style.transform='scale(1.3)';setTimeout(()=>face.style.transform='scale(1)',150);document.querySelectorAll('.em-card').forEach(c=>c.style.borderColor='var(--border)')}
function updateEmotion(id,val){document.getElementById(id).textContent=val}
</script>''')

# ======================================================================
# 10. ai-chat.html — AI角色对话
# ======================================================================
w('ai-chat.html', DH_HEAD.format(title='AI角色对话 · 智能互动', theme='sakura-academy') + '''
<style>
.page-container{position:relative;z-index:1;padding-top:80px;max-width:1200px;margin:0 auto}
.hero{text-align:center;padding:40px 20px}
.hero h1{font-size:2.4rem;font-weight:900;background:linear-gradient(135deg,#ff6b9d,#a855f7,#6366f1);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero p{color:var(--text-secondary);margin-top:6px;max-width:600px;margin-left:auto;margin-right:auto}
.chat-layout{display:flex;gap:20px;padding:0 20px 30px}
.chat-sidebar{width:280px;display:flex;flex-direction:column;gap:14px}
.char-list{display:flex;flex-direction:column;gap:6px}
.char-item{padding:14px;border:2px solid var(--border);border-radius:14px;cursor:pointer;transition:all .3s;display:flex;align-items:center;gap:12px}
.char-item:hover,.char-item.active{border-color:var(--accent);background:rgba(255,107,157,.05)}
.char-item .ci-avatar{font-size:2rem;flex-shrink:0}
.char-item .ci-info{flex:1;min-width:0}
.char-item .ci-name{font-weight:600;font-size:.85rem}
.char-item .ci-role{font-size:.7rem;color:var(--text-dim)}
.char-item .ci-status{width:8px;height:8px;border-radius:50%;flex-shrink:0}
.ci-status.online{background:#22c55e}.ci-status.busy{background:#f59e0b}.ci-status.offline{background:#6b7280}
.chat-main{flex:1;display:flex;flex-direction:column;background:var(--bg-card);border:1px solid var(--border);border-radius:20px;overflow:hidden}
.chat-header{padding:16px 20px;border-bottom:1px solid var(--border);display:flex;align-items:center;gap:12px}
.chat-header .ch-avatar{font-size:2rem}
.chat-header .ch-name{font-weight:700;font-size:.95rem}
.chat-header .ch-status{font-size:.72rem;color:#22c55e}
.chat-messages{flex:1;overflow-y:auto;padding:20px;display:flex;flex-direction:column;gap:14px;max-height:400px}
.msg{max-width:80%;padding:12px 16px;border-radius:16px;font-size:.85rem;line-height:1.5;animation:msgSlide .3s ease-out}
@keyframes msgSlide{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
.msg.bot{align-self:flex-start;background:var(--bg-secondary);color:var(--text);border-bottom-left-radius:4px}
.msg.user{align-self:flex-end;background:linear-gradient(135deg,var(--accent),var(--accent-secondary,#a78bfa));color:#fff;border-bottom-right-radius:4px}
.chat-input-area{padding:16px 20px;border-top:1px solid var(--border);display:flex;gap:10px}
.chat-input-area input{flex:1;padding:14px;border:2px solid var(--border);border-radius:14px;background:var(--bg-secondary);color:var(--text);outline:none;font-size:.88rem;transition:border-color .3s}
.chat-input-area input:focus{border-color:var(--accent)}
.chat-input-area button{padding:14px 24px;background:linear-gradient(135deg,var(--accent),var(--accent-secondary,#a78bfa));border:none;border-radius:14px;color:#fff;font-weight:700;cursor:pointer}
.persona-section{padding:0 20px 40px}
.persona-section h2{font-size:1.3rem;margin-bottom:14px}
.persona-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.persona-card{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:20px;text-align:center;transition:all .3s;cursor:pointer}
.persona-card:hover{transform:translateY(-4px);box-shadow:0 10px 30px rgba(255,107,157,.15)}
.persona-card .pc-avatar{font-size:3rem;display:block;margin-bottom:10px}
.persona-card .pc-name{font-weight:700;font-size:.9rem;margin-bottom:4px}
.persona-card .pc-desc{font-size:.75rem;color:var(--text-dim);line-height:1.4}
@media(max-width:768px){.chat-layout{flex-direction:column}.chat-sidebar{width:100%}.persona-grid{grid-template-columns:repeat(2,1fr)}.hero h1{font-size:1.8rem}}
</style>
</head>
<body>
<div id="nav-placeholder"></div>
<div class="page-container">
  <div class="hero"><h1>💬 AI角色对话 · 智能互动</h1><p>与你的数字人角色进行自然对话。每个角色拥有独立的人设、性格和知识库——从闲聊到角色扮演，体验最真实的AI互动。</p></div>
  <div class="chat-layout">
    <div class="chat-sidebar">
      <div class="char-list">
        <div class="char-item active" onclick="selectChar('琉璃','🌌','online',this)"><span class="ci-avatar">🌌</span><div class="ci-info"><div class="ci-name">星野 琉璃</div><div class="ci-role">赛博歌姬 · 元气少女</div></div><span class="ci-status online"></span></div>
        <div class="char-item" onclick="selectChar('龙姬','🐉','online',this)"><span class="ci-avatar">🐉</span><div class="ci-info"><div class="ci-name">虚空龙姬 Vaelith</div><div class="ci-role">龙族公主 · 威严御姐</div></div><span class="ci-status online"></span></div>
        <div class="char-item" onclick="selectChar('喵酱','🐱','busy',this)"><span class="ci-avatar">🐱</span><div class="ci-info"><div class="ci-name">喵酱 Neko</div><div class="ci-role">治愈主播 · 可爱萝莉</div></div><span class="ci-status busy"></span></div>
        <div class="char-item" onclick="selectChar('管家','🤖','online',this)"><span class="ci-avatar">🤖</span><div class="ci-info"><div class="ci-name">AI学院管家</div><div class="ci-role">智能助手 · 专业稳重</div></div><span class="ci-status online"></span></div>
      </div>
      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:14px;font-size:.78rem;color:var(--text-dim);line-height:1.6"><strong>💡 提示：</strong><br>• 角色保持人设对话<br>• 支持中/日/英多语言<br>• 可创建自定义角色<br>• 对话历史云端保存</div>
    </div>
    <div class="chat-main">
      <div class="chat-header"><span class="ch-avatar" id="chatAvatar">🌌</span><div><div class="ch-name" id="chatName">星野 琉璃</div><div class="ch-status" id="chatStatus">● 在线</div></div></div>
      <div class="chat-messages" id="chatMsgs">
        <div class="msg bot">こんにちは！我是星野琉璃~ 来自龙墟世界的赛博歌姬！有什么想聊的吗？唱歌、游戏、动漫——什么都可以哦~ ✨</div>
      </div>
      <div class="chat-input-area"><input type="text" id="chatInput" placeholder="输入消息..." onkeydown="if(event.key==='Enter')sendMsg()"><button onclick="sendMsg()">发送</button></div>
    </div>
  </div>
  <div class="persona-section"><h2>🎭 更多AI角色</h2><div class="persona-grid"><div class="persona-card"><span class="pc-avatar">⚔️</span><div class="pc-name">剑心</div><div class="pc-desc">武士浪人<br>严肃但有温柔一面</div></div><div class="persona-card"><span class="pc-avatar">🧙</span><div class="pc-name">魔法师Luna</div><div class="pc-desc">天才魔法少女<br>傲娇性格</div></div><div class="persona-card"><span class="pc-avatar">👻</span><div class="pc-name">幽灵君</div><div class="pc-desc">可爱幽灵<br>喜欢恶作剧</div></div><div class="persona-card"><span class="pc-avatar">🎸</span><div class="pc-name">摇滚Kai</div><div class="pc-desc">热血吉他手<br>永不言弃</div></div></div></div>
</div>
''' + DH_FOOT + '''
<script>
let currentChar='琉璃';
const charReplies={琉璃:['えへへ~ 谢谢夸奖！','来听我唱首新歌吧！','龙墟世界超好玩的哦~','今天也在努力直播！','有什么烦恼都可以跟我说哦 ✨'],龙姬:['吾乃虚空之主，凡人有何疑问？','龙墟的领域不容侵犯。','你，似乎有些不同...','想了解龙族的秘密吗？','力量需要智慧来驾驭。'],喵酱:['喵~ 欢迎来找我玩！','今天也是元气满满的一天喵！','给你小鱼干~ 🐟','要不要一起打滚？','喵喵喵喵喵！（翻译：好开心）'],管家:['您好，有什么可以帮助您的？','根据数据分析，我推荐...','已为您查询相关信息。','需要我帮您安排日程吗？','龙奕学院随时为您服务。']};
function selectChar(name,avatar,status,btn){currentChar=name;document.querySelectorAll('.char-item').forEach(b=>b.classList.remove('active'));btn.classList.add('active');document.getElementById('chatAvatar').textContent=avatar;document.getElementById('chatName').textContent=name==='琉璃'?'星野 琉璃':name==='龙姬'?'虚空龙姬 Vaelith':name==='喵酱'?'喵酱 Neko':'AI学院管家';document.getElementById('chatStatus').innerHTML=(status==='online'?'●':'●')+' '+(status==='online'?'在线':status==='busy'?'忙碌':'离线');const msgs=document.getElementById('chatMsgs');msgs.innerHTML='';addBotMsg('你好！我是'+name+'。有什么想聊的？')}
function addMsg(text,isUser){const msgs=document.getElementById('chatMsgs');const d=document.createElement('div');d.className='msg '+(isUser?'user':'bot');d.textContent=text;msgs.appendChild(d);msgs.scrollTop=msgs.scrollHeight}
function addBotMsg(text){addMsg(text,false)}
function sendMsg(){const input=document.getElementById('chatInput');const text=input.value.trim();if(!text)return;addMsg(text,true);input.value='';setTimeout(()=>{const replies=charReplies[currentChar];addBotMsg(replies[Math.floor(Math.random()*replies.length)])},600+Math.random()*800)}
</script>''')

print('=== Digital-Human Pages: Batch 2 done (clone, scene, emotion, ai-chat) ===')
print('All 10 digital-human pages completed!')

# -*- coding: utf-8 -*-
"""深度重写全部10个数字人子页面 — 实质性内容、交互功能、专业介绍"""
import os

BASE = r"C:\Users\28767\Downloads\cosrealm-site\pages\digital-human"
os.makedirs(BASE, exist_ok=True)

def write_page(filename, content):
    path = os.path.join(BASE, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  ✓ {filename} ({len(content)} chars)')

# Common head for all digital-human pages
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

# ======================================================================
# 1. studio.html — 数字人Studio (核心建模页面)
# ======================================================================
write_page('studio.html', DH_HEAD.format(title='数字人Studio · AI建模工坊', theme='sunset-academy') + '''
<style>
.page-container{position:relative;z-index:1;padding-top:80px;max-width:1300px;margin:0 auto}
.hero{text-align:center;padding:40px 20px 20px}
.hero h1{font-size:2.4rem;font-weight:900;background:linear-gradient(135deg,#ec4899,#a855f7,#6366f1);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero p{color:var(--text-secondary);margin-top:8px;max-width:600px;margin-left:auto;margin-right:auto}
.studio-layout{display:flex;gap:20px;padding:0 20px 40px}
/* Preview */
.preview-area{flex:1;background:var(--bg-card);border:1px solid var(--border);border-radius:20px;display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:520px;position:relative;overflow:hidden}
.preview-model{position:relative;width:200px;height:260px;margin-bottom:16px}
.preview-body{width:160px;height:200px;background:linear-gradient(135deg,var(--accent),var(--accent-secondary,#a78bfa));border-radius:80px 80px 30px 30px;margin:0 auto;position:relative;transition:all .5s}
.preview-head{width:100px;height:100px;background:linear-gradient(135deg,#fce7f3,#f5d0fe);border-radius:50%;position:absolute;top:-40px;left:30px;transition:all .5s}
.preview-eyes{position:absolute;top:35px;left:50%;transform:translateX(-50%);display:flex;gap:14px}
.preview-eye{width:14px;height:16px;background:#1e1b4b;border-radius:50%;transition:all .5s}
.preview-mouth{position:absolute;top:60px;left:50%;transform:translateX(-50%);width:16px;height:8px;border-radius:0 0 10px 10px;background:#ec4899;transition:all .5s}
.preview-hair{position:absolute;top:-15px;left:-5px;width:110px;height:50px;border-radius:50px 50px 10px 10px;transition:all .5s}
.preview-label{font-size:.82rem;color:var(--text-secondary);text-align:center;margin-top:8px}
.expression-bar{display:flex;gap:6px;margin-top:10px;flex-wrap:wrap;justify-content:center}
.expr-btn{padding:6px 12px;border:1px solid var(--border);border-radius:20px;background:none;color:var(--text-secondary);cursor:pointer;font-size:.75rem;transition:all .3s}
.expr-btn:hover,.expr-btn.active{border-color:var(--accent);color:#fff;background:var(--accent)}
/* Controls */
.control-panel{width:380px;overflow-y:auto;max-height:calc(100vh - 100px)}
.ctrl-card{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:18px;margin-bottom:12px}
.ctrl-card h3{font-size:.88rem;margin-bottom:12px;display:flex;align-items:center;gap:6px}
/* Style presets */
.style-presets{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.style-preset{padding:16px 10px;border:2px solid var(--border);border-radius:12px;text-align:center;cursor:pointer;transition:all .3s;font-size:.78rem}
.style-preset:hover,.style-preset.active{border-color:var(--accent);background:rgba(236,72,153,.08)}
.style-preset .sp-icon{display:block;font-size:1.8rem;margin-bottom:4px}
/* Sliders */
.slider-group{margin-bottom:10px}
.slider-group label{display:flex;justify-content:space-between;font-size:.75rem;color:var(--text-secondary);margin-bottom:3px}
.slider-group input[type=range]{width:100%;accent-color:var(--accent)}
/* Body types */
.body-types{display:grid;grid-template-columns:repeat(4,1fr);gap:6px}
.bt-item{padding:10px 6px;border:2px solid var(--border);border-radius:10px;text-align:center;cursor:pointer;font-size:.72rem;transition:all .3s}
.bt-item:hover,.bt-item.active{border-color:var(--accent);background:rgba(236,72,153,.08)}
/* Generate */
.generate-btn{width:100%;padding:16px;background:linear-gradient(135deg,#ec4899,#a855f7);border:none;border-radius:14px;color:#fff;font-size:1.1rem;font-weight:700;cursor:pointer;transition:all .3s;margin-top:4px;letter-spacing:1px}
.generate-btn:hover{box-shadow:0 8px 32px rgba(236,72,153,.4);transform:translateY(-2px)}
.export-options{display:flex;gap:8px;margin-top:12px}
.export-btn{flex:1;padding:10px;border:1px solid var(--border);border-radius:10px;background:none;color:var(--text-secondary);cursor:pointer;font-size:.75rem;text-align:center;transition:all .3s}
.export-btn:hover{border-color:var(--accent);color:var(--accent)}
/* Info section */
.info-section{padding:0 20px 40px;max-width:1100px;margin:0 auto}
.info-section h2{font-size:1.3rem;margin-bottom:14px}
.info-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.info-card{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:24px}
.info-card .ic-icon{font-size:2.5rem;margin-bottom:10px}
.info-card h4{font-size:.95rem;margin-bottom:6px}
.info-card p{font-size:.82rem;color:var(--text-secondary);line-height:1.6}
.model-specs{display:flex;gap:24px;flex-wrap:wrap;margin-top:10px}
.model-spec{text-align:center}
.model-spec .ms-val{font-size:1.1rem;font-weight:700;color:var(--accent)}
.model-spec .ms-label{font-size:.7rem;color:var(--text-dim)}
@media(max-width:768px){.studio-layout{flex-direction:column}.control-panel{width:100%}.info-grid{grid-template-columns:1fr}}
</style>
</head>
<body>
<div id="nav-placeholder"></div>
<div class="page-container">
  <div class="hero"><h1>🤖 数字人 Studio — AI 建模工坊</h1><p>从零创建你的专属数字人形象。支持二次元、写实、赛博、幻想四大风格体系，18项参数精细调节，一键导出多格式模型。</p><div class="model-specs"><div class="model-spec"><span class="ms-val">54,000+</span><span class="ms-label">面数支持</span></div><div class="model-spec"><span class="ms-val">PBR</span><span class="ms-label">材质系统</span></div><div class="model-spec"><span class="ms-val">72</span><span class="ms-label">BlendShape</span></div><div class="model-spec"><span class="ms-val">VRM/GLB</span><span class="ms-label">多格式导出</span></div></div></div>
  <div class="studio-layout">
    <div class="preview-area hologram">
      <div class="preview-model" id="modelPreview">
        <div class="preview-hair" id="previewHair" style="background:linear-gradient(135deg,#ff6b9d,#a855f7)"></div>
        <div class="preview-head" id="previewHead"><div class="preview-eyes"><span class="preview-eye"></span><span class="preview-eye"></span></div><div class="preview-mouth"></div></div>
        <div class="preview-body" id="previewBody"></div>
      </div>
      <div class="preview-label" id="previewLabel">🎭 二次元风格 · 默认体型</div>
      <div class="expression-bar">
        <button class="expr-btn active" onclick="setExpr('neutral',this)">😊 默认</button>
        <button class="expr-btn" onclick="setExpr('happy',this)">😆 开心</button>
        <button class="expr-btn" onclick="setExpr('surprised',this)">😲 惊讶</button>
        <button class="expr-btn" onclick="setExpr('sad',this)">😢 悲伤</button>
        <button class="expr-btn" onclick="setExpr('angry',this)">😠 愤怒</button>
        <button class="expr-btn" onclick="setExpr('blush',this)">😳 害羞</button>
      </div>
    </div>
    <div class="control-panel">
      <div class="ctrl-card"><h3>🎨 风格体系</h3><div class="style-presets"><div class="style-preset active" data-style="anime" onclick="setStyle('anime',this)"><span class="sp-icon">🎭</span>二次元</div><div class="style-preset" data-style="realistic" onclick="setStyle('realistic',this)"><span class="sp-icon">👤</span>写实</div><div class="style-preset" data-style="cyber" onclick="setStyle('cyber',this)"><span class="sp-icon">🤖</span>赛博</div><div class="style-preset" data-style="fantasy" onclick="setStyle('fantasy',this)"><span class="sp-icon">🧝</span>幻想</div><div class="style-preset" data-style="chibi" onclick="setStyle('chibi',this)"><span class="sp-icon">🍡</span>Q版</div><div class="style-preset" data-style="kemono" onclick="setStyle('kemono',this)"><span class="sp-icon">🐾</span>兽耳</div></div></div>
      <div class="ctrl-card"><h3>👤 体型预设</h3><div class="body-types"><div class="bt-item active" onclick="setBody('default',this)">标准</div><div class="bt-item" onclick="setBody('tall',this)">高挑</div><div class="bt-item" onclick="setBody('petite',this)">娇小</div><div class="bt-item" onclick="setBody('muscular',this)">健壮</div></div></div>
      <div class="ctrl-card"><h3>⚙️ 面部参数</h3><div class="slider-group"><label><span>脸型圆润度</span><span id="fv1">50</span></label><input type="range" min="0" max="100" value="50" oninput="updateSlider('fv1',this.value);updateFace()"></div><div class="slider-group"><label><span>眼距宽度</span><span id="fv2">50</span></label><input type="range" min="0" max="100" value="50" oninput="updateSlider('fv2',this.value);updateFace()"></div><div class="slider-group"><label><span>眼睛大小</span><span id="fv3">50</span></label><input type="range" min="0" max="100" value="50" oninput="updateSlider('fv3',this.value);updateFace()"></div><div class="slider-group"><label><span>鼻梁高度</span><span id="fv4">50</span></label><input type="range" min="0" max="100" value="50" oninput="updateSlider('fv4',this.value);updateFace()"></div><div class="slider-group"><label><span>嘴型宽度</span><span id="fv5">50</span></label><input type="range" min="0" max="100" value="50" oninput="updateSlider('fv5',this.value);updateFace()"></div><div class="slider-group"><label><span>下巴角度</span><span id="fv6">50</span></label><input type="range" min="0" max="100" value="50" oninput="updateSlider('fv6',this.value);updateFace()"></div></div>
      <div class="ctrl-card"><h3>🎨 色彩配置</h3><div class="slider-group"><label><span>发色色相</span><span id="cv1">330</span></label><input type="range" min="0" max="360" value="330" oninput="updateSlider('cv1',this.value);updateHair()"></div><div class="slider-group"><label><span>肤色明度</span><span id="cv2">75</span></label><input type="range" min="50" max="100" value="75" oninput="updateSlider('cv2',this.value);updateFace()"></div><div class="slider-group"><label><span>瞳色色相</span><span id="cv3">240</span></label><input type="range" min="0" max="360" value="240" oninput="updateSlider('cv3',this.value);updateFace()"></div></div>
      <button class="generate-btn" onclick="generateModel()">✨ 生成完整数字人模型</button>
      <div class="export-options"><button class="export-btn" onclick="exportModel('vrm')">📦 VRM (VRChat)</button><button class="export-btn" onclick="exportModel('glb')">🌐 GLB (Web)</button><button class="export-btn" onclick="exportModel('fbx')">🎬 FBX (Unreal)</button></div>
    </div>
  </div>
  <div class="info-section">
    <h2>🔬 技术规格</h2>
    <div class="info-grid">
      <div class="info-card"><div class="ic-icon">🦴</div><h4>骨骼系统</h4><p>支持Humanoid标准骨骼、65根骨骼完整绑定、IK/FK双模式、面部52个BlendShape、物理骨骼模拟（头发/裙摆/尾巴）。兼容Unity Mecanim、Unreal Animation Blueprint、VRM标准。</p></div>
      <div class="info-card"><div class="ic-icon">🎨</div><h4>材质系统</h4><p>PBR(物理基础渲染)全管线支持：Albedo/Normal/Metallic/Roughness/AO/Emission 六张贴图通道。内置二次元Toon Shader、写实Skin Shader、赛博Holo Shader三套材质模板。</p></div>
      <div class="info-card"><div class="ic-icon">💃</div><h4>动画系统</h4><p>内置200+基础动画（走跑跳坐躺挥手比心鞠躬），支持动作捕捉重定向、AI生成口型动画、物理布料模拟。导出时自动烘焙动画数据至模型文件。</p></div>
      <div class="info-card"><div class="ic-icon">📱</div><h4>多平台兼容</h4><p>一键适配VRChat / VSeeFace / LIVE2D / 龙墟元宇宙四种平台。自动处理Shader转换、骨骼映射、表情参数映射。导出版本含PC高配/VR/移动端精简三档。</p></div>
      <div class="info-card"><div class="ic-icon">🧠</div><h4>AI驱动</h4><p>集成GPT-4对话引擎（文字交互）、Whisper语音识别（语音交互）、Stable Diffusion贴图生成（自动生成服装纹理）、AnimateDiff动作生成（文本描述生成动画）。</p></div>
      <div class="info-card"><div class="ic-icon">🔒</div><h4>版权保护</h4><p>每个生成的数字人模型自动注册区块链版权，嵌入不可见的数字水印。导出模型包含创作者签名和版权声明元数据，有效防止模型盗用。</p></div>
    </div>
  </div>
</div>
''' + DH_FOOT + '''
<script>
let currentStyle='anime',currentBody='default',currentExpr='neutral';
const styles={anime:{hair:'linear-gradient(135deg,#ff6b9d,#a855f7)',skin:'#fce7f3',eye:'#6366f1',body:'linear-gradient(135deg,#ec4899,#a855f7)',label:'🎭 二次元风格'},realistic:{hair:'linear-gradient(135deg,#4a3728,#2d1f0e)',skin:'#f5d0c5',eye:'#3b82f6',body:'linear-gradient(135deg,#78716c,#57534e)',label:'👤 写实风格'},cyber:{hair:'linear-gradient(135deg,#22d3ee,#6366f1)',skin:'#e0e7ff',eye:'#22d3ee',body:'linear-gradient(135deg,#06b6d4,#6366f1)',label:'🤖 赛博风格'},fantasy:{hair:'linear-gradient(135deg,#a855f7,#22d3ee)',skin:'#ede9fe',eye:'#a855f7',body:'linear-gradient(135deg,#7c3aed,#06b6d4)',label:'🧝 幻想风格'},chibi:{hair:'linear-gradient(135deg,#f59e0b,#ef4444)',skin:'#fef3c7',eye:'#f59e0b',body:'linear-gradient(135deg,#fbbf24,#ef4444)',label:'🍡 Q版风格'},kemono:{hair:'linear-gradient(135deg,#f97316,#ef4444)',skin:'#fff1f2',eye:'#f97316',body:'linear-gradient(135deg,#fb923c,#ef4444)',label:'🐾 兽耳风格'}};
function setStyle(s,btn){currentStyle=s;document.querySelectorAll('.style-preset').forEach(b=>b.classList.remove('active'));btn.classList.add('active');const st=styles[s];document.getElementById('previewHair').style.background=st.hair;document.getElementById('previewHead').style.background=st.skin;document.querySelectorAll('.preview-eye').forEach(e=>e.style.background=st.eye);document.getElementById('previewBody').style.background=st.body;document.getElementById('previewLabel').textContent=st.label+' · '+({default:'标准',tall:'高挑',petite:'娇小',muscular:'健壮'})[currentBody]+'体型'}
function setBody(type,btn){currentBody=type;document.querySelectorAll('.bt-item').forEach(b=>b.classList.remove('active'));btn.classList.add('active');const scales={default:'scale(1)',tall:'scale(1,1.2)',petite:'scale(.85,.9)',muscular:'scale(1.15,1)'};document.getElementById('previewBody').style.transform=scales[type];document.getElementById('previewLabel').textContent=styles[currentStyle].label+' · '+({default:'标准',tall:'高挑',petite:'娇小',muscular:'健壮'})[type]+'体型'}
function setExpr(expr,btn){currentExpr=expr;document.querySelectorAll('.expr-btn').forEach(b=>b.classList.remove('active'));btn.classList.add('active');const mouthShapes={neutral:'0 0 10px 10px',happy:'50% 0 0 0',surprised:'50%',sad:'0 0 0 0',angry:'0 0 5px 5px',blush:'50% 50% 0 0'};document.querySelector('.preview-mouth').style.borderRadius=mouthShapes[expr];const eyeSizes={neutral:'14px',happy:'14px',surprised:'18px',sad:'12px',angry:'13px',blush:'14px'};document.querySelectorAll('.preview-eye').forEach(e=>{e.style.width=eyeSizes[expr];e.style.height=expr==='surprised'?'20px':expr==='sad'?'12px':'16px'})}
function updateSlider(id,val){document.getElementById(id).textContent=val}
function updateFace(){const v1=parseInt(document.getElementById('fv1').textContent);const v2=parseInt(document.getElementById('fv2').textContent);const v3=parseInt(document.getElementById('fv3').textContent);const v4=parseInt(document.getElementById('fv4').textContent);const v5=parseInt(document.getElementById('fv5').textContent);const v6=parseInt(document.getElementById('fv6').textContent);const head=document.getElementById('previewHead');head.style.borderRadius=(40+v1/3)+'%';head.style.width=(90+v3/2)+'px';head.style.height=(90+v3/2)+'px';const eyes=document.querySelector('.preview-eyes');eyes.style.gap=(10+v2/4)+'px';const mouth=document.querySelector('.preview-mouth');mouth.style.width=(12+v5/4)+'px'}
function updateHair(){const hue=parseInt(document.getElementById('cv1').textContent);document.getElementById('previewHair').style.background='linear-gradient(135deg,hsl('+hue+',80%,65%),hsl('+((hue+60)%360)+',70%,55%))'}
function generateModel(){const btn=event.target;btn.textContent='⏳ AI引擎运转中...';btn.disabled=true;const phases=['🔬 扫描参考图库','🦴 生成骨骼绑定','🎨 烘焙PBR材质','💃 加载动画蓝图','🧠 注入AI驱动','✅ 完成！'];let i=0;const iv=setInterval(()=>{if(i<phases.length){btn.textContent=phases[i];i++}else{clearInterval(iv);btn.textContent='✅ 模型生成成功！点击导出';btn.style.background='linear-gradient(135deg, #22c55e, #14b8a6)';setTimeout(()=>{btn.textContent='✨ 生成完整数字人模型';btn.style.background='linear-gradient(135deg,#ec4899,#a855f7)';btn.disabled=false},3000)}},600)}
function exportModel(fmt){const names={vrm:'VRM (VRChat兼容)',glb:'GLB (Web/移动端)',fbx:'FBX (Unreal引擎)'};alert('📦 导出格式: '+names[fmt]+'\\n\\n包含内容:\\n• 完整骨骼绑定（Humanoid）\\n• PBR材质（6通道贴图）\\n• 52 BlendShape面部表情\\n• 200+基础动画库\\n• 区块链版权证书\\n\\n模型ID: DH-'+Date.now().toString(36).toUpperCase()+'\\n\\n导出文件将通过邮件发送至您的注册邮箱。')}
</script>''')

# ======================================================================
# 2. showroom.html — 数字人展馆
# ======================================================================
write_page('showroom.html', DH_HEAD.format(title='数字人展馆 · 虚拟偶像阵列', theme='starlight-academy') + '''
<style>
.page-container{position:relative;z-index:1;padding-top:80px;max-width:1300px;margin:0 auto}
.hero{text-align:center;padding:40px 20px}
.hero h1{font-size:2.4rem;font-weight:900;background:linear-gradient(135deg,#a78bfa,#ec4899,#f59e0b);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero p{color:var(--text-secondary);margin-top:6px;max-width:600px;margin-left:auto;margin-right:auto}
.cat-tabs{display:flex;justify-content:center;gap:10px;padding:0 20px 20px;flex-wrap:wrap}
.cat-tab{padding:8px 20px;border:2px solid var(--border);border-radius:24px;cursor:pointer;font-size:.82rem;font-weight:600;background:none;color:var(--text-secondary);transition:all .3s}
.cat-tab:hover,.cat-tab.active{border-color:var(--accent);color:var(--accent);background:rgba(167,139,250,.08)}
.showroom-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:18px;padding:0 20px 20px}
.dh-card{background:var(--bg-card);border-radius:18px;overflow:hidden;border:1px solid var(--border);transition:all .35s;cursor:pointer}
.dh-card:hover{transform:translateY(-6px);box-shadow:0 16px 48px rgba(167,139,250,.25)}
.dh-card .dhc-cover{height:240px;position:relative;overflow:hidden}
.dh-card .dhc-cover-inner{width:100%;height:100%;display:flex;align-items:center;justify-content:center;font-size:5rem;transition:transform .5s}
.dh-card:hover .dhc-cover-inner{transform:scale(1.08)}
.dh-card .dhc-badge{position:absolute;top:10px;right:10px;padding:4px 10px;border-radius:10px;font-size:.68rem;font-weight:700;color:#fff}
.dh-card .dhc-rank{position:absolute;top:10px;left:10px;background:rgba(0,0,0,.7);color:#fff;padding:4px 10px;border-radius:10px;font-size:.72rem;font-weight:700;backdrop-filter:blur(6px)}
.dh-card .dhc-body{padding:18px}
.dh-card .dhc-name{font-weight:700;font-size:1rem;margin-bottom:4px}
.dh-card .dhc-creator{font-size:.78rem;color:var(--text-dim);margin-bottom:8px}
.dh-card .dhc-desc{font-size:.82rem;color:var(--text-secondary);line-height:1.5;margin-bottom:10px}
.dh-card .dhc-tags{display:flex;gap:6px;flex-wrap:wrap}
.dh-card .dhc-tag{padding:3px 10px;border-radius:10px;font-size:.7rem;border:1px solid var(--border);color:var(--text-dim)}
.dh-card .dhc-stats{display:flex;justify-content:space-between;margin-top:12px;padding-top:12px;border-top:1px solid var(--border);font-size:.75rem;color:var(--text-dim)}
.submit-section{text-align:center;padding:30px;margin:0 20px 40px;background:var(--bg-card);border:1px solid var(--border);border-radius:20px}
.submit-section h2{font-size:1.2rem;margin-bottom:8px}
@media(max-width:768px){.showroom-grid{grid-template-columns:1fr}.hero h1{font-size:1.8rem}}
</style>
</head>
<body>
<div id="nav-placeholder"></div>
<div class="page-container">
  <div class="hero"><h1>🏛️ 数字人展馆 — 虚拟偶像阵列</h1><p>浏览社区创作者们精心打造的数字人形象。从Vtuber到Cos数字分身，从原创角色到经典还原——这里汇聚了龙奕学院最顶尖的数字人创作。</p></div>
  <div class="cat-tabs"><button class="cat-tab active" onclick="filter('all',this)">全部</button><button class="cat-tab" onclick="filter('vtuber',this)">🎤 Vtuber</button><button class="cat-tab" onclick="filter('cos',this)">🎭 Cos还原</button><button class="cat-tab" onclick="filter('original',this)">✨ 原创角色</button><button class="cat-tab" onclick="filter('fantasy',this)">🐉 幻想生物</button><button class="cat-tab" onclick="filter('mecha',this)">🤖 机甲系</button></div>
  <div class="showroom-grid" id="showroomGrid"></div>
  <div class="submit-section"><h2>🌟 展示你的数字人作品</h2><p style="color:var(--text-secondary);margin-bottom:14px">将你在Studio中创建的数字人提交至展馆，获得社区曝光和官方推荐</p><button class="btn-primary btn-lg" onclick="alert('📤 作品提交\\n\\n1. 选择你的数字人模型\\n2. 填写作品介绍和标签\\n3. 上传展示截图/视频\\n4. 提交审核（24小时内完成）\\n\\n此功能将在下个版本上线！')" style="padding:12px 32px;background:var(--gradient-btn);border:none;border-radius:12px;color:#fff;font-weight:700;cursor:pointer;font-size:1rem">提交作品</button></div>
</div>
''' + DH_FOOT + '''
<script>
const digitalHumans=[{name:'星野 琉璃 (Hoshino Ruri)',creator:'by 虚空造物局',d:'原创Vtuber · 赛博歌姬主题。搭载AI情感引擎和实时语音合成，可在直播中根据弹幕情绪自动调整表情和语调。',tags:['Vtuber','赛博','原创'],cat:'vtuber',stats:'12.4万粉丝 · 892作品',rank:'#1',badge:'🏆 人气王',c:'linear-gradient(135deg,#22d3ee,#a855f7)',icon:'🌌'},{name:'初音未来 Miku - 龙奕特制版',creator:'by 龙奕AI实验室',d:'基于Crypton官方授权的初音未来3D模型进行AI增强：更高精度的面部捕捉、自然语言驱动的舞蹈动作生成、实时换装系统。',tags:['Cos还原','Vocaloid','官方授权'],cat:'cos',stats:'45.6万粉丝 · 2,340作品',rank:'#2',badge:'🔥 爆款',c:'linear-gradient(135deg,#22d3ee,#39ff14)',icon:'🎤'},{name:'虚空龙姬 Vaelith',creator:'by 龙墟世界团队',d:'龙奕学院元宇宙世界观中的核心角色。完全原创的龙族少女数字人，支持龙形态/人形态双模式切换，配备粒子龙翼特效。',tags:['原创角色','龙族','官方'],cat:'original',stats:'8.9万粉丝 · 567作品',rank:'#3',badge:'👑 官方',c:'linear-gradient(135deg,#7c3aed,#f59e0b)',icon:'🐉'},{name:'雷电将军 Raiden Shogun',creator:'by Cos大神·雷',d:'高度还原《原神》雷电将军。1:1比例建模，配备梦想一心太刀和雷元素特效粒子系统。支持拔刀/纳刀动画切换。',tags:['Cos还原','原神','武器'],cat:'cos',stats:'23.1万粉丝 · 1,890作品',rank:'#4',badge:'⭐ 精选',c:'linear-gradient(135deg,#a855f7,#ec4899)',icon:'⚡'},{name:'喵酱 Neko-chan',creator:'by 独立创作者·猫薄荷',d:'Q版猫耳Vtuber，主打治愈系直播。搭载AI卖萌引擎——自动识别观众送礼并触发对应的可爱反应（蹭蹭、打滚、摇尾巴）。',tags:['Vtuber','Q版','兽耳'],cat:'vtuber',stats:'6.7万粉丝 · 423作品',rank:'#5',badge:'💖 可爱',c:'linear-gradient(135deg,#fbbf24,#ef4444)',icon:'🐱'},{name:'赛博武士 · 斩',creator:'by 机甲工坊',d:'科幻机甲系原创数字人。融合日本武士文化与赛博朋克美学——全息刀、粒子推进器、可变形装甲。支持战斗姿态和待机姿态。',tags:['机甲','原创','动作'],cat:'mecha',stats:'4.2万粉丝 · 196作品',rank:'#6',badge:'⚔️ 酷炫',c:'linear-gradient(135deg,#ef4444,#1e1b4b)',icon:'🤖'},{name:'精灵公主 Aelindra',creator:'by 幻想工坊',d:'高精度写实风格精灵角色。透明翅膀、流动光效、树叶编织的服装——采用PBR材质完整渲染。专为VRChat社交场景优化。',tags:['幻想','写实','VRChat'],cat:'fantasy',stats:'9.8万粉丝 · 734作品',rank:'#7',badge:'✨ 唯美',c:'linear-gradient(135deg,#22c55e,#06b6d4)',icon:'🧝'},{name:'影山 飞雄 - Haikyuu!!',creator:'by 运动番Cos团',d:'《排球少年!!》影山飞雄的1:1数字人还原。包含乌野高校队服、排球道具、发球/托球/扣球动画组。高度还原角色表情。',tags:['Cos还原','运动番','动画'],cat:'cos',stats:'11.3万粉丝 · 856作品',rank:'#8',badge:'🔥 热作',c:'linear-gradient(135deg,#f97316,#3b82f6)',icon:'🏐'}];
function renderShowroom(filter){const grid=document.getElementById('showroomGrid');const list=filter==='all'?digitalHumans:digitalHumans.filter(d=>d.cat===filter);grid.innerHTML=list.map((d,i)=>'<div class="dh-card" onclick="viewDetail(\''+d.name+'\')"><div class="dhc-cover"><div class="dhc-cover-inner" style="background:'+d.c+'">'+d.icon+'</div><span class="dhc-rank">'+d.rank+'</span><span class="dhc-badge" style="background:'+(d.badge.includes('人气')?'#ec4899':d.badge.includes('爆款')?'#f59e0b':d.badge.includes('官方')?'#7c3aed':d.badge.includes('精选')?'#22c55e':'#6366f1')+'">'+d.badge+'</span></div><div class="dhc-body"><div class="dhc-name">'+d.name+'</div><div class="dhc-creator">'+d.creator+'</div><div class="dhc-desc">'+d.d+'</div><div class="dhc-tags">'+d.tags.map(t=>'<span class="dhc-tag">'+t+'</span>').join('')+'</div><div class="dhc-stats"><span>'+d.stats+'</span><span style="color:var(--accent)">查看详情 →</span></div></div></div>').join('')}
function filter(cat,btn){document.querySelectorAll('.cat-tab').forEach(b=>b.classList.remove('active'));btn.classList.add('active');renderShowroom(cat)}
function viewDetail(name){alert('🔍 '+name+'\\n\\n详细页面建设中...\\n\\n即将上线：\\n• 360° 模型预览\\n• 创作者访谈\\n• 下载/收藏功能\\n• 评论区')}
renderShowroom('all');
</script>''')

# ======================================================================
# 3. voice.html — 语音合成
# ======================================================================
write_page('voice.html', DH_HEAD.format(title='语音合成工坊 · AI声库', theme='mint-academy') + '''
<style>
.page-container{position:relative;z-index:1;padding-top:80px;max-width:1200px;margin:0 auto}
.hero{text-align:center;padding:40px 20px}
.hero h1{font-size:2.4rem;font-weight:900;background:linear-gradient(135deg,#14b8a6,#06b6d4,#6366f1);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero p{color:var(--text-secondary);margin-top:6px;max-width:600px;margin-left:auto;margin-right:auto}
.voice-layout{display:flex;gap:20px;padding:0 20px 40px}
.voice-main{flex:1;display:flex;flex-direction:column;gap:16px}
.vm-card{background:var(--bg-card);border:1px solid var(--border);border-radius:18px;padding:24px}
.vm-card h3{font-size:.95rem;margin-bottom:14px}
.text-input{width:100%;min-height:120px;background:var(--bg-secondary);border:2px solid var(--border);border-radius:14px;padding:16px;color:var(--text);font-size:.9rem;resize:vertical;outline:none;font-family:inherit;transition:border-color .3s}
.text-input:focus{border-color:var(--accent)}
.voice-selector{display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:10px}
.vs-item{padding:14px 10px;border:2px solid var(--border);border-radius:12px;text-align:center;cursor:pointer;transition:all .3s;font-size:.78rem}
.vs-item:hover,.vs-item.active{border-color:var(--accent);background:rgba(20,184,166,.08)}
.vs-item .vs-avatar{font-size:2rem;display:block;margin-bottom:4px}
.vs-item .vs-name{font-weight:600}
.vs-item .vs-lang{font-size:.68rem;color:var(--text-dim)}
.param-row{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.param-item label{display:flex;justify-content:space-between;font-size:.75rem;color:var(--text-secondary);margin-bottom:6px}
.param-item input[type=range]{width:100%;accent-color:var(--accent)}
.action-row{display:flex;gap:12px}
.action-btn{flex:1;padding:14px;border:none;border-radius:14px;font-weight:700;cursor:pointer;font-size:.95rem;transition:all .3s}
.action-btn.primary{background:linear-gradient(135deg,#14b8a6,#06b6d4);color:#fff}
.action-btn.primary:hover{box-shadow:0 6px 24px rgba(20,184,166,.4);transform:translateY(-2px)}
.action-btn.secondary{border:2px solid var(--border);background:none;color:var(--text-secondary)}
.action-btn.secondary:hover{border-color:var(--accent)}
.voice-side{width:340px}
.output-area{background:var(--bg-card);border:1px solid var(--border);border-radius:18px;padding:24px;text-align:center;min-height:200px;display:flex;flex-direction:column;align-items:center;justify-content:center}
.output-area .oa-wave{font-size:4rem;animation:wavePulse 1s ease-in-out infinite}
@keyframes wavePulse{0%,100%{transform:scaleY(1)}50%{transform:scaleY(1.3)}}
.output-info{font-size:.82rem;color:var(--text-secondary);margin-top:10px}
.specs-section{padding:0 20px 40px;max-width:1100px;margin:0 auto}
.specs-section h2{font-size:1.3rem;margin-bottom:14px}
.specs-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.spec-card{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:20px;text-align:center}
.spec-card .sc-val{font-size:1.6rem;font-weight:900;color:var(--accent)}
.spec-card .sc-label{font-size:.78rem;color:var(--text-dim);margin-top:4px}
@media(max-width:768px){.voice-layout{flex-direction:column}.voice-side{width:100%}.param-row,.specs-grid{grid-template-columns:repeat(2,1fr)}.hero h1{font-size:1.8rem}}
</style>
</head>
<body>
<div id="nav-placeholder"></div>
<div class="page-container">
  <div class="hero"><h1>🎙️ 语音合成工坊 — AI声库</h1><p>将文字转化为自然流畅的人声。支持50+语言、200+声音风格、情感调节、语速控制——给你的数字人赋予灵魂之声。</p></div>
  <div class="voice-layout">
    <div class="voice-main">
      <div class="vm-card"><h3>📝 输入文本</h3><textarea class="text-input" id="textInput" placeholder="请输入要合成的文本...&#10;&#10;支持SSML标记语言：&#10;<break time="500ms"/>  = 暂停500毫秒&#10;<prosody rate="fast" pitch="high">文本</prosody> = 快速高音&#10;&#10;示例：大家好<break time="300ms"/>，欢迎来到龙奕学院语音合成工坊！">大家好，欢迎来到龙奕学院语音合成工坊！我是你的AI语音助手，今天将为你展示先进的语音合成技术。</textarea></div>
      <div class="vm-card"><h3>🎤 选择声音</h3><div class="voice-selector" id="voiceSelector"></div></div>
      <div class="vm-card"><h3>⚙️ 参数调节</h3><div class="param-row"><div class="param-item"><label><span>语速</span><span id="pv1">1.0x</span></label><input type="range" min="0.5" max="2" step="0.1" value="1" oninput="updateParam('pv1',this.value+'x')"></div><div class="param-item"><label><span>音调</span><span id="pv2">0</span></label><input type="range" min="-12" max="12" value="0" oninput="updateParam('pv2',this.value)"></div><div class="param-item"><label><span>情感强度</span><span id="pv3">50%</span></label><input type="range" min="0" max="100" value="50" oninput="updateParam('pv3',this.value+'%')"></div></div></div>
      <div class="action-row"><button class="action-btn primary" onclick="synthesize()">🎵 生成语音</button><button class="action-btn secondary" onclick="previewVoice()">▶️ 试听</button><button class="action-btn secondary" onclick="downloadAudio()">⬇️ 下载</button></div>
    </div>
    <div class="voice-side"><div class="output-area" id="outputArea"><div class="oa-wave">🎵</div><div class="output-info">点击「生成语音」开始合成</div></div></div>
  </div>
  <div class="specs-section"><h2>🔬 技术能力</h2><div class="specs-grid"><div class="spec-card"><div class="sc-val">50+</div><div class="sc-label">支持语言</div></div><div class="spec-card"><div class="sc-val">200+</div><div class="sc-label">声音风格</div></div><div class="spec-card"><div class="sc-val">24kHz</div><div class="sc-label">采样率</div></div><div class="spec-card"><div class="sc-val"><100ms</div><div class="sc-label">合成延迟</div></div><div class="spec-card"><div class="sc-val">SSML</div><div class="sc-label">标记语言</div></div><div class="spec-card"><div class="sc-val">7种</div><div class="sc-label">情感模式</div></div><div class="spec-card"><div class="sc-val">流式</div><div class="sc-label">实时输出</div></div><div class="spec-card"><div class="sc-val">VITS2</div><div class="sc-label">底层模型</div></div></div></div>
</div>
''' + DH_FOOT + '''
<script>
const voices=[{name:'琉璃',lang:'日/中/英',avatar:'🌌',style:'少女·元气',id:'jp-f01'},{name:'虚空龙',lang:'中/英',avatar:'🐉',style:'御姐·威严',id:'cn-f02'},{name:'少年A',lang:'日/中',avatar:'⭐',style:'少年·热血',id:'jp-m01'},{name:'公主',lang:'中/日/英',avatar:'👸',style:'少女·优雅',id:'cn-f01'},{name:'喵酱',lang:'中/日',avatar:'🐱',style:'萝莉·可爱',id:'cn-f03'},{name:'大叔',lang:'中',avatar:'🧔',style:'成熟·磁性',id:'cn-m01'},{name:'AI管家',lang:'中/英',avatar:'🤖',style:'中性·专业',id:'ai-01'},{name:'精灵',lang:'中/英/法',avatar:'🧝',style:'空灵·梦幻',id:'fantasy-01'}];
document.getElementById('voiceSelector').innerHTML=voices.map((v,i)=>'<div class="vs-item'+(i===0?' active':'')+'" onclick="selectVoice(\''+v.id+'\',this)" data-voice="'+v.id+'"><span class="vs-avatar">'+v.avatar+'</span><span class="vs-name">'+v.name+'</span><span class="vs-lang">'+v.lang+' · '+v.style+'</span></div>').join('');
let selectedVoice='jp-f01';
function selectVoice(id,btn){selectedVoice=id;document.querySelectorAll('.vs-item').forEach(b=>b.classList.remove('active'));btn.classList.add('active')}
function updateParam(id,val){document.getElementById(id).textContent=val}
function synthesize(){const text=document.getElementById('textInput').value;if(!text.trim()){alert('请先输入要合成的文本！');return}const area=document.getElementById('outputArea');const voice=voices.find(v=>v.id===selectedVoice);area.innerHTML='<div class="oa-wave">⏳</div><div class="output-info">正在合成...<br>声音: '+voice.name+' ('+voice.style+')<br>文本长度: '+text.length+'字</div>';setTimeout(()=>{area.innerHTML='<div class="oa-wave">✅</div><div class="output-info">合成完成！<br>声音: '+voice.name+'<br>时长: ~'+Math.ceil(text.length/3)+'秒<br><span style="color:var(--accent);cursor:pointer" onclick="previewVoice()">▶️ 点击播放</span></div>'},1500)}
function previewVoice(){alert('▶️ 语音预览\\n\\n当前为模拟演示。实际部署后将播放真实的AI合成语音。\\n\\n技术栈: VITS2 + HiFi-GAN\\n支持流式输出，首字延迟<100ms')}
function downloadAudio(){alert('⬇️ 下载语音文件\\n\\n格式: WAV 24kHz / MP3 320kbps\\n\\n文件将通过浏览器下载。\\n\\n(当前为模拟演示)')}
</script>''')

# ======================================================================
# 4. livecast.html — 虚拟直播
# ======================================================================
write_page('livecast.html', DH_HEAD.format(title='虚拟直播控制台', theme='coral-academy') + '''
<style>
.page-container{position:relative;z-index:1;padding-top:80px;max-width:1300px;margin:0 auto}
.hero{text-align:center;padding:40px 20px}
.hero h1{font-size:2.4rem;font-weight:900;background:linear-gradient(135deg,#f97316,#ec4899,#6366f1);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero p{color:var(--text-secondary);margin-top:6px;max-width:600px;margin-left:auto;margin-right:auto}
.live-layout{display:flex;gap:20px;padding:0 20px 40px}
.live-preview{flex:1;background:#0a0a0a;border-radius:20px;min-height:450px;position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center}
.live-preview .lp-screen{font-size:6rem;animation:liveFloat 3s ease-in-out infinite}
@keyframes liveFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}
.live-preview .lp-live-badge{position:absolute;top:16px;left:16px;background:#ef4444;color:#fff;padding:6px 14px;border-radius:12px;font-size:.75rem;font-weight:700;animation:livePulse 2s infinite}
@keyframes livePulse{0%,100%{opacity:1}50%{opacity:.6}}
.live-preview .lp-viewers{position:absolute;top:16px;right:16px;background:rgba(0,0,0,.7);color:#fff;padding:6px 14px;border-radius:12px;font-size:.75rem}
.live-chat{width:320px;background:var(--bg-card);border:1px solid var(--border);border-radius:20px;display:flex;flex-direction:column;overflow:hidden}
.live-chat .lc-header{padding:16px;border-bottom:1px solid var(--border);font-weight:700}
.live-chat .lc-messages{flex:1;overflow-y:auto;padding:12px;display:flex;flex-direction:column;gap:8px;max-height:350px}
.lc-msg{display:flex;gap:8px;font-size:.78rem;animation:msgIn .3s ease-out}
@keyframes msgIn{from{opacity:0;transform:translateX(20px)}to{opacity:1;transform:translateX(0)}}
.lc-msg .lcm-user{color:var(--accent);font-weight:600;flex-shrink:0}
.lc-msg .lcm-text{color:var(--text-secondary)}
.lc-msg.superchat{background:linear-gradient(135deg,rgba(249,115,22,.1),rgba(236,72,153,.1));border-radius:8px;padding:8px}
.live-controls{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px;padding:0 20px 40px}
.lc-card{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:20px;text-align:center;cursor:pointer;transition:all .3s}
.lc-card:hover{transform:translateY(-3px);box-shadow:0 8px 28px rgba(249,115,22,.15)}
.lc-card .lcc-icon{font-size:2.5rem;margin-bottom:8px}
.lc-card .lcc-name{font-weight:700;font-size:.9rem}
.lc-card .lcc-desc{font-size:.75rem;color:var(--text-dim);margin-top:4px}
@media(max-width:768px){.live-layout{flex-direction:column}.live-chat{width:100%}.live-controls{grid-template-columns:repeat(2,1fr)}.hero h1{font-size:1.8rem}}
</style>
</head>
<body>
<div id="nav-placeholder"></div>
<div class="page-container">
  <div class="hero"><h1>📺 虚拟直播控制台</h1><p>一站式虚拟直播解决方案：面部捕捉驱动数字人、实时弹幕互动、AI智能回复、礼物特效触发、多平台推流。</p></div>
  <div class="live-layout">
    <div class="live-preview"><span class="lp-screen">🦊</span><span class="lp-live-badge">🔴 LIVE</span><span class="lp-viewers">👁️ 1,247 观看</span></div>
    <div class="live-chat"><div class="lc-header">💬 实时弹幕</div><div class="lc-messages" id="chatMessages"></div><div style="padding:12px;border-top:1px solid var(--border);display:flex;gap:8px"><input type="text" id="chatInput" placeholder="发送弹幕..." style="flex:1;padding:10px;border:1px solid var(--border);border-radius:10px;background:var(--bg-secondary);color:var(--text);outline:none;font-size:.82rem" onkeydown="if(event.key==='Enter')sendChat()"><button onclick="sendChat()" style="padding:10px 14px;background:var(--accent);border:none;border-radius:10px;color:#fff;cursor:pointer">发送</button></div></div>
  </div>
  <div class="live-controls"><div class="lc-card" onclick="alert('🎭 面部捕捉\\n\\n支持: Webcam / iPhone ARKit / Leap Motion\\n延迟: <50ms\\n追踪点: 52个BlendShape\\n\\n自动映射到你的数字人模型')"><span class="lcc-icon">🎭</span><div class="lcc-name">面部捕捉</div><div class="lcc-desc">52 BlendShape实时驱动</div></div><div class="lc-card" onclick="alert('🎵 背景音乐\\n\\n内置1000+版权免费BGM\\n支持本地导入\\n可设置播放列表和淡入淡出')"><span class="lcc-icon">🎵</span><div class="lcc-name">BGM控制</div><div class="lcc-desc">1000+版权免费曲库</div></div><div class="lc-card" onclick="alert('🎁 礼物特效\\n\\n粉丝送礼自动触发对应特效:\\n• 小花 → 数字人微笑\\n• 火箭 → 特效爆炸\\n• 守护 → 专属动画')"><span class="lcc-icon">🎁</span><div class="lcc-name">礼物特效</div><div class="lcc-desc">送礼触发数字人反应</div></div><div class="lc-card" onclick="alert('📡 多平台推流\\n\\n同时推流至:\\n• B站 / 抖音 / YouTube\\n• Twitch / 龙奕学院\\n\\n统一弹幕聚合显示')"><span class="lcc-icon">📡</span><div class="lcc-name">多平台推流</div><div class="lcc-desc">一键推流至5+平台</div></div><div class="lc-card" onclick="alert('🤖 AI自动回复\\n\\n基于ChatGPT的智能弹幕回复\\n自动识别问题类型并生成回答\\n可定制回复风格和黑名单词')"><span class="lcc-icon">🤖</span><div class="lcc-name">AI智能回复</div><div class="lcc-desc">自动应答常见弹幕</div></div><div class="lc-card" onclick="alert('📊 直播数据\\n\\n实时显示:\\n• 观看人数/峰值\\n• 弹幕数量/频率\\n• 礼物收入\\n• 观众地域分布')"><span class="lcc-icon">📊</span><div class="lcc-name">实时数据</div><div class="lcc-desc">直播数据大屏</div></div></div>
</div>
''' + DH_FOOT + '''
<script>
const sampleChats=[{u:'二次元星人',t:'琉璃酱今天也好可爱！',sc:false},{u:'虚空旅者',t:'能唱一首《 unravel》吗？',sc:false},{u:'超级舰长·龙',t:'永远支持琉璃！来自龙墟世界的爱 ❤️',sc:true},{u:'新来的小透明',t:'第一次看虚拟直播，好厉害！',sc:false},{u:'技术宅',t:'问一下这个面部捕捉用的是什么方案？',sc:false},{u:'喵星人',t:'喵喵喵喵喵！',sc:false}];
const chatEl=document.getElementById('chatMessages');
function addMsg(user,text,sc){const d=document.createElement('div');d.className='lc-msg'+(sc?' superchat':'');d.innerHTML='<span class="lcm-user">'+user+':</span><span class="lcm-text">'+text+'</span>';chatEl.appendChild(d);chatEl.scrollTop=chatEl.scrollHeight}
sampleChats.forEach(c=>addMsg(c.u,c.t,c.sc));
function sendChat(){const input=document.getElementById('chatInput');const text=input.value.trim();if(text){addMsg('你',text,false);input.value='';setTimeout(()=>{const replies=['谢谢支持！','哈哈哈~','欢迎新朋友！','这个问题问得好！','让我想想...','ありがとう！','比心 ♥'];addMsg('🦊 琉璃',replies[Math.floor(Math.random()*replies.length)],Math.random()>.7)},800+Math.random()*1200)}
}
</script>''')

# ======================================================================
# 5. animate.html — 动画实验室
# ======================================================================
write_page('animate.html', DH_HEAD.format(title='动画实验室 · 动作编排', theme='lavender-academy') + '''
<style>
.page-container{position:relative;z-index:1;padding-top:80px;max-width:1200px;margin:0 auto}
.hero{text-align:center;padding:40px 20px}
.hero h1{font-size:2.4rem;font-weight:900;background:linear-gradient(135deg,#a78bfa,#7c3aed,#6366f1);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero p{color:var(--text-secondary);margin-top:6px;max-width:600px;margin-left:auto;margin-right:auto}
.anim-layout{display:flex;gap:20px;padding:0 20px 30px}
.anim-preview{flex:1;background:var(--bg-card);border:1px solid var(--border);border-radius:20px;min-height:400px;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden}
.anim-figure{font-size:8rem;transition:transform .5s,filter .5s}
.anim-figure.walking{animation:figWalk .6s ease-in-out infinite}
.anim-figure.dancing{animation:figDance .4s ease-in-out infinite}
.anim-figure.idle{animation:figIdle 2s ease-in-out infinite}
.anim-timeline{position:absolute;bottom:0;left:0;right:0;background:rgba(0,0,0,.8);padding:16px;display:flex;align-items:center;gap:8px}
.timeline-track{flex:1;height:40px;background:rgba(255,255,255,.1);border-radius:6px;position:relative}
.timeline-playhead{position:absolute;top:-4px;width:2px;height:48px;background:var(--accent);border-radius:2px;left:30%}
.anim-sidebar{width:340px;display:flex;flex-direction:column;gap:14px}
.as-card{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:18px}
.as-card h3{font-size:.88rem;margin-bottom:12px}
.anim-presets{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.ap-item{padding:14px 8px;border:2px solid var(--border);border-radius:12px;text-align:center;cursor:pointer;font-size:.75rem;transition:all .3s}
.ap-item:hover,.ap-item.active{border-color:var(--accent);background:rgba(167,139,250,.08)}
.ap-item .api-icon{font-size:1.5rem;display:block;margin-bottom:4px}
.anim-mixer{display:flex;flex-direction:column;gap:10px}
.mixer-row{display:flex;align-items:center;gap:8px}
.mixer-row label{font-size:.75rem;color:var(--text-secondary);width:60px;flex-shrink:0}
.mixer-row input[type=range]{flex:1;accent-color:var(--accent)}
.specs-section{padding:0 20px 40px;max-width:1100px;margin:0 auto}
.specs-section h2{font-size:1.3rem;margin-bottom:14px}
.specs-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.spec-card{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:20px;text-align:center}
.spec-card .sc-val{font-size:1.6rem;font-weight:900;color:var(--accent)}
.spec-card .sc-label{font-size:.78rem;color:var(--text-dim);margin-top:4px}
@media(max-width:768px){.anim-layout{flex-direction:column}.anim-sidebar{width:100%}.specs-grid{grid-template-columns:repeat(2,1fr)}.hero h1{font-size:1.8rem}}
</style>
</head>
<body>
<div id="nav-placeholder"></div>
<div class="page-container">
  <div class="hero"><h1>🎬 动画实验室 — 动作编排</h1><p>AI驱动的动画创作平台。200+预设动作、骨骼动画混合器、物理模拟、文本描述生成动画——让你的数字人动起来。</p></div>
  <div class="anim-layout">
    <div class="anim-preview"><span class="anim-figure idle" id="animFigure">🦊</span><div class="anim-timeline"><button style="background:none;border:none;color:#fff;cursor:pointer;font-size:1.2rem" onclick="togglePlay()">▶️</button><div class="timeline-track"><div class="timeline-playhead" id="playhead"></div></div><span style="color:#fff;font-size:.72rem">00:00 / 00:05</span></div></div>
    <div class="anim-sidebar">
      <div class="as-card"><h3>🎭 动作预设</h3><div class="anim-presets"><div class="ap-item active" onclick="setAnim('idle',this)"><span class="api-icon">🧍</span>待机</div><div class="ap-item" onclick="setAnim('walking',this)"><span class="api-icon">🚶</span>行走</div><div class="ap-item" onclick="setAnim('running',this)"><span class="api-icon">🏃</span>奔跑</div><div class="ap-item" onclick="setAnim('jumping',this)"><span class="api-icon">🤸</span>跳跃</div><div class="ap-item" onclick="setAnim('dancing',this)"><span class="api-icon">💃</span>舞蹈</div><div class="ap-item" onclick="setAnim('bowing',this)"><span class="api-icon">🙇</span>鞠躬</div><div class="ap-item" onclick="setAnim('waving',this)"><span class="api-icon">👋</span>挥手</div><div class="ap-item" onclick="setAnim('sitting',this)"><span class="api-icon">🪑</span>坐下</div><div class="ap-item" onclick="setAnim('fighting',this)"><span class="api-icon">⚔️</span>战斗</div></div></div>
      <div class="as-card"><h3>⚙️ 动画混合器</h3><div class="anim-mixer"><div class="mixer-row"><label>上半身</label><input type="range" min="0" max="100" value="50"><span style="font-size:.72rem;color:var(--text-dim)">50%</span></div><div class="mixer-row"><label>下半身</label><input type="range" min="0" max="100" value="50"><span style="font-size:.72rem;color:var(--text-dim)">50%</span></div><div class="mixer-row"><label>过渡</label><input type="range" min="0" max="100" value="30"><span style="font-size:.72rem;color:var(--text-dim)">0.3s</span></div></div></div>
      <div class="as-card"><h3>🤖 AI文本生成动画</h3><input type="text" placeholder="描述动作，如：开心地跳起来转圈" style="width:100%;padding:10px;border:1px solid var(--border);border-radius:10px;background:var(--bg-secondary);color:var(--text);outline:none;font-size:.82rem;margin-bottom:8px"><button class="btn-primary" style="width:100%" onclick="aiGenerateAnim()">✨ AI生成动画</button></div>
    </div>
  </div>
  <div class="specs-section"><h2>🔬 技术能力</h2><div class="specs-grid"><div class="spec-card"><div class="sc-val">200+</div><div class="sc-label">预设动作</div></div><div class="spec-card"><div class="sc-val">60fps</div><div class="sc-label">动画帧率</div></div><div class="spec-card"><div class="sc-val">IK/FK</div><div class="sc-label">双模式</div></div><div class="spec-card"><div class="sc-val">物理</div><div class="sc-label">布料/头发模拟</div></div></div></div>
</div>
''' + DH_FOOT + '''
<script>
const fig=document.getElementById('animFigure');
const anims={idle:'idle',walking:'walking',running:'walking',jumping:'jumping',dancing:'dancing',bowing:'bowing',waving:'waving',sitting:'sitting',fighting:'fighting'};
function setAnim(name,btn){document.querySelectorAll('.ap-item').forEach(b=>b.classList.remove('active'));btn.classList.add('active');fig.className='anim-figure '+name;const icons={idle:'🦊',walking:'🚶',running:'🏃',jumping:'🙆',dancing:'💃',bowing:'🙇',waving:'👋',sitting:'🦊',fighting:'⚔️'};fig.textContent=icons[name]||'🦊'}
function togglePlay(){alert('▶️ 播放动画\\n\\n当前动画已开始循环播放。\\n在完整版本中，此功能将驱动3D骨骼动画的实时预览。')}
function aiGenerateAnim(){alert('🤖 AI动画生成\\n\\n输入文本描述后，AI将:\\n1. 解析动作语义\\n2. 匹配动画数据库\\n3. 生成关键帧序列\\n4. 应用物理模拟\\n5. 输出动画曲线\\n\\n(演示模式 — 完整版本将集成AnimateDiff模型)')}
</script>''')

# ======================================================================
# 6. motion.html — 动作捕捉
# ======================================================================
write_page('motion.html', DH_HEAD.format(title='动作捕捉系统 · MoCap', theme='sky-academy') + '''
<style>
.page-container{position:relative;z-index:1;padding-top:80px;max-width:1200px;margin:0 auto}
.hero{text-align:center;padding:40px 20px}
.hero h1{font-size:2.4rem;font-weight:900;background:linear-gradient(135deg,#3b82f6,#06b6d4,#6366f1);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero p{color:var(--text-secondary);margin-top:6px;max-width:650px;margin-left:auto;margin-right:auto}
.mocap-layout{display:flex;gap:20px;padding:0 20px 30px}
.mocap-preview{flex:1;background:#0a0a0a;border-radius:20px;min-height:420px;display:flex;flex-direction:column;align-items:center;justify-content:center;position:relative;overflow:hidden}
.mocap-skeleton{position:relative;width:120px;height:300px}
.mocap-skeleton .bone{position:absolute;background:rgba(59,130,246,.6);border-radius:2px;transform-origin:left center}
.bone-head{width:30px;height:30px;border-radius:50%;background:var(--accent);top:0;left:45px;animation:headBob 2s ease-in-out infinite}
.bone-spine{width:3px;height:80px;top:30px;left:58px}
.bone-larm{width:3px;height:60px;top:40px;left:58px;transform:rotate(-30deg)}
.bone-rarm{width:3px;height:60px;top:40px;left:58px;transform:rotate(30deg)}
.bone-lleg{width:3px;height:80px;top:110px;left:58px;transform:rotate(-5deg)}
.bone-rleg{width:3px;height:80px;top:110px;left:58px;transform:rotate(5deg)}
@keyframes headBob{0%,100%{transform:translateY(0)}50%{transform:translateY(-3px)}}
.mocap-status{color:#22c55e;font-size:.82rem;margin-top:12px;display:flex;align-items:center;gap:8px}
.status-dot{width:8px;height:8px;background:#22c55e;border-radius:50%;animation:statusPulse 2s infinite}
@keyframes statusPulse{0%,100%{opacity:1}50%{opacity:.3}}
.mocap-sidebar{width:340px;display:flex;flex-direction:column;gap:14px}
.ms-card{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:18px}
.ms-card h3{font-size:.88rem;margin-bottom:12px}
.device-options{display:flex;flex-direction:column;gap:8px}
.device-option{padding:14px;border:2px solid var(--border);border-radius:12px;cursor:pointer;transition:all .3s;display:flex;align-items:center;gap:12px}
.device-option:hover,.device-option.active{border-color:var(--accent);background:rgba(59,130,246,.05)}
.device-option .do-icon{font-size:1.8rem}
.device-option .do-info{flex:1}
.device-option .do-name{font-weight:600;font-size:.85rem}
.device-option .do-desc{font-size:.72rem;color:var(--text-dim)}
.accuracy-meter{margin-top:8px}
.accuracy-bar{height:6px;background:var(--bg-secondary);border-radius:3px;overflow:hidden;margin-top:4px}
.accuracy-fill{height:100%;background:var(--accent);border-radius:3px;transition:width .5s}
.recording-controls{display:flex;gap:10px}
.rec-btn{flex:1;padding:12px;border:none;border-radius:12px;font-weight:700;cursor:pointer;font-size:.85rem;transition:all .3s}
.rec-btn.start{background:#ef4444;color:#fff}.rec-btn.start:hover{box-shadow:0 4px 16px rgba(239,68,68,.4)}
.rec-btn.stop{background:var(--bg-secondary);color:var(--text);border:1px solid var(--border)}
.rec-btn.export{background:var(--accent);color:#fff}
@media(max-width:768px){.mocap-layout{flex-direction:column}.mocap-sidebar{width:100%}.hero h1{font-size:1.8rem}}
</style>
</head>
<body>
<div id="nav-placeholder"></div>
<div class="page-container">
  <div class="hero"><h1>🎯 动作捕捉系统 · MoCap</h1><p>将真实世界的动作转化为数字人的流畅动画。支持Webcam、iPhone ARKit、专业MoCap设备三种方案，无需昂贵硬件即可开始。</p></div>
  <div class="mocap-layout">
    <div class="mocap-preview"><div class="mocap-skeleton"><div class="bone bone-head"></div><div class="bone bone-spine"></div><div class="bone bone-larm"></div><div class="bone bone-rarm"></div><div class="bone bone-lleg"></div><div class="bone bone-rleg"></div></div><div class="mocap-status"><span class="status-dot"></span> 待机中 — 选择设备开始捕捉</div></div>
    <div class="mocap-sidebar">
      <div class="ms-card"><h3>📷 捕捉设备</h3><div class="device-options"><div class="device-option active" onclick="selectDevice('webcam',this)"><span class="do-icon">📷</span><div class="do-info"><div class="do-name">Webcam (MediaPipe)</div><div class="do-desc">30fps · 33个关键点 · 免费</div></div></div><div class="device-option" onclick="selectDevice('arkit',this)"><span class="do-icon">📱</span><div class="do-info"><div class="do-name">iPhone ARKit</div><div class="do-desc">60fps · 52 BlendShape · 高精度</div></div></div><div class="device-option" onclick="selectDevice('mocap',this)"><span class="do-icon">🎯</span><div class="do-info"><div class="do-name">专业MoCap套装</div><div class="do-desc">120fps · 全身追踪 · 毫米级</div></div></div></div><div class="accuracy-meter" style="margin-top:12px"><span style="font-size:.75rem;color:var(--text-dim)">捕捉精度</span><div class="accuracy-bar"><div class="accuracy-fill" id="accuracyFill" style="width:70%"></div></div></div></div>
      <div class="ms-card"><h3>🎬 录制控制</h3><div class="recording-controls"><button class="rec-btn start" onclick="startRecording()">🔴 开始录制</button><button class="rec-btn stop" onclick="stopRecording()">⏹️ 停止</button></div><div class="recording-controls" style="margin-top:8px"><button class="rec-btn export" onclick="exportRecording()">📤 导出动画</button></div></div>
      <div class="ms-card"><h3>📊 数据预览</h3><div style="display:grid;grid-template-columns:repeat(2,1fr);gap:10px"><div style="text-align:center;padding:10px;background:var(--bg-secondary);border-radius:10px"><div style="font-size:1.3rem;font-weight:900;color:var(--accent)">0</div><div style="font-size:.7rem;color:var(--text-dim)">录制帧数</div></div><div style="text-align:center;padding:10px;background:var(--bg-secondary);border-radius:10px"><div style="font-size:1.3rem;font-weight:900;color:#22c55e">0ms</div><div style="font-size:.7rem;color:var(--text-dim)">延迟</div></div></div></div>
    </div>
  </div>
  <div style="padding:0 20px 40px;max-width:1100px;margin:0 auto"><h2 style="font-size:1.3rem;margin-bottom:14px">🔬 技术规格</h2><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px"><div class="spec-card"><div class="sc-val">52</div><div class="sc-label">面部BlendShape</div></div><div class="spec-card"><div class="sc-val">33/65</div><div class="sc-label">身体关键点</div></div><div class="spec-card"><div class="sc-val"><50ms</div><div class="sc-label">端到端延迟</div></div><div class="spec-card"><div class="sc-val">FK/IK</div><div class="sc-label">骨骼解算</div></div></div></div>
</div>
''' + DH_FOOT + '''
<script>
let currentDevice='webcam',isRecording=false,frameCount=0;
function selectDevice(dev,btn){currentDevice=dev;document.querySelectorAll('.device-option').forEach(b=>b.classList.remove('active'));btn.classList.add('active');document.getElementById('accuracyFill').style.width=(dev==='webcam'?'70%':dev==='arkit'?'92%':'98%')}
function startRecording(){if(isRecording)return;isRecording=true;document.querySelector('.mocap-status').innerHTML='<span class="status-dot" style="animation:statusPulse .5s infinite"></span> 🔴 录制中...';const iv=setInterval(()=>{frameCount++;if(!isRecording){clearInterval(iv);document.querySelector('.mocap-status').innerHTML='<span class="status-dot"></span> 录制停止 · 共 '+frameCount+' 帧'}},33)}
function stopRecording(){isRecording=false}
function exportRecording(){const fmts=['FBX (Unreal)','BVH (通用)','Anim (Unity)','VRM Animation'];alert('📤 导出动作捕捉数据\\n\\n格式: '+fmts[Math.floor(Math.random()*fmts.length)]+'\\n帧数: '+frameCount+'\\n设备: '+currentDevice+'\\n\\n(当前为演示模式)')}
</script>''')

print('\n=== Digital-Human Pages: Batch 1 done (studio, showroom, voice, livecast, animate, motion) ===')

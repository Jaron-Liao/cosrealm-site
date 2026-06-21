const fs = require('fs');
const { execSync } = require('child_process');

const BASE = 'https://dce5d6e6af3d4530be2051ec56d3b7f5.app.codebuddy.work';
const ROOT = __dirname;

// Auto-discover all HTML files
const files = execSync('find . -name "*.html" | grep -v index-backup | sed "s|^\\./||" | sort')
  .toString().trim().split('\n').filter(f => f && f !== 'sitemap.html');

// Category config: [cat, icon, title]
const CATS = {
  root:        { icon: '🏠', title: '根目录 · 核心入口' },
  anime:       { icon: '📺', title: '番剧学院' },
  social:      { icon: '💬', title: '羁绊学院' },
  shop:        { icon: '🛒', title: '商贸学院' },
  metaverse:   { icon: '🌌', title: '虚空学院' },
  creator:     { icon: '🎨', title: '创作学院' },
  'digital-human': { icon: '🤖', title: '幻影学院 · 数字人' },
  academy:     { icon: '🎓', title: '研修学院' },
  events:      { icon: '🎉', title: '祭典学院' },
  wiki:        { icon: '📚', title: '百科书院' },
  auth:        { icon: '🔐', title: '用户认证' },
  company:     { icon: '🏢', title: '关于龙奕' },
  help:        { icon: '❓', title: '帮助中心' },
  meta:        { icon: '⚙️', title: '元信息' },
  user:        { icon: '👤', title: '用户中心' },
  extra:       { icon: '🎨', title: '扩展页面' },
};

// Group files by category
const groups = {};
for (const f of files) {
  let cat = 'extra';
  if (!f.includes('/')) cat = 'root';
  else {
    const dir = f.split('/')[1]; // pages/XXX/...
    cat = dir;
  }
  if (!groups[cat]) groups[cat] = [];
  groups[cat].push(f);
}

// Pretty names for pages
function pageName(p) {
  const basename = p.replace('.html','').replace('pages/','').replace(/\/index$/,'');
  return basename.replace(/\//g,'/').replace(/-/g,' ');
}

// Build HTML
let html = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>龙墟 CosRealm · 全站地图</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Segoe UI',system-ui,sans-serif;background:#0a0a1a;color:#e0e0e0;min-height:100vh;position:relative}
body::before{content:'';position:fixed;top:0;left:0;width:100%;height:100%;background:radial-gradient(ellipse at 20% 50%,rgba(255,107,53,0.06) 0%,transparent 60%),radial-gradient(ellipse at 80% 50%,rgba(120,80,255,0.05) 0%,transparent 60%);pointer-events:none;z-index:0}
.container{position:relative;z-index:1;max-width:1200px;margin:0 auto;padding:40px 24px}
h1{text-align:center;font-size:2.2rem;background:linear-gradient(135deg,#FF6B35,#ff9a56);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:6px}
.subtitle{text-align:center;color:#888;margin-bottom:32px;font-size:0.95rem}
.stats{display:flex;justify-content:center;gap:28px;margin-bottom:36px;flex-wrap:wrap}
.stat-card{background:rgba(255,107,53,0.08);border:1px solid rgba(255,107,53,0.2);border-radius:14px;padding:18px 32px;text-align:center;backdrop-filter:blur(8px)}
.stat-card .num{font-size:2rem;font-weight:800;color:#FF6B35}
.stat-card .label{font-size:0.78rem;color:#999;margin-top:4px}
.filter-bar{display:flex;gap:8px;margin-bottom:32px;flex-wrap:wrap;justify-content:center;position:sticky;top:0;z-index:100;background:rgba(10,10,26,0.92);backdrop-filter:blur(12px);padding:12px 0;margin-left:-24px;margin-right:-24px;padding-left:24px;padding-right:24px}
.filter-btn{background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);color:#aaa;padding:7px 16px;border-radius:20px;cursor:pointer;font-size:0.8rem;transition:all 0.2s;white-space:nowrap}
.filter-btn:hover,.filter-btn.active{background:rgba(255,107,53,0.18);border-color:#FF6B35;color:#FF6B35}
.section{margin-bottom:40px}
.section-title{font-size:1.15rem;font-weight:700;color:#FF6B35;margin-bottom:14px;padding-bottom:10px;border-bottom:1px solid rgba(255,107,53,0.18);display:flex;align-items:center;gap:10px}
.section-title .count{background:rgba(255,107,53,0.13);color:#FF6B35;font-size:0.72rem;padding:3px 12px;border-radius:20px;margin-left:auto;font-weight:500}
.link-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:10px}
.link-item{background:rgba(255,255,255,0.025);border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:12px 16px;transition:all 0.2s;position:relative;overflow:hidden}
.link-item::before{content:'';position:absolute;top:0;left:0;width:3px;height:100%;background:linear-gradient(180deg,#FF6B35,#ff9a56);opacity:0;transition:opacity 0.2s}
.link-item:hover{background:rgba(255,107,53,0.06);border-color:rgba(255,107,53,0.25);transform:translateY(-1px)}
.link-item:hover::before{opacity:1}
.link-item a{color:#ccc;text-decoration:none;font-size:0.88rem;display:block}
.link-item a:hover{color:#FF6B35}
.link-item .page-name{color:#e8e8e8;font-weight:600;font-size:0.85rem;margin-bottom:3px}
.link-item .page-path{color:#555;font-size:0.7rem;word-break:break-all;font-family:monospace}
.footer{text-align:center;color:#555;font-size:0.8rem;margin-top:60px;padding-top:24px;border-top:1px solid rgba(255,255,255,0.05)}
.theme-btn{position:fixed;bottom:24px;right:24px;width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,#FF6B35,#e55a28);border:none;color:#fff;font-size:1.3rem;cursor:pointer;z-index:999;box-shadow:0 4px 20px rgba(255,107,53,0.35);transition:transform 0.2s}
.theme-btn:hover{transform:scale(1.1)}
.hidden{display:none!important}
@media(max-width:640px){.link-grid{grid-template-columns:1fr}.stats{gap:12px}.stat-card{padding:12px 20px}}
</style>
</head>
<body>
<div class="container">
  <h1>🏛️ 龙墟 CosRealm 全站地图</h1>
  <p class="subtitle">全部页面链接一览 · 点击任意卡片跳转 · 共 ${files.length} 个页面</p>
  <div class="stats">
    <div class="stat-card"><div class="num">${files.length}</div><div class="label">总页面数</div></div>
    <div class="stat-card"><div class="num">${Object.keys(groups).length}</div><div class="label">分类板块</div></div>
    <div class="stat-card"><div class="num">9</div><div class="label">学院栏目</div></div>
    <div class="stat-card"><div class="num">${groups['extra'] ? groups['extra'].length : 0}</div><div class="label">扩展页面</div></div>
  </div>
  <div class="filter-bar">
    <button class="filter-btn active" onclick="filterAll()">全部</button>
`;

// Add filter buttons for categories that have pages
const catOrder = ['root','anime','social','shop','metaverse','creator','digital-human','academy','events','wiki','auth','company','help','meta','user','extra'];
for (const cat of catOrder) {
  if (groups[cat]) {
    const cfg = CATS[cat] || { icon: '📄', title: cat };
    html += `    <button class="filter-btn" onclick="filter('${cat}')">${cfg.icon} ${cfg.title.replace(' · ','<br>')}</button>\n`;
  }
}

html += `  </div>\n`;

// Generate sections
for (const cat of catOrder) {
  if (!groups[cat]) continue;
  const cfg = CATS[cat] || { icon: '📄', title: cat };
  const pages = groups[cat];
  html += `  <div class="section" data-cat="${cat}">\n`;
  html += `    <div class="section-title"><span>${cfg.icon}</span> ${cfg.title} <span class="count">${pages.length}页</span></div>\n`;
  html += `    <div class="link-grid">\n`;
  for (const p of pages) {
    const display = p.replace('.html','').replace('pages/','').replace('index','首页');
    html += `      <div class="link-item"><a href="${BASE}/${p}" target="_blank"><div class="page-name">${display}</div><div class="page-path">${p}</div></a></div>\n`;
  }
  html += `    </div>\n  </div>\n`;
}

html += `  <div class="footer">
    <p>🐉 龙墟 CosRealm · 二次元Cosplay综合社区平台</p>
    <p style="margin-top:8px">全站地图自动生成 · ${new Date().toLocaleDateString('zh-CN')} · 共 ${files.length} 个页面</p>
  </div>
</div>
<button class="theme-btn" onclick="toggleTheme()" title="切换日/夜间模式">🌓</button>
<script>
function filter(cat){
  document.querySelectorAll('.section').forEach(s=>{
    s.classList.toggle('hidden', cat!=='all' && s.dataset.cat!==cat);
  });
  document.querySelectorAll('.filter-btn').forEach(b=>{
    b.classList.toggle('active', (cat==='all'&&b.textContent.trim()==='全部') || b.onclick?.toString().includes("'"+cat+"'"));
  });
}
function filterAll(){filter('all');}
function toggleTheme(){
  const root=document.documentElement;
  const d=root.classList.contains('theme-dark');
  root.classList.remove(d?'theme-dark':'theme-light');
  root.classList.add(d?'theme-light':'theme-dark');
  localStorage.setItem('cosrealm-theme',d?'light':'dark');
}
(function(){const s=localStorage.getItem('cosrealm-theme')||'dark';document.documentElement.classList.add('theme-'+s);})();
</script>
</body>
</html>`;

fs.writeFileSync('sitemap.html', html, 'utf8');
console.log(`✅ sitemap.html generated — ${files.length} pages, ${Object.keys(groups).length} categories`);

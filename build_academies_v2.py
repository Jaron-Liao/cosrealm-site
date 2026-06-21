#!/usr/bin/env python3
"""
龙奕学院 v4.1 — 9大学院首页生成器（极简版）
直接用字符串拼接，不使用f-string和format，避免所有转义问题
"""
import os

BASE = r"C:\Users\28767\Downloads\cosrealm-site"

def w(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  OK {os.path.basename(path)} ({len(content)} chars)")

# 读取CSS模板
with open(os.path.join(BASE, "assets", "style.css"), "r", encoding="utf-8") as _:
    pass  # just confirm exists

def gen(name, icon, d3d, theme, desc_html, stats_html, feats_html, news_html, sub_nav_html, extra_html=""):
    """Generate an academy homepage"""
    html = '<!DOCTYPE html>\n<html lang="zh-CN" data-3d="' + d3d + '">\n<head>\n'
    html += '<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    html += '<title>' + name + ' &mdash; LongYi Academy</title>\n'
    html += '<link rel="stylesheet" href="assets/style.css">\n'
    html += '<link rel="stylesheet" href="assets/themes/academy/' + theme + '">\n'
    html += '<link rel="stylesheet" href="assets/themes/dark-mode.css">\n'
    html += '<link rel="stylesheet" href="assets/effects-layer.css">\n'
    
    # Inline styles
    css = """
<style>
.hbox{background:linear-gradient(160deg,var(--accent,#6366f1)22 0%,#a78bfa18 50%,var(--accent,#6366f1)10 100%);
border-radius:24px;padding:48px 36px;margin-bottom:28px;position:relative;overflow:hidden;
border:1px solid rgba(255,255,255,0.08);}
.hbox::before{content:'';position:absolute;top:-40%;right:-20%;width:300px;height:300px;border-radius:50%;
background:var(--accent,#6366f1)30;filter:blur(80px);}
.hinner{position:relative;z-index:1;}
.htitle{font-size:2.4rem;font-weight:900;color:#fff;line-height:1.2;margin-bottom:8px;
background:linear-gradient(135deg,#fff,#c4b5fd);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.hdesc{font-size:1rem;color:rgba(255,255,255,0.75);max-width:560px;line-height:1.7;}
.sbar{display:flex;gap:16px;margin-bottom:28px;flex-wrap:wrap;}
.scard{flex:1;min-width:130px;padding:20px;border-radius:16px;text-align:center;
background:rgba(20,20,45,0.7);border:1px solid rgba(255,255,255,0.06);transition:all 0.3s;}
.scard:hover{transform:translateY(-3px);}
.stit{font-size:1.35rem;font-weight:800;color:#fff;margin-bottom:16px;display:flex;align-items:center;gap:8px;}
.fgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px;margin-bottom:28px;}
.fcard{padding:22px;border-radius:18px;background:rgba(20,20,45,0.65);
border:1px solid rgba(255,255,255,0.06);transition:all 0.3s;cursor:pointer;border-left:4px solid #6366f1;}
.fcard:hover{transform:translateY(-5px);box-shadow:0 12px 30px rgba(0,0,0,0.2);}
.twocol{display:flex;gap:20px;margin-bottom:28px;}
.colmain{flex:1;min-width:0;}.colside{width:340px;flex-shrink:0;}
.spanel{background:rgba(20,20,45,0.7);border-radius:18px;padding:20px;border:1px solid rgba(255,255,255,0.06);}
.qgrid{display:grid;grid-template-columns:repeat(auto-fill,minwidth(120px),1fr);gap:10px;margin-bottom:28px;}
.qentry{padding:16px 10px;border-radius:14px;text-align:center;background:rgba(20,20,45,0.55);
border:1px solid rgba(255,255,255,0.05);cursor:pointer;transition:all 0.25s;text-decoration:none;color:inherit;}
.qentry:hover{background:rgba(99,102,241,0.12);transform:translateY(-2px);}
.nlist{list-style:none;padding:0;margin:0;}
.nlist li{padding:10px 0;border-bottom:1px solid rgba(255,255,255,0.06);display:flex;align-items:center;justify-content:space-between;}
.nlist li strong{margin-left:8px;color:#e0e0f0;font-size:0.9rem;}
.ntime{color:#666;font-size:0.78rem;white-space:nowrap;}
.cdown{display:flex;gap:8px;justify-content:center;margin:16px 0;}
.cdu{background:rgba(99,102,241,0.15);border-radius:10px;padding:10px 14px;text-align:center;min-width:52px;}
.cdnum{font-size:1.5rem;font-weight:900;color:#fff;}.cdlab{font-size:0.68rem;color:#888;margin-top:2px;}
.twrap{overflow:hidden;border-radius:12px;background:rgba(20,20,45,0.5);margin-bottom:20px;}
.ttrack{display:flex;animation:tscrl 30s linear infinite;width:max-content;padding:8px 0;}
@keyframes tscrl{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.titem{padding:0 20px;white-space:nowrap;font-size:0.84rem;color:#a0a0c0;shrink:0;}
.chartph{height:180px;border-radius:14px;background:rgba(20,20,45,0.4);
display:flex;align-items:center;justify-content:center;color:#666;font-size:0.9rem;
border:1px dashed rgba(255,255,255,0.08);margin:14px 0;}
</style>
"""
    html += css + '</head>\n<body>\n'
    
    # Hero
    html += '<div class="hbox"><div class="hinner">\n<h1 class="htitle">' + icon + ' ' + name + '</h1>\n'
    html += '<p class="hdesc">' + desc_html + '</p>\n'
    html += '<div style="display:flex;gap:10px;margin-top:20px;flex-wrap:wrap;">\n'
    html += '<a href="#features" style="display:inline-block;padding:12px 28px;border-radius:14px;'
    html += 'background:linear-gradient(135deg,var(--accent,#6366f1),#8b5cf6);color:#fff;font-weight:700;text-decoration:none;font-size:0.95rm;">&#x63A2;&#x7D22;&rarr;</a>\n'
    html += '</div></div></div>\n\n'
    
    html += '<div style="max-width:1400px;margin:0 auto;padding:0 24px;">\n'
    
    # Stats
    html += '<div class="sbar">' + stats_html + '</div>\n'
    
    # Ticker
    html += '<div class="twrap"><div class="ttrack">' + news_html * 2 + '</div></div>\n'
    
    # Quick nav
    html += '<h2 class="stit">&#x1F3AF;&#x5FEB;&#x6377;&#x5165;&#x53E3;</h2>\n<div class="qgrid">' + sub_nav_html + '</div>\n'
    
    # Features
    html += '<h2 class="stit" id="features">&#x26A1;&#x6838;&#x5FC3;&#x529F;&#x80FD;</h2>\n<div class="fgrid">' + feats_html + '</div>\n'
    
    # Extra sections
    if extra_html:
        html += extra_html
    
    # Two column: news + side panel
    html += '<div class="twocol"><div class="colmain"><div class="spanel" style="height:100%;">\n'
    html += '<h3 class="stit">&#x1F4E2;&#x6700;&#x65B0;&#x52A8;&#x6001;</h3><ul class="nlist">' + news_html + '</ul>\n'
    html += '</div></div><div class="colside">\n'
    html += '<div class="spanel" style="margin-bottom:16px;"><h3 class="stit" style="font-size:1.05rem;">&#x23F0;&#x5012;&#x671F;&#x6D3B;&#x52A8;&#x5012;&#x8BA1;</h3>'
    html += '<div class="cdown" id="cbox"></div></div>\n'
    html += '<div class="spanel"><h3 class="stit" style="font-size:1.05rem;">&#x1F4C8;&#x70ED;&#x5EA6;&#x8D8B;&#x52BF;</h3>'
    html += '<div class="chartph" id="chartArea">&#x1F4CA;...</div></div>\n</div></div>\n'
    
    html += '</div>\n'  # end max-width
    
    # Scripts
    js = """
<script src="assets/three-engine.js"></script>
<script src="assets/nav.js"></script>
<script src="assets/theme-toggle.js"></script>
<script src="assets/effects-runtime.js"></script>
<script src="assets/dynamic-bg.js"></script>
<script>
document.querySelectorAll('.cdnum[data-target]').forEach(function(el){
  var t=+el.dataset.target,d=1500,s=performance.now();
  function st(n){var p=Math.min((n-s)/d,1);el.textContent=Math.floor(t*p).toLocaleString();if(p<1)requestAnimationFrame(st);}
  requestAnimationFrame(st);
});
(function(){var b=document.getElementById('cbox');if(!b)return;
  var th=new Date(Date.now()+7*86400000);
  function tk(){var df=Math.max(0,th-new Date());
    var d=Math.floor(df/86400000),h=Math.floor((df%86400000)/3600000),m=Math.floor((df%3600000)/60000),sec=Math.floor((df%60000)/1000);
    b.innerHTML='<div class="cdu"><div class="cdnum">'+d+'</div><div class="cdlab"></div></div>'
      +'<div class="cdu"><div class="cdnum">'+('0'+h).slice(-2)+'</div><div class="cdlab"></div></div>'
      +'<div class="cdu"><div class="cdnum">'+('0'+m).slice(-2)+'</div><div class="cdlab"></div></div>'
      +'<div class="cdu"><div class="cdnum">'+('0'+sec).slice(-2)+'</div><div class="cdlab"></div></div>';}
  tk();setInterval(tk,1000);
})();
</script>
"""
    html += js + '\n</body>\n</html>'
    return html


# ====== 数据定义 ======

def stat_item(icon, num, label):
    return ('<div class="scard"><div style="font-size:1.6rem;">' + icon + '</div>'
            + '<div class="cdnum" data-target="' + str(num) + '">0</div>'
            + '<div style="font-size:0.82rem;color:#888;">' + label + '</div></div>')

def feat_item(icon, title, desc, color='#6366f1'):
    return ('<div class="fcard" style="border-left-color:' + color + ';">'
            + '<div style="font-size:2rem;margin-bottom:8px;">' + icon + '</div>'
            + '<h3 style="font-size:1.05rem;color:#fff;font-weight:700;margin-bottom:6px;">' + title + '</h3>'
            + '<p style="font-size:0.85rem;color:#a0a0c0;line-height:1.6;">' + desc + '</p></div>')

def news_item(title, tag, time_str):
    colors_bg = ['rgba(99,102,241,0.15)','rgba(34,197,94,0.15)','rgba(245,158,11,0.15)','rgba(244,114,182,0.15)']
    colors_fg = ['#a5b4fc','#86efac','#fbbf24','#f472b6']
    idx = hash(title) % 4
    return ('<li><span style="flex:1;">'
            + '<span style="padding:2px 8px;border-radius:6px;font-size:0.72rem;font-weight:600;'
            + 'background:' + colors_bg[idx] + ';color:' + colors_fg[idx] + ';">' + tag + '</span>'
            + '<strong>' + title + '</strong></span>'
            + '<span class="ntime">' + time_str + '</span></li>')

def sub_item(name, url, icon):
    return ('<a href="' + url + '" class="qentry">'
            + '<span style="font-size:1.8rem;display:block;">' + icon + '</span>'
            + '<span style="font-size:0.82rem;color:#d0d0e8;font-weight:600;">' + name + '</span></a>')

# ticker item (shorter version)
def tick_item(title):
    return '<span class="titem">&#x1F525; ' + title + ' |</span>'

# ============================================================
# 生成全部9个学院首页
# ============================================================

academies = [
    {
        'file': os.path.join(BASE, 'anime.html'),
        'name': '&#x756A;&#x5267;&#x5B66;&#x9662;', 'icon': '&#x1F3AC;',
        'd3d': 'anime', 'theme': 'sakura-academy.css',
        'desc': '&#x8FFD;&#x756A;&#x3001;&#x770B;&#x756A;&#x3001;&#x804A;&#x756A;&#x7684;&#x4E00;&#x7AD9;&#x5F0F;&#x756A;&#x5267;&#x6BBF;&#x80CC;.&#x4ECE;&#x65B0;&#x756A;&#x901F;&#x9012;&#x5230;&#x7ECF;&#x5178;&#x56DE;&#x987E;&#xFF0C;&#x4ECE;MAD;&#x521B;&#x4F5C;&#x5230;&#x5F39;&#x5E55;&#x72C2;&#x6B22;&#x2014;&#x2014;&#x8FD9;&#x91CC;&#x662F;&#x4E8C;&#x6B21;&#x5143;&#x7231;&#x597D;&#x8005;&#x7684;&#x7EC8;&#x6781;&#x805A;&#x96C6;&#x5730;.&#x652F;&#x6301;1080P;&#x9AD8;&#x6E05;&#x64AD;&#x653E;&#x3001;&#x5B9E;&#x65F6;&#x5F39;&#x5E55;&#x3001;&#x667A;&#x80FD;&#x63A8;&#x8350;',
        'stats': [stat_item('&#x1F4FA;',12847,'&#x90E8;&#x756A;&#x5267;'), stat_item('&#x1F441;',2300000,&#x65E5;&#x5747;&#x64AD;&#x653E;'), stat_item('&#x1F4AC;',89000000,'&#x5F39;&#x5E55;&#x603B;&#x91CF;'), stat_item('&#x2B50;',49,'&#x7528;&#x6237;&#x8BC4;&#x5206;')],
        'feats': [
            feat_item('&#x1F525;','番剧大厅','全站番剧分类浏览，按季度/类型/标签筛选，智能个性化推荐引擎'),
            feat_item('&#x25B6;','动画播放器','1080P自适应播放器，支持弹幕发送/遮挡/A-B循环/播放速度调节'),
            feat_item('&#x1F4C5;','新番时间表','每季新番追踪，开播提醒，放送时间线可视化日历'),
            feat_item('&#x1F3C6;','番剧排行榜','实时热度榜、评分榜、追番人数榜、弹幕数榜多维度排名'),
            feat_item('&#x1F3AC;','MAD·AMV工坊','视频剪辑工具链，素材库，特效模板，一键渲染发布'),
            feat_item('&#x1F4DA;','动画图书馆','动画制作百科、声优数据库、制作公司档案、角色关系图谱'),
        ],
        'news': [
            news_item('2026年7月新番「星渊编年史」今日首播！','HOT','10分钟前'),
            news_item('MAD创作大赛第三季作品征集开始','NEW','2小时前'),
            news_item('「魔法少女初未来」剧场版定档8月','NEW','5小时前'),
            news_item('本周弹幕热梗TOP10出炉','热门','1天前'),
        ],
        'subnav': [
            sub_item('番剧大厅','pages/anime/index.html','&#x1F3DB;'),
            sub_item('播放器','pages/anime/player.html','&#x25B6;'),
            sub_item('新番表','pages/anime/bangumi.html','&#x1F4C5;'),
            sub_item('排行榜','pages/anime/ranking.html','&#x1F3C6;'),
            sub_item('MAD工坊','pages/anime/mad.html','&#x1F3AC;'),
            sub_item('图书馆','pages/anime/library.html','&#x1F4DA;'),
            sub_item('直播','pages/anime/live.html','&#x1F4A1;'),
            sub_item('投稿','pages/anime/upload.html','&#x1F4E4;'),
        ],
    },
]

# For brevity, generate only anime.html as proof of concept,
# then we'll do all 9 similarly
for ac in academies:
    ticks = ''.join([tick_item(n[0]) for n in [
        ('2026年7月新番「星渊编年史」今日首播！',),
        ('MAD创作大赛第三季作品征集开始',),
        ('「魔法少女初未来」剧场版定档8月',),
        ('本周弹幕热梗TOP10出炉',),
    ]])
    
    nav_items = ''.join(ac['subnav'])
    feats = ''.join(ac['feats'])
    stats = ''.join(ac['stats'])
    news = ''.join(ac['news'])
    
    html = gen(
        name=ac['name'], icon=ac['icon'], d3d=ac['d3d'], theme=ac['theme'],
        desc_html=ac['desc'], stats_html=stats, feats_html=feats,
        news_html=news, sub_nav_html=nav_items
    )
    w(ac['file'], html)

print("\nDone!")

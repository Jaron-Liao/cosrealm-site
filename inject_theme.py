#!/usr/bin/env python3
"""
批量注入: theme-toggle.js + dark-mode.css + dynamic-bg.js 到所有HTML页面
"""
import os, re, glob

BASE = r"C:\Users\28767\Downloads\cosrealm-site"

# 要注入的CSS/JS（在 </head> 前插入CSS，</body> 前插入JS）
CSS_INJECT = '''<link rel="stylesheet" href="{ROOT}assets/themes/dark-mode.css">
<link rel="stylesheet" href="{ROOT}assets/effects-layer.css">'''
JS_INJECT = '''<script src="{ROOT}assets/theme-toggle.js"></script>
<script src="{ROOT}assets/dynamic-bg.js"></script>'''

def get_root(filepath):
    """计算从文件位置到站点根的相对路径"""
    rel = os.path.relpath(filepath, BASE)
    depth = rel.count(os.sep)
    if depth == 0: return ''
    return '../' * depth

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return False
    
    # 跳过纯脚本/数据文件
    if '<!DOCTYPE' not in content and '<html' not in content.lower():
        return False
    
    root = get_root(filepath)
    css = CSS_INJECT.format(ROOT=root)
    js = JS_INJECT.format(ROOT=root)
    
    changed = False
    
    # 注入CSS（在 </head> 前，避免重复）
    if 'dark-mode.css' not in content and '</head>' in content:
        content = content.replace('</head>', f'{css}\n</head>', 1)
        changed = True
    
    # 注入JS（在 </body> 前，避免重复）
    if 'theme-toggle.js' not in content and '</body>' in content:
        # 在已有的script标签之前或直接在</body>前
        content = content.replace('</body>', f'{js}\n</body>', 1)
        changed = True
    
    # 同时确保 effects-runtime.js 也在（如果页面没有的话）
    if 'effects-runtime.js' not in content and '</body>' in content:
        eff_js = f'<script src="{root}assets/effects-runtime.js"></script>'
        content = content.replace('</body>', f'{eff_js}\n</body>', 1)
        changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# 遍历所有HTML
count = 0
for root_dir, dirs, files in os.walk(BASE):
    for fname in files:
        if fname.endswith('.html'):
            fpath = os.path.join(root_dir, fname)
            if process_file(fpath):
                count += 1
                rel = os.path.relpath(fpath, BASE)
                print(f"  ✓ {rel}")

print(f"\n完成！共更新 {count} 个 HTML 文件")

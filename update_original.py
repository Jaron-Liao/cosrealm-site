#!/usr/bin/env python3
"""批量更新原始CosRealm页面为龙奕学院品牌"""
import os, re, glob

BASE = r"C:\Users\28767\Downloads\cosrealm-site"

# 旧主题 → 学院主题映射
THEME_MAP = {
    'kawaii.css': 'sakura-academy.css',
    'galaxy.css': 'starlight-academy.css',
    'ocean.css': 'sky-academy.css',
    'crystal.css': 'mint-academy.css',
    'cyberpunk.css': 'sunset-academy.css',
    'flame.css': 'coral-academy.css',
    'forest.css': 'mint-academy.css',
    'matrix.css': 'starlight-academy.css',
    'neonwave.css': 'sunset-academy.css',
    'sakura.css': 'sakura-academy.css',
    'starlight.css': 'starlight-academy.css',
    'void.css': 'lavender-academy.css',
    'aurora.css': 'sky-academy.css',
}

# 路径→场景映射
def get_scene(path):
    if '/social/' in path: return 'academy'
    if '/shop/' in path: return 'default'
    if '/metaverse/' in path: return 'cyber'
    if '/creator/' in path: return 'academy'
    if '/digital-human/' in path: return 'cyber'
    if '/events/' in path: return 'galaxy'
    if '/academy/' in path: return 'academy'
    if '/wiki/' in path: return 'academy'
    if '/auth/' in path: return 'default'
    if '/user/' in path: return 'default'
    if '/meta/' in path: return 'default'
    # Root pages
    if 'shop.html' in path: return 'default'
    if 'metaverse.html' in path: return 'cyber'
    if 'digital-human.html' in path: return 'cyber'
    if 'academy.html' in path: return 'academy'
    return 'academy'

# 跳过新生成的页面（已含龙奕学院品牌）
SKIP_PATTERNS = [
    'pages/anime/',
    'pages/social/club.html', 'pages/social/bbs.html', 'pages/social/match.html', 'pages/social/live-room.html',
    'pages/shop/flash.html', 'pages/shop/secondhand.html', 'pages/shop/custom.html', 'pages/shop/rental.html', 'pages/shop/points.html',
    'pages/metaverse/city.html', 'pages/metaverse/combat.html', 'pages/metaverse/guild.html', 'pages/metaverse/trade.html',
    'pages/metaverse/pets.html', 'pages/metaverse/fashion.html', 'pages/metaverse/realm.html', 'pages/metaverse/airship.html',
    'pages/digital-human/ai-chat.html', 'pages/digital-human/motion.html', 'pages/digital-human/clone.html',
    'pages/digital-human/scene.html', 'pages/digital-human/emotion.html',
    'pages/academy/exam.html', 'pages/academy/cert.html', 'pages/academy/live-class.html',
    'pages/academy/ranking.html', 'pages/academy/library.html',
    'pages/events/live-show.html', 'pages/events/exhibition.html', 'pages/events/festival.html',
    'pages/events/award.html', 'pages/events/fireworks.html',
    'pages/wiki/timeline.html', 'pages/wiki/characters.html', 'pages/wiki/studios.html', 'pages/wiki/seiyuu.html',
    'pages/help/faq.html', 'pages/help/feedback.html', 'pages/help/guide.html',
    'pages/meta/join.html', 'pages/meta/partners.html', 'pages/meta/privacy.html',
]

def should_skip(path):
    for p in SKIP_PATTERNS:
        if p in path.replace('\\', '/'):
            return True
    return False

# 收集所有需要更新的页面
files = []
for f in glob.glob(os.path.join(BASE, '**/*.html'), recursive=True):
    rel = os.path.relpath(f, BASE).replace('\\', '/')
    if should_skip(rel):
        continue
    files.append(f)

print(f"Found {len(files)} pages to update")

updated = 0
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    rel = os.path.relpath(fpath, BASE).replace('\\', '/')
    scene = get_scene(rel)
    
    # 1. 替换品牌名
    content = content.replace('龙墟 MetaSingularity', '龙奕学院 LongYi Academy')
    content = content.replace('CosRealm', '龙奕学院')
    content = content.replace('龙墟·MetaSingularity', '龙奕学院')
    
    # 2. 替换旧主题为学院主题
    for old, new in THEME_MAP.items():
        content = content.replace(f'assets/themes/{old}', f'assets/themes/academy/{new}')
    
    # 3. 添加 data-3d 属性
    if 'data-3d=' not in content:
        content = content.replace('<html lang="zh-CN">', f'<html lang="zh-CN" data-3d="{scene}">')
    
    # 4. 添加 three-engine.js (在 nav.js 之前，或在 </body> 之前)
    if 'three-engine.js' not in content:
        if 'nav.js' in content:
            content = content.replace(
                '<script src="../../assets/nav.js">',
                '<script src="../../assets/three-engine.js"></script>\n<script src="../../assets/nav.js">'
            )
            content = content.replace(
                '<script src="assets/nav.js">',
                '<script src="assets/three-engine.js"></script>\n<script src="assets/nav.js">'
            )
        else:
            content = content.replace(
                '</body>',
                '\n<script src="../../assets/three-engine.js"></script>\n<script src="../../assets/nav.js"></script>\n</body>'
            )
    
    # 5. 添加 nav.js (如果完全没有)
    # (上面的步骤可能已经处理了)
    
    # 6. 更新旧导航引用
    content = content.replace('Cos维基', 'LongYi Wiki')
    
    # 7. 修复可能的旧 CSS 变量引用（如果用了旧的变量系统）
    # 旧 → 新 常见映射
    VAR_MAP = {
        'var(--border-color)': 'var(--border)',
        'var(--text-primary)': 'var(--text)',
        'var(--accent-1)': 'var(--accent)',
        'var(--accent-2)': 'var(--accent-secondary, #a78bfa)',
        'var(--accent-3)': 'var(--accent-soft, #e0e7ff)',
    }
    for old_var, new_var in VAR_MAP.items():
        content = content.replace(old_var, new_var)
    
    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated += 1

print(f"Updated: {updated}/{len(files)} pages")
print("=== DONE ===")

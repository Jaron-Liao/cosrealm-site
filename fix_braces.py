#!/usr/bin/env python3
"""Fix unescaped braces in build_academies.py SHARED_CSS"""
import os, py_compile

BASE = r"C:\Users\28767\Downloads\cosrealm-site"
filepath = os.path.join(BASE, "build_academies.py")

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find SHARED_CSS string area
start_marker = 'SHARED_CSS = """'
end_marker = '"""\n\n# '
idx_start = content.find(start_marker)
if idx_start < 0:
    # Try alternate
    start_marker = "SHARED_CSS = '''"
    idx_start = content.find(start_marker)
idx_end = content.find('"""', idx_start + len(start_marker) + 10)

print(f"CSS region: {idx_start} to {idx_end}")
before = content[:idx_start]
css_raw = content[idx_start:idx_end]
after = content[idx_end:]

# Escape all bare braces
fixed_css = css_raw.replace('{', '{{').replace('}', '}}')
print(f"CSS: {len(css_raw)} -> {len(fixed_css)} chars")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(before + fixed_css + after)

# Test
try:
    py_compile.compile(filepath, doraise=True)
    print("COMPILATION SUCCESS!")
except Exception as e:
    print(f"Still error: {e}")

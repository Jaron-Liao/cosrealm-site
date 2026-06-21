#!/usr/bin/env python3
"""批量更新所有HTML页面，指向 three-engine-v3.js"""
import os

BASE = r"C:\Users\28767\Downloads\cosrealm-site"

count = 0
for root, _, files in os.walk(BASE):
    for f in files:
        if f.endswith(".html"):
            fp = os.path.join(root, f)
            try:
                c = open(fp, encoding="utf-8", errors="ignore").read()
                if "three-engine.js" in c:
                    c = c.replace("assets/three-engine.js", "assets/three-engine-v3.js")
                    c = c.replace("assets\\three-engine.js", "assets/three-engine-v3.js")
                    open(fp, "w", encoding="utf-8").write(c)
                    count += 1
            except: pass

print("更新了 {} 个页面 -> three-engine-v3.js".format(count))

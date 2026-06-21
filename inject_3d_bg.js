const fs = require('fs');
const path = require('path');

const ROOT = 'C:/Users/28767/Downloads/cosrealm-site';

function walkDir(dir) {
  let results = [];
  const list = fs.readdirSync(dir);
  list.forEach(f => {
    const full = path.join(dir, f);
    try {
      const stat = fs.statSync(full);
      if (stat.isDirectory()) {
        if (f !== 'node_modules' && f !== '.git')
          results = results.concat(walkDir(full));
      } else if (f.endsWith('.html') && f !== 'index-backup.html') {
        results.push(full);
      }
    } catch (e) {}
  });
  return results;
}

const files = walkDir(ROOT);
console.log(`Found ${files.length} HTML files`);

let updated = 0;
files.forEach(f => {
  let content = fs.readFileSync(f, 'utf8');
  let changed = false;

  // 计算相对路径前缀
  const rel = path.relative(path.dirname(f), ROOT).replace(/\\/g, '/');
  const prefix = rel === '' ? '' : rel + '/';

  // 1. 移除 dynamic-bg.js 引用（简单字符串替换）
  const bgOld = `<script src="${prefix}assets/dynamic-bg.js"></script>`;
  if (content.includes(bgOld)) {
    content = content.replace(new RegExp(bgOld.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g'), '');
    changed = true;
  }

  // 2. 插入 bg-3d.js（在 nav.js 之后）
  const bgNew = `<script src="${prefix}assets/bg-3d.js"></script>`;
  if (!content.includes('bg-3d.js')) {
    const navTag = `<script src="${prefix}assets/nav.js"></script>`;
    if (content.includes(navTag)) {
      content = content.replace(navTag, navTag + '\n    ' + bgNew);
      changed = true;
    }
  }

  if (changed) {
    fs.writeFileSync(f, content, 'utf8');
    updated++;
    if (updated <= 5) console.log('Updated:', f.replace(ROOT, ''));
  }
});

console.log(`\nDone: ${updated} files updated`);

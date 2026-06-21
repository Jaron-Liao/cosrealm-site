const fs = require('fs');
const path = require('path');

const ROOT = 'C:/Users/28767/Downloads/cosrealm-site';

function walkDir(dir) {
  let results = [];
  try {
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
  } catch (e) {}
  return results;
}

const files = walkDir(ROOT);
console.log(`Found ${files.length} HTML files`);

let updated = 0;
files.forEach(f => {
  let content = fs.readFileSync(f, 'utf8');
  let changed = false;

  const rel = path.relative(path.dirname(f), ROOT).replace(/\\/g, '/');
  const prefix = rel === '' ? '' : rel + '/';

  // 替换 bg-3d.js 为 bg-engine.js
  const oldTag = `<script src="${prefix}assets/bg-3d.js"></script>`;
  const newTag = `<script src="${prefix}assets/bg-engine.js"></script>`;
  if (content.includes(oldTag)) {
    content = content.replace(oldTag, newTag);
    changed = true;
  }
  // 如果只有 bg-3d.js 引用但路径不同，也替换
  if (content.includes('bg-3d.js') && !content.includes('bg-engine.js')) {
    content = content.replace(/assets\/bg-3d\.js/g, 'assets/bg-engine.js');
    changed = true;
  }

  if (changed) {
    fs.writeFileSync(f, content, 'utf8');
    updated++;
    if (updated <= 3) console.log('Updated:', f.replace(ROOT, ''));
  }
});

console.log(`Done: ${updated} files updated to bg-engine.js`);

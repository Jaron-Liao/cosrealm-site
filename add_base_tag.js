const fs = require('fs');
const path = require('path');

function walkDir(dir) {
  let results = [];
  const list = fs.readdirSync(dir);
  list.forEach(f => {
    const fp = path.join(dir, f);
    if (fs.statSync(fp).isDirectory()) {
      if (f !== '.git' && f !== 'node_modules') results = results.concat(walkDir(fp));
    } else if (f.endsWith('.html')) {
      results.push(fp);
    }
  });
  return results;
}

const files = walkDir('.');
let ok = 0, skip = 0;

files.forEach(fp => {
  let html = fs.readFileSync(fp, 'utf8');
  // 跳过已有 <base> 的文件
  if (/<base\s/i.test(html)) { skip++; return; }
  // 在 <head> 后插入 <base>
  const tag = '<base href="/cosrealm-site/">';
  if (html.includes('<head>')) {
    html = html.replace('<head>', '<head>\n  ' + tag);
  } else if (html.includes('<HEAD>')) {
    html = html.replace('<HEAD>', '<HEAD>\n  ' + tag);
  } else {
    // 没有 </head> 就在 <html> 后插
    html = '<!DOCTYPE html>\n<!-- AUTO-INSERTED BASE TAG -->\n' + html;
    // 直接在第一行后加
    const lines = html.split('\n');
    let inserted = false;
    for (let i = 0; i < lines.length; i++) {
      if (/^\s*<html/i.test(lines[i])) {
        lines.splice(i + 1, 0, '  <base href="/cosrealm-site/">');
        inserted = true;
        break;
      }
    }
    if (!inserted) lines.splice(1, 0, '<base href="/cosrealm-site/">');
    html = lines.join('\n');
  }
  fs.writeFileSync(fp, html, 'utf8');
  ok++;
});

console.log(`Done: ${ok} files updated, ${skip} skipped (already had <base>)`);

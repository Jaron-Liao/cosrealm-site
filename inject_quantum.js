const fs = require("fs");
const path = require("path");

// 递归查找所有 HTML 文件
function walkDir(dir) {
  let results = [];
  const list = fs.readdirSync(dir);
  list.forEach((f) => {
    const full = path.join(dir, f);
    if (fs.statSync(full).isDirectory()) {
      // 跳过 node_modules 等
      if (f === "node_modules" || f === ".git") return;
      results = results.concat(walkDir(full));
    } else if (f.endsWith(".html")) {
      results.push(full);
    }
  });
  return results;
}

const ROOT = "C:\\Users\\28767\\Downloads\\cosrealm-site";
const files = walkDir(ROOT).filter((f) => !f.includes("index-backup"));

console.log(`Found ${files.length} HTML files`);

let updated = 0;
files.forEach((file) => {
  let content = fs.readFileSync(file, "utf8");
  let changed = false;

  // 1. 移除旧的背景脚本（dynamic-bg.js, bg-3d.js, bg-engine.js）
  const oldPatterns = [
    /<script\s+src=["']assets\/dynamic-bg\.js["']\s*><\/script>\s*\n?/g,
    /<script\s+src=["']assets\/bg-3d\.js["']\s*><\/script>\s*\n?/g,
    /<script\s+src=["']assets\/bg-engine\.js["']\s*><\/script>\s*\n?/g,
  ];
  oldPatterns.forEach((pat) => {
    if (pat.test(content)) {
      content = content.replace(pat, "");
      changed = true;
    }
  });

  // 2. 注入 quantum-bg.js（在 </body> 前，或 nav.js 后）
  if (!content.includes("quantum-bg.js")) {
    const quantumScript = '    <script src="assets/quantum-bg.js"></script>\n';
    // 计算相对路径
    const relDepth = path.relative(ROOT, path.dirname(file)).split(path.sep).length - 1;
    const prefix = relDepth > 0 ? "../".repeat(relDepth) : "./";
    
    // 插入到 </body> 前
    if (content.includes("</body>")) {
      content = content.replace(
        "</body>",
        `${quantumScript.replace("assets/", prefix + "assets/")}</body>`
      );
      changed = true;
    }
  }

  if (changed) {
    fs.writeFileSync(file, content, "utf8");
    updated++;
  }
});

console.log(`Updated ${updated} files with quantum-bg.js`);

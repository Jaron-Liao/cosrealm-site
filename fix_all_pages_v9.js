/**
 * fix_all_pages_v9.js — 全局页面排版修复
 * 给所有HTML注入完整的内容CSS，不再依赖任何外部文件
 */
const fs = require('fs');
const path = require('path');

// ===== 完整的全局页面CSS =====
const GLOBAL_CSS = `
/* ===== CosRealm 全局样式 v9 ===== */

/* --- 基础重置与背景 --- */
* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  font-family: -apple-system, "Segoe UI", "PingFang SC", "Microsoft YaHei", "Source Han Sans CN", sans-serif;
  background: #0a0a1a;
  color: #e0e0e0;
  min-height: 100vh;
  line-height: 1.6;
  overflow-x: hidden;
}
a { color: #FF6B35; text-decoration: none; transition: color 0.2s; }
a:hover { color: #ff8c5a; text-decoration: underline; }
h1, h2, h3, h4 { font-weight: 700; line-height: 1.3; color: #fff; }
h2 { font-size: 1.6rem; margin-bottom: 1rem; }
h3 { font-size: 1.2rem; margin-bottom: 0.7rem; }

/* --- 导航间距占位 --- */
.ly-spacer, .lyn-spacer { height: 58px; }

/* --- 主容器 --- */
.page-wrap {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px 16px 60px;
  position: relative;
  z-index: 1;
}

/* === HERO 区域 === */
.hero-section {
  text-align: center;
  padding: 60px 24px 48px;
  border-radius: 20px;
  margin-bottom: 36px;
  position: relative;
  overflow: hidden;
}
.hero-section h1 {
  font-size: clamp(1.8rem, 5vw, 3rem);
  margin-bottom: 12px;
  letter-spacing: 2px;
}
.hero-sub {
  font-size: 1.05rem;
  color: #aaa;
  max-width: 650px;
  margin: 0 auto 28px;
  line-height: 1.7;
}
.hero-stats {
  display: flex;
  justify-content: center;
  gap: 32px;
  flex-wrap: wrap;
  margin-top: 24px;
}
.hero-stat {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.hs-val {
  font-size: 1.6rem;
  font-weight: 800;
  color: #FF6B35;
}
.hs-lbl {
  font-size: 0.78rem;
  color: #888;
  margin-top: 2px;
}

/* === 快捷链接卡片 === */
.quick-links {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 14px;
  margin-bottom: 40px;
}
.ql-card {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 18px 16px;
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,107,53,0.15);
  border-radius: 14px;
  transition: all 0.3s ease;
  cursor: pointer;
  text-decoration: none !important;
  color: #e0e0e0 !important;
}
.ql-card:hover {
  background: rgba(255,107,53,0.12);
  border-color: rgba(255,107,53,0.5);
  transform: translateY(-3px);
  box-shadow: 0 8px 30px rgba(255,107,53,0.15);
  text-decoration: none !important;
}
.qi { font-size: 1.8rem; }
.qn { font-weight: 600; font-size: 0.92rem; }

/* === 功能网格卡片 === */
.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 18px;
  margin-bottom: 40px;
}
.feat-card {
  display: block;
  padding: 26px 22px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 16px;
  transition: all 0.3s ease;
  text-decoration: none !important;
  color: inherit !important;
}
.feat-card:hover {
  background: rgba(255,107,53,0.08);
  border-color: rgba(255,107,53,0.3);
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(0,0,0,0.4);
  text-decoration: none !important;
}
.fi { font-size: 2rem; display: block; margin-bottom: 8px; }
.fn { font-size: 1.1rem; font-weight: 700; color: #fff; margin-bottom: 6px; }
.fd { font-size: 0.88rem; color: #999; line-height: 1.6; }

/* === 章节标题 === */
.sec-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 44px 0 20px;
}
.sh-icon { font-size: 1.3rem; }
.sec-header h2 {
  background: linear-gradient(135deg, #FF6B35, #ff9a6c);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* === 数字人面板 === */
.dh-layout {
  display: grid;
  grid-template-columns: 340px 1fr;
  gap: 24px;
  margin-bottom: 40px;
}
.dh-controls { display: flex; flex-direction: column; gap: 14px; }
.ctrl-card {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px;
  padding: 18px;
}
.ctrl-card h3 { font-size: 0.95rem; margin-bottom: 12px; color: #FF6B35; }

.style-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
}
.style-opt {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 10px 8px;
  border-radius: 10px;
  background: rgba(255,255,255,0.03);
  border: 1px solid transparent;
  cursor: pointer;
  font-size: 0.85rem;
  transition: all 0.2s;
  text-align: center;
  justify-content: center;
}
.style-opt:hover { background: rgba(255,107,53,0.1); }
.style-opt.selected {
  background: rgba(255,107,53,0.15);
  border-color: rgba(255,107,53,0.4);
  color: #FF6B35;
}
.se { font-size: 1.2rem; }

.slider-group {
  margin-bottom: 14px;
}
.slider-group label {
  display: flex;
  justify-content: space-between;
  font-size: 0.85rem;
  color: #bbb;
  margin-bottom: 6px;
}
.slider-group input[type="range"] {
  width: 100%;
  accent-color: #FF6B35;
  cursor: pointer;
}

.color-grid {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}
.color-dot {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  cursor: pointer;
  border: 2px solid transparent;
  transition: transform 0.2s;
}
.color-dot:hover { transform: scale(1.15); }
.color-dot.selected {
  border-color: #fff;
  box-shadow: 0 0 12px currentColor;
}

.preview-stage {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 420px;
  position: relative;
  overflow: hidden;
}
.pv-avatar {
  text-align: center;
}
.face {
  font-size: 6rem;
  display: block;
  filter: brightness(0.8);
  transition: filter 0.3s;
}
.pv-name { font-size: 1.1rem; font-weight: 700; color: #fff; margin-top: 8px; }
.pv-info { font-size: 0.82rem; color: #888; }

.voice-wave {
  display: flex;
  align-items: flex-end;
  gap: 3px;
  height: 24px;
  justify-content: center;
  margin-top: 12px;
  opacity: 0;
  transition: opacity 0.3s;
}
.voice-wave.show { opacity: 1; }
.voice-wave .bar {
  width: 4px;
  background: #FF6B35;
  border-radius: 2px;
  animation: waveBar 0.8s ease-in-out infinite;
}
.voice-wave .bar:nth-child(2) { animation-delay: 0.1s; }
.voice-wave .bar:nth-child(3) { animation-delay: 0.2s; }
.voice-wave .bar:nth-child(4) { animation-delay: 0.3s; }
.voice-wave .bar:nth-child(5) { animation-delay: 0.4s; }
@keyframes waveBar {
  0%, 100% { height: 6px; }
  50% { height: 22px; }
}

/* === Anime 卡片 === */
.anime-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 18px;
  margin-bottom: 36px;
}
.anime-card {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px;
  overflow: hidden;
  transition: all 0.3s ease;
  text-decoration: none !important;
  color: inherit !important;
}
.anime-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 35px rgba(0,0,0,0.4);
  border-color: rgba(255,107,53,0.3);
}
.ac-thumb {
  aspect-ratio: 3/4;
  background: linear-gradient(135deg, #1a1a3e, #2d1b4e);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
}
.ac-info { padding: 14px; }
.ac-title { font-weight: 700; font-size: 0.95rem; color: #fff; margin-bottom: 4px; }
.ac-meta { font-size: 0.8rem; color: #888; }
.ac-badge {
  display: inline-block;
  padding: 2px 8px;
  border-radius: 20px;
  font-size: 0.72rem;
  font-weight: 600;
  margin-top: 6px;
}
.genre-scroll { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 24px; }
.genre-tag {
  padding: 6px 16px;
  border-radius: 20px;
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.1);
  font-size: 0.83rem;
  cursor: pointer;
  transition: all 0.2s;
}
.genre-tag:hover, .genre-tag.active {
  background: rgba(255,107,53,0.2);
  border-color: rgba(255,107,53,0.4);
  color: #FF6B35;
}

/* === 通用网格卡片（Academy/Wiki等） === */
.gear-grid, .collab-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 18px;
  margin-bottom: 36px;
}
.gcard, .collab-card {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px;
  padding: 24px;
  transition: all 0.3s ease;
  text-decoration: none !important;
  color: inherit !important;
  display: block;
}
.gcard:hover, .collab-card:hover {
  border-color: rgba(255,107,53,0.3);
  transform: translateY(-3px);
  box-shadow: 0 8px 30px rgba(0,0,0,0.3);
}
.gi, .cd { font-size: 2rem; display: block; margin-bottom: 8px; }
.gn, .cn { font-size: 1.05rem; font-weight: 700; color: #fff; margin-bottom: 6px; }
.fb-desc { font-size: 0.87rem; color: #999; line-height: 1.6; }
.gtag, .gtags { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 10px; }
.gtag {
  padding: 3px 10px;
  border-radius: 12px;
  font-size: 0.75rem;
  background: rgba(255,107,53,0.1);
  color: #ff9a6c;
}

/* === FAQ 手风琴 === */
.faq-section { margin-bottom: 36px; }
.faq-item {
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 12px;
  margin-bottom: 8px;
  overflow: hidden;
  background: rgba(255,255,255,0.02);
}
.faq-q {
  padding: 16px 18px;
  cursor: pointer;
  font-weight: 600;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: background 0.2s;
}
.faq-q:hover { background: rgba(255,107,53,0.06); }
.faq-a {
  padding: 0 18px 16px;
  color: #aaa;
  font-size: 0.9rem;
  line-height: 1.7;
}

/* === Events 活动卡片 === */
.ev-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 18px;
  margin-bottom: 36px;
}
.ev-card {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 16px;
  overflow: hidden;
  transition: all 0.3s;
  text-decoration: none !important;
  color: inherit !important;
}
.ev-card:hover { transform: translateY(-3px); box-shadow: 0 10px 35px rgba(0,0,0,0.4); }
.ev-date-badge {
  background: linear-gradient(135deg, #FF6B35, #ff9a6c);
  color: #fff;
  padding: 12px;
  text-align: center;
  font-weight: 700;
}
.ev-body { padding: 18px; }
.ev-desc { color: #aaa; font-size: 0.9rem; line-height: 1.6; margin-bottom: 10px; }
.ev-footer { display: flex; justify-content: space-between; font-size: 0.82rem; color: #777; }

.activity-feed { margin-bottom: 36px; }
.act-item {
  display: flex;
  gap: 14px;
  padding: 16px;
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 12px;
  margin-bottom: 10px;
  transition: background 0.2s;
}
.act-item:hover { background: rgba(255,255,255,0.05); }
.act-av {
  width: 44px; height: 44px;
  border-radius: 50%;
  background: linear-gradient(135deg, #FF6B35, #c44dff);
  display: flex; align-items: center; justify-content: center;
  font-size: 1.3rem; flex-shrink: 0;
}
.act-body { flex: 1; }
.at { font-weight: 600; color: #fff; }
.atm { font-size: 0.85rem; color: #999; margin-top: 2px; }

.cta-section {
  text-align: center;
  padding: 48px 24px;
  background: linear-gradient(135deg, rgba(255,107,53,0.08), rgba(196,77,255,0.08));
  border: 1px solid rgba(255,107,53,0.15);
  border-radius: 20px;
  margin-bottom: 36px;
}
.cta-icon { font-size: 2.5rem; margin-bottom: 12px; }
.cta-title { font-size: 1.4rem; font-weight: 700; color: #fff; margin-bottom: 8px; }
.cta-desc { color: #aaa; margin-bottom: 20px; }
.cta-text { font-size: 0.95rem; color: #ccc; }

/* === Shop 商城 === */
.cart-fab {
  position: fixed;
  bottom: 24px;
  right: 24px;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: linear-gradient(135deg, #FF6B35, #ff9a6c);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  z-index: 998;
  box-shadow: 0 4px 20px rgba(255,107,53,0.4);
  cursor: pointer;
  border: none;
}
.cart-count {
  position: absolute;
  top: -4px; right: -4px;
  width: 20px; height: 20px;
  border-radius: 50%;
  background: #ff4081;
  color: #fff;
  font-size: 0.72rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
}
.cart-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.6);
  z-index: 999;
  display: none;
}
.cart-panel {
  position: fixed;
  top: 0; right: -380px;
  width: 370px;
  max-width: 90vw;
  height: 100vh;
  background: #12122a;
  border-left: 1px solid rgba(255,255,255,0.1);
  z-index: 1000;
  transition: right 0.3s;
  display: flex;
  flex-direction: column;
}
.cart-panel.open { right: 0; }
.cart-hd {
  padding: 18px 20px;
  border-bottom: 1px solid rgba(255,255,255,0.08);
  font-weight: 700;
  font-size: 1.05rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.cart-items { flex: 1; overflow-y: auto; padding: 12px; }
.ci-row {
  display: flex;
  gap: 12px;
  padding: 12px;
  background: rgba(255,255,255,0.03);
  border-radius: 10px;
  margin-bottom: 8px;
}
.ci-img {
  width: 60px; height: 60px;
  border-radius: 8px;
  background: linear-gradient(135deg, #1a1a3e, #2d1b4e);
  display: flex; align-items: center; justify-content: center;
  font-size: 1.5rem;
  flex-shrink: 0;
}
.ci-info { flex: 1; }
.ci-name { font-weight: 600; font-size: 0.88rem; color: #fff; }
.ci-price { color: #FF6B35; font-weight: 700; margin-top: 4px; }
.ci-qty { display: flex; align-items: center; gap: 8px; margin-top: 6px; }
.cart-ft {
  padding: 16px 20px;
  border-top: 1px solid rgba(255,255,255,0.08);
}
.cart-total {
  font-size: 1.1rem;
  font-weight: 700;
  display: flex;
  justify-content: space-between;
  margin-bottom: 12px;
}
.cta-banner {
  text-align: center;
  padding: 36px 20px;
  background: linear-gradient(135deg, rgba(255,107,53,0.06), rgba(196,77,255,0.06));
  border-radius: 16px;
  border: 1px solid rgba(255,107,53,0.12);
  margin-bottom: 28px;
}

/* === Social 社交 === */
.feed-post {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 14px;
  padding: 20px;
  margin-bottom: 16px;
  transition: border-color 0.2s;
}
.feed-post:hover { border-color: rgba(255,107,53,0.2); }
.badge {
  display: inline-block;
  padding: 2px 10px;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
}
.ai-zone {
  background: linear-gradient(135deg, rgba(196,77,255,0.08), rgba(0,229,255,0.08));
  border: 1px solid rgba(196,77,255,0.2);
  border-radius: 14px;
  padding: 20px;
  margin-bottom: 20px;
}
.az-icon { font-size: 1.5rem; }
.live-dot {
  width: 8px; height: 8px;
  border-radius: 50%;
  background: #ff4081;
  animation: livePulse 1.5s infinite;
  display: inline-block;
  margin-right: 4px;
}
@keyframes livePulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.3; }
}
.live-dots { display: flex; gap: 4px; }
.live-dots > div {
  width: 6px; height: 6px;
  border-radius: 50%;
  background: #ff4081;
  animation: livePulse 1.5s infinite;
}
.live-dots > div:nth-child(2) { animation-delay: 0.2s; }
.live-dots > div:nth-child(3) { animation-delay: 0.4s; }

/* === Wiki === */
.cat-row { display: flex; gap: 12px; margin-bottom: 24px; flex-wrap: wrap; }
.cat-card {
  padding: 20px 24px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px;
  min-width: 160px;
  flex: 1;
  transition: all 0.3s;
  text-decoration: none !important;
  color: inherit !important;
}
.cat-card:hover {
  border-color: rgba(255,107,53,0.3);
  background: rgba(255,107,53,0.06);
}
.cci { font-size: 1.8rem; display: block; margin-bottom: 6px; }
.ccn { font-weight: 700; color: #fff; font-size: 0.95rem; }

/* === 按钮 === */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 10px 24px;
  border-radius: 10px;
  font-weight: 600;
  font-size: 0.92rem;
  cursor: pointer;
  border: none;
  transition: all 0.25s ease;
  text-decoration: none !important;
  gap: 6px;
}
.btn-primary {
  background: linear-gradient(135deg, #FF6B35, #ff9a6c);
  color: #fff !important;
  box-shadow: 0 4px 16px rgba(255,107,53,0.3);
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 24px rgba(255,107,53,0.45);
}
.btn-outline {
  background: transparent;
  border: 1px solid rgba(255,107,53,0.4);
  color: #FF6B35 !important;
}
.btn-outline:hover {
  background: rgba(255,107,53,0.1);
  border-color: #FF6B35;
}
.btn-ghost {
  background: transparent;
  color: #ccc !important;
  border: 1px solid rgba(255,255,255,0.12);
}
.btn-ghost:hover { background: rgba(255,255,255,0.06); color: #fff !important; }
.btn-lg { padding: 14px 32px; font-size: 1.05rem; border-radius: 12px; }
.btn-sm { padding: 6px 14px; font-size: 0.82rem; border-radius: 8px; }

/* === Metaverse 3D立方体 === */
.cube-box {
  perspective: 800px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
}
.cube {
  width: 160px;
  height: 160px;
  position: relative;
  transform-style: preserve-3d;
  animation: cubeSpin 12s linear infinite;
}
@keyframes cubeSpin {
  0% { transform: rotateX(0) rotateY(0); }
  100% { transform: rotateX(360deg) rotateY(360deg); }
}
.cf {
  position: absolute;
  width: 160px; height: 160px;
  border: 2px solid rgba(255,107,53,0.4);
  background: rgba(255,107,53,0.06);
  display: flex; align-items: center; justify-content: center;
  font-size: 2rem;
  backface-visibility: visible;
}
.cf-front  { transform: translateZ(80px); }
.cf-back   { transform: rotateY(180deg) translateZ(80px); }
.cf-right  { transform: rotateY(90deg) translateZ(80px); }
.cf-left   { transform: rotateY(-90deg) translateZ(80px); }
.cf-top    { transform: rotateX(90deg) translateZ(80px); }
.cf-bottom { transform: rotateX(-90deg) translateZ(80px); }

.cube-stage {
  display: flex;
  justify-content: center;
  gap: 60px;
  flex-wrap: wrap;
  padding: 40px 0;
}
.day {
  text-align: center;
  padding: 20px;
}
.dot {
  width: 10px; height: 10px;
  border-radius: 50%;
  background: #FF6B35;
  display: inline-block;
  margin: 0 4px;
  opacity: 0.3;
}
.dot.active { opacity: 1; box-shadow: 0 0 10px #FF6B35; }

/* === Creator Dashboard === */
.dash-grid {
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: 24px;
  margin-bottom: 36px;
}
.dash-side {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.dash-main { min-width: 0; }

/* === Feature Banner === */
.feat-banner {
  background: linear-gradient(135deg, rgba(255,107,53,0.08), rgba(196,77,255,0.08));
  border: 1px solid rgba(255,107,53,0.15);
  border-radius: 16px;
  padding: 28px 24px;
  margin-bottom: 30px;
  display: flex;
  align-items: center;
  gap: 16px;
}
.fb-icon { font-size: 2.2rem; }
.fb-title { font-size: 1.15rem; font-weight: 700; color: #fff; }
.fb-desc { font-size: 0.88rem; color: #aaa; margin-top: 4px; }
.fb-tag {
  display: inline-block;
  padding: 3px 12px;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
  margin-top: 8px;
  background: rgba(255,107,53,0.15);
  color: #FF6B35;
}
.fb-overlay {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
}

/* === Countdown === */
.cd-item {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  padding: 10px 16px;
  background: rgba(255,255,255,0.05);
  border-radius: 12px;
  min-width: 64px;
}
.cd-num { font-size: 1.6rem; font-weight: 800; color: #FF6B35; }
.cd-label { font-size: 0.75rem; color: #888; }

/* === Emoji === */
.cemoji { font-size: 1.2rem; }

/* === Arrow === */
.arrow {
  font-size: 1.2rem;
  transition: transform 0.2s;
}
.faq-item.open .arrow { transform: rotate(180deg); }

/* === Responsive === */
@media (max-width: 768px) {
  .dh-layout { grid-template-columns: 1fr; }
  .dash-grid { grid-template-columns: 1fr; }
  .feature-grid { grid-template-columns: 1fr; }
  .ev-grid { grid-template-columns: 1fr; }
  .anime-grid { grid-template-columns: repeat(2, 1fr); }
  .quick-links { grid-template-columns: repeat(2, 1fr); }
  .gear-grid, .collab-grid { grid-template-columns: 1fr; }
  .hero-stats { gap: 20px; }
  .page-wrap { padding: 12px 12px 40px; }
  .hero-section { padding: 36px 16px 32px; }
  .cube-box { padding: 30px 10px; }
  .cart-panel { width: 100vw; right: -100vw; }
}
`;

let count = 0;
let errors = 0;

function processFile(filePath) {
  let html = fs.readFileSync(filePath, 'utf-8');
  
  // 检查是否已经注入过
  if (html.includes('id="cr-global-css"')) {
    return false; // 已处理过
  }
  
  // 删除无效的外部CSS链接（保留lyn-nav-css）
  html = html.replace(/<link[^>]*rel=["']stylesheet["'][^>]*href=["'](assets\/[^"']+\.css)["'][^>]*>/gi, '');
  
  // 在 lyn-nav-css 的 </style> 后面插入全局CSS
  const insertPoint = html.indexOf('</style>', html.indexOf('id="lynav-css"'));
  if (insertPoint === -1) {
    // 如果没有 lyn-nav-css，在 </head> 或 <body> 前面插入
    const headEnd = html.indexOf('</head>');
    if (headEnd !== -1) {
      html = html.slice(0, headEnd) + '<style id="cr-global-css">' + GLOBAL_CSS + '</style>' + html.slice(headEnd);
      count++;
      return true;
    }
    return false;
  }
  
  // 在 lyn-nav-css 的 style 结束标签后插入
  const pos = insertPoint + '</style>'.length;
  html = html.slice(0, pos) + '\n<style id="cr-global-css">' + GLOBAL_CSS + '</style>\n' + html.slice(pos);
  
  fs.writeFileSync(filePath, html, 'utf-8');
  count++;
  return true;
}

function walkDir(dir) {
  const files = fs.readdirSync(dir);
  for (const f of files) {
    const fp = path.join(dir, f);
    const stat = fs.statSync(fp);
    if (stat.isDirectory() && f !== '.git') {
      walkDir(fp);
    } else if (f.endsWith('.html') && f !== 'sitemap.html' && !f.startsWith('index-backup')) {
      try {
        processFile(fp);
      } catch(e) {
        console.error('ERR ' + fp + ': ' + e.message);
        errors++;
      }
    }
  }
}

console.log('=== CosRealm Global CSS Injection v9 ===');
walkDir('.');
console.log('\nDone! Updated ' + count + ' files (' + errors + ' errors)');

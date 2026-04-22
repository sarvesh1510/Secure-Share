<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SecureShare — Encrypted File Transfer</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>

/* ── RESET ── */
*, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
html { scroll-behavior: smooth; }

/* ── TOKENS ── */
:root {
  --bg:       #060912;
  --surface:  #0d1221;
  --card:     #111827;
  --border:   rgba(255,255,255,0.07);
  --accent:   #00e5ff;
  --accent2:  #7b61ff;
  --text:     #e8eaf0;
  --muted:    rgba(232,234,240,0.45);
  --font-h:   'Syne', sans-serif;
  --font-b:   'DM Sans', sans-serif;
  --glow:     0 0 40px rgba(0,229,255,0.18);
}

/* ── BODY ── */
body {
  font-family: var(--font-b);
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
  overflow-x: hidden;
}

/* ── NOISE OVERLAY ── */
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 512 512' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.035'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 0;
  opacity: 0.6;
}

/* ── BACKGROUND ORBS ── */
.bg-orbs {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 0;
  overflow: hidden;
}
.orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(100px);
  animation: drift 18s ease-in-out infinite alternate;
}
.orb-1 {
  width: 500px; height: 500px;
  background: radial-gradient(circle, rgba(0,229,255,0.12), transparent 70%);
  top: -100px; left: -100px;
  animation-delay: 0s;
}
.orb-2 {
  width: 600px; height: 600px;
  background: radial-gradient(circle, rgba(123,97,255,0.1), transparent 70%);
  bottom: -200px; right: -150px;
  animation-delay: -6s;
}
.orb-3 {
  width: 300px; height: 300px;
  background: radial-gradient(circle, rgba(0,229,255,0.07), transparent 70%);
  top: 50%; left: 50%;
  transform: translate(-50%,-50%);
  animation-delay: -12s;
}

@keyframes drift {
  0%   { transform: translate(0,0) scale(1); }
  50%  { transform: translate(40px,30px) scale(1.05); }
  100% { transform: translate(-20px,50px) scale(0.97); }
}

/* ── GRID LINES ── */
.grid-overlay {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.022) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.022) 1px, transparent 1px);
  background-size: 60px 60px;
}

/* ── WRAPPER ── */
.wrap {
  position: relative;
  z-index: 1;
  max-width: 1160px;
  margin: 0 auto;
  padding: 0 32px;
}

/* ── NAVBAR ── */
nav {
  position: sticky;
  top: 0;
  z-index: 100;
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  background: rgba(6,9,18,0.7);
  border-bottom: 1px solid var(--border);
}
.nav-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 68px;
}
.logo {
  font-family: var(--font-h);
  font-weight: 800;
  font-size: 1.25rem;
  letter-spacing: -0.03em;
  display: flex;
  align-items: center;
  gap: 10px;
  color: var(--text);
  text-decoration: none;
}
.logo-icon {
  width: 32px; height: 32px;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  border-radius: 8px;
  display: grid;
  place-items: center;
  font-size: 0.85rem;
  color: #000;
  box-shadow: var(--glow);
}
.nav-links {
  display: flex;
  gap: 8px;
  align-items: center;
}
.nav-link {
  font-size: 0.875rem;
  color: var(--muted);
  text-decoration: none;
  padding: 7px 14px;
  border-radius: 8px;
  transition: color 0.2s, background 0.2s;
  font-weight: 400;
}
.nav-link:hover { color: var(--text); background: rgba(255,255,255,0.05); }
.nav-cta {
  font-family: var(--font-h);
  font-size: 0.85rem;
  font-weight: 600;
  letter-spacing: 0.02em;
  color: #000;
  background: var(--accent);
  text-decoration: none;
  padding: 9px 20px;
  border-radius: 8px;
  transition: box-shadow 0.3s, transform 0.2s;
  box-shadow: 0 0 0 rgba(0,229,255,0);
}
.nav-cta:hover {
  box-shadow: 0 0 24px rgba(0,229,255,0.4);
  transform: translateY(-1px);
}

/* ── HERO ── */
.hero {
  padding: 110px 0 80px;
  text-align: center;
}
.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 16px;
  border: 1px solid rgba(0,229,255,0.25);
  border-radius: 100px;
  font-size: 0.78rem;
  font-weight: 500;
  color: var(--accent);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 32px;
  background: rgba(0,229,255,0.05);
  animation: fadeUp 0.6s ease both;
}
.badge-dot {
  width: 6px; height: 6px;
  background: var(--accent);
  border-radius: 50%;
  box-shadow: 0 0 6px var(--accent);
  animation: pulse 2s ease-in-out infinite;
}
@keyframes pulse {
  0%,100% { opacity: 1; transform: scale(1); }
  50%      { opacity: 0.4; transform: scale(0.7); }
}

.hero h1 {
  font-family: var(--font-h);
  font-size: clamp(3rem, 6vw, 5.5rem);
  font-weight: 800;
  line-height: 1.03;
  letter-spacing: -0.04em;
  max-width: 780px;
  margin: 0 auto 24px;
  animation: fadeUp 0.7s 0.1s ease both;
}
.hero h1 .highlight {
  background: linear-gradient(135deg, var(--accent) 0%, var(--accent2) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.hero-sub {
  font-size: 1.1rem;
  font-weight: 300;
  color: var(--muted);
  max-width: 520px;
  margin: 0 auto 48px;
  line-height: 1.7;
  animation: fadeUp 0.7s 0.2s ease both;
}

/* ── HERO BUTTONS ── */
.hero-actions {
  display: flex;
  gap: 14px;
  justify-content: center;
  flex-wrap: wrap;
  animation: fadeUp 0.7s 0.3s ease both;
}
.btn {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  padding: 15px 28px;
  border-radius: 12px;
  font-family: var(--font-h);
  font-size: 0.9rem;
  font-weight: 600;
  text-decoration: none;
  letter-spacing: 0.01em;
  transition: all 0.25s ease;
  cursor: pointer;
  border: none;
}
.btn-send {
  background: var(--accent);
  color: #000;
  box-shadow: 0 4px 30px rgba(0,229,255,0.25);
}
.btn-send:hover {
  box-shadow: 0 6px 40px rgba(0,229,255,0.45);
  transform: translateY(-3px);
}
.btn-receive {
  background: transparent;
  color: var(--text);
  border: 1px solid rgba(255,255,255,0.15);
  backdrop-filter: blur(8px);
}
.btn-receive:hover {
  background: rgba(255,255,255,0.06);
  border-color: rgba(255,255,255,0.3);
  transform: translateY(-3px);
}
.btn-ghost {
  background: transparent;
  color: var(--muted);
  padding: 15px 20px;
}
.btn-ghost:hover {
  color: var(--text);
  background: rgba(255,255,255,0.04);
}

/* ── TRUST BAR ── */
.trust-bar {
  margin-top: 64px;
  display: flex;
  justify-content: center;
  gap: 40px;
  flex-wrap: wrap;
  animation: fadeUp 0.7s 0.45s ease both;
}
.trust-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.82rem;
  color: var(--muted);
  font-weight: 300;
}
.trust-item i { color: var(--accent); font-size: 0.95rem; }

/* ── UPLOAD DEMO ── */
.demo-section {
  margin: 80px 0;
  animation: fadeUp 0.7s 0.5s ease both;
}
.demo-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 40px;
  position: relative;
  overflow: hidden;
  max-width: 680px;
  margin: 0 auto;
}
.demo-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--accent), transparent);
  opacity: 0.6;
}
.drop-zone {
  border: 2px dashed rgba(0,229,255,0.25);
  border-radius: 14px;
  padding: 50px 24px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s;
  position: relative;
}
.drop-zone:hover {
  border-color: rgba(0,229,255,0.6);
  background: rgba(0,229,255,0.03);
}
.drop-zone.drag-over {
  border-color: var(--accent);
  background: rgba(0,229,255,0.06);
  transform: scale(1.01);
}
.drop-icon {
  font-size: 2.5rem;
  color: var(--accent);
  margin-bottom: 14px;
  display: block;
  filter: drop-shadow(0 0 12px rgba(0,229,255,0.4));
}
.drop-title {
  font-family: var(--font-h);
  font-size: 1.1rem;
  font-weight: 700;
  margin-bottom: 6px;
}
.drop-sub { font-size: 0.85rem; color: var(--muted); }
.drop-sub span { color: var(--accent); cursor: pointer; }
.progress-bar-wrap {
  margin-top: 24px;
  display: none;
}
.progress-label {
  display: flex;
  justify-content: space-between;
  font-size: 0.82rem;
  color: var(--muted);
  margin-bottom: 8px;
}
.progress-track {
  background: rgba(255,255,255,0.07);
  border-radius: 100px;
  height: 6px;
  overflow: hidden;
}
.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--accent), var(--accent2));
  border-radius: 100px;
  width: 0;
  transition: width 0.4s ease;
  box-shadow: 0 0 10px rgba(0,229,255,0.5);
}
.demo-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 24px;
  flex-wrap: gap;
  gap: 12px;
}
.expire-badge {
  display: flex;
  align-items: center;
  gap: 7px;
  font-size: 0.8rem;
  color: var(--muted);
}
.expire-badge i { color: var(--accent2); }
.demo-send-btn {
  font-family: var(--font-h);
  font-size: 0.85rem;
  font-weight: 700;
  color: #000;
  background: var(--accent);
  border: none;
  padding: 11px 24px;
  border-radius: 9px;
  cursor: pointer;
  transition: all 0.25s;
  display: flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 4px 20px rgba(0,229,255,0.2);
}
.demo-send-btn:hover {
  box-shadow: 0 6px 30px rgba(0,229,255,0.5);
  transform: translateY(-2px);
}

/* ── STATS ROW ── */
.stats {
  margin: 40px 0 80px;
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: 16px;
  overflow: hidden;
}
.stat {
  background: var(--surface);
  padding: 36px 24px;
  text-align: center;
  transition: background 0.3s;
}
.stat:hover { background: var(--card); }
.stat-num {
  font-family: var(--font-h);
  font-size: 2.4rem;
  font-weight: 800;
  letter-spacing: -0.04em;
  background: linear-gradient(135deg, #fff 0%, rgba(255,255,255,0.55) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.stat-label { font-size: 0.82rem; color: var(--muted); margin-top: 6px; font-weight: 300; }

/* ── SECTION HEADING ── */
.section-label {
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 14px;
}
.section-title {
  font-family: var(--font-h);
  font-size: clamp(2rem, 3.5vw, 2.8rem);
  font-weight: 800;
  letter-spacing: -0.04em;
  line-height: 1.1;
  margin-bottom: 16px;
}
.section-desc {
  color: var(--muted);
  font-size: 1rem;
  font-weight: 300;
  line-height: 1.7;
  max-width: 540px;
}

/* ── FEATURES ── */
.features-section { margin: 80px 0; }
.features-header { margin-bottom: 52px; }
.features-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}
@media(max-width:640px){
  .features-grid { grid-template-columns: 1fr; }
  .stats { grid-template-columns: 1fr; }
  .hero h1 { font-size: 2.6rem; }
  .nav-links { display: none; }
}
.feat-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 32px;
  position: relative;
  overflow: hidden;
  transition: all 0.3s;
  cursor: default;
}
.feat-card::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 16px;
  opacity: 0;
  transition: opacity 0.3s;
  background: linear-gradient(135deg, rgba(0,229,255,0.04), transparent);
}
.feat-card:hover {
  border-color: rgba(0,229,255,0.2);
  transform: translateY(-4px);
  box-shadow: 0 20px 60px rgba(0,0,0,0.3);
}
.feat-card:hover::after { opacity: 1; }
.feat-icon {
  width: 46px; height: 46px;
  border-radius: 12px;
  display: grid;
  place-items: center;
  font-size: 1.1rem;
  margin-bottom: 20px;
  position: relative;
  z-index: 1;
}
.feat-icon-cyan  { background: rgba(0,229,255,0.1); color: var(--accent); box-shadow: 0 0 20px rgba(0,229,255,0.15); }
.feat-icon-violet { background: rgba(123,97,255,0.1); color: var(--accent2); box-shadow: 0 0 20px rgba(123,97,255,0.15); }
.feat-icon-green { background: rgba(0,255,170,0.1); color: #00ffaa; box-shadow: 0 0 20px rgba(0,255,170,0.1); }
.feat-icon-rose  { background: rgba(255,100,120,0.1); color: #ff6478; box-shadow: 0 0 20px rgba(255,100,120,0.1); }
.feat-title {
  font-family: var(--font-h);
  font-size: 1.05rem;
  font-weight: 700;
  margin-bottom: 10px;
  position: relative; z-index: 1;
}
.feat-text {
  font-size: 0.88rem;
  color: var(--muted);
  line-height: 1.65;
  font-weight: 300;
  position: relative; z-index: 1;
}
.feat-tag {
  display: inline-block;
  margin-top: 14px;
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  padding: 3px 10px;
  border-radius: 100px;
  position: relative; z-index: 1;
}
.tag-cyan   { background: rgba(0,229,255,0.1); color: var(--accent); }
.tag-violet { background: rgba(123,97,255,0.1); color: var(--accent2); }
.tag-green  { background: rgba(0,255,170,0.1); color: #00ffaa; }
.tag-rose   { background: rgba(255,100,120,0.1); color: #ff6478; }

/* ── HOW IT WORKS ── */
.how-section { margin: 80px 0; }
.steps {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 16px;
  margin-top: 52px;
  position: relative;
}
@media(max-width:768px){ .steps { grid-template-columns: 1fr; } }
.steps::before {
  content: '';
  position: absolute;
  top: 42px; left: calc(16.66% + 16px); right: calc(16.66% + 16px);
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--border), var(--border), transparent);
}
.step {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 32px 28px;
  transition: all 0.3s;
  position: relative;
}
.step:hover {
  border-color: rgba(0,229,255,0.2);
  transform: translateY(-4px);
}
.step-num {
  font-family: var(--font-h);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: var(--accent);
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.step-num::before {
  content: attr(data-n);
  width: 28px; height: 28px;
  background: rgba(0,229,255,0.1);
  border: 1px solid rgba(0,229,255,0.25);
  border-radius: 8px;
  display: grid;
  place-items: center;
  font-size: 0.8rem;
  font-weight: 700;
}
.step-title {
  font-family: var(--font-h);
  font-size: 1.05rem;
  font-weight: 700;
  margin-bottom: 10px;
}
.step-text { font-size: 0.875rem; color: var(--muted); line-height: 1.65; font-weight: 300; }

/* ── CTA ── */
.cta-section {
  margin: 80px 0 100px;
}
.cta-box {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 70px 48px;
  text-align: center;
  position: relative;
  overflow: hidden;
}
.cta-box::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--accent), transparent);
  opacity: 0.5;
}
.cta-box::after {
  content: '';
  position: absolute;
  bottom: -150px; left: 50%;
  transform: translateX(-50%);
  width: 400px; height: 300px;
  background: radial-gradient(ellipse, rgba(0,229,255,0.08), transparent 70%);
  pointer-events: none;
}
.cta-box h2 {
  font-family: var(--font-h);
  font-size: clamp(2rem, 4vw, 3rem);
  font-weight: 800;
  letter-spacing: -0.04em;
  margin-bottom: 16px;
}
.cta-box p {
  color: var(--muted);
  font-size: 1rem;
  font-weight: 300;
  max-width: 460px;
  margin: 0 auto 36px;
  line-height: 1.7;
}
.cta-buttons {
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
  position: relative; z-index: 1;
}

/* ── FOOTER ── */
footer {
  border-top: 1px solid var(--border);
  padding: 28px 0;
  position: relative; z-index: 1;
}
.footer-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
}
.footer-copy { font-size: 0.82rem; color: var(--muted); font-weight: 300; }
.footer-links {
  display: flex;
  gap: 24px;
}
.footer-link {
  font-size: 0.82rem;
  color: var(--muted);
  text-decoration: none;
  transition: color 0.2s;
}
.footer-link:hover { color: var(--text); }

/* ── ANIMATIONS ── */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0); }
}
.reveal {
  opacity: 0;
  transform: translateY(28px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
.reveal-delay-1 { transition-delay: 0.1s; }
.reveal-delay-2 { transition-delay: 0.2s; }
.reveal-delay-3 { transition-delay: 0.3s; }
.reveal-delay-4 { transition-delay: 0.4s; }

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(255,255,255,0.2); }

</style>
</head>
<body>

<!-- BG -->
<div class="bg-orbs">
  <div class="orb orb-1"></div>
  <div class="orb orb-2"></div>
  <div class="orb orb-3"></div>
</div>
<div class="grid-overlay"></div>

<!-- NAV -->
<nav>
  <div class="wrap">
    <div class="nav-inner">
      <a href="#" class="logo">
        <div class="logo-icon"><i class="fas fa-shield-halved"></i></div>
        SecureShare
      </a>
      <div class="nav-links">
        <a href="#features" class="nav-link">Features</a>
        <a href="#how" class="nav-link">How it works</a>
        <a href="#" class="nav-link">Docs</a>
      </div>
      <a href="{{ url_for('upload_page') }}" class="nav-cta">Send a File →</a>
    </div>
  </div>
</nav>

<!-- HERO -->
<div class="wrap">
  <div class="hero">
    <div class="hero-badge">
      <span class="badge-dot"></span>
      End-to-end encrypted
    </div>

    <h1>Transfer files with<br><span class="highlight">zero compromise.</span></h1>

    <p class="hero-sub">
      Drop any file. Generate a secure code. Share it. Files vanish after 24 hours — leaving no trace behind.
    </p>

    <div class="hero-actions">
      <a href="{{ url_for('upload_page') }}" class="btn btn-send">
        <i class="fas fa-arrow-up-from-bracket"></i> Send a File
      </a>
      <a href="{{ url_for('enter_code') }}" class="btn btn-receive">
        <i class="fas fa-key"></i> Enter Code
      </a>
      <a href="#how" class="btn btn-ghost">
        <i class="fas fa-play-circle"></i> See how it works
      </a>
    </div>

    <div class="trust-bar">
      <div class="trust-item"><i class="fas fa-lock"></i> AES-256 encrypted</div>
      <div class="trust-item"><i class="fas fa-clock"></i> Auto-delete in 24h</div>
      <div class="trust-item"><i class="fas fa-eye-slash"></i> No account needed</div>
      <div class="trust-item"><i class="fas fa-server"></i> No data retained</div>
    </div>
  </div>

  <!-- DEMO CARD -->
  <div class="demo-section reveal">
    <div class="demo-card">
      <div class="drop-zone" id="dropZone">
        <i class="fas fa-cloud-arrow-up drop-icon"></i>
        <div class="drop-title">Drag & drop your file here</div>
        <p class="drop-sub">or <span onclick="document.getElementById('fileInput').click()">browse files</span> — up to 2GB</p>
        <input type="file" id="fileInput" style="display:none" onchange="startFakeUpload(this)">
      </div>
      <div class="progress-bar-wrap" id="progressWrap">
        <div class="progress-label">
          <span id="fileName">document.pdf</span>
          <span id="progressPct">0%</span>
        </div>
        <div class="progress-track">
          <div class="progress-fill" id="progressFill"></div>
        </div>
      </div>
      <div class="demo-footer">
        <div class="expire-badge">
          <i class="fas fa-hourglass-half"></i>
          Expires after 24 hours
        </div>
        <button class="demo-send-btn" onclick="document.getElementById('fileInput').click()">
          <i class="fas fa-paper-plane"></i> Generate Link
        </button>
      </div>
    </div>
  </div>

  <!-- STATS -->
  <div class="stats reveal reveal-delay-1">
    <div class="stat">
      <div class="stat-num">2M+</div>
      <div class="stat-label">Files transferred</div>
    </div>
    <div class="stat">
      <div class="stat-num">99.9%</div>
      <div class="stat-label">Uptime guaranteed</div>
    </div>
    <div class="stat">
      <div class="stat-num">0</div>
      <div class="stat-label">Data breaches ever</div>
    </div>
  </div>

  <!-- FEATURES -->
  <div class="features-section" id="features">
    <div class="features-header reveal">
      <div class="section-label">Why SecureShare</div>
      <div class="section-title">Privacy isn't optional.</div>
      <p class="section-desc">Every feature is built around one principle: your files belong to you and no one else.</p>
    </div>
    <div class="features-grid">
      <div class="feat-card reveal reveal-delay-1">
        <div class="feat-icon feat-icon-cyan"><i class="fas fa-lock"></i></div>
        <div class="feat-title">Military-grade Encryption</div>
        <p class="feat-text">Files are encrypted with AES-256 before they ever leave your device. Even we can't read them.</p>
        <span class="feat-tag tag-cyan">AES-256</span>
      </div>
      <div class="feat-card reveal reveal-delay-2">
        <div class="feat-icon feat-icon-violet"><i class="fas fa-bolt"></i></div>
        <div class="feat-title">Instant Transfers</div>
        <p class="feat-text">Powered by edge infrastructure worldwide. Files reach their destination at the speed of light.</p>
        <span class="feat-tag tag-violet">Global CDN</span>
      </div>
      <div class="feat-card reveal reveal-delay-3">
        <div class="feat-icon feat-icon-green"><i class="fas fa-clock-rotate-left"></i></div>
        <div class="feat-title">Auto Expiry</div>
        <p class="feat-text">Files are automatically and permanently deleted after 24 hours. No lingering traces, no recovery.</p>
        <span class="feat-tag tag-green">24h TTL</span>
      </div>
      <div class="feat-card reveal reveal-delay-4">
        <div class="feat-icon feat-icon-rose"><i class="fas fa-mobile-screen"></i></div>
        <div class="feat-title">Any Device</div>
        <p class="feat-text">No app install required. Works on every browser, phone, tablet, and desktop out of the box.</p>
        <span class="feat-tag tag-rose">Web-native</span>
      </div>
    </div>
  </div>

  <!-- HOW IT WORKS -->
  <div class="how-section" id="how">
    <div class="reveal">
      <div class="section-label">How it works</div>
      <div class="section-title">Three steps.<br>That's it.</div>
    </div>
    <div class="steps">
      <div class="step reveal reveal-delay-1">
        <div class="step-num" data-n="1">UPLOAD</div>
        <div class="step-title">Drop your file</div>
        <p class="step-text">Drag and drop any file up to 2GB. Your file is encrypted instantly the moment it's selected.</p>
      </div>
      <div class="step reveal reveal-delay-2">
        <div class="step-num" data-n="2">SHARE</div>
        <div class="step-title">Get your code</div>
        <p class="step-text">Receive a unique 6-digit code or shareable link. Send it to your recipient via any channel.</p>
      </div>
      <div class="step reveal reveal-delay-3">
        <div class="step-num" data-n="3">RECEIVE</div>
        <div class="step-title">Download securely</div>
        <p class="step-text">The recipient enters the code and downloads the file. After 24 hours, everything is gone.</p>
      </div>
    </div>
  </div>

  <!-- CTA -->
  <div class="cta-section reveal">
    <div class="cta-box">
      <h2>Ready to send something?</h2>
      <p>No account. No tracking. No compromises. Start transferring in seconds.</p>
      <div class="cta-buttons">
        <a href="{{ url_for('upload_page') }}" class="btn btn-send">
          <i class="fas fa-arrow-up-from-bracket"></i> Send a File Now
        </a>
        <a href="{{ url_for('enter_code') }}" class="btn btn-receive">
          <i class="fas fa-key"></i> I Have a Code
        </a>
      </div>
    </div>
  </div>

</div>

<!-- FOOTER -->
<footer>
  <div class="wrap">
    <div class="footer-inner">
      <div class="footer-copy">© 2026 SecureShare — All rights reserved.</div>
      <div class="footer-links">
        <a href="#" class="footer-link">Privacy</a>
        <a href="#" class="footer-link">Terms</a>
        <a href="#" class="footer-link">Contact</a>
      </div>
    </div>
  </div>
</footer>

<script>
/* ── DRAG & DROP ── */
const dz = document.getElementById('dropZone');
dz.addEventListener('dragover', e => { e.preventDefault(); dz.classList.add('drag-over'); });
dz.addEventListener('dragleave', () => dz.classList.remove('drag-over'));
dz.addEventListener('drop', e => {
  e.preventDefault();
  dz.classList.remove('drag-over');
  if (e.dataTransfer.files.length) startFakeUpload({ files: e.dataTransfer.files });
});

/* ── FAKE UPLOAD PROGRESS ── */
function startFakeUpload(input) {
  const file = input.files[0];
  if (!file) return;
  const wrap = document.getElementById('progressWrap');
  const fill = document.getElementById('progressFill');
  const pct  = document.getElementById('progressPct');
  const fn   = document.getElementById('fileName');
  fn.textContent = file.name.length > 28 ? file.name.substring(0,25)+'...' : file.name;
  wrap.style.display = 'block';
  let p = 0;
  const iv = setInterval(() => {
    p += Math.random() * 14 + 4;
    if (p >= 100) { p = 100; clearInterval(iv); }
    fill.style.width = p + '%';
    pct.textContent  = Math.floor(p) + '%';
  }, 150);
}

/* ── SCROLL REVEAL ── */
const observer = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
</script>
</body>
</html>

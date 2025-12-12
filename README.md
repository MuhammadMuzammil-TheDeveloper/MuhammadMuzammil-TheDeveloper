<!--
────────────────────────────────────────────────────────────────────────────
   ✦ MUHAMMAD MUZAMMIL — FRONTEND WEB DEVELOPER ✦
   Ultra-professional, animated, website-style README (SVG-only, no GIFs)
────────────────────────────────────────────────────────────────────────────
-->

<div align="center">

<!-- ───────────────────────────── HERO (Animated Typing SVG) ───────────────────────────── -->
<svg width="920" height="240" viewBox="0 0 920 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Hero: Muhammad Muzammil — Frontend Web Developer">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="50%" stop-color="#7C4DFF"/>
      <stop offset="100%" stop-color="#00FFA3"/>
    </linearGradient>

    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Typing mask: animated reveal width -->
    <mask id="typingMask">
      <rect x="0" y="0" width="0" height="240" fill="#fff">
        <animate attributeName="width" values="0;860;860;0" keyTimes="0;0.55;0.85;1" dur="6.5s" repeatCount="indefinite"/>
      </rect>
    </mask>

    <!-- Cursor blink -->
    <g id="cursor">
      <rect x="0" y="0" width="10" height="34" rx="2" fill="#00E5FF">
        <animate attributeName="opacity" values="1;0;1" dur="0.9s" repeatCount="indefinite"/>
      </rect>
    </g>
  </defs>

  <!-- Background -->
  <rect x="10" y="10" width="900" height="220" rx="22" fill="#0B1020"/>
  <rect x="10" y="10" width="900" height="220" rx="22" fill="url(#g)" opacity="0.08"/>

  <!-- Top neon line -->
  <path d="M40 55 H880" stroke="url(#g)" stroke-width="2" opacity="0.9">
    <animate attributeName="opacity" values="0.35;1;0.35" dur="3.6s" repeatCount="indefinite"/>
  </path>

  <!-- Name -->
  <text x="60" y="110" font-family="ui-sans-serif, system-ui, Segoe UI, Arial" font-size="44" font-weight="800" fill="url(#g)" filter="url(#glow)">
    Muhammad Muzammil
  </text>

  <!-- Role pill -->
  <g>
    <rect x="60" y="128" width="330" height="36" rx="18" fill="#0D1633" stroke="url(#g)" opacity="0.95"/>
    <text x="78" y="152" font-family="ui-sans-serif, system-ui, Segoe UI, Arial" font-size="16" font-weight="700" fill="#CFE8FF">
      Frontend Web Developer
    </text>
  </g>

  <!-- Animated typing line -->
  <g mask="url(#typingMask)">
    <text x="60" y="196" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
          font-size="20" fill="#E6F6FF" opacity="0.95">
      Building modern UI • React • Tailwind • Performance • UX-first
    </text>
  </g>

  <!-- Cursor follows the “typing” -->
  <g transform="translate(60, 172)">
    <g>
      <animateTransform attributeName="transform" type="translate"
        values="60 172; 860 172; 860 172; 60 172"
        keyTimes="0;0.55;0.85;1" dur="6.5s" repeatCount="indefinite"/>
      <use href="#cursor"/>
    </g>
  </g>

  <!-- Subtle particles -->
  <g opacity="0.55">
    <circle cx="810" cy="72" r="2" fill="#00E5FF">
      <animate attributeName="cy" values="72;66;72" dur="2.2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="846" cy="96" r="2" fill="#7C4DFF">
      <animate attributeName="cy" values="96;90;96" dur="2.7s" repeatCount="indefinite"/>
    </circle>
    <circle cx="875" cy="78" r="2" fill="#00FFA3">
      <animate attributeName="cy" values="78;72;78" dur="3.1s" repeatCount="indefinite"/>
    </circle>
  </g>
</svg>

<br/>

<!-- Minimal nav -->
<p>
  <a href="#about">About</a> ·
  <a href="#achievements">Achievements</a> ·
  <a href="#skills">Skills</a> ·
  <a href="#projects">Projects</a> ·
  <a href="#stats">Stats</a> ·
  <a href="#contact">Contact</a>
</p>

<!-- SVG divider -->
<svg width="920" height="28" viewBox="0 0 920 28" xmlns="http://www.w3.org/2000/svg" aria-label="divider">
  <defs>
    <linearGradient id="d1" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#00E5FF"/>
      <stop offset="0.5" stop-color="#7C4DFF"/>
      <stop offset="1" stop-color="#00FFA3"/>
    </linearGradient>
  </defs>
  <path d="M20 14 H900" stroke="url(#d1)" stroke-width="2" opacity="0.9"/>
  <circle cx="460" cy="14" r="4" fill="url(#d1)">
    <animate attributeName="r" values="3;5;3" dur="1.8s" repeatCount="indefinite"/>
  </circle>
</svg>

</div>

---

## <a id="about"></a>✨ About Me — *Animated Reveal*

<!-- Animated reveal panel -->
<svg width="920" height="170" viewBox="0 0 920 170" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="About: Animated text reveal">
  <defs>
    <linearGradient id="g2" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="55%" stop-color="#7C4DFF"/>
      <stop offset="100%" stop-color="#00FFA3"/>
    </linearGradient>
    <filter id="softGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="4" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <mask id="reveal">
      <rect x="0" y="0" width="0" height="170" fill="#fff">
        <animate attributeName="width" values="0;920" dur="1.35s" repeatCount="1" fill="freeze"/>
      </rect>
    </mask>
  </defs>

  <rect x="10" y="10" width="900" height="150" rx="18" fill="#0B1020"/>
  <rect x="10" y="10" width="900" height="150" rx="18" fill="url(#g2)" opacity="0.06"/>

  <g mask="url(#reveal)">
    <text x="40" y="58" font-family="ui-sans-serif, system-ui, Segoe UI, Arial" font-size="18" fill="#EAF7FF">
      I’m <tspan font-weight="800" fill="url(#g2)" filter="url(#softGlow)">Muhammad Muzammil</tspan> — a frontend developer focused on
    </text>
    <text x="40" y="86" font-family="ui-sans-serif, system-ui, Segoe UI, Arial" font-size="18" fill="#EAF7FF">
      crafting <tspan font-weight="800">fast</tspan>, <tspan font-weight="800">responsive</tspan>, and <tspan font-weight="800">polished</tspan> web experiences.
    </text>
    <text x="40" y="114" font-family="ui-sans-serif, system-ui, Segoe UI, Arial" font-size="18" fill="#EAF7FF">
      I care about <tspan font-weight="800">UX</tspan>, <tspan font-weight="800">performance</tspan>, and <tspan font-weight="800">clean architecture</tspan>.
    </text>

    <!-- subtle animated accent -->
    <path d="M40 132 H320" stroke="url(#g2)" stroke-width="2" opacity="0.85">
      <animate attributeName="opacity" values="0.3;1;0.3" dur="2.8s" repeatCount="indefinite"/>
    </path>
  </g>
</svg>

---

## <a id="achievements"></a>🏆 Achievements

- **2× Hackathon Champion**
  - **🥇 SMIT Hackathon — Winner**
  - **🥇 CodEung2025 Hackathon — Winner**

---

## <a id="skills"></a>🧠 Skills — *Neon Skill Chips (SVG Icons)*

<div align="center">

<svg width="920" height="210" viewBox="0 0 920 210" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Skills: HTML, CSS, JavaScript, React, Tailwind, Bootstrap, Git, Python, C, C#, UI/UX">
  <defs>
    <linearGradient id="chip" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="50%" stop-color="#7C4DFF"/>
      <stop offset="100%" stop-color="#00FFA3"/>
    </linearGradient>
    <filter id="chipGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="bb"/>
      <feMerge>
        <feMergeNode in="bb"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- tiny animated icon -->
    <g id="dotIcon">
      <circle cx="10" cy="10" r="6" fill="url(#chip)" filter="url(#chipGlow)">
        <animate attributeName="r" values="5;7;5" dur="1.8s" repeatCount="indefinite"/>
      </circle>
    </g>

    <!-- Skill chip template -->
    <g id="skillChip">
      <rect x="0" y="0" width="170" height="40" rx="20" fill="#0B1020" stroke="url(#chip)" opacity="0.95"/>
      <rect x="0" y="0" width="170" height="40" rx="20" fill="url(#chip)" opacity="0.06"/>
    </g>
  </defs>

  <rect x="10" y="10" width="900" height="190" rx="18" fill="#0B1020"/>
  <rect x="10" y="10" width="900" height="190" rx="18" fill="url(#chip)" opacity="0.04"/>

  <!-- Row 1 -->
  <g transform="translate(40,40)">
    <g transform="translate(0,0)">
      <use href="#skillChip"/>
      <use href="#dotIcon" x="14" y="10"/>
      <text x="40" y="26" font-family="ui-sans-serif, system-ui, Segoe UI, Arial" font-size="14" font-weight="800" fill="#EAF7FF">HTML</text>
    </g>
    <g transform="translate(190,0)">
      <use href="#skillChip"/>
      <use href="#dotIcon" x="14" y="10"/>
      <text x="40" y="26" font-family="ui-sans-serif, system-ui, Segoe UI, Arial" font-size="14" font-weight="800" fill="#EAF7FF">CSS</text>
    </g>
    <g transform="translate(380,0)">
      <use href="#skillChip"/>
      <use href="#dotIcon" x="14" y="10"/>
      <text x="40" y="26" font-family="ui-sans-serif, system-ui, Segoe UI, Arial" font-size="14" font-weight="800" fill="#EAF7FF">JavaScript</text>
    </g>
    <g transform="translate(570,0)">
      <use href="#skillChip"/>
      <use href="#dotIcon" x="14" y="10"/>
      <text x="40" y="26" font-family="ui-sans-serif, system-ui, Segoe UI, Arial" font-size="14" font-weight="800" fill="#EAF7FF">React</text>
    </g>
    <g transform="translate(760,0)">
      <use href="#skillChip"/>
      <use href="#dotIcon" x="14" y="10"/>
      <text x="40" y="26" font-family="ui-sans-serif, system-ui, Segoe UI, Arial" font-size="14" font-weight="800" fill="#EAF7FF">Tailwind</text>
    </g>
  </g>

  <!-- Row 2 -->
  <g transform="translate(40,95)">
    <g transform="translate(0,0)">
      <use href="#skillChip"/>
      <use href="#dotIcon" x="14" y="10"/>
      <text x="40" y="26" font-family="ui-sans-serif, system-ui, Segoe UI, Arial" font-size="14" font-weight="800" fill="#EAF7FF">Bootstrap</text>
    </g>
    <g transform="translate(190,0)">
      <use href="#skillChip"/>
      <use href="#dotIcon" x="14" y="10"/>
      <text x="40" y="26" font-family="ui-sans-serif, system-ui, Segoe UI, Arial" font-size="14" font-weight="800" fill="#EAF7FF">Git</text>
    </g>
    <g transform="translate(380,0)">
      <use href="#skillChip"/>
      <use href="#dotIcon" x="14" y="10"/>
      <text x="40" y="26" font-family="ui-sans-serif, system-ui, Segoe UI, Arial" font-size="14" font-weight="800" fill="#EAF7FF">Python</text>
    </g>
    <g transform="translate(570,0)">
      <use href="#skillChip"/>
      <use href="#dotIcon" x="14" y="10"/>
      <text x="40" y="26" font-family="ui-sans-serif, system-ui, Segoe UI, Arial" font-size="14" font-weight="800" fill="#EAF7FF">C</text>
    </g>
    <g transform="translate(760,0)">
      <use href="#skillChip"/>
      <use href="#dotIcon" x="14" y="10"/>
      <text x="40" y="26" font-family="ui-sans-serif, system-ui, Segoe UI, Arial" font-size="14" font-weight="800" fill="#EAF7FF">C#</text>
    </g>
  </g>

  <!-- Row 3 -->
  <g transform="translate(40,150)">
    <g transform="translate(0,0)">
      <use href="#skillChip"/>
      <use href="#dotIcon" x="14" y="10"/>
      <text x="40" y="26" font-family="ui-sans-serif, system-ui, Segoe UI, Arial" font-size="14" font-weight="800" fill="#EAF7FF">UI / UX</text>
    </g>
    <text x="230" y="26" font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
          font-size="13" fill="#A9C7D9" opacity="0.9">
      ✦ Minimal UI · Motion · Accessibility · Component Systems · Performance
      <animate attributeName="opacity" values="0.55;1;0.55" dur="3.2s" repeatCount="indefinite"/>
    </text>
  </g>
</svg>

</div>

---

## <a id="projects"></a>🧩 Projects — *Website-Style Grid*

> Replace the links + titles with your real best projects (2–6). The layout is “premium landing page” style.


| 🚀 Project Card | Description | Stack | Links |
|---|---|---|---|
| **🧠 Neon UI Dashboard** | Futuristic admin UI with responsive layout + smooth micro-interactions. | React • Tailwind | 🔗 Live • 📦 Repo |
| **⚡ Performance Landing Page** | Lighthouse-focused landing page with optimized assets and animations. | HTML • CSS • JS | 🔗 Live • 📦 Repo |
| **🛒 Modern E-Commerce UI** | Product grid, filters, cart UX — clean, fast, scalable components. | React • Bootstrap | 🔗 Live • 📦 Repo |
| **🎨 UI/UX Component Kit** | Reusable components + design consistency for rapid builds. | UI/UX • Figma • CSS | 🔗 Live • 📦 Repo |

---

## <a id="stats"></a>📊 GitHub Stats — *SVG Services (No GIFs / No Photos)*

<div align="center">

<!-- GitHub Readme Stats (SVG) -->
<img
  alt="GitHub Stats"
  src="https://github-readme-stats.vercel.app/api?username=MuhammadMuzammil-TheDeveloper&show_icons=true&hide_border=true&bg_color=0B1020&title_color=00E5FF&text_color=EAF7FF&icon_color=00FFA3"
  height="165"
/>

<img
  alt="Top Languages"
  src="https://github-readme-stats.vercel.app/api/top-langs/?username=MuhammadMuzammil-TheDeveloper&layout=compact&hide_border=true&bg_color=0B1020&title_color=7C4DFF&text_color=EAF7FF"
  height="165"
/>

</div>

---

## 🔥 Contribution Streak — *SVG*

<div align="center">

<img
  alt="GitHub Streak"
  src="https://streak-stats.demolab.com?user=MuhammadMuzammil-TheDeveloper&hide_border=true&background=0B1020&ring=00E5FF&fire=00FFA3&currStreakLabel=EAF7FF&sideLabels=EAF7FF&dates=A9C7D9"
  height="180"
/>

</div>

---

## <a id="contact"></a>📬 Contact — *Animated SVG Buttons*

<div align="center">

<!-- Buttons are SVG-only (animated) + clickable -->
<a href="mailto:muhammadmuzammil.thedeveloper@gmail.com" title="Email">
  <svg width="220" height="52" viewBox="0 0 220 52" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Email button">
    <defs>
      <linearGradient id="btn1" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#00E5FF"/>
        <stop offset="100%" stop-color="#00FFA3"/>
      </linearGradient>
    </defs>
    <rect x="1" y="1" width="218" height="50" rx="14" fill="#0B1020" stroke="url(#btn1)" stroke-width="2"/>
    <rect x="1" y="1" width="218" height="50" rx="14" fill="url(#btn1)" opacity="0.10">
      <animate attributeName="opacity" values="0.06;0.18;0.06" dur="2.4s" repeatCount="indefinite"/>
    </rect>
    <text x="110" y="33" text-anchor="middle" font-family="ui-sans-serif, system-ui, Segoe UI, Arial" font-size="14" font-weight="800" fill="#EAF7FF">
      ✉️ Email Me
    </text>
  </svg>
</a>

<a href="https://muhammad-muzammil.netlify.app/" title="Portfolio">
  <svg width="220" height="52" viewBox="0 0 220 52" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Portfolio button">
    <defs>
      <linearGradient id="btn2" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#7C4DFF"/>
        <stop offset="100%" stop-color="#00E5FF"/>
      </linearGradient>
    </defs>
    <rect x="1" y="1" width="218" height="50" rx="14" fill="#0B1020" stroke="url(#btn2)" stroke-width="2"/>
    <rect x="1" y="1" width="218" height="50" rx="14" fill="url(#btn2)" opacity="0.10">
      <animate attributeName="opacity" values="0.06;0.18;0.06" dur="2.1s" repeatCount="indefinite"/>
    </rect>
    <text x="110" y="33" text-anchor="middle" font-family="ui-sans-serif, system-ui, Segoe UI, Arial" font-size="14" font-weight="800" fill="#EAF7FF">
      🌐 Portfolio
    </text>
  </svg>
</a>

<br/>

<a href="https://www.linkedin.com/in/muhammad-muzammil-7562bb316/" title="LinkedIn">
  <svg width="220" height="52" viewBox="0 0 220 52" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="LinkedIn button">
    <defs>
      <linearGradient id="btn3" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#00FFA3"/>
        <stop offset="100%" stop-color="#7C4DFF"/>
      </linearGradient>
    </defs>
    <rect x="1" y="1" width="218" height="50" rx="14" fill="#0B1020" stroke="url(#btn3)" stroke-width="2"/>
    <rect x="1" y="1" width="218" height="50" rx="14" fill="url(#btn3)" opacity="0.10">
      <animate attributeName="opacity" values="0.06;0.18;0.06" dur="2.7s" repeatCount="indefinite"/>
    </rect>
    <text x="110" y="33" text-anchor="middle" font-family="ui-sans-serif, system-ui, Segoe UI, Arial" font-size="14" font-weight="800" fill="#EAF7FF">
      💼 LinkedIn
    </text>
  </svg>
</a>

<a href="https://github.com/MuhammadMuzammil-TheDeveloper" title="GitHub">
  <svg width="220" height="52" viewBox="0 0 220 52" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="GitHub button">
    <defs>
      <linearGradient id="btn4" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#00E5FF"/>
        <stop offset="100%" stop-color="#7C4DFF"/>
      </linearGradient>
    </defs>
    <rect x="1" y="1" width="218" height="50" rx="14" fill="#0B1020" stroke="url(#btn4)" stroke-width="2"/>
    <rect x="1" y="1" width="218" height="50" rx="14" fill="url(#btn4)" opacity="0.10">
      <animate attributeName="opacity" values="0.06;0.18;0.06" dur="2.3s" repeatCount="indefinite"/>
    </rect>
    <text x="110" y="33" text-anchor="middle" font-family="ui-sans-serif, system-ui, Segoe UI, Arial" font-size="14" font-weight="800" fill="#EAF7FF">
      🧩 GitHub
    </text>
  </svg>
</a>

<br/>

<a href="https://www.instagram.com/muzammil_techteasure1" title="Instagram">
  <svg width="220" height="52" viewBox="0 0 220 52" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Instagram button">
    <defs>
      <linearGradient id="btn5" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#7C4DFF"/>
        <stop offset="100%" stop-color="#00FFA3"/>
      </linearGradient>
    </defs>
    <rect x="1" y="1" width="218" height="50" rx="14" fill="#0B1020" stroke="url(#btn5)" stroke-width="2"/>
    <rect x="1" y="1" width="218" height="50" rx="14" fill="url(#btn5)" opacity="0.10">
      <animate attributeName="opacity" values="0.06;0.18;0.06" dur="2.6s" repeatCount="indefinite"/>
    </rect>
    <text x="110" y="33" text-anchor="middle" font-family="ui-sans-serif, system-ui, Segoe UI, Arial" font-size="14" font-weight="800" fill="#EAF7FF">
      📸 Instagram
    </text>
  </svg>
</a>

<a href="https://www.youtube.com/@muzans786" title="YouTube">
  <svg width="220" height="52" viewBox="0 0 220 52" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="YouTube button">
    <defs>
      <linearGradient id="btn6" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#00FFA3"/>
        <stop offset="100%" stop-color="#00E5FF"/>
      </linearGradient>
    </defs>
    <rect x="1" y="1" width="218" height="50" rx="14" fill="#0B1020" stroke="url(#btn6)" stroke-width="2"/>
    <rect x="1" y="1" width="218" height="50" rx="14" fill="url(#btn6)" opacity="0.10">
      <animate attributeName="opacity" values="0.06;0.18;0.06" dur="2.0s" repeatCount="indefinite"/>
    </rect>
    <text x="110" y="33" text-anchor="middle" font-family="ui-sans-serif, system-ui, Segoe UI, Arial" font-size="14" font-weight="800" fill="#EAF7FF">
      ▶️ YouTube
    </text>
  </svg>
</a>

</div>

---

## 🌊 Footer — *Waving SVG Animation*

<div align="center">

<svg width="920" height="120" viewBox="0 0 920 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Waving footer">
  <defs>
    <linearGradient id="waveG" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="50%" stop-color="#7C4DFF"/>
      <stop offset="100%" stop-color="#00FFA3"/>
    </linearGradient>
  </defs>

  <rect width="920" height="120" fill="#0B1020"/>

  <path fill="url(#waveG)" opacity="0.25">
    <animate attributeName="d" dur="6s" repeatCount="indefinite"
      values="
        M0,70 C120,90 240,50 360,70 C480,90 600,50 720,70 C840,90 920,70 920,70 L920,120 L0,120 Z;
        M0,70 C120,50 240,90 360,70 C480,50 600,90 720,70 C840,50 920,70 920,70 L920,120 L0,120 Z;
        M0,70 C120,90 240,50 360,70 C480,90 600,50 720,70 C840,90 920,70 920,70 L920,120 L0,120 Z
      "/>
  </path>

  <path fill="url(#waveG)" opacity="0.40">
    <animate attributeName="d" dur="5s" repeatCount="indefinite"
      values="
        M0,82 C150,102 300,62 450,82 C600,102 750,62 900,82 L920,120 L0,120 Z;
        M0,82 C150,62 300,102 450,82 C600,62 750,102 900,82 L920,120 L0,120 Z;
        M0,82 C150,102 300,62 450,82 C600,102 750,62 900,82 L920,120 L0,120 Z
      "/>
  </path>

  <text x="460" y="42" text-anchor="middle"
        font-family="ui-sans-serif, system-ui, Segoe UI, Arial"
        font-size="14" font-weight="800" fill="#EAF7FF" opacity="0.92">
    ✦ Muhammad Muzammil • Frontend Web Developer • 2× Hackathon Champion ✦
    <animate attributeName="opacity" values="0.55;1;0.55" dur="3.2s" repeatCount="indefinite"/>
  </text>
</svg>

</div>

<!-- End -->

from datetime import datetime, timezone, timedelta

# Horário de Brasília
brt = timezone(timedelta(hours=-3))
hora = datetime.now(brt).hour

if 5 <= hora < 12:
    periodo = "Bom dia"
    emoji = "&#x1F305;"
    cor_destaque = "#4fc3f7"
    cor_bar = "#4fc3f7"
    cor_dot = "#4fc3f7"
    descricao = "Comecando mais um dia de codigo..."
elif 12 <= hora < 18:
    periodo = "Boa tarde"
    emoji = "&#x2600;&#xFE0F;"
    cor_destaque = "#A78BFA"
    cor_bar = "#7C3AED"
    cor_dot = "#A78BFA"
    descricao = "No flow, construindo coisas."
elif 18 <= hora < 22:
    periodo = "Boa noite"
    emoji = "&#x1F306;"
    cor_destaque = "#c084fc"
    cor_bar = "#9333ea"
    cor_dot = "#c084fc"
    descricao = "Noite boa para resolver problemas."
else:
    periodo = "Ainda acordado"
    emoji = "&#x1F319;"
    cor_destaque = "#34d399"
    cor_bar = "#10b981"
    cor_dot = "#34d399"
    descricao = "Madrugada. O melhor horario para codar."

svg = f'''<svg width="860" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#0d1117"/>
      <stop offset="100%" style="stop-color:#161b22"/>
    </linearGradient>
    <style>
      .bg {{ fill: url(#bgGrad); }}
      .grid-line {{ stroke: #21262d; stroke-width: 0.5; }}
      .name {{
        font-family: "Fira Code", monospace;
        font-size: 32px;
        font-weight: 700;
        fill: #ffffff;
        opacity: 0;
        animation: fadeSlideIn 0.8s ease forwards;
        animation-delay: 0.3s;
      }}
      .cursor {{
        fill: {cor_destaque};
        animation: blink 1s step-end infinite;
      }}
      .tag {{
        font-family: "Fira Code", monospace;
        font-size: 12px;
        fill: {cor_destaque};
        opacity: 0;
        animation: fadeIn 0.5s ease forwards;
      }}
      .tag-1 {{ animation-delay: 1.0s; }}
      .tag-2 {{ animation-delay: 1.3s; }}
      .tag-3 {{ animation-delay: 1.6s; }}
      .tag-4 {{ animation-delay: 1.9s; }}
      .bar-fill {{
        fill: {cor_bar};
        transform-origin: left;
        animation: growBar 1.2s ease forwards;
        transform: scaleX(0);
      }}
      .bar-1 {{ animation-delay: 1.1s; }}
      .bar-2 {{ animation-delay: 1.4s; }}
      .bar-3 {{ animation-delay: 1.7s; }}
      .bar-4 {{ animation-delay: 2.0s; }}
      .bar-5 {{ animation-delay: 2.3s; }}
      .bar-label {{
        font-family: "Fira Code", monospace;
        font-size: 11px;
        fill: #8b949e;
        opacity: 0;
        animation: fadeIn 0.4s ease forwards;
      }}
      .bl-1 {{ animation-delay: 1.1s; }}
      .bl-2 {{ animation-delay: 1.4s; }}
      .bl-3 {{ animation-delay: 1.7s; }}
      .bl-4 {{ animation-delay: 2.0s; }}
      .bl-5 {{ animation-delay: 2.3s; }}
      .dot {{
        fill: {cor_dot};
        opacity: 0;
        animation: popIn 0.4s ease forwards;
      }}
      .dot-1 {{ animation-delay: 1.0s; }}
      .dot-2 {{ animation-delay: 1.3s; }}
      .dot-3 {{ animation-delay: 1.6s; }}
      .dot-4 {{ animation-delay: 1.9s; }}
      .subtitle {{
        font-family: "Fira Code", monospace;
        font-size: 12px;
        fill: #8b949e;
        opacity: 0;
        animation: fadeIn 0.8s ease forwards;
        animation-delay: 0.8s;
      }}
      .prompt {{
        font-family: "Fira Code", monospace;
        font-size: 12px;
        fill: #3fb950;
        opacity: 0;
        animation: fadeIn 0.5s ease forwards;
        animation-delay: 0.5s;
      }}
      .greeting {{
        font-family: "Fira Code", monospace;
        font-size: 13px;
        fill: {cor_destaque};
        opacity: 0;
        animation: fadeIn 0.5s ease forwards;
        animation-delay: 0.1s;
      }}
      .divider {{
        stroke: #30363d;
        stroke-width: 1;
        opacity: 0;
        animation: fadeIn 0.5s ease forwards;
        animation-delay: 0.8s;
      }}
      @keyframes fadeSlideIn {{
        from {{ opacity: 0; transform: translateY(8px); }}
        to   {{ opacity: 1; transform: translateY(0); }}
      }}
      @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to   {{ opacity: 1; }}
      }}
      @keyframes blink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}
      @keyframes growBar {{
        from {{ transform: scaleX(0); }}
        to   {{ transform: scaleX(1); }}
      }}
      @keyframes popIn {{
        0%   {{ opacity: 0; transform: scale(0); }}
        70%  {{ transform: scale(1.3); }}
        100% {{ opacity: 1; transform: scale(1); }}
      }}
    </style>
  </defs>

  <rect width="860" height="200" class="bg" rx="12"/>

  <line x1="0" y1="50" x2="860" y2="50" class="grid-line"/>
  <line x1="0" y1="100" x2="860" y2="100" class="grid-line"/>
  <line x1="0" y1="150" x2="860" y2="150" class="grid-line"/>
  <line x1="210" y1="0" x2="210" y2="200" class="grid-line"/>

  <text x="24" y="30" class="greeting">{emoji}  {periodo}, visitante!</text>
  <text x="24" y="50" class="prompt">~/pedropaulucci27 $</text>
  <text x="24" y="82" class="name">Pedro Paulucci</text>
  <rect x="212" y="64" width="10" height="22" class="cursor"/>
  <text x="24" y="105" class="subtitle">Software Eng. + Data Science &amp; AI</text>
  <text x="24" y="120" class="subtitle">{descricao}</text>
  <text x="24" y="135" class="subtitle">Ibmec BH · Ibtech · BH</text>

  <line x1="24" y1="148" x2="190" y2="148" class="divider"/>

  <circle cx="32" cy="163" r="4" class="dot dot-1"/>
  <text x="42" y="167" class="tag tag-1">Data Science</text>
  <circle cx="32" cy="180" r="4" class="dot dot-2"/>
  <text x="42" y="184" class="tag tag-2">Web Dev</text>
  <circle cx="120" cy="163" r="4" class="dot dot-3"/>
  <text x="130" y="167" class="tag tag-3">Java &amp; OOP</text>
  <circle cx="120" cy="180" r="4" class="dot dot-4"/>
  <text x="130" y="184" class="tag tag-4">Node &amp; Express</text>

  <line x1="210" y1="20" x2="210" y2="185" class="divider"/>

  <text x="228" y="35" class="prompt">skills.json</text>

  <text x="228" y="62" class="bar-label bl-1">JavaScript</text>
  <rect x="318" y="52" width="510" height="9" rx="4" fill="#21262d"/>
  <rect x="318" y="52" width="459" height="9" rx="4" class="bar-fill bar-1"/>

  <text x="228" y="87" class="bar-label bl-2">Python</text>
  <rect x="318" y="77" width="510" height="9" rx="4" fill="#21262d"/>
  <rect x="318" y="77" width="357" height="9" rx="4" class="bar-fill bar-2"/>

  <text x="228" y="112" class="bar-label bl-3">Java</text>
  <rect x="318" y="102" width="510" height="9" rx="4" fill="#21262d"/>
  <rect x="318" y="102" width="306" height="9" rx="4" class="bar-fill bar-3"/>

  <text x="228" y="137" class="bar-label bl-4">C</text>
  <rect x="318" y="127" width="510" height="9" rx="4" fill="#21262d"/>
  <rect x="318" y="127" width="255" height="9" rx="4" class="bar-fill bar-4"/>

  <text x="228" y="162" class="bar-label bl-5">Node.js</text>
  <rect x="318" y="152" width="510" height="9" rx="4" fill="#21262d"/>
  <rect x="318" y="152" width="204" height="9" rx="4" class="bar-fill bar-5"/>

</svg>'''

with open("profile_animation.svg", "w") as f:
    f.write(svg)

print(f"SVG gerado! Periodo: {periodo} ({hora}h)")

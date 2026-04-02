from datetime import datetime, timezone, timedelta

brt = timezone(timedelta(hours=-3))
hora = datetime.now(brt).hour

if 5 <= hora < 12:
    periodo = "Bom dia"
    emoji = "&#x1F305;"
    cor1 = "#4fc3f7"
    cor2 = "#0ea5e9"
    descricao = "Comecando mais um dia de codigo..."
elif 12 <= hora < 18:
    periodo = "Boa tarde"
    emoji = "&#x2600;&#xFE0F;"
    cor1 = "#a78bfa"
    cor2 = "#7c3aed"
    descricao = "No flow, construindo coisas."
elif 18 <= hora < 22:
    periodo = "Boa noite"
    emoji = "&#x1F306;"
    cor1 = "#c084fc"
    cor2 = "#9333ea"
    descricao = "Noite boa para resolver problemas."
else:
    periodo = "Ainda acordado"
    emoji = "&#x1F319;"
    cor1 = "#34d399"
    cor2 = "#10b981"
    descricao = "Madrugada. O melhor horario para codar."

svg = f'''<svg width="860" height="280" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" style="stop-color:#0d1117"/>
    <stop offset="50%" style="stop-color:#0d1117"/>
    <stop offset="100%" style="stop-color:#161b22"/>
  </linearGradient>
  <linearGradient id="nameGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" style="stop-color:{cor1}">
      <animate attributeName="stop-color" values="{cor1};{cor2};{cor1}" dur="4s" repeatCount="indefinite"/>
    </stop>
    <stop offset="100%" style="stop-color:{cor2}">
      <animate attributeName="stop-color" values="{cor2};{cor1};{cor2}" dur="4s" repeatCount="indefinite"/>
    </stop>
  </linearGradient>
  <linearGradient id="lineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" style="stop-color:{cor1};stop-opacity:0"/>
    <stop offset="50%" style="stop-color:{cor1};stop-opacity:1"/>
    <stop offset="100%" style="stop-color:{cor2};stop-opacity:0"/>
  </linearGradient>
  <filter id="glow">
    <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
    <feMerge>
      <feMergeNode in="coloredBlur"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>
  <filter id="softglow">
    <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
    <feMerge>
      <feMergeNode in="coloredBlur"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>
  <style>
    .bg {{ fill: url(#bg); }}
    .name {{
      font-family: "Fira Code", monospace;
      font-size: 38px;
      font-weight: 700;
      fill: url(#nameGrad);
      filter: url(#softglow);
      opacity: 0;
      animation: fadeUp 1s ease forwards 0.5s;
    }}
    .greeting {{
      font-family: "Fira Code", monospace;
      font-size: 12px;
      fill: {cor1};
      opacity: 0;
      animation: fadeIn 0.6s ease forwards 0.2s;
    }}
    .prompt {{
      font-family: "Fira Code", monospace;
      font-size: 11px;
      fill: #3fb950;
      opacity: 0;
      animation: fadeIn 0.6s ease forwards 0.3s;
    }}
    .subtitle {{
      font-family: "Fira Code", monospace;
      font-size: 11px;
      fill: #8b949e;
      opacity: 0;
      animation: fadeIn 0.6s ease forwards;
    }}
    .s1 {{ animation-delay: 1.3s; }}
    .s2 {{ animation-delay: 1.5s; }}
    .s3 {{ animation-delay: 1.7s; }}
    .cursor {{
      fill: {cor1};
      opacity: 0;
      animation: fadeIn 0.1s ease forwards 1.4s, blink 1s step-end infinite 1.5s;
    }}
    .tag {{
      font-family: "Fira Code", monospace;
      font-size: 11px;
      fill: {cor1};
      filter: url(#glow);
      opacity: 0;
      animation: fadeIn 0.5s ease forwards;
    }}
    .tag-1 {{ animation-delay: 2.0s; }}
    .tag-2 {{ animation-delay: 2.2s; }}
    .tag-3 {{ animation-delay: 2.4s; }}
    .tag-4 {{ animation-delay: 2.6s; }}
    .tag-bg {{
      fill: none;
      stroke: {cor1};
      stroke-width: 0.5;
      rx: 4;
      opacity: 0;
      animation: fadeIn 0.5s ease forwards;
    }}
    .tb-1 {{ animation-delay: 2.0s; }}
    .tb-2 {{ animation-delay: 2.2s; }}
    .tb-3 {{ animation-delay: 2.4s; }}
    .tb-4 {{ animation-delay: 2.6s; }}
    .skill-label {{
      font-family: "Fira Code", monospace;
      font-size: 10.5px;
      fill: #8b949e;
      opacity: 0;
      animation: fadeIn 0.4s ease forwards;
    }}
    .sl-1 {{ animation-delay: 1.4s; }}
    .sl-2 {{ animation-delay: 1.6s; }}
    .sl-3 {{ animation-delay: 1.8s; }}
    .sl-4 {{ animation-delay: 2.0s; }}
    .sl-5 {{ animation-delay: 2.2s; }}
    .bar-fill {{
      fill: {cor1};
      transform-origin: left center;
      transform: scaleX(0);
      opacity: 0;
      animation: growBar 1s cubic-bezier(0.4,0,0.2,1) forwards;
      filter: url(#glow);
    }}
    .bf-1 {{ animation-delay: 1.4s; }}
    .bf-2 {{ animation-delay: 1.6s; }}
    .bf-3 {{ animation-delay: 1.8s; }}
    .bf-4 {{ animation-delay: 2.0s; }}
    .bf-5 {{ animation-delay: 2.2s; }}
    .bar-pct {{
      font-family: "Fira Code", monospace;
      font-size: 9px;
      fill: {cor1};
      opacity: 0;
      animation: fadeIn 0.4s ease forwards;
    }}
    .bp-1 {{ animation-delay: 2.0s; }}
    .bp-2 {{ animation-delay: 2.2s; }}
    .bp-3 {{ animation-delay: 2.4s; }}
    .bp-4 {{ animation-delay: 2.6s; }}
    .bp-5 {{ animation-delay: 2.8s; }}
    .section-title {{
      font-family: "Fira Code", monospace;
      font-size: 10px;
      fill: #3fb950;
      opacity: 0;
      animation: fadeIn 0.5s ease forwards 0.8s;
    }}
    .divv {{
      opacity: 0;
      animation: fadeIn 0.5s ease forwards 0.9s;
    }}
    .particle {{
      fill: {cor1};
      opacity: 0;
    }}
    @keyframes fadeUp {{
      from {{ opacity: 0; transform: translateY(12px); }}
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
      from {{ transform: scaleX(0); opacity: 0; }}
      to   {{ transform: scaleX(1); opacity: 1; }}
    }}
    @keyframes float1 {{
      0%   {{ opacity: 0; transform: translate(0,0); }}
      20%  {{ opacity: 0.6; }}
      100% {{ opacity: 0; transform: translate(-15px, -60px); }}
    }}
    @keyframes float2 {{
      0%   {{ opacity: 0; transform: translate(0,0); }}
      20%  {{ opacity: 0.5; }}
      100% {{ opacity: 0; transform: translate(10px, -80px); }}
    }}
    @keyframes float3 {{
      0%   {{ opacity: 0; transform: translate(0,0); }}
      25%  {{ opacity: 0.7; }}
      100% {{ opacity: 0; transform: translate(-8px, -50px); }}
    }}
    @keyframes pulse {{
      0%, 100% {{ r: 2; opacity: 0.4; }}
      50% {{ r: 3.5; opacity: 1; }}
    }}
  </style>
</defs>

<!-- Fundo -->
<rect width="860" height="280" class="bg" rx="14"/>

<!-- Borda superior com gradiente animado -->
<rect x="0" y="0" width="860" height="2" fill="url(#lineGrad)" rx="1"/>

<!-- Partículas flutuantes decorativas -->
<circle cx="80" cy="240" r="2" fill="{cor1}" opacity="0">
  <animate attributeName="opacity" values="0;0.5;0" dur="4s" begin="2s" repeatCount="indefinite"/>
  <animate attributeName="cy" values="240;180;240" dur="4s" begin="2s" repeatCount="indefinite"/>
  <animate attributeName="cx" values="80;70;80" dur="4s" begin="2s" repeatCount="indefinite"/>
</circle>
<circle cx="140" cy="220" r="1.5" fill="{cor2}" opacity="0">
  <animate attributeName="opacity" values="0;0.6;0" dur="5s" begin="3s" repeatCount="indefinite"/>
  <animate attributeName="cy" values="220;150;220" dur="5s" begin="3s" repeatCount="indefinite"/>
</circle>
<circle cx="55" cy="200" r="1" fill="{cor1}" opacity="0">
  <animate attributeName="opacity" values="0;0.4;0" dur="3.5s" begin="1s" repeatCount="indefinite"/>
  <animate attributeName="cy" values="200;140;200" dur="3.5s" begin="1s" repeatCount="indefinite"/>
</circle>
<circle cx="190" cy="260" r="1.5" fill="{cor2}" opacity="0">
  <animate attributeName="opacity" values="0;0.5;0" dur="6s" begin="0.5s" repeatCount="indefinite"/>
  <animate attributeName="cy" values="260;190;260" dur="6s" begin="0.5s" repeatCount="indefinite"/>
</circle>
<circle cx="110" cy="250" r="2" fill="{cor1}" opacity="0">
  <animate attributeName="opacity" values="0;0.3;0" dur="4.5s" begin="4s" repeatCount="indefinite"/>
  <animate attributeName="cy" values="250;170;250" dur="4.5s" begin="4s" repeatCount="indefinite"/>
</circle>

<!-- Coluna esquerda -->
<!-- Saudação -->
<text x="24" y="32" class="greeting">{emoji}  {periodo}, visitante!</text>
<text x="24" y="50" class="prompt">~/pedropaulucci27 $</text>

<!-- Nome com gradiente animado -->
<text x="24" y="100" class="name">Pedro Paulucci</text>
<rect x="24" y="106" width="8" height="3" fill="{cor1}" class="cursor"/>

<!-- Linha decorativa sob o nome -->
<rect x="24" y="112" width="0" height="1.5" fill="url(#lineGrad)" rx="1">
  <animate attributeName="width" from="0" to="230" dur="0.8s" begin="1.2s" fill="freeze"/>
</rect>

<!-- Subtítulos -->
<text x="24" y="132" class="subtitle s1">Software Eng. + Data Science &amp; AI</text>
<text x="24" y="148" class="subtitle s2">{descricao}</text>
<text x="24" y="164" class="subtitle s3">Ibmec BH · Ibtech · Belo Horizonte</text>

<!-- Tags com bordas -->
<rect x="22" y="178" width="110" height="18" rx="4" class="tag-bg tb-1"/>
<text x="30" y="191" class="tag tag-1">&#x25CF; Data Science</text>

<rect x="138" y="178" width="80" height="18" rx="4" class="tag-bg tb-2"/>
<text x="146" y="191" class="tag tag-2">&#x25CF; Web Dev</text>

<rect x="22" y="202" width="98" height="18" rx="4" class="tag-bg tb-3"/>
<text x="30" y="215" class="tag tag-3">&#x25CF; Java &amp; OOP</text>

<rect x="126" y="202" width="116" height="18" rx="4" class="tag-bg tb-4"/>
<text x="134" y="215" class="tag tag-4">&#x25CF; Node &amp; Express</text>

<!-- Divisor vertical animado -->
<line x1="248" y1="0" x2="248" y2="0" stroke="{cor1}" stroke-width="0.5" stroke-opacity="0.3" class="divv">
  <animate attributeName="y2" from="0" to="280" dur="0.8s" begin="0.5s" fill="freeze"/>
</line>

<!-- Coluna direita: skills -->
<text x="268" y="32" class="section-title">// skills.json</text>

<!-- Linha decorativa -->
<rect x="268" y="38" width="0" height="1" fill="url(#lineGrad)" rx="1">
  <animate attributeName="width" from="0" to="568" dur="0.8s" begin="0.9s" fill="freeze"/>
</rect>

<!-- JavaScript -->
<text x="268" y="82" class="skill-label sl-1">JavaScript</text>
<rect x="358" y="72" width="458" height="8" rx="4" fill="#21262d"/>
<rect x="358" y="72" width="412" height="8" rx="4" class="bar-fill bf-1"/>
<text x="824" y="82" class="bar-pct bp-1">90%</text>

<!-- Python -->
<text x="268" y="110" class="skill-label sl-2">Python</text>
<rect x="358" y="100" width="458" height="8" rx="4" fill="#21262d"/>
<rect x="358" y="100" width="321" height="8" rx="4" class="bar-fill bf-2"/>
<text x="824" y="110" class="bar-pct bp-2">70%</text>

<!-- Java -->
<text x="268" y="138" class="skill-label sl-3">Java</text>
<rect x="358" y="128" width="458" height="8" rx="4" fill="#21262d"/>
<rect x="358" y="128" width="275" height="8" rx="4" class="bar-fill bf-3"/>
<text x="824" y="138" class="bar-pct bp-3">60%</text>

<!-- C -->
<text x="268" y="166" class="skill-label sl-4">C</text>
<rect x="358" y="156" width="458" height="8" rx="4" fill="#21262d"/>
<rect x="358" y="156" width="229" height="8" rx="4" class="bar-fill bf-4"/>
<text x="824" y="166" class="bar-pct bp-4">50%</text>

<!-- Node.js -->
<text x="268" y="194" class="skill-label sl-5">Node.js</text>
<rect x="358" y="184" width="458" height="8" rx="4" fill="#21262d"/>
<rect x="358" y="184" width="183" height="8" rx="4" class="bar-fill bf-5"/>
<text x="824" y="194" class="bar-pct bp-5">40%</text>

<!-- Linha inferior com gradiente -->
<rect x="0" y="278" width="860" height="2" fill="url(#lineGrad)" rx="1"/>

<!-- Pontos de canto decorativos -->
<circle cx="12" cy="268" r="2" fill="{cor1}" opacity="0.3">
  <animate attributeName="opacity" values="0.3;0.8;0.3" dur="2s" repeatCount="indefinite"/>
</circle>
<circle cx="848" cy="268" r="2" fill="{cor2}" opacity="0.3">
  <animate attributeName="opacity" values="0.3;0.8;0.3" dur="2.5s" repeatCount="indefinite"/>
</circle>
<circle cx="12" cy="12" r="2" fill="{cor1}" opacity="0.3">
  <animate attributeName="opacity" values="0.3;0.8;0.3" dur="3s" repeatCount="indefinite"/>
</circle>
<circle cx="848" cy="12" r="2" fill="{cor2}" opacity="0.3">
  <animate attributeName="opacity" values="0.3;0.8;0.3" dur="1.8s" repeatCount="indefinite"/>
</circle>

</svg>'''

with open("profile_animation.svg", "w") as f:
    f.write(svg)

print(f"SVG gerado! Periodo: {periodo} ({hora}h)")

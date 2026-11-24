import re
import base64

with open('/Users/vijayyadav/Desktop/perceptron/Round1_Submission_Abstract.md', 'r') as f:
    md_content = f.read()

with open('/Users/vijayyadav/Desktop/perceptron/architecture_diagram.png', 'rb') as f:
    img_b64 = base64.b64encode(f.read()).decode('utf-8')

# Custom parser for clean academic layout
html_parts = []
in_table = False
table_rows = []
in_list = False

lines = md_content.split('\n')

i = 0
while i < len(lines):
    line = lines[i]
    
    # Skip Title & Author
    if line.startswith('# CREED:'):
        i += 1
        continue
    if line.strip() in ['**Vijay Yadav**', '**IIT Bombay**', '---']:
        i += 1
        continue

    # Tables
    if line.strip().startswith('|') and '|' in line[1:]:
        if not in_table:
            in_table = True
            table_rows = []
        table_rows.append(line.strip())
        i += 1
        continue
    else:
        if in_table:
            in_table = False
            t_html = ['<table>']
            for r_idx, row in enumerate(table_rows):
                if '---' in row:
                    continue
                cols = [c.strip() for c in row.split('|')[1:-1]]
                if r_idx == 0:
                    t_html.append('<thead><tr>' + ''.join(f'<th>{c}</th>' for c in cols) + '</tr></thead><tbody>')
                else:
                    t_html.append('<tr>' + ''.join(f'<td>{c}</td>' for c in cols) + '</tr>')
            t_html.append('</tbody></table>')
            html_parts.append('\n'.join(t_html))

    # Section Headers
    if line.startswith('### Section'):
        if in_list:
            html_parts.append('</ul>')
            in_list = False
        sec_title = line.replace('### ', '').strip()
        html_parts.append(f'<h2>{sec_title}</h2>')
        i += 1
        continue

    # Display Math ($$...$$)
    if line.strip().startswith('$$') and line.strip().endswith('$$') and len(line.strip()) > 4:
        if in_list:
            html_parts.append('</ul>')
            in_list = False
        html_parts.append(f'<div class="math-display">{line.strip()}</div>')
        i += 1
        continue

    # Bullet lists
    if line.strip().startswith('* ') or line.strip().startswith('- '):
        if not in_list:
            html_parts.append('<ul>')
            in_list = True
        item_text = line.strip()[2:]
        item_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item_text)
        item_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', item_text)
        item_text = re.sub(r'`(.*?)`', r'<code>\1</code>', item_text)
        html_parts.append(f'<li>{item_text}</li>')
        i += 1
        continue
    else:
        if in_list:
            html_parts.append('</ul>')
            in_list = False

    # Numbered list
    if re.match(r'^\d+\.\s', line.strip()):
        item_text = re.sub(r'^\d+\.\s', '', line.strip())
        item_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item_text)
        item_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', item_text)
        item_text = re.sub(r'`(.*?)`', r'<code>\1</code>', item_text)
        html_parts.append(f'<p style="margin-left: 18px; margin-bottom: 4px;"><strong>{line.strip()[:2]}</strong> {item_text}</p>')
        i += 1
        continue

    # Regular paragraph
    if line.strip():
        p_text = line.strip()
        p_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', p_text)
        p_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', p_text)
        p_text = re.sub(r'`(.*?)`', r'<code>\1</code>', p_text)
        html_parts.append(f'<p>{p_text}</p>')
    
    i += 1

if in_list:
    html_parts.append('</ul>')

body_content = '\n'.join(html_parts)

final_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CREED: Round 1 Abstract | Vijay Yadav (IIT Bombay)</title>
  <script>
    window.MathJax = {{
      tex: {{
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
        processEscapes: true
      }},
      options: {{
        skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
      }}
    }};
  </script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');
    
    @page {{
      size: A4;
      margin: 14mm 14mm 14mm 14mm;
    }}

    body {{
      font-family: 'Source Serif 4', Georgia, 'Times New Roman', serif;
      line-height: 1.42;
      color: #0f172a;
      background-color: #ffffff;
      margin: 0;
      padding: 0;
      font-size: 10pt;
    }}

    .container {{
      max-width: 100%;
      margin: 0 auto;
      background: #ffffff;
    }}

    .doc-header {{
      text-align: center;
      border-bottom: 1.5px solid #0f172a;
      padding-bottom: 10px;
      margin-bottom: 14px;
    }}

    h1 {{
      font-size: 17pt;
      font-weight: 700;
      color: #0f172a;
      margin: 0 0 4px 0;
      line-height: 1.25;
      letter-spacing: -0.3px;
    }}

    .author-name {{
      font-family: 'Inter', sans-serif;
      font-size: 11pt;
      font-weight: 700;
      color: #0f172a;
      margin-top: 2px;
    }}

    .affiliation {{
      font-family: 'Inter', sans-serif;
      font-size: 9.5pt;
      color: #334155;
      margin-top: 1px;
    }}

    h2 {{
      font-family: 'Inter', sans-serif;
      font-size: 10.5pt;
      font-weight: 700;
      color: #0f172a;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      margin-top: 14px;
      margin-bottom: 5px;
      border-bottom: 0.8px solid #cbd5e1;
      padding-bottom: 2px;
      break-after: avoid;
    }}

    p {{
      font-size: 9.8pt;
      color: #1e293b;
      margin: 0 0 6px 0;
      text-align: justify;
      text-justify: inter-word;
    }}

    ul {{
      margin: 0 0 6px 0;
      padding-left: 18px;
      font-size: 9.8pt;
      color: #1e293b;
    }}

    li {{
      margin-bottom: 3px;
    }}

    code {{
      font-family: 'JetBrains Mono', monospace;
      background: #f8fafc;
      padding: 1px 3px;
      border-radius: 2px;
      font-size: 8.5pt;
      color: #0f172a;
      border: 0.5px solid #e2e8f0;
    }}

    .math-display {{
      margin: 6px 0;
      text-align: center;
      font-size: 10.5pt;
      overflow-x: auto;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 8.5pt;
      margin: 10px 0;
      font-family: 'Inter', sans-serif;
      break-inside: avoid;
    }}

    th {{
      border-top: 1.2px solid #0f172a;
      border-bottom: 1.2px solid #0f172a;
      color: #0f172a;
      text-align: left;
      padding: 5px 8px;
      font-weight: 600;
      background: #f8fafc;
    }}

    td {{
      padding: 5px 8px;
      border-bottom: 0.5px solid #e2e8f0;
      color: #1e293b;
      vertical-align: top;
    }}

    tr:last-child td {{
      border-bottom: 1.2px solid #0f172a;
    }}

    .diagram-section {{
      page-break-before: always;
      padding-top: 8px;
      text-align: center;
    }}

    .diagram-section img {{
      width: 100%;
      height: auto;
      border: 1px solid #0f172a;
      border-radius: 3px;
      display: block;
    }}

    .diagram-caption {{
      font-family: 'Inter', sans-serif;
      font-size: 9pt;
      color: #475569;
      margin-top: 8px;
      text-align: center;
      font-style: italic;
    }}

    @media print {{
      body {{
        padding: 0;
        background: #ffffff;
      }}
      .diagram-section {{
        page-break-before: always;
      }}
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="doc-header">
      <h1>CREED: Trust-Gated Conformal Fusion of Financial Text &amp; Market Microstructure</h1>
      <div class="author-name">Vijay Yadav</div>
      <div class="affiliation">Indian Institute of Technology Bombay (IIT Bombay)</div>
    </div>

    {body_content}

    <div class="diagram-section">
      <h2>Figure 1: Complete System Architecture Specification</h2>
      <img src="data:image/png;base64,{img_b64}" alt="CREED System Architecture Diagram">
      <div class="diagram-caption">Figure 1: Architectural Data Flow of CREED &mdash; Dual-Stream Encoders, 5-Cue Trust Gating, Cross-Modal Attention, Mondrian CQR &amp; Online ACI, and Epistemic Abstention Gate.</div>
    </div>
  </div>
</body>
</html>
'''

with open('/Users/vijayyadav/Desktop/perceptron/Round1_Submission_Document.html', 'w') as f:
    f.write(final_html)

print("Saved compact, print-optimized Round1_Submission_Document.html")

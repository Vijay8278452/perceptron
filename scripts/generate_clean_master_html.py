import re
import base64

with open('/Users/vijayyadav/Desktop/perceptron/PERCEPTRON_HACKATHON_MASTER_REPORT.md', 'r') as f:
    md_content = f.read()

with open('/Users/vijayyadav/Desktop/perceptron/architecture_diagram.png', 'rb') as f:
    img_b64 = base64.b64encode(f.read()).decode('utf-8')

# Custom parser for clean academic layout
html_parts = []
in_table = False
table_rows = []
in_list = False
in_code = False
code_lines = []

lines = md_content.split('\n')

i = 0
while i < len(lines):
    line = lines[i]
    
    # Skip Title & Author
    if line.startswith('# PERCEPTRON HACKATHON 2026:'):
        i += 1
        continue
    if line.strip() in ['**Vijay Yadav**', '**IIT Bombay**', '*Techfest, IIT Bombay*', '---']:
        i += 1
        continue

    # Code blocks
    if line.strip().startswith('```'):
        if not in_code:
            in_code = True
            code_lines = []
        else:
            in_code = False
            html_parts.append('<pre><code>' + '\n'.join(code_lines) + '</code></pre>')
        i += 1
        continue
    if in_code:
        code_lines.append(line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
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

    # Headers
    if line.startswith('## '):
        if in_list:
            html_parts.append('</ul>')
            in_list = False
        sec_title = line.replace('## ', '').strip()
        html_parts.append(f'<h2>{sec_title}</h2>')
        i += 1
        continue
    if line.startswith('### '):
        if in_list:
            html_parts.append('</ul>')
            in_list = False
        sec_title = line.replace('### ', '').strip()
        html_parts.append(f'<h3>{sec_title}</h3>')
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
        html_parts.append(f'<p style="margin-left: 20px;"><strong>{line.strip()[:2]}</strong> {item_text}</p>')
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
  <title>PERCEPTRON HACKATHON 2026: Master Strategy &amp; Technical Report</title>
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
    
    body {{
      font-family: 'Source Serif 4', Georgia, 'Times New Roman', serif;
      line-height: 1.65;
      color: #0f172a;
      background-color: #ffffff;
      margin: 0;
      padding: 40px 20px;
    }}

    .container {{
      max-width: 920px;
      margin: 0 auto;
      background: #ffffff;
      padding: 20px 40px;
    }}

    .doc-header {{
      text-align: center;
      border-bottom: 2px solid #0f172a;
      padding-bottom: 24px;
      margin-bottom: 30px;
    }}

    h1 {{
      font-size: 26px;
      font-weight: 700;
      color: #0f172a;
      margin: 0 0 10px 0;
      line-height: 1.3;
      letter-spacing: -0.3px;
    }}

    .author-name {{
      font-family: 'Inter', sans-serif;
      font-size: 16px;
      font-weight: 700;
      color: #0f172a;
      margin-top: 6px;
    }}

    .affiliation {{
      font-family: 'Inter', sans-serif;
      font-size: 14px;
      color: #334155;
      margin-top: 2px;
    }}

    h2 {{
      font-family: 'Inter', sans-serif;
      font-size: 16px;
      font-weight: 700;
      color: #0f172a;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      margin-top: 36px;
      margin-bottom: 12px;
      border-bottom: 1.5px solid #0f172a;
      padding-bottom: 5px;
    }}

    h3 {{
      font-family: 'Inter', sans-serif;
      font-size: 14px;
      font-weight: 700;
      color: #1e293b;
      margin-top: 22px;
      margin-bottom: 8px;
    }}

    p {{
      font-size: 14.5px;
      color: #1e293b;
      margin: 0 0 14px 0;
      text-align: justify;
      text-justify: inter-word;
    }}

    ul {{
      margin: 0 0 14px 0;
      padding-left: 24px;
      font-size: 14.5px;
      color: #1e293b;
    }}

    li {{
      margin-bottom: 6px;
    }}

    code {{
      font-family: 'JetBrains Mono', monospace;
      background: #f8fafc;
      padding: 2px 5px;
      border-radius: 3px;
      font-size: 12.5px;
      color: #0f172a;
      border: 1px solid #e2e8f0;
    }}

    pre {{
      background: #f8fafc;
      padding: 14px 18px;
      border-radius: 4px;
      border: 1px solid #cbd5e1;
      font-family: 'JetBrains Mono', monospace;
      font-size: 12.5px;
      overflow-x: auto;
      line-height: 1.5;
    }}

    pre code {{
      background: none;
      padding: 0;
      border: none;
    }}

    .math-display {{
      margin: 16px 0;
      text-align: center;
      font-size: 15px;
      overflow-x: auto;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
      margin: 22px 0;
      font-family: 'Inter', sans-serif;
    }}

    th {{
      border-top: 1.5px solid #0f172a;
      border-bottom: 1.5px solid #0f172a;
      color: #0f172a;
      text-align: left;
      padding: 9px 12px;
      font-weight: 600;
      background: #f8fafc;
    }}

    td {{
      padding: 9px 12px;
      border-bottom: 1px solid #e2e8f0;
      color: #1e293b;
      vertical-align: top;
    }}

    tr:last-child td {{
      border-bottom: 1.5px solid #0f172a;
    }}

    .diagram-section {{
      margin-top: 40px;
      margin-bottom: 40px;
      text-align: center;
    }}

    .diagram-section img {{
      width: 100%;
      height: auto;
      border: 1px solid #0f172a;
      border-radius: 4px;
      display: block;
    }}

    .diagram-caption {{
      font-family: 'Inter', sans-serif;
      font-size: 13px;
      color: #475569;
      margin-top: 10px;
      text-align: center;
      font-style: italic;
    }}

    .doc-footer {{
      margin-top: 50px;
      border-top: 1px solid #cbd5e1;
      padding-top: 20px;
      text-align: center;
      font-family: 'Inter', sans-serif;
      font-size: 12.5px;
      color: #475569;
    }}

    @media print {{
      body {{
        padding: 0;
        background: #ffffff;
      }}
      .container {{
        padding: 10px;
        max-width: 100%;
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
      <h1>PERCEPTRON HACKATHON 2026: MASTER STRATEGY &amp; TECHNICAL REPORT</h1>
      <div class="author-name">Vijay Yadav</div>
      <div class="affiliation">IIT Bombay &bull; Techfest, IIT Bombay</div>
    </div>

    {body_content}

    <div class="diagram-section">
      <h2>Complete System Architecture Diagram</h2>
      <img src="data:image/png;base64,{img_b64}" alt="CREED System Architecture Diagram">
      <div class="diagram-caption">Figure 1: Complete Architectural Specification of CREED &mdash; Dual-Stream Encoders, Cross-Modal Attention with Dynamic Noise Gating, Adaptive Conformal Inference (ACI), and Epistemic Abstention Gate.</div>
    </div>

    <div class="doc-footer">
      <strong>IITB-Optiver AI Innovation Lab &bull; Perceptron Hackathon 2026</strong><br>
      Vijay Yadav &bull; Indian Institute of Technology Bombay
    </div>
  </div>
</body>
</html>
'''

with open('/Users/vijayyadav/Desktop/perceptron/PERCEPTRON_HACKATHON_MASTER_REPORT.html', 'w') as f:
    f.write(final_html)

print('Successfully generated clean PERCEPTRON_HACKATHON_MASTER_REPORT.html')

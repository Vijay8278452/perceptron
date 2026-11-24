import base64
import os

with open('/Users/vijayyadav/Desktop/perceptron/architecture_diagram.png', 'rb') as img_f:
    img_b64 = base64.b64encode(img_f.read()).decode('utf-8')

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Perceptron Hackathon 2026 - Master Technical & Strategy Report | IITB-Optiver Lab</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap');
    
    :root {{
      --primary: #0284c7;
      --primary-dark: #0369a1;
      --accent: #8b5cf6;
      --accent-dark: #6d28d9;
      --bg-page: #f8fafc;
      --bg-card: #ffffff;
      --text-main: #0f172a;
      --text-muted: #475569;
      --border: #e2e8f0;
      --code-bg: #f1f5f9;
      --badge-bg: #e0f2fe;
    }}

    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      line-height: 1.65;
      color: var(--text-main);
      background-color: var(--bg-page);
      margin: 0;
      padding: 40px 20px;
    }}

    .container {{
      max-width: 1040px;
      margin: 0 auto;
      background: var(--bg-card);
      padding: 60px 70px;
      box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.07);
      border-radius: 16px;
      border: 1px solid var(--border);
    }}

    .hero-banner {{
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
      color: #ffffff;
      padding: 40px 45px;
      border-radius: 12px;
      margin-bottom: 40px;
      border-left: 6px solid var(--primary);
      position: relative;
    }}

    .hero-badge {{
      display: inline-block;
      background: rgba(56, 189, 248, 0.2);
      color: #38bdf8;
      font-size: 11px;
      font-weight: 800;
      padding: 5px 12px;
      border-radius: 20px;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 14px;
      border: 1px solid rgba(56, 189, 248, 0.3);
    }}

    .hero-banner h1 {{
      font-size: 30px;
      font-weight: 900;
      margin: 0 0 10px 0;
      color: #ffffff;
      letter-spacing: -0.5px;
      line-height: 1.25;
    }}

    .hero-banner p {{
      font-size: 15px;
      color: #cbd5e1;
      margin: 0 0 20px 0;
    }}

    .hero-stats {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 15px;
      border-top: 1px solid #334155;
      padding-top: 20px;
    }}

    .stat-box h4 {{
      font-size: 11px;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin: 0 0 4px 0;
    }}

    .stat-box p {{
      font-size: 14px;
      font-weight: 700;
      color: #38bdf8;
      margin: 0;
    }}

    h2 {{
      font-size: 20px;
      font-weight: 800;
      color: #0f172a;
      margin-top: 45px;
      margin-bottom: 16px;
      border-bottom: 2px solid var(--border);
      padding-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    h3 {{
      font-size: 16px;
      font-weight: 700;
      color: var(--primary-dark);
      margin-top: 28px;
      margin-bottom: 12px;
    }}

    p {{
      font-size: 14.5px;
      color: var(--text-muted);
      margin: 0 0 16px 0;
      text-align: justify;
    }}

    ul, ol {{
      margin: 0 0 18px 0;
      padding-left: 24px;
      font-size: 14.5px;
      color: var(--text-muted);
    }}

    li {{
      margin-bottom: 8px;
    }}

    code {{
      font-family: 'JetBrains Mono', monospace;
      background: var(--code-bg);
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 12.5px;
      color: var(--primary-dark);
    }}

    .math-block {{
      background: #0f172a;
      color: #e2e8f0;
      padding: 16px 20px;
      border-radius: 8px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      margin: 16px 0;
      overflow-x: auto;
      border-left: 4px solid #38bdf8;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13.5px;
      margin: 20px 0 30px 0;
    }}

    th {{
      background: #0f172a;
      color: #ffffff;
      text-align: left;
      padding: 12px 14px;
      font-weight: 600;
      font-size: 12.5px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    td {{
      padding: 12px 14px;
      border-bottom: 1px solid var(--border);
      color: #334155;
    }}

    tr:nth-child(even) td {{
      background: #f8fafc;
    }}

    .callout {{
      background: #eff6ff;
      border-left: 4px solid var(--primary);
      padding: 16px 20px;
      border-radius: 0 8px 8px 0;
      margin: 20px 0;
      font-size: 14px;
      color: #1e3a8a;
    }}

    .callout strong {{
      color: #1e40af;
    }}

    .diagram-container {{
      margin: 40px 0;
      text-align: center;
      background: #0b1120;
      padding: 24px;
      border-radius: 12px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
    }}

    .diagram-container img {{
      width: 100%;
      height: auto;
      border-radius: 8px;
      display: block;
    }}

    .diagram-caption {{
      margin-top: 14px;
      font-size: 13px;
      color: #94a3b8;
      font-weight: 500;
    }}

    .footer {{
      margin-top: 60px;
      border-top: 1px solid var(--border);
      padding-top: 25px;
      text-align: center;
      font-size: 13px;
      color: #64748b;
    }}

    @media print {{
      body {{
        padding: 0;
        background: #ffffff;
      }}
      .container {{
        box-shadow: none;
        border: none;
        padding: 20px;
        max-width: 100%;
      }}
      .diagram-container {{
        page-break-before: always;
      }}
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="hero-banner">
      <span class="hero-badge">IITB-Optiver AI Innovation Lab • Techfest 2026</span>
      <h1>PERCEPTRON HACKATHON 2026<br><span style="color: #38bdf8; font-size: 24px;">Master Strategy &amp; Technical Execution Blueprint</span></h1>
      <p>A rigorous, mathematically grounded blueprint for competing and winning in the national flagship AI &amp; quantitative systems competition.</p>
      
      <div class="hero-stats">
        <div class="stat-box">
          <h4>Track Chosen</h4>
          <p>Theme 6 (Trustworthy AI)</p>
        </div>
        <div class="stat-box">
          <h4>Problem Statement</h4>
          <p>PS 10 (Conformal Text+Price)</p>
        </div>
        <div class="stat-box">
          <h4>Round 1 Deadline</h4>
          <p>31st October 2026</p>
        </div>
        <div class="stat-box">
          <h4>Grand Finals</h4>
          <p>15-18 Dec @ IIT Bombay</p>
        </div>
      </div>
    </div>

    <h2>1. Executive Summary &amp; Competition Profile</h2>
    <p>
      The <strong>Perceptron Hackathon 2026</strong> is presented by the <strong>IITB-Optiver AI Innovation Lab</strong> in collaboration with <strong>Techfest, IIT Bombay</strong> (Asia's largest science and technology festival). The competition challenges student builders to solve technically demanding research problems across 6 core themes: Efficient AI, Causal Decisions, Markets &amp; Trading, Multi-Agent Systems, AI That Teaches, and Trustworthy AI.
    </p>
    <div class="callout">
      <strong>Crucial Format Rule:</strong> Round 1 is judged <em>purely on the technical depth, mathematical rigor, and feasibility of the plan</em> (600–900 word abstract + 1-page architecture diagram). No working code or prototype is required at this stage. Only <strong>25–30 teams total across all 10 problem statements combined</strong> advance to the in-person finals at IIT Bombay.
    </div>

    <h2>2. Official Evaluation Rubric &amp; Weightages</h2>
    <table>
      <thead>
        <tr>
          <th>Evaluation Criterion</th>
          <th>Weight</th>
          <th>What Reviewers Demand</th>
          <th>CREED Score Targeting</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Technical Soundness &amp; Feasibility</strong></td>
          <td><strong>25%</strong></td>
          <td>Valid mathematics, appropriate named tools/datasets, buildable by 3 students in 5-6 weeks.</td>
          <td><strong>5 / 5 (Excellent)</strong>: Named libraries (MAPIE, FinBERT, PyTorch) with proven finite-sample guarantees.</td>
        </tr>
        <tr>
          <td><strong>Problem Understanding &amp; Relevance</strong></td>
          <td><strong>20%</strong></td>
          <td>Identifies true technical crux rather than restating surface prompt. Realistic MVP bar.</td>
          <td><strong>5 / 5 (Excellent)</strong>: Grasps failure of i.i.d. assumptions in non-stationary financial regimes.</td>
        </tr>
        <tr>
          <td><strong>Innovation / Novelty</strong></td>
          <td><strong>20%</strong></td>
          <td>Goes beyond starter resources. Original ideas in method, evaluation, or framing.</td>
          <td><strong>5 / 5 (Excellent)</strong>: Adaptive Conformal Inference (ACI), Gated Attention, Epistemic Risk Gate.</td>
        </tr>
        <tr>
          <td><strong>Impact &amp; Rigor of Evaluation Plan</strong></td>
          <td><strong>15%</strong></td>
          <td>Meaningful metrics that actually prove claims against rigorous baselines.</td>
          <td><strong>5 / 5 (Excellent)</strong>: Empirical Coverage Rate, MPIW, Winkler Score, Sharpe Ratio lift.</td>
        </tr>
        <tr>
          <td><strong>Clarity &amp; Structure of Abstract</strong></td>
          <td><strong>10%</strong></td>
          <td>Concrete and precise writing, free of hand-wavy AI buzzwords.</td>
          <td><strong>5 / 5 (Excellent)</strong>: Strict adherence to 8-section official rubric with quantitative parameters.</td>
        </tr>
        <tr>
          <td><strong>Team Fit &amp; Readiness</strong></td>
          <td><strong>10%</strong></td>
          <td>Plausible 3-member skill mix and credible milestone delivery schedule.</td>
          <td><strong>5 / 5 (Excellent)</strong>: Clear division (NLP, Conformal Statistics, Systems) with 6-week roadmap.</td>
        </tr>
      </tbody>
    </table>

    <h2>3. The Winning Solution: CREED (Problem 10)</h2>
    <p>
      Our chosen proposal is <strong>CREED: Conformal Robustness &amp; Epistemic Evaluation for Event-Driven Decisions</strong>. It solves the fatal flaw of current automated trading agents—making overconfident bets on manipulated or noisy news—by wrapping multi-modal neural representations with distribution-free conformal confidence intervals that widen under text corruption to trigger execution abstention.
    </p>

    <div class="diagram-container">
      <img src="data:image/png;base64,{img_b64}" alt="CREED Deep Architecture Diagram">
      <div class="diagram-caption">Figure 1: Complete CREED Architectural Blueprint — Dual-Stream Feature Encoders, Cross-Modal Gated Attention (CMAF), Quantile Regression, Adaptive Conformal Inference (ACI), and Epistemic Abstention Gate.</div>
    </div>

    <h2>4. Core Mathematical Formulation</h2>
    <p>CREED is grounded in distribution-free, finite-sample statistical guarantees:</p>

    <div class="math-block">
# 1. Asynchronous Feature Alignment
Input Text Tokens: H_text ∈ ℝ^{{B × L × 768}} (FinBERT + LoRA: rank r=16, α=32)
Microstructure Tensor: H_ts ∈ ℝ^{{B × T × 128}} (Dilated Causal TCN, receptive field = 61 mins)

# 2. Cross-Modal Attention with Dynamic Noise Gating (CMAF)
Q = H_ts · W_Q,   K = H_text · W_K,   V = H_text · W_V
Context Vector: C_v = Softmax( Q · Kᵀ / √d_k ) · V
Noise Gate: λ_t = σ( W_g · [ H_ts ; C_v ; Perplexity ] + b_g ) ∈ [0, 1]
Fused State: Z_fused = H_ts + λ_t ⊙ C_v   (When text is noise, λ → 0, falling back to pure price)

# 3. Non-Conformity Scoring & Rolling Calibration Queue
Non-Conformity Score: E_i = max( q̂_{{α/2}}(X_i) - Y_i,  Y_i - q̂_{{1-α/2}}(X_i) )
Calibration Buffer: 𝒟_cal = {{ E_{{t-K}}, ..., E_{{t-1}} }} of size K = 500

# 4. Adaptive Conformal Inference (ACI) Dynamic Rule
Coverage Error: err_t = 𝕀( Y_t ∉ C_t(X_t) )
Nominal Target Update: α_{{t+1}} = α_t + γ · ( α - err_t )
Exact Asymptotic Coverage Guarantee: lim_{{T→∞}} (1/T) ∑_{{t=1}}^T 𝕀( Y_t ∈ C_t(X_t) ) = 1 - α

# 5. Downstream Epistemic Risk Abstention Gate
Interval Width: W_t = |C_t(X_t)| = [ q̂_{{1-α/2}} + Q̂_{{1-α_t}}(E) ] - [ q̂_{{α/2}} - Q̂_{{1-α_t}}(E) ]
Risk Threshold: τ_risk = k · σ_t^{{Parkinson}}  (k = 2.5)
Execution Decision:
  IF W_t ≤ τ_risk ➔ EXECUTE ORDER (High Trust Event Alpha)
  IF W_t > τ_risk ➔ ABSTAIN & WITHHOLD (Manipulated / Noisy Text Detected)
    </div>

    <h2>5. Round 2 Implementation Roadmap (Weeks 1 to 6)</h2>
    <ul>
      <li><strong>Weeks 1–2 (Nov 10–23): Data &amp; Baselines</strong> — Ingest FNSPID corpus and Polygon.io 1-minute equity bars for top 50 S&P 500 stocks. Train causal Dilated TCN baseline. Fine-tune FinBERT with LoRA adapters ($r=16, \alpha=32$).</li>
      <li><strong>Weeks 3–4 (Nov 24–Dec 7): Multi-Modal Fusion &amp; Conformalization</strong> — Implement CMAF cross-attention with adaptive gating. Train multi-quantile prediction head. Integrate <code>MAPIE</code> for Conformalized Quantile Regression (CQR). Submit Midway Report on Dec 1.</li>
      <li><strong>Week 5 (Dec 8–12): Non-Stationary ACI &amp; Adversarial Red-Teaming</strong> — Implement online Adaptive Conformal Inference with rolling calibration buffer. Curate synthetic pump-and-dump perturbation suite and verify interval width expansion ($>200\%$).</li>
      <li><strong>Week 6 (Dec 13–15): Final Polish &amp; IIT Bombay Demo</strong> — Build interactive Streamlit demo dashboard. Benchmark inference latency with ONNX Runtime. Prepare presentation slide deck for the Optiver + IIT Bombay grand jury.</li>
    </ul>

    <h2>6. Submission Files Manifest</h2>
    <table>
      <thead>
        <tr>
          <th>File Name</th>
          <th>Format</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>Round1_Submission_Abstract.md</code></td>
          <td>Markdown</td>
          <td>The exact 1,000-word, 8-section technical abstract to copy into the portal or Google Docs.</td>
        </tr>
        <tr>
          <td><code>architecture_diagram.png</code></td>
          <td>PNG (2400px)</td>
          <td>Ultra-high-resolution system architecture diagram detailing layers, tensors, and data flow.</td>
        </tr>
        <tr>
          <td><code>architecture_diagram.svg</code></td>
          <td>SVG</td>
          <td>Scalable vector graphic source file for crisp, lossless zooming.</td>
        </tr>
        <tr>
          <td><code>Round1_Submission_Document.html</code></td>
          <td>HTML</td>
          <td>Self-contained, printable submission document (Abstract + Embedded Diagram) ready for PDF export via <code>Cmd + P</code>.</td>
        </tr>
        <tr>
          <td><code>PERCEPTRON_HACKATHON_MASTER_REPORT.md</code></td>
          <td>Markdown</td>
          <td>Comprehensive master intelligence, evaluation, and implementation report.</td>
        </tr>
      </tbody>
    </table>

    <div class="footer">
      <strong>IITB-Optiver AI Innovation Lab • Perceptron Hackathon 2026</strong><br>
      Official Competition Master Document | Prepared for IIT Bombay Techfest Finals
    </div>
  </div>
</body>
</html>
'''

with open('/Users/vijayyadav/Desktop/perceptron/PERCEPTRON_HACKATHON_MASTER_REPORT.html', 'w') as f:
    f.write(html_content)

print('Successfully generated PERCEPTRON_HACKATHON_MASTER_REPORT.html')

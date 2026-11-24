import base64

with open('/Users/vijayyadav/Desktop/perceptron/architecture_diagram.png', 'rb') as img_f:
    img_b64 = base64.b64encode(img_f.read()).decode('utf-8')

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CREED - Round 1 Submission Document | Perceptron Hackathon 2026</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');
    
    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      line-height: 1.55;
      color: #1e293b;
      background-color: #f8fafc;
      margin: 0;
      padding: 40px 20px;
    }}

    .container {{
      max-width: 960px;
      margin: 0 auto;
      background: #ffffff;
      padding: 50px 60px;
      box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.08);
      border-radius: 12px;
      border: 1px solid #e2e8f0;
    }}

    .header {{
      border-bottom: 2px solid #0284c7;
      padding-bottom: 20px;
      margin-bottom: 30px;
    }}

    .badge {{
      display: inline-block;
      background: #e0f2fe;
      color: #0369a1;
      font-size: 11px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 6px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 12px;
    }}

    h1 {{
      font-size: 26px;
      font-weight: 800;
      color: #0f172a;
      margin: 0 0 8px 0;
      letter-spacing: -0.5px;
    }}

    .subtitle {{
      font-size: 15px;
      color: #475569;
      font-weight: 500;
      margin: 0 0 16px 0;
    }}

    .meta-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
      background: #f1f5f9;
      padding: 14px 18px;
      border-radius: 8px;
      font-size: 13px;
    }}

    .meta-item strong {{
      color: #0f172a;
    }}

    h2 {{
      font-size: 16px;
      font-weight: 700;
      color: #0284c7;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-top: 32px;
      margin-bottom: 12px;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 6px;
    }}

    p {{
      font-size: 14px;
      color: #334155;
      margin: 0 0 14px 0;
      text-align: justify;
    }}

    ul {{
      margin: 0 0 14px 0;
      padding-left: 20px;
      font-size: 14px;
      color: #334155;
    }}

    li {{
      margin-bottom: 6px;
    }}

    code {{
      font-family: 'JetBrains Mono', monospace;
      background: #f1f5f9;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 12.5px;
      color: #0369a1;
    }}

    .table-container {{
      margin: 18px 0;
      overflow-x: auto;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
    }}

    th {{
      background: #0f172a;
      color: #ffffff;
      text-align: left;
      padding: 10px 14px;
      font-weight: 600;
    }}

    td {{
      padding: 10px 14px;
      border-bottom: 1px solid #e2e8f0;
      color: #334155;
    }}

    tr:nth-child(even) td {{
      background: #f8fafc;
    }}

    .diagram-section {{
      margin-top: 50px;
      page-break-before: always;
      border-top: 2px dashed #cbd5e1;
      padding-top: 40px;
    }}

    .diagram-section img {{
      width: 100%;
      height: auto;
      border-radius: 8px;
      box-shadow: 0 4px 14px rgba(0,0,0,0.12);
      border: 1px solid #334155;
    }}

    .diagram-caption {{
      text-align: center;
      font-size: 13px;
      color: #64748b;
      font-weight: 500;
      margin-top: 12px;
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
      .diagram-section {{
        page-break-before: always;
      }}
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <span class="badge">Techfest, IIT Bombay — Perceptron Hackathon 2026</span>
      <h1>CREED: Conformal Robustness &amp; Epistemic Evaluation for Event-Driven Decisions</h1>
      <div class="subtitle">Online Round 1 Technical Blueprint &amp; System Architecture Proposal</div>
      <div class="meta-grid">
        <div class="meta-item"><strong>Host Lab:</strong> IITB-Optiver AI Innovation Lab</div>
        <div class="meta-item"><strong>Track:</strong> Theme 6 (AI You Can Actually Trust)</div>
        <div class="meta-item"><strong>Problem Chosen:</strong> Problem 10 (Trusting Messy/Manipulated Text)</div>
        <div class="meta-item"><strong>Team Format:</strong> 3 Members | Submission Date: October 2026</div>
      </div>
    </div>

    <h2>Section 1: Problem &amp; Theme Chosen</h2>
    <p>
      We select <strong>Problem 10: "Trusting a Signal Extracted from Messy, Manipulated Text"</strong> under <strong>Theme 6: AI You Can Actually Trust</strong>. In modern electronic financial markets, quantitative models and autonomous execution agents increasingly rely on unstructured text (breaking news wires, regulatory filings, corporate disclosures, and algorithmic social sentiment) alongside microsecond-level order book and trade data. However, financial text is fundamentally adversarial: it is laden with epistemic noise, synthetic misinformation, hallucinated reporting, and deliberate market manipulation (such as promotional penny-stock shilling and coordinated pump-and-dump rumors). Our team is driven to solve the existential flaw of current AI trading agents: overconfident actions on unverified, manipulated textual signals. By marrying multi-modal representation learning with finite-sample conformal prediction, we propose <strong>CREED</strong> (<em>Conformal Robustness &amp; Epistemic Evaluation for Event-Driven Decisions</em>), an architecture that produces mathematically valid, distribution-free confidence intervals that dynamically expand under textual corruption, explicitly signaling execution systems to withhold capital from hazardous trades.
    </p>

    <h2>Section 2: Understanding of the Challenge</h2>
    <p>
      Standard natural language processing (NLP) models deployed in quantitative trading fail catastrophically in live environments due to two foundational statistical roadblocks:
    </p>
    <ul>
      <li><strong>The Overconfidence Fallacy under Distribution Shift:</strong> Deep neural models (e.g., FinBERT, RoBERTa, and LLMs) generate point predictions or uncalibrated softmax confidence scores. Under out-of-distribution (OOD) phrasing, semantic noise, or coordinated adversarial manipulation, these models yield severely uncalibrated, overconfident predictions. Traditional post-hoc calibration methods (Platt scaling, temperature scaling, isotonic regression) fundamentally assume independent and identically distributed (i.i.d.) stationary data—an assumption thoroughly invalidated by non-stationary financial volatility regimes.</li>
      <li><strong>Multi-Modal Asynchrony &amp; Spurious Attribution:</strong> Market microstructure data operates at continuous millisecond ticks, while news signals arrive intermittently and asynchronously. Simple feature concatenation causes neural networks to latch onto spurious correlations, erroneously attributing standard macroeconomic price drift to irrelevant background news headlines.</li>
    </ul>
    <p>
      <strong>The Core Technical Crux:</strong> Constructing a valid prediction set <code>C_t(X_t)</code> for forward returns <code>Y_{{t+h}}</code> such that the marginal coverage guarantee <code>P(Y_{{t+h}} ∈ C_t(X_t)) ≥ 1 - α</code> strictly holds across non-exchangeable, time-varying market conditions. Simultaneously, the interval width <code>|C_t(X_t)|</code> must act as an actionable epistemic uncertainty sensor that widens immediately when incoming text is corrupted, ambiguous, or manipulated.
    </p>

    <h2>Section 3: Proposed Approach</h2>
    <p>
      CREED is engineered around a tripartite pipeline: dual-stream representation encoders, cross-modal gated attention, and an adaptive conformal calibration engine:
    </p>
    <ul>
      <li><strong>Data Ingestion &amp; Asynchronous Alignment:</strong> We ingest the Financial News and Stock Price Integration Dataset (FNSPID; 1.5M+ timestamped articles linked to equities) augmented with Financial PhraseBank and SEC Form 8-K filings. Quantitative price/volume data is sourced at 1-minute and 5-minute resolutions via Polygon.io / Yahoo Finance, deriving log-returns <code>r_t</code>, volume imbalance (OFI), bid-ask spread <code>s_t</code>, and Parkinson realized volatility <code>σ_t</code>. An asynchronous forward-fill event window maps text at <code>t_0</code> to lookback features <code>[t_0 - τ, t_0]</code> and forward return targets <code>Y_{{t+h}} = ln(P_{{t+h}}/P_t)</code> for horizons <code>h ∈ {{5m, 15m, 1h}}</code>.</li>
      <li><strong>Dual-Stream Feature Encoders:</strong> 
        The <em>Semantic Stream</em> utilizes a pre-trained <code>ProsusAI/finbert</code> (or <code>modernbert-base</code>) fine-tuned with Low-Rank Adaptation (LoRA: rank <code>r=16</code>, <code>α=32</code>) over frozen backbone layers to extract contextual token embeddings <code>H_text ∈ R^{{L × 768}}</code>. The <em>Temporal Stream</em> employs a Dilated Temporal Convolutional Network (TCN) with causal residual blocks (dilations <code>d ∈ {{1, 2, 4, 8}}</code>) matching lookback horizon <code>τ = 60m</code>, generating price state representations <code>H_ts ∈ R^{{T × 128}}</code>.
      </li>
      <li><strong>Cross-Modal Attention Fusion (CMAF) with Gated Residuals:</strong> 
        Market queries probe semantic keys/values: <code>Q = H_ts · W_Q</code>, <code>K = H_text · W_K</code>, <code>V = H_text · W_V</code>. Crucially, we introduce an <em>Adaptive Text-Noise Suppression Gate</em>: <code>Z_fused = H_ts + λ_t ⊙ Softmax(QK^T / √d_k)V</code>, where <code>λ_t = σ(W_g[H_ts; C_v; Perplexity] + b_g)</code>. When text exhibits high perplexity or is ungrounded in trading volume, <code>λ_t → 0</code>, gracefully falling back to robust quantitative time-series dynamics.
      </li>
      <li><strong>Conformal Calibration Engine:</strong> 
        A multi-quantile head outputs conditional quantiles <code>q̂_{{α/2}}(X_t)</code>, <code>q̂_{{0.50}}(X_t)</code>, and <code>q̂_{{1-α/2}}(X_t)</code> via Pinball Loss. We wrap these outputs using <strong>Conformalized Quantile Regression (CQR)</strong> via <code>MAPIE</code> paired with <strong>Adaptive Conformal Inference (ACI)</strong> (Gibbs &amp; Candès). On a rolling calibration buffer <code>D_cal</code> (size <code>K = 500</code>), non-conformity scores <code>E_i = max(q̂_{{α/2}} - Y_i, Y_i - q̂_{{1-α/2}})</code> update nominal coverage via: <code>α_{{t+1}} = α_t + γ(α - err_t)</code>, guaranteeing exact coverage despite volatility clustering.
      </li>
      <li><strong>Epistemic Downstream Risk Gate:</strong> 
        When the calibrated prediction width <code>W_t = |C_t(X_t)|</code> breaches dynamic volatility threshold <code>τ_risk = k · σ_t</code>, an <strong>ABSTAIN &amp; WITHHOLD</strong> order is broadcast, canceling aggressive quotes and preventing toxic fills.
      </li>
    </ul>

    <h2>Section 4: Minimum Viable (MV) Scope</h2>
    <p>By the Round 2 prototype milestone, we will deliver:</p>
    <ul>
      <li><strong>End-to-End Pipeline:</strong> Feature extraction pipeline ingesting FinBERT text embeddings and multi-scale price series across 50 liquid US equities.</li>
      <li><strong>Trained Multi-Modal Model:</strong> Trained cross-modal attention network predicting 15-minute forward return quantiles.</li>
      <li><strong>Split Conformal Calibration:</strong> Integration with <code>MAPIE</code> producing valid 90% and 95% prediction intervals on held-out test splits.</li>
      <li><strong>Empirical Demonstration:</strong> Verifiable empirical proof that while uncalibrated point regressors suffer massive tail error during earnings announcements, CREED maintains empirical coverage <code>≥ 90%</code>.</li>
    </ul>

    <h2>Section 5: Stretch Ambitions</h2>
    <ul>
      <li><strong>Stretch Goal 1 (Online ACI under Volatility Shocks):</strong> Transitioning from static split conformal prediction to online Adaptive Conformal Inference, proving that empirical coverage remains rock-solid through abrupt macroeconomic regime shocks (e.g., Federal Reserve rate announcements).</li>
      <li><strong>Stretch Goal 2 (Adversarial Red-Teaming Testbed):</strong> Deploying an automated adversarial attack generator featuring: (a) synthetic LLM pump-and-dump prompts ("1000% breakout guaranteed" on stagnant volume), (b) syntactic inversion perturbations ("will not file bankruptcy" → "will file bankruptcy"), and (c) OCR/scraper noise. We will empirically verify that CREED’s interval width expands by <code>&gt; 200%</code>, triggering risk abstention.</li>
      <li><strong>Stretch Goal 3 (Efficiency &amp; Metric Benchmarking):</strong> Formal comparison of Winkler Scores and Mean Prediction Interval Width (MPIW) against Conformalized Monte Carlo Dropout and Bayesian Ensembles.</li>
    </ul>

    <h2>Section 6: Novelty &amp; Differentiation</h2>
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>Technical Dimension</th>
            <th>Starter Resources Baseline</th>
            <th>CREED Proposed Innovation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Feature Fusion</strong></td>
            <td>Simple concatenation of sentiment scores + prices</td>
            <td>Cross-Modal Gated Attention with adaptive textual suppression (<code>λ_t → 0</code>)</td>
          </tr>
          <tr>
            <td><strong>Conformal Setup</strong></td>
            <td>Static split conformal prediction (assumes i.i.d.)</td>
            <td>Adaptive Conformal Inference (ACI) on rolling non-stationary queues</td>
          </tr>
          <tr>
            <td><strong>Decision Utility</strong></td>
            <td>Passive error reporting</td>
            <td>Active <strong>Epistemic Abstention Gate</strong> preventing toxic execution slippage</td>
          </tr>
          <tr>
            <td><strong>Robustness Testing</strong></td>
            <td>Static evaluation on clean test splits</td>
            <td>Rigorous <strong>Adversarial Red-Teaming Testbed</strong> with synthetic manipulation injection</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2>Section 7: Evaluation Plan</h2>
    <ul>
      <li><strong>Benchmark Datasets:</strong> FNSPID (1.5M headlines), SEC 8-K filings, Financial PhraseBank, and Polygon.io 1-min tick bars (2021–2024).</li>
      <li><strong>Baselines for Comparison:</strong> (1) Unimodal Time-Series TCN (pure price data); (2) Uncalibrated Multi-Modal Network (FinBERT + TCN with MSE loss); (3) Static Conformal Baseline (standard MAPIE split conformal without temporal adaptation).</li>
      <li><strong>Evaluation Metrics:</strong>
        <ul>
          <li><em>Empirical Coverage Rate:</em> <code>(1/N) ∑ 𝕀(Y_t ∈ C_t(X_t))</code> (target: <code>≥ 1 - α = 90%</code>).</li>
          <li><em>Sharpness / Efficiency:</em> Mean Prediction Interval Width (<code>MPIW = (1/N) ∑ |C_t(X_t)|</code>).</li>
          <li><em>Winkler Score:</em> Joint metric penalizing excessive interval width and rewarding valid coverage.</li>
          <li><em>Economic Trading Utility:</em> Simulated Sharpe Ratio and Maximum Drawdown when withholding execution under interval explosion vs. naive continuous trading.</li>
        </ul>
      </li>
    </ul>

    <h2>Section 8: Feasibility and Risks</h2>
    <ul>
      <li><strong>Team Skill Matrix (3 Members):</strong>
        <ul>
          <li><em>Member 1 (NLP &amp; Multi-Modal DL Lead):</em> Transformer architectures, HuggingFace, LoRA parameter-efficient fine-tuning, cross-attention implementation.</li>
          <li><em>Member 2 (Time-Series &amp; Conformal Statistics Lead):</em> Temporal Convolutional Networks, MAPIE framework, non-exchangeable ACI formulation, statistical hypothesis tests.</li>
          <li><em>Member 3 (Data Pipeline &amp; Systems Lead):</em> High-frequency data alignment, adversarial perturbation generation, Streamlit visualization UI, latency profiling.</li>
        </ul>
      </li>
      <li><strong>Development Milestones:</strong> Weeks 1–2 (Data pipeline, TCN baseline); Weeks 3–4 (Cross-modal attention, MAPIE CQR integration); Week 5 (ACI temporal adaptation, adversarial red-teaming); Week 6 (Interactive demo UI, stress testing, documentation).</li>
      <li><strong>Identified Risks &amp; Mitigation:</strong>
        <ul>
          <li><em>Risk:</em> Non-exchangeability in financial time series causes undercoverage. <em>Mitigation:</em> Adopt Gibbs &amp; Candès Adaptive Conformal Inference (ACI) with dynamic error feedback.</li>
          <li><em>Risk:</em> Asynchronous latency between news release and price response. <em>Mitigation:</em> Multi-scale forward evaluation horizons (<code>h ∈ [5m, 60m]</code>) with exponential decay weighting.</li>
        </ul>
      </li>
    </ul>

    <div class="diagram-section">
      <h2>System Architecture Diagram</h2>
      <img src="data:image/png;base64,{img_b64}" alt="CREED System Architecture Diagram">
      <div class="diagram-caption">Figure 1: CREED End-to-End Architectural Data Flow — Dual-Stream Encoders, Cross-Modal Gated Attention, Adaptive Conformal Inference (ACI), and Epistemic Abstention Gate.</div>
    </div>
  </div>
</body>
</html>
'''

with open('/Users/vijayyadav/Desktop/perceptron/Round1_Submission_Document.html', 'w') as f:
    f.write(html_content)

print('Successfully generated Round1_Submission_Document.html')

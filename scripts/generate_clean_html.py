import base64

with open('/Users/vijayyadav/Desktop/perceptron/architecture_diagram.png', 'rb') as f:
    img_b64 = base64.b64encode(f.read()).decode('utf-8')

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CREED - Technical Abstract | Vijay Yadav (IIT Bombay)</title>
  <!-- MathJax for rendering math formulas -->
  <script>
    MathJax = {{
      tex: {{
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
      }},
      svg: {{
        fontCache: 'global'
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
      max-width: 900px;
      margin: 0 auto;
      background: #ffffff;
      padding: 40px 50px;
    }}

    .doc-header {{
      text-align: center;
      border-bottom: 2px solid #0f172a;
      padding-bottom: 24px;
      margin-bottom: 30px;
    }}

    h1 {{
      font-size: 25px;
      font-weight: 700;
      color: #0f172a;
      margin: 0 0 10px 0;
      line-height: 1.3;
      letter-spacing: -0.3px;
    }}

    .author-block {{
      font-size: 16px;
      font-weight: 600;
      color: #1e293b;
      margin: 6px 0 0 0;
    }}

    .affiliation {{
      font-size: 14px;
      color: #475569;
      margin-top: 2px;
      font-style: italic;
    }}

    h2 {{
      font-family: 'Inter', sans-serif;
      font-size: 15px;
      font-weight: 700;
      color: #0f172a;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      margin-top: 32px;
      margin-bottom: 12px;
      border-bottom: 1px solid #cbd5e1;
      padding-bottom: 5px;
    }}

    p {{
      font-size: 14.5px;
      color: #1e293b;
      margin: 0 0 14px 0;
      text-align: justify;
      text-justify: inter-word;
    }}

    ul, ol {{
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
      background: #f1f5f9;
      padding: 2px 5px;
      border-radius: 3px;
      font-size: 12.5px;
      color: #0f172a;
      border: 1px solid #e2e8f0;
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
      font-size: 13.5px;
      margin: 20px 0;
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

    .diagram-container {{
      margin-top: 50px;
      page-break-before: always;
      padding-top: 30px;
      border-top: 2px solid #0f172a;
      text-align: center;
    }}

    .diagram-container img {{
      width: 100%;
      height: auto;
      border: 1px solid #0f172a;
      border-radius: 4px;
    }}

    .diagram-caption {{
      font-family: 'Inter', sans-serif;
      font-size: 13px;
      color: #475569;
      margin-top: 10px;
      text-align: center;
      font-style: italic;
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
      .diagram-container {{
        page-break-before: always;
      }}
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="doc-header">
      <h1>CREED: Conformal Robustness &amp; Epistemic Evaluation for Event-Driven Decisions</h1>
      <div class="author-block">Vijay Yadav</div>
      <div class="affiliation">Indian Institute of Technology Bombay (IIT Bombay)</div>
    </div>

    <h2>Section 1: Problem &amp; Theme Chosen</h2>
    <p>
      We address Problem 10 (&ldquo;Trusting a Signal Extracted from Messy, Manipulated Text&rdquo;) under Theme 6 (&ldquo;AI You Can Actually Trust&rdquo;). Automated trading systems and quantitative risk pipelines increasingly ingest unstructured text&mdash;such as regulatory 8-K disclosures, news wires, and social commentary&mdash;alongside high-frequency order book and trade data. However, financial text is highly non-stationary and frequently manipulated by rumors, promotional spam, and coordinated pump-and-dump campaigns. Current machine learning models tend to issue overconfident point predictions on these corrupted signals, exposing execution algorithms to severe adverse selection. We propose CREED (Conformal Robustness &amp; Epistemic Evaluation for Event-Driven Decisions), an end-to-end framework that couples dual-stream feature representation with adaptive conformal inference. Rather than forcing point predictions, CREED outputs statistically guaranteed prediction intervals that dynamically widen under textual corruption, explicitly signaling execution algorithms when to withhold capital.
    </p>

    <h2>Section 2: Understanding of the Challenge</h2>
    <p>
      Natural language processing systems applied to quantitative finance consistently stumble on two fundamental technical hurdles:
    </p>
    <ul>
      <li><strong>The Overconfidence Fallacy under Distribution Shift:</strong> Deep language backbones (such as FinBERT or LLMs) output uncalibrated softmax scores or point regression estimates. When confronted with out-of-distribution phrasing, rhetorical hyperbole, or deliberate misdirection, their predicted probabilities diverge sharply from true error distributions. Standard calibration approaches (Platt scaling, temperature scaling, isotonic regression) depend on the assumption of independent and identically distributed (i.i.d.) stationary data&mdash;an assumption that fails during volatile market regimes.</li>
      <li><strong>Multi-Modal Asynchrony &amp; Spurious Attribution:</strong> High-frequency price and volume data evolve in continuous millisecond time, whereas unstructured news arrives intermittently. Naive concatenation of text embeddings with tabular price features causes deep neural networks to memorize spurious co-occurrences, attributing normal market drift to irrelevant background text.</li>
    </ul>
    <p>
      <strong>Core Technical Crux:</strong> Constructing a valid prediction set $C_t(X_t)$ for forward returns $Y_{{t+h}}$ such that the marginal coverage guarantee:
    </p>
    <div class="math-display">
      $$\mathbb{{P}}(Y_{{t+h}} \in C_t(X_t)) \ge 1 - \alpha$$
    </div>
    <p>
      strictly holds under non-exchangeable, non-stationary market conditions. Concurrently, the interval width:
    </p>
    <div class="math-display">
      $$W_t = |C_t(X_t)|$$
    </div>
    <p>
      must serve as an empirical proxy for epistemic uncertainty, expanding immediately when textual inputs are corrupted, ambiguous, or detached from market liquidity.
    </p>

    <h2>Section 3: Proposed Approach</h2>
    <p>
      CREED consists of dual-stream feature extraction, cross-modal gated attention, and an online conformal calibration engine:
    </p>
    <ul>
      <li><strong>Data Ingestion &amp; Alignment:</strong>
        We utilize the Financial News and Stock Price Integration Dataset (FNSPID; 1.5M+ articles) combined with SEC Form 8-K filings and Financial PhraseBank. Market data is sourced from Polygon.io / Yahoo Finance at 1-minute and 5-minute bar frequencies, calculating log returns $r_t$, order flow imbalance $\text{{OFI}}_t$, bid-ask spread $s_t$, and Parkinson realized volatility $\sigma_t$. An asynchronous forward-fill event window maps text published at $t_0$ to historical market features $[t_0 - 60\text{{m}}, t_0]$ and forward return targets:
        <div class="math-display">
          $$Y_{{t_0+h}} = \ln\left(\frac{{P_{{t_0+h}}}}{{P_{{t_0}}}}\right), \quad h \in \{{5\text{{m}}, 15\text{{m}}, 60\text{{m}}\}}$$
        </div>
      </li>
      <li><strong>Dual-Stream Feature Encoders:</strong>
        The <em>Semantic Stream</em> uses a pre-trained <code>ProsusAI/finbert</code> encoder fine-tuned using Low-Rank Adaptation (LoRA: rank $r=16$, scale $\alpha=32$) on frozen lower transformer weights, producing $H_{{\text{{text}}}} \in \mathbb{{R}}^{{B \times 128 \times 768}}$. The <em>Temporal Stream</em> uses a Dilated Causal Temporal Convolutional Network (TCN) with 4 residual blocks (dilations $d \in \{{1, 2, 4, 8\}}$, kernel size $k=3$, receptive field $R = 61$ minutes), generating $H_{{\text{{ts}}}} \in \mathbb{{R}}^{{B \times 60 \times 128}}$.
      </li>
      <li><strong>Cross-Modal Attention Fusion (CMAF) with Gated Residuals:</strong>
        Market price states act as Queries, while text tokens provide Keys and Values:
        <div class="math-display">
          $$Q = H_{{\text{{ts}}}} W_Q, \quad K = H_{{\text{{text}}}} W_K, \quad V = H_{{\text{{text}}}} W_V$$
          $$\text{{Attention}}(Q, K, V) = \text{{softmax}}\left(\frac{{Q K^T}}{{\sqrt{{d_k}}}}\right) V \in \mathbb{{R}}^{{B \times T \times 128}}$$
        </div>
        We implement an <em>Adaptive Text-Noise Suppression Gate</em> where a scalar $\lambda_t \in [0, 1]$ is computed from the representations and text perplexity $\text{{PPL}}(x)$:
        <div class="math-display">
          $$\lambda_t = \sigma(W_g [H_{{\text{{ts}}}}; C_v; \text{{PPL}}(x)] + b_g), \quad Z_{{\text{{fused}}}} = H_{{\text{{ts}}}} + \lambda_t \odot C_v$$
        </div>
        When text is noisy or ungrounded, $\lambda_t \to 0$, suppressing text and falling back to pure price dynamics.
      </li>
      <li><strong>Conformal Uncertainty Quantification:</strong>
        A multi-quantile projection head estimates conditional quantiles $\hat{{q}}_{{0.05}}(X_t)$, $\hat{{q}}_{{0.50}}(X_t)$, and $\hat{{q}}_{{0.95}}(X_t)$ via the asymmetric Pinball loss:
        <div class="math-display">
          $$\mathcal{{L}}_q(y, \hat{{q}}) = \max(q(y - \hat{{q}}), (1 - q)(\hat{{q}} - y))$$
        </div>
        Non-conformity scores are tracked across a rolling calibration window $\mathcal{{D}}_{{\text{{cal}}}}$ of size $K = 500$:
        <div class="math-display">
          $$E_i = \max(\hat{{q}}_{{0.05}}(X_i) - Y_i, \; Y_i - \hat{{q}}_{{0.95}}(X_i))$$
        </div>
        We apply <strong>Adaptive Conformal Inference (ACI)</strong> (Gibbs &amp; Cand&egrave;s) to adjust nominal coverage online under non-stationary market regimes:
        <div class="math-display">
          $$\alpha_{{t+1}} = \alpha_t + \gamma (\alpha - \text{{err}}_t), \quad \gamma = 0.005, \quad \text{{err}}_t = \mathbb{{I}}(Y_t \notin C_t(X_t))$$
        </div>
        The calibrated prediction interval is given by:
        <div class="math-display">
          $$C_t(X_t) = \left[\hat{{q}}_{{0.05}}(X_t) - \hat{{Q}}_{{1-\alpha_t}}(E), \; \hat{{q}}_{{0.95}}(X_t) + \hat{{Q}}_{{1-\alpha_t}}(E)\right]$$
        </div>
        This guarantees long-run marginal coverage: $\lim_{{T \to \infty}} \frac{{1}}{{T}} \sum_{{t=1}}^T \mathbb{{I}}(Y_t \in C_t(X_t)) = 1 - \alpha$.
      </li>
      <li><strong>Downstream Risk Abstention Gate:</strong>
        If interval width $W_t = |C_t(X_t)|$ exceeds the dynamic volatility ceiling $\tau_{{\text{{risk}}}} = 2.5 \cdot \sigma_t^{{\text{{Parkinson}}}}$, the system raises an <strong>ABSTAIN &amp; WITHHOLD</strong> flag, preventing execution on noisy or manipulated text.
      </li>
    </ul>

    <h2>Section 4: Minimum Viable (MV) Scope</h2>
    <p>For the Round 2 benchmark, we will deliver an end-to-end working pipeline:</p>
    <ul>
      <li><strong>Data Processing Pipeline:</strong> Automated ingestion and alignment of FNSPID news articles with 1-minute bar data across 50 liquid US equities.</li>
      <li><strong>Trained Multi-Modal Model:</strong> Functional PyTorch implementation of the FinBERT LoRA and TCN encoders with cross-attention fusion.</li>
      <li><strong>Split Conformal Calibration:</strong> Integration with <code>MAPIE</code> producing valid 90% and 95% confidence intervals on out-of-sample data.</li>
      <li><strong>Empirical Validation:</strong> Concrete benchmark showing that while uncalibrated point forecasts fail during high-volatility earnings announcements, CREED maintains empirical coverage $\ge 90\%$.</li>
    </ul>

    <h2>Section 5: Stretch Ambitions</h2>
    <ul>
      <li><strong>Stretch Goal 1 (Online ACI under Volatility Shocks):</strong> Deploying the dynamic step-size updater $\alpha_{{t+1}}$ on rolling calibration queues, proving that coverage remains stable across sudden macroeconomic volatility shocks (e.g., Federal Reserve rate releases).</li>
      <li><strong>Stretch Goal 2 (Adversarial Red-Teaming Testbed):</strong> Constructing an automated perturbation harness that evaluates model response against: (a) synthetic pump-and-dump promotional claims generated via LLMs on flat volume, (b) subtle syntactic negations (&ldquo;company will not file Chapter 11&rdquo; vs &ldquo;will file Chapter 11&rdquo;), and (c) scraper/OCR character corruptions. We will empirically verify that interval width $W_t$ expands by $> 200\%$, triggering abstention.</li>
      <li><strong>Stretch Goal 3 (Multi-Horizon Efficiency Profiling):</strong> Benchmarking Winkler Scores and interval sharpness against Conformalized Monte Carlo Dropout and Bayesian Ensembles.</li>
    </ul>

    <h2>Section 6: Novelty &amp; Differentiation</h2>
    <table>
      <thead>
        <tr>
          <th>Technical Dimension</th>
          <th>Starter Resources Baseline</th>
          <th>CREED Proposed Approach</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Feature Fusion</strong></td>
          <td>Unweighted concatenation of sentiment polarity and price features</td>
          <td>Cross-modal attention with an adaptive noise gate ($\lambda_t \to 0$ under noisy text)</td>
        </tr>
        <tr>
          <td><strong>Exchangeability</strong></td>
          <td>Static split conformal prediction (assumes i.i.d. exchangeability)</td>
          <td>Adaptive Conformal Inference (ACI) on rolling non-stationary calibration buffers</td>
        </tr>
        <tr>
          <td><strong>Downstream Utility</strong></td>
          <td>Passive error reporting without execution hooks</td>
          <td>Active <strong>Epistemic Abstention Gate</strong> controlling trade routing and slippage</td>
        </tr>
        <tr>
          <td><strong>Robustness Testing</strong></td>
          <td>Static evaluation on unperturbed test sets</td>
          <td>Formal <strong>Adversarial Red-Teaming Suite</strong> testing synthetic manipulation</td>
        </tr>
      </tbody>
    </table>

    <h2>Section 7: Evaluation Plan</h2>
    <ul>
      <li><strong>Datasets:</strong> FNSPID (1.5M headlines), SEC Form 8-K filings, Financial PhraseBank, and Polygon.io 1-minute equity bars (2021&ndash;2024).</li>
      <li><strong>Baselines for Comparison:</strong> (1) Unimodal Time-Series TCN (pure price and volume without text); (2) Uncalibrated Multi-Modal Network (FinBERT + TCN with MSE loss); (3) Static Conformal Model (standard MAPIE split conformal without temporal adaptation).</li>
      <li><strong>Evaluation Metrics:</strong>
        <ul>
          <li><em>Empirical Coverage Rate:</em> $\frac{{1}}{{N}} \sum_{{t=1}}^N \mathbb{{I}}(Y_t \in C_t(X_t))$ (target: $\ge 1 - \alpha = 90\%$).</li>
          <li><em>Mean Prediction Interval Width (MPIW):</em> Average interval span across test samples (measures sharpness).</li>
          <li><em>Winkler Score:</em> Joint penalty function scoring interval width and penalizing boundary violations.</li>
          <li><em>Economic Trading Utility:</em> Simulated Sharpe ratio, maximum drawdown, and slippage reduction when withholding orders during interval expansion vs. continuous trading.</li>
        </ul>
      </li>
    </ul>

    <h2>Section 8: Feasibility and Risks</h2>
    <ul>
      <li><strong>Skill Distribution &amp; Implementation Readiness:</strong>
        <ul>
          <li>Strong foundation in deep learning systems, PyTorch multi-modal architectures, and HuggingFace transformer stacks.</li>
          <li>Solid grasp of statistical learning theory, quantile regression, and non-exchangeable conformal inference literature.</li>
          <li>Experience handling time-series pipelines, financial tick data normalization, and building low-latency inference wrappers using ONNX Runtime.</li>
        </ul>
      </li>
      <li><strong>Execution Timeline:</strong> Weeks 1&ndash;2 (Data pipeline, alignment, causal TCN); Weeks 3&ndash;4 (FinBERT LoRA fine-tuning, CMAF fusion, MAPIE quantile calibration); Week 5 (Online ACI integration, adversarial test harness); Week 6 (Streamlit demo UI, latency profiling, presentation prep).</li>
      <li><strong>Identified Risks &amp; Mitigation:</strong>
        <ul>
          <li><em>Risk:</em> Volatility clustering violates standard conformal exchangeability, leading to temporary undercoverage. <em>Mitigation:</em> Implement Gibbs &amp; Cand&egrave;s Adaptive Conformal Inference (ACI) with dynamic online error feedback.</li>
          <li><em>Risk:</em> Latency mismatch between breaking news publication and market reaction. <em>Mitigation:</em> Evaluate multi-scale forward return horizons ($h \in [5\text{{m}}, 60\text{{m}}]$) with exponential decay weighting.</li>
        </ul>
      </li>
    </ul>

    <div class="diagram-container">
      <h2>System Architecture Diagram</h2>
      <img src="data:image/png;base64,{img_b64}" alt="CREED System Architecture Diagram">
      <div class="diagram-caption">Figure 1: Architectural Data Flow of CREED &mdash; Dual-Stream Encoders, Cross-Modal Attention with Adaptive Text-Noise Gating, Adaptive Conformal Inference (ACI), and Epistemic Abstention Gate.</div>
    </div>
  </div>
</body>
</html>
'''

with open('/Users/vijayyadav/Desktop/perceptron/Round1_Submission_Document.html', 'w') as f:
    f.write(html_content)

print("Saved clean academic Round1_Submission_Document.html")

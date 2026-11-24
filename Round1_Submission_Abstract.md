# CREED: Trust-Gated Conformal Fusion of Financial Text & Market Microstructure

**Vijay Yadav**  
**IIT Bombay**  

---

### Section 1: Problem & Theme Chosen
We select **Problem 10: "Trusting a Signal Extracted from Messy, Manipulated Text"** under **Theme 6: AI You Can Actually Trust**. The foundational challenge of extracting an actionable trading signal from unstructured financial text is not predicting; it is knowing when not to believe the prediction. In electronic markets, quantitative execution agents ingest breaking news wires, corporate regulatory disclosures (SEC Form 8-K), and social sentiment alongside high-frequency microstructure feeds. However, financial text is inherently non-stationary, noisy, and frequently manipulated by promotional shilling, syndicated bot republishing, and coordinated pump-and-dump schemes. Standard machine learning models issue overconfident point forecasts on these corrupted inputs, exposing automated liquidity providers to severe adverse selection. We propose **CREED** (*Conformal Robustness & Epistemic Evaluation for Event-Driven Decisions*), an end-to-end multi-modal framework that fuses natural language processing with finite-sample conformal prediction. Rather than forcing fragile point estimates, CREED outputs statistically calibrated prediction intervals that dynamically widen under textual corruption, explicitly instructing execution routers when to deploy capital and when to abstain.

---

### Section 2: Understanding of the Challenge
Deploying text-driven prediction systems in financial markets entails three fundamental statistical roadblocks:

1. **The Overconfidence Fallacy under Distribution Shift & Failure of Exchangeability**: Standard conformal prediction guarantees exact marginal coverage only under exchangeable data. Financial time series, however, are strongly non-stationary, heteroskedastic, and subject to abrupt volatility clustering. Consequently, conventional split conformal algorithms may achieve 90% coverage on average over long historical spans, yet under-cover catastrophically during the volatile, event-driven shocks that carry the highest financial risk.
2. **The Marginal vs. Conditional Coverage Trap**: Marginal coverage is an insufficient safety guarantee in risk management. A model can achieve 90% coverage globally across a multi-year test set while its empirical coverage collapses to 50–60% specifically on days afflicted by promotional manipulation or syndicated spam. True trustworthiness requires *slice-conditional coverage* across explicit text-trust and market-volatility regimes.
3. **Multi-Modal Asynchrony, Spurious Attribution & Low Signal-to-Noise**: High-frequency order book and trade data arrive continuously at millisecond latency, whereas news headlines arrive intermittently and asynchronously. Naive feature concatenation encourages deep neural networks to overfit spurious co-occurrences, attributing normal market volatility drift to irrelevant background headlines. Because the underlying financial signal-to-noise ratio is tiny, honest prediction intervals must be wide; genuine economic value lies in rigorous calibration, detecting when intervals clear zero (statistically significant directional edge), and executing risk abstention.

**The Technical Crux**: Constructing a valid prediction region $C_t(X_t)$ for forward excess returns $Y_{t+h}$ such that the slice-conditional coverage guarantee:
$$\mathbb{P}(Y_{t+h} \in C_t(X_t) \mid G_t = g) \ge 1 - \alpha$$
strictly holds across distinct operational regimes $g = (\tau\text{-bucket} \times \sigma\text{-regime})$ under non-exchangeable conditions. Concurrently, the interval width $W_t = |C_t(X_t)|$ must serve as an active epistemic uncertainty sensor that expands immediately when incoming text is corrupted, syndicated, or contradicted by market microstructure.

---

### Section 3: Proposed Approach
CREED synthesizes dual-stream feature representation, an explicit 5-cue text-trust estimator, cross-modal attention fusion, and Mondrian conformalized quantile regression with online drift adaptation:

1. **Data Ingestion & Leakage-Safe Alignment**:
   * *Textual Corpus*: Financial News and Stock Price Integration Dataset (FNSPID; 1.5M+ articles) combined with Benzinga analyst ratings and SEC Form 8-K disclosure filings.
   * *Market Microstructure*: 1-minute and 5-minute equity bar data (Polygon.io / Yahoo Finance) coupled with daily OHLCV across 50 liquid US equities, extracting log returns $r_t$, order flow imbalance $\text{OFI}_t$, Garman–Klass volatility $\sigma_t$, volume z-scores, and bid-ask spread $s_t$.
   * *Leakage-Safe Alignment Protocol*: News published after 16:00 ET is deterministically mapped to the next trading day's open. Splits use an expanding walk-forward window with a strict 5-day embargo to eliminate lookahead leakage. Targets span multiple horizons: intraday $h \in \{15\text{m}, 60\text{m}\}$ and multi-day $h \in \{1\text{d}, 5\text{d}\}$ forward return in excess of the sector ETF benchmark:
     $$Y_{t_0+h} = \ln\left(\frac{P_{t_0+h}}{P_{t_0}}\right) - r_{t_0+h}^{\text{sector}}$$

2. **Text Branch & Learned 5-Cue Trust Estimator ($\tau$)**:
   * *Deduplication*: MinHash with Locality-Sensitive Hashing (LSH) removes syndicated press releases and bot-generated headline bursts.
   * *Dual Semantic Scoring*: A pre-trained `ProsusAI/finbert` encoder fine-tuned using Low-Rank Adaptation (LoRA: rank $r=16$, scaling factor $\alpha=32$) on frozen lower transformer layers generates token representations $H_{\text{text}} \in \mathbb{R}^{B \times L \times 768}$ and sentiment class probabilities $P(\text{pos}, \text{neg}, \text{neu})$. A secondary Loughran–McDonald domain-specific lexicon computes independent dictionary polarity. Attention pooling aggregates representations into a ticker-event vector $e_{\text{text}} \in \mathbb{R}^{128}$.
   * *5-Cue Trust Model*: A gradient-boosted decision tree (GBDT) estimates a continuous trust score $\tau_t \in [0, 1]$ from five forensic reliability cues:
     1. *Syndication / Duplication Rate*: Cluster cardinality in the MinHash-LSH index.
     2. *Cosine Novelty*: Distance against prior 7-day headline embedding centroids.
     3. *Lexicon Conflict*: Polarity divergence between FinBERT and Loughran–McDonald scores.
     4. *Source Entropy*: Shannon entropy across reporting news outlets.
     5. *Lagged Sentiment–Return Discordance*: Absolute divergence between headline tone and recent price trajectory.
   * *Dual Utilization*: The trust score $\tau_t$ operates simultaneously as a model fusion gate and as a partitioning group in Mondrian conformal calibration.

3. **Temporal Microstructure Stream**:
   * A Dilated Causal Temporal Convolutional Network (TCN) with 4 residual blocks (dilation factors $d \in \{1, 2, 4, 8\}$, kernel size $k=3$, receptive field $R = 61$ bars) processes the 6-channel microstructure tensor without future leakage, outputting $H_{\text{ts}} \in \mathbb{R}^{B \times T \times 128}$ and pooled vector $e_{\text{ts}} \in \mathbb{R}^{128}$. A rolling Garman–Klass volatility tercile assigns the volatility regime label $v_t \in \{\text{Low}, \text{Mid}, \text{High}\}$.

4. **Cross-Modal Attention Fusion (CMAF) with Trust Gating**:
   * Market queries probe semantic keys and values:
     $$Q = H_{\text{ts}} W_Q, \quad K = H_{\text{text}} W_K, \quad V = H_{\text{text}} W_V$$
     $$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V \in \mathbb{R}^{B \times T \times 128}$$
   * *Dual Trust-Gated Integration*: A neural gating scalar $\lambda_t = \sigma(W_g [H_{\text{ts}}; C_v; \text{PPL}(x)] + b_g)$ modulated by the explicit trust score $\tau_t$ governs text infusion:
     $$Z_{\text{fused}} = H_{\text{ts}} + (\tau_t \cdot \lambda_t) \odot C_v$$
     When text is corrupted or ungrounded ($\tau_t \to 0$ or high perplexity $\text{PPL}$), the multiplier collapses to zero, ensuring the architecture gracefully falls back to robust quantitative price dynamics. The dispersion scale is parameterized as $\hat{\sigma}_t = \text{softplus}(h(e_{\text{ts}}, e_{\text{text}}, 1 - \tau_t))$.

5. **Mondrian Conformalized Quantile Regression & Online ACI Engine**:
   * A multi-quantile neural projection head trained with asymmetric Pinball loss predicts conditional quantiles $\hat{q}_{0.05}(X_t)$, $\hat{q}_{0.50}(X_t)$, and $\hat{q}_{0.95}(X_t)$, eliminating restrictive Gaussian assumptions on fat-tailed returns:
     $$\mathcal{L}_q(y, \hat{q}) = \max(q(y - \hat{q}), (1 - q)(\hat{q} - y))$$
   * Residual-normalized non-conformity scores adapt to local volatility across a rolling calibration window $\mathcal{D}_{\text{cal}}$ of size $K = 500$:
     $$s_i = \max\left(\frac{\hat{q}_{0.05}(X_i) - Y_i}{\hat{\sigma}_i}, \; \frac{Y_i - \hat{q}_{0.95}(X_i)}{\hat{\sigma}_i}\right)$$
   * *Mondrian Calibration*: Scores are binned by operational slice $g = (\tau\text{-bucket} \times v\text{-regime})$, deriving group-specific thresholds $\hat{Q}_{1-\alpha_t}^{(g)}(s)$ to enforce slice-conditional validity:
     $$C_t(X_t) = \left[\hat{q}_{0.05}(X_t) - \hat{Q}_{1-\alpha_t}^{(g)}(s) \cdot \hat{\sigma}_t, \; \hat{q}_{0.95}(X_t) + \hat{Q}_{1-\alpha_t}^{(g)}(s) \cdot \hat{\sigma}_t\right]$$
   * *Online Adaptive Conformal Inference (ACI)*: To handle non-stationary volatility shocks, nominal target $\alpha_t$ updates online via Gibbs & Candès feedback:
     $$\alpha_{t+1} = \alpha_t + \gamma (\alpha - \text{err}_t), \quad \gamma = 0.005, \quad \text{err}_t = \mathbb{I}(Y_t \notin C_t(X_t))$$
     This guarantees long-run marginal coverage $\lim_{T \to \infty} \frac{1}{T} \sum_{t=1}^T \mathbb{I}(Y_t \in C_t(X_t)) = 1 - \alpha$.

6. **Selective Execution & Downstream Risk Gate**:
   * *Rule 1 (Selective Bet)*: Transmit aggressive directional order if $0 \notin C_t(X_t)$, $\tau_t \ge 0.65$, and $W_t \le \tau_{\text{risk}} = 2.5 \cdot \sigma_t$. The prediction interval strictly excludes zero, establishing a statistically significant directional edge with high textual trust.
   * *Rule 2 (Risk Abstention & Capital Preservation)*: Withhold orders, cancel active quotes, and widen spreads if $0 \in C_t(X_t)$, $\tau_t < 0.40$, or $W_t > \tau_{\text{risk}}$. This shields the execution agent from flash-crash adverse selection and toxic order flow.

---

### Section 4: Minimum Viable (MV) Scope
By the Round 2 prototype milestone, we will deliver an end-to-end working system:
* **Feature Pipeline**: Automated extraction of cached FinBERT embeddings, MinHash-LSH clusters, and TCN/microstructure features across 50 liquid US equities.
* **Trained Multi-Modal Model**: Functional PyTorch implementation of the dual-stream CMAF architecture predicting multi-quantile return bounds.
* **Conformal Calibration**: Integration with `MAPIE` producing valid 90% and 95% confidence intervals on out-of-sample walk-forward test splits.
* **Demonstration Deliverable**: Shipped as a reproducible Jupyter notebook and interactive Streamlit UI demonstrating both clean coverage validation and abstention flags prior to the December 1 midway check.

---

### Section 5: Stretch Ambitions
* **Stretch Goal 1: Online Adaptive Conformal Inference (ACI) & Mondrian Grouping under Shock Regimes**: Implementing dynamic online step-size updates across macro market shocks (e.g., FOMC rate releases), maintaining exact empirical coverage.
* **Stretch Goal 2: 4-Scenario Adversarial Red-Teaming Testbed**: Deploying an automated attack generator evaluating: (A) sentiment-flipping LLM headlines on flat volume; (B) coordinated duplicate bot bursts; (C) stale republishing of 7-day-old news; (D) 10–20% label noise in training returns. We will generate empirical "coverage-under-attack" curves proving worst-slice coverage stays within 3% of nominal ($\ge 87\%$) while naive baselines collapse below 62%.
* **Stretch Goal 3: Econometric & Risk Audit**: Formal backtesting using the Kupiec Proportion of Failures likelihood ratio test, Christoffersen conditional coverage test, Winkler interval score, and full risk-coverage curves across abstention sweeps.

---

### Section 6: Novelty & Differentiation
| Technical Dimension | Starter Resources Baseline | CREED Proposed Approach |
| :--- | :--- | :--- |
| **Text Trust Modeling** | None (treats all text as authentic) | Learned 5-cue forensic trust estimator ($\tau_t \in [0, 1]$) detecting syndication, novelty, and discordance |
| **Multi-Modal Fusion** | Unweighted concatenation of sentiment and price | Cross-modal gated attention with dual suppression: $Z_{\text{fused}} = H_{\text{ts}} + (\tau_t \cdot \lambda_t) \odot C_v$ |
| **Conformal Calibration** | Standard split conformal (assumes i.i.d. exchangeability) | Mondrian Non-Parametric CQR (Pinball loss) with Gibbs & Candès online ACI drift correction |
| **Coverage Guarantee** | Marginal coverage only (collapses on bad text) | **Slice-Conditional Coverage**: $\mathbb{P}(Y \in C(X) \mid G=g) \ge 1 - \alpha$ across trust $\times$ volatility regimes |
| **Decision Rule** | Passive interval reporting | Active **Selective Betting** ($0 \notin C(X)$) + **Dynamic Volatility Ceiling Abstention** |
| **Robustness Validation** | Static evaluation on clean test set | 4-scenario **Adversarial Red-Teaming Testbed** (sentiment flips, duplicate bursts, stale news, label noise) |

---

### Section 7: Evaluation Plan
* **Datasets**: FNSPID (1.5M headlines), Benzinga analyst ratings, SEC Form 8-K filings, and Polygon.io / Yahoo Finance 1-min and daily bars (2021–2024).
* **Five Baselines (B0 to B4)**:
  1. *B0 (Historical Quantile)*: Unconditional empirical return quantiles.
  2. *B1 (Price-Only TCN)*: Pure microstructure model with split conformal calibration.
  3. *B2 (Text-Only FinBERT)*: Unimodal language model with split conformal calibration.
  4. *B3 (Concatenation + Split Conformal)*: Standard starter recipe combining sentiment and price features.
  5. *B4 (Concatenation + EnbPI / ACI)*: Concatenation model wrapped with ensemble time-series conformal inference.
  * *Proposed*: CREED Gated CMAF with Mondrian CQR and online ACI.
* **Metrics**:
  * *Point Accuracy*: Root Mean Squared Error (RMSE), Directional Accuracy, and Rank Information Coefficient (IC).
  * *Interval Validity & Sharpness*: Empirical Coverage at 80/90/95%, Mean Prediction Interval Width (MPIW), and Winkler Interval Score.
  * *Regime & Slices*: Worst-slice coverage gap, rolling 60-day coverage stability, Kupiec test p-value, and Christoffersen independence test.
  * *Economic Trading Utility*: Simulated Sharpe ratio lift, maximum drawdown reduction, execution slippage reduction, and risk-coverage curves under selective bet rules.
* **Empirical Claim to Prove**: At equal nominal 90% coverage, CREED maintains worst-slice empirical coverage within ~3% of nominal ($\ge 87\%$) under both clean and attacked data, whereas baseline B3 drops below 62%, without unnecessary interval width inflation.

---

### Section 8: Feasibility and Risks
* **Skill Allocation & Implementation Readiness**:
  * Strong competencies in PyTorch deep learning, HuggingFace transformers, LoRA parameter-efficient adaptation, and MinHash deduplication algorithms.
  * Deep mathematical foundation in non-exchangeable conformal prediction, quantile regression, and financial econometric testing (Kupiec/Christoffersen).
  * Extensive experience in financial time-series engineering, walk-forward validation protocols, and low-latency inference pipelines via ONNX Runtime.
* **Execution Milestones**:
  * *Nov 1–10*: Ingestion pipeline, walk-forward splits, 5-day embargo, causal TCN, and baselines B0–B1.
  * *Nov 11–30*: FinBERT feature caching, 5-cue trust model, CMAF cross-attention training, and MAPIE CQR integration (MVP ready before Dec 1 midway check).
  * *Dec 1–10*: Mondrian grouping, online ACI updater, and the 4-scenario adversarial red-teaming test harness.
  * *Dec 11–14*: Econometric audit, risk-coverage curve generation, Streamlit UI demo, and jury defense preparation.
* **Identified Risks & Mitigations**:
  * *Risk 1 (Low Predictive Signal in Financial Text)*: Mitigated by evaluating calibration quality, interval sharpness, and selective zero-exclusion rather than relying on noisy directional point alpha.
  * *Risk 2 (Lookahead Leakage in Financial Time Series)*: Mitigated by the 16:00 ET mapping rule, expanding walk-forward windows, and an enforced 5-day embargo.
  * *Risk 3 (Non-Exchangeability during Volatility Shocks)*: Mitigated by Mondrian calibration across volatility terciles combined with online ACI step-size adaptation.
  * *Risk 4 (Unrealistic Synthetic Adversarial Attacks)*: Attack scenarios are explicitly calibrated against empirical penny-stock pump-and-dump anomalies and historical news syndication patterns.

# CREED: Trust-Gated Conformal Fusion of Financial Text & Market Microstructure

**IITB-Optiver Perceptron Hackathon 2026**  
**Theme 6: AI You Can Actually Trust**  
**Problem 10: Trusting a Signal Extracted from Messy, Manipulated Text**  

**Author:** Vijay Yadav  
**Affiliation:** Indian Institute of Technology Bombay (IIT Bombay)  

---

## 📌 Executive Summary

Quantitative trading algorithms ingest vast streams of unstructured natural language (news feeds, corporate SEC 8-K filings, social sentiment) alongside microsecond-level limit order book (LOB) data. However, financial text is highly non-stationary, noisy, and frequently manipulated by promotional shilling, syndicated bot republishing, and coordinated pump-and-dump campaigns. Standard deep learning models output overconfident point predictions on these corrupted inputs, exposing liquidity providers to severe adverse selection and tail risk.

**CREED** (*Conformal Robustness & Epistemic Evaluation for Event-Driven Decisions*) is an end-to-end multi-modal architecture that solves this fundamental problem. Rather than relying on fragile point predictions, CREED couples multi-dimensional textual trust scoring with finite-sample **time-series conformal prediction**, outputting statistically guaranteed prediction intervals that dynamically widen when text is corrupted or uncorroborated by market microstructure. When uncertainty is elevated, CREED triggers an automated **abstention policy**, protecting capital from toxic order flow.

---

## 🏛️ System Architecture

![CREED System Architecture](architecture_diagram.png)

The CREED architecture is structured across four tightly integrated pipelines:

1. **Textual Trust Engine (TTE)**: Multi-dimensional corruption scoring decomposing raw text into:
   - $\tau_{\text{source}}$: Source authority and historical reliability weighting.
   - $\tau_{\text{bot}}$: LLM/bot artifact detection via token log-perplexity variance.
   - $\tau_{\text{synd}}$: Syndication and botnet deduplication via MinHash LSH and cosine similarity.
   - $\tau_{\text{hyp}}$: Stylometric manipulation & promotional hype scoring (Flesch-Kincaid, exclamation density, capitalization).
   - $\tau_{\text{entity}}$: Named entity resolution & ticker verification against official SEC CIK cross-references.
   - **Composite Text Trust Score:**  
     $$\tau_t = \sum_{k} w_k \cdot \tau_{t}^{(k)} \in [0, 1]$$

2. **Asynchronous Cross-Modal Fusion**:
   - Ingests high-frequency LOB microstructure (10-level order book depth, trade flow imbalance $\text{OFI}_t$, microsecond return volatility $\sigma_t$) and discrete NLP embeddings.
   - Cross-attention transformer correlates text tokens against prevailing market order book imbalance.
   - **Cross-Modal Consistency Residual:** Computes the divergence between text sentiment and pre-announcement microstructure movement.

3. **Time-Series Conformal Calibration (Non-Exchangeable Setting)**:
   - To overcome exchangeability breakdown during financial volatility clustering, CREED utilizes **Adaptive Conformal Inference (ACI)** and **Normalized Locally Weighted Conformal Prediction**:
     $$\alpha_{t+1} = \alpha_t + \gamma (\alpha - \text{err}_t)$$
   - Computes non-conformity scores weighted by epistemic uncertainty and regime volatility.
   - Provides finite-sample validity guarantees across slice-conditional market regimes:
     $$\mathbb{P}(Y_{t+h} \in C_t(X_t) \mid G_t = g) \ge 1 - \alpha$$

4. **Trust-Gated Execution Router & Abstention Policy**:
   - Directional signal is generated if and only if the calibrated prediction interval $C_t(X_t) = [\hat{Y}_{\text{lower}}, \hat{Y}_{\text{upper}}]$ strictly excludes zero ($0 \notin C_t(X_t)$) AND composite trust exceeds threshold ($\tau_t \ge \tau_{\text{threshold}}$).
   - If intervals straddle zero or text is flagged as manipulated, the execution engine enters an **Abstention State (Cash Neutral)**.

---

## 📐 Mathematical Formulation

### 1. Conformal Prediction Set
Given a significance level $\alpha \in (0, 1)$ (e.g., target 90% coverage where $\alpha = 0.10$), CREED produces prediction set:
$$C_t(X_t) = \left[ \hat{\mu}(X_t) - q_{1-\alpha_t} \cdot \hat{\sigma}(X_t), \; \hat{\mu}(X_t) + q_{1-\alpha_t} \cdot \hat{\sigma}(X_t) \right]$$
where $q_{1-\alpha_t}$ is the empirical quantile of non-conformity scores over an exponential decaying rolling window, and $\hat{\sigma}(X_t)$ is the estimated conditional variance.

### 2. Execution Policy
$$\text{Action}_t = \begin{cases} 
\text{Long} & \text{if } \hat{Y}_{\text{lower}} > 0 \text{ and } \tau_t \ge \tau^* \\
\text{Short} & \text{if } \hat{Y}_{\text{upper}} < 0 \text{ and } \tau_t \ge \tau^* \\
\text{Abstain (Hold Cash)} & \text{if } 0 \in C_t(X_t) \text{ or } \tau_t < \tau^* 
\end{cases}$$

---

## 📊 Core Documents & Deliverables

| Document | Format | Description |
| :--- | :---: | :--- |
| **[CREED Round 1 Submission PDF](CREED_Round1_Submission_Vijay_Yadav_IIT_Bombay.pdf)** | PDF (1.2 MB) | Official print-ready 5-page submission document with complete 8-section abstract and full-page high-res architecture diagram. |
| **[Round 1 Abstract](Round1_Submission_Abstract.md)** | Markdown | Complete technical proposal text (~2,100 words including formal mathematical derivations, tables, and references). |
| **[Architecture Diagram (PNG)](architecture_diagram.png)** | Image (2400px) | Ultra-high-resolution vector rasterization of the end-to-end 4-pipeline architecture. |
| **[Architecture Diagram (SVG)](architecture_diagram.svg)** | Vector | Scalable vector graphic source file. |
| **[Interactive Submission HTML](Round1_Submission_Document.html)** | HTML | Self-contained HTML report with MathJax 3 LaTeX rendering and embedded SVG/PNG graphics. |
| **[Master Hackathon Strategy Report](PERCEPTRON_HACKATHON_MASTER_REPORT.md)** | Markdown | Exhaustive intelligence report analyzing all 10 hackathon problem statements, scoring rubric analysis, and 6-week execution roadmap. |

---

## 🎯 Target Milestones & Roadmap

- [x] **Milestone 1: Mathematical Formulation & Abstract Formulation (Round 1 Complete)**
  - Problem selection and core difficulty analysis.
  - Formal multi-modal conformal calibration guarantees.
  - End-to-end pipeline architecture specification.
- [ ] **Milestone 2: Data Pipeline & Baseline Construction (Round 2 — Weeks 1-2)**
  - Ingest FNSPID, SEC 8-K filings, and synthetic adversarial noise injections.
  - Build baseline RoBERTa/FinBERT sentiment extractor without conformal gating.
- [ ] **Milestone 3: Textual Trust Engine & Microstructure Cross-Attention (Round 2 — Weeks 3-4)**
  - Implement 5-dimensional trust scorer $\tau_t$.
  - Deploy cross-attention transformer aligning order book imbalance with textual tokens.
- [ ] **Milestone 4: Conformal Calibration & Execution Backtesting (Round 2 — Weeks 5-6)**
  - Deploy Adaptive Conformal Inference (ACI) and slice-conditional coverage verification.
  - Run event-driven execution backtests against adverse selection benchmarks.

---

## 👨‍💻 Author

**Vijay Yadav**  
Indian Institute of Technology Bombay (IIT Bombay)  
Perceptron Hackathon 2026 — Theme 6: AI You Can Actually Trust  
Host: IITB-Optiver AI Innovation Lab

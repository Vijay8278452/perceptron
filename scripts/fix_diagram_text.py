with open('architecture_diagram.svg', 'r') as f:
    text = f.read()

# Fix Mondrian text width
text = text.replace(
    '<text x="262" y="258" font-size="10.5" font-weight="700" fill="#0f172a" text-anchor="middle">C_t(X_t) = [ q̂_{0.05} - Q̂_{1-α_t}^{(g)}(s) · σ̂_t,   q̂_{0.95} + Q̂_{1-α_t}^{(g)}(s) · σ̂_t ]</text>',
    '<text x="262" y="258" font-size="9.2" font-weight="700" fill="#0f172a" text-anchor="middle">C_t(X_t) = [ q̂_{0.05} - Q̂_{1-α_t}^{(g)}(s)·σ̂_t,   q̂_{0.95} + Q̂_{1-α_t}^{(g)}(s)·σ̂_t ]</text>'
)

text = text.replace(
    '<text x="32" y="162" font-size="10.5" fill="#475569">Locally normalized by estimated dispersion σ̂_i; high-volatility days scale bands proportionally</text>',
    '<text x="32" y="162" font-size="10" fill="#475569">Locally normalized by estimated dispersion σ̂_i; high-volatility days scale bands proportionally</text>'
)

with open('architecture_diagram.svg', 'w') as f:
    f.write(text)

print("Adjusted font sizes for perfect fit")

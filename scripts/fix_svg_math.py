with open('architecture_diagram.svg', 'r') as f:
    text = f.read()

# Replace any backslashes in SVG text
text = text.replace('s_i = max\\left( \\frac{q̂_{0.05}(X_i) - Y_i}{σ̂_i},  \\frac{Y_i - q̂_{0.95}(X_i)}{σ̂_i} \\right)',
                    's_i = max( (q̂_{0.05}(X_i) - Y_i) / σ̂_i,  (Y_i - q̂_{0.95}(X_i)) / σ̂_i )')

with open('architecture_diagram.svg', 'w') as f:
    f.write(text)

print("Replaced backslash formula in SVG")

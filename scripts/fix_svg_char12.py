with open('architecture_diagram.svg', 'rb') as f:
    data = f.read()

# Replace any \x0c or \r or weird escape sequences
data = data.replace(b'\x0crac', b'frac')
data = data.replace(b'\\left(', b'(')
data = data.replace(b'\\right)', b')')
data = data.replace(b'frac{q\xcc\x82_{0.05}(X_i) - Y_i}{\xcf\x83\xcc\x82_i}', b'(q\xcc\x82_{0.05}(X_i) - Y_i) / \xcf\x83\xcc\x82_i')
data = data.replace(b'frac{Y_i - q\xcc\x82_{0.95}(X_i)}{\xcf\x83\xcc\x82_i}', b'(Y_i - q\xcc\x82_{0.95}(X_i)) / \xcf\x83\xcc\x82_i')

with open('architecture_diagram.svg', 'wb') as f:
    f.write(data)

# Let's verify line 220
with open('architecture_diagram.svg', 'r') as f:
    lines = f.readlines()
print('Line 220 now:', repr(lines[219]))

# Strings

text = "X-DSPAM-Confidence:    0.8475"
f = text.find("0")
x=float(text[f:40])
print(x)

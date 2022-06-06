# Strings
string = 'X-DSPAM-Confidence: 0.8475'
pos = string.find(':')
number = string[pos + 1:]
convert = float(number)
print(convert)

text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(":")
num_str = text[pos+1:].strip()
num = float(num_str)
print(num)
# Read the encrypted text
with open('/home/saide/Desktop/all-about-ctf-main/picoCTF/Reverse Engineering/Easy/transformation/enc', 'r', encoding='utf-8') as f:
    encrypted = f.read()

# List to store the decoded characters
decoded = []

for c in encrypted:
    code = ord(c)        # Get Unicode number
    high = (code >> 8)    # Top 8 bits (original first character)
    low = (code & 0xFF)   # Bottom 8 bits (original second character)
    decoded.append(chr(high))
    decoded.append(chr(low))

# Join the decoded characters
flag = ''.join(decoded)

print("Decoded flag:", flag)

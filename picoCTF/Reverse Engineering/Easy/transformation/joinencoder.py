# Read the flag (normal text)
with open('flag.txt', 'r') as f:
    flag = f.read().strip()

# Make sure the flag has even length (padding if necessary)
if len(flag) % 2 != 0:
    flag += '\x00'  # pad with null byte if odd length

# List to hold encoded characters
encoded = []

# Process two characters at a time
for i in range(0, len(flag), 2):
    first = ord(flag[i])      # Get ASCII code of first character
    second = ord(flag[i + 1]) # Get ASCII code of second character
    combined = (first << 8) + second  # Pack them together
    encoded.append(chr(combined))     # Turn into a single Unicode character

# Join the encoded characters
encrypted_text = ''.join(encoded)

# Write it to a file
with open('enc', 'w', encoding='utf-8') as f:
    f.write(encrypted_text)

print("Flag encoded and saved to 'enc'!")

# Read the encrypted content
with open('enc', 'r', encoding='utf-8') as f:
    enc = f.read()

# Convert each character to its corresponding hex value and join them
hex_string = ''.join([hex(ord(c)).lstrip("0x") for c in enc])

# Convert the hex string back to bytes and decode to reveal the flag
flag = bytes.fromhex(hex_string).decode()

# Print the decoded flag
print("Decoded flag:", flag)

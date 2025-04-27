import time
import base64
import hashlib
import sys
import secrets
import binascii
import codecs
import ast  # << NEW import

class Block:
    def __init__(self, index, previous_hash, timestamp, encoded_transactions, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.encoded_transactions = encoded_transactions
        self.nonce = nonce

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.encoded_transactions}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

def proof_of_work(previous_block, encoded_transactions):
    index = previous_block.index + 1
    timestamp = int(time.time())
    nonce = 0

    block = Block(index, previous_block.calculate_hash(), timestamp, encoded_transactions, nonce)

    while not is_valid_proof(block):
        nonce += 1
        block.nonce = nonce

    return block

def is_valid_proof(block):
    guess_hash = block.calculate_hash()
    return guess_hash[:2] == "00"

def decode_transactions(encoded_transactions):
    return base64.b64decode(encoded_transactions).decode('utf-8')

def get_all_blocks(blockchain):
    return blockchain

def blockchain_to_string(blockchain):
    block_strings = [f"{block.calculate_hash()}" for block in blockchain]
    return '-'.join(block_strings)

def encrypt(plaintext, inner_txt, key):
    midpoint = len(plaintext) // 2
    first_part = plaintext[:midpoint]
    second_part = plaintext[midpoint:]
    modified_plaintext = first_part + inner_txt + second_part

    block_size = 16
    plaintext = pad(modified_plaintext, block_size)
    key_hash = hashlib.sha256(key).digest()

    ciphertext = b''
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]
        cipher_block = xor_bytes(block, key_hash)
        ciphertext += cipher_block

    return ciphertext

def decrypt(ciphertext, key):
    block_size = 16
    inner_text = b''

    key_hash = hashlib.sha256(key).digest()

    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i + block_size]
        plaintext_block = xor_bytes(block, key_hash)
        inner_text += plaintext_block

    num_pad = inner_text[-1]
    inner_text = inner_text[:-num_pad]

    # remove blockchain pre/post padding
    inner_text = inner_text[162:]
    inner_text = inner_text[:-162]

    return inner_text

def pad(data, block_size):
    padding_length = block_size - len(data) % block_size
    padding = bytes([padding_length] * padding_length)
    return data.encode() + padding

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def generate_random_string(length):
    return secrets.token_hex(length // 2)

random_string = generate_random_string(64)

def main(token):
    key = bytes.fromhex(random_string)

    print("Key:", key)

    genesis_block = Block(0, "0", int(time.time()), "EncodedGenesisBlock", 0)
    blockchain = [genesis_block]

    for i in range(1, 5):
        encoded_transactions = base64.b64encode(
            f"Transaction_{i}".encode()).decode('utf-8')
        new_block = proof_of_work(blockchain[-1], encoded_transactions)
        blockchain.append(new_block)

    all_blocks = get_all_blocks(blockchain)
    blockchain_string = blockchain_to_string(all_blocks)
    encrypted_blockchain = encrypt(blockchain_string, token, key)

    print("Encrypted Blockchain:", encrypted_blockchain)

def main2(enc_file):
    with open(enc_file, 'r') as file:
        key_line = file.readline().strip()
        enc_blockchain_line = file.readline().strip()

        if key_line.startswith("Key:"):
            key_text = key_line[5:].strip()
            key = ast.literal_eval(key_text)  # 🛠️ fix: parse bytes
        else:
            raise ValueError("Invalid Key line format.")

        if enc_blockchain_line.startswith("Encrypted Blockchain:"):
            enc_text = enc_blockchain_line[22:].strip()
            encrypted_blockchain = ast.literal_eval(enc_text)  # 🛠️ fix: parse bytes
        else:
            raise ValueError("Invalid Blockchain line format.")

    decrypted_token = decrypt(encrypted_blockchain, key)
    print("Decrypted Token:", decrypted_token.decode('utf-8', errors='ignore'))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python block_chain_dec.py <enc_file>")
        sys.exit(1)

    text = sys.argv[1]
    main2(text)

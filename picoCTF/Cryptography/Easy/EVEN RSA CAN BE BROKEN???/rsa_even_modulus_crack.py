# # from Crypto.Util.number import inverse
# # from sympy import factorint

# # # === INPUT: Replace with your own values ===
# # N = 21574599938073278107952706043493359120604838577174767614172330500541370207129509610744973485117811069054157743594202693901845233747550163413776857029186122
# # e = 65537
# # ciphertext = 20942555760802740624394402810467426186693172363181294545254349403206237375187875930838132410724623263103189348562921353472749585137989119799760748058490591

# # # === STEP 1: Factor N ===
# # factors = factorint(N)
# # if len(factors) != 2:
# #     raise ValueError("N does not have exactly two prime factors. Not standard RSA.")

# # p, q = list(factors.keys())
# # print(f"[+] p = {p}")
# # print(f"[+] q = {q}")

# # # === STEP 2: Compute φ(N) ===
# # phi = (p - 1) * (q - 1)

# # # === STEP 3: Compute private exponent d ===
# # d = inverse(e, phi)
# # print(f"[+] d = {d}")

# # # === STEP 4: Decrypt ciphertext ===
# # m = pow(ciphertext, d, N)
# # print(f"[+] Decrypted integer = {m}")

# # # === STEP 5: Convert to string if possible ===
# # try:
# #     m_bytes = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')
# #     plaintext = m_bytes.decode('utf-8')
# #     print(f"[+] Plaintext message = {plaintext}")
# # except Exception as err:
# #     print(f"[!] Could not decode message: {err}")
# #     print(f"[+] Raw bytes = {m_bytes}")
# import time
# from Crypto.Util.number import inverse
# from sympy import factorint

# # === 🧠 LESSON CHALLENGE (RSA WEAKNESS: EVEN MODULUS) ===
# """
# 🔐 CHALLENGE:
# You are given the public RSA parameters and an encrypted message:

#     N = 21574599938073278107952706043493359120604838577174767614172330500541370207129509610744973485117811069054157743594202693901845233747550163413776857029186122
#     e = 65537
#     ciphertext = 20942555760802740624394402810467426186693172363181294545254349403206237375187875930838132410724623263103189348562921353472749585137989119799760748058490591

# 📌 Your task:
# Recover the original plaintext message by identifying and exploiting the weakness in the modulus N.

# Hint: N is even.
# """

# # === 💡 Styled Print Helpers ===
# def slow_print(msg, delay=0.03):
#     for ch in msg:
#         print(ch, end='', flush=True)
#         time.sleep(delay)
#     print()

# def header(title):
#     print("\033[1;36m" + "="*60)
#     print(f"{title.center(60)}")
#     print("="*60 + "\033[0m")

# def success(msg):
#     print("\033[1;32m[✔] " + msg + "\033[0m")

# def error(msg):
#     print("\033[1;31m[✘] " + msg + "\033[0m")

# def info(msg):
#     print("\033[1;34m[→] " + msg + "\033[0m")

# # === 🔐 Inputs ===
# N = 21574599938073278107952706043493359120604838577174767614172330500541370207129509610744973485117811069054157743594202693901845233747550163413776857029186122
# e = 65537
# ciphertext = 20942555760802740624394402810467426186693172363181294545254349403206237375187875930838132410724623263103189348562921353472749585137989119799760748058490591

# header("🔓 LESSON 03: CRACKING RSA WITH EVEN MODULUS")
# slow_print("Let's walk through decrypting this ciphertext by exploiting a weak RSA setup! 💥\n")

# # === STEP 1: Factor N ===
# info("Step 1: Factoring N... 🧮")
# time.sleep(1)
# factors = factorint(N)

# if len(factors) != 2:
#     error("N does not have exactly two prime factors. This is not standard RSA.")
#     exit()

# p, q = list(factors.keys())
# success(f"Found primes!\n   → p = {p}\n   → q = {q}\n")

# # === STEP 2: Compute φ(N) ===
# info("Step 2: Calculating Euler's Totient Function φ(N) = (p - 1)(q - 1)...")
# phi = (p - 1) * (q - 1)
# success(f"φ(N) = {phi}\n")

# # === STEP 3: Compute Private Exponent d ===
# info("Step 3: Computing modular inverse d ≡ e⁻¹ mod φ(N)...")
# d = inverse(e, phi)
# success(f"Private exponent d = {d}\n")

# # === STEP 4: Decrypt the Ciphertext ===
# info("Step 4: Decrypting ciphertext with m = c^d mod N...")
# m = pow(ciphertext, d, N)
# success(f"Decrypted integer m = {m}\n")

# # === STEP 5: Convert to Readable Message ===
# info("Step 5: Converting integer to bytes and decoding...")

# try:
#     m_bytes = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')
#     plaintext = m_bytes.decode('utf-8')
#     success(f"Plaintext message: \033[1;33m{plaintext}\033[0m\n")
# except Exception as err:
#     error(f"Could not decode the message: {err}")
#     print(f"[+] Raw bytes = {m_bytes}")

# # === ✅ Final Message ===
# header("✅ LESSON COMPLETE")
# slow_print("You cracked RSA with an even modulus! 🧠💥 Never use an even N!", 0.04)
import time
from Crypto.Util.number import inverse
from sympy import factorint

# === 💡 Styled Print Helpers ===
def slow_print(msg, delay=0.03):
    for ch in msg:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def header(title):
    print("\033[1;36m" + "="*60)
    print(f"{title.center(60)}")
    print("="*60 + "\033[0m")

def success(msg):
    print("\033[1;32m[✔] " + msg + "\033[0m")

def error(msg):
    print("\033[1;31m[✘] " + msg + "\033[0m")

def info(msg):
    print("\033[1;34m[→] " + msg + "\033[0m")


# === 🧠 CHALLENGE DEFINITION ===
N = 21574599938073278107952706043493359120604838577174767614172330500541370207129509610744973485117811069054157743594202693901845233747550163413776857029186122
e = 65537
ciphertext = 20942555760802740624394402810467426186693172363181294545254349403206237375187875930838132410724623263103189348562921353472749585137989119799760748058490591


# === 🧑‍🏫 PRESENT CHALLENGE TO LEARNER ===
header("🎯 CHALLENGE: RSA With Weak (Even) Modulus")

slow_print("You are given the following RSA parameters:\n", 0.04)
slow_print(f"    N  = {N}", 0.002)
slow_print(f"    e  = {e}", 0.01)
slow_print(f"    c  = {ciphertext}\n", 0.002)

slow_print("🧩 Task: Recover the original message from the ciphertext.\n", 0.04)
slow_print("💡 Hint: The modulus N is even. This makes it insecure.\n", 0.04)

time.sleep(2)

header("🔓 SOLVING: Breaking RSA Step by Step")

# === STEP 1: Factor N ===
info("Step 1: Factoring N... 🧮")
time.sleep(1)
factors = factorint(N)

if len(factors) != 2:
    error("N does not have exactly two prime factors. This is not standard RSA.")
    exit()

p, q = list(factors.keys())
success(f"Found primes!\n   → p = {p}\n   → q = {q}\n")

# === STEP 2: Compute φ(N) ===
info("Step 2: Calculating Euler's Totient Function φ(N) = (p - 1)(q - 1)...")
phi = (p - 1) * (q - 1)
success(f"φ(N) = {phi}\n")

# === STEP 3: Compute Private Exponent d ===
info("Step 3: Computing modular inverse d ≡ e⁻¹ mod φ(N)...")
d = inverse(e, phi)
success(f"Private exponent d = {d}\n")

# === STEP 4: Decrypt the Ciphertext ===
info("Step 4: Decrypting ciphertext with m = c^d mod N...")
m = pow(ciphertext, d, N)
success(f"Decrypted integer m = {m}\n")

# === STEP 5: Convert to Readable Message ===
info("Step 5: Converting integer to bytes and decoding...")

try:
    m_bytes = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')
    plaintext = m_bytes.decode('utf-8')
    success(f"Plaintext message: \033[1;33m{plaintext}\033[0m\n")
except Exception as err:
    error(f"Could not decode the message: {err}")
    print(f"[+] Raw bytes = {m_bytes}")

# === ✅ Final Message ===
header("✅ Congratulations!ss")
slow_print("You cracked RSA with an even modulus! 💥 Never use even N! 🧠🔐", 0.04)

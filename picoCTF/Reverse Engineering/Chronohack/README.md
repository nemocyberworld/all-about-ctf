#### Description

**Can you guess the exact token and unlock the hidden flag?**Our school relies on tokens to authenticate students. Unfortunately, someone leaked an important [file for token generation](https://challenge-files.picoctf.net/c_verbal_sleep/34be374fd7bba204c6d394c7460c58c4330b3d769116a4667025bf18b8074198/token_generator.py). Guess the token to get the flag.

Additional details will be available after launching your challenge instance.

## 🚩 **Challenge Type:**

**Time-based token brute-force using insecure PRNG**

---

## 💣 **Vulnerability:**

The server uses **`random.seed(time_in_milliseconds)`** to generate a **pseudo-random token** (probably a session token, login token, or registration code). Because:

* Python’s `random` module is deterministic.
* The `seed` is predictable (based on current time).

Anyone can **recreate the exact same random string** if they know **approximately when** it was generated.

---

## 🧠 **Challenge Mechanics:**

You are trying to guess the **correct 20-character token** generated using this logic:

```python
def get_random(length, seed):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    random.seed(seed)
    return ''.join(random.choice(alphabet) for _ in range(length))
```

The server likely expects this exact 20-char string from the user to "log in" or "verify"—and if correct, it prints the flag.

---

## 🕵️‍♂️ **Your Exploit Script:**

What you did:

1. You assumed the server called `random.seed(time_in_ms)` just before the token was generated.
2. You looped over a  **range of nearby times** , simulating what the server *might* have used as the seed.
3. For each possible time:
   * You generated a token with the same function.
   * You sent it to the server.
   * If the response wasn't "Sorry," you got the flag!

That’s called a  **time-based token brute-force attack** —and it **worked** because the token generation was:

* **Predictable**
* **Not cryptographically secure**

---

## 🧑‍🏫 **Real-World Lesson:**

This is why developers should **never** use `random.seed()` or Python’s `random` for cryptographic purposes.

Instead, they should use:

```python
import secrets
token = ''.join(secrets.choice(alphabet) for _ in range(length))
```

Or similar **CSPRNGs** (cryptographically secure PRNGs).

---

## 🎯 Summary:

* **Challenge Goal:** Recreate a token based on a predictable time seed.
* **Your Exploit:** Brute-force tokens based on likely generation time.
* **Vuln Type:** Insecure random token generation (time-seeded PRNG).
* **Fix:** Use `secrets` or OS-level secure randomness.

---

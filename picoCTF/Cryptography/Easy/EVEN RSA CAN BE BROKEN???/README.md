### 📌 Given:

* **N (modulus)** = `21574599938073278107952706043493359120604838577174767614172330500541370207129509610744973485117811069054157743594202693901845233747550163413776857029186122`
* **e (public exponent)** = `65537`
* **ciphertext (c)** = `20942555760802740624394402810467426186693172363181294545254349403206237375187875930838132410724623263103189348562921353472749585137989119799760748058490591`

---

![1746244519210](image/README/1746244519210.png)

### 🔍 Step 1: Check if `N` is Weak

If `N` is weak (e.g. too small, or has small/close prime factors), it may be factorable quickly. Let me try factoring `N` for you.

🛠️ **Attempting factorization...**

(This may take a moment depending on the size and complexity.)

Let me run a factorization check now.

✅ Success! We factored `N`:

* `p = 2`
* `q = 10787299969036639053976353021746679560302419288587383807086165250270685103564754805372486742558905534527078871797101346950922616873775081706888428514593061`

So `N = p × q`, and in this case `p = 2`, meaning  **`N` is even** , which is  **an insecure RSA configuration** .

---

### 🔓 Step 2: Compute Private Key `d`

We’ll now compute:

Then we’ll decrypt using:

![1746244567891](image/README/1746244567891.png)
Let’s compute the plaintext.

🔓 **Decryption Complete!**

The **plaintext (m)** is:

```
3030612722376619015339251852200174143198160267120074875669937770226045
```

If this number represents encoded text (e.g., ASCII or UTF-8), we can try converting it to a string. Would you like me to attempt that conversion?

![1746244275137](image/README/1746244275137.png)

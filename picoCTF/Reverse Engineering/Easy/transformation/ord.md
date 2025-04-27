# 🔥 What is `ord`?

* `ord(c)` is a **Python function** that:
  > **Takes a character** (like `'A'`, `'b'`, `'1'`, etc)
  >
  > **and gives you the integer (ASCII/Unicode) number for it** .
  >

Example:

```python
ord('A')  # -> 65
ord('B')  # -> 66
ord('0')  # -> 48
ord('!')  # -> 33
```

 **ASCII Table** : Every character you type (letter, number, symbol) has an underlying **number** — that's what `ord` gives you.

✅ `ord('A')` → `65`

✅ `ord('a')` → `97`

✅ `ord(' ')` → `32` (space)

---

# 🔥 How to **read** this kind of code:

Let's look again at your line:

```python
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

And break it  **slowly** :

|                Step                | Meaning                                                            |
| :---------------------------------: | :----------------------------------------------------------------- |
| `for i in range(0, len(flag), 2)` | Go through flag**two characters at a time**                  |
|    `flag[i]`and `flag[i+1]`    | Pick two letters                                                   |
|          `ord(flag[i])`          | Get number of first letter                                         |
|         `ord(flag[i+1])`         | Get number of second letter                                        |
|        `ord(flag[i]) << 8`        | Move the first letter number**8 bits left**(multiply by 256) |
|        `+ ord(flag[i+1])`        | Add the second letter number                                       |
|            `chr(...)`            | Turn the combined number into a**character**                 |
|         `''.join([...])`         | Glue all these new characters together                             |

---

# 🔥 Visual Example:

Suppose `flag = 'Hi'`

`H` → `ord('H') = 72`

`i` → `ord('i') = 105`

Now:

```python
(ord('H') << 8) + ord('i')
= (72 << 8) + 105
= (72 * 256) + 105
= 18432 + 105
= 18537
```

Then:

```python
chr(18537)
```

→ Some weird Unicode character.

---

# 🔥 Why does this matter?

This **combines 2 characters** (`H` and `i`) into **1 character** (special Unicode).

It's a form of **packing** or **hiding** data.

✅ Very common in  **CTFs** ,  **reverse engineering** ,  **binary protocols** .

---

# ✨ Short summary:

| Command    | What it does                        |
| :--------- | :---------------------------------- |
| `ord(c)` | Turn a character into a number      |
| `chr(n)` | Turn a number back into a character |

#### Description

**We invented a new cypher that uses "quantum entanglement" to encode the flag. Do you have what it takes to decode it?**Connect to the program with netcat:`$ nc verbal-sleep.picoctf.net 61849`The program's source code can be downloaded [here](https://challenge-files.picoctf.net/c_verbal_sleep/90141f0e9372fecd46d0143f5be59d7d3369394eae1c41cb733a254a5a3201b9/quantum_scrambler.py).

#### Solution:

we got a long srings from **nc**

then we got from cyberchef

![1745734913557](image/README/1745734913557.png)


Let's test:

![1745734967459](image/README/1745734967459.png)


#### Observerb the pattern 

![1745735248633](image/README/1745735248633.png)

**Let's build a python script to automate this**

![1745735329326](image/README/1745735329326.png)

Flag hex value:

![1745735426095](image/README/1745735426095.png)

Got the flag:

![1745735452100](image/README/1745735452100.png)

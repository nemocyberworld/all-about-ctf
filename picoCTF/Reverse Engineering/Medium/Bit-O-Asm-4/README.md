
#### Description

**Can you figure out what is in the** `eax` **register? Put your answer in the picoCTF flag format:** `picoCTF{n}` **where** `n` **is the contents of the** `eax` **register in the decimal number base. If the answer was** `0x11` **your flag would be** `picoCTF{17}`.**Download the assembly dump** [here](https://artifacts.picoctf.net/c/511/disassembler-dump0_d.txt).

#### Sol:

**main part to observe**

```
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    cmp    DWORD PTR [rbp-0x4],0x2710
<+29>:    jle    0x55555555514e <main+37>
<+31>:    sub    DWORD PTR [rbp-0x4],0x65
<+35>:    jmp    0x555555555152 <main+41>
<+37>:    add    DWORD PTR [rbp-0x4],0x65
<+41>:    mov    eax,DWORD PTR [rbp-0x4]
```

**or value in decimal:**

```
<+15>:    mov    DWORD PTR [rbp-0x4],654874
<+22>:    cmp    DWORD PTR [rbp-0x4],10000
<+29>:    jle    0x55555555514e <main+37>
<+31>:    sub    DWORD PTR [rbp-0x4],101
<+35>:    jmp    0x555555555152 <main+41>
<+37>:    add    DWORD PTR [rbp-0x4],101
<+41>:    mov    eax,DWORD PTR [rbp-0x4]
```

1. load `654874` to `[rbp-0x4]`
2. compare `654874` with `10000`
3. if `654874` is less than `10000` then next jump, but condition is not true so, jump will not happen
4. jump to `<main+37>` will not happen
5. subtract `101` from `654874 = 654874 - 101 = 654773`
6. then jump to `<main+41>`, so `<+37>` will not take part
7. load `654773` to `eax`
   so the flag is `picoCTF{654773}`

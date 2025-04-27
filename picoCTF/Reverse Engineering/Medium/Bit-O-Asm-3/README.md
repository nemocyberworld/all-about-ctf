#### Description

**Can you figure out what is in the** `eax` **register? Put your answer in the picoCTF flag format:** `picoCTF{n}` **where** `n` **is the contents of the** `eax` **register in the decimal number base. If the answer was** `0x11` **your flag would be** `picoCTF{17}`.**Download the assembly dump** [here](https://artifacts.picoctf.net/c/530/disassembler-dump0_c.txt).

#### Sol:

Look at this lines

```
<+15>:    mov    DWORD PTR [rbp-0xc],0x9fe1a
<+29>:    mov    eax,DWORD PTR [rbp-0xc]

<+22>:    mov    DWORD PTR [rbp-0x8],0x4
<+32>:    imul   eax,DWORD PTR [rbp-0x8]

<+36>:    add    eax,0x1f5

<+41>:    mov    DWORD PTR [rbp-0x4],eax
<+44>:    mov    eax,DWORD PTR [rbp-0x4]
```

#### Steps:

1. load `0x9fe1a` to `[rbp-0xc]`
3. load the value of `[rbp-0xc]` to `eax`
4. load `0x4` to `[rbp-0x8]`
5. multiply `[rbp-0x8]` with `eax`
   multiplication: `0x9fe1a * 0x4 = 0x27f868`
6. add `0x1f5` to `eax`
   addition: `0x27f868 + 0x1f5`
7. load `0x27f868 + 0x1f5` to `[rbp-0x4]`
8. then load the value of `[rbp-0x4]` to `eax`

so, eax value `0x27f868 + 0x1f5 = 0x27fa5d = 2619997 in decimal`
so the flag `picoCTF{2619997}`

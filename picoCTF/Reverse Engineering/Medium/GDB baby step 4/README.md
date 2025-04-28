
#### Description

`main` **calls a function that multiplies** `eax` **by a constant. The flag for this challenge is that constant in decimal base. If the constant you find is 0x1000, the flag will be** `picoCTF{4096}`.**Debug** [this](https://artifacts.picoctf.net/c/532/debugger0_d).


#### sol:

```
(gdb) disassemble main
Dump of assembler code for function main:
   0x000000000040111c <+0>:     endbr64
   0x0000000000401120 <+4>:     push   rbp
   0x0000000000401121 <+5>:     mov    rbp,rsp
   0x0000000000401124 <+8>:     sub    rsp,0x20
   0x0000000000401128 <+12>:    mov    DWORD PTR [rbp-0x14],edi
   0x000000000040112b <+15>:    mov    QWORD PTR [rbp-0x20],rsi
   0x000000000040112f <+19>:    mov    DWORD PTR [rbp-0x4],0x28e
   0x0000000000401136 <+26>:    mov    DWORD PTR [rbp-0x8],0x0
   0x000000000040113d <+33>:    mov    eax,DWORD PTR [rbp-0x4]
   0x0000000000401140 <+36>:    mov    edi,eax
   0x0000000000401142 <+38>:    call   0x401106 <func1>
   0x0000000000401147 <+43>:    mov    DWORD PTR [rbp-0x8],eax
   0x000000000040114a <+46>:    mov    eax,DWORD PTR [rbp-0x4]
   0x000000000040114d <+49>:    leave
   0x000000000040114e <+50>:    ret
End of assembler dump.
(gdb) info functions
All defined functions:

Non-debugging symbols:
0x0000000000401000  _init
0x0000000000401020  _start
0x0000000000401050  _dl_relocate_static_pie
0x0000000000401060  deregister_tm_clones
0x0000000000401090  register_tm_clones
0x00000000004010d0  __do_global_dtors_aux
0x0000000000401100  frame_dummy
0x0000000000401106  func1
0x000000000040111c  main
0x0000000000401150  __libc_csu_init
0x00000000004011c0  __libc_csu_fini
0x00000000004011c8  _fini
(gdb) disassemble func1 
Dump of assembler code for function func1:
   0x0000000000401106 <+0>:     endbr64
   0x000000000040110a <+4>:     push   rbp
   0x000000000040110b <+5>:     mov    rbp,rsp
   0x000000000040110e <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x0000000000401111 <+11>:    mov    eax,DWORD PTR [rbp-0x4]
   0x0000000000401114 <+14>:    imul   eax,eax,0x3269
   0x000000000040111a <+20>:    pop    rbp
   0x000000000040111b <+21>:    ret
End of assembler dump.
```


Look carefully and try to understand:

```
first look at this step:
<+33>:    mov    eax,DWORD PTR [rbp-0x4]
so we need to figure out what value contain [rbp-0x4], so we need to look at <+19>
<+19>:    mov    DWORD PTR [rbp-0x4],0x28e
then look eax value is transferedto edi
<+36>:    mov    edi,eax
then it call <func1> function
<+38>:    call   0x401106 <func1>
to see what functions are available run this command

info functions
find out func1

0x0000000000401106  func1

now  disassemble it

disassemble func1

look at this step
edi is moved to [rbp-0x4]
<+8>:     mov    DWORD PTR [rbp-0x4],edi
then [rbp-0x4] is moved to eax
<+11>:    mov    eax,DWORD PTR [rbp-0x4]
then eax is multiplied by 0x3269, which is our desired number to convert from hex to decimal
<+14>:    imul   eax,eax,0x3269

so our flag is picoCTF{12905}
```

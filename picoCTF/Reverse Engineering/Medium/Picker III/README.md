
#### Sol:

look source code carefully.

![1745916712632](image/README/1745916712632.png)

this function allows us to write in the table and

![1745916825099](image/README/1745916825099.png)

 it also execute our input with eval comand.

our main target is to call `win` function. let's add `win` function to the table to read the `flag` file

Here is our test flag

![1745917345081](image/README/1745917345081.png)


Let's do it

```
==> 1
1: print_table
2: read_variable
3: write_variable
4: getRandomNumber
==> 2
Please enter variable name to read: read_variable
<function read_variable at 0x7c2813207ba0>
==> 3
Please enter variable name to write: write_variable
Please enter new value of variable: win
==> 2
Please enter variable name to read: win
<function win at 0x7c2813228180>
==> 1
1: print_table
2: read_variable
3: write_variable
4: getRandomNumber
==> 3
0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x48 0x65 0x6c 0x6c 0x6f 0x7d 
==> quit
```


![1745917407654](image/README/1745917407654.png)


Let's get the final flag

![1745917521670](image/README/1745917521670.png)

![1745917543899](image/README/1745917543899.png)

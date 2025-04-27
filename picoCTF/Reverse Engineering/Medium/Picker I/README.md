#### Description

**This service can provide you with a random number, but can it do anything else?** 

Connect to the program with netcat:

`$ nc saturn.picoctf.net 54864`

The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/514/picker-I.py).

#### Solution

Source code is vulnerable.

functions are

```
getRandomNumber
exit
esoteric1
esoteric2
win
```

it's calling the function directly with corresponding name as input we provide

![1745748229257](image/README/1745748229257.png)

I tried to call **win**

![1745748276265](image/README/1745748276265.png)

Let's create a **flag.txt** file and check again

![1745748361920](image/README/1745748361920.png)

Let's check

Got our flag's corresponding hex

![1745748407198](image/README/1745748407198.png)

Now, let's get the final flag from **netcat**

![1745748463209](image/README/1745748463209.png)

![1745748491778](image/README/1745748491778.png)

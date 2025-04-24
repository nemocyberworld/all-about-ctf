#!/usr/bin/env python3

from pwn import *

import random
import time

def get_random(length, seed):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    random.seed(seed) #, version=1)
    s = ""
    for i in range(length):
        s += random.choice(alphabet)
    return s

found_flag = False

for adjust in range(-50, 1000, 40):
  print('=================== Adjustment: ' + str(adjust) + ' ==================')
  
  start_time = time.time()
  target_proc = remote(sys.argv[1], sys.argv[2])

  for i in range(0, 50):
    print('Tweak: ' + str(i + adjust))
    token = get_random(20, (int(start_time * 1000) + i + adjust)).encode("utf-8")

    x = target_proc.recvuntil(b'(or exit):')
    print(b'Tryng: ' + token)
    target_proc.sendline(token)
    y = target_proc.readline()
    if y[:5] != b'Sorry':
      print('*' * 160)
      print(y)
      print(target_proc.recvline())
      found_flag = True;
      break
    print(y)
  
  target_proc.close()

  if found_flag == True:
    break
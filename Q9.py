# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 15:17:36 2023

@author: abdul
"""

from pwn import xor	

message = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")


# The resulting XOR is "myXORke". It's safe to assume that the complete word is "myXORkey" thus the additional 'y'
partial_key = xor(message[:7], "crypto{").decode() + 'y'  

complete_key = (partial_key * (len(message)//len(partial_key)+1))[:len(message)]


flag = xor(message, complete_key)

print(flag.decode())
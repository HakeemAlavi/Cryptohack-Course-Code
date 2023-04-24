# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 15:01:20 2023

@author: abdul
"""
text = "label"
result = ""

for n in text:
    result += chr(ord(n)^13)

print(f"crypto{{{result}}}")
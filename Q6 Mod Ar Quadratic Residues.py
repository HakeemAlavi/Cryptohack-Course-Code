# -*- coding: utf-8 -*-
"""
Created on Sat May 13 17:59:09 2023

@author: abdul
"""

p = 29
ints = [14, 6, 11]

qr = [a for a in range(p-1) if pow(a,2,p) in ints]
print(min(qr))

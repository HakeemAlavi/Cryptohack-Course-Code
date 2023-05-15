# -*- coding: utf-8 -*-
"""
Created on Sun May  7 11:34:44 2023

@author: abdul
"""

def gcd(a,b):
    print(f"a = {a}, b = {b} - modulo result = {a%b}")
    while a%b != 0:
        c = a%b
        a = b
        b = c
        
        print(f"a = {a}, b = {b} - modulo result = {a%b}")
        
    return b
print(f"GCD: {gcd(66528,52920)}")
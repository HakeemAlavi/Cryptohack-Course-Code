# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:25:54 2023

@author: abdul
"""
text = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

print(bytes.fromhex(text).decode('utf-8'))

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:27:58 2023

@author: abdul
"""

import base64

text = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

result = bytes.fromhex(text)
print(base64.b64encode(result).decode('utf-8'))


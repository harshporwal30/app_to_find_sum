# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 22:20:32 2024

@author: Harsh
"""

valuea = input('enter number')
sum = 0
product = 1
count = 0
while (valuea != 'q'):
    value = int(valuea)
    sum = sum+value
    product = product * value
    count = count+1
    valuea = input('enter number')
else:
    print(sum, 'sum')
    print(product, 'product')
    print(sum/count, 'avg')

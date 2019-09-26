# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 12:16:02 2019

@author: Himanshu Khairajani
"""

import random
n=11
g=7


x=random.randint(1000,2000)
A = (g**x) % n

y=random.randint(1000,2000)
B = (g**y) % n

k1 = (B**x)%n
k2 = (A**y)%n

if (k1==k2):
    print("Key is %d",k1)

else:
    print("attackers attack")
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 14:14:05 2017

@author: Hunter Davis huntertigerdavis@gmail.com
@author Brianna Malaya Regan regan.briannamalaya@gmail.com
"""
def multiplication_table(x, y):
    print("", end = " ")
    for a in range(1, y + 1, 1):
        print("", a, end = "")
    print() 
    for b in range(1, x + 1, 1):
        print(b, end = " ")
        for c in range(1, y + 1, 1):
            print(b * c, end = " ")
        print()
multiplication_table(3, 4)
    

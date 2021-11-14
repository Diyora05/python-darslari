# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 18:06:22 2021

@author: Demo
"""

import turtle
window = turtle.Screen()
t = turtle.Turtle()
t.color('blue')

def kvadr():
    for i in range(4):
        t.forward(100)
        t.left(90)
for j in range(12):
    kvadr()
    t.left(30)

t.screen.mainloop()

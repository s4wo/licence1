#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def chiffres():
    i=0
    a=0
    while a!=1:
        i = i + 1
        a = 1+(1/(2)**i)
    return i
        
print(chiffres())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randrange


def lancerDe():
    return randrange(1,7)

def obtenirUnNombre(n):
    c = 0
    while lancerDe() != n: 
        c = c + 1
    return c

print(obtenirUnNombre(6))

def obtenirUnDouble(n):
    c = 0
    lancerDe() == c
    


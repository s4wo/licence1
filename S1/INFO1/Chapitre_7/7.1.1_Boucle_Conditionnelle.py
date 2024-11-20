#!/usr/bin/env python3
# -*- coding: utf-8 -*-

placement = 100
taux = 1

def interets(placement: int, taux: int):
    total = placement
    years = 0
    while total < placement*2 :
        total = total + (total/100*taux)
        years = years+1
    return years

print(interets(placement, taux))

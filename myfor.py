#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""

Programa em pytho que usa os conceito o de programação de repetição com for

"""
__author__ = "Luiz Santos"
__copyright__ = "Copyright 2020, by Santos"
__credits__ = "Todos desenvolvedores de software livre"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Luiz Santos"
__email__ = "luizcsbh@gmail.com"
__status__ = "Prototype"
__date__ = "4 March 2020"

#myFor
print("Exercicio do For")
for n  in range (2,10):
    for x in range (2,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""

Programa em pytho que usa o conceito de programação de Pilha

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

print("Pilha")
pilha = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
print("Minha Pilha: ", pilha)

pilha.append(1597)
print("Inserindo um elemento: ", pilha)

pilha.append(2584)
print("Inserindo um elemento: ", pilha)

pilha.pop()
print("Removendo um elemento: ", pilha)

pilha.pop()
print("Removendo um elemento: ", pilha)
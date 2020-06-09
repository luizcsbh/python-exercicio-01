#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""

Programa em pytho que usa os conceitos de recursividade e estrutura 
de dados do tipo LIFO(last-in first-ou), onde o último elemento a
ser inserido, será o primeiro a ser retirado) que cria uma sequencia
Fibonacci de acordo com a quantidade de termos informada pelo usuário
em  seguida e adiciona cada termo em um pilha e o usuário pode informar
a quantidade de termos que ele pode remover da pillha sendo que o número
não pode ser maior que a quantidade de termos da sequencia Fibonacci
inseridos na pilha.

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

print('-'*30)
print('Sequência de Fibonacci em Pilha')
print('-'*30)
term = int(input('Quantos termos a sequência deve ter?'))
pilha = []
t1 = 0
pilha.append(t1)
t2 = 1
pilha.append(t2)

print('~'*30)
print('{} → {}'.format(t1, t2),end='')
cont = 3
while cont <= term:
    t3 = t1 + t2
    pilha.append(t3)
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('→ FIM')
print('-'*30)
print("A pilha é: ",pilha)
print('-'*30)
num = int(input('Quantos termos deseja retirar?')) 
ret = 0
if num < term:
    while ret < num:
        pilha.pop()
        ret += 1
    print('-'*30)    
    print("A nova pilha é: ",pilha)
else:
    print('-'*30)    
    print("O número digitado é maior que o número de termos!")

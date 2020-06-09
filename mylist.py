#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""

Programa em pytho que usa o conceito de programação de Lista

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

#mylist
mylist =  ["banana","uva","pera","goiaba","morango","manga","melancia","abacate"]
#imprimindo mylist
print('-'*30)
print (mylist)
print('-'*30)
n = int(input('Informe qual indice que deseja acessar?'))
if n < 7:
    print("Exibindo o conteudo da List: ", mylist[n])
else:
    print("Número maior que o tamanho List que é 7")
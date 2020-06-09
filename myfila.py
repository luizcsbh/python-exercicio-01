#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""

Programa em pytho que usa o conceito de programação de Fila

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

#myFila
from collections import deque
#Criando uma fila 
fila = deque(["banana","uva","pera","goiaba","morango","manga","melancia","abacate"])
print("Minha Fila: ", fila)

#Adicionar um elemento
fila.append("laranja")
print("Adicionando um elemento: ",fila)

# Remover um elemento
fila.popleft()
print("Removendo um elemento: ", fila)
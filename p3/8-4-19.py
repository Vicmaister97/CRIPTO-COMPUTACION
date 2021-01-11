#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Autor: Víctor García Carrera victorgarcia@correo.ugr.es
	Cálculo de raíces cuadradas
	"""

import sys
from math import *
from random import *
from fractions import *
import numpy


"""
1. Raiz cuadrada de 263
s= 17
2.[182,182*112,...,182*112^16]		Pasos pequeños
[182,133,168,143,236!!,132,56...]
3. [112^17,112^2*17, 112^3*17,...,]
	141,156,167,140,15,11,236!!!	Pasos gigantes

logbase a (b) mod p
1. s = IntPorEncima [sqrt(p)]
2. S = [b, b*a, ... , b*a^s-1]
3. T = [a^s, a^2s, ... , a^(s^2)]
4 Si a^(t*s) = b*a^j
		Devuelv3e t*s -j

c = a^s mod p 								a^s 						112^(7*17) = 182 * 112^4
x = c 										a^s * a^s = a^2s			112^(7*17) * 112^-4= 182
tabla2=[X]									a^2s * a^s = a^3s
for i i range(1,s)
	x = (x*c) % p
	tabla.append(x)
print (tabla2)

ro(phi?) de pollard
"""

"""
# PROBLEMA SQRT: REDONDEA EL RESULTADO Y NO SALE X


x = 3145282147376476178927489641907928465684974644478221999199747877222191911143264748382L
print "X = " + str(x)
y = (x**2) + 3433488137413427727

print "DISTINTO DE X, REDONDEA"
print sqrt(y)
print ceil(sqrt(y))
"""


""" Método de Newton-Raphson adaptado para calcular raices cuadradas		x^2-a parábola"""
def raiz(n):
	i = 0
	m = len(bin(n)) // 2
	x = 2**m 	# Punto aproximado que sé que está por encima de la solucion
	y = (x**2 + n) // (2*x)
	while x > y:
		(x, y) = (y, (y**2 + n)//(2*y))
		i = i+1
	return (i, x)

""" ALGORITMO RHO DE POLLARD, el + EFICIENTE para cálculo logaritmo discreto
	Busca en una sucesion "aleatoria"(mentira, cíclica más bien) en Zp cuando coindiden 2 elems rollo x^3 = x^9 -> x^4 = x^10...

	logbase a (b) mod p


"""



# AUX FUNCS -------------------------------------
def read_in():
	if len(sys.argv) != 2:
		print ("Error en los params de entrada")
		exit()
	num = int(sys.argv[1])

	# Optimizamos el elevar el numero "a" a la potencia "b"

	return num

# Optimización mejor, coste alg O(log(b))
def potenciamodular (a, b, m):
	aux = 1
	while (b > 0):
		if (b%2 == 1):
			aux = (aux * a) % m
		a = (a**2) % m
		b /= 2

	return aux
#--------------

def main():	
	
	num = read_in()
	(iteras, resul) = raiz(num)
	print "ITERACIONES: " + str(iteras) + "\tRESULTADO = " + str(resul)
	print "Num entonces estaba en el rango ( " + str(resul**2) + ", " + str((resul+1)**2) + " )"

	# Paradoja Cumpleaños: 23!!! personas para que la prob de que coincidan 2 cumples sea aprox 1/2

if __name__ == '__main__':
	main()
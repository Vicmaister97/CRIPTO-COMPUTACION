#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from math import *

# SI el modulo c ES PRIMO, EL RESULTADO DE a^b mod c sale 1
# a^p-1 mod p = 1       si p PRIMO
# Nos sirve para ver si p es PRIMO, si da != 1 no lo es

def read_in():
	if len(sys.argv) != 4:
		print ("Error en los params de entrada")
		return
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	c = int(sys.argv[3])

	# Optimizamos el elevar el numero "a" a la potencia "b"

	return potenciamodular (a, b, c)


# Primera optimización, coste alg O(b)
def potencia (a, b, m):
	result = a
	for x in range(b-1):
	   result*=a
	return result%m

# Optimización mejor, coste alg O(log(b))
def potenciamodular (a, b, m):
	aux = 1
	while (b > 0):
		if (b%2 == 1):
			aux = (aux * a) % m
		a = (a**2) % m
		b /= 2

	return aux
	

def main():
	print ("Programa que, dados 3 enteros positivos a b c (en ese orden), calcula a^b mod c")
	#sol = read_in()
	#print sol

	# Realizamos un test de Fermat para ver si p = 2199733160881 es primo
	p = 2199733160881
	print potenciamodular(245, p-1, p)
	print potenciamodular(46372, p-1, p)
	print potenciamodular(3335, p-1, p)
	print potenciamodular(444, p-1, p)

	print "NEW PRIME"
	p = 561
	print potenciamodular(245, p-1, p)
	print potenciamodular(46372, p-1, p)
	print potenciamodular(3335, p-1, p)
	print potenciamodular(444, p-1, p)

if __name__ == '__main__':
	main()

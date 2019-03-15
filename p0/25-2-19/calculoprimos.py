#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from math import *

# SI el modulo c ES PRIMO, EL RESULTADO DE a^b mod c sale 1
# a^p-1 mod p = 1       si p PRIMO
# Nos sirve para ver si p es PRIMO, si da != 1 no lo es

def read_in():
	if len(sys.argv) != 2:
		print ("Error en los params de entrada")
		return
	n = int(sys.argv[1])

	# Optimizamos el elevar el numero "a" a la potencia "b"

	return n


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
	print ("Programa que, dado un número natural n, Devuelve una lista de todos los numeros naturales x entre 1 y n-1 tq x^2 = 1 mod n")

	print "TEST MILLER-RABIN: Encontrar sols de x^2 = 1 mod p para ver si p es primo"
	
	n = read_in()
	L = []
	for x in xrange(1, n):
		if ((x**2)%n == 1):
			L.append(x)
	print L
if __name__ == '__main__':
	main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from math import *

# TESTS DE PRIMALIDAD
# Pruebas test de primalidad
# Cálculo siguiente primo
# Cálculo siguiente primo fuerte, p es primo fuerte si p es primo ^ (p-1)/2 es primo
# Cálculo primo de n bits, 2^n-1 <= p <= 2^n

# SI el modulo c ES PRIMO, EL RESULTADO DE a^b mod c sale 1
# a^p-1 mod p = 1       si p PRIMO
# si p NO PRIMO, puede valer 1, pero el test fallará en algún caso
# Nos sirve para ver si p es PRIMO, si da != 1 es compuesto

# Si p es primo, x²-1=0 mod p tiene 2 sols en Zn
# Si m es impar ^ producto de r primos, x²-1=0 tiene 2^r sols

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

	# Fermat falla mucho
	# Test de Miller_Rabin, m es primo??
	# m-1 = 2^u * s (s es impar)
	# Elegimos a 2 <= a <= m-2
	print read_in()

if __name__ == '__main__':
	main()

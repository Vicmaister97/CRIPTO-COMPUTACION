#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from math import *
from random import *
from fractions import *

# AUX FUNCS -------------------------------------
def read_in():
	if len(sys.argv) != 3:
		print ("Error en los params de entrada")
		exit()
		return
	p = int(sys.argv[1])
	t = int(sys.argv[2])

	# Optimizamos el elevar el numero "a" a la potencia "b"

	return p, t

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

def miller_rabin0(p):
	if (p%2 == 0):		# Si el número p es PAR
		print "Numero PAR, NO PRIMO"
		exit()
	m = p-1	##Como introducimos un número que es impar
	u = 0
	while m%2 == 0:	# Expresamos m (p-1) como 2^u * s
		m = m//2	##Lo vamos factorizando en potencias de 2
		u += 1		##Vamos añadiendo uno a la u
	return u, (p-1)//potenciamodular(2, u, p)
	# El segundo término que devolvemos (lo llamaremos s) es impar: m par, m expresado como potencia de 2 (obvio) * IMPAR, ver casos (20=4*5, 88= 4*11)


##Escogemos un numero entero a , al azar, entre {2,....,p-2} que sea primo con n.
def obtener_a (p,t):
	L = []
	while len(L) < t:
		a = randint(2,p-2)	# CUIDAO RANGO
		if gcd(a,p) == 1:
			L.append(a)
		else:				# No seguimos el test, ya hemos encontrado un divisor de p
			print "1Testigo: " + str(a)
			return False
	return L

##Comprobamos que o bien a^d es congruente con 1 modulo n
def miller_rabin1(p,a,u,s):
	if potenciamodular(a, s, p) == 1 or potenciamodular(a,s,p) == p-1:
		return True
	else:
		for i in xrange(1, u):
			aux = potenciamodular(a, 2, p)
			if aux == p-1:
				return True
			if aux == 1:
				print "2Testigo: " + str(a)
				return False

	# Si ha llegado hasta aquí, no puede ser primo
	print "3Testigo: " + str(a)
	return False


# p >= 5, p impar
##Si encontramos un a primo con p tal que no se cumple ninguna de las dos condiciones definidas anteriormente, podemos 
##afirmar que el numero p es compuesto y entonces a es un "testigo" de la no primalidad de p
def miller_rabin(p,t):

	u,s = miller_rabin0(p)
	L = obtener_a(p,t)
	
	if L == False:
		print p, "NO es primo"
		return False
	else:
		for a in L:
			if (miller_rabin1(p,a,u,s)==True):
				print p, "es PROBABLE que sea primo"
			else: 
				print p, "NO es primo"
				return False
	
def main():
	print "TEST MILLER-RABIN(num, t) del primer argumento de entrada num con t testigos de primalidad"
	
	p, t = read_in()
	miller_rabin(p, t)

if __name__ == '__main__':
	main()

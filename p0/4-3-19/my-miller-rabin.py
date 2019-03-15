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
		print "Numero PAR, es COMPUESTO"
		exit()
	m = p-1	##Como introducimos un número que es impar
	u = 0
	while m%2 == 0:	# Expresamos m (p-1) como 2^u * s
		m = m//2	##Lo vamos factorizando en potencias de 2
		u += 1		##Vamos añadiendo uno a la u
	return u, (p-1)//potenciamodular(2, u, p)
	# El segundo término que devolvemos (lo llamaremos s) es impar: m par, m expresado como potencia de 2 (obvio) * IMPAR, ver casos (20=4*5, 88= 4*11)


# Función que devuelve una lista de testigos para el test
##Escogemos un numero entero a , al azar, entre {2,....,p-2} que sea primo con n.
def obtener_a (p,t):
	L = []
	while len(L) < t:
		a = randint(2,p-2)	# CUIDADO CON SI EL RANGO INCLUYE P-2
		if gcd(a,p) == 1:
			L.append(a)
		else:				# No seguimos el test, ya hemos encontrado un divisor de p
			print "1Testigo (NO es coprimo con): " + str(a)
			return False
	return L

##Comprobamos que o bien a^d es congruente con 1 modulo n
def miller_rabin1(p,a,u,s):
	potencias = []	# Lista donde almacenaremos los resultados del intento a^s = 1
	for i in xrange(0, u):
		elevar = (2**i)*s
		potencias.append(potenciamodular(a, elevar, p))
	if ( (any (i == p-1 for i in potencias) == True) or (all (i == 1 for i in potencias) == True) ):
		return True		# Es probable que sea primo
	else:
		for pos in xrange(0,len(potencias)):
			if potencias[pos] == 1:
				if pos > 0:
					if potencias[pos-1] != p-1:
						print "2Testigo (NO es coprimo con): " + str(a)
						return False
	if (all (i != 1 for i in potencias) == True or all (i != p-1 for i in potencias) == True):
		print "3Testigo (NO es coprimo con): " + str(a)
		return False
	if ( (potenciamodular(a,s,p) == 1) or any (i == p-1 for i in potencias) == True):
		print "3Testigo FALSO (cumple pequeño teorema fermat sin ser primo): " + str(a)
		return False

	#print potencias
	"""else:
		for i in xrange(1, u):
			aux = potenciamodular(a, 2, p)
			if aux == p-1:
				return True
			if aux == 1:
				return False"""

	# Si ha llegado hasta aquí, puede ser primo
	return True

# Busca los falsos testigos para un numero p compuesto (numeros que cumplen pequeño teorema fermat)
def findFalsosTestigos(p,a,u,s):
	potencias = []	# Lista donde almacenaremos los resultados del intento a^s = 1
	for i in xrange(0, u):
		elevar = (2**u)*s
		potencias.append(potenciamodular(a, elevar, p))
	
	if (potenciamodular(a,s,p) == 1 or any (i == p-1 for i in potencias) == True):
		print "4Testigo FALSO (cumple pequeño teorema fermat sin ser primo): " + str(a)
		return False


# p >= 5, p impar
##Si encontramos un a primo con p tal que no se cumple ninguna de las dos condiciones definidas anteriormente, podemos 
##afirmar que el numero p es compuesto y entonces a es un "testigo" de la no primalidad de p
def miller_rabin(p,t):

	u,s = miller_rabin0(p)
	print u,s
	L = obtener_a(p,t)
	print L
	if L == False:
		print p, "es COMPUESTO"
		return False

	else:
		#print "TESTIGOS" + str(L)
		for a in L:
			#findFalsosTestigos(p,a,u,s)
			
			if (miller_rabin1(p,a,u,s)==True):
				print p, "es PROBABLE que sea primo"
			else: 
				print p, "es COMPUESTO"
				return False
	
def main():
	print "TEST MILLER-RABIN(num, t) del primer argumento de entrada num con t testigos de primalidad"
	
	p, t = read_in()
	miller_rabin(p, t)

if __name__ == '__main__':
	main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Autor: Víctor García Carrera victorgarcia@correo.ugr.es
	Implementa los apartados 7 y 8 de la practica1 de CRIPTO&COMPUT
	"""

import sys
from math import *
from random import *
from fractions import *

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

# AUX FUNCS -------------------------------------

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
		a = randint(2,p-1)
		if gcd(a,p) == 1:
			L.append(a)

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
						#print "Testigo (NO es coprimo con): " + str(a)
						return False
	if ( (all (i != 1 for i in potencias) == True) or (	all (i != p-1 for i in potencias) == True)):
		#print "Testigo (NO es coprimo con): " + str(a)
		return False

	# Si ha llegado hasta aquí, puede ser primo
	return True

def miller_rabin(p,t):
	if (p%2 == 0):		# Si el número p es PAR
		return False
	u,s = miller_rabin0(p)
	#print u,s
	L = obtener_a(p,t)
	#L = [2,3,5,10]
	#print L
	if L == False:
		#print p, "es COMPUESTO"
		return False

	else:
		#print "TESTIGOS" + str(L)
		for a in L:
			#findFalsosTestigos(p,a,u,s)
			if (miller_rabin1(p,a,u,s)==False):
				#print p, "es COMPUESTO"
				return False
			#else:
				#print p, "es PROBABLE que sea PRIMO"

		#print p, "es PRIMO con probabilidad 1/(4^10)"
		return True

# p >= 5, p impar
##Si encontramos un a primo con p tal que no se cumple ninguna de las dos condiciones definidas anteriormente, podemos 
##afirmar que el numero p es compuesto y entonces a es un "testigo" de la no primalidad de p
def miller_rabin2(p,t):
	if (p%2 == 0):		# Si el número p es PAR
		return False
	u,s = miller_rabin0(p)
	#print u,s
	L = obtener_a(p,t)

	#L = [2,3,5,10]
	#print L
		#print "TESTIGOS" + str(L)
	for a in L:
		#findFalsosTestigos(p,a,u,s)
		if (miller_rabin1(p,a,u,s)==True):
			print a, "es un FALSO TESTIGO de " + str(p)
			#else:
				#print p, "es PROBABLE que sea PRIMO"

		#print p, "es PRIMO con probabilidad 1/(4^10)"
	return True

##	Función que devuelve el siguiente número primo
def nextPrime (num):
	numorg = num
	TESTIGOS = 10
	while True:	#	Utilizamos el test de miller-rabin con los naturales sucesivos al numero "num" hasta dar con un probable primo
		num+=1
		if miller_rabin(num, TESTIGOS) == True:
			#print "El siguiente primo es el " + str(num)
			return num

	print "No se ha encontrado el siguiente primo a " + str(numorg)
	return False

##	Función que devuelve el siguiente número primo fuerte
def nextprimoFuerte (num):
	primo = nextPrime(num)
	while miller_rabin ( (primo-1)/2 , TESTIGOS) != True:
		primo = nextPrime(primo)

	return primo


##	Función que devuelve un número primo fuerte de num bits
def PrimoFuerte(num):
	potencia = 2**(num-1)
	primoFuerte = nextprimoFuerte(potencia)
	if potencia < 2**num:
		#print "ENCONTRADO primo fuerte de " + str(num) + " bits:	" + str(potencia)
		return True
	else:
		print "No se ha encontrado un primo fuerte de " + str(num) + " bits"
		return False

def main():	

	TESTIGOS = 200
	p1 = nextPrime(6)
	p2 = nextPrime(20)
	p3 = nextPrime(30)

	big1 = nextPrime(60000)
	big2 = nextPrime(20000)
	big3 = nextPrime(30000)

	print "PRUEBA DE LOS 200 TESTIGOS"

	n1 = p1*p2*p3
	n2 = big1*big2*big3

	print "\nPrueba del número " + str(n1) + " ---"
	miller_rabin2(n1, TESTIGOS)

	print "\nPrueba del número " + str(n2) + " ---"
	miller_rabin2(n2, TESTIGOS)

	n1 = 3215031751
	n2 = 2199733160881

	print "\nPrueba del número " + str(n1) + " ---"
	miller_rabin2(n1, TESTIGOS)
	print "\nPrueba del número " + str(n2) + " ---"
	miller_rabin2(n2, TESTIGOS)


	# PROBABILDIAD DE ERROR = 1/(4^10)

if __name__ == '__main__':
	main()

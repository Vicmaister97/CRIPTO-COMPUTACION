#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Autor: Víctor García Carrera victorgarcia@correo.ugr.es
	Utiliza el test de Miller Rabin para obtener a partir de un número de entrada "num"
	el siguiente primo (mejor dicho, el siguiente mejor probable primo), entre otras funciones similares
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
def read_in():
	if len(sys.argv) != 3:
		print ("Error en los params de entrada")
		exit()
	p = int(sys.argv[1])
	num = int(sys.argv[2])

	# Optimizamos el elevar el numero "a" a la potencia "b"

	return p, num

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
		a = randint(2,p-1)	# CUIDADO CON SI EL RANGO INCLUYE P-2
		if gcd(a,p) == 1:
			L.append(a)
		else:				# No seguimos el test, ya hemos encontrado un divisor de p
			#print "Testigo (NO es coprimo con): " + str(a)
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
						#print "Testigo (NO es coprimo con): " + str(a)
						return False
	if ( (all (i != 1 for i in potencias) == True) or (	all (i != p-1 for i in potencias) == True)):
		#print "Testigo (NO es coprimo con): " + str(a)
		return False

	# Si ha llegado hasta aquí, puede ser primo
	return True


# p >= 5, p impar
##Si encontramos un a primo con p tal que no se cumple ninguna de las dos condiciones definidas anteriormente, podemos 
##afirmar que el numero p es compuesto y entonces a es un "testigo" de la no primalidad de p
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

##	Función que devuelve el siguiente número primo
def nextPrime (num):
	if num%2 == 0:	# Si es par
		num-=1

	TESTIGOS = 10
	while True:		#	Utilizamos el test de miller-rabin con los naturales sucesivos al numero "num" hasta dar con un probable primo
		num+=2      #   Damos saltos de 2 en 2 evitando los pares
		if miller_rabin(num, TESTIGOS) == True:
			#print "El siguiente primo es el " + str(num)
			return num

	print "No se ha encontrado el siguiente primo "
	return False

##	Función que devuelve el siguiente número primo fuerte
def nextprimoFuerte (num):
	primo = nextPrime(num)
	TESTIGOS = 10

	while miller_rabin ( (primo-1)/2 , TESTIGOS) != True:
		primo = nextPrime(primo)

	return primo


##	Función que devuelve un número primo fuerte de num bits
def PrimoFuerte(num):
	potencia = 2**(num-1)
	primoFuerte = nextprimoFuerte(potencia)
	if potencia < 2**num:
		#print "ENCONTRADO primo fuerte de " + str(num) + " bits:	" + str(primoFuerte)
		return primoFuerte
	else:
		print "No se ha encontrado un primo fuerte de " + str(num) + " bits"
		return primoFuerte

def main():	
	p, num = read_in()

	print "--- Cálculo del siguiente número primo (y primo fuerte) a " + str(p) + " ---"

	TESTIGOS = 10
	
	nextprime = nextPrime(p)
	print "El siguiente primo es el " + str(nextprime)
	nextstrongprime = nextprimoFuerte(p)
	print "El siguiente primo FUERTE es el " + str(nextstrongprime)


	print "\n\n--- Cálculo de un número primo fuerte de " + str(num) + " bits---"

	nbits = PrimoFuerte(num)
	if nbits != False:
		print "ENCONTRADO primo fuerte de " + str(num) + " bits:	" + str(nbits)



	# PROBABILDIAD DE ERROR = 1/(4^10)

if __name__ == '__main__':
	main()

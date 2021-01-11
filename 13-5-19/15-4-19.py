#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Autor: Víctor García Carrera victorgarcia@correo.ugr.es
	3 maneras de obtener p,q de un numero n conocidos distintos datos
	- Factorización n = p*q
	- Encontrar phi(n)
	- Encontrar landa(n)
	"""

import sys
from math import *
from random import *
from fractions import *
import numpy

""" ->-> MIRAR romperRSA.ipynb BIEN EXPLICADO <-<-<-

	p*q = n 	p,q primos 		(n,e) clave pública, d clave privada		e*d = 1 mod phi(n)		mcd(e, phi(n))
	p+q = n - phi(n) + 1
	 s
	p^2 - s*p + n = 0			IMP !!! Resolver ec 2do grado
	n = 135651523807
	phi(n) = 135645218856 = (p-1)*(q-1)

	p = 21589
	q = 6283363

Para romper RSA es factorizando o calculando phi(n) """

""" Datos
	n es producto de p y q
	landa(n) = mcm(p-1,q-1)
	n = 589
	landa(n) = 90

	Calculamos r = n mod landa(n)
	r = 49

	1)	phi(n) = n - r
	2)	phi(n) = n-r-landa(n)		2 opciones, si una no da raices enteras es la otra

	1) phi(n) = 540
	2) phi(n) = 450

	suma = n - phi(n) + 1
"""

"""def encontrarPrimos(num, phiNum):
	s = num - phiNum + 1
	# Debemos resolver la siguiente ecuacion"""

"""
	e = 65537
	clave publica (n, e)
	d' = 12920070665
	d' = 80742680093

	Calcular m^(e*d') mod n
	Se tiene que cumplir si e es un exponente de cifrado

	n = 135651523807
	phiNum = 135645218856 	# = (p-1)*(q-1)
	e = 65537

	d1 = 12920070665

	m = 987654321
	mPost = potenciamodular(m, e*d1, n)
	print m
"""


def miller_rabin0(p):
	m = p-1	##Como introducimos un número que es impar
	u = 0
	while m%2 == 0:	# Expresamos m (p-1) como 2^u * s
		m = m//2	##Lo vamos factorizando en potencias de 2
		u += 1		##Vamos añadiendo uno a la u
	return u, (p-1)//potenciamodular(2, u, p)
	# El segundo término que devolvemos (lo llamaremos s) es impar: m par, m expresado como potencia de 2 (obvio) * IMPAR, ver casos (20=4*5, 88= 4*11)



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
	
	n = 135651523807
	phiNum = 135645218856 	# = (p-1)*(q-1)
	#pmasq = 6304952
	e = 65537

	d1 = 12920070665
	#d2 = 8074268009

	"""m = 987654321
	mPost = potenciamodular(m, e*d1, n)
	print m"""

	"""	
	d*e -1 = 2^u * s   (s impar)
	X al azar entre 2 y n-2
	y = x^s mod n
	[y^2 % n, y^4 % n, y^8 % n]

	[ ..., z, 1]
	mcd (z+1,n)
	z² % n = 1
	z² - 1 es multiplo de n
	(z+1)(z-1)

	"""

	prueba = e*d1
	u, s = miller_rabin0(prueba)
	# u = 3, s = 105842833896513
	print u, s
	#x = randint(2, n-2)
	x = 96735889556
	y = potenciamodular(x, s, n)
	print ("x = {}, y= {}".format(x,y))
	y_2 = (y**2)%n
	y_4 = (y**4)%n
	y_8 = (y**8)%n

	L = []
	pot = 1
	for i in xrange(1,4):
		print i
		pot = pot*2
		L.append(potenciamodular(y, pot, n))

	print L
	# Cojemos 3 porque u = 3
	print ("y_2 = {}, y_4 = {}, y_8 = {}".format(y_2,y_4,y_8))
	#print ("mcd (z-1,n)={}".format(mt.mcd(y_2-1,n)))
	"""z^2 % n = 1
	z^2 -1 es multiplo de n
	(z+1)(z-1) es multiplo de n """


if __name__ == '__main__':
	main()
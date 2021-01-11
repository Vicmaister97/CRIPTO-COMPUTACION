#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Autor: Víctor García Carrera victorgarcia@correo.ugr.es
	Funciones para obtener generadores de grupos Zp y calcular resultado de logaritmos discretos
	"""

import sys
from math import *
from random import *
from fractions import *

# p primo, alfa generador de Zp, función obtener potencias de un elem en Zp (VER SI ES GENERADOR)

# LOGARITMO DISCRETO, FACTORIZACION


# AUX FUNCS -------------------------------------
def read_in():
	if len(sys.argv) != 2:
		print ("Error en los params de entrada")
		exit()
	p = int(sys.argv[1])

	return p

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

def potenciasZ(elem, orden):
	powers = [1]
	res = elem

	while res != 1:
		powers.append(res)
		res = (res * elem) % orden
		# Si ya hay un elem repetido, no va a ser generador
		if res in powers:
			break

	return powers


def main():	
	# x
	
	p = read_in()

	elems = []
	generadores = []

	# Elems de Zp
	#for i in xrange(1,p):
	#	elems.append(i)
	# Obtenemos subgrupo generado por x
	#subgr = potenciasZ(x,p)

	#print elems

	# --- GENERADOR V1.0 MUY LENTA ---
	"""
	# Para cada elemento de Zp calculamos el subgrupo que genera
	for i in xrange(1,p):
		#print "CALCULANDO SUBGRUPO DE " + str(i)
		subgr = potenciasZ(i,p)
		#print subgr
		#print "NUM: " + str(i) + " " + str( subgr )
		# Si el subgrupo generado tiene orden p, es generador
		if len(subgr) == p-1:
			generadores.append(i)
			break"""
	
    # PRIMER METODO INUTIL PARA NUMEROS DEL ORDEN DE 12855847883

	#potenciasZ(2,p)
	
	"""
	#pmenos1 = 2*17*307*757*1627
	pmenos1 = p-1
	entre2 = pmenos1/2
	
	# alfa es generador de Zp si alfa^(p-1)/(DIVISORES DE P-1) ES DISTINTO DE 1
	alfa = 2
	print (potenciamodular(alfa,pmenos1/2,p) )
	print (potenciamodular(alfa,pmenos1/17,p) )
	print (potenciamodular(alfa,pmenos1/307,p) )
	print (potenciamodular(alfa,pmenos1/757,p) )
	print (potenciamodular(alfa,pmenos1/1627,p) )

	
	# Si p es un primo fuerte, p-1 = 2*q
	# alfa: 2 < alfa < p-2 es GENERADOR ssi alfa^(p-1)/2 ES DISTINTO DE 1
	pot = potenciamodular(alfa, entre2, p)
	if pot != 1:
		print "GENERADOR: " + str(alfa)"""


	# Calculamos un generador a
	# Calcula un x tq a^x= 97 mod p
	# Calcula un y tq a^y=3 mod p
	b = 1
	while b==1:
		a = randint(2,p-1)
		b = potenciamodular(a,((p-1)/2), p)

	print "GENERADOR: " + str(a)

	x = randint(2, p-1)
	while potenciamodular(a,x,p) != 97:
		x = randint(2, p-1)
	print "X= " + str(x)

	y = randint(2, p-1)
	while potenciamodular(a,y,p) != 3:
		y = randint(2, p-1)
	print "Y= " + str(y)

	#print potenciamodular(a,y,p)
	# x = log(base a) 97 mod p
	# p=227, a=2, x=186,
	# p=2819, a=2,
	# p=1319,a=1317
	

	print "--- Generadores de Z" + str(p) + " ---"
	print generadores
	# Vemos los elems de Zp que son generador, es decir, aquellos cuyo subgr generado es Zp.


if __name__ == '__main__':
	main()

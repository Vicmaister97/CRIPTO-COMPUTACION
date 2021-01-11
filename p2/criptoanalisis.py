#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Autor: Víctor García Carrera victorgarcia@correo.ugr.es
	Funciones para el criptoAnalisis de ficheros txt codificados con MAYUSCULAS y los 27 caracteres del alfabeto español
	"""

import sys
from math import *
from random import *
from fractions import *





def main():	
	p = read_in()

	print "--- TEST MILLER-RABIN de " + str(p) + " ---"

	TESTIGOS = 10
	miller_rabin(p, TESTIGOS)

	# PROBABILDIAD DE ERROR = 1/(4^10)

if __name__ == '__main__':
	main()

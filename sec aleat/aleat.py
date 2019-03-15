#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from math import *
from decimal import *

# Víctor García Carrera, victorgarcia@correo.ugr.es

def analisis_frec(T):
    frecuencias = {}
    N = len(T)
    for letra in T:
        if letra in frecuencias:
            frecuencias[letra] += (1/N).n()
        else:
            frecuencias[letra]=(1/N).n()
    return frecuencias

def invertir(dicc):
    dict_inv = {}
    for key in dicc:
        dict_inv[dicc[key]] = ord2(key)
    return dict_inv

def analisis_frec_compl(T):
    dicc = analisis_frec(T)
    dicc2 = invertir(dicc)
    L = dicc2.items()
    L.sort(reverse=True)
    return L




def main():

	"""
	FF = analisis_frec_compl(cortado[0])
	print FF
	"""
	"""

	print "Dado un fichero txt con texto, codifica como 0 las consonantes y como 1 las vocales para tratar de generar una secuencia -aleatoria-"

	if len(sys.argv) != 2:
		print ("Error en los params de entrada")
		return

	textIn = str(sys.argv[1])
	fileIn = open(textIn, "r")
	fileOut = open("aleat.txt", "w")

	consonantes = ["b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z","B","C","D","F","G","H","J","K","L","M","N","Ñ","P","Q","R","S","T","V","W","X","Y","Z"]
	vocales = ["a","e","i","o","u","A","E","I","O","U"]

	# Posible implementar más estadísticos
	consonants = 0
	vocals = 0
	aleat = []

	while True:
		letra = fileIn.read(1)
		if not letra:
			print "End of file"
			break
		if (letra in consonantes):
			consonants+=1
			aleat.append(0)
		if (letra in vocales):
			vocals+=1
			aleat.append(1)

	print "Consonantes = " + str(consonants)
	print "Vocales = " + str(vocals)

	fileOut.close()
	fileIn.close()
	"""
	"""
	# Escribimos los 10000 primeros digitos del numero irracional elegido

	getcontext().prec = 10000
	fileprev = open("prueba.txt", "w")
	fileprev.write(str(Decimal(7).sqrt()))
	fileprev.close()
	"""
	print "Dado un fichero txt con los digitos de un numero irracional, genera en aleat.txt una secuencia binaria -aleatoria-, codificando como 0 los digitos pares y como 1 los impares"
	if len(sys.argv) != 2:
		print ("Error en los params de entrada")
		return

	textIn = str(sys.argv[1])
	fileIn = open(textIn, "r")
	fileOut = open("aleat.txt", "a")

	par = 0
	impar = 0
	numletras = 0

	while True:
		letra = fileIn.read(1)
		try:
			num = int(letra)
			numletras+=1
			
			if (int(letra)%2 == 0):
				par+=1
				fileOut.write("0")
			if (int(letra)%2 == 1):
				impar+=1
				fileOut.write("1")

		except ValueError:
			if not letra:
				print "End of file"
				break
			pass

	print "Pares(%) = " + str(float(par)/float(numletras))
	print "Impares(%) = " + str(float(impar)/float(numletras))

	fileOut.close()
	fileIn.close()


if __name__ == '__main__':
	main()


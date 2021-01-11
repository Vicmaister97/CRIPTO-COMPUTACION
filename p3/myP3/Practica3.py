#!/usr/bin/env python
# -*- coding: utf-8 -*-



""" Autor: Víctor García Carrera victorgarcia@correo.ugr.es
	Metodo de Pollard para logaritmos discretos
	"""

import sys
import matplotlib.pyplot as plt
from time import time
from math import *
from random import *
from fractions import *
import numpy



#Calcula el máximo común divisor de dos números.
def mcd(a,b):
		while b!=0:
				(a,b) = (b,a%b)
		return a

#Calcula el inverso de a módulo b (si existe). Si ni existe, lo dice y devuelve 0.
def inversomodular(a,b):
		(u0,u1) = (1,0)
		while b>0:
			 (u0,u1) = (u1,u0-(a//b)*u1)
			 (a,b) = (b,a%b)
		if a == 1:
			 return u0
		else:
			 print("No existe el inverso")
			 return 0

#Resuelve la congruencia ax = b mod m. Da todas las soluciones comprendidas entre 0 y m-1.
def congruencia(a,b,m):
		d = mcd(a,m)
		if b%d == 0:
			 n = m//d
			 u = inversomodular(a//d,n)
			 x = (u*(b//d))%n
			 sol = []
			 for i in range(d):
					 sol.append(x)
					 x = x+n
			 return sol
		print("La congruencia no tiene solución")
		return([0])

#Calcula la raíz cuadrada entera de un número natural.
def raiz(n):
		m = (len(bin(n))-1) // 2
		x = 2**m
		y = (x**2+n)//(2*x)
		while x > y:
				(x,y) = (y,(y**2+n)//(2*y))
		return x

#Comprueba si un número natural es cuadrado perfecto.
def escuadrado(n):
		y = raiz(n)
		return(y**2 == n)


############################### LOGARITMO DISCRETO

####### DECIR A LOS COMPAÑEROS QUE NO VARIE ITERACIONES

# AUX FUNCS -------------------------------------
def read_in():
	if len(sys.argv) != 4:
		print ("Error en los params de entrada")
		exit()

	a = int(sys.argv[1])
	b = int(sys.argv[2])
	p = int(sys.argv[3])

	# Optimizamos el elevar el numero "a" a la potencia "b"

	return a, b, p

# Optimización mejor, coste alg O(log(b))
def potenciamodular (a, b, m):
	aux = 1
	while (b > 0):
		if ((b%2) == 1):
			aux = (aux * a) % m
		a = (a**2) % m
		b = b//2

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




# PROBLEMA: log a (x) mod p

# RO DE POLLARD para el cálculo de logaritmos discretos
# Esta versión implementada es la más eficiente de las vistas, donde construimos dos sucesiones de elems basandonos en el logaritmo
# a resolver, una sucesión xn y otra x2n, de forma que buscamos cuando coinciden sus valores sin tener que almacenar toda la sucesión 
# ni por cada nuevo término comparar con todos los anteriores
def PollardLog(a, b, p, MaxIter):
	# Construimos 3 subconjuntos disjuntos (S1,S2,S3) para particionar X={1,2,...,p-1} tq 1 !e S2
	# S1 = {x e X tq congruencia(1,1,3)}, S2 = {x e X tq congruencia(1,0,3)}, S1 = {x e X tq congruencia(1,2,3)}

	# Terna (xi,ai,bi) representa la sucesión para resolver el logaritmo
	# Valor inicial (x0, a0, b0) = (1,0,0)
	# Sucesión que recorre los valores de 1 en 1, valores iniciales
	x1 = 1*b
	alfa1 = 0
	beta1 = 1

	# Sucesión que recorre los valores de 2 en 2, valores iniciales
	(x2, alfa2, beta2) = nextIterPollard(x1,alfa1,beta1, a, b, p)

	iters = 0
	while (iters<MaxIter and (x1 != x2)):
		iters += 1
		
		(x1, alfa1, beta1) = nextIterPollard(x1,alfa1,beta1, a, b, p)
		# La sucesion2 avanza de 2 en 2, por eso iteramos 2 veces
		(x2, alfa2, beta2) = nextIterPollard(x2,alfa2,beta2, a, b, p)
		(x2, alfa2, beta2) = nextIterPollard(x2,alfa2,beta2, a, b, p)


	# Si x1==x2, hemos encontrado una coincidencia en la sucesión, 
	# y planteamos la siguiente congruencia que serán las soluciones del logaritmo discreto
	if (x1 == x2):
		"""print("COINCIDEN")
		print("X1: " + str(x1) + " , " + str(alfa1) + " , " + str(beta1))
		print("X2: " + str(x2) + " , " + str(alfa2) + " , " + str(beta2))"""
		soluciones = congruencia(beta2 - beta1, alfa1 - alfa2, p-1)
		#print(soluciones)
		if (soluciones == [0]):
			return None

		for sol in soluciones:
			# Si la solucion encontrada NO es verdaderamente una solucion del logaritmo planteado
			if ( potenciamodular(a,sol,p) != b):		# Posible optimizar
				soluciones.remove(sol)

		return soluciones

	# MaxIter alcanzado
	else:
		#print("MAXITER ALCANZADO SIN ENCONTRAR UNA SOLUCION")
		return None


def nextIterPollard(x, alfa, beta, a, b, p):
	if (x%3 == 1):
		x = (x*b)%p
		beta += 1
		return (x, alfa, beta)
		# SI x1 e S2	
	if (x%3 == 0):
		x = (x**2)%p
		alfa = (2*alfa)%(p-1)
		beta = (2*beta)%(p-1)
		return (x, alfa, beta)
		# SI x1 e S3	
	if (x%3 == 2):
		x = (x*a)%p
		alfa += 1
		return (x, alfa, beta)

def PollardLogINEFIC(a, b, p, MaxIter):
	# Construimos 3 subconjuntos disjuntos (S1,S2,S3) para particionar X={1,2,...,p-1} tq 1 !e S2
	# S1 = {x e X tq congruencia(1,1,3)}, S2 = {x e X tq congruencia(1,0,3)}, S1 = {x e X tq congruencia(1,2,3)}

	# Terna (xi,ai,bi) representa la sucesión para resolver el logaritmo
	# Valor inicial (x0, a0, b0) = (1,0,0)
	# Sucesión que recorre los valores de 1 en 1, valores iniciales
	x = 1*b
	alfa = 0
	beta = 1
	sucesion = []
	sucesion.append((x, alfa, beta))


	iters = 0
	while (iters<MaxIter):
		iters += 1
		
		(x, alfa, beta) = nextIterPollard(x,alfa,beta, a, b, p)
		pos = 0
		while pos < len(sucesion):
			if (x == sucesion[pos][0]):
				(x1, alfa1, beta1) = sucesion[pos]
				(x2, alfa2, beta2) = (x, alfa, beta)

				# Si x1==x2, hemos encontrado una coincidencia en la sucesión, 
				# y planteamos la siguiente congruencia que serán las soluciones del logaritmo discreto
				
				"""print("COINCIDEN")
				print("X1: " + str(x1) + " , " + str(alfa1) + " , " + str(beta1))
				print("X2: " + str(x2) + " , " + str(alfa2) + " , " + str(beta2))"""
				soluciones = congruencia(beta2 - beta1, alfa1 - alfa2, p-1)
				#print(soluciones)

				for sol in soluciones:
					# Si la solucion encontrada NO es verdaderamente una solucion del logaritmo planteado
					if ( potenciamodular(a,sol,p) != b):
						soluciones.remove(sol)

				if len(soluciones) > 0:
					return soluciones
				
			pos += 1

		sucesion.append((x, alfa, beta))


	# MaxIter alcanzado
	else:
		#print("MAXITER ALCANZADO SIN ENCONTRAR UNA SOLUCION")
		return None


def main():

	MAXITER = 10000000
	tries = 0
	tiempos = []
	tiempos2 = []
	primosTam = []
	"""inic = 0
	inic2 = 0
	tiempo_ejec = 0
	tiempo_ejec2 = 0"""
	nBits = 20	## bits del primo que conforma Zp
	#p = PrimoFuerte(bits)

	"""
	print("PRIMO FUERTE: " + str(p))

	nogen = False
	Gen = []
	for num in xrange(PrimoFuerte(20),p):		# Al estar en Zp, los elementos tienen orden 1 o p (siendo generadores en este caso)
		for i in xrange(2, p-2):
			if potenciamodular(num, i, p) == 1:
				nogen = True
				break
		if (nogen == False):
			Gen.append(num)

		else:
			nogen = False


	porcent = len(Gen)/(p-1.0)
	print("HAY " + str(len(Gen)) + " GENERADORES: " + str(porcent) + " %")
	#print(Gen)
	for elem in Gen:
		print("SUBGR GEN POR " + str(elem))
		for i in xrange(0,p-1):
			print (potenciamodular(elem,i,p))
	"""
	

	# Vamos a probar a realizar 30 mediciones
	## PARAMOS CUANDO LA INEFICIENTE ROMPE PARA ARRIBA, ALREDEDOR DE NBITS=34
	while (nBits < 36 ):
		tries = 0
		p = PrimoFuerte(nBits)
		nBits +=2
		a = randint(2, p-2)		# p-2
		b = randint(1, p-1)		# p-1
		print("RHO DE POLLARD DE " + str(a) + ", " + str(b) + " mod " + str(p))

		### INICIO DEL TIEMPO ###
		inic = time()
		sols = PollardLog(a, b, p, MAXITER)
		tiempo_ejec = time() - inic
		### FIN DEL TIEMPO

		### INICIO DEL TIEMPO ###
		inic2 = time()
		sols2 = PollardLogINEFIC(a, b, p, (MAXITER))
		tiempo_ejec2 = time() - inic2
		### FIN DEL TIEMPO

		while (sols == None and tries < 10):			# Hasta que encuentre solucion
			print("SIN SOLUCION, PROBANDO INTENTO " + str(tries) + " CON NBITS " + str(nBits))
			tries+=1
			a = randint(2, p-2)
			b = randint(1, p-1)

			### INICIO DEL TIEMPO ###
			inic = time()
			sols = PollardLog(a, b, p, MAXITER)
			tiempo_ejec = time() - inic
			### FIN DEL TIEMPO ###

			### INICIO DEL TIEMPO ###
			inic2 = time()
			sols2 = PollardLogINEFIC(a, b, p, (MAXITER))
			tiempo_ejec2 = time() - inic2
			### FIN DEL TIEMPO

		# ÈNCONTRADAS LAS soluciones, guardamos el par Tiempo-nBits
		if (sols != None):
			#print("PRIMO: " + str(p) + ", SOLS: " + str(sols))
			print("TIEMPO: " + str(tiempo_ejec) + " , nBits: " + str(nBits))
			print("TIEMPOINEFIC: " + str(tiempo_ejec2) + " , nBits: " + str(nBits))
			tiempos.append(tiempo_ejec)
			tiempos2.append(tiempo_ejec2)
			primosTam.append(nBits)


	print("REPRESENTAMOS LA GRAFICA")
	print(primosTam)
	plt.plot(primosTam, tiempos, primosTam, tiempos2)
	#plt.xticks(y_pos, ['10','16','20','26','30','36','40','46','50','60','70','80','90','100','110','120','130','140','150','160'],rotation=45)
	plt.ylabel("Tiempo(s)")
	plt.xlabel("Nbits del primo")
	plt.title("LOG_DISCRETO: RHO de POLLARD")
	#plt.ylim(-0.0001,0.001)
	#plt.title('a=%i' %i)

	"""plt.ioff()
	plt.plot(primosTam, tiempos2)
	plt.ion()
	plt.plot(primosTam, tiempos2)"""
	plt.show()

	#print("--- ALGORITMO RO DE POLLARD para el CÁLCULO DEL LOGARITMO DISCRETO en base " + str(a) + " de " + str(b) + " modulo el primo " + str(p) + " ---")



	"""sols = PollardLog(a, b, p, MAXITER)
	print("SOLUCIONES: " + str(sols))
	print("QUE VIENE\n\n\n\n")"""
	"""sols = PollardLogINEFIC(a, b, p, MAXITER)
	print("SOLUCIONESINEFICIENTES: " + str(sols))"""

if __name__ == '__main__':
	main()
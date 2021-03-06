#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Autores: José Manuel García, Manuel Alejandro Sanchez, Marcel Kemp, Víctor García
      Implementación de los diversos algoritmos propuestos en la P3 de la asignatura Criptografía y Computación de la UGR
      para resolver problemas de cálculo de logaritmos, factorización y raíces cuadradas, junto con un estudio de
      su eficiencia y complejidad para comprobar los mejores métodos"""

import sys
import matplotlib.pyplot as plt
from time import time
import math
import random


#Calcula el máximo común divisor de dos números.
def mcd(a,b):
    while b!=0:
        (a,b) = (b,a%b)
    return a

def Potencia(a,b,m): #ORDEN log(b), calcula a^b % m
    aux=1
    while(b>0):
        if(b%2==1):
            aux=aux*a
            aux=aux%m
        b=b//2
        a=(a*a)%m
    return aux 

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

###########################################################    METODO DEL logaritmo

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
  m = p-1 ##Como introducimos un número que es impar
  u = 0
  while m%2 == 0: # Expresamos m (p-1) como 2^u * s
    m = m//2  ##Lo vamos factorizando en potencias de 2
    u += 1    ##Vamos añadiendo uno a la u
  return u, (p-1)//potenciamodular(2, u, p)
  # El segundo término que devolvemos (lo llamaremos s) es impar: m par, m expresado como potencia de 2 (obvio) * IMPAR, ver casos (20=4*5, 88= 4*11)


# Función que devuelve una lista de testigos para el test
##Escogemos un numero entero a , al azar, entre {2,....,p-2} que sea primo con n.
def obtener_a (p,t):
  L = []
  while len(L) < t:
    a = randint(2,p-1)  # CUIDADO CON SI EL RANGO INCLUYE P-2
    if gcd(a,p) == 1:
      L.append(a)
    else:       # No seguimos el test, ya hemos encontrado un divisor de p
      #print "Testigo (NO es coprimo con): " + str(a)
      return False

  return L

##Comprobamos que o bien a^d es congruente con 1 modulo n
def miller_rabin1(p,a,u,s):
  potencias = []  # Lista donde almacenaremos los resultados del intento a^s = 1
  for i in xrange(0, u):
    elevar = (2**i)*s
    potencias.append(potenciamodular(a, elevar, p))
  
  if ( (any (i == p-1 for i in potencias) == True) or (all (i == 1 for i in potencias) == True) ):
    return True   # Es probable que sea primo
  else:
    for pos in xrange(0,len(potencias)):
      if potencias[pos] == 1:
        if pos > 0:
          if potencias[pos-1] != p-1:
            #print "Testigo (NO es coprimo con): " + str(a)
            return False
  if ( (all (i != 1 for i in potencias) == True) or ( all (i != p-1 for i in potencias) == True)):
    #print "Testigo (NO es coprimo con): " + str(a)
    return False

  # Si ha llegado hasta aquí, puede ser primo
  return True


# p >= 5, p impar
##Si encontramos un a primo con p tal que no se cumple ninguna de las dos condiciones definidas anteriormente, podemos 
##afirmar que el numero p es compuesto y entonces a es un "testigo" de la no primalidad de p
def miller_rabin(p,t):
  if (p%2 == 0):    # Si el número p es PAR
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



##  Función que devuelve el siguiente número primo
def nextPrime (num):
  if num%2 == 0:  # Si es par
    num-=1

  TESTIGOS = 10
  while True:   # Utilizamos el test de miller-rabin con los naturales sucesivos al numero "num" hasta dar con un probable primo
    num+=2      #   Damos saltos de 2 en 2 evitando los pares
    if miller_rabin(num, TESTIGOS) == True:
      #print "El siguiente primo es el " + str(num)
      return num

  print "No se ha encontrado el siguiente primo "
  return False

##  Función que devuelve el siguiente número primo fuerte
def nextprimoFuerte (num):
  primo = nextPrime(num)
  TESTIGOS = 10

  while miller_rabin ( (primo-1)/2 , TESTIGOS) != True:
    primo = nextPrime(primo)

  return primo


##  Función que devuelve un número primo fuerte de num bits
def PrimoFuerte(num):
  potencia = 2**(num-1)
  primoFuerte = nextprimoFuerte(potencia)
  if potencia < 2**num:
    #print "ENCONTRADO primo fuerte de " + str(num) + " bits: " + str(primoFuerte)
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
    soluciones = congruencia(beta2 - beta1, alfa1 - alfa2, p-1)

    for sol in soluciones:
      # Si la solucion encontrada NO es verdaderamente una solucion del logaritmo planteado
      if ( potenciamodular(a,sol,p) != b):
        soluciones.remove(sol)

    return soluciones

  # MaxIter alcanzado
  else:
    print("MAXITER ALCANZADO SIN ENCONTRAR UNA SOLUCION")

# Funcion que calcula el siguiente valor de la sucesión
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
        soluciones = congruencia(beta2 - beta1, alfa1 - alfa2, p-1)

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
    print("MAXITER ALCANZADO SIN ENCONTRAR UNA SOLUCION")


###########################################################    METODO DE LA Factorización


def siguiente_primo(p):
	primo=False
	while (primo==False):
		if (MillerRabin(p+1)):
			primo=True
			return p+1
		p=p+1

def MillerRabin(p):
	for i in range (40):
		if( Rabin(p)== False):
			return False
	return True



def Rabin(p,testigo=1):
	u= 0
	caso = p-1
	while(caso % 2 == 0):
		u+=1
		caso = caso //2
	s= caso 
	if (testigo ==1):
		a=random.randrange(2,p-2)
	else:
		a=testigo
	
	a=Potencia(a,s,p)
	
	if (a == 1 or a ==p-1 ):
		
		return True
	else :
		for i in range(u-1):
			a=Potencia(a,2,p)
			if ( a ==p-1 ):
				
				return True
			elif (a ==1 ):
				
				return False
		
		return False





def tentativa(num,iteraciones):
	i=2
	divisores=[]
	
	while(i<= math.sqrt(num)):
		 iteraciones-=1
		 if (num%i ==0):
			 divisores.append(i)
			 num=num//i
			 i=1
			 iteraciones=0
			 return divisores
		 if (i>=5):
			  i=siguiente_primo(i)
		 else:
			 i+=1
		 if( iteraciones<0):
			 return 0
 
	divisores.append(num)
	return divisores

def Graficasfactorizacion():
    t,f,p,nums=SacarTiempotentativayfermatypollard()
    y_pos = range(len(nums))
    xticks=[str(len(bin(i)))for i in nums]
					
    
    plt.plot(y_pos, t)
    plt.plot(y_pos, f)
    plt.plot(y_pos, p)
    plt.xticks(y_pos,xticks,rotation=45)
    plt.ylabel('tiempo')
    plt.xlabel('tamaño del numero')
    plt.title('factorizacion tentativa')
 

    plt.show()

               

def SacarTiempotentativayfermatypollard():
    t=[]
    f=[]
    pollard=[]
		
    iteraciones=100000
    pruebas =[]
    
##    PRUEBAS  tentativa 
#    pruebas=sorted([696295307, 541796183, 11088659641, 24389, 14010083304673, 700296511538203, 877937561, 12167,390000,3031099,21233035,1982692267])
#    Prueba fermat
#    pruebas = sorted([14751210111547687874195101969009189, 31877830253060928649389026953141459, 36072596027370412229656419950863141, 25791583157891640306535115513674369, 10696482407930785670089540283304234976042001, 22325297617843711929081066391807048684272839, 49178161458256630753025869622335161355817413, 2588639896281414443586550883425864291, 49178161458256630753025869622335161355817413, 24190962688047137367098839, 10696482407930785670089540283304234976042001, 1073782960471773420899734973046444959])	 

		 

    pruebas=sorted([696295307, 541796183, 11088659641, 24389, 14010083304673, 700296511538203, 877937561, 12167,390000,3031099,21233035,1982692267])
    for p in pruebas:
        print("\nChequeamos si ",p ,"es primo:" ,MillerRabin(p))
        start_time = time()
#        for z in range(0,50):
#					    if (z==9):
        print (tentativa(p,iteraciones*10))
        elapsed_time = time() - start_time
        t.append(elapsed_time)
        print("tentativa",elapsed_time,"\n")
        
        start_time = time()
        print (Fermat(p,iteraciones*1000))
        elapsed_time = time() - start_time
        f.append(elapsed_time)
        print("Fermat",elapsed_time,"\n")
				
        start_time = time()
        print (Pollard(p,iteraciones*100))
        elapsed_time = time() - start_time
        pollard.append(elapsed_time)
        print("Pollard",elapsed_time)
				
    
    return t,f,pollard,pruebas



def Fermat(num,iteraciones):
	raiz =int(math.sqrt(num))
	cuadrado_perfecto=False
	
	
	while(cuadrado_perfecto==False ):
		raiz+=1
		if( (raiz**2 )-num>0):
			valor=math.sqrt( (raiz**2 )-num)
		
			p_entera=int(valor)
			iteraciones-=1
	
			if(iteraciones<0):
				return (num,1)
				
			if(p_entera**2 == valor**2):
				cuadrado_perfecto=True	
		
		
	return (raiz+p_entera,raiz-p_entera)

	
	
def Pollard(num,iteraciones):
	i=1
	x=1
	x_2=2
	
	while(mcd(x_2-x,num)==1):
		i+=1
		x=Potencia(1+x**2 ,1,num)
		iteraciones -=1
		for z in range(2):
			x_2=(1+x_2**2)%num
		if(iteraciones < 0):
			return 0
							
	return mcd(x_2-x,num)



###########################################################    METODO DE LAS RAICES


def Descomponer(p):  # descompone p-1 en 2^u *s, con s impar
    s, u = p, 0
    while s > 0 and s % 2 == 0:
        s //= 2
        u += 1
    return u, s


def Jacobi(a, p): 
    if p % 2 != 0:
        res = 1  # inicializamos el símbolo de jacobi
        a = a % p  # 1: aplicamos (a / p) = (a % p / p)
    
        if a == 0:
          return 0
        if a == 1: #(1/p)=1
          return 1
        if a == -1:  #(-1 / p) = -1^(p-1/2)
            return ((-1) ** ((p - 1) // 2))    
        
        u,s=Descomponer(a) # a lo descompones en 2^u * s  y queda (a/p)=(2^u / p)(s/p)
        
        if u > 0:  # (2 / p)  = (-1)**((p^2 - 1)/8)
            res = ((-1) ** ((p ** 2 - 1) // 8))
            if u % 2 == 0:
                res=res*res
         
        #Una vez resuelto el simbolo de (2^u / p), calculamos el de (s/p) 
        
        if s == 1:  # si s=1  entonces => (1/p) = 1
            return res
        elif s == -1:  #  si s=-1  =>  (-1/p) = -1^(p-1)/2
            return res * ((-1) ** ((p - 1) // 2))
        if p % 2 != 0:  # si ambos son impares  (q/p)  = (-1)^((p-1)(q-1)/4) * (p/q)
            return res * Jacobi(p, s) * (-1) ** ((p - 1) * (s - 1) // 4)
    else:
        print('p tiene que ser primo')
        return 0


# para realizar este metodo, (a/p)=1, ademas p= primo, devuelve r tal que r**2= a mod p
def MetodoRaices(a,p): 
    if (Jacobi(a,p) == 1): #si tiene raiz
        for n in range(2,p-1):
            if (Jacobi(n,p)==-1):
                break
            
        u,s=Descomponer(p-1)
        
        if (u==1):
            return Potencia(a,((p+1)//4),p)
        else:
            r=Potencia(a,((s+1)//2),p)
            b=Potencia(n,s,p)
            c=Potencia(a,p-2,p)
            d=c*r**2
            for j in range(0,u-1):
                if (Potencia(d,2**(u-2-j),p)==p-1):
                    r=(r*b)%p
                    d=(d*b*b)%p
                b=b**2
            return r
        
    else:#si no tiene raiz
        print("No tiene raiz",a,p)
        return 0

def GraficasRaices():
    t,nums=SacarTiempo()
    y_pos = range(len(nums))
    plt.plot(y_pos, t)
    plt.xticks(y_pos, ['10','16','20','26','30','36','40','46','50','60','70','80','90','100','110','120','130','140','150','160'],rotation=45)
    plt.ylabel('tiempo')
    plt.xlabel('número nbits del primo')
    plt.title('raices')
    plt.ylim(-0.0001,0.001)
#    plt.title('a=%i' %i)
    plt.show()

               

def SacarTiempo():
    t=[]
    nums=[653,64271,743377,50931521,800473007,66890854637,620229115019,40180118467187,596317283850721,
          761181220384054447,820462229029141988141,798966282447117686035903,1071404596312053013481453123,696826136406719997404315119471,
          1025274472585836996459365825413993,860010656083049867910925345486332611,1119570490581794118332155040648605252273,
          1207936072022102571105388223602999300510937,1097835525308120668052224878844625180291081123,1338286454942451715194168127094369648021682810041]
    den=[10560, 10562, 10560, 10567, 10560, 10561, 10560, 10562, 10560, 10560, 10560, 10560, 10560, 10562, 10560, 10560, 10561, 10561, 10567, 10560]
    i=0
    for p in nums:
        start_time = time()
        for z in range(0,3000):
            MetodoRaices(den[i],p)
        elapsed_time = time() - start_time
        t.append(elapsed_time/3000)
#        print(elapsed_time)
        i=i+1
    return t,nums


#a=10560
#p=653 
#nums=[653,64271,743377,50931521,800473007,66890854637,620229115019,40180118467187,596317283850721,
#          761181220384054447,820462229029141988141,798966282447117686035903,1071404596312053013481453123,696826136406719997404315119471,
#          1025274472585836996459365825413993,860010656083049867910925345486332611,1119570490581794118332155040648605252273,
#          1207936072022102571105388223602999300510937,1097835525308120668052224878844625180291081123,1338286454942451715194168127094369648021682810041]
#asd=[]
#for n in nums:
#    for aes in range(a,a+20):
#        if (Jacobi(aes,n)==1):
#            asd.append(aes)
#            break
#print(asd)



def main():
	GraficasRaices()
	Graficasfactorizacion()
	
	
Graficasfactorizacion()
#main


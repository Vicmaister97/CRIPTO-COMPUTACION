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

###########################################################    METODO DE el logaritmo

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
##        for z in range(0,50):
##					    if (z==9):
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
	raizm =raiz(num) 
	cuadrado_perfecto=False
	
	
	while(cuadrado_perfecto==False ):
		raizm+=1
		valor=math.sqrt( (raizm*raizm )-num)
		
		p_entera=math.floor(valor)
		iteraciones-=1
	
		if(iteraciones<0):
			return (num,1)
				
		if(valor ** 2 == p_entera **2):
			
			return (raizm+p_entera,raizm-p_entera)
		
		
	


	
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
    plt.xticks(y_pos, ['10','16','20','26','30','36','40','46','50','60','70','80','90','100','110','120','130','140','150','160'])
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
        for z in range(0,100):
            MetodoRaices(den[i],p)
        elapsed_time = time() - start_time
        t.append(elapsed_time/100)
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

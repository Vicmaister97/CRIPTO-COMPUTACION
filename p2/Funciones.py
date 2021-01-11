import time
import base64

#Dado un texto (string) solo con mayusculas lo transforma en una lista de números (A-0,...,Z-26). Por un espacio añade un -1
def cadenatolista(cadena):
    l = []
    for s in cadena:
        x = ord(s)
        if x == 32:
            l.append(-1)
        elif x < 79:
            l.append(x-65)
        elif x == 209:
            l.append(14)
        else:
            l.append(x-64)
    return l

#Inverso del anterior. Una lista de números (0--26) lo transforma en un string con mayúsculas
def listatocadena(l):
    s = ''
    for x in l:
        if x == -1:
            s = s + ' '
        elif x <= 13:
            s = s + chr(x+65)
        elif x == 14:
            s = s + 'Ñ'
        else:
            s = s + chr(x+64)
    return s


#Calcula las frecuencias de aparición de cada letra en una cadena de texto (en mayúsculas)
def frecuencias(texto):
    tabla = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    lista = cadenatolista(texto)
    for x in lista:
        tabla[x] = tabla[x]+1
    return tabla


#Calcula el indice de coincidencia de un texto.
def indice_coincidencia(texto):
    tabla = frecuencias(texto)
    num_caracteres = 0
    aux = 0
    for x in tabla:
        num_caracteres +=x
        aux = aux + x*(x-1)
    ic = aux/(num_caracteres*(num_caracteres-1))
    return ic


#Divide un texto en n subtextos, recorriéndolo de n en n.
def divide_cadena(cadena,n):
     subcadenas = []
     for i in range(n):
         subcadenas.append('')
     j = 0
     for x in cadena:
         subcadenas[j] = subcadenas[j] + x
         j = (j+1)%n
     return subcadenas


#Dado un texto y una clave  (ambos un string con mayúsculas), lo cifra usando el cifrado de Vigenère
def cifra_vigenere(texto,clave):
     lista_texto = cadenatolista(texto)
     lista_clave = cadenatolista(clave)
     (n,m) = (len(lista_texto),len(lista_clave))
     for i in range(n):
          lista_texto[i] = (lista_texto[i] + lista_clave[i%m])%27
     texto_cifrado = listatocadena(lista_texto)
     return texto_cifrado

#Dado un texto y una clave  (ambos un string con mayúsculas), lo cifra usando el cifrado de Vigenère
def descifra_vigenere(texto,clave):
     lista_texto = cadenatolista(texto)
     lista_clave = cadenatolista(clave)
     (n,m) = (len(lista_texto),len(lista_clave))
     for i in range(n):
          lista_texto[i] = (lista_texto[i] - lista_clave[i%m])%27
     texto_cifrado = listatocadena(lista_texto)
     return texto_cifrado


"""Dado un texto y una permutación de las letras (diccionario) lo cifra aplicando la sustitución dada
La sustitución hay que darla como un diccionario. Por ejemplo:
sustitucion = {'A':'B', 'B':'C', 'C':'D', 'D':'E', 'E':'F', 'F':'G', 'G':'H', 'H':'I', 'I':'J', 'J':'K', 'K':'L', 'L':'M', 'M':'N', 'N':'Ñ', 'Ñ':'O', 'O':'P', 'P':'Q', 'Q':'R', 'R':'S', 'S':'T', 'T':'U', 'U':'V', 'V':'W', 'W':'X', 'X':'Y', 'Y':'Z', 'Z':'A'}
que sustituye cada carácter por el que le sigue en el alfabeto
"""
def cifra_sustitucion(texto,permutacion):
     texto_cifrado = ''
     for x in texto:
         y = permutacion.get(x)
         texto_cifrado = texto_cifrado + str(y)
     return texto_cifrado

"""permutación es una lista de dos strings (de igual longitud). Por ejemplo, ['AEG',fkl']. En este caso, se recorre el texto y cada vez que encuentre un carácter que coincida con un de los que hay en 'AEG' lo sustituye por el correspondiente carácter en 'fkl'"""
def descifra_sustitucion(texto,permutacion):
     texto_des = ''
     p0 = permutacion[0]
     p1 = permutacion[1]
     for x in texto:
         if x in p0:
              pos = p0.index(x)
              texto_des = texto_des + p1[pos]
         else:
              texto_des = texto_des + x
     return texto_des 


#En un texto selecciona los m n-gramas que más se repiten (m=5 por defecto) y da la frecuencia de aparición de cada uno de ellos.
def ngramas_repetidos(texto,n,m=5):
    ngramas = []
    ngramasrep = []
    frecuencias = []
    for i in range(m):
        frecuencias.append(0)
        ngramasrep.append(texto[i:i+n])
    minimo = 0
    for i in range(len(texto)-n):
         aux = texto[i:i+n]
         if aux not in ngramas:
             f = 1
             ngramas.append(aux)
             for j in range(i+1,len(texto)-n):
                 if aux == texto[j:j+n]:
                     f+=1
             if f > minimo:
                 k = frecuencias.index(minimo)
                 ngramasrep[k] = aux
                 frecuencias[k] = f
                 minimo = min(frecuencias)
    return (ngramasrep,frecuencias)



#Dada una cadena y un texto calcula las veces en que aparece la cadena, y la separación entre estas apariciones.
def apariciones(cadena,texto):
    m = len(cadena)
    n = len(texto)
    posicion = []
    for i in range(n-m):
        if cadena == texto[i:i+m]:
            posicion.append(i)
    return (posicion,len(posicion))
     


#Recorre el texto de n en n, comenzando por la primera posición. Al llegar al final, comienza por la segunda posición y así sucesivamente. 
def cifra_transposicion(texto,n):
     m = len(texto)
     k = m%n
     texto_cif = ''
     for i in range(n):
         if i < k:
             aux = m//n+1
         else: 
             aux = m//n
         for j in range(aux):
             texto_cif = texto_cif + texto[i+n*j]
     return texto_cif

#Suponiendo que se ha recorrido de n en n un texto de tamaño m, nos dice en que posición estaría el carácter siguiente al que está en la posición x. Primero calculamos donde estaría el último, pues ese no tiene siguiente.
def siguiente(m,n,x):
     aux = m%n
     aux2 = m//n
     if aux == 0:
         ultimo = -1
     else: 
         ultimo = aux * (aux2 + 1) - 1
     if ultimo == -1 and x == m-1:
         return -1
     elif x < ultimo:
         return x+1+aux2
     elif x >= m - aux2:
         return x + aux2 + 1 - m
     elif x > ultimo:
         return x+aux2
     else:
         return -1


#Cuenta cuantas veces se repite una cadena en el fichero texto suponiendo que éste se ha obtenido recorriendo un fichero de n en n.
def ocurrencias(cadena,texto,n):
     l = len(texto)
     k = len(cadena)
     ocur = 0
     for i in range(l):
          contador = i
          cadenab = ''
          for j in range(k):
              if contador == -1:
                    cadenab = cadenab + ' '
                    contador = 0
              else:
                    cadenab = cadenab + texto[contador]
                    contador = siguiente(l,n,contador)
          if cadena == cadenab:
              ocur +=1
     return ocur

f1 = open('VictorGarciaMarcelKemp1.txt', mode='r', encoding='utf-8')    #Resuelto
f2 = open('VictorGarciaMarcelKemp2.txt', mode='r', encoding='utf-8')    #Resuelto
f3 = open('VictorGarciaMarcelKemp3.txt', mode='r', encoding='utf-8')    #Resuelto
f4 = open('VictorGarciaMarcelKemp4.txt', mode='r', encoding='utf-8')    #Resuelto
#f5 = open('Textocifrado.txt', mode='r', encoding='utf-8')               #Resuelto

#------------------------------------
""" #Algoritmo Cesar
abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
#cad="ABCZ"
cad3=f3.read()

max = 0
frecuencias = frecuencias(cad3)
print(frecuencias)
# Obtenemos la letra del texto cifrado
for frecletra in frecuencias:
    if frecletra > max:
        max = frecletra

# La letra con mayor frecuencia en un texto en castellano es la "E", codificada como 4
# La letra con mayor frecuencia en frecuencias(cad3) será la "E" cifrada
posclave = frecuencias.index(max) - 4

print("Posible clave por análisis de frecuencias: K = " + str(posclave) )

descif=""
for k in range(1,27):
    for i in cad3:
        if i in abc:
            # Función de descifrado de Cesar con clave k
            descif += abc[(abc.index(i)-k)%(len(abc))]
        else:
            descif += i
    print(descif)
    descif=""
    time.sleep(2)
print("Texto descifrado con clave: K = 10")
k=10
for i in cad3:
        if i in abc:
            # Función de descifrado de Cesar con clave k
            descif += abc[(abc.index(i)-k)%(len(abc))]
        else:
            descif += i

print(descif) """

#----------------------------------------
"""#Algoritmo de sustitucion
sustitucion = {'A':'M','B':'X','C':'T','D':'G','E':'C','F':'K','G':'P','H':'J','I':'I','J':'B','K':'Z','L':'H',
               'M':'A', 'N':'R', 'Ñ':'S','O':'V','P':'Q','Q':'Y','R':'F','S':'L', 'T':'O', 'U':'N',
               'V':'Ñ', 'W':'E','X':'W', 'Y':'D','Z':'U'}
#perm=['','QUE']
cad=f2.read()       
print(ngramas_repetidos(cad,1))
print(ngramas_repetidos(cad,2))
print(ngramas_repetidos(cad,3))
print(ngramas_repetidos(cad,4))
print(frecuencias(cad))
print(cifra_sustitucion(cad,sustitucion))"""
#----------------------------------------
#Algoritmo de transposicion
cad='QUE'
cad4=f4.read()
#print(frecuencias(cad4))
    
#print(divide_cadena(cad4,2))
#print(ngramas_repetidos(cad4,3))
""" for k in range(1,len(cad4)):
    if(ocurrencias(cad,cad4,k)>5):
        print(ocurrencias(cad,cad4,k), k)  """

""" for k in range(1,len(cad4)): 
    if((k%31)==0): 
        print(cifra_transposicion(cad4,k), k) #217  """

#print(ocurrencias(cad,cad4,31))


 
""" texto=divide_cadena(cad4,217)

for x in range(0,31):
    txt=""
    for i in range(0,217):
        for j in range(0,31):
            txt+=texto[i][(j+x)%31]
    
    print(txt)
    print(x)
    time.sleep(3) """

"""
num=0
txt=""

for y in range(0,len(cad4)):
    txt+=cad4[num]
    num=siguiente(6731,31,num)
    
    
print(txt) """


#print(divide_cadena(cad4,217))
#txt2=cifra_transposicion(cad4,217)
#print(ngramas_repetidos(txt,3))
#print(len(cad4))

#------------------------------------------------------------------
#Cifrado de Vigenere

#cad1=f1.read()

#print(ngramas_repetidos(cad1,3))
#(['RJO', 'IJG', 'FFI', 'SUP', 'QGF'], [15, 14, 11, 13, 12])
""" print(apariciones('IJG',cad1)) """
#RJO: 204, 408, 444, 1339, 156, 413, 564, 1608, 48, 228, 252, 960, 264, 1452 mcd=1
#IJG: 1284, 588, 204, 12, 324, 588, 1080, 192, 264, 528, 456, 144, 1500 mcd=12

""" txt=divide_cadena(cad1,12)
print(frecuencias(txt[11]))          #R-O-C-A-M-B-O-L-E-S-C-O
print(ngramas_repetidos(txt[11],1))  """

#print(descifra_vigenere(cad1,'ROCAMBOLESCO'))

#----------------------------------------------------------------------
#Texto optativo: Vigenere
#cad5=f5.read()
""" for i in range(1,101):
    txt=divide_cadena(cad5,i)
    print(indice_coincidencia(txt[0]), i) """

""" print(ngramas_repetidos(cad5,1))
print(ngramas_repetidos(cad5,2))
print(ngramas_repetidos(cad5,3))
print(ngramas_repetidos(cad5,4)) """

#print(apariciones('ENL',cad5))     
#620, 230, 155, 115, 180, 15, 140, 470, 100, 70, 155, 350 mcd=5

""" txt=divide_cadena(cad5,5)
print(frecuencias(txt[4]))          #C-L-A-V-E
print(ngramas_repetidos(txt[4],1))   """

#print(descifra_vigenere(cad5,'CLAVE'))

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()

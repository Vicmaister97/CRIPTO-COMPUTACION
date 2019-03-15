En el fichero aleat.py se encuentran 2 códigos de generación de una secuencia aleatoria de bits.
    La primera versión (COMENTADA) se basa en codificar las letras de un texto cualquiera, generando una secuencia "aleatoria" de bits
        donde codificamos las vocales como 0 y las consonantes como 1. Basándome en que la estructura de las sílabas, que conforman las
        palabras del lenguaje, constan de parejas de consonantes y vocales que suelen alternarse, puede generarse una secuencia de 0 y 1
        donde el número de 0's y de 1's son "casi" iguales. Podríamos refinar los 2 grupos en los que particionamos la codificación de las letras,
        pero es necesario un estudio más profundo de la estructura de las sílabas y del lenguaje para analizar la posibilidad de obtener una
        secuencia con igual número de 0's que de 1's y que cumpla con otros estadísticos para poder considerarla algorítmicamente aleatoria

    NOTA: http://www.elcastellano.org/ns/edicion/2014/abril/silabas.html 
    
    La segunda versión (IMPLEMENTADA), la que considero la más óptima y aleatoria con la que pude dar, es la que aparece en el fichero aleat.py,
        que consta básicamente en codificar los dígitos de un número irracional cualquiera (carpeta "/ficheros",elegidas 2 versiones de pi y un irracional 
        ejemplo sqrt(7)) de forma que los dígitos pares se codifiquen como 0 y los impares como 1. La secuencia obtenida tiene mismo número de 0's que de 1's (igual
        distribución de pares-impares entre los dígitos 0-9) y es EQUIPROBABLE que, en los infinitos dígitos de un irracional, el siguiente dígito sea un dígito par
        o impar. Me baso, pues, en el supuesto matemático de que los dígitos de un número irracional son aleatorios (creo que demostrado). Considero algorítmicamente
        aleatorio este método de obtención de secuencias de bits aleatorios, y tremendamente óptimo pues existen infinitos irracionales que se pueden expresar y
        calcular de forma sencilla y rápida.

La secuencia aleatoria obtenida se encuentra en el fichero "aleat.txt", mediante la ejecución: python aleat.py /ficheros/pi.txt
NOTA: Si se desea replicar el resultado, borrar primero el actual fichero "aleat.txt"

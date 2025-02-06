# Señal EMG

## Descripción 
Este proyecto contiene el código para mostrar una señal EMG (electromiografía) a partir de los datos obtenidos del sitio web pyshionet, del estudio Gesture Recognition and Biometrics ElectroMyogram (Electromiograma de reconocimiento de gestos y biometría); también se muestra la relación señal ruido (SNR) con ruido gaussiano, ruido impulso y ruidos tipo artefacto.  

## Como lo realizamos 
Iniciamos obteniendo los datos de sitio web PhysioNet, después de elegir el estudio que tenga que ver con datos de EMG a trabajar, se buscan entre los archivos cargados uno que termine con la extensión .dat y .hea, que nos indican los datos obtenidos durante la toma de la EMG del estudio a trabajar.  
### Muestra de la señal EMG
Luego de descargar los archivos con los datos que contiene los movimientos de en este caso el participante 1, se cargan a Python que es el lenguaje trabajado para esta practica, con ayuda de la libreria wfdb, para que el eje x mostrara el tiempo y no las muestras tomadas realizamos el siguiente vector:
```pitón
tiempo = np.arange(len(senal)) / fs
```
Se logra obtener la siguiente señal emg, que es de los movimientos de flexión de muñeca, extensión de muñeca:

![señal ](https://github.com/user-attachments/assets/48740300-8fb9-4100-830d-b2c84479f3cf)
*Señal EMG, voltaje vs tiempo.*

### 1 Calculos estadisticos 
Despues de obtener lo anterior,realizamos los calculos a mano y con funciones de python del promedio (media),desviacion estandar y coefisiente de variacion,

### -La media:
En este caso desimos que es el valor ("promedio") de todos los puntos en la señal de la EMG, para que sea mejor entendido se puede imaginar que la señal es como un grafico entonces el promedio seria el punto medio de esta linea.

 Calculo manual:
 ``` pitón
total=0
for i in range(len(senal)):
    total += senal[i]
media_manual = toatal / len(senal)
```
Funcion de python:
``` pitón
media_numpy = np.mean(senal)
```

### -Desviacion estandar:
Es la muestra de que tan dispesa es la señal, seidentifica las dos modalidades pues si la desviacion es baja o pequeña podemos decir que la señal es constante pero si la desviacion es grande la señal tiene muchas variaciones (seria lo contrario a la pequeña).

 Calculo manual:
``` pitón
suma_cuadrados = 0
for i in range(len(senal)):
    suma_cuadrados += (senal[i] - media_manual) ** 2
desv_manual = (suma_cuadrados / len(senal)) ** 0.5 
```
Funcion de python:
``` pitón
desv_numpy = np.std(senal)
```
### -Coefisiente de variacion:
Aca se centra en la relacion de la desviacion estandar y la media,lo cual indica si la señal es más estable o muy cambiante en comparación con su valor promedio.

 Calculo manual:
``` pitón
coef_var_manual = desv_manual / media_manual
```
Funcion de python:
``` pitón
coef_var_numpy = desv_numpy / media_numpy
```
## 2. Histograma y funcion de probabilidad 



## 3. Gerneramos ruidos 

Realizamos los calculos adecuados para los siguientes items:

### Ruido gausiano: 
Podemos evidenciar que este puede ser una interferencia muy fuerte o muy suave,lo podemos evidenciar si lo comparamos como si fuese un "Ruido de fondo" que en su totalidad afectarian a la señal. Lo entenderiamos mejor como si estuvieramos gravando un audio y al mismo tiempo alguien estuviera hablando de fondo 

### Ruido de impulsos: 
imaginemos que esta la señal y de repente en el medio hay un golpe o se crea una distorsion en un punto especifico, que seria lo que crea este ruido. 

### Ruido de artefacto:
Es un ruido repetitivo que parece una onda constante, como si fuera un sonido rítmico que no tiene nada que ver con la señal original.


## 3.1 Relacion Señal / Ruido 

El concepto de Relacion Señal-Ruido o mas conocido por sus siglas "SNR" es una medida que nos dice que tan clara esta la señal o si por el contrario esta tapada por el ruido, si el SNR es alto quiere decir que la señal es clara y el ruido como tal no la interrumpe mucho pero si la señal es baja seria todo lo contrario,el ruido estaria interrumpiendo demasiado con la señal haciendola mas dificil de analizar 










# Señal EMG

## Descripción 
Este proyecto contiene el código para mostrar una señal EMG (electromiografía) a partir de los datos obtenidos del sitio web pyshionet, del estudio Gesture Recognition and Biometrics ElectroMyogram (Electromiograma de reconocimiento de gestos y biometría) realizado por Jiang N., Pradha A., He, J.; también se muestra la relación señal ruido (SNR) con ruido gaussiano, ruido impulso y ruidos tipo artefacto.  

## Como lo realizamos 
Lo que hace este código es:
### 1. Obtenemos la señal 
Despues de obtener la señal, el archivo contiene los datos de una persona relizando algun ovimiento,despues el codigo los carga, sabemos que esta señal obtenida muestra la actividad de los musculos cuando alguien se mueve,siendo muy paresida a una onda senosoidal (una onda que sube y baja ) segun la fuerza con la que el musculo es movido.
### 1
Despues de obtener lo anterior,realizamos los calculos a mano y con funciones de python del promedio (media),desviacion estandar y coefisiente de variacion,

### -La media:
En este caso desimos que es el valor ("promedio") de todos los puntos en la señal de la EMG, para que sea mejor entendido se puede imaginar que la señal es como un grafico entonces el promedio seria el punto medio de esta linea

### -Desviacion estandar:
Es la muestra de que tan dispesa es la señal, seidentifica las dos modalidades pues si la desviacion es baja o pequeña podemos decir que la señal es constante pero si la desviacion es grande la señal tiene muchas variaciones (seria lo contrario a la pequeña).

### -Coefisiente de variacion:
Aca se centra en la relacion de la desviacion estandar y la media,lo cual indica si la señal es más estable o muy cambiante en comparación con su valor promedio.

### 2

``` pitón
total=0
for i in range(len(senal)):
    total += senal[i]
media_manual = toatal / len(senal)
```

``` pitón
suma_cuadrados = 0
for i in range(len(senal)):
    suma_cuadrados += (senal[i] - media_manual) ** 2
desv_manual = (suma_cuadrados / len(senal)) ** 0.5 
```

``` pitón
coef_var_manual = desv_manual / media_manual
```

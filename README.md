# Señal EMG

## Descripción 
Este proyecto contiene el código para mostrar una señal EMG (electromiografía) a partir de los datos obtenidos del sitio web pyshionet, del estudio Gesture Recognition and Biometrics ElectroMyogram (Electromiograma de reconocimiento de gestos y biometría) realizado por Jiang N., Pradha A., He, J.; también se muestra la relación señal ruido (SNR) con ruido gaussiano, ruido impulso y ruidos tipo artefacto.  

## Como lo realizamos 
Lo que hace este código es:

1. Obtener la señal: Primero, el código recibe una grabación (como si fuera un video, pero de señales eléctricas) de una persona moviendo su brazo. Esta señal nos muestra la fuerza con la que se mueve el músculo.

2. Calcular algunos números importantes: El código calcula algunos valores sobre esta señal para poder entenderla mejor:

- Promedio (media): Es como si contaras todos los puntos de la señal y luego encontraras el número que más o menos "representa" a todos esos puntos. Es como encontrar el punto medio de algo.
- Desviación estándar: Este número nos dice qué tan "dispersa" o "repartida" está la señal. Si está muy dispersa, quiere decir que hay muchos cambios grandes; si está menos dispersa, los cambios son pequeños.
- Coeficiente de variación: Es como un número que compara la dispersión con el promedio para ver si la señal es más estable o muy variable.

3. Generar ruidos: El código luego pone "ruidos" a la señal, como si alguien hablara mientras grabas, y queremos ver cómo cambia la señal cuando eso pasa. Hay diferentes tipos de ruidos:

- Ruido Gaussiano: Es como un sonido suave o fuerte que se mete en la señal. Algunos ruidos son muy fuertes y otros son más suaves, como si alguien hablara bajito.
- Ruido de Impulsos: Es como si, de repente, un sonido muy fuerte (como un golpe) aparece en la señal.
- Ruido de Artefactos: Es como un sonido repetitivo, como si algo estuviera haciendo un ruido constante, pero no tiene que ver con la señal real.
- Medir la relación entre la señal y el ruido (SNR): Después, el código calcula algo llamado SNR. Esto nos dice qué tan fuerte es la señal original comparada con el ruido que la interrumpe. Si la SNR es alta, eso significa que la señal es más clara y el ruido no la molesta mucho. Si la SNR es baja, el ruido hace más difícil escuchar la señal real.

4. Dibujar los resultados: Finalmente, el código dibuja todo lo que sucedió en gráficos para que podamos verlo:

- Un gráfico muestra cómo se ve la señal original.
- Otro gráfico muestra cómo la señal cambia con el ruido.
- También dibuja el histograma (gráficos de barras) que nos ayudan a ver cómo se distribuyen los valores de la señal y el ruido.


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

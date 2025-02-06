# Señal EMG

## Descripción 
Este proyecto contiene el código para mostrar una señal EMG (electromiografía) a partir de los datos obtenidos del sitio web pyshionet, del estudio Gesture Recognition and Biometrics ElectroMyogram (Electromiograma de reconocimiento de gestos y biometría); también se muestra la relación señal ruido (SNR) con ruido gaussiano, ruido impulso y ruidos tipo artefacto.  

## Como lo realizamos 
Iniciamos obteniendo los datos de sitio web PhysioNet, después de elegir el estudio que tenga que ver con datos de EMG a trabajar, se buscan entre los archivos cargados uno que termine con la extensión .dat y .hea, que nos indican los datos obtenidos durante la toma de la EMG del estudio a trabajar.  
### Muestra de la señal EMG
Luego de descargar los archivos con los datos que contiene los movimientos de en este caso el participante 1, se cargan a Python que es el lenguaje trabajado para esta practica, con ayuda de la libreria wfdb, se logra obtener la siguiente señal emg, que es de los movimientos de flexión de muñeca, extensión de muñeca con una señal de muestreo de 1000 Hz:

![señal ](https://github.com/user-attachments/assets/48740300-8fb9-4100-830d-b2c84479f3cf)
*Señal EMG, voltaje vs tiempo.*

Para que el eje x mostrará el tiempo y no las muestras tomadas realizamos el siguiente vector:
```pitón
tiempo = np.arange(len(senal)) / fs
```
### Cálculos Estadísticos
Despues de obtener lo anterior, realizamos los cálculos estadísticos de la media, desviación estándar y coeficiente de variación, utilizando dos tipos de métodos para hallar esos valores, el primer método es “manual” generando un for donde recorra cada muestra de la señal y nos indique cada valor usando las formulas estadísticas descritas para cada medida. 
Por otro lado, también se realizaron los cálculos de cada medida con las funciones que vienen incluidas en el lenguaje de Python
### -La media:
En este caso, nos referimos a la media como el "promedio" de todos los puntos en la señal de la EMG. Para entenderlo mejor, imagina que la señal es un gráfico: el promedio seria el punto medio de esa línea, representando el valor central de todos los puntos en la señal. 

 Cálculo manual:
 ``` pitón
total=0
for i in range(len(senal)):
    total += senal[i]
media_manual = toatal / len(senal)
```
Cálculo de python:
``` pitón
media_numpy = np.mean(senal)
```

### -Desviación estándar:
Es la muestra de que tan alejados están cada uno de los datos de la media o promedio, si están muy dispersos la desviación estándar será grande, por el contrario, si son muy concentrados la desviación estándar será pequeña. 

 Cálculo manual:
``` pitón
suma_cuadrados = 0
for i in range(len(senal)):
    suma_cuadrados += (senal[i] - media_manual) ** 2
desv_manual = (suma_cuadrados / len(senal)) ** 0.5 
```
Cálculo de python:
``` pitón
desv_numpy = np.std(senal)
```
### -Coeficiente de variación:
Se centra en la relación de la desviación estándar y la media,lo cual indica si la señal es más estable o muy cambiante en comparación con su valor promedio.

 Cálculo manual:
``` pitón
coef_var_manual = desv_manual / media_manual
```
Cálculo de python:
``` pitón
coef_var_numpy = desv_numpy / media_numpy
```
 
## 2. Histograma y funcion de probabilidad 
Con la señal obtenida, logramos graficar el histograma y la función de probabilidad de la señal EMG trabajada.
``` pitón
hist, bins = np.histogram(senal, bins=50, density=True)
bin_centers = (bins[:-1] + bins[1:]) / 2
```
Se obtuvo lo siguiente:

![histograma](https://github.com/user-attachments/assets/58bee68a-8078-4a61-b5aa-da5a61fba413)
*Histograma + funcion de probabilidad.*

## 3.Relacion Señal / Ruido 

El concepto de Relacion Señal-Ruido o mas conocido por sus siglas "SNR" es una medida que nos dice que tan clara esta la señal o si por el contrario esta tapada por el ruido, si el SNR es alto quiere decir que la señal es clara y el ruido como tal no la interrumpe mucho pero si la señal es baja seria todo lo contrario,el ruido estaria interrumpiendo demasiado con la señal haciendola mas dificil de analizar 

## 3.1 Gerneramos ruidos 

Realizamos los calculos adecuados para generar los ruidos gaussiano, ruido de impulsos y ruido de artefacto, como se evidenciará más adelante. 

### Ruido gaussiano: 
Podemos evidenciar que este puede ser una interferencia muy fuerte o muy suave, se logra ver si lo comparamos como si fuese un "Ruido de fondo" que en su totalidad afectaria a la señal. Lo entenderiamos mejor como si estuvieramos grabando un audio y al mismo tiempo alguien estuviera hablando de fondo, esto lo realizamos para un ruido fuerte y uno sueve:

```pitón
ruido_gauss_fuerte = np.random.normal(0, 0.2, len(senal))
ruido_gauss_suave = np.random.normal(0, 0.1, len(senal))
senal_ruidosa_gauss_fuerte = senal + ruido_gauss_fuerte
senal_ruidosa_gauss_suave = senal + ruido_gauss_suave
snr_gauss_fuerte = calcular_snr(senal_ruidosa_gauss_fuerte, ruido_gauss_fuerte)
snr_gauss_suave = calcular_snr(senal_ruidosa_gauss_suave, ruido_gauss_suave)
```


### Ruido de impulsos: 
Imaginemos que esta la señal y de repente en el medio hay un golpe o se crea una distorsion en un punto especifico, que seria lo que crea este ruido, esto lo realizamos para un ruido fuerte y uno sueve:

```pitón
ruido_impulsos_fuerte = np.zeros(len(senal))
indices_fuerte = np.random.choice(len(senal), size=int(len(senal) * 0.05), replace=False)
ruido_impulsos_fuerte[indices_fuerte] = np.random.uniform(-1, 1, len(indices_fuerte))
ruido_impulsos_suave = np.zeros(len(senal))
indices_suave = np.random.choice(len(senal), size=int(len(senal) * 0.025), replace=False)
ruido_impulsos_suave[indices_suave] = np.random.uniform(-0.5, 0.5, len(indices_suave))

senal_ruidosa_impulsos_fuerte = senal + ruido_impulsos_fuerte
senal_ruidosa_impulsos_suave = senal + ruido_impulsos_suave
snr_impulsos_fuerte = calcular_snr(senal_ruidosa_impulsos_fuerte, ruido_impulsos_fuerte)
snr_impulsos_suave = calcular_snr(senal_ruidosa_impulsos_suave, ruido_impulsos_suave)
```
### Ruido de artefacto:
Es un ruido repetitivo que parece una onda constante, como si fuera un sonido rítmico que no tiene nada que ver con la señal original,esto lo realizamos para un ruido fuerte y uno sueve:

```pitón
ruido_artefacto_fuerte = 0.3 * np.sin(2 * np.pi * np.arange(len(senal)) / 50)
ruido_artefacto_suave = 0.15 * np.sin(2 * np.pi * np.arange(len(senal)) / 50)
senal_ruidosa_artefacto_fuerte = senal + ruido_artefacto_fuerte
senal_ruidosa_artefacto_suave = senal + ruido_artefacto_suave
snr_artefacto_fuerte = calcular_snr(senal_ruidosa_artefacto_fuerte, ruido_artefacto_fuerte)
snr_artefacto_suave = calcular_snr(senal_ruidosa_artefacto_suave, ruido_artefacto_suave)
```
Segun lo anterior se obtuvo lo siguiente:

![ruido](https://github.com/user-attachments/assets/a520c2b2-f0f7-4a92-81f3-626a4be27422)
*SNR*

## Referencias 
[1] Quevedo F. Medidas de tendencia central y dispersión. Medwave 2011 Mar;11(3). https://dsp.facmed.unam.mx/wp-content/uploads/2013/12/Quevedo-F.-Medidas-de-tendencia-central-y-dispersion.-Medwave-2011-Ma-113..pdf
[2] Recursos Informáticos, T. del C. A. (s/f). SNR (Signal To Noise Ratio). Weebly.com. https://recursoinformatico.weebly.com/uploads/1/0/7/3/107381475/snr.pdf










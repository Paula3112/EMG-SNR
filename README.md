# Señal EMG

## Descripción 
Este proyecto contiene el código para mostrar una señal EMG (electromiografía) a partir de los datos obtenidos del sitio web pyshionet, del estudio Gesture Recognition and Biometrics ElectroMyogram (Electromiograma de reconocimiento de gestos y biometría) realizado por Jiang N., Pradha A., He, J.; también se muestra la relación señal ruido (SNR) con ruido gaussiano, ruido impulso y ruidos tipo artefacto.  

## 1. Carga de la Señal desde PhysioNet

Se importa la biblioteca wfdb para leer registros de PhysioNet y numpy para el manejo de datos numéricos. Además, se utiliza matplotlib para la visualización de datos.
``` pitón
import wfdb
import numpy as np
import matplotlib.pyplot as plt

archivo = "session1_participant1_gesture10_trial5"
registro = wfdb.rdrecord(archivo)
datos = registro.p_signal
canales = registro.sig_name
fs = registro.fs  # Frecuencia de muestreo
```



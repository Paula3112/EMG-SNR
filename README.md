# Señal EMG

## Descripción 
Este documento abarca informacion.

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



import wfdb
import numpy as np
import matplotlib.pyplot as plt

# Cargar la señal desde PhysioNet ---
archivo = "session1_participant1_gesture10_trial5"
registro = wfdb.rdrecord(archivo)
datos = registro.p_signal
canales = registro.sig_name
fs = registro.fs  # Frecuencia de muestreo

# Selección de canal
canal_seleccionado = 0
senal = datos[:, canal_seleccionado]
nombre_canal = canales[canal_seleccionado]

# Crear vector de tiempo en segundos
tiempo = np.arange(len(senal)) / fs

# Cálculo manual de estadísticos
total = 0
for i in range(len(senal)):
    total += senal[i]
media_manual = total / len(senal)

suma_cuadrados = 0
for i in range(len(senal)):
    suma_cuadrados += (senal[i] - media_manual) ** 2
desv_manual = (suma_cuadrados / len(senal)) ** 0.5  # Desviación estándar

coef_var_manual = desv_manual / media_manual
# Histograma + Función de Probabilidad
hist, bins = np.histogram(senal, bins=50, density=True)
bin_centers = (bins[:-1] + bins[1:]) / 2

# Comparación con funciones de Python 
media_numpy = np.mean(senal)
desv_numpy = np.std(senal)
coef_var_numpy = desv_numpy / media_numpy


# Relación Señal-Ruido (SNR) ---
def calcular_snr(senal_ruidosa, ruido):
    potencia_senal_ruidosa = np.mean(senal_ruidosa ** 2)  # Potencia de la señal con ruido
    potencia_ruido = np.mean(ruido ** 2)  # Potencia del ruido
    return 10 * np.log10(potencia_senal_ruidosa / potencia_ruido)  # SNR positivo

#  Generación de ruidos con dos niveles de intensidad ---
# Ruido Gaussiano
ruido_gauss_fuerte = np.random.normal(0, 0.2, len(senal))
ruido_gauss_suave = np.random.normal(0, 0.1, len(senal))
senal_ruidosa_gauss_fuerte = senal + ruido_gauss_fuerte
senal_ruidosa_gauss_suave = senal + ruido_gauss_suave
snr_gauss_fuerte = calcular_snr(senal_ruidosa_gauss_fuerte, ruido_gauss_fuerte)
snr_gauss_suave = calcular_snr(senal_ruidosa_gauss_suave, ruido_gauss_suave)

# Ruido de Impulsos
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

# Ruido de Artefacto
ruido_artefacto_fuerte = 0.3 * np.sin(2 * np.pi * np.arange(len(senal)) / 50)
ruido_artefacto_suave = 0.15 * np.sin(2 * np.pi * np.arange(len(senal)) / 50)
senal_ruidosa_artefacto_fuerte = senal + ruido_artefacto_fuerte
senal_ruidosa_artefacto_suave = senal + ruido_artefacto_suave
snr_artefacto_fuerte = calcular_snr(senal_ruidosa_artefacto_fuerte, ruido_artefacto_fuerte)
snr_artefacto_suave = calcular_snr(senal_ruidosa_artefacto_suave, ruido_artefacto_suave)
# Interfaz de la Señal EMG y su Histograma ---
fig1, axs1 = plt.subplots(2, 1, figsize=(10, 8), constrained_layout=True)

# Señal EMG en función del tiempo
axs1[0].plot(tiempo, senal, color='pink')
axs1[0].set_title("Señal EMG Original")
axs1[0].set_xlabel("Tiempo (s)")
axs1[0].set_ylabel("Voltaje (mV)")
axs1[0].grid()
# Histograma + Función de Probabilidad
axs1[1].hist(senal, bins=50, color='purple', alpha=0.7, label="Histograma", density=True)
axs1[1].plot(bin_centers, hist, color='orange', linewidth=2, label="Densidad de Probabilidad")
axs1[1].set_title("Histograma y Función de Probabilidad")
axs1[1].set_xlabel("Voltaje (mV)")
axs1[1].set_ylabel("Frecuencia / Densidad") 
axs1[1].grid()
axs1[1].legend()
#--- Agregar resultados en la pantalla (Primera interfaz) ---
resultados_texto = f"""
Cálculos Manuales:
Media: {media_manual:.4f} mV
Desviación estándar: {desv_manual:.4f} mV
Coef. de variación: {coef_var_manual:.4f}

Cálculos con Python:
Media: {media_numpy:.4f} mV
Desviación estándar: {desv_numpy:.4f} mV
Coef. de variación: {coef_var_numpy:.4f}
"""
axs1[1].text(0.05, 0.8, resultados_texto, transform=axs1[1].transAxes, fontsize=10,
             verticalalignment='top', bbox=dict(facecolor='white', alpha=0.7))


#  Gráficos de ruidos en una sola interfaz ---
fig, axs = plt.subplots(3, 2, figsize=(12, 10), constrained_layout=True)

# Ruido Gaussiano
axs[0, 0].plot(tiempo, senal, label="Señal Original", alpha=0.5, color='black')
axs[0, 0].plot(tiempo, senal_ruidosa_gauss_fuerte, label="Ruido Gaussiano Fuerte", alpha=0.7, color='red')
axs[0, 0].set_title(f"Ruido Gaussiano Fuerte (SNR = {snr_gauss_fuerte:.2f} dB)")
axs[0, 0].legend()
axs[0, 0].grid()

axs[0, 1].plot(tiempo, senal, label="Señal Original", alpha=0.5, color='black')
axs[0, 1].plot(tiempo, senal_ruidosa_gauss_suave, label="Ruido Gaussiano Suave", alpha=0.7, color='darkred')
axs[0, 1].set_title(f"Ruido Gaussiano Suave (SNR = {snr_gauss_suave:.2f} dB)")
axs[0, 1].legend()
axs[0, 1].grid()

# Ruido de Impulsos
axs[1, 0].plot(tiempo, senal, label="Señal Original", alpha=0.5, color='black')
axs[1, 0].plot(tiempo, senal_ruidosa_impulsos_fuerte, label="Ruido de Impulsos Fuerte", alpha=0.7, color='green')
axs[1, 0].set_title(f"Ruido de Impulsos Fuerte (SNR = {snr_impulsos_fuerte:.2f} dB)")
axs[1, 0].legend()
axs[1, 0].grid()

axs[1, 1].plot(tiempo, senal, label="Señal Original", alpha=0.5, color='black')
axs[1, 1].plot(tiempo, senal_ruidosa_impulsos_suave, label="Ruido de Impulsos Suave", alpha=0.7, color='darkgreen')
axs[1, 1].set_title(f"Ruido de Impulsos Suave (SNR = {snr_impulsos_suave:.2f} dB)")
axs[1, 1].legend()
axs[1, 1].grid()

# Ruido de Artefacto
axs[2, 0].plot(tiempo, senal, label="Señal Original", alpha=0.5, color='black')
axs[2, 0].plot(tiempo, senal_ruidosa_artefacto_fuerte, label="Ruido de Artefacto Fuerte", alpha=0.7, color='blue')
axs[2, 0].set_title(f"Ruido de Artefacto Fuerte (SNR = {snr_artefacto_fuerte:.2f} dB)")
axs[2, 0].legend()
axs[2, 0].grid()

axs[2, 1].plot(tiempo, senal, label="Señal Original", alpha=0.5, color='black')
axs[2, 1].plot(tiempo, senal_ruidosa_artefacto_suave, label="Ruido de Artefacto Suave", alpha=0.7, color='darkblue')
axs[2, 1].set_title(f"Ruido de Artefacto Suave (SNR = {snr_artefacto_suave:.2f} dB)")
axs[2, 1].legend()
axs[2, 1].grid()



# Mostrar gráficos
plt.show()

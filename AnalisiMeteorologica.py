import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Dati simulati per la temperatura (in gradi Celsius) e l'umidità (in percentuale)
giorni = ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica']
temperature = [22, 24, 19, 21, 23, 25, 26]
umidita = [60, 55, 65, 70, 50, 45, 40]


# 1. Grafico a linee: Temperatura durante la settimana
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
plt.plot(giorni, temperature, marker='o', color='blue', label='Temperatura (°C)')
plt.title('Temperatura durante la Settimana')
plt.xlabel('Giorni')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.legend()

# 2. Grafico a linee: Umidità durante la settimana
plt.subplot(2, 2, 2)
plt.plot(giorni, umidita, marker='o', color='green', label='Umidità (%)')
plt.title('Umidità durante la Settimana')
plt.xlabel('Giorni')
plt.ylabel('Umidità (%)')
plt.grid(True)
plt.legend()


# 3. Linea di regressione sulla temperatura
# Creiamo un array di indici per la regressione
x = np.arange(len(giorni))  # Indici dei giorni (0, 1, 2, ..., 6)
slope, intercept, r_value, p_value, std_err = stats.linregress(x, temperature)

# Linea di regressione
plt.subplot(2, 2, 3)
plt.plot(giorni, temperature, marker='o', color='blue', label='Temperatura (°C)')
plt.plot(giorni, slope * x + intercept, color='red', linestyle='--', label='Linea di Regressione')
plt.title('Temperatura e Linea di Regressione')
plt.xlabel('Giorni')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.legend()

# 4. Grafico combinato: Confronto tra Temperatura e Umidità
plt.subplot(2, 2, 4)
plt.plot(giorni, temperature, marker='o', color='blue', label='Temperatura (°C)')
plt.plot(giorni, umidita, marker='o', color='green', label='Umidità (%)')
plt.title('Confronto tra Temperatura e Umidità')
plt.xlabel('Giorni')
plt.ylabel('Valori')
plt.grid(True)
plt.legend()

#Mostra i grafici con un layout più ordinato
plt.tight_layout()
plt.show()


# 5. Analisi della correlazione tra Temperatura e Umidità
correlation = np.corrcoef(temperature, umidita)[0, 1]
print(f"Correlazione tra Temperatura e Umidità: {correlation:.2f}")
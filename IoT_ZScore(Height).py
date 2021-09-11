# Análisis de código de Python en la lección 12 de agosto con la variable Height.

import pandas as pd # importar libreria pandas, apodar con pd
import seaborn as sn # importat libreria seaborn, apodar sn
import matplotlib.pyplot as plt # importar libreria matplotlib.pyplot, apodar plt

filename = 'peso&altura.csv' # Nombre del archivo
df = pd.read_csv( filename ) # Cargar archivo csv en la variable df
df.head() # Imprimir solo las primeras 5 lineas de la variable df
df.describe() # Pedir caracteristicas generales de estadistica
sn.histplot( df.Height, kde = True ) # Impresión de mis datos en forma de histograma
plt.show() # Mostrar histograma basado en la altura

# Limpieza
mean = df.Height.mean() # Media de los datos
std = df.Height.std() # Desviación estandar
lowerBound = mean - 3 * std # Limite inferior
upperBound = mean + 3 * std  # Limite superior

df.Height[ df.Height < lowerBound ] # Outlier Fuera del rango de limete innferior
df.Height[ df.Height > upperBound ] # Outlier Fuera del rango de limite superior
df.Height[ ( df.Height < lowerBound ) | ( df.Height > upperBound ) ] # Mostrar ambos Outlier

df_no_outlier = df[ ( df.Height > lowerBound ) & ( df.Height < upperBound ) ]
df_no_outlier.head() # Imprimir solo las primeras 5 lineas de la variable df_no_outlier
df_no_outlier.count # Contar total de row

# Z-core Z = (x-u)/o = (dato - media) / desviación estandar
df[ 'z-score' ] = ( df.Height - mean ) / std # Conocer a cuantas desviaciones estandar se encuentran alejados nuestros datos de la media
df.head() # Imprimir solo las primeras 5 lineas de la variable df
sn.histplot( df['z-score'], kde = True ) # Impresión de mis datos en forma de histograma
plt.show() # Mostrar histograma basado en z-score
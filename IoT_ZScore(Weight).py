# Instrucciones
# Realice el mismo análisis de código de Python en la lección 12 de agosto, pero con la variable Weight. 
# Adjunte un pdf con la ejecución del código y los valores de salida, y también, incluya el enlace del repositorio de github.

import pandas as pd # importar libreria pandas, apodar con pd
import seaborn as sn # importat libreria seaborn, apodar sn
import matplotlib.pyplot as plt # importar libreria matplotlib.pyplot, apodar plt

filename = 'peso&altura.csv' # Nombre del archivo
df = pd.read_csv( filename ) # Cargar archivo csv en la variable df
df.head() # Imprimir solo las primeras 5 lineas de la variable df
df.describe() # Pedir caracteristicas generales de estadistica
sn.histplot( df.Weight, kde = True ) # Impresión de mis datos en forma de histograma
plt.show() # Mostrar histograma basado en la variable peso

# Limpieza
mean = df.Weight.mean() # Media de los datos
std = df.Weight.std() # Desviación estandar
lowerBound = mean - 3 * std # Limite inferior
upperBound = mean + 3 * std  # Limite superior

df.Weight[ df.Weight < lowerBound ] # Outlier Fuera del rango de limete innferior
df.Weight[ df.Weight > upperBound ] # Outlier Fuera del rango de limite superior
df.Weight[ ( df.Weight < lowerBound ) | ( df.Weight > upperBound ) ] # Mostrar ambos Outlier

# Datos limpios de Outlier
df_no_outlier = df[ ( df.Weight > lowerBound ) & ( df.Weight < upperBound ) ]
df_no_outlier.head() # Imprimir solo las primeras 5 lineas de la variable df_no_outlier
df_no_outlier.count # Contar total de row

# Z-core Z = ( x - u ) / o = (dato - media) / desviación estandar
df[ 'z-score' ] = ( df.Weight - mean ) / std # Conocer a cuantas desviaciones estandar se encuentran alejados nuestros datos de la media
df.head() # Imprimir solo las primeras 5 lineas de la variable df
sn.histplot( df['z-score'], kde = True ) # Impresión de mis datos en forma de histograma
plt.show() # Mostrar histograma basado en z-score

#End
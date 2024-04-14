# Maquina_Galton
Generar la simulación de la maquina de Galton

********************************************************************************
import numpy as np
import matplotlib.pyplot as plt
from random import randint                    #Añadieron las librerias para la generación de la grafica

niveles = 12
carril = [0]*(niveles)                        #Se declara el valor de las variables


for h in range(3000):
  stored = -1                                          #Se genera el contador para los niveles en un rango de 3000 posiciones (canicas)
  for j in range(niveles):
    stored += randint(0, 1) 
  carril[stored] += 1
print((3000), "las canicas se utilizaron en total")   #Se imprime el mensaje para identificar que el contador ha terminado
print(carril)


X = np.arange(-((len(carril)/2)-.5), (len(carril)/2)+.5)
plt.xlabel('Distribución de canicas')
plt.ylabel('Cantidad de canicas')                            #Se le da diseño a la grafica (Titulo, nombre de los ejes, ancho de las barras y color).
plt.title('Simulación de Máquina de Galton')
plt.bar(X + 0.00, carril, width=0.90, color = "green")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from random import randint

niveles = 12
carril = [0]*(niveles)


for h in range(3000):
  stored = -1
  for j in range(niveles):
    stored += randint(0, 1) 
  carril[stored] += 1
print((3000), "las canicas se utilizaron en total")
print(carril)


X = np.arange(-((len(carril)/2)-.5), (len(carril)/2)+.5)
plt.xlabel('Distribución de canicas')
plt.ylabel('Cantidad de canicas')
plt.title('Simulación de Máquina de Galton')
plt.bar(X + 0.00, carril, width=0.90, color = "green")
plt.show()

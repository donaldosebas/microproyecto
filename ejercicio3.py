import random
import numpy as np

limite = 10
resultados = []

for i in range(limite):
  u = random.random()
  if i < 1:
    ui = (1 / limite) * u + ((limite - 1) / limite)
  elif i < 3:
    ui = (3 / limite) * u + ((limite - 4) / limite)
  else:
    ui = ((limite - 4) / limite) * u

  resultados.append(-1*np.log(ui))

res = sum(resultados) / len(resultados)
print("Valor esperado", res)

  

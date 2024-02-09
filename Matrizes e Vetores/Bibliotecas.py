# Para operações mais avançadas com matrizes, você pode usar bibliotecas como NumPy.

import numpy as np

# Criando arrays (equivalentes a vetores/matrizes) com NumPy
vetor_numpy = np.array([1, 2, 3])
matriz_numpy = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Operações com NumPy
soma_vetores_numpy = vetor_numpy + vetor_numpy
produto_matrizes_numpy = np.dot(matriz_numpy, matriz_numpy)

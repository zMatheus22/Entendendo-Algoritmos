# Ordenação por Seleção

"""
Retorna o índice do menor elemento em uma lista.
Parâmetros:
  arr (list): Lista de elementos comparáveis de onde o menor elemento será buscado.
Retorna:
  int: O índice do menor elemento encontrado na lista.
Exemplo:
  >>> buscaMenor([3, 1, 4, 2])
  1
"""
def buscaMenor(arr):
  menor = arr[0]
  menor_index = 0
  for i in range(1, len(arr)):
    if arr[i] < menor:
      menor = arr[i]
      menor_index = i
  return menor_index


"""
Ordena uma lista de elementos usando o algoritmo de ordenação por seleção.
Parâmetros:
  arr (list): Lista de elementos comparáveis a serem ordenados. 
Retorna:
  list: Uma nova lista contendo os elementos ordenados em ordem crescente.
Exemplo:
  >>> ordenacaoSelecao([3, 1, 4, 2])
  [1, 2, 3, 4]
"""
def ordenacaoSelecao(arr):
  novoArr = []
  for i in range(len(arr)):
    menor = buscaMenor(arr)
    novoArr.append(arr.pop(menor))
  return novoArr


print(ordenacaoSelecao([5, 3, 6, 2, 10])) # retorno [2, 3, 5, 6, 10]
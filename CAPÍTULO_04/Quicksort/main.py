'''
❶ Base: arrays com 0 ou 1 elemento já estão “ordenados”.
❷ Caso recursivo.
❸ Subarray de todos os elementos menores do que o pivô.
❹ Subarray de todos os elementos maiores do que o pivô.
'''
def quicksort(array: list[int]) -> list[int]:
  if len(array) < 2:
    return array # ❶
  else:
    pivo = array[0] # ❷
    menores = [i for i in array[1:] if i <= pivo] # ❸
    maiores = [i for i in array[1:] if i > pivo] # ❹
    return quicksort(menores) + [pivo] + quicksort(maiores)

# Example usage
print(quicksort([3, 6, 8, 10, 1, 2, 1])) # Output: [1, 1, 2, 3, 6, 8, 10]

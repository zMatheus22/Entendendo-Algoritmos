# 4.1 Escreva o código para a função soma, vista anteriormente.
def soma(x: list[int]) -> int:
  if not x:
    return 0
  else:
    return x[0] + soma(x[1:])

print("Soma dos elementos da lista:")  
print(soma([1, 2, 3, 4, 5]))  # Output: 15
print(soma([]))  # Output: 0
print(soma([10, 20, 30]))  # Output: 60

# 4.2 Escreva uma função recursiva que conte o número de itens em uma lista.
def contar_itens(x: list) -> int:
  if not x:
    return 0
  else:
    return 1 + contar_itens(x[1:])

print("Número de itens na lista:")
print(contar_itens([1, 2, 3, 4, 5]))  # Output: 5
print(contar_itens([]))  # Output: 0
print(contar_itens(['a', 'b', 'c']))  # Output: 3

# 4.3 Encontre o valor mais alto em uma lista.
def maior(x: list[int])-> int:
  if not x:
    return 0
  elif len(x) == 1:
    return x[0]
  else:
    m = maior(x[1:])
    return x[0] if x[0] > m else m

print("Maior elemento da lista:")
print(maior([1, 2, 3, 4, 5]))  # Output: 5
print(maior([]))  # Output: 0
print(maior([10, 20, 30, 25]))  # Output: 30

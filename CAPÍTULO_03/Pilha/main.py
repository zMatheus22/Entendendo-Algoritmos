# Estrutura de uma pilha:
def sauda(nome):
  print("Olá, " + nome +"!")
  sauda2(nome) # Chama a função sauda2 (topo da pilha)
  print("preparando para dizer tchau...")
  tchau() # Chama a função tchau (topo da pilha)
  # Remove a pilha (Acabou!)


def sauda2(nome):
  print("Como vai "+nome+"?") 
  # Remove do topo da pilha


def tchau():
  print("ok, tchau!")
  # Remove do topo da pilha


# A pilha de chamada com recursão
def fatorial(num):
  if num == 1:
    return 1
  else:
    return num * fatorial(num - 1)

# print(fatorial(4))
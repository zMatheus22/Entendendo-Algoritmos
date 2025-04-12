# 1° opção para encontra a chave, recursão.
def porcure_pela_chave(caixa_principal):
  pilha = main_box.crie_uma_pilha_para_busca()
  while pilha is not vazio:
    caixa = pilha.pegue_caixa()
    for item in caixa:
      if item.e_uma_caixa():
        pilha.append(item)
      elif item.e_uma_chave():
        print("Achei a chave!")


# 2° opção para encontrar a chave, recursão
def procure_pela_chave(caixa):
  for item in caixa:
    if item.e_uma_caixa():
        procure_pela_chave(item)
    elif item.e_uma_chave():
      print("Achei a chave!")


# Caso-base e caso recursivo
def regressiva(num):
  print(num)
  if num <= 1:
    return # Caso-base
  else:
    regressiva(num - 1) # Caso recursivo

def pesquisa__binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        # Se o chute for muito baixo, você atualizará a variável baixo proporcionalmente:
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        if chute < item:
            baixo = meio + 1
    return None


minha_lista = [1, 3, 5, 7, 9]

print(pesquisa__binaria(minha_lista, 3)) # => Retorno 1
print(pesquisa__binaria(minha_lista, -1)) # => Retorno None

# EXERCÍCIO

É importante que funções hash retornem o mesmo valor de saída quando o
mesmo valor de entrada for inserido. Caso contrário, não será possível
encontrar o item que você deseja na tabela hash!
Quais destas funções hash são consistentes?

**(A)** `f(x) = 1` — Retorna **1** para qualquer entrada.

**(B)** `f(x) = rand()` — Retorna um número aleatório a cada execução.

**(C)** `f(x) = proximo_espaco_vazio()` — Retorna o índice do próximo espaço livre da tabela hash.

**(D)** `f(x) = len(x)` — Usa o comprimento da string como índice.

Resposta: Alternativa correta é a letra **(A)**

<hr>

É importante que funções hash tenham uma boa distribuição. Dessa forma,
elas ficam com o mapeamento mais amplo possível. O pior caso é uma
função hash que mapeia todos os itens para o mesmo espaço da tabela hash.
Suponha que você tenha estas quatro funções hash que operam com strings:

**(A)** Retorne “1” para qualquer entrada.

**(B)** Use o comprimento da string como o índice.

**(C)** Use o primeiro caractere da string como índice. Assim, todas as strings
que iniciam com a letra a são hasheadas juntas e assim por diante.

**(D)** Mapeie cada letra para um número primo: `a = 2, b = 3, c = 5, d = 7, e = 11`, e assim por diante. Para uma string, a função hash é a soma de todos
os caracteres-módulo
2 conforme o tamanho da hash. Se o tamanho de sua
hash for 10, por exemplo, e a string for “bag”, o índice será `(3 + 2 + 17) %
10 => 22 % 10 => 2`.

Para cada um destes exemplos, qual função hash fornecerá uma boa
distribuição? Considere que o tamanho da tabela hash tenha dez espaços.

**I** Uma lista telefônica em que as chaves são os nomes e os valores são os
números telefônicos. Os nomes são os seguintes: Esther, Ben, Bob e Dan.

**II** Um mapeamento do tamanho de baterias e sua devida potência. Os
tamanhos são A, AA, AAA e AAAA.

**III** Um mapeamento de títulos de livros e autores. Os títulos são Maus, Fun
Home e Watchmen.

Resposta:

| Caso | Melhor função hash                                                 |
| ---- | ------------------------------------------------------------------ |
| I    | (D) - Distribui bem os nomes com base nos caracteres               |
| II   | (B) ou (D) - Ambas distribuem bem, já que o padrão é o tamanho     |
| III  | (C) - Usar o primeiro caractere funciona bem para títulos variados |

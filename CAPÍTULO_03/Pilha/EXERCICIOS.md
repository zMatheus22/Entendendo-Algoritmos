# EXERCÍCIOS

### 3.1 Suponha que eu forneça uma pilha de chamada como esta:

| Pilha                       |
| --------------------------- |
| `Sauda2` -> Nome \| Matheus |
| `Sauda` -> Nome \| Matheus  |

### Quais informações você pode retirar baseando-se apenas nesta pilha de chamada?

Resposta: Considerando que se trata de uma pilha (último a entrar primeiro a sair), o elemento `Sauda2` é o primeiro a ser removido.

### 3.2 Suponha que você acidentalmente escreva uma função recursiva que fique executando infinitamente. Como você viu, seu computador aloca memória na pilha para cada chamada de função. O que acontece com a pilha quando a função recursiva fica executando infinitamente?

Resposta: Cada chamada recursiva irá adicionar dados na memória, e com a pilha sem a liberação dos dados anteriores (que não serão mais uteis). A função não terminar, a pilha crescerá continuamente até esgotar os recursos de memória.

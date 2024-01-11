# EXERCÍCIOS

## Forneça o tempo de execução para cada um dos casos a seguir em termos da notação Big O.

### 1.3 Você tem um nome e deseja encontrar o número de telefone para esse nome em uma agenda telefônica.

1° Resposta: Para a <strong>busca simples</strong> o pior caso seria O(n).
2° Resposta: Para a <strong>busca binária</strong> o pior caso seria O(log n).

### 1.4 Você tem um número de telefone e deseja encontrar o dono dele em uma agenda telefônica. (Dica: Deve procurar pela agenda inteira!)

Resposta: Para isso só é possivel utilizar a <strong>busca simples</strong> que no pior caso seria O(n).

### 1.5 Você quer ler o número de cada pessoa da agenda telefônica.

Resposta: Para isso devese utilizar a <strong>busca simples</strong> com pior caso sendo O(n).

### 1.6 Você quer ler os números apenas dos nomes que começam com A. (Isso é complicado! Esse algoritmo envolve conceitos que são abordados mais profundamente no Capítulo 4. Leia a resposta – você cará surpreso!)

Resposta: O(n). Você pode pensar: “Só estou fazendo isso para 1 dentre 26 caracteres, portanto o tempo de execução deve ser O(n/26).” Uma regra simples é a de ignorar números que são somados, subtraídos, multiplicados ou divididos. Nenhum desses são tempos de execução Big O: O(n + 26), O(n - 26), O(n \* 26), O(n / 26). Eles são todos o mesmo que O(n)! Por quê? Se você está com dúvidas, vá para “Notação Big O revisada”, no Capítulo 4, e leia a parte sobre constantes na notação Big O (uma constante é apenas um número; 26 era a constante desta questão).

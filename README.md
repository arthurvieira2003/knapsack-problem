# Algoritmo Genético para o Problema da Mochila

Este projeto implementa um algoritmo genético para resolver o problema da mochila, um problema clássico de otimização combinatória.

## Descrição do Problema

O problema da mochila consiste em selecionar itens de uma lista, cada um com um peso e um valor associados, para maximizar o valor total dos itens selecionados, respeitando uma capacidade máxima de peso da mochila.

## Implementação

O algoritmo genético é implementado em Python e segue as seguintes etapas:

1. **Inicialização**: Uma população inicial de soluções candidatas é gerada aleatoriamente.
2. **Avaliação**: Cada solução é avaliada com base em sua aptidão (valor total dos itens selecionados).
3. **Seleção**: Pais são selecionados para reprodução com base em sua aptidão.
4. **Cruzamento**: Novos indivíduos são criados combinando características dos pais.
5. **Mutação**: Pequenas alterações aleatórias são introduzidas nos novos indivíduos.
6. **Substituição**: A nova geração substitui a antiga.
7. **Iteração**: O processo é repetido por um número definido de gerações.

## Estrutura do Código

O código está organizado em várias funções:

- `criar_individuo()`: Gera um indivíduo aleatório.
- `criar_populacao()`: Cria a população inicial.
- `calcular_aptidao()`: Calcula a aptidão de um indivíduo.
- `selecao()`: Seleciona pais para reprodução.
- `cruzamento()`: Realiza o cruzamento entre dois pais.
- `mutacao()`: Aplica mutação a um indivíduo.
- `algoritmo_genetico()`: Executa o algoritmo genético completo.

## Parâmetros do Algoritmo

Os principais parâmetros do algoritmo são:

- Tamanho da população: 10
- Tamanho do genoma: 8
- Taxa de mutação: 0.1
- Número de gerações: 20
- Capacidade da mochila: 15

## Como Executar

Para executar o algoritmo, simplesmente rode o script Python.

O programa imprimirá a melhor aptidão encontrada em cada geração e, ao final, mostrará a melhor solução encontrada, incluindo o genoma, a aptidão e os itens selecionados.

## Resultados

O algoritmo imprime a melhor aptidão encontrada em cada geração e, ao final, exibe:

- O genoma da melhor solução
- A aptidão da melhor solução
- Os itens selecionados na melhor solução

Este algoritmo demonstra como técnicas de computação evolutiva podem ser aplicadas para resolver problemas de otimização complexos.

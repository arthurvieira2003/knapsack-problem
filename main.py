import random

TAMANHO_POPULACAO = 10
TAMANHO_GENOMA = 8
TAXA_MUTACAO = 0.1
GERACOES = 20
CAPACIDADE_MOCHILA = 15

itens = [(2, 3), (3, 4), (4, 5), (5, 8), (9, 10), (4, 7), (2, 6), (1, 2)]

def criar_individuo():
    return [random.randint(0, 1) for _ in range(TAMANHO_GENOMA)]

def criar_populacao():
    return [criar_individuo() for _ in range(TAMANHO_POPULACAO)]

def calcular_aptidao(individuo):
    peso_total = sum(itens[i][0] for i in range(TAMANHO_GENOMA) if individuo[i] == 1)
    valor_total = sum(itens[i][1] for i in range(TAMANHO_GENOMA) if individuo[i] == 1)
    
    if peso_total > CAPACIDADE_MOCHILA:
        return 0
    return valor_total

def selecao(populacao):
    pais = random.choices(
        populacao,
        weights=[calcular_aptidao(ind) for ind in populacao],
        k=2
    )
    return pais[0], pais[1]

def cruzamento(pai1, pai2):
    ponto_corte = random.randint(1, TAMANHO_GENOMA - 1)
    filho = pai1[:ponto_corte] + pai2[ponto_corte:]
    return filho

def mutacao(individuo):
    for i in range(TAMANHO_GENOMA):
        if random.random() < TAXA_MUTACAO:
            individuo[i] = 1 - individuo[i]
    return individuo

def algoritmo_genetico():
    populacao = criar_populacao()
    
    for geracao in range(GERACOES):
        nova_populacao = []
        
        for _ in range(TAMANHO_POPULACAO):
            pai1, pai2 = selecao(populacao)
            filho = cruzamento(pai1, pai2)
            filho = mutacao(filho)
            nova_populacao.append(filho)
        
        populacao = nova_populacao
        
        melhor_individuo = max(populacao, key=calcular_aptidao)
        print(f"Geração {geracao + 1}: Melhor aptidão = {calcular_aptidao(melhor_individuo)}")
    
    return max(populacao, key=calcular_aptidao)

melhor_solucao = algoritmo_genetico()
print("\nMelhor solução encontrada:")
print(f"Genoma: {melhor_solucao}")
print(f"Aptidão: {calcular_aptidao(melhor_solucao)}")
print(f"Itens selecionados: {[itens[i] for i in range(TAMANHO_GENOMA) if melhor_solucao[i] == 1]}")
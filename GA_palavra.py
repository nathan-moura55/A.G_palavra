import string 
import random
import time

palavra = input("Digite o texto: ")
x = len(palavra)

if x == 0:
    print("A palavra não pode ser vazia!")
    exit()

def gerar_individuo(tamanho=x):
    "gera individuos aleatorios"
    caracteres = string.ascii_letters + string.digits + "- "
    return ''.join(random.choices(caracteres, k=tamanho))

def calculo_fitness(individuo, palavra):
    "calcula o fitness"
    fitness = 0
    for char_ind, char_palavra in zip(individuo, palavra):
        if char_ind == char_palavra:
            fitness += 1
    return fitness

def gerar_populacao(tamanho_populacao):
    "gera uma população de individuos"
    return [gerar_individuo() for _ in range(tamanho_populacao)]

def selecao(populacao, palavra, k=50):
    "seleciona individuos para comparacao k = quantidade de individuos" 
    selecionados = random.choices(populacao, k=k)
    return max(selecionados, key=lambda ind: calculo_fitness(ind, palavra))

def crossover(pai_a, pai_b):
    "cruzamento de individuos"
    if len(pai_a) <= 1:
        return random.choice([pai_a, pai_b])
    ponto_corte = random.randint(1, len(pai_a) - 1)
    filho = pai_a[:ponto_corte] + pai_b[ponto_corte:]
    return filho

def mutacao(individuo, taxa_mutacao=0.05):
    "mutação de caracteristicas de individuos"
    lista_caracteres = list(individuo)
    caracteres_possiveis = string.ascii_letters + string.digits + "- "

    for i, char in enumerate(lista_caracteres):
        if random.random() < taxa_mutacao:
            lista_caracteres[i] = random.choice(caracteres_possiveis)
            
    return ''.join(lista_caracteres)


# --- CONFIGURAÇÕES DO USUÁRIO ---
TAMANHO_POPULACAO = 1000  
GERACOES_MAXIMAS = 1000
VELOCIDADE = 0.0

populacao = gerar_populacao(TAMANHO_POPULACAO)
historico_fitness = []  

print("\n--- INICIANDO A.G ---")

for geracao in range(1, GERACOES_MAXIMAS + 1):
    melhor_da_geracao = max(populacao, key=lambda ind: calculo_fitness(ind, palavra))
    fitness_melhor = calculo_fitness(melhor_da_geracao, palavra)
    
    historico_fitness.append(fitness_melhor)
    
    # --- CÁLCULO DA TAXA DE MUTAÇÃO DINÂMICA ---
    taxa_mutacao_atual = 0.20 - (0.18 * (fitness_melhor / x))
        
    tamanho_max_barra = 20
    proporcao = int((fitness_melhor / x) * tamanho_max_barra)
    barra = "█" * proporcao
    espacos = " " * (tamanho_max_barra - proporcao)
    
    print(f"Geracao {geracao:03d} | Mutação: {taxa_mutacao_atual*100:.1f}% | Melhor: {melhor_da_geracao} | Fitness: {fitness_melhor:02d}/{x:02d} | [{barra}{espacos}]")
    
    if fitness_melhor == x:
        print(f"\n>> Palavra encontrada na geração: {geracao}")
        break
        
    time.sleep(VELOCIDADE)

    nova_populacao = []
    nova_populacao.append(melhor_da_geracao)
    
    while len(nova_populacao) < TAMANHO_POPULACAO:
        pai1 = selecao(populacao, palavra)
        pai2 = selecao(populacao, palavra)
        
        filho = crossover(pai1, pai2)
        filho = mutacao(filho, taxa_mutacao_atual)
        
        nova_populacao.append(filho)
        
    populacao = nova_populacao
else:
    print("\n>> Limite de geracoes atingido.")

# --- GRÁFICO ---
print("\n" + "="*50)
print("       HISTORICO DE DESEMPENHO (EIXO Y)")
print("="*50)
print("Fitness")

linhas_grafico = 10
for i in range(linhas_grafico, 0, -1):
    nivel_fitness = int((i / linhas_grafico) * x)
    linha_texto = f"{nivel_fitness:02d} | "
    
    passo = max(1, len(historico_fitness) // 40)
    for g in range(0, len(historico_fitness), passo):
        if historico_fitness[g] >= nivel_fitness:
            linha_texto += "* "
        else:
            linha_texto += "  "
    print(linha_texto)

total_pontos_plotados = len(historico_fitness[::passo])
tamanho_linha = (2 * total_pontos_plotados) + 1

espaco_meio = max(1, (tamanho_linha // 2) - 5)

print("   " + "-" * tamanho_linha)
print("    0" + " " * espaco_meio + "Gerações (Eixo X)" + " " * espaco_meio + f"{len(historico_fitness)}")
# ============================================================
# Projeto: Teoria da Amostragem
# Autor: Leyvino Bezerra do Nascimento
# Data: 02/12/2025
# Descrição: Algoritmo da disciplina Estatistica com o conteudo do
# Professor Iranildo Guimaraes, sobre a Teoria da Amostragem em Python.
# ============================================================


# ------------------------------------------------------------
#  Introdução
# ------------------------------------------------------------

# A Teoria da Amostragem é o ramo da Estatística responsável pelo estudo de métodos para
# selecionar parte de uma população com o objetivo de obter informações sobre o todo. Em
# grande parte das situações práticas, observar toda a população é inviável devido a restrições
# de custo, tempo ou acessibilidade. Assim, torna-se necessário selecionar uma amostra
# bem planejada, que represente adequadamente a população.
# Uma amostra bem selecionada permite estimar parâmetros, construir intervalos de
# confiança, realizar testes de hipóteses e tomar decisões fundamentadas.


# ------------------------------------------------------------
# Conceitos Básicos
# ------------------------------------------------------------
# ============================================================
# População e Amostra
# População: conjunto de todos os elementos de interesse.
# Amostra: subconjunto da população selecionado conforme um método.
# ------------------------------------------------------------

# Unidade Amostral
# Elemento indivisível da população: pessoa, empresa, máquina, produto, lote, viveiro, etc.
# ------------------------------------------------------------

# Parâmetros e Estatísticas
# Parâmetro: característica desconhecida da população (µ, p, σ²).
# Estatística: medida calculada a partir da amostra (x̄, p̂, s²).
# ------------------------------------------------------------

# Erro Amostral
# É a diferença entre o valor verdadeiro do parâmetro e sua estimativa amostral:
# E = θ − θ̂
# ------------------------------------------------------------

# Amostragem Probabilística
# Na amostragem probabilística, cada unidade possui probabilidade conhecida e positiva de seleção.
# Isso permite realização de inferência estatística.
# ------------------------------------------------------------

# Amostragem Casual Simples (ACS)
# A Amostragem Casual Simples (ACS) ocorre quando todas as amostras possíveis de tamanho n
# têm a mesma probabilidade de serem escolhidas.
# ------------------------------------------------------------
# Exemplo Numérico:
# Uma loja tem uma lista com 10 clientes: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}.
# Deseja-se selecionar n = 3 clientes aleatoriamente.
# Uma possível amostra: {2, 5, 9}.
# ============================================================
# Exemplo em Python

import random as rd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


populacao = list (range(1 , 11) )
amostra = rd.sample(populacao, 3)
print('Amostragem Casual Simples (ACS)')
print ("Amostra selecionada :", amostra)

# ============================================================
# Amostragem Sistemática
# Nesse método, os elementos são selecionados em intervalos regulares,
# definidos pela fórmula: k = N / n
#
# Exemplo Numérico:
# População: 20 elementos
# Tamanho da amostra: 5
# k = 20 / 5 = 4
# Ponto inicial sorteado: 3
# Amostra resultante: {3, 7, 11, 15, 19}
# ============================================================
#Exemplo em Python:
N = 20
n = 5
k = N // n

inicio = rd.randint (1 , k )
amostra = list (range (inicio ,N +1 ,k ))
print('Amostragem Sistemática:')
print ("Amostra selecionada :", amostra)
# ============================================================
# Amostragem Estratificada
# A população é dividida em estratos homogêneos e amostras são retiradas de cada estrato.
# Exemplo Numérico:
# Uma empresa possui:
#   - 200 funcionários do setor A
#   - 100 funcionários do setor B
#   -  50 funcionários do setor C
# Deseja-se amostrar 35 funcionários.
#
# Alocação proporcional:
#   nA = 35 * (200 / 350) = 20
#   nB = 35 * (100 / 350) = 10
#   nC = 35 * (50 / 350)  = 5
#
# Dessa forma, cada estrato contribui para a amostra na mesma proporção
# que representa na população, garantindo representatividade e precisão.
# Exemplo em Python:

A = list(range(1, 201))
B = list(range(201, 301))
C = list(range(301, 351))

amostra_A = rd.sample(A, 20)
amostra_B = rd.sample(B, 10)
amostra_C = rd.sample(C, 5)

amostra_total = amostra_A + amostra_B + amostra_C

print('Amostragem Estratificada:', amostra_total)
print('Tamanho da amostra total:', len(amostra_total))

# ============================================================
# Amostragem por Conglomerados
# Nesse método, primeiro selecionam-se conglomerados (grupos maiores),
# e depois, dentro deles, escolhem-se as unidades para análise.
#
# Exemplo Numérico:
# Uma cidade possui 12 bairros.
# Selecionam-se 3 bairros para pesquisa.
# ============================================================
# Exemplo em Python:

bairros = [f" Bairro {i}" for i in range(1 ,13)]
selecionados = rd.sample(bairros ,3)
print (selecionados)

# ============================================================
# Amostragem Não Probabilística
#
# Amostragem a Esmo ou Sem Norma
# Seleciona-se quem estiver disponível.
# Baixa representatividade.
#
# Amostragem Intencional
# Selecionam-se unidades que atendem critérios específicos do pesquisador.
# ============================================================
# ============================================================
# Exemplo Comparativo: Python
#
# Nesta seção, apresentamos um código em Python que compara três
# técnicas de amostragem:
#   - Amostragem Casual Simples (ACS)
#   - Amostragem Sistemática
#   - Amostragem Estratificada
#
# Objetivo:
# Demonstrar como cada método seleciona elementos de uma população
# e como as médias amostrais se comparam à média populacional.
# ============================================================
# Código Completo:

np.random.seed(0)
pop = np.random.randint (1 , 101 , 100)

# ACS
amostra_acs = rd.sample(list(pop),10)

# Sistematic
k = len(pop) // 10
inicio = rd.randint (0 , k -1)
amostra_sist = pop [ inicio :: k ][:10]

# Estratificada
estrato1 = pop[:50]
estrato2 = pop[50:]

a1 =  rd.sample(list(estrato1),5)
a2 =  rd.sample(list(estrato2),5)
amostra_est = a1 + a2

print ("Media populacional :",np.mean(pop))
print ("ACS:", np.mean(amostra_acs))
print ("Sistematica :",np.mean(amostra_sist))
print ("Estratificada :",np.mean (amostra_est))

# ============================================================
# Explicação Passo-a-Passo
#
# Passo 1: Importação das Bibliotecas
# 1) import numpy as np
# 2) import random
# Importamos duas bibliotecas essenciais:
# - numpy: permite operações matemáticas avançadas e manipulação eficiente de arrays.
# - random: fornece funções para geração de números aleatórios e amostragem.
# ------------------------------------------------------------
#
# Passo 2: Definição da Semente Aleatória
# np.random.seed(0)
# A função seed(0) garante que os números aleatórios gerados sejam sempre os mesmos
# a cada execução do código. Isso é importante para reprodutibilidade dos resultados
# em pesquisas científicas e demonstrações didáticas.
# ------------------------------------------------------------
#
# Passo 3: Criação da População
#pop = np.random.randint(1, 101, 100)
# Criamos uma população artificial com 100 elementos, onde cada elemento é um número
# inteiro aleatório entre 1 e 100 (inclusive). Esta população simula, por exemplo,
# idades, notas, valores de vendas, etc.
# ------------------------------------------------------------
#
# Passo 4: Amostragem Casual Simples (ACS)
#amostra_acs = rd.sample(list(pop), 10)
# Neste passo:
# 1. Convertemos o array NumPy para lista usando list(pop).
# 2. Utilizamos random.sample() para selecionar 10 elementos aleatoriamente.
# 3. Cada elemento tem a mesma probabilidade de ser escolhido.
# 4. Não há repetição: cada elemento pode ser selecionado apenas uma vez.
# ------------------------------------------------------------
#
# Passo 5: Amostragem Sistemática
# k = len(pop) // 10
# inicio = rd.randint(0, k - 1)
# amostra_sist = pop[inicio::k][:10]
# Este método segue três etapas:
# 1. Cálculo do intervalo: k = N / n = 100 / 10 = 10. O operador // realiza divisão inteira.
# 2. Sorteio do ponto inicial: escolhemos aleatoriamente um número entre 0 e k − 1 (0 a 9).
# 3. Seleção sistemática: a partir do ponto inicial, selecionamos elementos a cada k posições
#    usando slicing pop[inicio::k]. O [:10] garante que teremos exatamente 10 elementos.
# Por exemplo, se inicio = 3, a amostra será: posições 3, 13, 23, 33, ..., 93.
# ============================================================
# ============================================================
# Passo 6: Amostragem Estratificada
# 1) estrato1 = pop[:50]
# 2) estrato2 = pop[50:]
# 3)
# 4) a1 = random.sample(list(estrato1), 5)
# 5) a2 = random.sample(list(estrato2), 5)
# 6) amostra_est = a1 + a2
# Este processo envolve:
# 1. Divisão em estratos:
#    - estrato1: primeiros 50 elementos da população.
#    - estrato2: últimos 50 elementos da população.
# 2. Amostragem proporcional: como cada estrato tem 50% da população,
#    selecionamos 5 elementos de cada (total de 10).
# 3. Combinação: as duas amostras parciais são concatenadas formando
#    a amostra estratificada completa com 10 elementos.
# ------------------------------------------------------------
#
# Passo 7: Cálculo e Exibição dos Resultados
# 1) print("Media populacional:", np.mean(pop))
# 2) print("ACS:", np.mean(amostra_acs))
# 3) print("Sistematica:", np.mean(amostra_sist))
# 4) print("Estratificada:", np.mean(amostra_est))
# Finalmente, calculamos e exibimos:
# - Média populacional (µ): valor verdadeiro que queremos estimar, calculado com np.mean(pop).
# - Médias amostrais (x̄): estimativas obtidas por cada método de amostragem.
# ------------------------------------------------------------
#
# Interpretação dos Resultados
# A comparação entre as médias amostrais e a média populacional permite avaliar:
# - Viés: quão próximas as estimativas estão do valor verdadeiro.
# - Eficiência: qual método produz estimativas mais estáveis.
# - Representatividade: se a amostra reflete adequadamente a população.
# É esperado que todas as médias amostrais estejam próximas da média populacional,
# embora pequenas diferenças sejam naturais devido ao erro amostral. Em média, com
# amostras suficientemente grandes, os três métodos produzem estimadores não viesados
# para a média populacional.
# ------------------------------------------------------------
#
# Conclusão
# A Teoria da Amostragem fornece fundamentos para a seleção adequada de amostras e
# aplicações estatísticas confiáveis. A integração com Python permite simular, visualizar e
# compreender profundamente cada técnica estudada.
# ============================================================



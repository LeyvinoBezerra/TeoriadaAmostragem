# ============================================================
# Projeto: Teoria da Amostragem
# Autor: Leyvino Bezerra do nascimento
# Data: 02/12/2025
# Descrição: Algoritmo da disciplina Estatistica com o conteudo do
# Professor Iranildo Guimaraes sobre Teoria da Amostragem em Python.
# ============================================================


# ------------------------------------------------------------
# 1: Introdução
# ------------------------------------------------------------

# A Teoria da Amostragem é o ramo da Estatística responsável pelo estudo de métodos para
# selecionar parte de uma população com o objetivo de obter informações sobre o todo. Em
# grande parte das situações práticas, observar toda a população é inviável devido a restrições
# de custo, tempo ou acessibilidade. Assim, torna-se necessário selecionar uma amostra
# bem planejada, que represente adequadamente a população.
# Uma amostra bem selecionada permite estimar parâmetros, construir intervalos de
# confiança, realizar testes de hipóteses e tomar decisões fundamentadas.


# ------------------------------------------------------------
# 2: Conceitos Básicos
# ------------------------------------------------------------
# ============================================================
# 2.1 População e Amostra
# População: conjunto de todos os elementos de interesse.
# Amostra: subconjunto da população selecionado conforme um método.
# ------------------------------------------------------------

# 2.2 Unidade Amostral
# Elemento indivisível da população: pessoa, empresa, máquina, produto, lote, viveiro, etc.
# ------------------------------------------------------------

# 2.3 Parâmetros e Estatísticas
# Parâmetro: característica desconhecida da população (µ, p, σ²).
# Estatística: medida calculada a partir da amostra (x̄, p̂, s²).
# ------------------------------------------------------------

# 2.4 Erro Amostral
# É a diferença entre o valor verdadeiro do parâmetro e sua estimativa amostral:
# E = θ − θ̂
# ------------------------------------------------------------

# 3 Amostragem Probabilística
# Na amostragem probabilística, cada unidade possui probabilidade conhecida e positiva de seleção.
# Isso permite realização de inferência estatística.
# ------------------------------------------------------------

# 3.1 Amostragem Casual Simples (ACS)
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
import matplotlib.pyplot as plt

populacao = list (range(1 , 11) )
amostra = rd.sample(populacao, 3)
print('Amostragem Casual Simples (ACS)')
print ("Amostra selecionada :", amostra)

# ============================================================
# 3.2 Amostragem Sistemática
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

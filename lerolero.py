
"""
Gerador de LEROLERO de frases aleatórias
"""
import random

# Cada frase é composa por três partes aleatórios; aqui,


parte1 = [
    "O sistema em desenvolvimento",
    "O novo protocolo de comunicação",
    "O algoritmo otimizado"
]
parte2 = [
    "Possui excelente desempenho",
    "oferece garantias de precisão acima da média",
    "preenche uma lacum significiativa"
]
parte3 = [
    "nas aplicações a que se destina",
    "em relações às opções disponíveis no mercado",
    ", provendo ampla vantagem competitiva a seus usuários"
]
lingua = int(input("Escolha a língua: 1 - português; 2 - inglês\n"))

if lingua == 2:
    parte1 = ["hi", "hello"]
    parte2 = ["apple", "yes"]
    parte3 = ["horse", "dial"]

# Combina as partes aleatoriamentes
#
print (random.choice(parte1), random.choice(parte2), random.choice(parte3))

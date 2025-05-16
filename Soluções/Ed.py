import os
os.system('cls' if os.name == 'nt' else 'clear')

#AULA 05/05/25
#1. Crie um dicionário chamado aluno com as chaves "nome", "idade" e "nota". 
#Atribua valores fictícios e imprima cada valor individualmente.
# aluno = {
#   "nome": "João", 
#   "idade": 20, 
#   "nota": 8.5
# }

# print(f"Nome: {aluno['nome']}" )
# print(f"Idade: {aluno["idade"]}")
# print(f"Nota: {aluno["nota"]}") 

# #2. Dado o dicionário abaixo:
# dados = {"nome": "Carlos", "idade": 30, "curso": "Python"}
# #Altere o valor da chave "idade" para 31 e adicione uma nova chave "email" com qualquer e-mail fictício.
# dados["idade"] = 31
# dados["email"] = "carlos30@email.com"
# print(dados)

# #3. Escreva um código que pergunte ao usuário o nome de um produto e seu preço. 
# # Guarde essas informações em um dicionário e exiba-o no final.
# produto = {}
# produto["nome"] = input("Digite o nome do produto: ")
# produto["preço"] = float(input("Digite o preço do produto: "))
# print(produto)

#AULA 07/05/2025

# 4.Dado o dicionário:
# Escreva um código que:
# - Peça ao usuário o nome de uma fruta.
# - Verifique se a fruta está no dicionário.
# - Se estiver, mostre quantas unidades têm.
# Caso contrário, diga que a fruta não está disponível.

# frutas = {"maçã": 3, "banana": 5, "laranja": 2}

# fruta = input("Digite o nome de uma fruta: ")

# if fruta in frutas :
#   print(f'{fruta}: {frutas[fruta]} unidades')
# else :
#   print('A fruta não está disponível.')

# 5. Crie um dicionário chamado notas_alunos, onde a chave é o nome do aluno e o valor é a média final.
#  Depois, mostre apenas os alunos com média maior ou igual a 7.

# notas_alunos = {'João':  2.0, 'Lucas': 5.0, 'Pedro': 8.0, 'Fátima': 9.0, 'Joana': 10}

# for aluno in notas_alunos :
#   if notas_alunos[aluno] >= 7 :
#     print(f'Aluno: {aluno} - Nota: {notas_alunos[aluno]}')

# aprovados = {nota: nome for nome, nota in notas_alunos.items() if nota >= 7}
# print(aprovados)

# 09/05/2025
# 06. Quadrados de Números - Enunciado: Crie uma lista com os quadrados dos números de 0 a 9.
# quadradros_coprensao = [n**2 for n in range(0, 10)]
# print(quadradros_coprensao)

# 07. Filtrar Números Pares
# Enunciado: A partir da lista nums = list(range(20)), crie uma nova lista apenas com os números pares.
# nums = list(range(20))
# pares = [n for n in nums if n % 2 == 0]
# print(pares)

#  Converter para Letras Maiúsculas
# Enunciado: Dada a lista palavras = ["python", "é", "legal"], crie uma nova lista com todas as palavras em maiúsculas.
# palavras = ["globo", "é", "legal"]
# maiusculas = [palavra.upper() for palavra in palavras]
# print(maiusculas)

# nums = list(range(20))
# pares = [n if n % 2 == 0 else 0 for n in nums]
# print(pares)

# nomes = ["Pedro", "Lucas", "Tiago", "Fátima"]
# sobrenomes = ["Silva", "Souza", "Oliveira", "Pereira"]

# lista_completa = [nome + ' ' + sobrenome for nome in nomes for sobrenome in sobrenomes]

# for nome in lista_completa:
#   print(nome)

# times = ['Atlético Python', 'JavaScript United', 'C Seniors', 'Javeiros do Norte']
# entradas = ['V', 'E', 'D']

# tabela = [[int(input(f'Digite a quantidade de {tipo} do time {time}: ')) for tipo in entradas] for time in times]

# print(tabela)

# 08. Você faz parte do time de dados da Globo, e está recebendo uma 
# lista com os nomes dos programas e suas respectivas audiências em 
# pontos de ibope, de uma semana.
# Seu objetivo é gerar um dicionário onde:

# A chave seja o nome do programa.
# O valor seja uma classificação textual baseada na audiência:
# 'Alta' se audiência ≥ 25
# 'Média' se audiência entre 15 e 24
# 'Baixa' se audiência < 15

# audiencias = [
#     ("Jornal Nacional", 30),
#     ("Big Brother Brasil", 28),
#     ("Altas Horas", 18),
#     ("Sessão da Tarde", 12),
#     ("É de Casa", 14),
#     ("Fantástico", 26)
# ]

# classificacoes_1 = { 
#   chave[0]: classificacao  
#   for chave in audiencias
#   if (
#     classificacao := 'Alta' if chave[1] >= 25 
#     else 'Média' if 15 <= chave[1] < 25 
#     else 'Baixa'
#   )
# } 
# for programa, classificacao in classificacoes_1.items():
#     print(f"{programa}: {classificacao}")

# print(f"\n{'---'*10}\n")

# classificacoes_2 = { 
#     programa: (
#         'Alta' if audiencia >= 25 
#         else 'Média' if 15 <= audiencia < 25 
#         else 'Baixa'
#     )
#     for programa, audiencia in audiencias
# }

#12/05/2025
# for programa, classificacao in classificacoes_2.items():
#     print(f"{programa}: {classificacao}")

# Você trabalha com análise de audiência na Rede Globo e precisa retornar
# os valores máximo e mínimo de uma lista de índices de audiência.

# Implemente a função audiencia_extremos() e atribua os 
# valores máximo e mínimo às variáveis maximo e minimo via desempacotamento. 
# Imprima os dois valores, um por linha.

# lista_audiencia = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# def audiencia_extremos(lista):
#   return max(lista), min(lista)

# maximo, minimo = audiencia_extremos(lista_audiencia)

# print(f'Máximo: {maximo}')
# print(f'Mínimo: {minimo}')

# Padronização de nomes de arquivos do jornalismo com valor padrão upper=False. 
# Implemente padroniza_titulo() e teste.

# lista_titulos = [
#   "Jornal Nacional",
#   "Fantástico",
#   "Altas Horas",
#   "Sessão da Tarde",
#   "É de Casa"
# ]

# def padroniza_titulo(lista, type='title'):
#   return [
#     titulo.upper() if type == 'upper' else 
#     titulo.lower() if type == 'lower' else
#     titulo.title()
#     for titulo in lista
#   ]

# print(padroniza_titulo(lista_titulos))
# print(padroniza_titulo(lista_titulos, 'upper'))
# print(padroniza_titulo(lista_titulos, 'lower'))

# print("jornal nacional".title())

# Você trabalha com um sistema interno da Globo Educação. Precisa criar uma função que receba o nome de um aluno e retorne suas informações formatadas (curso, média e status).
# Dicionário com dados de 4 alunos
# alunos = {
#     'Ana Clara': {'curso': 'Jornalismo', 'media': 8.5, 'status': 'Aprovada'},
#     'Bruno Silva': {'curso': 'Engenharia de Dados', 'media': 6.8, 'status': 'Aprovado'},
#     'Carlos Lima': {'curso': 'Publicidade', 'media': 4.2, 'status': 'Reprovado'},
#     'Débora Souza': {'curso': 'Design Gráfico', 'media': 9.3, 'status': 'Aprovada'}
# }

# def exibe_dados_aluno(nome):
#     aluno = alunos.get(nome)
#     if aluno:
#         print(f"Nome: {nome}")
#         print(f"Curso: {aluno['curso']}")
#         print(f"Média: {aluno['media']}")
#         print(f"Status: {aluno['status']}")
#     else:
#         print("Aluno não encontrado.")

# entrada = input("Digite o nome do aluno (ou 'sair' para encerrar): ")

# while entrada.lower() != "sair":
#   exibe_dados_aluno(entrada)
#   entrada = input("Digite o nome do aluno (ou 'sair' para encerrar): ")

# 14/05/2025

# Faça uma calculadora que você digite os valores e o operador (soma, subtração e etc) e ele ira fazer a operação aritmetica.
# def calculadora(num1, num2, operador):
#     if operador == '+':
#         return num1 + num2
#     elif operador == '-':
#         return num1 - num2
#     elif operador == '*':
#         return num1 * num2
#     elif operador == '/':
#         return num1 / num2
#     else:
#         return "Operador inválido"

# resultado = calculadora(calculadora(10, 5, '+') , calculadora(10, 5, '-') , '*')

# print(f"Resultado: {resultado}")

# 3 Você recebeu uma lista com a duração (em minutos) de cada programa da Globo em um dia. 
# Escreva uma função chamada `filtrar_programas_longo` que receba a lista e retorne outra lista apenas com os programas que duram **mais de 60 minutos**.
# Use compreensão de listas.

# duracoes = [45, 90, 30, 120, 60]

# def filtrar_programas_longo(duracoes : list, limite=60 ) -> list:
#     return [duracao for duracao in duracoes if duracao > limite]

# print(filtrar_programas_longo(duracoes, 40))
# print(filtrar_programas_longo(duracoes))


# 5 Crie uma função chamada `gerar_episodios` que receba dois parâmetros: o nome de uma série da Globo (ex: "Sob Pressão") e o número de episódios. 
# A função deve retornar uma lista com os nomes dos episódios, numerados.
# Deve retornar: ['Sob Pressão - Episódio 1', 'Sob Pressão - Episódio 2', 'Sob Pressão - Episódio 3']
# Use **laço `for`.

# def gerar_episodios(nome_serie, num_episodios):
#     episodios = []
#     for i in range(1, num_episodios + 1):
#         episodios.append(f"{nome_serie} - Episódio {i}")
#     return episodios

# def imprime_episodios(lista : list):
#     for episodio in lista:
#         print(episodio)

# imprime_episodios(gerar_episodios("Sob Pressão", 10))
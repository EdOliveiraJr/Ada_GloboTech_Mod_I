
#05/05/25
#1. Crie um dicionário chamado aluno com as chaves "nome", "idade" e "nota". 
#Atribua valores fictícios e imprima cada valor individualmente.
# aluno = {
#   "nome": "Joao", 
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
# produto["preco"] = float(input("Digite o preço do produto: "))
# print(produto)

# 4.Dado o dicionário:
# Escreva um código que:
# - Peça ao usuário o nome de uma fruta.
# - Verifique se a fruta está no dicionário.
# - Se estiver, mostre quantas unidades têm.
# Caso contrário, diga que a fruta não está disponível.

# frutas = {"maçã": 3, "banana": 5, "laranja": 2}

# fruta = input("Dgite o nome de uma fruta: ")

# if fruta in frutas :
#   print(f'{fruta}: {frutas[fruta]} unidades')
# else :
#   print('A fruta não está disponível.')

# 5. Crie um dicionário chamado notas_alunos, onde a chave é o nome do aluno e o valor é a média final.
#  Depois, mostre apenas os alunos com média maior ou igual a 7.

# notas_alunos = {'Joao':  2.0, 'Lucas': 5.0, 'Pedro': 8.0, 'Fátima': 9.0, 'Joana': 10}

for aluno in notas_alunos :
  if notas_alunos[aluno] >= 7 :
    print(f'Aluno: {aluno} - Nota: {notas_alunos[aluno]}')

aprovados = {nota: nome for nome, nota in notas_alunos.items() if nota >= 7}
print(aprovados)
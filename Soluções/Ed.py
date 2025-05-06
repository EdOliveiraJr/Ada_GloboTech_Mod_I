
#05/05/25
#1. Crie um dicionário chamado aluno com as chaves "nome", "idade" e "nota". 
#Atribua valores fictícios e imprima cada valor individualmente.
aluno = {
  "nome": "Joao", 
  "idade": 20, 
  "nota": 8.5
}

print(f"Nome: {aluno['nome']}" )
print(f"Idade: {aluno["idade"]}")
print(f"Nota: {aluno["nota"]}") 

#2. Dado o dicionário abaixo:
dados = {"nome": "Carlos", "idade": 30, "curso": "Python"}
#Altere o valor da chave "idade" para 31 e adicione uma nova chave "email" com qualquer e-mail fictício.
dados["idade"] = 31
dados["email"] = "carlos30@email.com"
print(dados)

#3. Escreva um código que pergunte ao usuário o nome de um produto e seu preço. 
# Guarde essas informações em um dicionário e exiba-o no final.
produto = {}
produto["nome"] = input("Digite o nome do produto: ")
produto["preco"] = float(input("Digite o preço do produto: "))
print(produto)
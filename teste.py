# Uma classe define o estado e o comportamento de um objeto implementando atributos e métodos. 
# Os atributos (por vezes referidos como "campos", "membros de dados" ou "propriedades")

class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura



# Criando instâncias da classe Pessoa
pessoa1 = Pessoa("Alice", 25, 1.65)
pessoa2 = Pessoa("Bob", 30, 1.80)
pessoa3 = Pessoa("Vitor", 30, 1.80)

# Acessando os atributosS
# print(pessoa1.nome)    # Saída: Alice
# print(pessoa2.altura)  # Saída: 1.8

resposta = input("Escreva seu nome:") 

if resposta == 'Alice'.lower():
  print(pessoa1.nome, pessoa1.idade, pessoa1.altura)  
elif resposta == 'Vitor'.lower():
  print(pessoa3.nome, pessoa3.idade, pessoa3.altura)   
else:
  print(pessoa2.nome, pessoa2.idade, pessoa2.altura)  



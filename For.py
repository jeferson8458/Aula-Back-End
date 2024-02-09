
# for: Indica o início de um loop. Em português, você poderia interpretar isso como "para cada".

# elemento: Este é um nome de variável temporária que representa cada item individual da lista a cada iteração do loop. 
# Você pode escolher qualquer nome válido para essa variável.

# In:  Indica a relação entre a variável temporária (elemento) e a lista que estamos percorrendo. Em português, você poderia interpretar isso como "dentro".

# Lista:  Este é o objeto iterável sobre o qual estamos iterando. Pode ser uma lista, tupla, string, dicionário, etc.
# Em cada iteração do loop, a variável elemento assume o valor do próximo item na lista.




# Neste exemplo, o loop percorre a lista de números de 1 a 5. A cada iteração, a variável elemento assume o valor do próximo número na lista, 
# e o bloco de código dentro do loop (no caso, print(elemento)) é executado.

# Esse é um conceito fundamental em programação e é muito útil para realizar tarefas repetitivas de maneira eficiente.


# Tupla:
#Uma tupla em Python é uma estrutura de dados semelhante a uma lista, mas com uma diferença crucial: as tuplas são imutáveis, 
# o que significa que, uma vez que você cria uma tupla, não pode alterar seu conteúdo - adicionar, remover ou modificar elementos. 
# As tuplas são representadas por parênteses ().

#Sintaxe:
# minha_tupla = (1, 2, 3, 'abc')

lista = [1,2,3,4,5]

for elemento in lista:
  print(elemento)
  
  

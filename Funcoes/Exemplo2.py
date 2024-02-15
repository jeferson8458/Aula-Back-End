def calcular_peso_comida():
    # Solicitar ao usuário que insira os pesos dos alimentos
    peso_carne = float(input("Digite o peso da carne (em gramas): "))
    peso_legumes = float(input("Digite o peso dos legumes (em gramas): "))
    peso_arroz = float(input("Digite o peso do arroz (em gramas): "))

    # Calcular o peso total da comida
    peso_total = peso_carne + peso_legumes + peso_arroz

    # Exibir o resultado
    print(f"O peso total da comida é: {peso_total} gramas")

# Chamar a função
calcular_peso_comida()


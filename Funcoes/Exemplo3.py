def calcular_calorias(tempo, intensidade):
    # Suponhamos que a queima de calorias seja 5 por minuto, e intensidade seja um multiplicador.
    calorias_por_minuto = 5
    calorias_totais = tempo * calorias_por_minuto * intensidade

    return calorias_totais

# Exemplo de uso
tempo_atividade = 30  # em minutos
intensidade_atividade = 1.5  # fator de intensidade

calorias_gastas = calcular_calorias(tempo_atividade, intensidade_atividade)
print(f"Você queimou {calorias_gastas} calorias durante a atividade.")
def switch_case(case):
    switch_dict = {
        'case1': 'Esta é a execução do Case 1',
        'case2': 'Esta é a execução do Case 2',
        'case3': 'Esta é a execução do Case 3',
        'default': 'Esta é a execução do Default'
    }

    return switch_dict.get(case, switch_dict['default'])

# Exemplos de uso
resultado_case1 = switch_case('case1')
resultado_case2 = switch_case('case2')
resultado_case4 = switch_case('case4')  # Este é o caso padrão (default)

print(resultado_case1)
print(resultado_case2)
print(resultado_case4)

# Neste exemplo, a função switch_case recebe um argumento chamado case e usa um dicionário 
# para mapear valores de caso para suas respectivas ações. 
# Se o valor de case não estiver no dicionário, ele retornará a ação padrão.

# Lembre-se de que, em muitos casos em Python, é mais comum usar instruções if, elif, 
# else para lidar com várias condições. 
# O uso do dicionário é apenas uma maneira de simular um comportamento semelhante ao switch em linguagens que o suportam nativamente.
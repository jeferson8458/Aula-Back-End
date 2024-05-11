import random

def escolher_palavra():
    palavras = ['python', 'programacao', 'desenvolvimento', 'computador', 'algoritmo', 'openai', 'inteligencia']
    return random.choice(palavras)

def jogar_forca():
    palavra = escolher_palavra()
    letras_corretas = []
    letras_erradas = []
    tentativas = 6

    while True:
        palavra_escondida = ''.join([letra if letra in letras_corretas else '_' for letra in palavra])
        print("\nPalavra: ", palavra_escondida)
        print("Letras Erradas: ", ', '.join(letras_erradas))
        print("Tentativas Restantes:", tentativas)
        
        if palavra_escondida == palavra:
            print("\nParabéns! Você venceu!")
            break
        
        if tentativas == 0:
            print("\nGame Over! A palavra era:", palavra)
            break
        
        letra = input("\nDigite uma letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue
        
        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou esta letra. Tente outra.")
            continue
        
        if letra in palavra:
            print("Letra correta!")
            letras_corretas.append(letra)
        else:
            print("Letra errada!")
            letras_erradas.append(letra)
            tentativas -= 1

if __name__ == "__main__":
    print("Bem-vindo ao Jogo da Forca!")
    jogar_forca()

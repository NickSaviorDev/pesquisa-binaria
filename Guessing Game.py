# Programa de adivinhação de um número inteiro conforme level escolhido pelo jogador
import random


def main():  # Define função principal
    level = get_level()  # Obtém level válido
    answer = generate_integer(level)  # Gera número inteiro aleatório conforme level escolhido
    while True:  # Gera loop infinito que só irá parar quando jogador acertar o número
        guess = get_guess()  # Obtém palpite válido
        if guess == answer:  # Em caso de acerto, interrompe loop e finaliza o programa
            print('Just right!')
            break
        elif guess > answer:  # Se palpite acima do número certo, informa o jogador
            print('Too large!')
        else:  # Se palpite abaixo do número certo, informa o jogador
            print('Too small!')


def get_level():  # Função criada para obter level válido (número inteiro positivo)
    while True:
        try:
            level = int(input('Level: '))
            if level > 0:
                return level  # Quebra loop infinito e retorna level válido
        except ValueError:
            pass


def generate_integer(level):  # Função criada para gerar um número inteiro aleatório (de 1 ao level escolhido)
    integer = random.randint(1, level)
    return integer


def get_guess():  # Função criada para validar o palpite do jogador (número inteiro positivo)
    while True:
        try:
            guess = int(input('Guess: '))
            if guess > 0:
                return guess
        except ValueError:
            pass


if __name__ == '__main__':  # Comando condicional para rodar a função principal do programa
    main()

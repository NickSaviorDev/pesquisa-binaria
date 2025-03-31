# Função pesquisa binária:
# -> Recebe lista ordenada e item
# -> Retorna índice do item na lista
def pesquisa_binaria(lista, item):
    # Limites superiores e inferiores (índices)
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:  # Enquanto houver elementos a serem verificados...
        meio = (alto + baixo) // 2  # Calcula-se o índice do elemento central da lista
        chute = lista[meio]
        if chute == item:  # Se encontrou o item, retorna o índice
            return meio
        if chute > item:  # Chute alto, descarta-se a metade superior
            alto = meio - 1
        else:  # Chute baixo, descarta-se a metade inferior
            baixo = meio + 1
    return None  # Caso item não esteja na lista, retorna None


def main():
    minha_lista = [1, 2, 3, 7, 10, 13, 30, 33, 40, 50]
    print(pesquisa_binaria(minha_lista, 10))


if __name__ == "__main__":
    main()

import main


def alterarproduto():
    codigo_produto = int(input("Código: "))
    if codigo_produto in main.estoque:
        print("Descrição: ", main.estoque[1], "Quantidade: ", main.estoque[2])
    else:
        print("\033[31mProduto não cadastrado.\033[m")

import main


def alterarproduto():
    codigoproduto = int(input("Código: "))
    if codigoproduto in main.codproduto:
        print("Descrição: ", main.descproduto, "Quantidade: ", main.qtdeproduto)
        main.descproduto[main.codproduto.index(codigoproduto)] = input("Nova descrição: ").upper()
        main.qtdeproduto[main.codproduto.index(codigoproduto)] = int(input("Nova quantidade: "))
        print("Descrição alterada para: ", main.descproduto, "Quantidade alterada para: ", main.qtdeproduto)
    else:
        print("\033[31mProduto não cadastrado.\033[m")

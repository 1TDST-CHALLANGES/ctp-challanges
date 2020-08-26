import main


def cadastrarprodutos():
    codigoproduto = int(input("Código: "))
    if codigoproduto in main.codproduto:
        print("\033[31mCódigo já cadastrado\033[m")
    else:
        main.produtos.append([main.codproduto, main.descproduto, main.qtdeproduto])
        main.codproduto.append(codigoproduto)
        main.descproduto[main.codproduto.index(codigoproduto)] = input("Descrição: ").upper()
        main.qtdeproduto[main.codproduto.index(codigoproduto)] = int(input("Quantidade: "))

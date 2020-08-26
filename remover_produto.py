import main


def removerproduto():
    codigoproduto = int(input("Código: "))
    if codigoproduto in main.codproduto:
        print("Descrição: ", main.descproduto, "Quantidade: ", main.qtdeproduto)
        opcao = input("Deseja excluir o produto? [S] ou [N]").upper()
        if opcao == "s".upper():
            main.codproduto.pop(main.codproduto.index(codigoproduto))
            main.descproduto.pop(main.codproduto.index(codigoproduto))
            main.qtdeproduto.pop(main.codproduto.index(codigoproduto))
            print("\033[32mPRODUTO EXCLUIDO COM SUCESSO\033[m")
        elif opcao == "n".upper():
            print("\033[31mPRODUTO NÃO EXCLUÍDO\033[m")
        else:
            print("\033[31mOPÇÃO INVÁLIDA\033[m")
    else:
        print("\033[31mPRODUTO NÃO CADASTRADO\033[m")

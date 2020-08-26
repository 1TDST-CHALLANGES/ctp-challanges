import main


def removerproduto():
    codigoproduto = int(input("Código: "))
    if codigoproduto in menuXPTO.codproduto:
        print("Descrição: ", menuXPTO.descproduto, "Quantidade: ", menuXPTO.qtdeproduto)
        opcao = input("Deseja excluir o produto? [S] ou [N]").upper()
        if opcao == "s".upper():
            menuXPTO.codproduto.pop(menuXPTO.codproduto.index(codigoproduto))
            menuXPTO.descproduto.pop(menuXPTO.codproduto.index(codigoproduto))
            menuXPTO.qtdeproduto.pop(menuXPTO.codproduto.index(codigoproduto))
            print("\033[32mPRODUTO EXCLUIDO COM SUCESSO\033[m")
        elif opcao == "n".upper():
            print("\033[31mPRODUTO NÃO EXCLUÍDO\033[m")
        else:
            print("\033[31mOPÇÃO INVÁLIDA\033[m")
    else:
        print("\033[31mPRODUTO NÃO CADASTRADO\033[m")

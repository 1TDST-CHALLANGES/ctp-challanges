import main


def removerproduto():
    codigo_produto = int(input("Código: "))
    if codigo_produto in main.cod_produto:
        print("Descrição: ", main.desc_produto, "Quantidade: ", main.qtdeproduto)
        opcao = input("Deseja excluir o produto? [S] ou [N]").upper()
        if opcao == "s".upper():
            main.cod_produto.pop(main.cod_produto.index(codigo_produto))
            main.desc_produto.pop(main.cod_produto.index(codigo_produto))
            main.qtdeproduto.pop(main.cod_produto.index(codigo_produto))
            print("\033[32mPRODUTO EXCLUIDO COM SUCESSO\033[m")
        elif opcao == "n".upper():
            print("\033[31mPRODUTO NÃO EXCLUÍDO\033[m")
        else:
            print("\033[31mOPÇÃO INVÁLIDA\033[m")
    else:
        print("\033[31mPRODUTO NÃO CADASTRADO\033[m")

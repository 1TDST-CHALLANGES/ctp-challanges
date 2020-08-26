import main


def cadastrarprodutos():
    codigo_produto = int(input("Código: "))
    if codigo_produto in main.cod_produto:
        print("\033[31mCódigo já cadastrado\033[m")
    else:
        main.produtos.append([main.cod_produto, main.desc_produto, main.qtd_produto])
        main.cod_produto.append(codigo_produto)
        main.desc_produto[main.cod_produto.index(codigo_produto)] = input("Descrição: ").upper()
        main.qtd_produto[main.cod_produto.index(codigo_produto)] = int(input("Quantidade: "))

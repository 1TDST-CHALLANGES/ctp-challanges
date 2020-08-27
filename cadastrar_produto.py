import main


def cadastrar_produtos():
    desc_produto = input("Descrição: ").upper()
    qtd_produto = int(input("Quantidade: "))
    main.estoque.append([desc_produto, qtd_produto])


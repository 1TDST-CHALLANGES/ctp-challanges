import main

def cadastrarprodutos():
    cod_produto = int(input("Código: "))
    if cod_produto in main.estoque[0]:
        print("\033[31mCódigo já cadastrado\033[m")
    else:
        desc_produto = input("Descrição: ").upper()
        qtd_produto = int(input("Quantidade: "))
        main.estoque.append([cod_produto, desc_produto, qtd_produto])
        

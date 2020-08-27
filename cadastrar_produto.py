import main

def cadastrar_produtos():

    if len(main.estoque) == 0:
        cod_produto = input("Código: ")
    else:
        cod_produto = input("Código: ")
        if cod_produto in main.estoque[0]:
            print("\033[31mCódigo já cadastrado\033[m")

    desc_produto = input("Descrição: ").upper()
    qtd_produto = int(input("Quantidade: "))
    main.estoque.append([cod_produto, desc_produto, qtd_produto])
        

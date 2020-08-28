import main
import validar_codigo
def cadastrar_produtos():

    desc_produto = input("Descrição: ").upper()
    qtd_produto = int(input("Quantidade: "))
    main.estoque.append([main.cod_produto, desc_produto, qtd_produto])
        

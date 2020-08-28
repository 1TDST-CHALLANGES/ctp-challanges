import main


def comprar():
    cod_produto = int(input("Código do produto: "))
    for alterar in main.estoque:
        if alterar[0] == cod_produto:
            for produto in main.estoque:
                print("\nCÓDIGO\tDESCRIÇÃO\tQUANTIDADE EM ESTOQUE:")
                print(6 * '-', '', 9 * '-', ' ', 22 * '-')
                print(str(produto[0]) + '\t' + str(produto[1]) + '\t\t' + str(produto[2]))
            quant_prod = int(input("Quantos deseja comprar: "))
            quant_prod_final = quant_prod + main.qtd_produto
            quant_prod_final.append(main.qtd_produto)
        else:
            print("\033[31mProduto não cadastrado\033[m")

import main


def listarprodutos():
    for produto in main.estoque:
        print("CÓDIGO\tDESCRIÇÃO\tQUANTIDADE EM ESTOQUE:")
        print(6 * '-', '', 9 * '-', ' ', 22 * '-')
        print(str(produto[0]) + '\t' + str(produto[1]) + '\t\t' + str(produto[2]))
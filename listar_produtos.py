import main


def listarprodutos():
    for produto in main.estoque:
        print("CÓDIGO\tDESCRIÇÃO\tQUANTIDADE EM ESTOQUE:")
        print(6 * '-', '', 9 * '-', ' ', 22 * '-')
        print(f" {produto[0]}  {produto[1].ljust(20)} {produto[2]}")
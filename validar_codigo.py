import main

def validar_produto():
    if main.cod_produto in main.estoque[0]:
        print("\033[31mCódigo já cadastrado\033[m")

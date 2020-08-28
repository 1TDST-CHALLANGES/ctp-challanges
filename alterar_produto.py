import main
import listar_produtos

def alterar_produto():
    codigo = input("Código: ")
    for produto in main.estoque:
        if codigo in produto[0]:
            if produto[0] == codigo:
                print("Descrição: ", f"{produto[1]}", "\nQuantidade: ", f"{produto[2]}")
                novo_desc = input("Digite a nova descrição: ").upper()
                novo_quant = int(input("Digite a nova quantia: "))
                produto[1] = novo_desc
                produto[2] = novo_quant
                print("\nAlteração finalizada!")
        else:
            print("\033[31mProduto não cadastrado.\033[m")
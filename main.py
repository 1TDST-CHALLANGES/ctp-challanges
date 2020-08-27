import alterar_produto
import cadastrar_produto
import remover_produto
import listar_produtos

opcao = 0

cod_produto = []
desc_produto = []
qtd_produto = []
estoque = []


while opcao != 7:
    print('\nMenu')
    opcao = int(input(
        "\t1. Cadastrar Produto\n\t2. Alterar Produto\n\t3. Excluir Produto\n\t4. Listar Estoque de Peça\n\t5. "
        "Comprar Produto\n\t6. Vender Produto\n\t7. Sair\n\nDigite a opção desejada: "))
    if opcao == 1:
        cod_produto = int(input("Digite um codigo(validao)? "))
        if len(estoque) == 0:
            cadastrar_produto.cadastrar_produtos()
        elif cod_produto in estoque[0]:
            print("\033[31mCódigo já cadastrado\033[m")



    elif opcao == 2:
        cont = 3
        senha = input("Digite sua senha: ")
        while senha != "yN1825*a" and cont > 1:
            print("\033[31mSenha incorreta, você têm mais ", cont - 1, " tentativas.\033[m")
            senha = input("Digite novamente.")
            cont = cont - 1
        if senha == "yN1825*a":
            print("\033[31mAcesso permitido!\033[m")
            alterar_produto.alterarproduto()
        else:
            print("\033[31mSenha bloqueada! Procure o setor responsável.\033[m")

    elif opcao == 3:
        cont = 3
        senha = int(input("Digite sua senha: "))
        while senha != "yN1825*a" and cont > 1:
            print("\033[31mSenha incorreta, você têm mais ", cont - 1, " tentativas.\033[m")
            senha = int(input("Digite novamente."))
            cont = cont - 1
        if senha == "yN1825*a":

            print("\033[32mACESSO PERMITIDO\033[m")

            print("\033[31mAcesso permitido!\033[m")

            remover_produto.removerproduto()
        else:
            print("\033[31mSenha bloqueada! Procure o setor responsável.\033[m")

    elif opcao == 4:
        listar_produtos.listarprodutos()

    elif opcao == 5:
        print("Comprar produto")

    elif opcao == 6:
        print("Vender produto")

    elif opcao == 7:
        print("Saindo...")
        break

    else:
        print("\033[31mOpção inválida!\033[m")
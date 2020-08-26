import alterar_produto
import cadastrar_produto
import remover_produto

opcao = 0

cod_produto = []
desc_produto = []
qtd_produto = []
produtos = (cod_produto, desc_produto, qtd_produto)

while opcao != 7:
    print('\nMenu')
    opcao = int(input(
        "\t1. Cadastrar Produto\n\t2. Alterar Produto\n\t3. Excluir Produto\n\t4. Listar Estoque de Peça\n\t5. "
        "Comprar Produto\n\t6. Vender Produto\n\t7. Sair\n\tDigite a opção desejada: "))
    if opcao == 1:
        cadastrar_produto.cadastrar_produtos()

    elif opcao == 2:
        senha = input("Digite sua Senha: ")
        if senha == "yN1825*a":
            print("\033[32mAcesso permitido.\033[m")
            alterar_produto.alterar_produto()
        else:
            print("\033[31mSENHA INCORRETA\033[m")

    elif opcao == 3:
        senha = input("Digite sua Senha: ")
        if senha == "yN1825*a":
            print("\033[32mACESSO PERMITIDO\033[m")
            remover_produto.removerproduto()
        else:
            print("\033[31mSENHA INCORRETA\033[m")

    elif opcao == 4:
        print(sorted(produtos))

    elif opcao == 5:
        print("Comprar produto")

    elif opcao == 6:
        print("Vender produto")

    elif opcao == 7:
        print("Saindo...")
        break

    else:
        print("\033[31mOpção inválida!\033[m")
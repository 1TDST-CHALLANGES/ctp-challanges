import main

def cadastrarprodutos():
    codigo_produto = int(input("Código: "))
    if codigo_produto in main.cod_produto:
        print("\033[31mCódigo já cadastrado\033[m")
    else:
        descricao_produto = input("Descrição: ").upper()
        quantidade_produto = int(input("Quantidade: "))
        main.cod_produto.append(codigo_produto)
        main.desc_produto.append(descricao_produto)
        main.qtd_produto.append(quantidade_produto)
        main.estoque.append({codigo_produto,descricao_produto,quantidade_produto})
10
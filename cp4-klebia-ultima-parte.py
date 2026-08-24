produtos = []

def cadastrar_produto(id_produto, nome, preco, quantidade, categoria):
    novo_produto = {
        "id": id_produto,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
        "categoria": categoria
                    }
    produtos.append(novo_produto)
    print("\nProduto cadastrado com sucesso!")

def exibir_produto(produto):
    print("ID: ", produto["id"])
    print("Nome:", produto["nome"])
    print("Preço: R$", produto["preco"])
    print("Quantidade:", produto["quantidade"])
    print("Categoria:", produto["categoria"])

def remover_produto(produto):
    produtos.remove(produto)
    print("Produto removido.")


opcao = 0
while opcao != 6:
    print("\n========================================") 
    print("          CRUD DE PRODUTOS") 
    print("========================================") 
 
    print("1 - Cadastrar produto") 
    print("2 - Listar produtos") 
    print("3 - Buscar produto") 
    print("4 - Atualizar produto") 
    print("5 - Excluir produto") 
    print("6 - Sair") 
    print("========================================")
    try:
        opcao = int(input("Digite uma opção: "))
    except ValueError:
        print("Digite apenas números.")
        continue

    match opcao:
        case 1:
            print("\n========== CADASTRO ==========") 
            try:
                nome = input("Insira o nome do produto: ").strip()
                if nome == "":
                    raise ValueError("O nome não pode ser vazio.")

                id_produto = int(input("Digite o ID do produto: "))
                for produto in produtos:
                    if id_produto == produto["id"]:
                        raise ValueError("O ID de um produto não pode se repetir.")
                if id_produto <= 0:
                    raise ValueError("O ID precisa ser um número inteiro maior que 0.")

                preco = float(input("Insira o preço do produto: "))
                if preco <= 0:
                    raise ValueError("O preço deve ser maior que 0.")
                quantidade = int(input("Insira a quantidade disponível do produto: "))
                if quantidade < 0:
                    raise ValueError("A quantidade não pode ser negativa.")
                categoria = input("Insira a categoria do produto: ").strip()
                if categoria == "":
                    raise ValueError("A categoria não pode ser vazia.")
                cadastrar_produto(id_produto, nome, preco, quantidade, categoria)

            except ValueError as erro:
                print("Erro:", erro)

        case 2:
            print("\n========== PRODUTOS ==========")
            if len(produtos) == 0:
                print("Não há produtos cadastrados.")
            else:
                for produto in produtos:
                    print("\n===================")
                    exibir_produto(produto)
        case 3:
            try:
                id_busca = int(input("Digite o ID do produto: "))
                encontrado = False
                for produto in produtos:
                    if id_busca == produto["id"]:
                        print("Produto encontrado!")
                        exibir_produto(produto)
                        encontrado = True
                        break

                if not encontrado:
                    print("Produto não encontrado.")

            except ValueError:
                print("Digite o ID do produto.")

        case 4:
            try:
                id_alteracao = int(input("Digite o ID do produto que será alterado: "))
                encontrado = False
                for produto in produtos:
                    if id_alteracao == produto["id"]:
                        encontrado = True 
                        opcao_alteracao = 0
                        while opcao_alteracao != 5:
                            print("\n============ Menu de Alterações ============")
                            print("1 - Nome.")
                            print("2 - Categoria.")
                            print("3 - Preço.")
                            print("4 - Quantidade em estoque.")
                            print("5 - Voltar.")
                            try:
                                opcao_alteracao = int(input("Digite o número do atributo que você deseja alterar: "))
                            except ValueError:
                                print("Digite uma opção válida.")
                                continue
                            match opcao_alteracao:
                                case 1:
                                    try: 
                                        novo_nome = input("Digite o novo nome do produto: ").strip()
                                        if novo_nome == "":
                                            raise ValueError("O nome não pode ser vazio.")
                                        else:
                                            produto["nome"] = novo_nome
                                            print("Nome alterado com sucesso!")

                                    except ValueError as erro:
                                        print("Erro:", erro)

                                case 2:
                                    try:
                                        nova_categoria = input("Digite a nova categoria do produto: ").strip()
                                        if nova_categoria == "":
                                            raise ValueError("A categoria não pode ser vazia.")
                                        else:
                                            produto["categoria"] = nova_categoria
                                            print("Categoria alterada com sucesso!")

                                    except ValueError as erro:
                                        print("Erro:", erro)

                                case 3:
                                    try:
                                        novo_preco = float(input("Digite o novo preço do produto: "))
                                        if novo_preco <= 0:
                                            raise ValueError("O preço não pode ser igual ou menor que 0.")
                                        else:
                                            produto["preco"] = novo_preco
                                            print("Preço alterado com sucesso!")

                                    except ValueError as erro:
                                        print("Erro:", erro)

                                case 4:
                                    try:
                                        nova_quantidade = int(input("Digite a nova quantidade em estoque do produto: "))
                                        if nova_quantidade < 0:
                                            raise ValueError("O estoque não pode ser menor que 0.")
                                        else:
                                            produto["quantidade"] = nova_quantidade
                                            print("Estoque alterado com sucesso!")

                                    except ValueError as erro:
                                        print("Erro:", erro)

                                case 5:
                                    print("Voltando ao menu principal...")
                                    break

                                case _:
                                    print("Opção inválida. Digite uma opção válida do menu.") 

                if not encontrado:
                    print("O produto não foi encontrado.")

            except ValueError:
                print("Digite um ID válido.")

        case 5:
            try:
                print("\n============ Exclusão ============")
                id_excluir = int(input("Digite o ID do produto que você gostaria de tirar: "))
                encontrado1 = False
 
                for produto in produtos:
                    if produto["id"] == id_excluir:
                        encontrado1 = True
 
                        decisao = input(
                            "Deseja mesmo apagar esse produto?\n"
                            "1: Não\n"
                            "2: Sim\n"
                            "Resposta: "
                        ).strip()
 
                        if decisao == "2":
                            remover_produto(produto)
                        elif decisao == "1":
                            print("Encerrando exclusão.")
                        else:
                            print("Nenhuma das opções foi escolhida.")
 
                        break
 
                if encontrado1 == False:
                    print("Produto não encontrado/Não existe.")
 
            except ValueError:
                print("Digite um valor válido.")


        case 6:
            print("Encerrando programa...")
            break

        case _:
            print("Opção inválida. Digite uma opção válida do menu.")

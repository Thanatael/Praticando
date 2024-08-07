produtos = []


def cadastro(codigo, valor, nome, quantidade):
    produtos.append({"Codigo": codigo,
                     "Valor": valor,
                     "Nome": nome,
                     "Quantidade": quantidade})
    return produtos


def atualizar():
    while True:
        if len(produtos) != 0:
            print("=" * 50)
            ic = input("Digite o índice que deseja atualizar, há no total {} indices. \n"
                       "Ou digite [exit] para sair dessa função. \n"
                       "--> "
                       .format(len(produtos)))
            if ic != "exit":
                if ic.isnumeric():
                    if int(ic) < len(produtos):  # Verifica se existe
                        while True:
                            print("=" * 50)
                            op = input("Digite a chave que deseja atualizar: \n"
                                       "[1] Codigo \n"
                                       "[2] Valor \n"
                                       "[3] Nome \n"
                                       "[4] Quantidade \n"
                                       "[5] Voltar \n"
                                       "--> ")
                            print("=" * 50)
                            if op == "5":
                                print("Obrigado!")
                                break
                            elif op == "1":
                                produtos[int(ic)]["Codigo"] = input(
                                    "O valor atual é [{}], Digite o novo valor para ['Codigo'] : "
                                    .format(produtos[int(ic)]["Codigo"]))
                            elif op == "2":
                                produtos[int(ic)]["Valor"] = input(
                                    "O valor atual é [{}], Digite o novo valor para ['Valor'] : "
                                    .format(produtos[int(ic)]["Valor"]))
                            elif op == "3":
                                produtos[int(ic)]["Nome"] = input(
                                    "O valor atual é [{}], Digite o novo valor para ['Nome'] : "
                                    .format(produtos[int(ic)]["Nome"]))
                            elif op == "4":
                                produtos[int(ic)]["Quantidade"] = input(
                                    "O valor atual é [{}], Digite o novo valor para ['Quantidade'] : "
                                    .format(produtos[int(int(ic))]["Quantidade"]))
                            else:
                                print("Chave inválida, tente novamente")
                    else:
                        print("Não há esse índice amigo, tente de novo")
                else:
                    print("Valor inválido amigo, tente de novo")
            else:
                print("Funçao finalizada")
                break
        else:
            print("Não existe nenhum dicionário criado! Crie ao menos um.")
            break


def deletar():
    while True:
        if len(produtos) != 0:
            print("=" * 50)
            op = input("Digite o índice que deseja deletar, há no total {} indices. \n"
                       "Ou digite [exit] para sair dessa função. \n"
                       "--> "
                       .format(len(produtos)))
            if op != "exit":
                if op.isnumeric():
                    if int(op) < len(produtos):  # Verifica se existe
                        print("O dicionario de índice {} foi deletado.".format(op))
                        produtos.pop(int(op))
                        break
                else:
                    print("Valor inválido, tente novamente")
            else:
                print("Função finalizada...")
                break
        else:
            print("Não existe nenhum dicionário para ser deletado! Crie ao menos um.")
            break


def listar():
    print("=" * 50)
    print("Aqui está os valores listados.")
    for i in enumerate(produtos):
        print(list(i))


while True:
    print("=" * 50)
    print("Bem-vindo oque deseja fazer?")
    f = input("[1] Cadastrar \n"
              "[2] Atualizar \n"
              "[3] Deletar \n"
              "[4] Listar \n"
              "[5] Sair \n"
              "Escolha uma dessas opções para se fazer na lista --> ")
    if f == "5":
        print("Saindo...")
        break
    elif f == "1":  # CADASTRO
        print("=" * 50)
        print("Você está cadastrando um novo dicionario na lista, digite os seguintes valores...")
        cadastro(codigo=input("Digite o codigo: "),
                 valor=input("Digite o valor: "),
                 nome=input("Digite o nome: "),
                 quantidade=input("Digite a quantidade: "))
    elif f == "2":  # ATUALIZAR
        atualizar()
    elif f == "3":  # DELETAR
        deletar()
    elif f == "4":  # LISTAR
        listar()
    else:
        print("Valor incorreto! Tente novamente")

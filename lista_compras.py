# Lista para armazenar os produtos
lista_de_compras = []
# Contador para gerar IDs únicos
id_counter = 1

def exibir_cabecalho():

    print("    Lista de Compras Simples        ")

def exibir_menu():
    print("\nMenu de Opções:")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Pesquisar produtos")
    print("4. Sair do programa")


def adicionar_produto():
    global id_counter
    print("\nAdicionar Produto:")
    nome = input("Nome do produto: ")
    

    print("\nUnidades de Medida:")
    unidades = ["Quilograma", "Grama", "Litro", "Mililitro", "Unidade", "Metro", "Centímetro"]
    for i, unidade in enumerate(unidades, 1):
        print(f"{i}. {unidade}")
    
    while True:
        try:
            opcao_unidade = int(input("Escolha a unidade de medida (1-7): "))
            if 1 <= opcao_unidade <= 7:
                unidade_medida = unidades[opcao_unidade - 1]
                break
            else:
                print("Opção inválida. Escolha um número entre 1 e 7.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
    
    # quantidade
    while True:
        try:
            quantidade = float(input("Quantidade: "))
            if quantidade > 0:
                break
            else:
                print("A quantidade deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
    
    descricao = input("Descrição do produto: ")
    

    produto = {
        "ID": id_counter,
        "Nome": nome,
        "Unidade": unidade_medida,
        "Quantidade": quantidade,
        "Descrição": descricao
    }
    lista_de_compras.append(produto)
    print(f"Produto '{nome}' adicionado com sucesso! ID: {id_counter}")
    id_counter += 1

# Função para remover um produto
def remover_produto():
    print("\nRemover Produto:")
    try:
        id_produto = int(input("Digite o ID do produto que deseja remover: "))
        for produto in lista_de_compras:
            if produto["ID"] == id_produto:
                lista_de_compras.remove(produto)
                print(f"Produto '{produto['Nome']}' removido com sucesso!")
                return
        print("Produto não encontrado.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

# Função para pesquisar produtos por nome
def pesquisar_produtos():
    print("\nPesquisar Produtos:")
    termo = input("Digite o nome ou parte do nome do produto: ")
    resultados = [produto for produto in lista_de_compras if termo.lower() in produto["Nome"].lower()]
    
    if resultados:
        print(f"\n{len(resultados)} produto(s) encontrado(s):")
        for produto in resultados:
            print(f"ID: {produto['ID']}, Nome: {produto['Nome']}, Unidade: {produto['Unidade']}, Quantidade: {produto['Quantidade']}, Descrição: {produto['Descrição']}")
    else:
        print("Nenhum produto encontrado.")

# Função para listar todos os produtos
def listar_produtos():
    if lista_de_compras:
        print("\nLista de Produtos:")
        for produto in lista_de_compras:
            print(f"ID: {produto['ID']}, Nome: {produto['Nome']}, Unidade: {produto['Unidade']}, Quantidade: {produto['Quantidade']}, Descrição: {produto['Descrição']}")
    else:
        print("\nNenhum produto na lista de compras.")

# Loop principal do programa
while True:
    exibir_cabecalho()
    listar_produtos()
    exibir_menu()
    
    try:
        opcao = int(input("\nEscolha uma opção (1-4): "))
        
        if opcao == 1:
            adicionar_produto()
        elif opcao == 2:
            remover_produto()
        elif opcao == 3:
            pesquisar_produtos()
        elif opcao == 4:
            print("Obrigado por utilizar o programa.")
            break
        else:
            print("Opção inválida. Escolha um número entre 1 e 4.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
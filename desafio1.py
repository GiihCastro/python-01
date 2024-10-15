# Resolução com Listas
# lista_de_precos = []
# while True:
#     menu = input("""
#     Escolha uma opção:
#     1 - Cadastrar Preços de Produtos
#     2 - Sair
#     """)
#     match menu:
#         case "1":
#             try:
#                 produto = float(input("Digite um preço: "))
#                 lista_de_precos.append(produto)
#             except:
#                 print("Digite um preço válido")
#         case "2":
#             print("Fim do Programa")
#             break
#         case _:
#             print("Opção Inválida")

# maior_preco = max(lista_de_precos)

# print(f"O maior preço é: {maior_preco}")


# Resolução com If
maior_preco = 0

while True:
    menu = input("""
    Escolha uma opção:
    1 - Cadastrar Preços
    2 - Sair
    """)
    match menu:
        case "1":
            try:
                preco = float(input("Digite um preço: "))
                if preco > maior_preco:
                    maior_preco = preco
            except:
                print("Digite um preço válido")
        case "2":
            print("Fim do Programa")
            break
        case _:
            print("Opção Inválida")

print(f"O maior preço é: {maior_preco}")

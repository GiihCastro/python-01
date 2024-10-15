soma_total = 0
qtde_notas = 0

while True:
    menu = input("""
    Escolha uma opção:
    1 -  Cadastrar Nota
    2 - Sair
    """)
    match menu:
        case "1":
            nota = float(input("Digite uma nota: "))
            soma_total += nota
            qtde_notas += 1
        case "2":
            print("Fim do Programa")
            break
        case _:
            print("Opção Inválida")

media = soma_total / qtde_notas

print(f"A média das notas é {media:.2f}")

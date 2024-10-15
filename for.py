numeros = ['1','2','3','4','5','6','7','8','9','0']

consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

vogais = ['a', 'e', 'i', 'o', 'u']


contador_numeros = 0

contador_consoantes = 0

contador_vogais = 0

contador_especiais = 0

senha = input("Digite uma senha: ").lower()

for caractere in senha:
    if caractere in consoantes:
        contador_consoantes += 1
    elif caractere in vogais:
        contador_vogais += 1
    elif caractere in numeros:
        contador_numeros += 1
    else:
        contador_especiais += 1


print(f"""
    A senha: {senha} 
    Possui:
    {contador_consoantes} consoantes 
    {contador_vogais} vogais 
    {contador_numeros} números
    {contador_especiais} caracteres especiais
    """)

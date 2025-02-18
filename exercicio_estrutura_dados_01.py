# Programa para calcular a média do aluno e permitir prova substitutiva

# Solicita os dados do aluno
nome = input("Informe o nome do aluno: ")
P1 = float(input("Informe a nota da P1: "))
P2 = float(input("Informe a nota da P2: "))
listas = float(input("Informe a pontuação das listas (máximo 5 pontos): "))

# Calcula a média inicial com a equação fornecida
media = ((P1 * 35) / 100) + ((P2 * 35) / 100) + listas

# Exibe a média inicial
print(f"O aluno {nome} está com média {media:.2f}")

# Verifica se o aluno foi aprovado ou precisa da prova substitutiva
if media >= 6:
    print("Aluno aprovado direto!")
else:
    print("Aluno em recuperação.")

    # Determina a menor nota para permitir a prova substitutiva
    if P1 < P2:
        menorNota = P1
        provaSubs = "P1"
    else:
        menorNota = P2
        provaSubs = "P2"

    # Solicita a nova nota da prova de menor valor
    novaNota = float(input(f"Informe a nova nota para {provaSubs}: "))

    # Atualiza a média com a nova nota
    if provaSubs == "P1":
        P1 = novaNota
    else:
        P2 = novaNota

    media = ((P1 * 35) / 100) + ((P2 * 35) / 100) + listas

    # Exibe a nova média e o resultado final
    print(f"Nova média de {nome}: {media:.2f}")

    if media >= 6:
        print("Aluno aprovado após prova subs!")
    else:
        print("Aluno reprovado com subs!")

# Exercícios de Programação em Python

## 🔹 Exercício 01
📌 Enunciado: Cálculo da Média Final de um Aluno
Desenvolva um programa em Python que solicite ao usuário:

- Nome do aluno.
- Nota da Prova 1 (P1)
- A nota da Prova 2 (P2)
- Pontuação obtida nas listas de exercícios (máximo de 5 pontos)
  
O programa calculará a média final do aluno utilizando a seguinte fórmula:

![Nova-Imagem](https://github.com/user-attachments/assets/396884bd-2e73-4094-871a-5e96404e65bd)


### Regras de aprovação:
- Se a média final for maior ou igual a 6, exibir: "Aluno aprovado direto!"
- Caso contrário, identificar a menor nota entre P1 e P2, permitir ao aluno refazer essa prova e recalcular a média.
- Exibir a nova média e a decisão final:
- Se a média final continuar abaixo de 6, exibir: "Aluno reprovado com subs!"

### Código em Pyhon:

## Cálculo da Média com Substitutiva em Python

Este programa solicita o nome do aluno, as notas da P1, P2 e listas. Se a média for menor que 6, permite refazer a menor prova.

```python
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

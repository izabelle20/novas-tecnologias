#Escreva um aplicativo que lê um inteiro, determina e imprime se ele é ímpar ou par.

# Ler um número inteiro do usuário
num = int(input("Digite um número: "))

print(f"O número é par." if num % 2 == 0 else "O número é ímpar.")

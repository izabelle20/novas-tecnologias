#O fatorial de um inteiro não negativo n é escrito como n! (pronuncia-se “n fatorial”) e é definido como segue: n! = n · (n – 1) · (n – 2) · ... · 1 (para valores de n maiores ou iguais a 1) e n! = 1 (para n = 0) Por exemplo, 5! = 5 · 4 · 3 · 2 · 1, o que dá 120.Escreva um aplicativo que lê um inteiro não negativo, calcula e imprime seu fatorial

n = int(input("Digite um número inteiro positivo: "))

if n < 0:
    print("Número inválido")
elif n == 0:
    print("O fatorial de 0 é: 1")
else:
    resultado = 1
    original_n = n  # Salvamos o valor original de n
    while n > 0:
        resultado *= n
        n -= 1
    print(f"O fatorial de {original_n} é: {resultado}")



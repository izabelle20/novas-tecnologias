#O quadrado de um número natural n é dado pela soma dos n primeiros números ímpares consecutivos. Por exemplo, 1^2 =1, 2^2 = 1+3 etc. Dado um número n, calcule seu quadrado usando a soma de ímpares ao invés de produto.

n = int(input("Digite um número natural: "))

if n <= 0:
    print("Número inválido")
else:
    quadrado = 0
    impar = 1
    for _ in range(n):
        quadrado += impar
        impar += 2
    print(f"O quadrado de {n} usando a soma de números ímpares é: {quadrado}")

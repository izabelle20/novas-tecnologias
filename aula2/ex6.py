#A série de Fibonacci é 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, … Os dois primeiros termos são iguais a 1, e a partir do terceiro, o termo é dado pela soma dos dois termos anteriores. Dado um número n≥ 3, exiba o n-ésimo termo da série de Fibonacci.

n = int(input("Digite o valor de n (n >= 3): "))

if n <= 0:
    print("Número inválido")
elif n == 1 or n == 2:
    print("O", n, "-ésimo termo da série de Fibonacci é: 1")
else:
    a, b = 1, 1  

    i = 3  
    while i <= n:
        a, b = b, a + b 
        i += 1

    print("O", n, "-ésimo termo da série de Fibonacci é:", b)
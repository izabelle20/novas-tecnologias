#A série de Fibonacci é 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, … Os dois primeiros termos são iguais a 1, e a partir do terceiro, o termo é dado pela soma dos dois termos anteriores. Dado um número n≥ 3, exiba o n-ésimo termo da série de Fibonacci.

def fibonacci(n):
    if n <= 0:
        return "Número inválido"
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        fib = [1, 1]
        i = 2
        while i < n:
            fib[i % 2] = fib[0] + fib[1] 
            i += 1
        return fib[i % 2]

n = int(input("Digite o valor de n (n >= 3): "))
print(f"O {n}-ésimo termo da série de Fibonacci é: {fibonacci(n)}")

#Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.

n = int(input("Digite um número positivo: "))
contador = 0
numero = 2

while contador < n:
    eh_primo = True
    divisor = 2
    while divisor <= numero ** 0.5: 
        if numero % divisor == 0:
            eh_primo = False
            break
        divisor += 1
    if eh_primo:
        print(numero, end=" ")
        contador += 1
    numero += 1
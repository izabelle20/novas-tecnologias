#Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida Repita até que a opção saída seja escolhida.

while True:
    #MENU
    print("Menu:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    #OPERAÇÃO
    ope = int(input("Escolha a operação: "))

    if ope == 5:
        print("Programa encerrado.")
        break

    num1 = float(input("Entre com o primeiro número: "))
    num2 = float(input("Entre com o segundo número: "))

    if ope == 1:
        print(f"Resultado: {num1} + {num2} = {num1 + num2}")
    elif ope == 2:
        print(f"Resultado: {num1} - {num2} = {num1 - num2}")
    elif ope == 3:
        print(f"Resultado: {num1} * {num2} = {num1 * num2}")
    elif ope == 4:
        if num2 != 0:
            print(f"Resultado: {num1} / {num2} = {num1 / num2}")
        else:
            print("Erro: Divisão por zero.")
    else:
        print("Opção inválida. Digite um número entre 1 e 5.")



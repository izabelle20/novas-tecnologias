num1 = float(input("entre com o num 1:"))
num2 = float(input("entre com o num 2:"))
ope= 6

while ope!=5:
    ope = int(input(f"Qual operação: "))
    if ope==1: print(f"O resultado é {num1}+{num2}={num1+num2}")
    elif ope==2: print(f"O resultado é {num1}-{num2}={num1-num2}")
    elif ope==3: print(f"O resultado é {num1}*{num2}={num1*num2}")
    elif ope==4: print(f"O resultado é {num1}/{num2}={num1/num2}")
    else ope>5: print("Digite o numero entre 1 e 4")


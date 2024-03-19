#Escreva um aplicativo que receba a, b e c, coeficientes de uma equação do segundo grau, e calcule as raízes x’ e x” através da fórmula de Báskara.

import math

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

d= b**2 - 4*a*c
if d>= 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print(f"As raízes são: x' = {x1} e x'' = {x2}")
else:
    print(f"A equação não possui raízes reais.")

#Escreva um programa que converta uma temperatura digitada em "C” em “F”. A fórmula para essa conversão é: F = (9/5)*C+32

#Temperatura em celsius
TE = float(input("Digite a temperatura em Celsius: "))

#convertendo para F
TF = (9/5) * TE+ 32

#resultado
print(f"A temperatura em Fahrenheit é: {TF}°F")


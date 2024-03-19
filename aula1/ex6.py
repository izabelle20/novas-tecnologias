#Escreva um programa que leia a quantidade em segundos e imprima o resultado em dias, horas, minutos e segundos.

#Rascunho
#78246%60= 1304 minutos e 6 segundos (resto)

num = int(input("Entre com a quantidade em segundos: "))

#dias 
num = num//24
horas = num%24

#horas
num = num//60
min = num%60

#minutos
seg = num%60
num = num//609750

print(f"são {num} dias, {horas} horas, {min} minutos, {seg}, segundos")

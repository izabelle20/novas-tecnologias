#Numa certa agência bancária, as contas são identificadas por números de até seis dígitos seguidos de um dígito verificador, calculado conforme exemplificado a seguir. Dado um número de conta n, exiba o número de conta completo correspondente. Seja n = 7314 o número da conta. Adicionamos os dígitos de n e obtemos a soma s = 4+1+3+7 = 15; Calculamos o resto da divisão de s por 10 e obtemos o dígito d = 5. Número de conta completo: 007314−5

Nconta = 7314
s = 0
temp = Nconta
while temp > 0:
    digito = temp % 10
    s += digito
    temp //= 10

DigVerificador = s % 10

Ccompleta = f"{Nconta:06d}-{DigVerificador}"

print("Número de conta completo:", Ccompleta)


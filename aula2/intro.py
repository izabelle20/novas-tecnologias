#Cálculo do Imposto de Renda

sal = float(input("Digite o salário para cálculo do imposto: "))
base = sal
imp = 0

if base > 3000:
    imp = imp + ((base - 3000) * 0.35)
    base = 3000

if base > 1000:
    imp = imp + ((base - 1000) * 0.20)

print(f"Salário: R${sal:.2f} Imposto a pagar: R${imp:.2f}")
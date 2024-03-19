#Escreva um aplicativo que insere um número consistindo em cinco dígitos do usuário, separa o número em seus dígitos individuais e imprime os 
#dígitos separados uns dos outros por três espaços cada. Por exemplo, se o usuário digitar o número 42339, o programa deve imprimir: 4 2 3 3 9.


#Rascunho
#42339%1000=2339
#2339%1000=339
#339%1000=39
#39%1000=9

num = int(input("Entre com um numero: "))

c1=num//10000

num = num%10000
c2=num//1000

num = num%1000
c3=num//100

num = num%100
c4=num//10

num = num%10
c5=num

print(f"{c1} {c2} {c3} {c4} {c5}")
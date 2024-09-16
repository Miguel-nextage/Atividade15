# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.

N1 = float(input("Seu primeiro numero"))
op = input("Qual operação deseja")
N2 = float(input("Seu segundo numero"))

result = 0

if op == "soma" or "+":
    result = N1 + N2
    print(F"Seu resultado é {result}") 

elif op == "subtração" or "-":
    result = N1 - N2
    print(F"Seu resultado é {result}") 

elif op == "multiplicação" or "*":
    result = N1 * N2
    print(F"Seu resultado é {result}") 

elif op == "divisão" or "/":
    result = N1 / N2
    print(F"Seu resultado é {result}") 

else:
    print("Numero Invalido")

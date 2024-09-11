# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.

N1, N2 = float(input("Seu primeiro numero")), float(input("Seu segundo numero"))
op = input("Qual operação deseja?")
result = 0

if op == "soma":
    result = N1 + N2
    print(F"Seu resultado é {result}") 

elif op == "subtração":
    result = N1 - N2
    print(F"Seu resultado é {result}") 

elif op == "multiplicação":
    result = N1 * N2
    print(F"Seu resultado é {result}") 

elif op == "divisão":
    result = N1 / N2
    print(F"Seu resultado é {result}") 



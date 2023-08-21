'''
14) Desenvolver um programa que calcule o fatorial do número 5, ou seja, 5!. Desta forma, temos que 5! = 5 . 4 . 3 .
2 . 1 ou 5! = 1 . 2 . 3 . 4 . 5, equivalente a 12
'''

n = 5
fatorial = 1

for i in range(1, n + 1):
    fatorial *= i

print(f"O fatorial de {n} é {fatorial}")


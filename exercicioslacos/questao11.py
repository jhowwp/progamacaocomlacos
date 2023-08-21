'''
11) Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável b) elevada a um
expoente qualquer (Variável e), ou seja, de be
. (Sem usar Math.pow();)
'''

base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = 1

for _ in range(expoente):
    resultado *= base

print(f"{base} elevado a {expoente} é igual a {resultado}")


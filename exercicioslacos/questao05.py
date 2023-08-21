'''
5) Desenvolver um programa que apresente os resultados de uma tabela de um número qualquer. Ela deve ser
impressa no seguinte formato:
'''
num = int(input("Digite um número: "))

print(f"Tabela de multiplicação para o número {num}:")

for multiplicador in range(1, 11):
    resultado = num * multiplicador
    print(f"{num} x {multiplicador} = {resultado}")

'''
13) Desenvolver um programa que imprima a tabuada de 3 a 6
'''

for numero in range(3, 7):
    print(f"Tabuada do {numero}:")
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")

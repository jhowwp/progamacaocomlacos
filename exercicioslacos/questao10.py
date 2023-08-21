'''
10) Desenvolver um programa que apresente as potências de 3 variando de 0 a 15. Deve ser considerado que
qualquer número elevado a zero é 1, e elevado a 1 é ele próprio. A apresentação deve observar a seguinte
exibição na tela
'''

print("Potências de 3:")
for expoente in range(16):
    resultado = 3 ** expoente
    print(f"3^{expoente} = {resultado}")

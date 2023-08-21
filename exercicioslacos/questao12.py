'''
12) Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o
menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção
de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem
como maior, nem como menor, e nem na contagem da média
'''

contador = 0
soma = 0
maior = float('-inf')
menor = float('inf')

while True:
    numero = float(input("Digite um número real ou -1 para parar): "))

    if numero == -1:
        break

    contador += 1
    soma += numero

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

if contador == 0:
    print("Nenhum número foi inserido.")
else:
    media = soma / contador
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")
    print(f"A média

'''
4) Desenvolver um programa que apresente o valor da soma dos cem primeiros números inteiros (1 + 2 + 3 + 4 + ...
+ 97 + 98 + 99 + 100)
'''

soma = 0
for num in range(1, 101):
    soma += num

print(f"A soma dos cem primeiros números inteiros é {soma}")

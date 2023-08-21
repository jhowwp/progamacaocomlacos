'''
15) Desenvolver um programa que apresente a série de Fibonacci até o décimo quinto termo. A série de Fibonacci é
formada pela sequência 1,1,2,3,5,8,13,21,34, ... etc. Ela se caracteriza pela soma de um termo posterior com seu
anterior subsequente
'''

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    fib_sequence = [1, 1]
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence


n_termos = 15
serie_fibonacci = fibonacci(n_termos)

print(f"Série de Fibonacci até o {n_termos}º termo:")
for termo in serie_fibonacci:
    print(termo, end=", ")
print("\n")



# nome = input('qual eh o seu nome ? ')
# print(f'prazer em te conhecer {nome:^30} !')

# Operadores aritimeticos

n1 = int(input('um valor : '))
n2 = int(input('outro valor : '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print(f'a soma vale {s}, \na multiplicacao vale {m}, \ne a divisao vale {d:.3},', end=' ')
print(f'\na divisao inteira vale {di}, \na expo vale {e}.')

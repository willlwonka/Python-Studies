# Ex005 --> Faca um programa que leia um numero inteiro e mostre na tela e seu sucessor e antecessor

a = int(input("digite um numero"))
r1 = (a + 1)
r2 = (a - 1)
print('analisando o numero {}, seu sucessor eh {} e seu antecessor eh {}'.format(a, r1, r2))

# outra opcao 
b = int(input("digite um numero"))
print('analisando o numero {}, seu antecessor eh {} e seu sucessor eh {}' .format(b, b -1, b + 1))
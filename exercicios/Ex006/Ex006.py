# Ex006 --> Crie um algoritimo que leia o numero e mostre o seu dobro, o seu triplo e a raiz quadrada

n = int(input("digite um numero: "))
m = (n*2)
k = (n*3)
t = (n**(1/2))
print('o numero {} tem como seu dobro o numero {}, o seu triplo {} e sua raiz quadrada {}' .format(n, m, k, t))
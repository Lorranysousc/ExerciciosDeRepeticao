'''Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.'''

numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))

if numero1 < numero2:
    for cont in range (numero1, numero2+1):
        print(cont)
else:
    for cont in range (numero1, numero2-1, -1):
        print(cont)
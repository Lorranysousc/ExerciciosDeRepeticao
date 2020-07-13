'''Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.'''

conjunto = int(input('Quantos Números terá seu conjunto? '))

menor_valor = maior_valor = soma = 0
for cont in range (1, conjunto+1):
    num = float(input(f'{cont}º número: '))
    soma += num
    if cont == 1:
        menor_valor = num
    else:
        if num < menor_valor:
            menor_valor = num
    if num > maior_valor:
        maior_valor = num
print(f'Menor valor: {menor_valor} \nMaior valor: {maior_valor} \nSoma: {soma}')
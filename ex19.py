'''Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.'''

conjunto = int(input('Quantos Números terá seu conjunto? '))

menor_valor = maior_valor = soma = 0
for cont in range (1, conjunto+1):
    num = float(input(f'{cont}º número: '))
    soma += num
    if num < 0 or num > 1000:
        print('Digite apenas números entre 0 e 1000.')
        exit()
    else:
        if cont == 1:
            menor_valor = num
        else:
            if num < menor_valor:
                menor_valor = num
        if num > maior_valor:
            maior_valor = num
print(f'Menor valor: {menor_valor} \nMaior valor: {maior_valor} \nSoma: {soma}')

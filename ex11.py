'''Altere o programa anterior para mostrar no final a soma dos números.'''

numero1 = int(input('Digite o 1º número: '))
numero2 = int(input('Digite o 2º número: '))

soma = 0
if numero1 < numero2:
    for cont in range (numero1, numero2+1):
        print(cont)
        soma += cont
else:
    for cont in range (numero1, numero2-1, -1):
        print(cont)
        soma += cont
print(f'A soma do intervalo dos números é {soma}.')

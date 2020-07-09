'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:'''

from time import sleep
from sys import exit 

numero = int(input('Escolha um número de 1 a 10: '))

if numero > 10:
    exit() #Encerra o programa
if numero < 1:
    exit()
else:
    print('Processando...')
    sleep(1)

    print(f'Tabuada de {numero}:')
    for cont in range (1, 11):
        print(f'{numero} x {cont} = {numero*cont}')

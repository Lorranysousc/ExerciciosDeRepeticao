'''Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo: '''

num = int(input('Montar a tabuada de: '))
inicio = int(input('Começar por: '))
final = int(input('Terminar em: '))
while final < inicio:
    final = int(input('Escolha um final maior que o inicio. \nTerminar em: '))
for cont in range (inicio, final+1):
    print(f'{num} x {cont} = {num*cont}')

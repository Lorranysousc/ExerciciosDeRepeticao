'''Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.'''

num_par = num_impar = 0  #Ambas variáveis iniciam o programa valendo 0.
for cont in range (1, 11):
    num = int(input(f'Digite o {cont}º número: '))
    if num % 2 == 0:
        num_par += 1  #Abreviação de "num_par = num_par + 1"
    else:
        num_impar += 1
print(f'Você digitou {num_par} números pares e {num_impar} números ímpares.')
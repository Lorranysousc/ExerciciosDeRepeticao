'''Faça um programa que leia 5 números e informe a soma e a média dos números.'''

soma = 0
for cont in range (1, 6):
	numero = float(input(f'Digite o {cont}º número: '))
	soma += numero
media = soma/cont
print(f'Soma: {soma:.2f} \nMédia: {media:.2f}') #:.2f formatação do número de casas depois da vírgula
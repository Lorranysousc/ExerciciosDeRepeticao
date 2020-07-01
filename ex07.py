'''Faça um programa que leia 5 números e informe o maior número.'''

maior_num = 0
for cont in range (1, 6):
	numero = float(input(f'Digite o {cont}º número: '))
	if numero > maior_num:
		maior_num = numero
print(f'O maior número é o {maior_num:.2f}')
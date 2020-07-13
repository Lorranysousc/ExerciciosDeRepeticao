'''Faça um programa que calcule o mostre a média aritmética de N notas.'''

quant_notas = int(input('Quantas notas deseja inserir? '))

soma_notas = 0
for cont in range (1, quant_notas+1):
    nota = float(input(f'{cont}ª nota: '))
    soma_notas += nota
media = soma_notas/quant_notas
print(f'Média: {media:.1f}.')

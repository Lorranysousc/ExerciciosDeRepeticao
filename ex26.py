'''Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.'''

total_eleitores = int(input('Número total de eleitores: '))

total_votosA = total_votosB = total_votosC = 0
for cont in range (1, total_eleitores+1):
    print(f'{cont}º ELEITOR')
    nome = str(input('Nome: '))
    print('[1]Candidato A [2]Candidato B [3]Candidato C')
    candidato = int(input('Vote: '))

    if candidato == 1:
        total_votosA += 1
    elif candidato == 2:
        total_votosB += 1
    else:
        total_votosC += 1
print('**TOTAL DE VOTOS**')
print(f'Candidato A: {total_votosA} voto(s) \nCandidato B: {total_votosB} voto(s) \nCandidato C: {total_votosC} voto(s)')

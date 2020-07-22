'''Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.'''

aluno_mais_alto = aluno_mais_baixo = 0
num_mais_alto = num_mais_baixo = 0
for cont in range (1, 10+1):
    print(f'ALUNO {cont}') #ALUNO 1
    num_aluno = str(input('Número aluno: '))
    altura_aluno = float(input('Altura: '))*100 #Converter em centímetros
    if cont == 1: #Ambas as variáveis vão receber o 1° valor digitado, que vai servir de parâmetro para os outros
        aluno_mais_alto = aluno_mais_baixo = altura_aluno
        num_mais_alto = num_mais_baixo = num_aluno
    else:
        if altura_aluno > aluno_mais_alto:
            aluno_mais_alto = altura_aluno
            num_mais_alto = num_aluno
        if aluno_mais_baixo > altura_aluno:
            aluno_mais_baixo = altura_aluno
            num_mais_baixo = num_aluno
print(
    f'O aluno mais alto é o {num_mais_alto} com {aluno_mais_alto:.0f}cm. \nO aluno mais baixo é o {num_mais_baixo} com {aluno_mais_baixo:.0f}cm.')

'''Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
a. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
b. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.'''

from datetime import datetime #Módulo para importar data atual

ano_entrada = int(input('Ano entrada: '))
salario_inicial = float(input('Salário inicial: R$ '))

ano_atual = datetime.now().year 
percentual = 0
while ano_entrada < ano_atual:
    ano_entrada += 1
    percentual += + 1.5 #1.5 é o percentual de aumento a cada ano
salario_atual = (salario_inicial*percentual/100)+salario_inicial
print(f'Ano: {ano_atual} \nSalário atual: R$ {salario_atual:.2f}')

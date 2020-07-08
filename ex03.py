'''Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd'
'''

nome = str(input('Digite seu nome: '))
tamanho_nome = len(nome)
while tamanho_nome < 3:
    nome = str(input('Nome Inválido. \nDigite seu nome: '))
    tamanho_nome = len(nome)

idade = int(input('Idade: '))
while idade < 0 or idade > 150:
    idade = int(input('Idade Inválido. \nIdade: '))

salario = float(input('Salário R$: '))
while salario < 0:
    salario = float(input('Salário Inválido. \nSalário R$: '))

sexo = str(input('Sexo [F/M]: '))[0] #[0] pega a primeira letra da palavra.
while sexo not in 'FfMm':
    sexo = str(input('Sexo Inválido. \nSexo [F/M]: '))[0]

estado_civil = int(input('Estado Civil \n[1]Solteiro(a) \n[2]Casado(a) \n[3]Viúvo(a) \n[4]Divorciado(a) \n'))
while estado_civil < 1 or estado_civil > 4:
    estado_civil = int(input('Estado Civil inválido. \n[1]Solteiro(a) \n[2]Casado(a) \n[3]Viúvo(a) \n[4]Divorciado(a) \n'))

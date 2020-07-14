'''O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:'''

preco_pao = float(input('Preço do pão: R$ '))

print('-' * 45)
print('Panificadora Pão de Ontem - Tabela de preços')
print('-' * 45)
for cont in range (1, 51):
    print(f'{cont} - R$ {cont*preco_pao:.2f}') #":.2f" formatação de 2 casas depois do ponto.
print('-' * 45)

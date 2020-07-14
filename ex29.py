'''O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo: '''

print('-' * 36)
print('Lojas Quase Dois - Tabela de preços')
print('-' * 36)
for cont in range (1, 51):
    print(f'{cont} - R$ {cont*1.99:.2f}') #":.2f" formatação de 2 casas depois do ponto.
print('-' * 36)

quant_produtos = int(input('Quantidade de produtos comprados: '))
print(f'Valor R$ {quant_produtos*1.99:.2f}')

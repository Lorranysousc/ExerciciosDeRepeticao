'''O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo: '''

from time import sleep

start = 1
while start == 1: #Reinicia o programa quando chega ao final.
    print('LOJAS TABAJARA')
    cont = 1
    valor_produto = ''
    total_compra = 0
    while valor_produto != 0: #Recebe valor dos produtos comprados.
        valor_produto = float(input(f'Produto {cont}: R$ ')) 
        total_compra += valor_produto
        cont += 1
        if valor_produto == 0: #Finaliza o programa.
            print(f'Total: R$ {total_compra:.2f}')        
            dinheiro_cliente = float(input('Dinheiro: R$ '))
            troco = dinheiro_cliente - total_compra
            print(f'Troco: R$ {troco:.2f}')
    sleep(3)
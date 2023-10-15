print('Seja bem-vindo à loja de Geovanna Melo! RU: 4466904\n') # Apresentação inicial da loja

valor_produto = float(input('Digite o valor do produto: ')) # Pergunta direcionada ao cliente
quantidade_produto = int(input('Digite a quantidade desejada: ')) # Pergunta direcionada ao cliente
desconto_produto = 0
sem_desconto = valor_produto * quantidade_produto # Calcula o valor sem desconto

if quantidade_produto < 10: # Poderia ser também "<= 9"
    desconto_produto = 0.00 # Desconto de 0%
    print('Não há desconto a ser aplicado.')
elif quantidade_produto > 10 and quantidade_produto < 100:
    desconto_produto = 0.05 # Desconto de 5%
    print('Desconto de 5%')
elif quantidade_produto > 100 and quantidade_produto < 1000:
    desconto_produto = 0.10 # Desconto de 10%
    print('Desconto de 10%')
else:
    desconto_produto = 0.15 # Desconto de 15%
    print('Desconto de 15%')

com_desconto = sem_desconto - sem_desconto * desconto_produto  # Calcula o valor com desconto
print('O valor total das compras sem desconto é de: R$ {:.2f}'.format(sem_desconto)) # Imprime o valor sem desconto
print('O valor total das compras com desconto é de: R$ {:.2f}'.format(com_desconto)) # Imprime o valor com desconto
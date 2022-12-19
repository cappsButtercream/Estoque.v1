from time import sleep

estoque = ('Arroz', 35, 'Feijão', 17, 'Macarrão', 28, 'Farinha', 47, 'Açucar', 46, 'Sal refinado', 32,
           'Sal grosso', 7, 'Tempero', 57, 'milho', 52, 'óleo de cozinha', 39)

preco = ('3,50', '5,40', '2,30', '5,00', '3,00', '2,50', '6,00', '3,50', '4,00', '7,00',)


print('Savan')
print('=' * 10)
print('Preparando Software...')
print('=' * 10)
print('Carregando....')
sleep(2)
while True:
    print('''Opções:
          (1) Verificar estoque'
          (2) Preços dos itens'
          (3) Fazer pedidos'
          (4) Sair....''')
    o = int(input('Qual irá escolher: '))
    if o == 1:
        print('----------------------------')
        print('Verificar Estoque:')
        print('----------------------------')
        print(f'''{estoque[0]}..............[{estoque[1]}]
{estoque[2]}..............[{estoque[3]}]
{estoque[4]}..............[{estoque[5]}]
{estoque[6]}..............[{estoque[7]}]
{estoque[8]}..............[{estoque[9]}]
{estoque[10]}..............[{estoque[11]}]
{estoque[12]}..............[{estoque[13]}]
{estoque[14]}..............[{estoque[15]}]
{estoque[16]}..............[{estoque[17]}]
{estoque[18]}..............[{estoque[19]}]''')
        print('=' * 10)
        print('Carregando....')
        sleep(2)
        print('=' * 10)
    if o == 2:
        print('----------------------------')
        print('Preços:')
        print('----------------------------')
        print(f'''{estoque[0]}..............[{preco[0]}]
{estoque[2]}..............[{preco[1]}]
{estoque[4]}..............[{preco[2]}]
{estoque[6]}..............[{preco[3]}]
{estoque[8]}..............[{preco[4]}]
{estoque[10]}..............[{preco[5]}]
{estoque[12]}..............[{preco[6]}]
{estoque[14]}..............[{preco[7]}]
{estoque[16]}..............[{preco[8]}]
{estoque[18]}..............[{preco[9]}]''')
        print('=' * 10)
        print('Carregando....')
        sleep(2)
        print('=' * 10)
    if o == 3:
        estoque = (
            'Arroz', 35 + 60, 'Feijão', 17 + 60, 'Macarrão', 28 + 60, 'Farinha', 47 + 60, 'Açucar', 46 + 60,
            'Sal refinado',
            32 + 60,
            'Sal grosso', 7 + 60, 'Tempero', 57 + 60, 'milho', 52 + 60, 'óleo de cozinha', 39 + 60)
        print('=' * 10)
        print('Pedido de estoque feito....')
        print('Carregando....')
        sleep(2)
        print('=' * 10)
    if o == 4:
        break
    if o > 4:
        print('=' * 10)
        print('Tente de novo')
        print('=' * 10)
    if o < 1:
        print('=' * 10)
        print('Tente de novo')
        print('=' * 10)
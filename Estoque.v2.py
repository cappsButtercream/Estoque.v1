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
          (3) Sair....''')
    o = int(input('Qual irá escolher: '))
    if o == 1:
        print('----------------------------')
        print('Verificar Estoque:')
        print('----------------------------')
        for pos in range(0, len(estoque)):
            if pos % 2 == 0:
                print(f'{estoque[pos]:.<30}', end='')
            else:
                print(f'[{estoque[pos]:<7}')
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
        break
    if o > 3:
        print('=' * 10)
        print('Tente de novo')
        print('=' * 10)
    if o < 1:
        print('=' * 10)
        print('Tente de novo')
        print('=' * 10)
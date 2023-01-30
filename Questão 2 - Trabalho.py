print('Bem-Vindo a Pizzaria de Renan Henrique Soares Santos')
print('--------------Cardápio--------------')
print('| Código | Descrição   | Pizza Média | Pizza Grande | ')
print('|   21   | Napolithana |    R$ 20,00 |    R$ 26,00  | ')
print('|   22   | Margherita  |    R$ 20,00 |    R$ 26,00  | ')
print('|   23   | Calabresa   |    R$ 25,00 |    R$ 32,50  | ')
print('|   24   | Toscana     |    R$ 30,00 |    R$ 39,00  | ')
print('|   25   | Portuguesa  |    R$ 30,00 |    R$ 39,00  | ')

#definição de contador para os laços de repetição
contador = 0

#While infinitito para começar a usar os laços de condição
while(True):
    tamanho = input('Qual o tamanho da pizza que deseja (M/G): ')
    codigo = int(input('Entre com o código do sabor desejado: '))
    #if e elif seguidos dos respectivos tamanhos G e M inde codigo por codigo
    if(codigo == 21 and tamanho == 'G'):
        contador  = contador + 26
        print('Você pediu uma Pizza Napolitana')
    elif(codigo == 21 and tamanho == 'M'):
        contador = contador + 20
        print('Você pediu uma Pizza Napolitana')
    elif codigo == 22 and tamanho == 'G':
        contador = contador + 26
        print('Você pediu uma Pizza Margherita')
    elif(codigo == 22 and tamanho == 'M'):
        contador = contador + 20
        print('Você pediu uma Pizza Margherita')
    elif codigo == 23 and tamanho == 'G':
        contador = contador + 32.50
        print('Você pediu uma Pizza Calabresa')
    elif(codigo == 23 and tamanho == 'M'):
        contador = contador +25
        print('Você pediu uma Pizza Calabresa')
    elif codigo == 24 and tamanho == 'G':
        contador = contador + 39
        print('Você pediu uma Pizza Toscana')
    elif(codigo == 24 and tamanho == 'M'):
        contador = contador + 30
        print('Você pediu uma Pizza Toscana')
    elif codigo == 25 and tamanho == 'G':
        contador = contador + 39
        print('Você pediu uma Pizza Portuguesa')
    elif(codigo == 25 and tamanho == 'M'):
        contador = contador + 30
        print('Você pediu uma Pizza Portuguesa')
    #else para caso o usuário digite qualquer coisa que não seja M ou G
    else:
        print('Opção invalida')
        continue
    print('1- Sim')
    print('0- Não')
    #Criação da variável continuar para ver se vamos encerrar o laco com o break ou fazer um pedido a mais
    continuar = int(input('Gostaria de pedir algo a mais?'))
    if( continuar == 1):
        continue
    else:
        print('O total a ser pago é: R${}' .format(contador))
        break
    #e o ultimo else para o calculo do valor caso o usuario digite 0 na parte de fazer o pedido a mais



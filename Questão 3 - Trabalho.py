print('Bem-vindo ao Programa de Feijoada de Renan Henrique Soares Santos')
print('Menu Volume Feijoada')
basica = 'b'
premium = 'p'
suprema = 's'
arroz = 1
farofa = 2
couve = 3
laranja = 4
#Definição de variáveis para usar no codigo principal nos laços de repetição e nos comparadores if


#Criação da função feijoada com o uso do try para evitar o erro de digitar uma string no lugar do int
def volumeFeijoada(pergunta):
    try:
        global volume #definição da variavel volume para global para utilizar ela no final do código especificamente no calculo
        volume = int(input(pergunta))
    except ValueError: #uso do except para evitar o erro ValueError e voltar a perguntar o volume até estar nos parametros certos
        return volumeFeijoada(pergunta)
    if(volume  >= 300 and volume <= 5000):
        volume *= 0.08
        return volume
    elif(volume > 5000 or volume < 300):
        print('Não aceitamos porções menores que 300ml ou maiores 5L. Tente novamente !')
        print('Menu Volume Feijoada')
        volumeFeijoada(pergunta)

#Criação da função feijoada para fazer a pergunta de qual opção o usuário quer escolher
def opcaoFeijoada(pergunta):
    print('Menu Opção Feijoada')
    print('b - Básica (Feijão + paiol + costelinha)')
    print('p - Premium (Feijão + paiol + costelinha + partes de porco)')
    print('s - Suprema (Feijão + paiol + costelinha + partes de porco + charque + calabresa + bacon)')
    opcoes = input(pergunta)
    global opcao #definição da variavel opcao para global para utilizar ela no final do codigo especificamente no calculo
    opcao = 0
    if (opcoes == basica):
        opcao = 1
        return opcao
    elif(opcoes == premium):
        opcao = 1.25
        return opcao
    elif(opcoes == suprema):
        opcao = 1.50
        return opcao
    else:
        print('Você não digitou uma opção válida')
        return opcaoFeijoada(pergunta)
    #valores a serem multiplicados já definidos nos laços de repetições
    #else para caso o usuário digite qualquer coisa além das opções de feijoada retornar para o inicio da função

def acompanhamentoFeijoada(pergunta):
    print('\n')
    global extra #definição da variavel extra para global para utilizar ela no final do codigo especificamente no calculo
    extra = 0
    while True:
        print('0 - não desejo mais acompanhamentos (encerrar pedido)')
        print('1- 200g de arroz ')
        print('2- 150g de farofa especial ')
        print('3- 100g de couve cozida ')
        print('4- 1 laranja descacada')
        print('\n')
        acompanhamento = int(input(pergunta))
        if (acompanhamento == arroz):
                extra = extra + 5
        elif (acompanhamento == farofa):
                extra = extra + 6

        elif (acompanhamento == couve):
                extra = extra + 7

        elif (acompanhamento == laranja):
                extra = extra + 3
        elif (acompanhamento == 0):
            print('Encerrando pedido...')
            break
        else:
            print('Digite uma opção válida!')
        # valores a serem somados já definidos nos laços de repetições
        # else para caso o usuário digite qualquer coisa além dos acompanhamentos de feijoada certos retornar para o inicio da função








a = volumeFeijoada('Entre com a quantidade que deseja(ml): ')
b = opcaoFeijoada(('Entre com a opção de Feijoada: '))
c = acompanhamentoFeijoada('Deseja mais algum acompanhamento: ')
soma = volume * opcao + extra
print(f'O valor a ser pago é (R$): {soma:.2f} (Volume = {volume:.2f} * Opção = {opcao:.2f} + Acompanhamento = {extra:.2f})')



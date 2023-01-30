print('Bem a loja de Renan Henrique Soares Santos')
valor = float(input('Diga o valor unitário do produto '))
quantidade = int(input('Diga a quantidade do produto a ser adquirida '))
calculo = valor * quantidade
#Criação de variáveis para uso no codigo principal

#caso o usuário digite uma quantidade menor que ira ficar repetindo o print e pedindo novamente para ele digitar
if(valor <= 0 or quantidade <= 0 ):
    print('Você digitou algum valor invalido')
#caso o usuário digite uma quantidade menor que 4 não ira ter desconto
elif(quantidade <=4):
    print('o total a pagar é {} R$'.format(calculo))
#caso o usuário digite uma quantidade maior que 5 ira ter o desconto equivalente a 3%
elif(quantidade <= 19):
    print('O valor a pagar sem desconto foi R${} '.format(calculo))
    print('O valor a pagar com desconto é R${}' . format(calculo-(calculo * 0.03)))

#caso o usuário digite uma quantidade maior que 19 ira ter o desconto equivalente a 6%
elif(quantidade <= 99):
    print('O valor a pagar sem desconto foi R${} '.format(calculo))
    print('O valor a pagar com desconto é R${}' . format(calculo-(calculo * 0.06)))
else:
    print('O valor a pagar sem desconto foi R${} '.format(calculo))
    print('O valor a pagar com desconto é R${}'.format(calculo - (calculo * 0.1)))
    # caso o usuário digite uma quantidade maior que 19 ira ter o desconto equivalente a 10%
    #todos os prints já estão juntos de seus laços de condições assim como o calculo do desconto

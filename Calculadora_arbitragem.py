import time

def wait(t):
    time.sleep(t)
    return

def calcular_odds(odds_casa_1, odds_casa_2): # parametros são 2 listas com 2 integers dentro
    casa_1_chances = [100 / num for num in odds_casa_1] # Aqui viram floats
    casa_2_chances = [100 / num for num in odds_casa_2]

    soma_prob1 = casa_1_chances[0] + casa_2_chances[1] # aqui faz a soma da odd casa 1 indice 0
    soma_prob2 = casa_1_chances[1] + casa_2_chances[0] # aqui faz a soma da odd casa 2 indice 1

    probs = {}

    if soma_prob1 > 100:
        print('Soma das probabilidades das Odds {} e {} resultou maior que 100% ({:.2f}%), não apostar!'.format(odds_casa_1[0], odds_casa_2[1], soma_prob1))
    else: 
        print('Soma das probabilidades das Odds {} e {} resultou menor que 100%! ({:.2f}%)'.format(odds_casa_1[0], odds_casa_2[1], soma_prob1))

        sobra1 = (100 - soma_prob1) / 100 + 1              # Aqui já ajusta a sobra da banca e já vai ajustar na hora de montar o dict
        probs[odds_casa_1[0]] = casa_1_chances[0] * sobra1 # Aqui define o dict > chave_0 = 1ª odd casa 1 : prob correspondente
        probs[odds_casa_2[1]] = casa_2_chances[1] * sobra1 #                      chave_1 = 2ª odd casa 2 : prob correspondente

    if soma_prob2 > 100:
        print('Soma das probabilidades das Odds {} e {} resultou maior que 100% ({:.2f}%), não apostar!'.format(odds_casa_1[1], odds_casa_2[0], soma_prob2))
    else:
        print('Soma das probabilidades das Odds {} e {} resultou menor que 100%! ({:.2f}%)'.format(odds_casa_1[1], odds_casa_2[0], soma_prob2))

        sobra2 = (100 - soma_prob2) / 100 + 1
        probs[odds_casa_1[1]] = casa_1_chances[1] * sobra2
        probs[odds_casa_2[0]] = casa_2_chances[0] * sobra2
    
    return probs # probs é definida por uma matriz 2x2 calculando-se a soma dos valores cruzados


def calcula_valores(porcentagens): # Essa função recebe o dict no formato {odd : porcentagem da odd}
    banca = float(input('Insira valor a ser alocado:\n'))
    valor_ajustado = {odd: round(probabilidade * banca / 100, 2) for odd, probabilidade in porcentagens.items()} # Este é o dict usado para possiveis operações
    valor_exibicao = {k: f'R${v:.2f}' for k, v in valor_ajustado.items()} # Esse dict tem os valores convertidos para STRING somente para exibição formatada
    print(valor_exibicao)

i = True
while i:
    try: 
        seleciona_odds1 = input('Insira as 2 odds da PRIMEIRA casa(separados por espaço): \n')
        odds_casa_1 = [float(num)/100 for num in seleciona_odds1.split(" ")]
        
    except:        
        if 'sair' in seleciona_odds1:
            print('Encerrando programa...')
            wait(1)
            break
        else:
            print('Insira apenas numeros, separados por espaço, seu José Roela!!!')
            wait(1.5)

    try: 
        seleciona_odds2 = input('Insira as 2 odds da SEGUNDA casa(separados por espaço): \n')
        odds_casa_2 = [float(num)/100 for num in seleciona_odds2.split(" ")]
        
    except:        
        if 'sair' in seleciona_odds2:
            print('Encerrando programa...')
            wait(1)
            break
        else:
            print('Insira apenas numeros, separados por espaço, seu José Roela!!!')
            wait(1.5)
    i = False

porcentagens = calcular_odds(odds_casa_1, odds_casa_2) # Aqui é um dict no formato {odds : %chances}

#porcentagens = {1.69: 59,1715,
#                2.70: 37,0370}   # usar essas entradas para testes

print(porcentagens)

calcula_valores(porcentagens)



'''POSSÍVEIS ATUALIZAÇÕES FUTURAS:
- implementar analise de mais de 2 Odds
- Webscraping pra coleta automatica de odds nas casas
'''
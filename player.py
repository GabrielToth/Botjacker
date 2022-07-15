def max_card_value(hand_value): #Recebe valor da mão - Retorna Carta de maior valor
    max_card = 0
    for next_card_value in range(1,12):
        if hand_value + next_card_value <= 21:
            max_card = next_card_value
    return max_card


def card_quantity(hand_value): #Recebe valor da mão - Retorna a quantidade de cartas possível
    if hand_value > 21:
        return 0
    
    max_card = max_card_value(hand_value)
    total_cards = max_card
    if max_card >= 10:
        total_cards += 3
    if max_card == 11:
        total_cards -= 1
    return total_cards
    

def cards_list(hand_value): #Recebe valor da mão - Retorna o valor das Cartas possíveis
    if hand_value > 21:
        return 'BUSTED - ReMoVe Me FrOm CaRdS_lIsT'

    quant_card = card_quantity(hand_value)
    
    if quant_card < 1:
        return 'VINTE_E_UM - ReMoVe Me FrOm CaRdS_lIsT'
    
    frenchsuits_list = []
    
    if quant_card <= 10:
        for i in range(quant_card):
            frenchsuits_list.append(i+1)
    else:
        for i in range(10):
            frenchsuits_list.append(i+1)
        if quant_card >= 11: frenchsuits_list.append('J')
        if quant_card >= 12: frenchsuits_list.append('Q')
        if quant_card == 13: frenchsuits_list.append('K')
    final_list = cards_identifier(frenchsuits_list)
    return final_list
    

def cards_identifier(list): #Uso Restrito ao cards_list()
    txt_fsuit_list = ''
    for i in list:
        if i == 1: 
            txt_fsuit_list += f'A'

        else:
            txt_fsuit_list += f', {i}'
    return txt_fsuit_list


def card_probability(card_value):#Recebe Carta - Retorna valor percentual de chance
    if card_value == 10:
        return (1/13)*100*4
    else:
        return (1/13)*100
    

def lista_das_listas_final(hand_value): #Recebe valor da mão - Retorna lista das cartas possíveis
    if hand_value > 21:
        return 0
    
    max_card = max_card_value(hand_value)
    rank_lists = ''
    for i in range(max_card, 0, -1):
        if i == max_card/2:
            rank_lists += '\n'

        rank = i
        if i == 1:
            rank = 'A(1)'
        if i == 10:
            rank = '10, J, Q, K'
        if i == 11:
            rank = 'A(11)'

        rank_lists += f'{rank} - {card_probability(i):.2f}% | '
        
    return rank_lists
    
    

    

from re import M
from xml.dom.expatbuilder import parseString
import numpy as np
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import os
import player

#time.sleep(3)


print(player.lista_das_listas_final(19))

"""
def deck_probability(cards_q): #Recebe a quantidade...
    return 100 - (cards_q * card_weight)



def dealer_bust(cards_q):
    if cards_q > 4: return deck_probability(cards_q)
    return 0

def next_card_prob(dealer_hand_value): #10
    # Qual a maior carta q pode vir
    if dealer_hand_value >= 17:
        return 0

    m_card = max_card_value(dealer_hand_value)
    quantidade_cartas = card_quantity(m_card)
    aux_dealer = dealer_hand_value


    for i in range (m_card, -1, -1): #Anotação - (,0,) -> (,-1,)
        if aux_dealer + i >= 17:
            pass
        else:
            peso = card_weight
            if i == 10:
                peso = card_weight * 4
            if i == 0: peso = 0

            print(f'Dealer: {aux_dealer} | {i+1} - {peso:.2f}% | {cards_identifier(quantidade_cartas)}')

            aux_dealer = dealer_hand_value + i
            
            for j in range (i, 0, -1):
                pass
                #next_card_prob(aux_dealer)

            

    print(f'    {(card_quantity(m_card) * card_weight):.2f}% das cartas' )


def read_image_list(category):
    filenames = []
    French_Suits_list = ['black', 'yellow']
    ranks_list = ['1_11','2','3','4','5','6','7','8','9','10']
    for i in French_Suits_list:
        for j in ranks_list:
            filenames.append(j + "_" + i)

    print("list file")
    list = os.listdir(category)
    dir_names = []

    for file in list:
        dir_names.append(category + file)

    print("list file ending!")

    length = len(dir_names)
    perm = np.arange(length)
    dir_names = np.array(dir_names)
    dir_names = dir_names[perm]
    
    return dir_names
def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)



local_dir = 'images/'
dirs_list = read_image_list(local_dir)

card_weight = (1/13)*100

while not keyboard.is_pressed('q'):
    

    for dir in dirs_list:
        '''
        r_pixel = pyautogui.pixel[0]
        g_pixel = pyautogui.pixel[1]
        b_pixel = pyautogui.pixel[2]
        if (r_pixel == 241 or r_pixel == 240) and (g_pixel == 146 or g_pixel == 145):
        '''
        dealer_value = pyautogui.locateOnScreen(dir, region=(620, 560, 60, 40), grayscale=True, confidence=0.95)
        #print(dir)
        if dealer_value is not None:
            image = dir
            image = image.replace('images/', '')
            image = image.replace('.png', '')
            dealer_hand = ''

            if '1_11' in image:
                dealer_hand = '1'
                image.replace('1_11', '')

            for i in range(0,len(image)):

                if image[i] == '_':
                    dealer_hand = image[:i]
                    image.replace(dealer_hand, '')
                    
            
            image.replace('_', '')
            fsuits = image
            dealer_hand = int(dealer_hand)
            deck_weight = 0

            m_card = player.max_card_value(dealer_hand)
            card_quant = player.card_quantity(dealer_hand)
            deck_prob = deck_probability(card_quant)
            

            print(f'''Rank: {rank} | FSuit: {fsuits}
Dealer:
    Maior carta possível: {m_card}
    Quantidade de Cartas possíveis: {card_quant}
    Cartas possíveis: {player.cards_identifier(card_quant)}
    Dealer Bust next hand: {dealer_bust(card_quant):.2f}%
    Próxima probabilidade :  next_card_prob(dealer_hand)
    
            ''')
                

            #pyautogui.moveTo(card) # Moves the mouse to the coordinates of the image
            #click()
"""
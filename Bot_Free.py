from xml.dom.expatbuilder import parseString
import numpy as np
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import os

time.sleep(3)

def max_card_value(dealer):
    max_card = 0
    for next_card_value in range(1,12):
        if dealer + next_card_value <= 21:
            max_card = next_card_value
    return max_card

def card_quantity(dealer):
    m_card = max_card_value(dealer)
    total_cards = m_card
    if m_card >= 10:
        total_cards += 3
    if m_card == 11:
        total_cards -= 1
    return total_cards

def deck_probability(cards_q):
    return 100 - (cards_q * card_weight)

def dealer_bust(cards_q):
    if cards_q > 4: return deck_probability(cards_q)
    return 0

def cards_identifier(val):

    if val < 1:
        return ''

    frenchsuits_list = []
    frenchsuits_list.clear()
    txt_fsuit_list = ''
    if val <= 10:
        for i in range(val):
            frenchsuits_list.append(i+1)
    else:
        for i in range(10):
            frenchsuits_list.append(i+1)
        if val >= 11: frenchsuits_list.append('J')
        if val >= 12: frenchsuits_list.append('Q')
        if val == 13: frenchsuits_list.append('K')
    
    for i in frenchsuits_list:
        txt_fsuit_list += f'{i}, '
        
    return txt_fsuit_list

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
        """
        r_pixel = pyautogui.pixel[0]
        g_pixel = pyautogui.pixel[1]
        b_pixel = pyautogui.pixel[2]
        if (r_pixel == 241 or r_pixel == 240) and (g_pixel == 146 or g_pixel == 145):
        """ 
        card = pyautogui.locateOnScreen(dir, region=(620, 560, 60, 40), grayscale=True, confidence=0.95)
        #print(dir)
        if card is not None:
            image = dir
            image = image.replace('images/', '')
            image = image.replace('.png', '')
            rank = ''

            if '1_11' in image:
                if 1 == 1:
                    pass #RETORNAR QUANDO HOUVER CONTABILIZAÇÃO
                    rank = '1_11'
                image.replace('1_11', '')

            for i in range(0,len(image)):

                if image[i] == '_':
                    rank = image[:i]
                    image.replace(rank, '')
                    
            
            image.replace('_', '')
            fsuits = image
            print(f'Rank: {rank} | FSuit: {fsuits}')

            rank = int(rank)
            deck_weight = 0
            dealer_hand = int(rank)
            card_quant = card_quantity(dealer_hand)
            deck_prob = deck_probability(card_quant)
            print(f"""
    Quantidade de Cartas possíveis: {card_quant}
    Cartas possíveis: {cards_identifier(card_quant)}
    Dealer Bust next hand: {dealer_bust(card_quant):.2f}%
    17 > : 
    Maior carta possível: {max_card_value(dealer_hand)}
            """)
                

            #pyautogui.moveTo(card) # Moves the mouse to the coordinates of the image
            #click()
        
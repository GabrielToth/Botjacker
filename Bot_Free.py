import numpy as np
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import os

time.sleep(3)

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

local_dir = 'images/Dealer/'
dirs_list = read_image_list(local_dir)

while not keyboard.is_pressed('q'):
    

    for dir in dirs_list:
        """
        r_pixel = pyautogui.pixel[0]
        g_pixel = pyautogui.pixel[1]
        b_pixel = pyautogui.pixel[2]
        if (r_pixel == 241 or r_pixel == 240) and (g_pixel == 146 or g_pixel == 145):
        """ 
        card = pyautogui.locateCenterOnScreen(dir, region=(300, 400, 700, 600), grayscale=False, confidence=0.98)
        print(dir)
        if card is not None:
            image = dir
            image = image.replace('images/Dealer/', '')
            image = image.replace('.png', '')
            rank = ''
            if '10' in image:
                rank = '10'
                image.replace('10_', '')
            rank = image[0]
            image.replace(rank, '')
            image.replace('_', '')
            fsuits = image
            print(f'Rank: {rank} | FSuit: {fsuits}')
            #pyautogui.moveTo(card) # Moves the mouse to the coordinates of the image
            #click()
        
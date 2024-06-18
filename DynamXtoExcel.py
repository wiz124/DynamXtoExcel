"""
requirements:
resolution: 1920x1200
orientation:landscape
scale:125%
Usage:
1) Drag main DynamX to the top left
2) Drag spectral plots to the top right, resize to ensure spectral plots show three at a time
4) Drag excel window to the bottom left. Select your starting cell (e.g. A2)
5) Select the desired peptide, scroll to the top of the spectra (or whatever the desired starting point), and then press escape (or whatever its been bound to)
6) ???
7) profit
"""

import pyautogui as pg
from pynput.keyboard import Key, Listener
#from pynput import keyboard
import pandas as pd


pg.PAUSE = 0.1
#pg.PAUSE=1

#BOTTOM_PIXEL = (133, 133, 133) # otherwise, should be (240, 240, 240)
BOTTOM_PIXEL = (240, 240, 240)
DATA_SEQUENCE = ['down', 'down', 'down', 'down', 'enter', 'down', 'down', 'down', 'enter']
ARROW_MOVEMENT = ['right', 'right']
TOP = (1310, 200)
MIDDLE = (1315, 330) 
BOTTOM = (1310, 450)

    
def get_data(click_pos):
    pg.click(click_pos) # get spectra
    pg.click(940, 320, button='right') # open context menu
    pg.press(DATA_SEQUENCE) # copies data
    pg.click(574, 600) # activates excel tab
    pg.hotkey('ctrl', 'shift', 'v') # paste data
    pg.press(ARROW_MOVEMENT) # move right two columns
    #print(pg.pixel(1910, 485))


def on_press(key):
    
    if key == Key.esc: # get data
        counter = 3
        while (pg.pixel(1910, 485) == BOTTOM_PIXEL): # check the scroll wheel pixel
            get_data(TOP)
            pg.doubleClick(1910, 500) # next spectra
            counter += 1
        get_data(TOP)
        get_data(MIDDLE)
        get_data(BOTTOM)
        print(f"Copied {counter} spectra!")
        
 
  
    #if key == Key.left: # align window
    #    pg.moveTo(1471, 572) # position at bottom of screen
    #    pg.dragTo(1471, 421, button='left') # drag up

#open up new excel file when done copying spectrum data

#filename=input("input file name for  new excel sheet: ")


#listener = Listener(on_press=on_press)

#listener.start()


loop =True
permission=''
while loop:
    permission=input("Begin?(Y/N): ")
    if permission.upper()=='Y':
        on_press(Key.esc)
    else:
        loop= False




 

"""
Things to look out for:

1) if the context menu changed (e.g. one of the spikes is selected), then the data sequence must change
2) if the scroll bar size changes (more/less experiments), then measuring the scroll bar pixel may no longer be accurate (currently set to 1910, 335)
3) ensure that the four way split screen is all evenly spaced, if not, coordinates may have to be adjusted
"""

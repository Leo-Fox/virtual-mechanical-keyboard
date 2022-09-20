from pynput.keyboard import Listener
from playsound import playsound
from random import choice
import sys

def on_press(key):
    if sys.argv[1] == 'click':
        random_choice = choice(['1', '2', '3', '4', '5', '6'])
    elif sys.argv[1] == 'smash':
        random_choice = choice(['1', '2', '3', '4'])

    playsound(f"./sounds/{sys.argv[1]}{random_choice}.wav", False)


with Listener(on_press=on_press) as listener:
    listener.join()
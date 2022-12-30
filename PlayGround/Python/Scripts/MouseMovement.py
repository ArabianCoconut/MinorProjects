import pyautogui
import random
import time

while True:
    
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    pyautogui.moveTo(x, y, duration=0.5)
    time.sleep(0.5)

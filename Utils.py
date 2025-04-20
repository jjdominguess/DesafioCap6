import os
import time

def waitAndClean(seconds):
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')            
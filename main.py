import os
from os import listdir
from os.path import isfile, join
import threading
import time
import random
from playsound import playsound

def clock(timeS):
   pass
def noises(timeS):
    soundpath = './sounds'
    sounds = [f for f in listdir(soundpath) if isfile(join(soundpath, f))]
    print(random.choice(sounds))
    playsound("./sounds/"+ random.choice(sounds))

def main():
    clockThread = threading.Thread(target=clock, args=(2,))
    alertThread = threading.Thread(target=noises, args=(1,))
    clockThread.start()
    alertThread.start()
    alertThread.join()
    clockThread.join()

if __name__ == "__main__":
    main()

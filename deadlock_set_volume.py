import threading
from time import sleep
from random import randint

import pygame.mixer


def thread1():
    music = pygame.mixer.music
    music.load('Astral_Dreams.it')
    sleep(0.001)  # Just a little offset - higher chance of deadlock
    music.play()
    while True:
        music.set_volume(1)
        print('Volume was set to 1')
        sleep(randint(300, 400) / 1000)
        

def thread2():
    mixer = pygame.mixer
    sound = mixer.Sound('dealwaste.wav')
    while True:
        print('Playing sound effect')
        sound.play()
        sleep(randint(250, 350) / 1000)


def main():
    pygame.mixer.init()

    music = threading.Thread(target=thread1)
    sound = threading.Thread(target=thread2)

    music.start()
    sound.start()

    music.join()
    sound.join()


if __name__ == '__main__':
    main()

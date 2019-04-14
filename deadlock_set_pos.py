import threading
from time import sleep
from random import randint, random

import pygame.mixer


def thread1():
    music = pygame.mixer.music
    music.load('Astral_Dreams.it')
    sleep(0.001)  # Just a little offset - higher chance of deadlock
    music.play()
    while True:
        # NOTE: Because of the set_pos function, this is going to sound like
        # a deadlock right from the start, but the deadlock occurs after the
        # text stops scrolling down the screen
        music.set_pos(0.5)
        print('music.set_pos() called')
        sleep(randint(250, 350) / 1000)


def thread2():
    mixer = pygame.mixer
    sound = mixer.Sound('dealwaste.wav')
    while True:
        print('Playing sound effect')
        sound.play()
        sleep(randint(240, 360) / 1000)


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

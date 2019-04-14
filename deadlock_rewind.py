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
        # NOTE: Because of the rewind function, this is going to sound like
        # a deadlock right from the start, but the deadlock occurs after the
        # text stops scrolling down the screen
        music.rewind()
        print('Music was rewound')
        sleep(randint(250, 350) / 1000)


def thread2():
    mixer = pygame.mixer
    sound = mixer.Sound('dealwaste.wav')
    while True:
        print('Playing sound effect')
        sound.play()
        sleep(randint(250, 500) / 1000)


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

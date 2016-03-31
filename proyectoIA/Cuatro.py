import pygame, sys
from pygame.locals import *
import numpy as np
from Tablero import Tablero

def main():
    board = Tablero()

    pygame.init()
    board.set_dimension()

    hecho = False
    clock = pygame.time.Clock()

    while not hecho:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                hecho = True
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                board.click()
                board.reiniciar()

        board.generate()

        clock.tick(20)
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
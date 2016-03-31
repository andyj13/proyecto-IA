import pygame, sys
from pygame.locals import *
import numpy as np
from Reglas import Reglas

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
LARGO = 60
ALTO = 60
MARGEN = 3
DIMENSION = [700, 380]


class Tablero:
    def __init__(self):
        self.grid = np.zeros([6,7],dtype= np.int)
        self.use = 0
        self.jug = 0
        self.ver = 0
        self.rules = Reglas()
        self.win = 0
        self.jugando = "En Espera"

        self.screen = pygame.display.set_mode(DIMENSION)
        self.cursor = pygame.Rect(0, 0, 1, 1)
        self.clock = pygame.time.Clock()

    def set_dimension(self):
        pygame.display.set_caption("Cuatro en raya")

    def reiniciar(self):
        if self.cursor.colliderect(self.rect):
            self.grid = np.zeros([6, 7], dtype=np.int)
            self.win = 0

    def click(self):
        pos = pygame.mouse.get_pos()
        col = pos[0] // (LARGO + MARGEN)
        fil = pos[1] // (ALTO + MARGEN)

        if col < 7:
            if fil < 6:
                if self.win != 1 and self.rules.movida(self.grid, fil, col) == 1 and self.jug == 1:
                    if self.grid[fil][col] != 2 and self.grid[fil][col] != 1:
                        self.grid[fil][col] = 1
                        self.win =self.rules.verificar(self.grid, fil, col, 1)
                elif self.win != 1 and self.rules.movida(self.grid, fil, col) == 1 and self.jug == 0:
                    if self.grid[fil][col] != 2 and self.grid[fil][col] != 1:
                        self.grid[fil][col] = 2
                        self.win =self.rules.verificar(self.grid, fil, col, 0)

        if self.jug == 0 and self.win != 1 and self.rules.movida(self.grid, fil, col) == 1:
            self.jugando = "Jugador1"
            self.jug = 1
        elif self.jug == 1 and self.win != 1 and self.rules.movida(self.grid, fil, col) == 1:
            self.jugando = "Jugador2"
            self.jug = 0

        if self.rules.empate(self.grid, fil) == 1 and self.win == 0:
            self.jugando = "Empate"


    def generate(self):
        self.screen.fill(NEGRO)
        self.imagen1 = pygame.image.load("imagenesIA/rueda1.png")
        self.imagen2 = pygame.image.load("imagenesIA/rueda2.png")
        self.imagen3 = pygame.image.load("imagenesIA/rueda3.png")
        imagen4 = pygame.image.load("imagenesIA/btnRe.png")

        pygame.draw.rect(self.screen, (64, 64, 64), (0, 0, 435, 380))
        pygame.draw.rect(self.screen,(160,160,160),(435,0,290,380))

        pygame.draw.rect(self.screen, (32, 32, 32), (0, 59, 435, 2))
        pygame.draw.rect(self.screen, (32, 32, 32), (0, 122, 435, 2))
        pygame.draw.rect(self.screen, (32, 32, 32), (0, 185, 435, 2))
        pygame.draw.rect(self.screen, (32, 32, 32), (0, 249, 435, 2))
        pygame.draw.rect(self.screen, (32, 32, 32), (0, 311, 435, 2))

        pygame.draw.rect(self.screen, (32, 32, 32), (58, 0, 2, 380))
        pygame.draw.rect(self.screen, (32, 32, 32), (122, 0, 2, 380))
        pygame.draw.rect(self.screen, (32, 32, 32), (185, 0, 2, 380))
        pygame.draw.rect(self.screen, (32, 32, 32), (248, 0, 2, 380))
        pygame.draw.rect(self.screen, (32, 32, 32), (310, 0, 2, 380))
        pygame.draw.rect(self.screen, (32, 32, 32), (374, 0, 2, 380))

        font = pygame.font.SysFont(None, 30)
        texto = font.render("", 0, NEGRO)
        texto1 = font.render("Turno: ", 0, NEGRO)
        textoJugando = font.render(self.jugando, 0, NEGRO)
        textoMG = font.render("Ganador:", 0, NEGRO)


        if self.win == 1:
            if self.jug == 1:
                texto = font.render("Jugador1", 0, NEGRO)
            if self.jug == 0:
                texto = font.render("Jugador2", 0, NEGRO)

        self.screen.blit(texto, (500, 190))
        self.rect = imagen4.get_rect()
        self.rect.left, self.rect.top = (520, 290)
        self.cursor.left, self.cursor.top = pygame.mouse.get_pos()
        self.screen.blit(imagen4, self.rect)
        self.screen.blit(texto1,(450,50))
        self.screen.blit(textoJugando, (450, 75))
        self.screen.blit(textoMG, (450, 150))

        for fil in range(6):
            for col in range(7):
                if self.grid[fil][col] == 1:
                    self.screen.blit(self.imagen2,
                                     [(MARGEN + LARGO) * col + MARGEN, (MARGEN + ALTO) * fil + MARGEN, LARGO, ALTO])
                if self.grid[fil][col] == 2:
                    self.screen.blit(self.imagen3,[(MARGEN + LARGO) * col + MARGEN, (MARGEN + ALTO) * fil + MARGEN, LARGO, ALTO])
                elif self.grid[fil][col] != 2 and self.grid[fil][col] != 1:
                    self.screen.blit(self.imagen1,[(MARGEN + LARGO) * col + MARGEN,(MARGEN + ALTO) * fil + MARGEN,LARGO,ALTO])


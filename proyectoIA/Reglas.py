import pygame, sys
from pygame.locals import *
import numpy as np

class Reglas(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def contar_puntos_j(self, matriz, iterador, limite):
        self.i = 0
        self.cont = 0

        if matriz[iterador] == 1:
            self.i = iterador
            while self.i > -1:
                if matriz[self.i] == 1:
                    self.cont += 1
                elif matriz[self.i] == 2 or matriz[self.i] == 0:
                    self.i = -1
                self.i -= 1
            self.i = iterador + 1
            while self.i < limite:
                if matriz[self.i] == 1:
                    self.cont += 1
                elif matriz[self.i] == 2 or matriz[self.i] == 0:
                    self.i = limite
                self.i += 1

        return self.cont

    def contar_puntos_ia(self, matriz, iterador, limite):
        self.i = 0
        self.cont = 0

        if matriz[iterador] == 2:
            self.i = iterador
            while self.i > -1:
                if matriz[self.i] == 2:
                    self.cont += 1
                elif matriz[self.i] == 1 or matriz[self.i] == 0:
                    self.i = -1
                self.i -= 1
            self.i = iterador + 1
            while self.i < limite:
                if matriz[self.i] == 2:
                    self.cont += 1
                elif matriz[self.i] == 1 or matriz[self.i] == 0:
                    self.i = limite
                self.i += 1

        return self.cont

    def empate (self,matriz,fila):
        self.flag = 0
        if fila == 0:
            for fil in range(6):
                for col in range(7):
                    if matriz[fil][col] < 1:
                        self.flag = 1
        return self.flag

    def contar_puntos_dia (self,matriz,fil,col,jugador):  #jugador si se compara con 0 o 1
        self.i=fil
        self.j=col
        self.cont = 0
        self.contCol = 0

        if matriz[self.i][self.j] == jugador:
            while self.i < 6:
                if self.j + self.contCol >= 0:
                    if matriz[self.i][self.j+self.contCol] == jugador:
                        self.cont += 1
                        self.contCol -= 1
                    elif matriz[self.i][self.j+self.contCol] != jugador:
                        self.i = 6
                elif self.j + self.contCol < 0:
                    self.i = 6
                self.i += 1

            if self.cont < 4:
                self.contCol = 1
                self.i = fil -1
                while self.i > -1:
                    if self.j + self.contCol < 7 and self.i < 6:
                        if matriz[self.i][self.j + self.contCol] == jugador:
                            self.cont += 1
                            self.contCol += 1
                        elif matriz[self.i][self.j + self.contCol] != jugador:
                            self.i = -1
                    elif self.j + self.contCol < 0:
                        self.i = -1
                    self.i -= 1

                if self.cont < 4:
                    self.cont = 0
                    self.contCol = 0
                    self.i = fil
                    while self.i < 6:
                        if self.j + self.contCol < 7:
                            if matriz[self.i][self.j + self.contCol] == jugador:
                                self.cont += 1
                                self.contCol += 1
                            elif matriz[self.i][self.j + self.contCol] != jugador:
                                self.i = 6
                        elif self.j + self.contCol > 7:
                            self.i = 6
                        self.i += 1

                    if self.cont < 4:
                        self.i = fil - 1
                        self.contCol = -1

                        while self.i > -1:
                            if self.j + self.contCol > -1:
                                if matriz[self.i][self.j + self.contCol] == jugador:
                                    self.cont += 1
                                    self.contCol -= 1
                                elif matriz[self.i][self.j + self.contCol] != jugador:
                                    self.i = -1
                            elif self.j + self.contCol < 0:
                                self.i = -1
                            self.i -= 1


        return self.cont

    def verificar(self, matriz, fil, col, flag):
        self.cont = 0
        self.i = 0

        self.auxFila = matriz[fil]
        self.auxColumna = matriz[:, col]

        if flag == 1:
            self.puntos = self.contar_puntos_j(self.auxFila, col, 7)
        elif flag == 0:
            self.puntos = self.contar_puntos_ia(self.auxFila, col, 7)

        print self.puntos
        if self.puntos >= 4:
            return 1

        elif self.puntos <4:
            if flag == 1:
                self.puntos = self.contar_puntos_j(self.auxColumna, fil, 6)
            elif flag == 0:
                self.puntos = self.contar_puntos_ia(self.auxColumna, fil, 6)
            if self.puntos == 4:
                return 1
            elif self.puntos < 4:
                if flag == 1:
                    self.puntos = self.contar_puntos_dia(matriz, fil, col, 1)
                elif flag == 0:
                    self.puntos = self.contar_puntos_dia(matriz, fil, col, 2)
                if self.puntos == 4:
                    return 1

    def movida(self, grid, fil, col):
        if fil == 5:
            return 1
        elif grid[fil + 1][col] == 1 or grid[fil + 1][col] == 2:
            return 1
        else:
            return 0
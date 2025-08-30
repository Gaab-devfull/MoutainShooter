#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.const import WIN_WIDTH, WIN_HEIGTH
from code.menu import Menu


class Game:
    def __init__(self):
        # iniciando o código
        pygame.init()
        # criando a janela do pygame e definindo tamanho
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGTH))

    def run(self):
# 'loop' para eventos que guiarão ações da janela
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

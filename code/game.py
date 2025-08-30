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
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
# 'loop' para eventos que guiarão ações da janela
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
    # checando cada evento da janela
         #for event in pygame.event.get():
             #if event.type == pygame.QUIT:
                #pygame.quit()  # Para fechar a janela
                #quit()  # para de fato fechar o pygame
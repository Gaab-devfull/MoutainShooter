import pygame

print('setup start')
# iniciando o código
pygame.init()
# criando a janela do pygame e definindo tamanho
window = pygame.display.set_mode(size=(600, 480))
print('setup end')

# 'loop' para eventos que guiarão ações da janela
print('loop start')
while True:
    # checando cada evento da janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Para fechar a janela
            quit()  # para de fato fechar o pygame

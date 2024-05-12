import pygame

# Inicializar o pygame
pygame.init()

# Definir o clock
clock = pygame.time.Clock()

# Criando a janela do jogo
tamanho_janela = (800, 600)
janela = pygame.display.set_mode(tamanho_janela)

# Definindo o título da janela
pygame.display.set_caption("Show do Milho")

# Loop principal do jogo
rodando = True
while rodando:
    # Verificar eventos (como fechamento da janela)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Preencher a tela com a cor de fundo
    janela.fill("#198536")

    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)  # limitar o FPS para 60

# Encerrar o jogo
pygame.quit()
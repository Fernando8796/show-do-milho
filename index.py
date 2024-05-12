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

# Criando o título do jogo
titulo = pygame.font.Font(None, 60).render("Show do Milho", True, (242, 250, 17))
posicao_titulo = titulo.get_rect(center=(800 // 2, 100))  # Pegando a posição central do título

# Definindo as cores dos botões
cor_botao = (242, 250, 17)

# Função para criar botões
def criar_botao(texto, posicao, tamanho, cor):
    retangulo = pygame.Rect(posicao, tamanho)
    pygame.draw.rect(janela, cor, retangulo, border_radius=10)
    
    texto_renderizado = pygame.font.Font(None, 36).render(texto, True, (0, 0, 0))
    pos_texto = texto_renderizado.get_rect(center=retangulo.center)
    janela.blit(texto_renderizado, pos_texto)
    
    return retangulo

# Loop principal do jogo
rodando = True
while rodando:
    # Verificar eventos (como fechamento da janela)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    # Preencher a tela com a cor de fundo
    janela.fill("#198536")

    # Escrevendo o título na tela
    janela.blit(titulo, posicao_titulo)

    # Criar os botões
    botao_jogar = criar_botao("Jogar", (250, 200), (300, 50), cor_botao)
    botao_ranking = criar_botao("Ranking", (250, 300), (300, 50), cor_botao)
    botao_creditos = criar_botao("Créditos", (250, 400), (300, 50), cor_botao)
    
    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)  # limitar o FPS para 60

# Encerrar o jogo
pygame.quit()
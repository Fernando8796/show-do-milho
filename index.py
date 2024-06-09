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

# Função para verificar se o botão foi clicado
def botao_clicado(botao, posicao_mouse):
    return botao.collidepoint(posicao_mouse)

# Função que vai ser o modelo da tela inicial
def tela_inicial():

    # Criando o título do jogo
    titulo = pygame.font.Font(None, 60).render("Show do Milho", True, (242, 250, 17))
    posicao_titulo = titulo.get_rect(center=(800 // 2, 100))  # Pegando a posição central do título

    # Escrevendo o título na tela
    janela.blit(titulo, posicao_titulo)

    # Criando e retornando os botões
    return {
        "Jogar": criar_botao("Jogar", (250, 200), (300, 50), cor_botao),
        "Ranking" : criar_botao("Ranking", (250, 300), (300, 50), cor_botao),
        "Creditos": criar_botao("Créditos", (250, 400), (300, 50), cor_botao)
    }

# Função que vai ser o modelo da tela jogar
def tela_jogar():
    return {
        "Resposta1": criar_botao("Resposta1", (90, 320), (300, 70), cor_botao), 
        "Resposta2": criar_botao("Resposta2", (410, 320), (300, 70), cor_botao),
        "Resposta3": criar_botao("Resposta3", (90, 410), (300, 70), cor_botao),
        "Resposta4": criar_botao("Resposta4", (410, 410), (300, 70), cor_botao)
    }

# Dicionário para as telas disponíveis
telas = {
    "Inicial": tela_inicial,
    "Jogar": tela_jogar
}

# Começar com a tela inicial, mas ir mudando com o tempo
tela_atual = "Inicial"

# Loop principal do jogo
rodando = True
while rodando:
    # Loop para manipular os eventos
    for evento in pygame.event.get():
        # Manipulando evento de saída do jogo
        if evento.type == pygame.QUIT:
            rodando = False
        # Se o evento foi o clique do botão esquerdo 
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            # Pegando a posição do mouse
            posicao_mouse = pygame.mouse.get_pos()
            if botao_clicado(botoes["Jogar"], posicao_mouse):
                tela_atual = "Jogar"
            elif botao_clicado(botoes["Ranking"], posicao_mouse):
                print("Botão ranking clicado!")
            elif botao_clicado(botoes["Creditos"], posicao_mouse):
                print("Botão crédito clicado!")
    
    # Tela de fundo do jogo
    janela.fill("#198536")

    # Chamando a função da tela atual
    botoes = telas[tela_atual]()
    # ^-- Vai receber os botoes da tela atual
    
    # Atualizar a tela
    pygame.display.flip()
    clock.tick(10)  # limitar o FPS para 10

# Encerrar o jogo
pygame.quit()
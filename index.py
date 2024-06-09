import pygame
import json
import random

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

# Abrindo o arquivo
with open('database.json', 'r') as arquivo:
    dados = json.load(arquivo)

# Pegando 13 perguntas aleatórias da base de dados
perguntas = random.sample(dados, 13)
questao = 0


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

    criar_botao("Jogar", (250, 200), (300, 50), cor_botao)
    criar_botao("Ranking", (250, 300), (300, 50), cor_botao)
    criar_botao("Créditos", (250, 400), (300, 50), cor_botao)
        

# Função que vai ser o modelo da tela jogar
def tela_jogar():

    # Variáveis declaradas globais aqui dentro para evitar erro
    global questao
    global tela_atual
    global rodando

    if questao >= 12:
        tela_atual = "Inicial"
    
    # Criando o texto que vai conter o número da questão
    numeroQuestao = pygame.font.Font(None, 30).render(f"Pergunta Nº {questao + 1}", True, (242, 250, 17))
    janela.blit(numeroQuestao, (50, 50))

    # Criando a pergunta
    pergunta = pygame.font.Font(None, 30).render(perguntas[questao]["pergunta"], True, (242, 250, 17))
    janela.blit(pergunta, (50, 80))

    btn0 = criar_botao(perguntas[questao]["alternativas"][0], (90, 320), (300, 70), cor_botao)
    btn1 = criar_botao(perguntas[questao]["alternativas"][1], (410, 320), (300, 70), cor_botao)
    btn2 = criar_botao(perguntas[questao]["alternativas"][2], (90, 410), (300, 70), cor_botao)
    btn3 = criar_botao(perguntas[questao]["alternativas"][3], (410, 410), (300, 70), cor_botao)

    # Pegar os eventos dos botões, para ver se acertou ou não
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            posicao_mouse = pygame.mouse.get_pos()

            if botao_clicado(btn0, posicao_mouse):
                if perguntas[questao]["resposta"] == 0:
                    questao += 1
            elif botao_clicado(btn1, posicao_mouse):
                if perguntas[questao]["resposta"] == 1:
                    questao += 1
            elif botao_clicado(btn2, posicao_mouse):
                if perguntas[questao]["resposta"] == 2:
                    questao += 1
            elif botao_clicado(btn3, posicao_mouse):
                if perguntas[questao]["resposta"] == 3:
                    questao += 1

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
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            posicao_mouse = pygame.mouse.get_pos()

            if tela_atual == "Inicial":
                #Clicando no botão de Jogar
                if botao_clicado(pygame.Rect((250, 200), (300, 50)), posicao_mouse):
                    tela_atual = "Jogar"
    
    # Tela de fundo do jogo
    janela.fill("#198536")

    # Chamando a função da tela atual
    telas[tela_atual]()
    
    # Atualizar a tela
    pygame.display.flip()
    clock.tick(30)  # limitar o FPS para 10

# Encerrar o jogo
pygame.quit()
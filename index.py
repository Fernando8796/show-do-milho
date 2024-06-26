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
with open('database.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

perguntas = random.sample(dados, 14)
questao = 0

# Função para pegar 14 perguntas da base de dados (desconsiderar uma)
def pegarQuestoesNovas():

    # Pegando essa variáveis do escopo global
    global perguntas
    global questao

    perguntas = random.sample(dados, 14)
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

    # Variáveis declaradas globais aqui dentro para evitar erros de escopo
    global tela_atual
    global questao

    # Quando completar todas as questões, ele sai da tela de jogo
    if questao >= 13:
        tela_atual = "Inicial"
        pegarQuestoesNovas()
    
    # Criando o texto que vai conter o número da questão
    numeroQuestao = pygame.font.Font(None, 30).render(f"Pergunta Nº {questao + 1}", True, (242, 250, 17))
    janela.blit(numeroQuestao, (50, 50))

    # Criando a pergunta
    pergunta = pygame.font.Font(None, 30).render(perguntas[questao]["pergunta"], True, (242, 250, 17))
    janela.blit(pergunta, (50, 80))

    # Criando todos os botões das alternativas
    criar_botao(perguntas[questao]["alternativas"][0], (90, 320), (300, 70), cor_botao)
    criar_botao(perguntas[questao]["alternativas"][1], (410, 320), (300, 70), cor_botao)
    criar_botao(perguntas[questao]["alternativas"][2], (90, 410), (300, 70), cor_botao)
    criar_botao(perguntas[questao]["alternativas"][3], (410, 410), (300, 70), cor_botao)

# Começar com a tela inicial, mas ir mudando com o tempo
tela_atual = "Inicial"

# Botões vai ser um dicionário, e vai receber todos os botões das telas
botoes = {
    "tela_inicial": {
        "Jogar": pygame.Rect((250, 200), (300, 50)),
        "Ranking": pygame.Rect((250, 300), (300, 50)),
        "Creditos": pygame.Rect((250, 400), (300, 50))
    },
    "tela_jogar": {
        "btn0": pygame.Rect((90, 320), (300, 70)),
        "btn1": pygame.Rect((410, 320), (300, 70)),
        "btn2": pygame.Rect((90, 410), (300, 70)),
        "btn3": pygame.Rect((410, 410), (300, 70))
    }
}

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
                if botao_clicado(botoes["tela_inicial"]["Jogar"], posicao_mouse):
                    tela_atual = "Jogar"
                if botao_clicado(botoes["tela_inicial"]["Ranking"], posicao_mouse):
                    print("Botão Ranking clicado")
                if botao_clicado(botoes["tela_inicial"]["Creditos"], posicao_mouse):
                    print("Botão Créditos clicado")
            
            if tela_atual == "Jogar":
                if botao_clicado(botoes["tela_jogar"]["btn0"], posicao_mouse):
                    if perguntas[questao]["resposta"] == 0:
                        questao += 1
                    else:
                        tela_atual = "Inicial"
                        pegarQuestoesNovas()
                elif botao_clicado(botoes["tela_jogar"]["btn1"], posicao_mouse):
                    if perguntas[questao]["resposta"] == 1:
                        questao += 1
                    else:
                        tela_atual = "Inicial"
                        pegarQuestoesNovas()
                elif botao_clicado(botoes["tela_jogar"]["btn2"], posicao_mouse):
                    if perguntas[questao]["resposta"] == 2:
                        questao += 1
                    else:
                        tela_atual = "Inicial"
                        pegarQuestoesNovas()
                elif botao_clicado(botoes["tela_jogar"]["btn3"], posicao_mouse):
                    if perguntas[questao]["resposta"] == 3:
                        questao += 1
                    else:
                        tela_atual = "Inicial"
                        pegarQuestoesNovas()

    # Tela de fundo do jogo
    janela.fill("#198536")

    # Chamando a função da tela atual
    if tela_atual == "Inicial":
        tela_inicial()
    elif tela_atual == "Jogar":
        tela_jogar()
    
    # Atualizar a tela
    pygame.display.flip()
    clock.tick(30)  # limitar o FPS para 10

# Encerrar o jogo
pygame.quit()
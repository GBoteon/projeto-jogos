from pygame.locals import *
import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((1000, 625), 0, 32)
pygame.display.set_caption('WEIGHTLIFTER - Jogos Digitais')
clock = pygame.time.Clock()
# ---------[CORES]---------#
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (162, 162, 162)
BLACK = (0, 0, 0)
MONEY = (6, 152, 0)
# ------------------------#

# -----[VARIÁVEIS GLOBAIS]-----#
salario = 50
hit = False
multiplicador = 1
score = 0
sec = 900
trofeu = 0
peso = 1
comprimento = 100
velocidade = 5
dia = 0
progressao = 0
dinheiro = 0
fome = 150
energia = 150
v_hamburguer = 25.0
v_refri = 5.0
v_saudavel = 15.0
v_peru = 30.0
v_whey = 100.0
# -----------------------------#

# ---------[IMAGENS]---------#
background_image_filename = 'background.jpg'
background_image_filename2 = 'background2.png'
fundo_transparente_image = 'bg.png'
idle_image_filename = 'personagens/idle.png'
title_image_filename = 'title.svg'
volume_image_filename = 'volume.svg'
mutado_image_filename = 'mute.svg'
hunger_image_filename = 'icones/fome.png'
energy_image_filename = 'icones/forca.png'
dolar_image_filename = 'icones/dolar.png'
cama_image_filename = 'icones/cama.png'
loja_image_filename = 'icones/logo_da_loja.png'
halter_image_filename = 'icones/halter.png'
podio_image_filename = 'icones/podio.png'
comida_hamburguer_image_filename = 'icones/comidas/mal_nutritiva/hamburguer.png'
comida_refri_image_filename = 'icones/comidas/mal_nutritiva/refri.png'
comida_saudavel_image_filename = 'icones/comidas/saudavel/comida_saudavel.png'
comida_peru_image_filename = "icones/comidas/saudavel/peru.png"
comida_whey_image_filename = 'icones/comidas/saudavel/whey.png'
close_store_image_filename = 'icones/close_store.svg'
trofeu1_image_filename = 'icones/trofeu_1.png'
trofeu2_image_filename = 'icones/trofeu_2.png'
trofeu3_image_filename = 'icones/trofeu_3.png'

background = pygame.image.load(background_image_filename).convert()
background2 = pygame.image.load(background_image_filename2).convert()
fundo_tutorial = pygame.image.load(fundo_transparente_image).convert()
fundo_transparente = pygame.transform.scale(pygame.image.load(fundo_transparente_image), (350, 475)).convert_alpha()
fundo_trans = pygame.transform.scale(pygame.image.load(fundo_transparente_image), (400, 100)).convert_alpha()
fundo_banner = pygame.transform.scale(pygame.image.load(fundo_transparente_image), (180, 120)).convert_alpha()
idle = pygame.image.load(idle_image_filename).convert_alpha()
title = pygame.image.load(title_image_filename).convert_alpha()
volume = pygame.image.load(volume_image_filename).convert_alpha()
mutado = pygame.image.load(mutado_image_filename).convert_alpha()
hunger = pygame.transform.scale(pygame.image.load(hunger_image_filename), (50, 50)).convert_alpha()
energy = pygame.transform.scale(pygame.image.load(energy_image_filename), (50, 50)).convert_alpha()
dolar = pygame.transform.scale(pygame.image.load(dolar_image_filename), (40, 40)).convert_alpha()
cama = pygame.transform.scale(pygame.image.load(cama_image_filename), (100, 100)).convert_alpha()
loja = pygame.transform.scale(pygame.image.load(loja_image_filename), (100, 100)).convert_alpha()
halter = pygame.transform.scale(pygame.image.load(halter_image_filename), (100, 100)).convert_alpha()
podio = pygame.transform.scale(pygame.image.load(podio_image_filename), (100, 100)).convert_alpha()
comida_hamburguer = pygame.transform.scale(pygame.image.load(comida_hamburguer_image_filename),(85, 85)).convert_alpha()
comida_refri = pygame.transform.scale(pygame.image.load(comida_refri_image_filename), (85, 85)).convert_alpha()
comida_saudavel = pygame.transform.scale(pygame.image.load(comida_saudavel_image_filename), (85, 85)).convert_alpha()
comida_peru = pygame.transform.scale(pygame.image.load(comida_peru_image_filename), (85, 85)).convert_alpha()
comida_whey = pygame.transform.scale(pygame.image.load(comida_whey_image_filename), (85, 85)).convert_alpha()
botao_fechar_loja = pygame.transform.scale(pygame.image.load(close_store_image_filename), (25, 25)).convert_alpha()
trofeu1 = pygame.transform.scale(pygame.image.load(trofeu1_image_filename), (85, 85)).convert_alpha()
trofeu2 = pygame.transform.scale(pygame.image.load(trofeu2_image_filename), (85, 85)).convert_alpha()
trofeu3 = pygame.transform.scale(pygame.image.load(trofeu3_image_filename), (85, 85)).convert_alpha()

volume_alpha = 500
mutado_alpha = 0
# --------------------------

# ---------[SONS]---------#
pygame.mixer.init()
pygame.mixer.music.load('menu.mp3')
pygame.mixer.music.play(-1)
som_on = True
# ------------------------#

# ---------[TEXTO]---------#
fonte = pygame.font.SysFont(None, 30)
fonte_loja = pygame.font.SysFont(None, 15, bold=False)
dindin = pygame.font.SysFont(None, 60)
txt_dia = pygame.font.SysFont(None, 50)
txt_win = pygame.font.SysFont(None, 45)


def imprimir(texto, fonte, cor, surface, x, y):
    texto = fonte.render(texto, 1, cor)
    texto_posi = texto.get_rect()
    texto_posi.topleft = (x, y)
    surface.blit(texto, texto_posi)


class Texto(pygame.sprite.Sprite):
    def __init__(self, texto, fonte, cor, surface, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.texto = fonte.render(texto, 1, cor)
        self.rect = self.texto.get_rect()
        self.rect.topleft = (x, y)
        self.surface = surface

    def imprimir(self):
        self.surface.blit(self.texto, self.rect)

    def get_rect(self):
        return self.texto.get_rect()


def hist1():
    imprimir("Fernanda é uma competidora profissional de", fonte, (0, 0, 0), screen, 80, 250),
    imprimir("levantamento de pesos. Com a pandemia do novo ", fonte, (0, 0, 0), screen, 80, 270)
    imprimir("coronavírus, Fernanda acabou saindo um pouco da", fonte, (0, 0, 0), screen, 80, 290)
    imprimir("rotina, portanto precisa regular novamente seus  ", fonte, (0, 0, 0), screen, 80, 310)
    imprimir("hábitosalimentares e de exercícios, para então  ", fonte, (0, 0, 0), screen, 80, 330)
    imprimir("poder voltar às competições, ajude a Fernada ", fonte, (0, 0, 0), screen, 80, 350)
    imprimir("nessa jornada!", fonte, (0, 0, 0), screen, 80, 370)
    imprimir("Fernanda quer chegar ao topo, ajude ela em seus ", fonte, (0, 0, 0), screen, 80, 390)
    imprimir("treinamentos e competições, mas fique atendo ela deve ", fonte, (0, 0, 0), screen, 80, 410)
    imprimir("ganhar os três campeonatos e não pode perder o DIA.", fonte, (0, 0, 0), screen, 80, 430)
    imprimir("Campeonato Regional Dia 5,", fonte, (0, 0, 0), screen, 80, 470)
    imprimir("Campeonato Estadual Dia 10,", fonte, (0, 0, 0), screen, 80, 490)
    imprimir("Campeonato Nacional dia 15.", fonte, (0, 0, 0), screen, 80, 510)

def hist2():
    imprimir("Fernanda é uma competidora profissional de", fonte, (0, 0, 0), screen, 80, 250),
    imprimir("Campeonato Estadual Dia 10", fonte, (0, 0, 0), screen, 80, 270)

def hist3():
    imprimir("Fernanda é uma competidora profissional de", fonte, (0, 0, 0), screen, 80, 250),
    imprimir("Campeonato Nacional dia 15", fonte, (0, 0, 0), screen, 80, 270)
# -------------------------#

# ----------[CLASSES]------#
class Ponteiro(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, spriteGroup):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.speedx = 0
        self.pos_x = pos_x
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.spriteGroup = spriteGroup
        self.speedx = velocidade

    def update(self):
        self.rect.x += self.speedx
        if self.rect.x > (self.pos_x + 585):
            self.speedx = velocidade * -1
        if self.rect.x < (self.pos_x + 10):
            self.speedx = velocidade

    def treinar(self):
        global velocidade
        if velocidade < 15:
            velocidade += 1

    def perder(self):
        global velocidade
        if velocidade > 1:
            velocidade -= 1

    def fechar(self):
        self.spriteGroup.remove(self)
        self.rect.x = self.pos_x

    def abrir(self):
        self.spriteGroup.add(self)


class Acerto(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, spriteGroup):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((comprimento, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.spriteGroup = spriteGroup

    def emagrece(self):
        global comprimento
        if comprimento <= 300:
            self.rect.x -= 5
            comprimento += 10
            self.image = pygame.Surface((comprimento, 50))
            self.image.fill(GREEN)

    def engorda(self):
        global comprimento
        if comprimento >= 50:
            self.rect.x += 5
            comprimento -= 10
            self.image = pygame.Surface((comprimento, 50))
            self.image.fill(GREEN)

    def fechar(self):
        self.spriteGroup.remove(self)

    def abrir(self):
        self.spriteGroup.add(self)


class Barra(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, spriteGroup):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((600, 50))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.spriteGroup = spriteGroup
        self.hittable = False
        self.acertos = 0
        self.erros = 0
        self.rival = 0
        self.hit = False
        self.open = False
        self.scores = True

        global comprimento

        self.divisao = (600 - comprimento) / 2
        self.acerto = Acerto((pos_x + self.divisao), pos_y, spriteGroup)

        self.ponteiro = Ponteiro(pos_x, pos_y, spriteGroup)

    def fechar(self):
        self.spriteGroup.remove(self)
        self.open = False
        self.acerto.fechar()
        self.ponteiro.fechar()

    def abrir(self):
        self.spriteGroup.add(self)
        self.open = True
        self.acerto.abrir()
        self.ponteiro.abrir()

    def update(self):
        global hit
        if self.scores:
            self.score()
        if not self.scores:
            self.compe()
        if self.ponteiro.rect.x >= self.acerto.rect.x or self.ponteiro.rect.x <= (self.acerto.rect.x + comprimento):
            self.hittable = True
        if self.ponteiro.rect.x <= self.acerto.rect.x or self.ponteiro.rect.x >= (self.acerto.rect.x + comprimento):
            self.hittable = False
            self.hit = False
            hit = False

    def acertar(self):
        if self.hittable and self.hit == False:
            self.acertos += 1
            self.hit = True
        if not self.hittable:
            self.erros += 1

    def score(self):
        screen.blit(fundo_trans, (125, 350))
        imprimir("Acertos", dindin, (6, 152, 0), screen, 150, 360)
        imprimir(str(self.acertos), dindin, (6, 152, 0), screen, 215, 400)
        imprimir("Erros", dindin, RED, screen, 380, 360)
        imprimir(str(self.erros), dindin, RED, screen, 425, 400)

    def compe(self):
        imprimir("Acertos", dindin, (6, 152, 0), screen, 25, 190)
        imprimir(str(self.acertos), dindin, (6, 152, 0), screen, 90, 230)
        imprimir("Acertos", dindin, (6, 152, 0), screen, 820, 190)
        imprimir(str(self.rival), dindin, (6, 152, 0), screen, 885, 230)

    def dado(self):
        if random.randint(1, 10) > 3:
            self.rival += 1


class Peso1(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, spriteGroup):
        super().__init__()
        self.sprites = [pygame.image.load('personagens/peso_1/P01_0001.png'),
                        pygame.image.load('personagens/peso_1/P01_0002.png'),
                        pygame.image.load('personagens/peso_1/P01_0003.png'),
                        pygame.image.load('personagens/peso_1/P01_0004.png'),
                        pygame.image.load('personagens/peso_1/P01_0005.png'),
                        pygame.image.load('personagens/peso_1/P01_0006.png'),
                        pygame.image.load('personagens/peso_1/P01_0007.png'),
                        pygame.image.load('personagens/peso_1/P01_0008.png'),
                        pygame.image.load('personagens/peso_1/P01_0009.png'),
                        pygame.image.load('personagens/peso_1/P01_0010.png'),
                        pygame.image.load('personagens/peso_1/P01_0011.png'),
                        pygame.image.load('personagens/peso_1/P01_0012.png'),
                        pygame.image.load('personagens/peso_1/P01_0013.png'),
                        pygame.image.load('personagens/peso_1/P01_0014.png'),
                        pygame.image.load('personagens/peso_1/P01_0015.png'),
                        pygame.image.load('personagens/peso_1/P01_0016.png'),
                        pygame.image.load('personagens/peso_1/P01_0017.png'),
                        pygame.image.load('personagens/peso_1/P01_0018.png'),
                        pygame.image.load('personagens/peso_1/P01_0019.png'),
                        pygame.image.load('personagens/peso_1/P01_0020.png'),
                        pygame.image.load('personagens/peso_1/P01_0021.png'),
                        pygame.image.load('personagens/peso_1/P01_0022.png'),
                        pygame.image.load('personagens/peso_1/P01_0023.png'),
                        pygame.image.load('personagens/peso_1/P01_0024.png'),
                        pygame.image.load('personagens/peso_1/P01_0025.png'),
                        pygame.image.load('personagens/peso_1/P01_0026.png'),
                        pygame.image.load('personagens/peso_1/P01_0027.png'),
                        pygame.image.load('personagens/peso_1/P01_0028.png'),
                        pygame.image.load('personagens/peso_1/P01_0029.png'),
                        pygame.image.load('personagens/peso_1/P01_0030.png'),
                        pygame.image.load('personagens/peso_1/P01_0031.png'),
                        pygame.image.load('personagens/peso_1/P01_0032.png'),
                        pygame.image.load('personagens/peso_1/P01_0033.png'),
                        pygame.image.load('personagens/peso_1/P01_0034.png'),
                        pygame.image.load('personagens/peso_1/P01_0035.png'),
                        pygame.image.load('personagens/peso_1/P01_0036.png'),
                        pygame.image.load('personagens/peso_1/P01_0037.png'),
                        pygame.image.load('personagens/peso_1/P01_0038.png'),
                        pygame.image.load('personagens/peso_1/P01_0039.png'),
                        pygame.image.load('personagens/peso_1/P01_0040.png'),
                        pygame.image.load('personagens/peso_1/P01_0041.png'),
                        pygame.image.load('personagens/peso_1/P01_0042.png'),
                        pygame.image.load('personagens/peso_1/P01_0043.png'),
                        pygame.image.load('personagens/peso_1/P01_0044.png'),
                        pygame.image.load('personagens/peso_1/P01_0045.png'),
                        pygame.image.load('personagens/peso_1/P01_0046.png'),
                        pygame.image.load('personagens/peso_1/P01_0047.png'),
                        pygame.image.load('personagens/peso_1/P01_0048.png'),
                        pygame.image.load('personagens/peso_1/P01_0049.png'),
                        pygame.image.load('personagens/peso_1/P01_0050.png'),
                        pygame.image.load('personagens/peso_1/P01_0051.png'),
                        pygame.image.load('personagens/peso_1/P01_0052.png'),
                        pygame.image.load('personagens/peso_1/P01_0053.png'),
                        pygame.image.load('personagens/peso_1/P01_0054.png'),
                        pygame.image.load('personagens/peso_1/P01_0055.png'),
                        pygame.image.load('personagens/peso_1/P01_0056.png'),
                        pygame.image.load('personagens/peso_1/P01_0057.png'),
                        pygame.image.load('personagens/peso_1/P01_0058.png'),
                        pygame.image.load('personagens/peso_1/P01_0059.png'),
                        pygame.image.load('personagens/peso_1/P01_0060.png'),
                        pygame.image.load('personagens/peso_1/P01_0061.png'),
                        pygame.image.load('personagens/peso_1/P01_0062.png'),
                        pygame.image.load('personagens/peso_1/P01_0063.png'),
                        pygame.image.load('personagens/peso_1/P01_0064.png'),
                        pygame.image.load('personagens/peso_1/P01_0065.png'),
                        pygame.image.load('personagens/peso_1/P01_0066.png'),
                        pygame.image.load('personagens/peso_1/P01_0067.png'),
                        pygame.image.load('personagens/peso_1/P01_0068.png'),
                        pygame.image.load('personagens/peso_1/P01_0069.png'),
                        pygame.image.load('personagens/peso_1/P01_0070.png'),
                        pygame.image.load('personagens/peso_1/P01_0071.png'),
                        pygame.image.load('personagens/peso_1/P01_0072.png'),
                        pygame.image.load('personagens/peso_1/P01_0073.png'),
                        pygame.image.load('personagens/peso_1/P01_0074.png'),
                        pygame.image.load('personagens/peso_1/P01_0075.png'),
                        pygame.image.load('personagens/peso_1/P01_0076.png'),
                        pygame.image.load('personagens/peso_1/P01_0077.png'),
                        pygame.image.load('personagens/peso_1/P01_0078.png'),
                        pygame.image.load('personagens/peso_1/P01_0079.png'),
                        pygame.image.load('personagens/peso_1/P01_0080.png'),
                        pygame.image.load('personagens/peso_1/P01_0081.png'),
                        pygame.image.load('personagens/peso_1/P01_0082.png'),
                        pygame.image.load('personagens/peso_1/P01_0083.png'),
                        pygame.image.load('personagens/peso_1/P01_0084.png'),
                        pygame.image.load('personagens/peso_1/P01_0085.png')]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.spriteGroup = spriteGroup

    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

    def fechar(self):
        self.spriteGroup.remove(self)

    def abrir(self):
        self.spriteGroup.add(self)


class Peso2(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, spriteGroup):
        super().__init__()
        self.sprites = [pygame.image.load('personagens/peso_2/P02_0001.png'),
                        pygame.image.load('personagens/peso_2/P02_0002.png'),
                        pygame.image.load('personagens/peso_2/P02_0003.png'),
                        pygame.image.load('personagens/peso_2/P02_0004.png'),
                        pygame.image.load('personagens/peso_2/P02_0005.png'),
                        pygame.image.load('personagens/peso_2/P02_0006.png'),
                        pygame.image.load('personagens/peso_2/P02_0007.png'),
                        pygame.image.load('personagens/peso_2/P02_0008.png'),
                        pygame.image.load('personagens/peso_2/P02_0009.png'),
                        pygame.image.load('personagens/peso_2/P02_0010.png'),
                        pygame.image.load('personagens/peso_2/P02_0011.png'),
                        pygame.image.load('personagens/peso_2/P02_0012.png'),
                        pygame.image.load('personagens/peso_2/P02_0013.png'),
                        pygame.image.load('personagens/peso_2/P02_0014.png'),
                        pygame.image.load('personagens/peso_2/P02_0015.png'),
                        pygame.image.load('personagens/peso_2/P02_0016.png'),
                        pygame.image.load('personagens/peso_2/P02_0017.png'),
                        pygame.image.load('personagens/peso_2/P02_0018.png'),
                        pygame.image.load('personagens/peso_2/P02_0019.png'),
                        pygame.image.load('personagens/peso_2/P02_0020.png'),
                        pygame.image.load('personagens/peso_2/P02_0021.png'),
                        pygame.image.load('personagens/peso_2/P02_0022.png'),
                        pygame.image.load('personagens/peso_2/P02_0023.png'),
                        pygame.image.load('personagens/peso_2/P02_0024.png'),
                        pygame.image.load('personagens/peso_2/P02_0025.png'),
                        pygame.image.load('personagens/peso_2/P02_0026.png'),
                        pygame.image.load('personagens/peso_2/P02_0027.png'),
                        pygame.image.load('personagens/peso_2/P02_0028.png'),
                        pygame.image.load('personagens/peso_2/P02_0029.png'),
                        pygame.image.load('personagens/peso_2/P02_0030.png'),
                        pygame.image.load('personagens/peso_2/P02_0031.png'),
                        pygame.image.load('personagens/peso_2/P02_0032.png'),
                        pygame.image.load('personagens/peso_2/P02_0033.png'),
                        pygame.image.load('personagens/peso_2/P02_0034.png'),
                        pygame.image.load('personagens/peso_2/P02_0035.png'),
                        pygame.image.load('personagens/peso_2/P02_0036.png'),
                        pygame.image.load('personagens/peso_2/P02_0037.png'),
                        pygame.image.load('personagens/peso_2/P02_0038.png'),
                        pygame.image.load('personagens/peso_2/P02_0039.png'),
                        pygame.image.load('personagens/peso_2/P02_0040.png'),
                        pygame.image.load('personagens/peso_2/P02_0041.png'),
                        pygame.image.load('personagens/peso_2/P02_0042.png'),
                        pygame.image.load('personagens/peso_2/P02_0043.png'),
                        pygame.image.load('personagens/peso_2/P02_0044.png'),
                        pygame.image.load('personagens/peso_2/P02_0045.png'),
                        pygame.image.load('personagens/peso_2/P02_0046.png'),
                        pygame.image.load('personagens/peso_2/P02_0047.png'),
                        pygame.image.load('personagens/peso_2/P02_0048.png'),
                        pygame.image.load('personagens/peso_2/P02_0049.png'),
                        pygame.image.load('personagens/peso_2/P02_0050.png'),
                        pygame.image.load('personagens/peso_2/P02_0051.png'),
                        pygame.image.load('personagens/peso_2/P02_0052.png'),
                        pygame.image.load('personagens/peso_2/P02_0053.png'),
                        pygame.image.load('personagens/peso_2/P02_0054.png'),
                        pygame.image.load('personagens/peso_2/P02_0055.png'),
                        pygame.image.load('personagens/peso_2/P02_0056.png'),
                        pygame.image.load('personagens/peso_2/P02_0057.png'),
                        pygame.image.load('personagens/peso_2/P02_0058.png'),
                        pygame.image.load('personagens/peso_2/P02_0059.png'),
                        pygame.image.load('personagens/peso_2/P02_0060.png'),
                        pygame.image.load('personagens/peso_2/P02_0061.png'),
                        pygame.image.load('personagens/peso_2/P02_0062.png'),
                        pygame.image.load('personagens/peso_2/P02_0063.png'),
                        pygame.image.load('personagens/peso_2/P02_0064.png'),
                        pygame.image.load('personagens/peso_2/P02_0065.png'),
                        pygame.image.load('personagens/peso_2/P02_0066.png'),
                        pygame.image.load('personagens/peso_2/P02_0067.png'),
                        pygame.image.load('personagens/peso_2/P02_0068.png'),
                        pygame.image.load('personagens/peso_2/P02_0069.png'),
                        pygame.image.load('personagens/peso_2/P02_0070.png'),
                        pygame.image.load('personagens/peso_2/P02_0071.png'),
                        pygame.image.load('personagens/peso_2/P02_0072.png'),
                        pygame.image.load('personagens/peso_2/P02_0073.png'),
                        pygame.image.load('personagens/peso_2/P02_0074.png'),
                        pygame.image.load('personagens/peso_2/P02_0075.png'),
                        pygame.image.load('personagens/peso_2/P02_0076.png'),
                        pygame.image.load('personagens/peso_2/P02_0077.png'),
                        pygame.image.load('personagens/peso_2/P02_0078.png'),
                        pygame.image.load('personagens/peso_2/P02_0079.png'),
                        pygame.image.load('personagens/peso_2/P02_0080.png'),
                        pygame.image.load('personagens/peso_2/P02_0081.png'),
                        pygame.image.load('personagens/peso_2/P02_0082.png'),
                        pygame.image.load('personagens/peso_2/P02_0083.png'),
                        pygame.image.load('personagens/peso_2/P02_0084.png'),
                        pygame.image.load('personagens/peso_2/P02_0085.png')]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.spriteGroup = spriteGroup

    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

    def fechar(self):
        self.spriteGroup.remove(self)

    def abrir(self):
        self.spriteGroup.add(self)


class Peso3(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, spriteGroup):
        super().__init__()
        self.sprites = [pygame.image.load('personagens/peso_3/P03_0001.png'),
                        pygame.image.load('personagens/peso_3/P03_0002.png'),
                        pygame.image.load('personagens/peso_3/P03_0003.png'),
                        pygame.image.load('personagens/peso_3/P03_0004.png'),
                        pygame.image.load('personagens/peso_3/P03_0005.png'),
                        pygame.image.load('personagens/peso_3/P03_0006.png'),
                        pygame.image.load('personagens/peso_3/P03_0007.png'),
                        pygame.image.load('personagens/peso_3/P03_0008.png'),
                        pygame.image.load('personagens/peso_3/P03_0009.png'),
                        pygame.image.load('personagens/peso_3/P03_0010.png'),
                        pygame.image.load('personagens/peso_3/P03_0011.png'),
                        pygame.image.load('personagens/peso_3/P03_0012.png'),
                        pygame.image.load('personagens/peso_3/P03_0013.png'),
                        pygame.image.load('personagens/peso_3/P03_0014.png'),
                        pygame.image.load('personagens/peso_3/P03_0015.png'),
                        pygame.image.load('personagens/peso_3/P03_0016.png'),
                        pygame.image.load('personagens/peso_3/P03_0017.png'),
                        pygame.image.load('personagens/peso_3/P03_0018.png'),
                        pygame.image.load('personagens/peso_3/P03_0019.png'),
                        pygame.image.load('personagens/peso_3/P03_0020.png'),
                        pygame.image.load('personagens/peso_3/P03_0021.png'),
                        pygame.image.load('personagens/peso_3/P03_0022.png'),
                        pygame.image.load('personagens/peso_3/P03_0023.png'),
                        pygame.image.load('personagens/peso_3/P03_0024.png'),
                        pygame.image.load('personagens/peso_3/P03_0025.png'),
                        pygame.image.load('personagens/peso_3/P03_0026.png'),
                        pygame.image.load('personagens/peso_3/P03_0027.png'),
                        pygame.image.load('personagens/peso_3/P03_0028.png'),
                        pygame.image.load('personagens/peso_3/P03_0029.png'),
                        pygame.image.load('personagens/peso_3/P03_0030.png'),
                        pygame.image.load('personagens/peso_3/P03_0031.png'),
                        pygame.image.load('personagens/peso_3/P03_0032.png'),
                        pygame.image.load('personagens/peso_3/P03_0033.png'),
                        pygame.image.load('personagens/peso_3/P03_0034.png'),
                        pygame.image.load('personagens/peso_3/P03_0035.png'),
                        pygame.image.load('personagens/peso_3/P03_0036.png'),
                        pygame.image.load('personagens/peso_3/P03_0037.png'),
                        pygame.image.load('personagens/peso_3/P03_0038.png'),
                        pygame.image.load('personagens/peso_3/P03_0039.png'),
                        pygame.image.load('personagens/peso_3/P03_0040.png'),
                        pygame.image.load('personagens/peso_3/P03_0041.png'),
                        pygame.image.load('personagens/peso_3/P03_0042.png'),
                        pygame.image.load('personagens/peso_3/P03_0043.png'),
                        pygame.image.load('personagens/peso_3/P03_0044.png'),
                        pygame.image.load('personagens/peso_3/P03_0045.png'),
                        pygame.image.load('personagens/peso_3/P03_0046.png'),
                        pygame.image.load('personagens/peso_3/P03_0047.png'),
                        pygame.image.load('personagens/peso_3/P03_0048.png'),
                        pygame.image.load('personagens/peso_3/P03_0049.png'),
                        pygame.image.load('personagens/peso_3/P03_0050.png'),
                        pygame.image.load('personagens/peso_3/P03_0051.png'),
                        pygame.image.load('personagens/peso_3/P03_0052.png'),
                        pygame.image.load('personagens/peso_3/P03_0053.png'),
                        pygame.image.load('personagens/peso_3/P03_0054.png'),
                        pygame.image.load('personagens/peso_3/P03_0055.png'),
                        pygame.image.load('personagens/peso_3/P03_0056.png'),
                        pygame.image.load('personagens/peso_3/P03_0057.png'),
                        pygame.image.load('personagens/peso_3/P03_0058.png'),
                        pygame.image.load('personagens/peso_3/P03_0059.png'),
                        pygame.image.load('personagens/peso_3/P03_0060.png'),
                        pygame.image.load('personagens/peso_3/P03_0061.png'),
                        pygame.image.load('personagens/peso_3/P03_0062.png'),
                        pygame.image.load('personagens/peso_3/P03_0063.png'),
                        pygame.image.load('personagens/peso_3/P03_0064.png'),
                        pygame.image.load('personagens/peso_3/P03_0065.png'),
                        pygame.image.load('personagens/peso_3/P03_0066.png'),
                        pygame.image.load('personagens/peso_3/P03_0067.png'),
                        pygame.image.load('personagens/peso_3/P03_0068.png'),
                        pygame.image.load('personagens/peso_3/P03_0069.png'),
                        pygame.image.load('personagens/peso_3/P03_0070.png'),
                        pygame.image.load('personagens/peso_3/P03_0071.png'),
                        pygame.image.load('personagens/peso_3/P03_0072.png'),
                        pygame.image.load('personagens/peso_3/P03_0073.png'),
                        pygame.image.load('personagens/peso_3/P03_0074.png'),
                        pygame.image.load('personagens/peso_3/P03_0075.png'),
                        pygame.image.load('personagens/peso_3/P03_0076.png'),
                        pygame.image.load('personagens/peso_3/P03_0077.png'),
                        pygame.image.load('personagens/peso_3/P03_0078.png'),
                        pygame.image.load('personagens/peso_3/P03_0079.png'),
                        pygame.image.load('personagens/peso_3/P03_0080.png'),
                        pygame.image.load('personagens/peso_3/P03_0081.png'),
                        pygame.image.load('personagens/peso_3/P03_0082.png'),
                        pygame.image.load('personagens/peso_3/P03_0083.png'),
                        pygame.image.load('personagens/peso_3/P03_0084.png'),
                        pygame.image.load('personagens/peso_3/P03_0085.png')]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.spriteGroup = spriteGroup

    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

    def fechar(self):
        self.spriteGroup.remove(self)

    def abrir(self):
        self.spriteGroup.add(self)


class Idle(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, spriteGroup):
        pygame.sprite.Sprite.__init__(self)
        self.image = idle
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.spriteGroup = spriteGroup

    def fechar(self):
        self.spriteGroup.remove(self)

    def abrir(self):
        self.spriteGroup.add(self)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, peso, spriteGroup):
        super().__init__()
        self.sprites = [pygame.image.load('personagens/menina_01/M01_0001.png'),
                        pygame.image.load('personagens/menina_01/M01_0002.png'),
                        pygame.image.load('personagens/menina_01/M01_0003.png'),
                        pygame.image.load('personagens/menina_01/M01_0004.png'),
                        pygame.image.load('personagens/menina_01/M01_0005.png'),
                        pygame.image.load('personagens/menina_01/M01_0006.png'),
                        pygame.image.load('personagens/menina_01/M01_0007.png'),
                        pygame.image.load('personagens/menina_01/M01_0008.png'),
                        pygame.image.load('personagens/menina_01/M01_0009.png'),
                        pygame.image.load('personagens/menina_01/M01_0010.png'),
                        pygame.image.load('personagens/menina_01/M01_0011.png'),
                        pygame.image.load('personagens/menina_01/M01_0012.png'),
                        pygame.image.load('personagens/menina_01/M01_0013.png'),
                        pygame.image.load('personagens/menina_01/M01_0014.png'),
                        pygame.image.load('personagens/menina_01/M01_0015.png'),
                        pygame.image.load('personagens/menina_01/M01_0016.png'),
                        pygame.image.load('personagens/menina_01/M01_0017.png'),
                        pygame.image.load('personagens/menina_01/M01_0018.png'),
                        pygame.image.load('personagens/menina_01/M01_0019.png'),
                        pygame.image.load('personagens/menina_01/M01_0020.png'),
                        pygame.image.load('personagens/menina_01/M01_0021.png'),
                        pygame.image.load('personagens/menina_01/M01_0022.png'),
                        pygame.image.load('personagens/menina_01/M01_0023.png'),
                        pygame.image.load('personagens/menina_01/M01_0024.png'),
                        pygame.image.load('personagens/menina_01/M01_0025.png'),
                        pygame.image.load('personagens/menina_01/M01_0026.png'),
                        pygame.image.load('personagens/menina_01/M01_0027.png'),
                        pygame.image.load('personagens/menina_01/M01_0028.png'),
                        pygame.image.load('personagens/menina_01/M01_0029.png'),
                        pygame.image.load('personagens/menina_01/M01_0030.png'),
                        pygame.image.load('personagens/menina_01/M01_0031.png'),
                        pygame.image.load('personagens/menina_01/M01_0032.png'),
                        pygame.image.load('personagens/menina_01/M01_0033.png'),
                        pygame.image.load('personagens/menina_01/M01_0034.png'),
                        pygame.image.load('personagens/menina_01/M01_0035.png'),
                        pygame.image.load('personagens/menina_01/M01_0036.png'),
                        pygame.image.load('personagens/menina_01/M01_0037.png'),
                        pygame.image.load('personagens/menina_01/M01_0038.png'),
                        pygame.image.load('personagens/menina_01/M01_0039.png'),
                        pygame.image.load('personagens/menina_01/M01_0040.png'),
                        pygame.image.load('personagens/menina_01/M01_0041.png'),
                        pygame.image.load('personagens/menina_01/M01_0042.png'),
                        pygame.image.load('personagens/menina_01/M01_0043.png'),
                        pygame.image.load('personagens/menina_01/M01_0044.png'),
                        pygame.image.load('personagens/menina_01/M01_0045.png'),
                        pygame.image.load('personagens/menina_01/M01_0046.png'),
                        pygame.image.load('personagens/menina_01/M01_0047.png'),
                        pygame.image.load('personagens/menina_01/M01_0048.png'),
                        pygame.image.load('personagens/menina_01/M01_0049.png'),
                        pygame.image.load('personagens/menina_01/M01_0050.png'),
                        pygame.image.load('personagens/menina_01/M01_0051.png'),
                        pygame.image.load('personagens/menina_01/M01_0052.png'),
                        pygame.image.load('personagens/menina_01/M01_0053.png'),
                        pygame.image.load('personagens/menina_01/M01_0054.png'),
                        pygame.image.load('personagens/menina_01/M01_0055.png'),
                        pygame.image.load('personagens/menina_01/M01_0056.png'),
                        pygame.image.load('personagens/menina_01/M01_0057.png'),
                        pygame.image.load('personagens/menina_01/M01_0058.png'),
                        pygame.image.load('personagens/menina_01/M01_0059.png'),
                        pygame.image.load('personagens/menina_01/M01_0060.png'),
                        pygame.image.load('personagens/menina_01/M01_0061.png'),
                        pygame.image.load('personagens/menina_01/M01_0062.png'),
                        pygame.image.load('personagens/menina_01/M01_0063.png'),
                        pygame.image.load('personagens/menina_01/M01_0064.png'),
                        pygame.image.load('personagens/menina_01/M01_0065.png'),
                        pygame.image.load('personagens/menina_01/M01_0066.png'),
                        pygame.image.load('personagens/menina_01/M01_0067.png'),
                        pygame.image.load('personagens/menina_01/M01_0068.png'),
                        pygame.image.load('personagens/menina_01/M01_0069.png'),
                        pygame.image.load('personagens/menina_01/M01_0070.png'),
                        pygame.image.load('personagens/menina_01/M01_0071.png'),
                        pygame.image.load('personagens/menina_01/M01_0072.png'),
                        pygame.image.load('personagens/menina_01/M01_0073.png'),
                        pygame.image.load('personagens/menina_01/M01_0074.png'),
                        pygame.image.load('personagens/menina_01/M01_0075.png'),
                        pygame.image.load('personagens/menina_01/M01_0076.png'),
                        pygame.image.load('personagens/menina_01/M01_0077.png'),
                        pygame.image.load('personagens/menina_01/M01_0078.png'),
                        pygame.image.load('personagens/menina_01/M01_0079.png'),
                        pygame.image.load('personagens/menina_01/M01_0080.png'),
                        pygame.image.load('personagens/menina_01/M01_0081.png'),
                        pygame.image.load('personagens/menina_01/M01_0082.png'),
                        pygame.image.load('personagens/menina_01/M01_0083.png'),
                        pygame.image.load('personagens/menina_01/M01_0084.png'),
                        pygame.image.load('personagens/menina_01/M01_0085.png')]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.spriteGroup = spriteGroup
        self.idle = Idle((pos_x + 211), (pos_y + 166), spriteGroup)

        if peso == 1:
            self.peso = Peso1((pos_x + 159), (pos_y + 174), spriteGroup)
        if peso == 2:
            self.peso = Peso2((pos_x + 159), (pos_y + 174), spriteGroup)
        if peso == 3:
            self.peso = Peso3((pos_x + 159), (pos_y + 174), spriteGroup)

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.current_money = dinheiro
        self.salary = salario
        self.current_hunger = fome
        self.maximum_hunger = 200
        self.hunger_bar_lenght = 200
        self.hunger_ratio = self.maximum_hunger / self.hunger_bar_lenght
        self.current_energy = energia
        self.maximum_energy = 200
        self.energy_bar_lenght = 200
        self.energy_ratio = self.maximum_energy / self.energy_bar_lenght
        self.score = score

    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

    def basic_score(self):
        imprimir("SCORE: " + str(self.score), dindin, (0, 0, 0), screen, 700, 590)

    def lost_score(self, amount):
        global score
        self.score = score - (amount * multiplicador)
        score = self.score

    def get_score(self, amount):
        global score
        self.score = score + (amount * multiplicador)
        score = self.score

    def basic_money(self):
        imprimir(str(self.current_money), dindin, (6, 152, 0), screen, 810, 130)
        screen.blit(dolar, (760, 125))

    def get_money(self):
        global dinheiro
        self.current_money += self.salary
        dinheiro = self.current_money

    def lost_money(self, amout):
        global dinheiro
        self.current_money -= amout
        dinheiro = self.current_money

    def set_salario(self, amount):
        global salario
        self.salary = amount
        salario = amount

    def get_train(self, amount):
        global fome
        if self.current_hunger > 0:
            self.current_hunger -= amount
            fome = self.current_hunger
        if self.current_hunger <= 0:
            self.current_hunger = 0
            fome = self.current_hunger

    def get_food(self, amount):
        global fome
        if self.current_hunger < self.maximum_hunger:
            self.current_hunger += amount
            fome = self.current_hunger
        if self.current_hunger >= self.maximum_hunger:
            self.current_hunger = self.maximum_hunger
            fome = self.current_hunger

    def basic_hunger(self):
        pygame.draw.rect(screen, (236, 124, 48), (770, 80, self.current_hunger / self.hunger_ratio, 25))
        pygame.draw.rect(screen, (255, 255, 255), (770, 80, self.hunger_bar_lenght, 25), 4)
        screen.blit(hunger, (750, 65))

    def get_tired(self, amount):
        global energia
        if self.current_energy > 0:
            self.current_energy -= amount
            energia = self.current_energy
        if self.current_energy <= 0:
            self.current_energy = 0
            energia = self.current_energy

    def get_rest(self, amount):
        global energy
        if self.current_energy < self.maximum_energy:
            self.current_energy += amount
            energy = self.current_energy
        if self.current_energy >= self.maximum_energy:
            self.current_energy = self.maximum_energy
            energy = self.current_energy

    def basic_energy(self):
        pygame.draw.rect(screen, (255, 255, 0), (770, 20, self.current_energy / self.energy_ratio, 25))
        pygame.draw.rect(screen, (255, 255, 255), (770, 20, self.energy_bar_lenght, 25), 4)
        screen.blit(energy, (750, 10))

    def call_idle(self):
        self.idle.abrir()

    def close_idle(self):
        self.idle.fechar()

    def fechar(self):
        self.spriteGroup.remove(self)
        self.peso.spriteGroup.remove(self.peso)

        self.call_idle()

    def abrir(self):
        self.spriteGroup.add(self)
        self.peso.spriteGroup.add(self.peso)

        self.close_idle()

    def gui(self):
        self.basic_money()
        self.basic_energy()
        self.basic_hunger()
        self.basic_score()


class Menina2(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, peso, spriteGroup):
        super().__init__()
        self.sprites = [pygame.image.load('personagens/menina_02/M02_0001.png'),
                        pygame.image.load('personagens/menina_02/M02_0002.png'),
                        pygame.image.load('personagens/menina_02/M02_0003.png'),
                        pygame.image.load('personagens/menina_02/M02_0004.png'),
                        pygame.image.load('personagens/menina_02/M02_0005.png'),
                        pygame.image.load('personagens/menina_02/M02_0006.png'),
                        pygame.image.load('personagens/menina_02/M02_0007.png'),
                        pygame.image.load('personagens/menina_02/M02_0008.png'),
                        pygame.image.load('personagens/menina_02/M02_0009.png'),
                        pygame.image.load('personagens/menina_02/M02_0010.png'),
                        pygame.image.load('personagens/menina_02/M02_0011.png'),
                        pygame.image.load('personagens/menina_02/M02_0012.png'),
                        pygame.image.load('personagens/menina_02/M02_0013.png'),
                        pygame.image.load('personagens/menina_02/M02_0014.png'),
                        pygame.image.load('personagens/menina_02/M02_0015.png'),
                        pygame.image.load('personagens/menina_02/M02_0016.png'),
                        pygame.image.load('personagens/menina_02/M02_0017.png'),
                        pygame.image.load('personagens/menina_02/M02_0018.png'),
                        pygame.image.load('personagens/menina_02/M02_0019.png'),
                        pygame.image.load('personagens/menina_02/M02_0020.png'),
                        pygame.image.load('personagens/menina_02/M02_0021.png'),
                        pygame.image.load('personagens/menina_02/M02_0022.png'),
                        pygame.image.load('personagens/menina_02/M02_0023.png'),
                        pygame.image.load('personagens/menina_02/M02_0024.png'),
                        pygame.image.load('personagens/menina_02/M02_0025.png'),
                        pygame.image.load('personagens/menina_02/M02_0026.png'),
                        pygame.image.load('personagens/menina_02/M02_0027.png'),
                        pygame.image.load('personagens/menina_02/M02_0028.png'),
                        pygame.image.load('personagens/menina_02/M02_0029.png'),
                        pygame.image.load('personagens/menina_02/M02_0030.png'),
                        pygame.image.load('personagens/menina_02/M02_0031.png'),
                        pygame.image.load('personagens/menina_02/M02_0032.png'),
                        pygame.image.load('personagens/menina_02/M02_0033.png'),
                        pygame.image.load('personagens/menina_02/M02_0034.png'),
                        pygame.image.load('personagens/menina_02/M02_0035.png'),
                        pygame.image.load('personagens/menina_02/M02_0036.png'),
                        pygame.image.load('personagens/menina_02/M02_0037.png'),
                        pygame.image.load('personagens/menina_02/M02_0038.png'),
                        pygame.image.load('personagens/menina_02/M02_0039.png'),
                        pygame.image.load('personagens/menina_02/M02_0040.png'),
                        pygame.image.load('personagens/menina_02/M02_0041.png'),
                        pygame.image.load('personagens/menina_02/M02_0042.png'),
                        pygame.image.load('personagens/menina_02/M02_0043.png'),
                        pygame.image.load('personagens/menina_02/M02_0044.png'),
                        pygame.image.load('personagens/menina_02/M02_0045.png'),
                        pygame.image.load('personagens/menina_02/M02_0046.png'),
                        pygame.image.load('personagens/menina_02/M02_0047.png'),
                        pygame.image.load('personagens/menina_02/M02_0048.png'),
                        pygame.image.load('personagens/menina_02/M02_0049.png'),
                        pygame.image.load('personagens/menina_02/M02_0050.png'),
                        pygame.image.load('personagens/menina_02/M02_0051.png'),
                        pygame.image.load('personagens/menina_02/M02_0052.png'),
                        pygame.image.load('personagens/menina_02/M02_0053.png'),
                        pygame.image.load('personagens/menina_02/M02_0054.png'),
                        pygame.image.load('personagens/menina_02/M02_0055.png'),
                        pygame.image.load('personagens/menina_02/M02_0056.png'),
                        pygame.image.load('personagens/menina_02/M02_0057.png'),
                        pygame.image.load('personagens/menina_02/M02_0058.png'),
                        pygame.image.load('personagens/menina_02/M02_0059.png'),
                        pygame.image.load('personagens/menina_02/M02_0060.png'),
                        pygame.image.load('personagens/menina_02/M02_0061.png'),
                        pygame.image.load('personagens/menina_02/M02_0062.png'),
                        pygame.image.load('personagens/menina_02/M02_0063.png'),
                        pygame.image.load('personagens/menina_02/M02_0064.png'),
                        pygame.image.load('personagens/menina_02/M02_0065.png'),
                        pygame.image.load('personagens/menina_02/M02_0066.png'),
                        pygame.image.load('personagens/menina_02/M02_0067.png'),
                        pygame.image.load('personagens/menina_02/M02_0068.png'),
                        pygame.image.load('personagens/menina_02/M02_0069.png'),
                        pygame.image.load('personagens/menina_02/M02_0070.png'),
                        pygame.image.load('personagens/menina_02/M02_0071.png'),
                        pygame.image.load('personagens/menina_02/M02_0072.png'),
                        pygame.image.load('personagens/menina_02/M02_0073.png'),
                        pygame.image.load('personagens/menina_02/M02_0074.png'),
                        pygame.image.load('personagens/menina_02/M02_0075.png'),
                        pygame.image.load('personagens/menina_02/M02_0076.png'),
                        pygame.image.load('personagens/menina_02/M02_0077.png'),
                        pygame.image.load('personagens/menina_02/M02_0078.png'),
                        pygame.image.load('personagens/menina_02/M02_0079.png'),
                        pygame.image.load('personagens/menina_02/M02_0080.png'),
                        pygame.image.load('personagens/menina_02/M02_0081.png'),
                        pygame.image.load('personagens/menina_02/M02_0082.png'),
                        pygame.image.load('personagens/menina_02/M02_0083.png'),
                        pygame.image.load('personagens/menina_02/M02_0084.png'),
                        pygame.image.load('personagens/menina_02/M02_0085.png')]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.spriteGroup = spriteGroup

        if peso == 1:
            self.peso = Peso1((pos_x + 159), (pos_y + 174), spriteGroup)
        if peso == 2:
            self.peso = Peso2((pos_x + 159), (pos_y + 174), spriteGroup)
        if peso == 3:
            self.peso = Peso3((pos_x + 159), (pos_y + 174), spriteGroup)

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, (pos_y + 12)]

    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

    def fechar(self):
        self.spriteGroup.remove(self)
        self.peso.spriteGroup.remove(self.peso)

    def abrir(self):
        self.spriteGroup.add(self)
        self.peso.spriteGroup.add(self.peso)


class Menina3(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, peso, spriteGroup):
        super().__init__()
        self.sprites = [pygame.image.load('personagens/menina_03/M03_0001.png'),
                        pygame.image.load('personagens/menina_03/M03_0002.png'),
                        pygame.image.load('personagens/menina_03/M03_0003.png'),
                        pygame.image.load('personagens/menina_03/M03_0004.png'),
                        pygame.image.load('personagens/menina_03/M03_0005.png'),
                        pygame.image.load('personagens/menina_03/M03_0006.png'),
                        pygame.image.load('personagens/menina_03/M03_0007.png'),
                        pygame.image.load('personagens/menina_03/M03_0008.png'),
                        pygame.image.load('personagens/menina_03/M03_0009.png'),
                        pygame.image.load('personagens/menina_03/M03_0010.png'),
                        pygame.image.load('personagens/menina_03/M03_0011.png'),
                        pygame.image.load('personagens/menina_03/M03_0012.png'),
                        pygame.image.load('personagens/menina_03/M03_0013.png'),
                        pygame.image.load('personagens/menina_03/M03_0014.png'),
                        pygame.image.load('personagens/menina_03/M03_0015.png'),
                        pygame.image.load('personagens/menina_03/M03_0016.png'),
                        pygame.image.load('personagens/menina_03/M03_0017.png'),
                        pygame.image.load('personagens/menina_03/M03_0018.png'),
                        pygame.image.load('personagens/menina_03/M03_0019.png'),
                        pygame.image.load('personagens/menina_03/M03_0020.png'),
                        pygame.image.load('personagens/menina_03/M03_0021.png'),
                        pygame.image.load('personagens/menina_03/M03_0022.png'),
                        pygame.image.load('personagens/menina_03/M03_0023.png'),
                        pygame.image.load('personagens/menina_03/M03_0024.png'),
                        pygame.image.load('personagens/menina_03/M03_0025.png'),
                        pygame.image.load('personagens/menina_03/M03_0026.png'),
                        pygame.image.load('personagens/menina_03/M03_0027.png'),
                        pygame.image.load('personagens/menina_03/M03_0028.png'),
                        pygame.image.load('personagens/menina_03/M03_0029.png'),
                        pygame.image.load('personagens/menina_03/M03_0030.png'),
                        pygame.image.load('personagens/menina_03/M03_0031.png'),
                        pygame.image.load('personagens/menina_03/M03_0032.png'),
                        pygame.image.load('personagens/menina_03/M03_0033.png'),
                        pygame.image.load('personagens/menina_03/M03_0034.png'),
                        pygame.image.load('personagens/menina_03/M03_0035.png'),
                        pygame.image.load('personagens/menina_03/M03_0036.png'),
                        pygame.image.load('personagens/menina_03/M03_0037.png'),
                        pygame.image.load('personagens/menina_03/M03_0038.png'),
                        pygame.image.load('personagens/menina_03/M03_0039.png'),
                        pygame.image.load('personagens/menina_03/M03_0040.png'),
                        pygame.image.load('personagens/menina_03/M03_0041.png'),
                        pygame.image.load('personagens/menina_03/M03_0042.png'),
                        pygame.image.load('personagens/menina_03/M03_0043.png'),
                        pygame.image.load('personagens/menina_03/M03_0044.png'),
                        pygame.image.load('personagens/menina_03/M03_0045.png'),
                        pygame.image.load('personagens/menina_03/M03_0046.png'),
                        pygame.image.load('personagens/menina_03/M03_0047.png'),
                        pygame.image.load('personagens/menina_03/M03_0048.png'),
                        pygame.image.load('personagens/menina_03/M03_0049.png'),
                        pygame.image.load('personagens/menina_03/M03_0050.png'),
                        pygame.image.load('personagens/menina_03/M03_0051.png'),
                        pygame.image.load('personagens/menina_03/M03_0052.png'),
                        pygame.image.load('personagens/menina_03/M03_0053.png'),
                        pygame.image.load('personagens/menina_03/M03_0054.png'),
                        pygame.image.load('personagens/menina_03/M03_0055.png'),
                        pygame.image.load('personagens/menina_03/M03_0056.png'),
                        pygame.image.load('personagens/menina_03/M03_0057.png'),
                        pygame.image.load('personagens/menina_03/M03_0058.png'),
                        pygame.image.load('personagens/menina_03/M03_0059.png'),
                        pygame.image.load('personagens/menina_03/M03_0060.png'),
                        pygame.image.load('personagens/menina_03/M03_0061.png'),
                        pygame.image.load('personagens/menina_03/M03_0062.png'),
                        pygame.image.load('personagens/menina_03/M03_0063.png'),
                        pygame.image.load('personagens/menina_03/M03_0064.png'),
                        pygame.image.load('personagens/menina_03/M03_0065.png'),
                        pygame.image.load('personagens/menina_03/M03_0066.png'),
                        pygame.image.load('personagens/menina_03/M03_0067.png'),
                        pygame.image.load('personagens/menina_03/M03_0068.png'),
                        pygame.image.load('personagens/menina_03/M03_0069.png'),
                        pygame.image.load('personagens/menina_03/M03_0070.png'),
                        pygame.image.load('personagens/menina_03/M03_0071.png'),
                        pygame.image.load('personagens/menina_03/M03_0072.png'),
                        pygame.image.load('personagens/menina_03/M03_0073.png'),
                        pygame.image.load('personagens/menina_03/M03_0074.png'),
                        pygame.image.load('personagens/menina_03/M03_0075.png'),
                        pygame.image.load('personagens/menina_03/M03_0076.png'),
                        pygame.image.load('personagens/menina_03/M03_0077.png'),
                        pygame.image.load('personagens/menina_03/M03_0078.png'),
                        pygame.image.load('personagens/menina_03/M03_0079.png'),
                        pygame.image.load('personagens/menina_03/M03_0080.png'),
                        pygame.image.load('personagens/menina_03/M03_0081.png'),
                        pygame.image.load('personagens/menina_03/M03_0082.png'),
                        pygame.image.load('personagens/menina_03/M03_0083.png'),
                        pygame.image.load('personagens/menina_03/M03_0084.png'),
                        pygame.image.load('personagens/menina_03/M03_0085.png')]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.spriteGroup = spriteGroup

        if peso == 1:
            self.peso = Peso1((pos_x + 159), (pos_y + 174), spriteGroup)
        if peso == 2:
            self.peso = Peso2((pos_x + 159), (pos_y + 174), spriteGroup)
        if peso == 3:
            self.peso = Peso3((pos_x + 159), (pos_y + 174), spriteGroup)

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y - 17]

    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

    def fechar(self):
        self.spriteGroup.remove(self)
        self.peso.spriteGroup.remove(self.peso)

    def abrir(self):
        self.spriteGroup.add(self)
        self.peso.spriteGroup.add(self.peso)


class Menina4(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, peso, spriteGroup):
        super().__init__()
        self.sprites = [pygame.image.load('personagens/menina_04/M04_0001.png'),
                        pygame.image.load('personagens/menina_04/M04_0002.png'),
                        pygame.image.load('personagens/menina_04/M04_0003.png'),
                        pygame.image.load('personagens/menina_04/M04_0004.png'),
                        pygame.image.load('personagens/menina_04/M04_0005.png'),
                        pygame.image.load('personagens/menina_04/M04_0006.png'),
                        pygame.image.load('personagens/menina_04/M04_0007.png'),
                        pygame.image.load('personagens/menina_04/M04_0008.png'),
                        pygame.image.load('personagens/menina_04/M04_0009.png'),
                        pygame.image.load('personagens/menina_04/M04_0010.png'),
                        pygame.image.load('personagens/menina_04/M04_0011.png'),
                        pygame.image.load('personagens/menina_04/M04_0012.png'),
                        pygame.image.load('personagens/menina_04/M04_0013.png'),
                        pygame.image.load('personagens/menina_04/M04_0014.png'),
                        pygame.image.load('personagens/menina_04/M04_0015.png'),
                        pygame.image.load('personagens/menina_04/M04_0016.png'),
                        pygame.image.load('personagens/menina_04/M04_0017.png'),
                        pygame.image.load('personagens/menina_04/M04_0018.png'),
                        pygame.image.load('personagens/menina_04/M04_0019.png'),
                        pygame.image.load('personagens/menina_04/M04_0020.png'),
                        pygame.image.load('personagens/menina_04/M04_0021.png'),
                        pygame.image.load('personagens/menina_04/M04_0022.png'),
                        pygame.image.load('personagens/menina_04/M04_0023.png'),
                        pygame.image.load('personagens/menina_04/M04_0024.png'),
                        pygame.image.load('personagens/menina_04/M04_0025.png'),
                        pygame.image.load('personagens/menina_04/M04_0026.png'),
                        pygame.image.load('personagens/menina_04/M04_0027.png'),
                        pygame.image.load('personagens/menina_04/M04_0028.png'),
                        pygame.image.load('personagens/menina_04/M04_0029.png'),
                        pygame.image.load('personagens/menina_04/M04_0030.png'),
                        pygame.image.load('personagens/menina_04/M04_0031.png'),
                        pygame.image.load('personagens/menina_04/M04_0032.png'),
                        pygame.image.load('personagens/menina_04/M04_0033.png'),
                        pygame.image.load('personagens/menina_04/M04_0034.png'),
                        pygame.image.load('personagens/menina_04/M04_0035.png'),
                        pygame.image.load('personagens/menina_04/M04_0036.png'),
                        pygame.image.load('personagens/menina_04/M04_0037.png'),
                        pygame.image.load('personagens/menina_04/M04_0038.png'),
                        pygame.image.load('personagens/menina_04/M04_0039.png'),
                        pygame.image.load('personagens/menina_04/M04_0040.png'),
                        pygame.image.load('personagens/menina_04/M04_0041.png'),
                        pygame.image.load('personagens/menina_04/M04_0042.png'),
                        pygame.image.load('personagens/menina_04/M04_0043.png'),
                        pygame.image.load('personagens/menina_04/M04_0044.png'),
                        pygame.image.load('personagens/menina_04/M04_0045.png'),
                        pygame.image.load('personagens/menina_04/M04_0046.png'),
                        pygame.image.load('personagens/menina_04/M04_0047.png'),
                        pygame.image.load('personagens/menina_04/M04_0048.png'),
                        pygame.image.load('personagens/menina_04/M04_0049.png'),
                        pygame.image.load('personagens/menina_04/M04_0050.png'),
                        pygame.image.load('personagens/menina_04/M04_0051.png'),
                        pygame.image.load('personagens/menina_04/M04_0052.png'),
                        pygame.image.load('personagens/menina_04/M04_0053.png'),
                        pygame.image.load('personagens/menina_04/M04_0054.png'),
                        pygame.image.load('personagens/menina_04/M04_0055.png'),
                        pygame.image.load('personagens/menina_04/M04_0056.png'),
                        pygame.image.load('personagens/menina_04/M04_0057.png'),
                        pygame.image.load('personagens/menina_04/M04_0058.png'),
                        pygame.image.load('personagens/menina_04/M04_0059.png'),
                        pygame.image.load('personagens/menina_04/M04_0060.png'),
                        pygame.image.load('personagens/menina_04/M04_0061.png'),
                        pygame.image.load('personagens/menina_04/M04_0062.png'),
                        pygame.image.load('personagens/menina_04/M04_0063.png'),
                        pygame.image.load('personagens/menina_04/M04_0064.png'),
                        pygame.image.load('personagens/menina_04/M04_0065.png'),
                        pygame.image.load('personagens/menina_04/M04_0066.png'),
                        pygame.image.load('personagens/menina_04/M04_0067.png'),
                        pygame.image.load('personagens/menina_04/M04_0068.png'),
                        pygame.image.load('personagens/menina_04/M04_0069.png'),
                        pygame.image.load('personagens/menina_04/M04_0070.png'),
                        pygame.image.load('personagens/menina_04/M04_0071.png'),
                        pygame.image.load('personagens/menina_04/M04_0072.png'),
                        pygame.image.load('personagens/menina_04/M04_0073.png'),
                        pygame.image.load('personagens/menina_04/M04_0074.png'),
                        pygame.image.load('personagens/menina_04/M04_0075.png'),
                        pygame.image.load('personagens/menina_04/M04_0076.png'),
                        pygame.image.load('personagens/menina_04/M04_0077.png'),
                        pygame.image.load('personagens/menina_04/M04_0078.png'),
                        pygame.image.load('personagens/menina_04/M04_0079.png'),
                        pygame.image.load('personagens/menina_04/M04_0080.png'),
                        pygame.image.load('personagens/menina_04/M04_0081.png'),
                        pygame.image.load('personagens/menina_04/M04_0082.png'),
                        pygame.image.load('personagens/menina_04/M04_0083.png'),
                        pygame.image.load('personagens/menina_04/M04_0084.png'),
                        pygame.image.load('personagens/menina_04/M04_0085.png')]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.spriteGroup = spriteGroup

        if peso == 1:
            self.peso = Peso1((pos_x + 159), (pos_y + 174), spriteGroup)
        if peso == 2:
            self.peso = Peso2((pos_x + 159), (pos_y + 174), spriteGroup)
        if peso == 3:
            self.peso = Peso3((pos_x + 159), (pos_y + 174), spriteGroup)

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y + 12]

    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

    def fechar(self):
        self.spriteGroup.remove(self)
        self.peso.spriteGroup.remove(self.peso)

    def abrir(self):
        self.spriteGroup.add(self)
        self.peso.spriteGroup.add(self.peso)


class Loja_fundo(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, spriteGroup):
        pygame.sprite.Sprite.__init__(self)
        self.image = fundo_transparente
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.spriteGroup = spriteGroup
        self.open = False
        self.hamburguer = Items_loja(25, 200, comida_hamburguer, v_hamburguer, spriteGroup)
        self.refri = Items_loja(180, 200, comida_refri, v_refri, spriteGroup)
        self.saudavel = Items_loja(25, 350, comida_saudavel, v_saudavel, spriteGroup)
        self.peru = Items_loja(180, 350, comida_peru, v_peru, spriteGroup)
        self.whey = Items_loja(110, 470, comida_whey, v_whey, spriteGroup)
        self.title = Texto('LOJA', fonte, (255, 255, 255), fundo_transparente, 146, 10)
        self.botao_fechar = Botao_fechar_loja(315, 162, botao_fechar_loja, spriteGroup)

    def fechar(self):
        self.spriteGroup.remove(self)
        self.open = False
        self.close_icones()

    def abrir(self):
        self.spriteGroup.add(self)
        self.open = True
        self.call_icones()

    def update(self):
        self.title.imprimir()

    def call_icones(self):
        self.hamburguer.abrir()
        self.refri.abrir()
        self.saudavel.abrir()
        self.peru.abrir()
        self.whey.abrir()
        self.botao_fechar.abrir()

    def close_icones(self):
        self.hamburguer.fechar()
        self.refri.fechar()
        self.saudavel.fechar()
        self.peru.fechar()
        self.whey.fechar()
        self.botao_fechar.fechar()


class Items_loja(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, img, preco, spriteGroup):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.preco = preco
        self.spriteGroup = spriteGroup
        self.texto_preco = Texto(('$' + str(self.preco)), fonte_loja, MONEY, fundo_transparente, (self.rect.x + 15), (self.rect.y - 60))

    def update(self):
        self.texto_preco.imprimir()

    def abrir(self):
        self.spriteGroup.add(self)

    def fechar(self):
        self.spriteGroup.remove(self)


class Botao_fechar_loja(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, img, spriteGroup):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.spriteGroup = spriteGroup

    def abrir(self):
        self.spriteGroup.add(self)

    def fechar(self):
        self.spriteGroup.remove(self)


class Loja(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, spriteGroup):
        pygame.sprite.Sprite.__init__(self)
        self.spriteGroup = spriteGroup
        self.loja_fundo = Loja_fundo(pos_x, pos_y, spriteGroup)
        self.texto = Texto('LOJA', fonte, (255, 255, 255), screen, 10, 105)

    def update(self):
        self.texto.imprimir()


#--------[TUTORIAL]----------#

def Tutorial_hunger(pos_x, pos_y):
    pygame.draw.rect(screen, (236, 124, 48), (pos_x, pos_y, 150, 25))
    pygame.draw.rect(screen, (255, 255, 255), (pos_x, pos_y, 150, 25), 4)
    screen.blit(hunger, (pos_x-20, pos_y))

def Tutorial_energy(pos_x, pos_y):
    pygame.draw.rect(screen, (255, 255, 0), (pos_x, pos_y, 150, 25))
    pygame.draw.rect(screen, (255, 255, 255), (pos_x, pos_y, 150, 25), 4)
    screen.blit(energy, (pos_x-20, pos_y-10))

def Tutorial_money(player_teste, pos_x, pos_y):
    imprimir(str(player_teste.current_money), dindin, (6, 152, 0), screen, pos_x, pos_y)
    screen.blit(dolar, (pos_x-50, pos_y-5))

def Tutorial_score(player_teste, pos_x, pos_y):
    imprimir("SCORE: " + str(player_teste.score), fonte, (0, 0, 0), screen, pos_x, pos_y)

class Tutorial_barra(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, spriteGroup):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((600, 50))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.spriteGroup = spriteGroup

        self.divisao = (600 - comprimento) / 2
        self.acerto = Acerto((pos_x + self.divisao), pos_y, spriteGroup)

        self.ponteiro = Ponteiro(pos_x, pos_y, spriteGroup)

    def fechar(self):
        self.spriteGroup.remove(self)
        self.acerto.fechar()
        self.ponteiro.fechar()

    def abrir(self):
        self.spriteGroup.add(self)
        self.acerto.abrir()
        self.ponteiro.abrir()

    def update(self):
        self.score()

    def score(self):
        screen.blit(fundo_trans, (70, 290))
        imprimir("Acertos", dindin, (6, 152, 0), screen, 95, 300)
        imprimir(str(0), dindin, (6, 152, 0), screen, 160, 340)
        imprimir("Erros", dindin, RED, screen, 325, 300)
        imprimir(str(0), dindin, RED, screen, 370, 340)

# -------------------------#


click = False


def gui():
    # --------GAME LOOP-------#
    while True:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(title, (-470, 50))
        screen.blit(pygame.transform.scale(fundo_tutorial, (200, 180)), (660, 210))
        imprimir("TOP 5", dindin, (0, 0, 0), screen, 675, 220)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        b_mute = pygame.Rect(925, 15, 50, 50)
        b_jogar = pygame.Rect(340, 250, 150, 50)
        b_como_jogar = pygame.Rect(340, 325, 150, 50)
        b_sair = pygame.Rect(340, 400, 150, 50)

        # Sprites Ranking
        recordes = trofeu3
        posy = 0
        # Ranking Loop
        scores = open("leaderboard.txt")
        conteudo = scores.readlines()
        screen.blit(recordes, (780, 190))
        for i in conteudo:
            i = i.strip("\n")
            x = fonte.render(i, 1, (0, 0, 0))
            screen.blit(x, (670, (posy+280)))
            posy += 22

        if b_mute.collidepoint((mouse_x, mouse_y)):
            if click:
                mute(som_on)
        if b_jogar.collidepoint((mouse_x, mouse_y)):
            if click:
                jogo()
        if b_como_jogar.collidepoint((mouse_x, mouse_y)):
            if click:
                como_jogar()
        if b_sair.collidepoint((mouse_x, mouse_y)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, (0, 0, 0), b_mute, border_radius=100)
        pygame.draw.rect(screen, (0, 0, 0), b_jogar, border_radius=15)
        pygame.draw.rect(screen, (0, 0, 0), b_como_jogar, border_radius=15)
        pygame.draw.rect(screen, (0, 0, 0), b_sair, border_radius=15)

        volume.set_alpha(volume_alpha)
        screen.blit(volume, (709, -200))
        mutado.set_alpha(mutado_alpha)
        screen.blit(mutado, (725, -185))

        t_jogar = Texto('Jogar', fonte, (255, 255, 255), screen, 385, 265)
        t_como_jogar = Texto('Como Jogar', fonte, (255, 255, 255), screen, 355, 340)
        t_sair = Texto('Sair', fonte, (255, 255, 255), screen, 393, 415)

        t_jogar.imprimir()
        t_como_jogar.imprimir()
        t_sair.imprimir()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)


def mute(status):
    global som_on
    global volume_alpha
    global mutado_alpha

    if status == True:
        pygame.mixer.music.set_volume(0)
        mutado_alpha = 1000
        volume_alpha = 0
        som_on = False
    elif status == False:
        pygame.mixer.music.set_volume(100)
        mutado_alpha = 0
        volume_alpha = 1000
        som_on = True


def como_jogar():
    como_jogar_sprites = pygame.sprite.Group()
    player_teste = Player(0, 0, 1, como_jogar_sprites)
    barra = Tutorial_barra(70, 500, como_jogar_sprites)
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background2, (0, 0))
        screen.blit(pygame.transform.scale(fundo_tutorial, (900, 525)), (50, 50))

        texto_cama = pygame.Rect(180, 60, 300, 100)
        texto_halter = pygame.Rect(180, 180, 300, 100)
        texto_loja = pygame.Rect(620, 60, 300, 100)
        texto_podio = pygame.Rect(620, 180, 300, 100)
        texto_barra = pygame.Rect(70, 400, 400, 90)
        texto_status = pygame.Rect(675, 300, 255, 250)

        pygame.draw.rect(screen, (92, 168, 165), texto_cama, border_radius=15)
        imprimir("Fernanda também se cansa,", fonte, (0, 0, 0), screen, 190, 75)
        imprimir("use a cama para dar", fonte, (0, 0, 0), screen, 190, 95)
        imprimir("a ela seu devido descanço", fonte, (0, 0, 0), screen, 190, 115)
        pygame.draw.rect(screen, (92, 168, 165), texto_halter, border_radius=15)
        imprimir("Para melhorar seu desem-", fonte, (0, 0, 0), screen, 190, 195)
        imprimir("penho nos treinamentos ", fonte, (0, 0, 0), screen, 190, 215)
        imprimir("é necessario treinar.", fonte, (0, 0, 0), screen, 190, 235)
        pygame.draw.rect(screen, (92, 168, 165), texto_loja, border_radius=15)
        imprimir("Para o reabastecimento da ", fonte, (0, 0, 0), screen, 630, 75)
        imprimir("barra de fome será neces-", fonte, (0, 0, 0), screen, 630, 95)
        imprimir("sario comprar alimentos", fonte, (0, 0, 0), screen, 630, 115)
        imprimir("na loja.", fonte, (0, 0, 0), screen, 630, 135)
        pygame.draw.rect(screen, (92, 168, 165), texto_podio, border_radius=15)
        imprimir("Este é o caminho para ", fonte, (0, 0, 0), screen, 630, 195)
        imprimir("as competições que ", fonte, (0, 0, 0), screen, 630, 215)
        imprimir("ficará disponivel em", fonte, (0, 0, 0), screen, 630, 235)
        imprimir("seus dias", fonte, (0, 0, 0), screen, 630, 255)
        pygame.draw.rect(screen, (92, 168, 165), texto_barra, border_radius=15)
        imprimir("Essa é a barra de treino. Acerte o pon-", fonte, (0, 0, 0), screen, 80, 410)
        imprimir("teiro com a tecla “SPACE” na parte", fonte, (0, 0, 0), screen, 80, 430)
        imprimir("verde para ganhar acertos, com 10", fonte, (0, 0, 0), screen, 80, 450)
        imprimir("acertos o treino termina.", fonte, (0, 0, 0), screen, 80, 470)
        pygame.draw.rect(screen, (92, 168, 165), texto_status, border_radius=15)
        imprimir("Conforme você treina", fonte, (0, 0, 0), screen, 685, 315)
        imprimir("Fernanda se cansa, ", fonte, (0, 0, 0), screen, 685, 335)
        imprimir("não faça mais oque.", fonte, (0, 0, 0), screen, 685, 355)
        imprimir("você pode", fonte, (0, 0, 0), screen, 685, 375)
        imprimir("Fernanda também sente", fonte, (0, 0, 0), screen, 685, 395)
        imprimir("fome, mas preste", fonte, (0, 0, 0), screen, 685, 415)
        imprimir("atenção em sua dieta!", fonte, (0, 0, 0), screen, 685, 435)
        imprimir("Fique atento com seu ", fonte, (0, 0, 0), screen, 685, 455)
        imprimir("dinheiro, nem sempre", fonte, (0, 0, 0), screen, 685, 475)
        imprimir("compensa pegar o", fonte, (0, 0, 0), screen, 685, 495)
        imprimir("mais caro", fonte, (0, 0, 0), screen, 685, 515)

        imprimir("Como Jogar", dindin, (0, 0, 0,), screen, 380, 10)
        imprimir("DIA " + str(dia), txt_dia, (0, 0, 0), screen, 500, 460)

        Tutorial_energy(500, 300)
        Tutorial_hunger(500, 350)
        Tutorial_money(player_teste, 550, 400)
        Tutorial_score(player_teste, 500, 440)
        screen.blit(cama, (70, 40))
        screen.blit(halter, (70, 180))
        screen.blit(loja, (500, 60))
        screen.blit(podio, (500, 160))
        barra.abrir()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        como_jogar_sprites.draw(screen)
        como_jogar_sprites.update()
        pygame.display.update()
        clock.tick(60)


def competir():
    global click, trofeu, peso, progressao, sec
    SECOND = pygame.USEREVENT
    pygame.time.set_timer(SECOND, sec)
    competicao_sprite = pygame.sprite.Group()
    barra = Barra(200, 50, competicao_sprite)
    player = Player(-55, 20, peso, competicao_sprite)
    if progressao == 0:
        trofeu = trofeu1
        menina = Menina4(370, 20, peso, competicao_sprite)
    if progressao == 1:
        trofeu = trofeu2
        menina = Menina3(370, 20, peso, competicao_sprite)
        sec -= 200
    if progressao == 2:
        trofeu = trofeu3
        menina = Menina2(370, 20, peso, competicao_sprite)
        sec -= 200
    somWin = pygame.mixer.Sound('mixkit-video-game-win-2016.wav')
    running = True
    barra.scores = False
    while running:
        global energia, dia, comprimento, hit
        screen.fill((0, 0, 0))
        screen.blit(background2, (0, 0))
        background2.blit(fundo_banner, (15, 180))
        background2.blit(fundo_banner, (805, 180))
        screen.blit(trofeu, (455, 400))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        menina.abrir()
        player.abrir()
        barra.abrir()
        player.basic_score()

        if barra.acertos == 10:
            peso += 1
            progressao += 1
            dia += 1
            if progressao == 1:
                player.set_salario(100)
            if progressao == 2:
                player.set_salario(150)
            running = False
            somWin.play()
            jogo()

        if barra.rival == 10:
            running = False

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if barra.open:
                        barra.acertar()
                        if barra.hittable and hit == False:
                            player.get_score(100)
                            hit = True
                        if not barra.hittable:
                            player.lost_score(100)
            if event.type == SECOND:
                barra.dado()

        click = False
        competicao_sprite.draw(screen)
        competicao_sprite.update()
        pygame.display.update()
        clock.tick(60)


def vitoria():
    global energia, dia, comprimento, multiplicador, hit, progressao, salario, velocidade, peso, sec, trofeu, dinheiro, fome, score
    # Loop
    nome = ""
    pts = dindin.render(str(score), 1, (0, 0, 0))
    while True:
        letras = dindin.render(str(nome), 1, (0, 0, 0))
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(pygame.transform.scale(fundo_tutorial, (450, 400)), (50, 50))
        imprimir("PARABÉNS VOCÊ VENCEU!!", txt_win, (0, 0, 0), screen, 60, 60)
        imprimir("Sua pontuação foi:", txt_win, (0, 0, 0), screen, 80, 110)
        screen.blit(pts, (180, 170))
        imprimir("Digite seu nome:", txt_win, (0, 0, 0), screen, 80, 240)
        screen.blit(letras, (100, 280))
        imprimir("Prescione Enter", txt_win, (0, 0, 0), screen, 240, 390)
        screen.blit(trofeu1, (540, 290))
        screen.blit(trofeu2, (540, 168))
        screen.blit(trofeu3, (540, 78))
        screen.blit(idle, ((424 + 211), (59 + 166)))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and len(nome) < 11:
                    nome += "a"
                if event.key == pygame.K_b and len(nome) < 11:
                    nome += "b"
                if event.key == pygame.K_c and len(nome) < 11:
                    nome += "c"
                if event.key == pygame.K_d and len(nome) < 11:
                    nome += "d"
                if event.key == pygame.K_e and len(nome) < 11:
                    nome += "e"
                if event.key == pygame.K_f and len(nome) < 11:
                    nome += "f"
                if event.key == pygame.K_g and len(nome) < 11:
                    nome += "g"
                if event.key == pygame.K_h and len(nome) < 11:
                    nome += "h"
                if event.key == pygame.K_i and len(nome) < 11:
                    nome += "i"
                if event.key == pygame.K_j and len(nome) < 11:
                    nome += "j"
                if event.key == pygame.K_k and len(nome) < 11:
                    nome += "k"
                if event.key == pygame.K_l and len(nome) < 11:
                    nome += "l"
                if event.key == pygame.K_m and len(nome) < 11:
                    nome += "m"
                if event.key == pygame.K_n and len(nome) < 11:
                    nome += "n"
                if event.key == pygame.K_o and len(nome) < 11:
                    nome += "o"
                if event.key == pygame.K_p and len(nome) < 11:
                    nome += "p"
                if event.key == pygame.K_q and len(nome) < 11:
                    nome += "q"
                if event.key == pygame.K_r and len(nome) < 11:
                    nome += "r"
                if event.key == pygame.K_s and len(nome) < 11:
                    nome += "s"
                if event.key == pygame.K_t and len(nome) < 11:
                    nome += "t"
                if event.key == pygame.K_u and len(nome) < 11:
                    nome += "u"
                if event.key == pygame.K_v and len(nome) < 11:
                    nome += "v"
                if event.key == pygame.K_w and len(nome) < 11:
                    nome += "w"
                if event.key == pygame.K_x and len(nome) < 11:
                    nome += "x"
                if event.key == pygame.K_y and len(nome) < 11:
                    nome += "y"
                if event.key == pygame.K_z and len(nome) < 11:
                    nome += "z"
                if event.key == pygame.K_BACKSPACE:
                    nome = ""
                if event.key == pygame.K_RETURN:
                    if nome == "":
                        nome = "semnome"
                    ranking = open("leaderboard.txt", "r+")
                    conteudo = ranking.readlines()
                    for i in range(len(conteudo)):
                        recorde = conteudo[i].split(" ")
                        if score > int(recorde[1]):
                            conteudo.insert(i, nome + " " + str(score) + "\n")
                            break
                    ranking.truncate(0)
                    ranking.seek(0)
                    for i in range(5):
                        ranking.write(conteudo[i])
                    ranking.close()
                    salario = 50
                    multiplicador = 1
                    score = 0
                    sec = 1500
                    trofeu = 0
                    peso = 1
                    comprimento = 100
                    velocidade = 5
                    dia = 0
                    progressao = 0
                    dinheiro = 0
                    fome = 150
                    energia = 150
                    gui()


def jogo():
    global click, peso
    hist = True
    jogo_sprites = pygame.sprite.Group()
    loja1 = Loja(0, 150, jogo_sprites)
    player1 = Player(424, 59, peso, jogo_sprites)
    barra = Barra(25, 500, jogo_sprites)
    player1.call_idle()
    somComer = pygame.mixer.Sound('mixkit-chewing-something-crunchy-2244.wav')
    somBeber = pygame.mixer.Sound('mixkit-swallowing-a-water-drink-in-the-throat-150.wav')
    somMetal = pygame.mixer.Sound('mixkit-pull-and-drop-gym-machine-2115.wav')
    somMetal2 = pygame.mixer.Sound('mixkit-metal-gym-plate-2116.wav')
    somPapel = pygame.mixer.Sound('mixkit-pile-of-paper-trash-2381.wav')
    somCama = pygame.mixer.Sound('mixkit-male-sleep-breathe-2236.wav')
    somPodi = pygame.mixer.Sound('mixkit-audience-light-applause-354.wav')
    # game loop
    running = True
    while running:
        global energia, dia, comprimento, multiplicador, hit, progressao
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        mouse_x, mouse_y = pygame.mouse.get_pos()

        imprimir("DIA " + str(dia), txt_dia, (0, 0, 0), screen, 0, 0)
        b_cama = screen.blit(cama, (10, 10))
        b_loja = screen.blit(loja, (120, 10))
        b_treino = screen.blit(halter, (230, 10))
        b_competicao = screen.blit(podio, (340, 10))

        if progressao == 1:
            screen.blit(trofeu1, (540, 290))
        if progressao == 2:
            screen.blit(trofeu1, (540, 290))
            screen.blit(trofeu2, (540, 168))
        if progressao == 3:
            vitoria()

        if hist:
            screen.blit(pygame.transform.scale(fundo_tutorial, (600, 450)), (50, 150))
            imprimir("HISTÓRIA", dindin, (0, 0, 0), screen, 250, 170)
            if progressao == 0:
                hist1()
            if progressao == 1:
                hist2()
            if progressao == 2:
                hist3()

        if b_cama.collidepoint((mouse_x, mouse_y)):
            if click:
                hist = False
                if dia != 5 and dia != 10 and dia != 15:
                    player1.fechar()
                    barra.fechar()
                    player1.current_energy = 200
                    dia += 1
                    player1.get_money()
                    somCama.play()

        if not loja1.loja_fundo.open:
            if b_loja.collidepoint((mouse_x, mouse_y)) and click:
                hist = False
                loja1.loja_fundo.abrir()
                player1.fechar()
                barra.fechar()
                somPapel.play()

        if loja1.loja_fundo.open:
            b_fechar_loja = loja1.loja_fundo.botao_fechar.rect
            b_comprar_hamburguer = loja1.loja_fundo.hamburguer.rect
            b_comprar_refri = loja1.loja_fundo.refri.rect
            b_comprar_saudavel = loja1.loja_fundo.saudavel.rect
            b_comprar_peru = loja1.loja_fundo.peru.rect
            b_comprar_whey = loja1.loja_fundo.whey.rect

            if b_fechar_loja.collidepoint((mouse_x, mouse_y)) and click:
                loja1.loja_fundo.fechar()
                player1.fechar()
                barra.fechar()

            if b_comprar_hamburguer.collidepoint((mouse_x, mouse_y)) and click:
                if v_hamburguer <= dinheiro:
                    player1.lost_money(v_hamburguer)
                    player1.get_food(70)
                    player1.lost_score(1)
                    barra.acerto.engorda()
                    barra.acerto.engorda()
                    somComer.play()

            if b_comprar_refri.collidepoint((mouse_x, mouse_y)) and click:
                if v_refri <= dinheiro:
                    player1.lost_money(v_refri)
                    player1.get_food(20)
                    player1.lost_score(1)
                    barra.acerto.engorda()
                    somBeber.play()

            if b_comprar_saudavel.collidepoint((mouse_x, mouse_y)) and click:
                if v_saudavel <= dinheiro:
                    player1.lost_money(v_saudavel)
                    player1.get_food(20)
                    player1.get_score(1)
                    barra.acerto.emagrece()
                    somComer.play()

            if b_comprar_peru.collidepoint((mouse_x, mouse_y)) and click:
                if v_peru <= dinheiro:
                    player1.lost_money(v_peru)
                    player1.get_food(70)
                    player1.get_score(1)
                    barra.acerto.emagrece()
                    barra.acerto.emagrece()
                    somComer.play()

            if b_comprar_whey.collidepoint((mouse_x, mouse_y)) and click:
                if v_whey <= dinheiro:
                    player1.lost_money(v_whey)
                    multiplicador += 1

        if b_treino.collidepoint((mouse_x, mouse_y)):
            if click:
                hist = False
                loja1.loja_fundo.fechar()
                if player1.current_energy >= 25 and player1.current_hunger >= 50:
                    player1.abrir()
                    barra.abrir()
                    somMetal2.play()

        if b_competicao.collidepoint((mouse_x, mouse_y)):
            if click:
                hist = False
                if dia == 5 or dia == 10 or dia == 15:
                    running = False
                    somPodi.play()
                    competir()

        click = False
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_SPACE:
                    if barra.open:
                        barra.acertar()
                        if barra.hittable and hit == False:
                            player1.get_score(10)
                            hit = True
                        if not barra.hittable:
                            player1.lost_score(10)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if barra.acertos == 10:
            barra.fechar()
            player1.fechar()
            barra.acertos = 0
            barra.erros = 0
            barra.ponteiro.treinar()
            player1.get_tired(40)
            player1.get_train(50)
            somMetal.play()
            barra.hittable = False

        if barra.erros == 10:
            barra.fechar()
            player1.fechar()
            barra.acertos = 0
            barra.erros = 0
            barra.ponteiro.perder()
            player1.get_tired(40)
            player1.get_train(50)
            somMetal.play()
            barra.hittable = False

        jogo_sprites.update()
        player1.gui()
        jogo_sprites.draw(screen)
        pygame.display.update()
        clock.tick(60)


gui()

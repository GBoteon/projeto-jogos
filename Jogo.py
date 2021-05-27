from pygame.locals import *
import pygame
import sys
import random
import time

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
engordou = False
emagreceu = False
comprimento = 100
velocidade = 10
dia = 0
dinheiro = 1000
fome = 150
energia = 150
v_hamburguer = 10.0
v_refri = 5.0
v_saudavel = 15
v_whey = 10.0
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
comida_whey_image_filename = 'icones/comidas/saudavel/whey.png'
close_store_image_filename = 'icones/close_store.svg'
trofeu1_image_filename = 'icones/trofeu_1.png'
trofeu2_image_filename = 'icones/trofeu_2.png'
trofeu3_image_filename = 'icones/trofeu_3.png'

background = pygame.image.load(background_image_filename).convert()
background2 = pygame.image.load(background_image_filename2).convert()
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
        velocidade += 2

    def perder(self):
        global velocidade
        velocidade -= 2

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
        else:
            print("limite")

    def engorda(self):
        global comprimento
        if comprimento >= 50:
            self.rect.x += 5
            comprimento -= 10
            self.image = pygame.Surface((comprimento, 50))
            self.image.fill(GREEN)
        else:
            print("limite")

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
        self.hit = False
        self.open = False
        self.scores = True
        self.rival = 0
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
        if self.scores:
            self.score()
        if not self.scores:
            self.compe()
        if self.ponteiro.rect.x >= self.acerto.rect.x or self.ponteiro.rect.x <= (self.acerto.rect.x + comprimento):
            self.hittable = True
        if self.ponteiro.rect.x <= self.acerto.rect.x or self.ponteiro.rect.x >= (self.acerto.rect.x + comprimento):
            self.hittable = False
            self.hit = False

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
        n = random.randint(1, 10)
        if n < 6:
            self.rival += 1

# adicionar 159 no x & 174 #


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
        self.salary = 100
        self.current_hunger = fome
        self.maximum_hunger = 200
        self.hunger_bar_lenght = 200
        self.hunger_ratio = self.maximum_hunger / self.hunger_bar_lenght
        self.current_energy = energia
        self.maximum_energy = 200
        self.energy_bar_lenght = 200
        self.energy_ratio = self.maximum_energy / self.energy_bar_lenght

    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

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
        self.salary = amount

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
        self.whey = Items_loja(180, 350, comida_whey, v_whey, spriteGroup)
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
        self.whey.abrir()
        self.botao_fechar.abrir()

    def close_icones(self):
        self.hamburguer.fechar()
        self.refri.fechar()
        self.saudavel.fechar()
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
        self.texto_preco = Texto(('$' + str(self.preco)), fonte_loja, MONEY, fundo_transparente, (self.rect.x + 15),
                                 (self.rect.y - 60))

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


# -------------------------#


click = False


def gui():
    # --------GAME LOOP-------#
    while True:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(title, (-470, 105))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        b_mute = pygame.Rect(925, 15, 50, 50)
        b_jogar = pygame.Rect(440, 250, 150, 50)
        b_como_jogar = pygame.Rect(440, 325, 150, 50)
        b_sair = pygame.Rect(440, 400, 150, 50)

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

        t_jogar = Texto('Jogar', fonte, (255, 255, 255), screen, 485, 265)
        t_como_jogar = Texto('Como Jogar', fonte, (255, 255, 255), screen, 455, 340)
        t_sair = Texto('Sair', fonte, (255, 255, 255), screen, 493, 415)

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
    barra_display = Barra(250, 150, como_jogar_sprites)
    player_display = Player(-100, 20, 1, como_jogar_sprites)
    me_display = Menina2(150, 20, 1, como_jogar_sprites)
    men_display = Menina3(250, 20, 1, como_jogar_sprites)
    meni_display = Menina4(350, 20, 1, como_jogar_sprites)
    barra_display.abrir()
    me_display.abrir()
    # meni_display.abrir()
    men_display.abrir()
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background2, (0, 0))
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
    competicao_sprite = pygame.sprite.Group()
    barra = Barra(200, 50, competicao_sprite)
    player = Player(-55, 20, 1, competicao_sprite)
    m = random.randint(2, 4)
    if m == 2:
        menina = Menina2(370, 20, 1, competicao_sprite)
    if m == 3:
        menina = Menina3(370, 20, 1, competicao_sprite)
    if m == 4:
        menina = Menina4(370, 20, 1, competicao_sprite)
    running = True
    barra.scores = False
    now = 0
    future = now + 5
    while running:
        global energia
        global dia
        global comprimento
        screen.fill((0, 0, 0))
        screen.blit(background2, (0, 0))
        background2.blit(fundo_banner, (15, 180))
        background2.blit(fundo_banner, (805, 180))
        background2.blit(trofeu1, (455, 400))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        menina.abrir()
        player.abrir()
        barra.abrir()

        now = time.time()

        if now == future:
            future = now + 5
            barra.dado()

        click = False
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

        competicao_sprite.draw(screen)
        competicao_sprite.update()
        pygame.display.update()
        clock.tick(60)


def jogo():
    peso = 1
    jogo_sprites = pygame.sprite.Group()
    loja1 = Loja(0, 150, jogo_sprites)
    player1 = Player(424, 59, peso, jogo_sprites)
    barra = Barra(25, 500, jogo_sprites)
    player1.call_idle()
    # game loop
    running = True
    while running:
        global energia
        global dia
        global comprimento
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        mouse_x, mouse_y = pygame.mouse.get_pos()

        b_cama = screen.blit(cama, (10, 10))
        b_loja = screen.blit(loja, (120, 10))
        b_treino = screen.blit(halter, (230, 10))
        b_competicao = screen.blit(podio, (340, 10))

        if b_cama.collidepoint((mouse_x, mouse_y)):
            if click:
                player1.fechar()
                barra.fechar()
                player1.current_energy = 200
                dia += 1

        if not loja1.loja_fundo.open:
            if b_loja.collidepoint((mouse_x, mouse_y)) and click:
                loja1.loja_fundo.abrir()
                player1.fechar()
                barra.fechar()

        if loja1.loja_fundo.open:
            b_fechar_loja = loja1.loja_fundo.botao_fechar.rect
            b_comprar_hamburguer = loja1.loja_fundo.hamburguer.rect
            b_comprar_refri = loja1.loja_fundo.refri.rect
            b_comprar_saudavel = loja1.loja_fundo.saudavel.rect
            b_comprar_whey = loja1.loja_fundo.whey.rect

            if b_fechar_loja.collidepoint((mouse_x, mouse_y)) and click:
                loja1.loja_fundo.fechar()
                player1.fechar()
                barra.fechar()

            if b_comprar_hamburguer.collidepoint((mouse_x, mouse_y)) and click:
                player1.lost_money(v_hamburguer)
                player1.get_food(70)
                barra.acerto.engorda()

            if b_comprar_refri.collidepoint((mouse_x, mouse_y)) and click:
                player1.lost_money(v_refri)
                player1.get_food(20)
                barra.acerto.engorda()

            if b_comprar_saudavel.collidepoint((mouse_x, mouse_y)) and click:
                player1.lost_money(v_saudavel)
                player1.get_food(50)
                barra.acerto.emagrece()

            if b_comprar_whey.collidepoint((mouse_x, mouse_y)) and click:
                player1.lost_money(v_whey)

        if b_treino.collidepoint((mouse_x, mouse_y)):
            if click:
                loja1.loja_fundo.fechar()
                player1.abrir()
                barra.abrir()

        if b_competicao.collidepoint((mouse_x, mouse_y)):
            if click:
                competir()

        click = False
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

        if barra.acertos == 10:
            barra.fechar()
            player1.fechar()
            barra.acertos = 0
            barra.erros = 0
            barra.ponteiro.treinar()
            player1.get_tired(25)
            player1.get_train(50)
            barra.hittable = False

        if barra.erros == 10:
            barra.fechar()
            player1.fechar()
            barra.acertos = 0
            barra.erros = 0
            barra.ponteiro.perder()
            player1.get_tired(25)
            player1.get_train(50)
            barra.hittable = False

        jogo_sprites.update()
        player1.gui()
        jogo_sprites.draw(screen)
        pygame.display.update()
        clock.tick(60)


gui()

from pygame.locals import *
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 625), 0, 32)
pygame.display.set_caption('WEIGHTLIFTER - Jogos Digitais')
clock = pygame.time.Clock()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
engordou = False
emagreceu = False
comprimento = 100
velocidade = 10
dia = 0
#---------[IMAGENS]---------#
background_image_filename = 'background.jpg'
background_image_filename2 = 'background2.png'
title_image_filename = 'title.svg'
volume_image_filename = 'volume.svg'
mutado_image_filename = 'mute.svg'
hunger_image_filename = 'icones/fome.png'
energy_image_filename = 'icones/forca.png'

background = pygame.image.load(background_image_filename).convert()
background2 = pygame.image.load(background_image_filename2).convert()
title = pygame.image.load(title_image_filename).convert_alpha()
volume = pygame.image.load(volume_image_filename).convert_alpha()
mutado = pygame.image.load(mutado_image_filename).convert_alpha()
hunger = pygame.transform.scale(pygame.image.load(hunger_image_filename), (50, 50)).convert_alpha()
energy = pygame.transform.scale(pygame.image.load(energy_image_filename), (50, 50)).convert_alpha()

volume_alpha = 500
mutado_alpha = 0
#---------------------------#

#---------[SONS]---------#
pygame.mixer.init()
pygame.mixer.music.load('menu.mp3')
pygame.mixer.music.play(-1)
som_on = True
#------------------------#

#---------[TEXTO]---------#
fonte = pygame.font.SysFont(None, 30)
dindin = pygame.font.SysFont(None, 60)


def texto(texto, fonte, cor, surface, x, y):
    texto = fonte.render(texto, 1, cor)
    texto_posi = texto.get_rect()
    texto_posi.topleft = (x, y)
    surface.blit(texto, texto_posi)
#-------------------------#

#----------[CLASSES]------#
class Ponteiro(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.speedx = 0
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speedx = velocidade
    
    def update(self):
        self.rect.x += self.speedx
        if self.rect.x > 915:
            self.speedx = velocidade*-1
        if self.rect.x < 125:
            self.speedx = velocidade
        
    def treinar(self):
        global velocidade
        velocidade += 2

class Acerto(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((comprimento,50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def emagrece(self):
        global comprimento
        if comprimento <= 300:
            self.rect.x -= 5
            comprimento += 10
            self.image = pygame.Surface((comprimento,50))
            self.image.fill(GREEN)
        else:
            print("limite")
            
    def engorda(self):
        global comprimento
        if comprimento >= 50: 
            self.rect.x += 5
            comprimento -= 10
            self.image = pygame.Surface((comprimento,50))
            self.image.fill(GREEN)
        else:
            print("limite")

# adicionar 159 no x & 174 #
class Peso1(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
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

    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

class Peso2(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
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

    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

class Peso3(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
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

    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, peso):
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

        if peso == 1:
            self.peso = Peso1((pos_x + 159), (pos_y + 174))

        if peso == 2:
            self.peso = Peso2((pos_x + 159), (pos_y + 174))

        if peso == 3:
            self.peso = Peso3((pos_x + 159), (pos_y + 174))

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.current_money = 1000
        self.salary = 100
        self.current_hunger = 150
        self.maximum_hunger = 200
        self.hunger_bar_lenght = 200
        self.hunger_ratio = self.maximum_hunger / self.hunger_bar_lenght
        self.current_energy = 150
        self.maximum_energy = 200
        self.energy_bar_lenght = 200
        self.energy_ratio = self.maximum_energy / self.energy_bar_lenght
        self.image = self.sprites[self.current_sprite]

    def update(self):
        self.basic_hunger()
        self.basic_energy()
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

    def basic_money(self):
        self.current_money += self.salary
        texto("$ " + str(self.current_money), dindin,(6, 152, 0), screen, 770, 120)

    def get_train(self, amount):
        if self.current_hunger > 0:
            self.current_hunger -= amount
        if self.current_hunger <= 0:
            self.current_hunger = 0

    def get_food(self, amount):
        if self.current_hunger < self.maximum_hunger:
            self.current_hunger += amount
        if self.current_hunger >= self.maximum_hunger:
            self.current_hunger = self.maximum_hunger

    def basic_hunger(self):
        pygame.draw.rect(screen, (236, 124, 48), (770, 80, self.current_hunger/self.hunger_ratio, 25))
        pygame.draw.rect(screen, (255, 255, 255), (770, 80, self.hunger_bar_lenght, 25), 4)
        screen.blit(hunger, (750, 65))

    def get_tired(self, amount):
        if self.current_energy > 0:
            self.current_energy -= amount
        if self.current_energy <= 0:
            self.current_energy = 0

    def get_rest(self, amount):
        if self.current_energy < self.maximum_energy:
            self.current_energy += amount
        if self.current_energy >= self.maximum_energy:
            self.current_energy = self.maximum_energy

    def basic_energy(self):
        pygame.draw.rect(screen, (255, 255, 0), (770, 20, self.current_energy/self.energy_ratio, 25))
        pygame.draw.rect(screen, (255, 255, 255), (770, 20, self.energy_bar_lenght, 25), 4)
        screen.blit(energy, (750, 10))

class Menina2(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, peso):
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

        if peso == 1:
            self.peso = Peso1((pos_x + 159), (pos_y + 174))

        if peso == 2:
            self.peso = Peso2((pos_x + 159), (pos_y + 174))

        if peso == 3:
            self.peso = Peso3((pos_x + 159), (pos_y + 174))

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

class Menina3(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, peso):
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

        if peso == 1:
            self.peso = Peso1((pos_x + 159), (pos_y + 174))

        if peso == 2:
            self.peso = Peso2((pos_x + 159), (pos_y + 174))

        if peso == 3:
            self.peso = Peso3((pos_x + 159), (pos_y + 174))

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

class Menina4(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, peso):
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

        if peso == 1:
            self.peso = Peso1((pos_x + 159), (pos_y + 174))

        if peso == 2:
            self.peso = Peso2((pos_x + 159), (pos_y + 174))

        if peso == 3:
            self.peso = Peso3((pos_x + 159), (pos_y + 174))

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
#-------------------------#

click = False



def gui():
    #--------GAME LOOP-------#
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
        texto('Jogar', fonte, (255, 255, 255), screen, 485, 265)
        texto('Como Jogar', fonte, (255, 255, 255), screen, 455, 340)
        texto('Sair', fonte, (255, 255, 255), screen, 493, 415)

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


def jogo():
    peso = 3
    barra = pygame.Rect(125, 400, 800, 50)
    #fundo = pygame.Rect(0, 0, )
    acer = Acerto(475, 400)
    pont = Ponteiro(125, 400)
    player1 = Player(40, 40, peso)
    jogo_sprites = pygame.sprite.Group()
    jogo_sprites.add(acer)
    jogo_sprites.add(pont)
    jogo_sprites.add(player1)
    jogo_sprites.add(player1.peso)
    # game loop
    running = True
    while running:
        global comprimento
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        mouse_x, mouse_y = pygame.mouse.get_pos()

        pygame.draw.rect(screen, (169, 169, 169), barra)
        b_emagrece = pygame.Rect(10, 100, 170, 50)
        b_engordar = pygame.Rect(10, 10, 170, 50)
        b_treinar = pygame.Rect(300, 10, 170, 50)
        if b_engordar.collidepoint((mouse_x, mouse_y)):
            if click:
                acer.engorda()
        if b_emagrece.collidepoint((mouse_x, mouse_y)):
            if click:
                acer.emagrece()
        if b_treinar.collidepoint((mouse_x, mouse_y)):
            if click:
                pont.treinar()
        pygame.draw.rect(screen, (0, 0, 0), b_treinar, border_radius=15)
        texto('Treinar', fonte, (255, 255, 255), screen, 325, 25)
        pygame.draw.rect(screen, (0, 0, 0), b_emagrece, border_radius=15)
        texto('Comida boa', fonte, (255, 255, 255), screen, 25, 125)
        pygame.draw.rect(screen, (0, 0, 0), b_engordar, border_radius=15)
        texto('Comida engorda', fonte, (255, 255, 255), screen, 25, 25)
        
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
                if event.key == pygame.K_UP:
                    player1.get_food(50)
            if event.type == KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player1.get_train(50)

        jogo_sprites.update()
        jogo_sprites.draw(screen)
        pygame.display.update()
        clock.tick(60)


def como_jogar():
    barra_display = pygame.Rect(125, 550, 800, 50)
    player_display = Player(50, 30)
    pont_display = Ponteiro(125, 550)
    acer_display = Acerto(475, 550)
    como_jogar_sprites = pygame.sprite.Group()
    como_jogar_sprites.add(player_display)
    como_jogar_sprites.add(acer_display)
    como_jogar_sprites.add(pont_display)
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background2, (0, 0))
        pygame.draw.rect(screen, (169, 169, 169), barra_display)
        texto('Como Jogar', fonte, (255, 255, 255), screen, 20, 20)
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


gui()

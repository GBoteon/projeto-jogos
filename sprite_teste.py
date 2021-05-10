from pygame.locals import *
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 625), 0, 32)
pygame.display.set_caption('Teste de sprites')
clock = pygame.time.Clock()

background_image_filename = 'background.jpg'
background = pygame.image.load(background_image_filename).convert()

# ---------[TEXTO]---------#
fonte = pygame.font.SysFont(None, 30)


def texto(texto, fonte, cor, surface, x, y):
    texto = fonte.render(texto, 1, cor)
    texto_posi = texto.get_rect()
    texto_posi.topleft = (x, y)
    surface.blit(texto, texto_posi)


# -------------------------#
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
    def __init__(self, pos_x, pos_y):
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

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.current_hunger = 150
        self.maximum_hunger = 200
        self.hunger_bar_lenght = 400
        self.hunger_ratio = self.maximum_hunger / self.hunger_bar_lenght
        self.image = self.sprites[self.current_sprite]

    def update(self):
        self.basic_hunger()
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

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
        pygame.draw.rect(screen, (255, 0, 0), (10, 400, self.current_hunger, 25))
        pygame.draw.rect(screen, (255, 255, 255), (10,400, self.hunger_bar_lenght, 25), 4)

class Menina2(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
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

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

class Menina3(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
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

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

class Menina4(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
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

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

player1 = Player(40, 40)
menina2 = Menina2(140, 52)
menina3 = Menina3(240, 23)
menina4 = Menina4(340, 52)
peso1 = Peso1(199, 214)
peso2 = Peso1(299, 214)
peso3 = Peso1(399, 214)
peso4 = Peso1(499, 214)

como_jogar_sprites = pygame.sprite.Group()
como_jogar_sprites.add(player1)
como_jogar_sprites.add(menina2)
como_jogar_sprites.add(menina3)
como_jogar_sprites.add(menina4)
como_jogar_sprites.add(peso1)
como_jogar_sprites.add(peso2)
como_jogar_sprites.add(peso3)
como_jogar_sprites.add(peso4)

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
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

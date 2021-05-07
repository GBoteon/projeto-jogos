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
#---------[IMAGENS]---------#
background_image_filename = 'prop/background.jpg'
title_image_filename = 'title.svg'
volume_image_filename = 'volume.svg'
mutado_image_filename = 'mute.svg'

background = pygame.image.load(background_image_filename).convert()
title = pygame.image.load(title_image_filename).convert_alpha()
volume = pygame.image.load(volume_image_filename).convert_alpha()
mutado = pygame.image.load(mutado_image_filename).convert_alpha()

volume_alpha = 1000
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


def texto(texto, fonte, cor, surface, x, y):
    texto = fonte.render(texto, 1, cor)
    texto_posi = texto.get_rect()
    texto_posi.topleft = (x, y)
    surface.blit(texto, texto_posi)
#-------------------------#

#----------[CLASSES]------#
class Ponteiro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.speedx = 0
        self.rect.x = 125
        self.rect.y = 400
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
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((comprimento,50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = 475
        self.rect.y = 400

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
#-------------------------#

#--------[OBJETOS]--------#
barra = pygame.Rect(125, 400, 800, 50)
pont = Ponteiro()
acer = Acerto()
all_sprites = pygame.sprite.Group()
all_sprites.add(acer)
all_sprites.add(pont)
#-------------------------#
click = False


def gui():
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
    # game loop
    running = True
    while running:
        global comprimento
        all_sprites.update()
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
        
        engordou = False
        click = False
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
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

        all_sprites.draw(screen)
        pygame.display.update()
        clock.tick(60)


def como_jogar():
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

        pygame.display.update()
        clock.tick(60)


gui()

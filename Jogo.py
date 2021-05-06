from pygame.locals import *
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 625), 0, 32)
pygame.display.set_caption('WEIGHTLIFTER - Jogos Digitais')
clock = pygame.time.Clock()

#---------[IMAGENS]---------#
background_image_filename = 'background.jpg'
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
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        texto('Jogo', fonte, (255, 255, 255), screen, 20, 20)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

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

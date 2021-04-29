from pygame.locals import *
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((626, 325), 0, 32)
pygame.display.set_caption('WEIGHTLIFTER - Jogos Digitais')

background_image_filename = 'background.jpg'
title_image_filename = 'title.png'

clock = pygame.time.Clock()

background = pygame.image.load(background_image_filename).convert()
title = pygame.image.load(title_image_filename).convert_alpha()


fonte = pygame.font.SysFont(None, 30)


def texto(texto, fonte, cor, surface, x, y):
    texto = fonte.render(texto, 1, cor)
    texto_posi = texto.get_rect()
    texto_posi.topleft = (x, y)
    surface.blit(texto, texto_posi)


click = False


def gui():
    while True:

        screen.fill((0, 0, 0))
        screen.blit(title, (105, 1))

        mx, my = pygame.mouse.get_pos()

        b_jogar = pygame.Rect(250, 100, 120, 40)
        b_como_jogar = pygame.Rect(250, 160, 120, 40)
        b_sair = pygame.Rect(250, 225, 120, 40)
        if b_jogar.collidepoint((mx, my)):
            if click:
                jogo()
        if b_como_jogar.collidepoint((mx, my)):
            if click:
                como_jogar()
        if b_sair.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, (178, 35, 35, 30), b_jogar)
        pygame.draw.rect(screen, (178, 35, 35), b_como_jogar)
        pygame.draw.rect(screen, (178, 35, 35), b_sair)
        texto('Jogar', fonte, (255, 255, 255), screen, 280, 110)
        texto('Como Jogar', fonte, (255, 255, 255), screen, 252, 170)
        texto('Sair', fonte, (255, 255, 255), screen, 285, 235)

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
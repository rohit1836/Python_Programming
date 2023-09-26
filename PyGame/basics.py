import pygame
from sys import exit



pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("My First Game using PyGame")

clock = pygame.time.Clock()

sky_surface = pygame.image.load("graphics/sky.png")
ground_surface = pygame.image.load("graphics/ground.png")

text_font = pygame.font.Font("font/Pixeltype.ttf",50)
text_surface = text_font.render("My Game",False,"Green")

snail_surface = pygame.image.load("graphics/snail/snail1.png")
snail_x_pos = 800

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))

    screen.blit(snail_surface,(snail_x_pos,270))
    snail_x_pos -= 5

    if snail_x_pos < -50:
        snail_x_pos = 800
    
    clock.tick(60)
    pygame.display.update()




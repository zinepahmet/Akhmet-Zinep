"""Task 4."""


import pygame
import math

pygame.init()
screen = pygame.display.set_mode((500, 500))
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))

arcsurface = pygame.Surface((400, 400))
arcsurface.fill((255, 255, 255))
Arc = pygame.draw.arc(arcsurface, (255, 128, 128), (0, 0, 400, 400), 0, math.pi)

#pygame.transform.rotate(Arc, 45)

running = True
FPS = 30
clock = pygame.time.Clock()

screen.blit(background, (0, 0))
screen.blit(arcsurface, (50, 50))

while running:
    milliseconds = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    pygame.display.flip()


pygame.quit()
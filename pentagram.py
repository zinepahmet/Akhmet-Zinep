"""Task 3. It is not possible to draw a pentagram by pygame.draw.polygon function, 
my variant is to draw a pentagram by drawing lines."""


import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))

polsurface = pygame.Surface((400, 400))
polsurface.fill((255, 255, 255))

pygame.draw.line(polsurface, (64, 255, 128), (200, 0), (100, 350), 4)
pygame.draw.line(polsurface, (64, 255, 128), (200, 0), (300, 350), 4)
pygame.draw.line(polsurface, (64, 255, 128), (100, 350), (400, 110), 4)
pygame.draw.line(polsurface, (64, 255, 128), (300, 350), (0, 110), 4)
pygame.draw.line(polsurface, (64, 255, 128), (0, 110), (400, 110), 4)

running = True
FPS = 30
clock = pygame.time.Clock()

screen.blit(background, (0, 0))
screen.blit(polsurface, (50, 50))
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
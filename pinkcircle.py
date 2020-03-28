"""Task 1."""


import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))

ballsurface = pygame.Surface((400, 400))
ballsurface.set_colorkey((0, 0, 0))
pygame.draw.circle(ballsurface, (255, 64, 128), (200, 200), 200)

running = True
FPS = 100
clock = pygame.time.Clock()

background = background.convert()
ballsurface = ballsurface.convert()
screen.blit(background, (0, 0))
screen.blit(ballsurface, (50, 50))

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
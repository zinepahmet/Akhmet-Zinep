"""Task 6."""


import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
darkBlue = (0, 0, 128)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 200, 200)
screen.fill(white)
for point in range(0, 256, 10): 
    pygame.draw.line(screen, (0, point, point), (0, 0), (640, point), 1)
    pygame.draw.line(screen, (point, 0, point), (0,0), (point, 480), 1)

clock = pygame.time.Clock()

running = True
FPS = 100
clock = pygame.time.Clock()

while running:
    milliseconds = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    pygame.display.flip()

pygame.display.update()
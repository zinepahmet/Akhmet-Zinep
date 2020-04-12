import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

ballx = 100
bally = 100

dx = 20
dy = 20

FPS = 50
running = True
clock = pygame.time.Clock()

while running:
    milliseconds = clock.tick(FPS)
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (255, 0 ,0), (ballx, bally), 25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT] and ballx >= 20: 
        ballx -= dx
    
    if pressed[pygame.K_RIGHT] and ballx <= 620: 
        ballx += dx
        
    if pressed[pygame.K_UP] and bally >= 20: 
        bally -= dy
    
    if pressed[pygame.K_DOWN] and bally <= 460: 
        bally += dy
    
    pygame.display.flip()

pygame.quit()
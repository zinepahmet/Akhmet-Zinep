import pygame
import random
from enum import Enum

pygame.init()
screen = pygame.display.set_mode((800, 600))
bg_image = pygame.image.load("bg_image.png")
bulletsound = pygame.mixer.Sound("bulletsound.wav")
winnersound = pygame.mixer.Sound("winnersound.wav")
explosionsound = pygame.mixer.Sound("explosionsound.wav")
bg_music = pygame.mixer.Sound("bg_music.wav")
bg_music.play()

class Direction(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

class Tank:
    def __init__(self, name, x, y, speed, colour, lives, d_right = pygame.K_RIGHT, d_left = pygame.K_LEFT, d_up = pygame.K_UP, d_down = pygame.K_DOWN):
        self.name = name
        self.x = x
        self.y = y
        self.speed = speed
        self.colour = colour
        self.width = 40
        self.lives = 3
        self.direction = Direction.RIGHT

        self.KEY = {d_right: Direction.RIGHT, d_left: Direction.LEFT, d_up: Direction.UP, d_down: Direction.DOWN}

    def draw(self):
        center = (self.x + int(self.width / 2), self.y + int(self.width / 2))
        pygame.draw.rect(screen, self.colour, (self.x, self.y, int(self.width), int(self.width)), 2)
        pygame.draw.circle(screen, self.colour, center, int(self.width / 2))

        if self.direction == Direction.RIGHT:
            pygame.draw.line(screen, self.colour, center, (self.x + int(self.width) + int(self.width / 2), self.y + int(self.width / 2)), 6)

        if self.direction == Direction.LEFT:
            pygame.draw.line(screen, self.colour, center, (self.x - int(self.width / 2), self.y + int(self.width / 2)), 6)

        if self.direction == Direction.UP:
            pygame.draw.line(screen, self.colour, center, (self.x + int(self.width / 2), self.y - int(self.width / 2)), 6)

        if self.direction == Direction.DOWN:
            pygame.draw.line(screen, self.colour, center, (self.x + int(self.width / 2), self.y + int(self.width) + int(self.width / 2)), 6)

    def change_direction(self, direction):
        self.direction = direction

    def move(self):
        if self.direction == Direction.RIGHT:
            self.x += self.speed
            if self.x > 770:
                self.x = -30
        if self.direction == Direction.LEFT:
            self.x -= self.speed
            if self.x < -30:
                self.x = 770
        if self.direction == Direction.UP:
            self.y -= self.speed
            if self.y < -30:
                self.y = 570
        if self.direction == Direction.DOWN:
            self.y += self.speed
            if self.y > 570:
                self.y = -30
        self.draw()

    def scores(self):
        f1 = pygame.font.Font(None, 45)
        score1 = f1.render("LIVES: " + str(tank1.lives), True, (255, 255, 255))
        screen.blit(score1, (625, 50))
        
        f2 = pygame.font.Font(None, 45)
        score2 = f2.render("LIVES: " + str(tank2.lives), True, (255, 255, 255))
        screen.blit(score2, (50, 50))
    def win(self):
        winnersound.play()
        f3 = pygame.font.Font(None, 100)
        winner = f3.render(str(self.name) + " is winner!!!", True, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        screen.blit(winner, (80, 250))

class Bullet:
    def __init__(self, x, y, colour, drop):
        self.x = x
        self.y = y
        self.colour = colour
        self.speed = 5
        self.radius = 5
        self.dx = 0
        self.dy = 0
        self.drop = False
    
    def draw2(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius)
    
    def start(self, x, y):
        if self.drop == True:
            self.x += self.dx
            self.y += self.dy
            self.draw2()
     
    def shoot(self, Tank):
        bulletsound.play()
        if Tank.direction == Direction.RIGHT:
            self.x = Tank.x + int(Tank.width / 2)
            self.y = Tank.y + int(Tank.width / 2)
            self.dx = 15
            self.dy = 0
        if Tank.direction == Direction.LEFT:
            self.x = Tank.x + int(Tank.width / 2)
            self.y = Tank.y + int(Tank.width / 2)
            self.dx = -15
            self.dy = 0
        if Tank.direction == Direction.UP:
            self.x = Tank.x + int(Tank.width / 2)
            self.y = Tank.y + int(Tank.width / 2)
            self.dx = 0
            self.dy = -15
        if Tank.direction == Direction.DOWN:
            self.x = Tank.x + int(Tank.width / 2)
            self.y = Tank.y + int(Tank.width / 2)
            self.dx = 0
            self.dy = 15
    def bulletout(self): 
        if self.x >= 800 or self.x <= 0 or self.y >= 600 or self.y <= 0:
            return True
        return False
    
    def col(self, Tank): #collision
        if Tank.direction == Direction.RIGHT and self.drop == True:
            if (self.x > Tank.x and self.x < Tank.x + 60) and (self.y > Tank.y and self.y < Tank.y + 40):
                return True
        if Tank.direction == Direction.LEFT and self.drop == True:
            if (self.x > Tank.x - 20 and self.x < Tank.x + 40) and (self.y > Tank.y and self.y < Tank.y + 40):
                return True
        if Tank.direction == Direction.UP and self.drop == True:
            if (self.y > Tank.y - 20 and self.y < Tank.y + 40) and (self.x > Tank.y and self.x < Tank.x + 40):
                return True
        if Tank.direction == Direction.DOWN and self.drop == True:
            if (self.y > Tank.y and self.y < Tank.y + 60) and (self.x > Tank.x and self.x < Tank.x + 40):
                return True 

running = True

tank1 = Tank("Player 1", 100, 460, 3, (170, 190, 50), 3)
tank2 = Tank("Player 2", 100, 100, 3, (155, 205, 155, 255), 3, pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s)

bullet1 = Bullet(tank1.x, tank1.y, (0, 0, 0), False)
bullet2 = Bullet(tank2.x, tank2.y, (0, 0, 0), False)
tanks = [tank1, tank2]
bullets = [bullet1, bullet2]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
            if event.key == pygame.K_RETURN:
                if bullet1.drop == False:
                    bullet1.drop = True
                    bullet1.shoot(tank1)
            if event.key == pygame.K_SPACE:
                if bullet2.drop == False:
                    bullet2.drop = True
                    bullet2.shoot(tank2)  
            for tank in tanks:
                if event.key in tank.KEY.keys():
                    tank.change_direction(tank.KEY[event.key])
    if bullet1.col(tank2) == True:
        explosionsound.play()
        tank2.lives -= 1
        bullet1.drop = False
        bullet1.x, bullet1.y = tank1.x + int(tank1.width / 2), tank1.y + int(tank1.width / 2)
    if bullet2.col(tank1) == True:
        explosionsound.play()
        tank1.lives -= 1
        bullet2.drop = False
        bullet2.x, bullet2.y = tank2.x + int(tank2.width / 2), tank2.y + int(tank2.width / 2)
    for bullet in bullets:
        if bullet.bulletout() == True:
            bullet.drop = False
                   
    screen.blit(bg_image, (0, 0))

    for tank in tanks:
        tank.move()
        tank.scores()
        if tank.lives == 0:
            tank.win()
            tank1.speed = 0
            tank2.speed = 0
            tank1.width = 0
            tank2.width = 0
    bullet2.start(tank2.x + int(tank2.width / 2), tank2.y + int(tank2.width / 2))    
    bullet1.start(tank1.x + int(tank1.width / 2), tank1.y + int(tank1.width / 2))
    pygame.display.flip()

pygame.quit()
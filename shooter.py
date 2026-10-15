import pygame
from pygame.key import get_pressed as keyboard

pygame.init()


WIDTH   = 1000
HEIGHT  = 800
FPS     = 30

display = pygame.display.set_mode( (WIDTH, HEIGHT) )
clock   = pygame.time.Clock()


class Background:
    
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 1000, 150)
    
    
    def draw(self, display):
        pygame.draw.rect(display, "#e09f3e", self.rect)


class Player:
    
    def __init__(self, x, y):
        
        self.speed = 10
        self.color = "blue"
        
        self.rect = pygame.Rect(x, y, 50, 50) 
        

    def draw(self, display):
        pygame.draw.rect(display, self.color, self.rect)

    
    def move(self):
        
        if keyboard()[pygame.K_d]:
            self.rect.x += self.speed
            self.color = "darkblue"
        
        elif keyboard()[pygame.K_a]:
            self.rect.x -= self.speed
            self.color = "darkblue"
        
        else:
            self.color = "blue"
    
    
    def update(self):
        self.move()


background = Background(0, 650)
player     = Player(x=100, y=600)


running = True
while running:
    """
        Asosiy sikl
    """
    # Har siklda oynani yangilaydi
    pygame.display.update()
    # Oynani oq ranga boyaydi
    display.fill("white")
    # 1 sonida 30 kadr aylanadi
    clock.tick(30) # FPS
    
    
    background.draw(display)
    player.draw(display)
    player.update()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.quit()
    


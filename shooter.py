import os
import pygame
from pygame.image import load
from pygame.transform import scale
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
        
        self.images = self.collect_images()
        self.state = 0
        self.index = 0
        
        self.speed = 10
        self.color = "blue"
        
        self.is_jumping = False
        self.jump_force = 9
        self.velocity = self.jump_force
        
        self.image = self.images[self.state][self.index]
        self.rect = self.image.get_rect(topleft=(x, y))
    
    def collect_images(self):
        
        data = []
        
        for state in ["Idle", "Run", "Jump", "Death"]:
            
            states = []
            images = os.listdir(f"images/player/{state}")
            
            for img_file in images:
                
                image = load(f"images/player/{state}/{img_file}").convert_alpha()
                width = image.get_width() * 2
                print(f"{width = }")
                heigh = image.get_height() * 2
                image = scale(image, (width, heigh))
                states.append(image)
                
            data.append(states)
               
        return data
        
    
    def animate(self, anim_speed=3):
        
        total = len(self.images[self.state])
        
        if self.index < total * anim_speed - 1:
            self.index += 1
        else:
            self.index = 0
            
        self.image = self.images[self.state][self.index // anim_speed]
            
        
    
    
    def move(self):
        
        if keyboard()[pygame.K_d]:
            self.rect.x += self.speed
            self.color = "darkblue"
        
        elif keyboard()[pygame.K_a]:
            self.rect.x -= self.speed
            self.color = "darkblue"
        
        else:
            self.color = "blue"
    
    
    def jump(self):
        
        if not self.is_jumping:
            if keyboard()[pygame.K_w]:
                self.is_jumping = True
        
        if self.is_jumping:
            if self.velocity > 0:
                self.rect.y -= self.velocity ** 2 // 2
            else:
                self.rect.y += self.velocity ** 2 // 2
            self.velocity -= 1
            
            if self.velocity == -self.jump_force - 1:
                self.velocity = self.jump_force
                self.is_jumping = False
     
        
    def draw(self, display):
    # pygame.draw.rect(display, self.color, self.rect)
        display.blit(self.image, self.rect)

    
    def update(self):
        self.move()
        self.jump()
        self.animate()


background = Background(0, 650)
player     = Player(x=100, y=580)


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
    
    
    background.draw(display) # yer chizib beradi
    player.draw(display)     # playerni chizib beradi
    player.update()          
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.quit()
    


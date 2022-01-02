"""
Author : mahesh patapalli
Date : 01-01-2022
"""

import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 30
frames_per_sec = pygame.time.Clock()
color_dict = {"blue" : (0, 0, 255),
              "red" : (255, 0, 0), 
              "green": (0, 255, 0), 
              "white" : (255, 255, 255), 
              "black" : (0, 0, 0)}

scale_factor = 0.20
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 800
e_speed = 5
p_speed = 5
SCORE = 0

# setting up fonts
font = pygame.font.SysFont("Verdara", 80)
font_small = pygame.font.SysFont("Verdara", 50)
game_over = font.render("Game Over", True, color_dict["black"])
background = pygame.image.load("assets/bg_1.jpg")

# setting up canvas
Display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
Display_surface.fill(color_dict["white"])
pygame.display.set_caption("Beta")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/base_1.png")
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0] * scale_factor), int(self.size[1] * scale_factor)))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, e_speed)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/destroyer.png")
        # scale the sprite to 33% of its original size
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0] * scale_factor), int(self.size[1] * scale_factor)))
        self.rect = self.image.get_rect()
        self.rect.center = (160, SCREEN_HEIGHT - 150)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-p_speed, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(p_speed, 0)


p1 = Player()
e1 = Enemy()

# sprite groups

enemies = pygame.sprite.Group()
enemies.add(e1)

all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)


## difficulty increase
speed_increase = pygame.USEREVENT + 1
pygame.time.set_timer(speed_increase, 1000)


# main Loop
while True:
    for event in pygame.event.get():

        if event.type == speed_increase:
            e_speed += 2
            p_speed += 1

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    Display_surface.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, color_dict["black"])
    Display_surface.blit(scores, (10, 10))

    for entity in all_sprites:
        Display_surface.blit(entity.image, entity.rect)
        entity.move()

    # collision and game over 
    if pygame.sprite.spritecollideany(p1, enemies):
        pygame.mixer.Sound("assets/sounds/crash.wav").play()
        time.sleep(0.5)

        Display_surface.fill(color_dict["red"])
        Display_surface.blit(game_over, (170,350))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    frames_per_sec.tick(FPS)

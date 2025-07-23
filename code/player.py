import os
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups, obstacle_sprites, crop_rect, save_path=None):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/NinjaAdventure/Actor/Characters/Knight/SeparateAnim/Idle.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.original_size = self.image.get_size()
        new_size = (self.original_size[0] * 4, self.original_size[1] * 4)
        self.scaled_image = pygame.transform.scale(self.image, new_size)
        self.crop_rect = pygame.Rect(crop_rect)
        self.crop_image = self.scaled_image.subsurface(self.crop_rect).copy()
        
        if save_path:
            pygame.image.save(self.crop_image, save_path)
            if os.path.exists(save_path):
                print("player exists")
            else:
                print("player is saved")
        
        
        self.image = pygame.image.load('../graphics/NinjaAdventure/Backgrounds/ZeldaTiles/Player_cropped.png').convert_alpha()
        self.rect = self.crop_image.get_rect(topleft = pos)
        
        self.direction = pygame.math.Vector2()
        self.speed = 5
        
        self.obstacle_sprites = obstacle_sprites
    
    def input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
            
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: #moving left
                        self.rect.left = sprite.rect.left
        
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: #moving left
                        self.rect.left = sprite.rect.left
     
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.center += self.direction * speed
        
    def update(self):
        self.input()
        self.move(self.speed)
    
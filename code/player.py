import os
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups, crop_rect, save_path=None):
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
        
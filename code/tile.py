import os
import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups, crop_rect, save_path=None):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/NinjaAdventure/Backgrounds/Tilesets/TilesetNature.png').convert_alpha()
        #self.rect = self.image.get_rect(topleft = pos)
        self.original_size = self.image.get_size()
        new_size = (self.original_size[0] * 2, self.original_size[1] * 2)
        self.scaled_image = pygame.transform.scale(self.image, new_size)
        self.crop_rect = pygame.Rect(crop_rect)
        self.crop_image = self.scaled_image.subsurface(self.crop_rect).copy()
        
        if save_path:
            pygame.image.save(self.crop_image, save_path)
            if os.path.exists(save_path):
                print("rock exists")
            else:
                print("rock is saved")
        
        self.image = pygame.image.load('../graphics/NinjaAdventure/Backgrounds/ZeldaTiles/Rock_cropped.png').convert_alpha()
        self.rect = self.crop_image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)
        
        
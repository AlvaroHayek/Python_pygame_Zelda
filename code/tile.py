import os
import pygame
from PIL import Image
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups, crop_rect, save_path=None, ntimes=1):
        super().__init__(groups)
        
        if ntimes > 0:
            def clean_and_load_png(filename, png_path):
                img = Image.open(png_path)
                img.save(filename, icc_profile=None)
                return pygame.image.load(filename).convert_alpha()
            
            self.image = clean_and_load_png('../graphics/NinjaAdventure/Backgrounds/Tilesets/TilesetNature.png','../graphics/NinjaAdventure/Backgrounds/Tilesets/TilesetNature.png')
            self.original_size = self.image.get_size()
            new_size = (self.original_size[0] * 2, self.original_size[1] * 2)
            self.scaled_image = pygame.transform.scale(self.image, new_size)
            self.crop_rect = pygame.Rect(crop_rect)
            self.crop_image = self.scaled_image.subsurface(self.crop_rect).copy()
            pygame.image.save(self.crop_image, save_path)
        
        self.image = pygame.image.load('../graphics/NinjaAdventure/Backgrounds/ZeldaTiles/Rock_cropped.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,HITBOX_OFFSET['grass'])
        
        
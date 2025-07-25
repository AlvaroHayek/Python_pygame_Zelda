import os
import pygame
from PIL import Image
from settings import *

class Water(pygame.sprite.Sprite):
    def __init__(self,pos,groups, crop_rect, save_path=None):
        super().__init__(groups)
        #self.sprite_type = sprite_type
        #self.image = surface
        
        def clean_and_load_png(filename, png_path):
            img = Image.open(png_path)
            img.save(filename, icc_profile=None)
            return pygame.image.load(filename).convert_alpha()
        
        self.image = clean_and_load_png('TilesetWater2.png','../graphics/NinjaAdventure/Backgrounds/Tilesets/TilesetWater.png')
        #self.rect = self.image.get_rect(topleft = pos)
        self.original_size = self.image.get_size()
        new_size = (self.original_size[0] * 2.8, self.original_size[1] * 2.8)
        self.scaled_image = pygame.transform.scale(self.image, new_size)
        self.crop_rect = pygame.Rect(crop_rect)
        self.crop_image = self.scaled_image.subsurface(self.crop_rect).copy()
        
        if save_path:
            pygame.image.save(self.crop_image, save_path)
            if os.path.exists(save_path):
                print("water exists")
            else:
                print("water is saved")
        
        self.image = clean_and_load_png('WaterCropped2.png','../graphics/NinjaAdventure/Backgrounds/ZeldaTiles/Water_cropped.png')
        self.rect = self.crop_image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)
    
       
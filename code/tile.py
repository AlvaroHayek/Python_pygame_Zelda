import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups, crop_rect):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/NinjaAdventure/Backgrounds/Tilesets/TilesetNature.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.crop_rect = pygame.Rect(crop_rect)
        self.crop_image = self.image.subsurface(self.crop_rect).copy()
        
        
import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/NinjaAdventure/Backgrounds/Tilesets/TilesetNature.png').convert_alpha()
        self.crop_rect = pygame.Rect(0, 0, 20, 20)
        self.crop_image = self.image.subsurface(self.crop_rect)
        self.rect = self.crop_image.get_rect(topleft = pos)
        
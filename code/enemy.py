import pygame
from settings import *
from entity import Entity

class Enemy(Entity):
    def __init__(self,monster_name,pos,groups):
        
        # general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'
        
        # graphics setup
        self.import_graphics(monster_name)
        self.image = pygame.Surface((64,64))
        self.rect = self.image.get_rect(topleft=pos)
        
    def import_graphics(self,name):
        self.animations = {'idle':[],'move':[],'attack':[]}
        main = f'../graphics/NinjaAdventure/Actor/Monsters/{name}'
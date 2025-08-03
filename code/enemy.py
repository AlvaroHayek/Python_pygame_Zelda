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
        self.status = 'idle'
        self.image = pygame.image.load(self.animations[self.status]).convert_alpha()
        self.original_size = self.image.get_size()
        new_size = (self.original_size[0] * 4, self.original_size[1] * 4)
        self.image = pygame.transform.scale(self.image, new_size)
        self.rect = self.image.get_rect(topleft=pos)
        
    def import_graphics(self,name):
        self.animations = {'idle':[],'move':[],'attack':[]}
        enemy_path = f'../graphics/NinjaAdventure/Actor/Monsters/{name}/'
        for animation in self.animations.keys():
            full_path = enemy_path + animation + '.png'
            self.animations[animation] = full_path
        print(self.animations)
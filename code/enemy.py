import pygame
from settings import *
from entity import Entity

class Enemy(Entity):
    def __init__(self,monster_name,pos,groups,obstacle_sprites):
        
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
        
        # movement
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-10)
        self.obstacle_sprites = obstacle_sprites
        
        # stats
        self.monster_name = monster_name
        monster_info = monster_data[self.monster_name]
        self.health = monster_info['health']
        self.exp = monster_info['exp']
        self.speed = monster_info['speed']
        self.attack_damage = monster_info['damage']
        self.resistance = monster_info['resistance']
        self.attack_radius = monster_info['attack_radius']
        self.notice_radius = monster_info['notice_radius']
        self.attack_type = monster_info['attack_type']
        
        
    def import_graphics(self,name):
        self.animations = {'idle':[],'move':[],'attack':[]}
        enemy_path = f'../graphics/NinjaAdventure/Actor/Monsters/{name}/'
        for animation in self.animations.keys():
            full_path = enemy_path + animation + '.png'
            self.animations[animation] = full_path
    
    def get_status(self,player):
        distance = ???
        
        if distance <= self.attack_radius:
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'
            
    def update(self):
        self.move(self.speed)
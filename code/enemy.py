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
        self.walking_change = 100
        self.walking_time = pygame.time.get_ticks()
        self.num_frames = 3
        self.current_frame = 0
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
        
        # player interaction
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400
        
    def import_graphics(self,name):
        self.animations = {'idle':[],'move':[],'attack':[]}
        enemy_path = f'../graphics/NinjaAdventure/Actor/Monsters/{name}/'
        for animation in self.animations.keys():
            full_path = enemy_path + animation + '.png'
            self.animations[animation] = full_path
    
    def get_player_distance_direction(self,player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()
        
        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()
        
        return (distance,direction)
    
    def get_status(self,player):
        distance = self.get_player_distance_direction(player)[0]

        if distance <= self.attack_radius and self.can_attack:
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'
    
    def actions(self,player):
        if self.status == 'attack':
            self.attack_time = pygame.time.get_ticks()
        elif self.status == 'move':
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()
            
    def animate(self):
        animation = self.animations[self.status]
        self.image = pygame.image.load(animation).convert_alpha()
        self.image_rect = self.image.get_rect()
        self.original_size = self.image.get_size()
        new_size = (self.original_size[0] * 4, self.original_size[1] * 4)
        self.image = pygame.transform.scale(self.image, new_size)
        if self.image_rect.height >= 32:
            if self.status == 'attack':
                if self.current_frame >= 2:
                    self.current_frame = 0
                self.can_attack = False
            current_time_anim = pygame.time.get_ticks()
            self.frame_height = self.image.get_height() // 4
            self.crop_rect = pygame.Rect(0,64*self.current_frame,64,64)
   
            self.image = self.image.subsurface(self.crop_rect).copy()
            if current_time_anim - self.walking_time > self.walking_change:
                self.walking_time = current_time_anim
                current_time_anim = 0
                self.current_frame+=1
                if self.image_rect.height == 32:
                    if self.current_frame == 2:
                        self.current_frame = 1
                else:
                    if self.current_frame == 4:
                        self.current_frame = 1
    
    def attack_cooldown(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.attack_time >= self.attack_cooldown:
            self.can_attack = True
    
    def update(self):
        self.move(self.speed)
        self.animate()
        
    def enemy_update(self,player):
        self.get_status(player)
        self.actions(player)
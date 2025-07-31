import os
import pygame
from PIL import Image
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups, obstacle_sprites, create_attack, crop_rect, save_path=None, ntimes=1):
        super().__init__(groups)
        
        if ntimes > 0:
            def clean_and_load_png(filename, png_path):
                img = Image.open(png_path)
                img.save(filename, icc_profile=None)
                return pygame.image.load(filename).convert_alpha()
        
        
            self.image = clean_and_load_png('Idle.png','../graphics/NinjaAdventure/Actor/Characters/Knight/SpriteSheet.png')
            self.rect = self.image.get_rect(topleft = pos)
            self.original_size = self.image.get_size()
            new_size = (self.original_size[0] * 4, self.original_size[1] * 4)
            self.scaled_image = pygame.transform.scale(self.image, new_size)
            self.crop_rect = pygame.Rect(crop_rect)
            self.crop_image = self.scaled_image.subsurface(self.crop_rect).copy()
            pygame.image.save(self.crop_image, save_path)
        
        self.image = pygame.image.load('../graphics/NinjaAdventure/Actor/Characters/Knight/down_idle.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)
        
        # graphics setup
        self.import_player_assets()
        self.status = 'down'
        
        # movement
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.attacking = False
        self.attack_cooldown = 400
        self.walking_change = 100
        self.walking_time = pygame.time.get_ticks()
        self.attack_time = None
        self.num_frames = 3
        self.current_frame = 0
        self.obstacle_sprites = obstacle_sprites
        
        # weapon
        self.create_attack = create_attack
    
    def import_player_assets(self):
        character_path = "../graphics/NinjaAdventure/Actor/Characters/Knight/"
        self.animations = {'up': [],'down': [],'left': [],'right': [],
                           'right_idle': [],'left_idle': [],'up_idle': [],'down_idle': [],
                           'right_attack': [],'left_attack': [],'up_attack': [],'down_attack': []}
        
        for animation in self.animations.keys():
            full_path = character_path + animation + '.png'
            self.animations[animation] = full_path
            
        
    def input(self):
        keys = pygame.key.get_pressed()
        
        # movement input
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0
            
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

        # attack input
        if keys[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            self.create_attack()
        # magic input
        if keys[pygame.K_LCTRL] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            print('magic')
    
    def get_status(self):
        # idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'
        
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle','_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack','')
    
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center
        
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: #moving left
                        self.hitbox.left = sprite.hitbox.right
        
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: #moving up
                        self.hitbox.top = sprite.hitbox.bottom
        
    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
    
    def animate(self):
        animation = self.animations[self.status]
        self.image = pygame.image.load(animation).convert_alpha()
        self.image_rect = self.image.get_rect()
        if self.image_rect.height == 256:
            current_time_anim = pygame.time.get_ticks()
            self.frame_height = self.image.get_height() // 4
            self.crop_rect = pygame.Rect(0,64*self.current_frame,64,64)
            self.image = self.image.subsurface(self.crop_rect).copy()
            if current_time_anim - self.walking_time > self.walking_change:
                self.walking_time = current_time_anim
                current_time_anim = 0
                self.current_frame+=1
                if self.current_frame == 4:
                    self.current_frame = 1
    
    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)
    
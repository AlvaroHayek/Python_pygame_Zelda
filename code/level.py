import pygame
from settings import *
from tile import Tile
from player import Player
from water import Water
from debug import debug
from weapon import Weapon
from random import choice
from ui import UI
from enemy import Enemy

class Level:
    def __init__(self):
        
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        
        # attack sprites
        self.current_attack = None
        
        # sprite setup
        self.create_map()
        
        # user interface
        self.ui = UI()
        
        
    def create_map(self):
        tile_save_path = "../graphics/NinjaAdventure/Backgrounds/ZeldaTiles/Rock_cropped.png"
        player_save_path = "../graphics/NinjaAdventure/Actor/Characters/Knight/down_idle.png"
        water_save_path = "../graphics/NinjaAdventure/Backgrounds/ZeldaTiles/Water_cropped.png"
        nuptimes = 1
        nuxtimes = 1
        nuwtimes = 1
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites], (480,385,64,64), tile_save_path, nuxtimes)
                    nuxtimes=0
                if col == 'w':
                    Water((x,y),[self.visible_sprites,self.obstacle_sprites], (35,38,64,64), water_save_path,nuwtimes)
                    nuwtimes=0
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites], self.obstacle_sprites, 
                                         self.create_attack, self.destroy_attack, self.create_magic,
                                         (0,0,64,64), player_save_path, nuptimes)
                    nuptimes = 0
                if col == 'ea': Enemy('axolot',(x,y),[self.visible_sprites])
                if col == 'er': Enemy('raccoon',(x,y),[self.visible_sprites])
                if col == 'es': Enemy('spirit',(x,y),[self.visible_sprites])
                if col == 'eb': Enemy('bamboo',(x,y),[self.visible_sprites])
                    
                    
                    
    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites])
    
    def create_magic(self,style,strength,cost):
        print(style)
        print(strength)
        print(cost)
    
    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None
    
    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        #debug(self.player.status)
        self.ui.display(self.player)
        
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        
        # creating the floor
        floor_save_path = '../graphics/NinjaAdventure/Backgrounds/ZeldaTiles/tilemap_v02.png'
        self.floor_surf = pygame.image.load(floor_save_path)
        self.floor_rect = self.floor_surf.get_rect(topleft = (608,416))
        
        
    def custom_draw(self, player):
        
        # getting offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        #drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)
        
        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
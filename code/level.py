import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):
        
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # sprite group setup
        #self.visible_sprites = pygame.sprite.Group()
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        
        # sprite setup
        self.create_map()
        
    def create_map(self):
        tile_save_path = "../graphics/NinjaAdventure/Backgrounds/ZeldaTiles/Rock_cropped.png"
        player_save_path = "../graphics/NinjaAdventure/Backgrounds/ZeldaTiles/Player_cropped.png"
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites], (480,385,64,64), tile_save_path)
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites], self.obstacle_sprites, (0,0,64,64), player_save_path)
                
    
    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw()
        self.visible_sprites.update()
        debug(self.player.direction)
        
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        
    def custom_draw(self):
        for sprite in self.sprites():
            self.display_surface.blit(sprite.image,sprite.rect)
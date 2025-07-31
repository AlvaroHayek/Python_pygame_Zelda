import pygame
from PIL import Image

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player,groups):
        super().__init__(groups)
        direction = player.status.split('_')[0]
        
        # graphic
        full_path = f'../graphics/NinjaAdventure/Items/Weapons/{player.weapon}/SpriteInHand.png'
        def clean_and_load_png(png_path):
                img = Image.open(png_path)
                img.save(png_path, icc_profile=None)
                return pygame.image.load(png_path).convert_alpha()
            
        self.image = clean_and_load_png(full_path).convert_alpha()
        self.original_size = self.image.get_size()
        new_size = (self.original_size[0] * 3, self.original_size[1] * 3)
        self.image = pygame.transform.scale(self.image, new_size)
        
        # placement
        if direction == 'right':
            self.image = pygame.transform.rotate(self.image, 90)
            self.rect = self.image.get_rect(midleft=player.rect.midright + pygame.math.Vector2(0,16))
        elif direction == 'left':
            self.image = pygame.transform.rotate(self.image, -90)
            self.rect = self.image.get_rect(midright=player.rect.midleft + pygame.math.Vector2(0,16))
        elif direction == 'down':
            self.rect = self.image.get_rect(midtop=player.rect.midbottom + pygame.math.Vector2(-8,0))
        else:
            self.image = pygame.transform.rotate(self.image, 180)
            self.rect = self.image.get_rect(midbottom=player.rect.midtop + pygame.math.Vector2(-12,0))
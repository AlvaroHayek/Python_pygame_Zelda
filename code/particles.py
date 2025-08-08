import pygame
from random import choice
from PIL import Image

class AnimationPlayer:
    def __init__(self):
        self.frames = {
            # magic
            'Flame':'../graphics/NinjaAdventure/FX/Elemental/Flame/SpriteSheet.png',
            'Aura':'../graphics/NinjaAdventure/FX/Magic/Aura/SpriteSheet.png',
            'Spark':'../graphics/NinjaAdventure/FX/Magic/Spark/SpriteSheet.png', # used to heal
            
            # attacks
            'Claw':{'graphic':'../graphics/NinjaAdventure/FX/SlashFx/Claw/SpriteSheet.png', 'divisions': 4},
            'Slash':{'graphic':'../graphics/NinjaAdventure/FX/SlashFx/Slash/SpriteSheet.png', 'divisions': 4},
            'Cut':{'graphic':'../graphics/NinjaAdventure/FX/SlashFx/Cut/SpriteSheet.png', 'divisions': 5},
            'Plant':{'graphic':'../graphics/NinjaAdventure/FX/Elemental/Plant/SpriteSheet.png', 'divisions': 8},
            'Thunder':{'graphic':'../graphics/NinjaAdventure/FX/Elemental/Thunder/SpriteSheet.png', 'divisions': 8},
            # monster deaths
            'axolot':{'graphic':'../graphics/NinjaAdventure/FX/Smoke/Smoke/SpriteSheet.png', 'divisions': 6},
            'raccoon':{'graphic':'../graphics/NinjaAdventure/FX/Magic/Circle/SpriteSheetOrange.png', 'divisions': 4},
            'spirit':{'graphic':'../graphics/NinjaAdventure/FX/Magic/Spirit/SpriteSheetBlue.png', 'divisions': 5},
            'bamboo':{'graphic':'../graphics/NinjaAdventure/FX/Elemental/Plant/SpriteSheetB.png', 'divisions': 7},
            # leafs
            'leaf': (
                '../graphics/NinjaAdventure/FX/Particle/Leaf.png',
                '../graphics/NinjaAdventure/FX/Particle/LeafPink.png',
                '../graphics/NinjaAdventure/FX/Particle/Bamboo.png',
                '../graphics/NinjaAdventure/FX/Particle/Grass.png',
                #self.reflect_images('../graphics/NinjaAdventure/FX/Particle/Leaf.png'),
                #self.reflect_images('../graphics/NinjaAdventure/FX/Particle/LeafPink.png'),
                #self.reflect_images('../graphics/NinjaAdventure/FX/Particle/Bamboo.png'),
                #self.reflect_images('../graphics/NinjaAdventure/FX/Particle/Grass.png'),
            )
            
        }
        
    def reflect_images(self,frame):
        new_frames = []
        self.image = pygame.image.load(frame).convert_alpha()
        flipped_frame = pygame.transform.flip(self.image,True,False)
        return flipped_frame
    
    def create_grass_particles(self,pos,groups):
        animation_frames = []
        animation_full_frame = choice(self.frames['leaf'])
        self.image = pygame.image.load(animation_full_frame).convert_alpha()
        self.original_size = self.image.get_size()
        new_size = (self.original_size[0] * 4, self.original_size[1] * 4)
        self.image = pygame.transform.scale(self.image, new_size)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.frame_width = self.width / 6
        for init_factor in range(6):
            self.crop_rect = pygame.Rect(init_factor*self.frame_width, 0, self.frame_width, self.height)
            self.cropped_image = self.image.subsurface(self.crop_rect).copy()
            self.rect = self.cropped_image.get_rect()
            animation_frames.append(self.cropped_image)
        ParticleEffect(pos,animation_frames,groups)
        
    def create_particles(self,animation_type,pos,groups):
        #self.animation_type = animation_type
        animation_info = self.frames[animation_type]
        animation_full_frame = animation_info['graphic']
        animation_divisions = animation_info['divisions']
        animation_frames = []
        #animation_full_frame = choice(self.frames['leaf'])
        self.image = pygame.image.load(animation_full_frame).convert_alpha()
        self.original_size = self.image.get_size()
        new_size = (self.original_size[0] * 4, self.original_size[1] * 4)
        self.image = pygame.transform.scale(self.image, new_size)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.frame_width = self.width / animation_divisions
        for init_factor in range(animation_divisions):
            self.crop_rect = pygame.Rect(init_factor*self.frame_width, 0, self.frame_width, self.height)
            self.cropped_image = self.image.subsurface(self.crop_rect).copy()
            self.rect = self.cropped_image.get_rect()
            animation_frames.append(self.cropped_image)
        
        #animation_frames = self.frames[animation_type]
        ParticleEffect(pos,animation_frames,groups)

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self,pos,animation_frames,groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]
            
    def update(self):
        self.animate()
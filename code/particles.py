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
            'Claw':'../graphics/NinjaAdventure/FX/SlashFx/Claw/SpriteSheet.png',
            'Slash':'../graphics/NinjaAdventure/FX/SlashFx/Slash/SpriteSheet.png',
            'Cut':'../graphics/NinjaAdventure/FX/SlashFx/Cut/SpriteSheet.png',
            'Plant':'../graphics/NinjaAdventure/FX/Elemental/Plant/SpriteSheet.png',
            'Thunder':'../graphics/NinjaAdventure/FX/Elemental/Thunder/SpriteSheet.png',
            # monster deaths
            'axolot':'../graphics/NinjaAdventure/FX/Smoke/Smoke/SpriteSheet.png',
            'raccoon':'../graphics/NinjaAdventure/FX/Magic/Circle/SpriteSheetOrange.png',
            'Spirit':'../graphics/NinjaAdventure/FX/Magic/Spirit/SpriteSheetBlue.png',
            'bamboo':'../graphics/NinjaAdventure/FX/Elemental/Plant/SpriteSheetB.png',
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
        animation_frames = choice(self.frames['leaf'])
        self.image = pygame.image.load(animation_frames).convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        print('ares ',animation_frames)
        print(self.width)
        print(self.height)
        #ParticleEffect(pos,animation_frames,groups)
        
    def create_particles(self,animation_type,pos,groups):
        animation_frames = self.frames[animation_type]
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
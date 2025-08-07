import pygame


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
            'raccoon':,
            'Spirit':'../graphics/NinjaAdventure/FX/Magic/Spirit/SpriteSheetBlue.png',
            'bamboo':,
            # leafs
            
        }

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self,pos,animation_frames,groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.image.get_rect[self.frame_index]
        
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]
            
    def update(self):
        self.animate()
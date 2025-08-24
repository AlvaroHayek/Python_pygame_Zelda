import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Zelda like game')
        self.clock = pygame.time.Clock()
        self.level = Level()
        
        # mouse setup
        mouse_icon = pygame.image.load("../graphics/NinjaAdventure/Ui/mouse_icon.png").convert_alpha()
        new_mouse_size = (32,32)
        mouse_hotspot = (new_mouse_size[0]//2,new_mouse_size[1]//2)
        resized_mouse_icon = pygame.transform.scale(mouse_icon, new_mouse_size)
        #mouse_pos = pygame.mouse.get_pos()
        mouse_cursor = pygame.cursors.Cursor(mouse_hotspot,resized_mouse_icon)
        pygame.mouse.set_cursor(mouse_cursor)
        pygame.mouse.set_visible(False)
        
        # sound
        main_sound = pygame.mixer.Sound('../graphics/NinjaAdventure/Audio/Sounds/Ambient/Wind.wav')
        main_sound.set_volume(0.5)
        main_sound.play(loops=-1)
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()
                        if pygame.mouse.get_visible() == False:
                            pygame.mouse.set_visible(True)
                        else:
                            pygame.mouse.set_visible(False)
            
            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
            
if __name__ == '__main__':
    game = Game()
    game.run()
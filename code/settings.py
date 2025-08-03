# game setup
WIDTH = 1200
HEIGHT = 720
FPS = 60
TILESIZE = 64

# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../graphics/NinjaAdventure/Ui/Font/NormalFont.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# weapons
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic':'../graphics/NinjaAdventure/Items/Weapons/Sword/SpriteInHand.png', 'box':'../graphics/NinjaAdventure/Items/Weapons/Sword/Sprite.png'},
    'axe': {'cooldown': 400, 'damage': 30, 'graphic':'../graphics/NinjaAdventure/Items/Weapons/Axe/SpriteInHand.png', 'box':'../graphics/NinjaAdventure/Items/Weapons/Axe/Sprite.png'},
    'club': {'cooldown': 200, 'damage': 25, 'graphic':'../graphics/NinjaAdventure/Items/Weapons/Club/SpriteInHand.png', 'box':'../graphics/NinjaAdventure/Items/Weapons/Club/Sprite.png'},
    'rapier': {'cooldown': 50, 'damage': 8, 'graphic':'../graphics/NinjaAdventure/Items/Weapons/Rapier/SpriteInHand.png', 'box':'../graphics/NinjaAdventure/Items/Weapons/Rapier/Sprite.png'},
    'stick': {'cooldown': 90, 'damage': 12, 'graphic':'../graphics/NinjaAdventure/Items/Weapons/Stick/SpriteInHand.png', 'box':'../graphics/NinjaAdventure/Items/Weapons/Stick/Sprite.png'},
    'whip': {'cooldown': 150, 'damage': 20, 'graphic':'../graphics/NinjaAdventure/Items/Weapons/Whip/SpriteInHand.png', 'box':'../graphics/NinjaAdventure/Items/Weapons/Whip/Sprite.png'}}

# magic
magic_data = {
    'flame': {'strength': 5, 'cost': 20, 'graphic':'../graphics/NinjaAdventure/FX/Elemental/Flame/FlameBox.png'},
    'heal': {'strength': 20, 'cost': 10, 'graphic':'../graphics/NinjaAdventure/FX/Magic/Spark/SparkBox.png'}
}

# world map
WORLD_MAP = [
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ','x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ','x',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ','p',' ','x',' ',' ',' ',' ',' ',' ','x',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ','x',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ',' ','x',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ',' ',' ',' ',' ','x',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],
]
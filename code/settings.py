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

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

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

# enemy
monster_data = {
    'axolot': {'health':100,'exp':100,'damage':20,'attack_type':'Slash','attack_sound':'../graphics/NinjaAdventure/Audio/Sounds/Whoosh & Slash/Slash.wav','speed':3, 'resistance':3, 'attack_radius':80, 'notice_radius':360},
    'raccoon': {'health':300,'exp':250,'damage':40,'attack_type':'Cut','attack_sound':'../graphics/NinjaAdventure/Audio/Sounds/Hit & Impact/Hit1.wav','speed':2, 'resistance':3, 'attack_radius':120, 'notice_radius':400},
    'spirit': {'health':100,'exp':110,'damage':8,'attack_type':'Thunder','attack_sound':'../graphics/NinjaAdventure/Audio/Sounds/Elemental/Explosion2.wav','speed':4, 'resistance':3, 'attack_radius':60, 'notice_radius':350},
    'bamboo': {'health':70,'exp':120,'damage':6,'attack_type':'Plant','attack_sound':'../graphics/NinjaAdventure/Audio/Sounds/Whoosh & Slash/Slash5.wav','speed':3, 'resistance':3, 'attack_radius':50, 'notice_radius':300}
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
['w','w','w','w','w','w','w','w','w','w','x',' ',' ','x',' ','er',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ','eb',' ','x',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ','x',' ',' ',' ','ea',' ',' ',' ',' ',' ','x',' ',' ',' ',' ','er',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ','x',' ','es',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ','x',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ','p',' ','x',' ',' ',' ','ea',' ',' ','x',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ','x',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ',' ','x',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ',' ',' ',' ',' ','x',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ',' ','ea',' ',' ','x','x','x',' ',' ',' ','eb',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
['w','w','w','w','w','w','w','w','w','w','x',' ',' ',' ',' ',' ',' ',' ',' ','er',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','w','w','w','w','w','w','w','w'],
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
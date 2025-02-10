import pygame
from pathlib import Path

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# layers

LAYER_BG = 0
LAYER_ENTITY = 1
LAYER_GUI = 2
LAYER_CURSOR = 3

# Sprite files name convention: <prefix><number padding 4>.png (please don't use jpg)


def loadFolderIntoList(folderPath: str, prefix: str, list: list[pygame.Surface], startNum: int, endNum: int) -> list[pygame.Surface]:
    "Animation loader function, stores loaded frames inside list"
    for i in range(startNum, endNum):
        list.append(pygame.image.load(Path(folderPath) / f'{prefix}{i:04d}.png'))
    return list


# Loads assets into variables
# backgrounds
BG_TITLE = pygame.image.load((Path('./assets/background') / 'bg_title.png'))
BG_TITLE = pygame.transform.smoothscale(BG_TITLE, (SCREEN_WIDTH, SCREEN_HEIGHT))
BG_GARDEN = pygame.image.load((Path('./assets/background') / 'bg_shroom_garden.png'))
BG_GARDEN = pygame.transform.smoothscale(BG_GARDEN, (SCREEN_WIDTH, SCREEN_HEIGHT))

# particles
PARTICLE_POW = pygame.image.load((Path('./assets/particle') / 'Pow.png'))
PARTICLE_POW = pygame.transform.smoothscale(PARTICLE_POW, (70, 70))

# cursors
CURSOR_HAMMER_STATIC = pygame.image.load((Path('./assets/hammer') / 'hammer0001.png'))
CURSOR_HAMMER_ANIM = loadFolderIntoList('./assets/hammer', 'Hammer', [], 1, 9)

# gui

BUTTON_START = pygame.image.load((Path('./assets') / 'button_play.png'))
BUTTON_BACK = pygame.image.load((Path('./assets') / 'button_back.png'))

# zombies
ZOMBIE_ANIM_RISE = loadFolderIntoList('./assets/digger', 'Zombie_digger', [], 146, 180)
ZOMBIE_ANIM_IDLE = loadFolderIntoList('./assets/digger', 'Zombie_digger', [], 1, 18)
ZOMBIE_ANIM_LEAVE = loadFolderIntoList('./assets/digger', 'Zombie_digger', [], 1111, 1119)
ZOMBIE_ANIM_DEAD = loadFolderIntoList('./assets/digger', 'Zombie_digger', [], 89, 128)

# sounds

pygame.mixer.init()
SOUND_BTN = pygame.mixer.Sound((Path('./assets/sound') / 'buttonclick.ogg'))

SOUND_HAMMER_SWING = pygame.mixer.Sound((Path('./assets/sound') / 'swing.ogg'))
SOUND_HAMMER_BONK = pygame.mixer.Sound((Path('./assets/sound') / 'bonk.ogg'))

# music

MUSIC_TITLE = pygame.mixer.Sound((Path('./assets/sound') / 'Plants vs Zombies Soundtrack. [Main Menu].mp3'))
MUSIC_MAIN = pygame.mixer.Sound((Path('./assets/sound') / 'Plants vs Zombies Soundtrack. [Mini Games].mp3'))

# custom event

E_TYPE_ZOMBIE_HIT = pygame.USEREVENT + 1
E_ZOMBIE_HIT = pygame.event.Event(E_TYPE_ZOMBIE_HIT)
E_TYPE_ZOMBIE_MISS = pygame.USEREVENT + 2
E_ZOMBIE_MISS = pygame.event.Event(E_TYPE_ZOMBIE_MISS)

# font

pygame.font.init()
FONT = pygame.font.Font((Path('./assets') / 'Brianne_s_hand.ttf'), 24)

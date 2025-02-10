import pygame
from core import gameSpace, constants
from components.entity.Scene import Scene
from components.preset.Button import Button
from components.preset.Background import Background

SCENE_TITLE = Scene()


SCENE_TITLE.addEntity(constants.LAYER_BG, Background(constants.BG_TITLE))


def start():
    pygame.mixer.Channel(0).play(constants.MUSIC_TITLE, 1)


def exit():
    pygame.mixer.Channel(0).stop()


SCENE_TITLE.setStart(start)
SCENE_TITLE.setExit(exit)

BTN_START = Button((550, 350))

BTN_START.visibility.setStatic(constants.BUTTON_START)
BTN_START.hitbox.pos = BTN_START.visibility.pos
BTN_START.hitbox.sz = (209, 46)


def startGame(_, __):
    x, y = pygame.mouse.get_pos()
    if BTN_START.hitbox.isPointInHitbox((x, y)):
        gameSpace.sceneManager.switchScene('SCENE_MAIN')
        pygame.mixer.Channel(1).play(constants.SOUND_BTN)


BTN_START.eventListener._handlers[pygame.MOUSEBUTTONDOWN] = startGame

SCENE_TITLE.addEntity(constants.LAYER_GUI, BTN_START)

import pygame
from components.entity.Scene import Scene
from components.preset.Button import Button
from components.preset.Cursor import Cursor
from components.preset.Zombie import Zombie
from components.preset.Background import Background
from components.preset.Score import Score
from core import gameSpace, constants

# scene

SCENE_MAIN = Scene()
SCENE_MAIN.addEntity(constants.LAYER_BG, Background(constants.BG_GARDEN))

# score

SCORE = Score()
SCENE_MAIN.addEntity(constants.LAYER_GUI, SCORE)


def start():
    pygame.mixer.Channel(0).play(constants.MUSIC_MAIN, 1)
    SCORE.reset()
    if constants.LAYER_ENTITY in SCENE_MAIN.layers:
        SCENE_MAIN.layers[constants.LAYER_ENTITY].clear()

    # initiate zombies
    pos_list = [(609, 204), (910, 303), (552, 308), (730, 444), (401, 418), (183, 479), (501, 518), (826, 559)]

    for pos in pos_list:
        SCENE_MAIN.addEntity(constants.LAYER_ENTITY, Zombie(pos))


def exit():
    pygame.mixer.Channel(0).stop()


SCENE_MAIN.setStart(start)
SCENE_MAIN.setExit(exit)

# gui

BTN_BACK = Button()

BTN_BACK.visibility.setStatic(constants.BUTTON_BACK)
BTN_BACK.hitbox.sz = (209, 46)


def backToTitle(_, __):
    x, y = pygame.mouse.get_pos()
    if BTN_BACK.hitbox.isPointInHitbox((x, y)):
        gameSpace.sceneManager.switchScene('SCENE_TITLE')
    pygame.mixer.Channel(1).play(constants.SOUND_BTN)


BTN_BACK.eventListener._handlers[pygame.MOUSEBUTTONDOWN] = backToTitle

SCENE_MAIN.addEntity(constants.LAYER_GUI, BTN_BACK)

# cursor

CURSOR = Cursor()
CURSOR.visibility.setStatic(constants.CURSOR_HAMMER_STATIC, (-20, -35))
CURSOR.visibility.addAnimation(constants.CURSOR_HAMMER_ANIM, 'swing', 0.1, (-20, -35))


def swing(_, __):
    pygame.mixer.Channel(2).play(constants.SOUND_HAMMER_SWING)
    CURSOR.visibility.playAnimation('swing')


CURSOR.eventListener._handlers[pygame.MOUSEBUTTONDOWN] = swing

SCENE_MAIN.addEntity(constants.LAYER_CURSOR, CURSOR)

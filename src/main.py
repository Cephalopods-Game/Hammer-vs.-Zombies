import pygame
from core import gameSpace, EventHandler, constants
from components.entity.SceneManager import SceneManager
from components.preset.scene_main.scene_main import SCENE_MAIN
from components.preset.scene_title.scene_title import SCENE_TITLE


def init():
    pygame.init()
    pygame.display.set_caption("Hammer vs. Zombies")

    gameSpace.window = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    gameSpace.clock = pygame.time.Clock()

    # event handler
    gameSpace.eventHandler = EventHandler()

    # scenes
    gameSpace.sceneManager = SceneManager()
    gameSpace.sceneManager.addScene('SCENE_TITLE', SCENE_TITLE)
    gameSpace.sceneManager.addScene('SCENE_MAIN', SCENE_MAIN)
    gameSpace.sceneManager.switchScene('SCENE_TITLE')


def main():

    init()

    run = True
    while run:
        dt = gameSpace.clock.tick(120) / 1000

        gameSpace.sceneManager.currentScene.prep(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            gameSpace.eventHandler.handle(event, dt)
        gameSpace.sceneManager.draw(dt, 1)
        pygame.display.update()
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()

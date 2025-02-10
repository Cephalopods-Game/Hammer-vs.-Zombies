from core.game import gameSpace
from components.entity.Scene import Scene


class SceneManager:
    scenes: dict[str, Scene]
    currentScene: Scene

    def __init__(self):
        self.scenes = {}
        self.currentScene = None

    def addScene(self, name: str, scene: Scene):
        scene.start()
        self.scenes[name] = scene

    def removeScene(self, name: str):
        if name in self.scenes:
            self.scenes[name].exit()
            del self.scenes[name]

    def switchScene(self, name: str) -> None:
        if name not in self.scenes:
            return

        if self.currentScene:
            self.currentScene.exit()

            # unregister listeners
            for idx in self.currentScene.layers:
                for entity in self.currentScene.layers[idx]:
                    if hasattr(entity, 'eventListener'):
                        gameSpace.eventHandler.unregisterAll(entity.eventListener)

        # switch scene
        self.currentScene = self.scenes[name]
        self.currentScene.start()

        # registers the new listeners with event handler
        for idx in self.currentScene.layers:
            for entity in self.currentScene.layers[idx]:
                if hasattr(entity, 'eventListener'):
                    gameSpace.eventHandler.registerAll(entity.eventListener)

    def draw(self, dt: float, speed: int = 1):
        # check if entity has visibility property (and it's toggled on)
        for idx in sorted(self.currentScene.layers.keys()):
            for entity in self.currentScene.layers[idx]:
                if hasattr(entity, 'visibility'):
                    if entity.visibility.toggle:
                        data = entity.visibility.getSpriteData(dt, speed)
                        gameSpace.window.blit(data.sprite, tuple(
                            a + b for a, b in zip(data.pos, data.offset)))

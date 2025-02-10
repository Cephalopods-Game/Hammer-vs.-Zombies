from ..entity.Entity import Entity
from typing import Callable


class Scene():
    # layers are rendered starting from 0
    layers: dict[int, list[Entity]]

    def __init__(self):
        self.layers = {}

    # method to use when the scene is set at the current scene
    # executes before the event handler

    # usually you'd just want to call the entity's prep method
    def prep(self, dt: float) -> None:
        for _, entities in self.layers.items():
            for entity in entities:
                entity.prep(dt)

    # method to use when loading the scene into whatever
    # eg. resets entities' data and such
    def start(self) -> None:
        pass

    # method to use when unloading the scene
    def exit(self) -> None:
        pass

    # method setter methods (lol)
    # better not touch this, also i thought of making a hook but that is too much work for such a small game
    # and i'm not touching pygame again :skull:
    def setPrep(self, prep: Callable[[], None]) -> None:
        self.prep = prep

    def setStart(self, start: Callable[[], None]) -> None:
        self.start = start

    def setExit(self, exit: Callable[[], None]) -> None:
        self.exit = exit

    # methods to edit entity duh
    def addEntity(self, layer: int, entity: Entity) -> None:
        if layer not in self.layers:
            self.layers[layer] = []
        self.layers[layer].append(entity)

    def removeEntity(self, layer: int, entity: Entity) -> None:
        if layer in self.layers:
            self.layers[layer].remove(entity)

import pygame
from components.entity.Entity import Entity
from components.entity.property.Visibility import Visibility


class Background(Entity):
    visibility: Visibility

    def __init__(self, sprite: pygame.Surface):
        self.visibility = Visibility()
        self.visibility.static.sprite = sprite

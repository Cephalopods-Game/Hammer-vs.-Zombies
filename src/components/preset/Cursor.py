import pygame
from components.entity.Entity import Entity
from components.entity.property.Visibility import Visibility
from core import EventListener


class Cursor(Entity):
    eventListener: EventListener
    visibility: Visibility

    def __init__(self):
        self.eventListener = EventListener()
        self.visibility = Visibility()

    def prep(self, _):
        self.visibility.pos = pygame.mouse.get_pos()

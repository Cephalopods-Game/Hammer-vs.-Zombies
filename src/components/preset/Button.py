from components.entity.Entity import Entity
from components.entity.property.Hitbox import Hitbox
from components.entity.property.Visibility import Visibility
from core import EventListener


class Button(Entity):
    hitbox: Hitbox
    eventListener: EventListener
    visibility: Visibility

    def __init__(self, pos: tuple[int, int] = (0, 0)):
        self.hitbox = Hitbox()
        self.eventListener = EventListener()
        self.visibility = Visibility()
        self.visibility.pos = pos

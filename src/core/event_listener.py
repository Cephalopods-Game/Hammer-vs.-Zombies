import pygame
from typing import Callable


class EventListener():
    # Event type mapped to Function(event: pygame.event.Event, dt: float) -> None
    _handlers: dict[int, Callable[[pygame.event.Event, int], None]]

    def __init__(self):
        self._handlers = {}

    def onEvent(self, event: pygame.event.Event, dt: float) -> None:
        if event.type in self._handlers:
            self._handlers[event.type](event, dt)

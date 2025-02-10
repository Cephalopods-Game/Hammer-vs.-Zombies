import pygame
from .event_listener import EventListener


class EventHandler():
    _notifiers: dict[int, list[EventListener]] = {}

    def register(self, eventType: int, listener: EventListener) -> None:
        if eventType not in self._notifiers:
            self._notifiers[eventType] = []
        self._notifiers[eventType].append(listener)

    def registerAll(self, listener: EventListener) -> None:
        for eventType in listener._handlers:
            self.register(eventType, listener)

    def unregister(self, eventType: int, listener: EventListener) -> None:
        if eventType in self._notifiers and listener in self._notifiers[eventType]:
            self._notifiers[eventType].remove(listener)

    def unregisterAll(self, listener: EventListener) -> None:
        for eventType in listener._handlers:
            self.unregister(eventType, listener)

    def clear(self):
        self._notifiers.clear()

    def handle(self, event: pygame.event.Event, dt: float) -> None:
        if event.type in self._notifiers:
            for listener in self._notifiers[event.type]:
                listener.onEvent(event, dt)

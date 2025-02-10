import pygame
from components.entity.Entity import Entity
from components.entity.property.Visibility import Visibility
from core import constants, EventListener


class Score(Entity):
    visibility: Visibility
    eventListener: EventListener

    totalClicks: int
    hit: int
    miss: int

    def __init__(self):
        self.totalClicks = 0
        self.hit = 0
        self.miss = 0
        self.visibility = Visibility()
        self.visibility.pos = (20, 650)
        self.eventListener = EventListener()
        self.eventListener._handlers[constants.E_TYPE_ZOMBIE_HIT] = lambda _, __: self.registerHit()
        self.eventListener._handlers[pygame.MOUSEBUTTONDOWN] = lambda _, __: self.registerClick()
        self.eventListener._handlers[constants.E_TYPE_ZOMBIE_MISS] = lambda _, __: self.registerMiss()

    def reset(self):
        self.totalClicks = 0
        self.hit = 0
        self.miss = 0

    def getMiss(self):
        return self.totalClicks - self.hit + self.miss

    def getHit(self):
        return self.hit

    def registerClick(self):
        self.totalClicks += 1

    def registerHit(self):
        self.hit += 1

    def registerMiss(self):
        self.miss += 1

    def prep(self, _):
        strHit = 'HIT: ' + str(self.getHit())
        strMiss = ', MISS: ' + str(self.getMiss())
        self.visibility.setStatic(constants.FONT.render((strHit + strMiss), True, (255, 255, 255)))

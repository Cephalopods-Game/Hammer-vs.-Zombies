import pygame
import random
from components.entity.Entity import Entity
from components.entity.property.Hitbox import Hitbox
from components.entity.property.Visibility import Visibility
from core import EventListener, gameSpace, constants


class HitParticle(Entity):
    visibility: Visibility
    timeLeft: int

    def __init__(self, pos: tuple[int, int] = (0, 0)):
        self.visibility = Visibility()
        self.visibility.static.sprite = constants.PARTICLE_POW
        self.visibility.static.offset = (-35, -35)
        self.visibility.pos = pygame.mouse.get_pos()
        self.timeLeft = 1
        gameSpace.sceneManager.currentScene.addEntity(constants.LAYER_ENTITY, self)

    def prep(self, dt):
        self.timeLeft -= dt
        if self.timeLeft <= 0:
            gameSpace.sceneManager.currentScene.removeEntity(constants.LAYER_ENTITY, self)


class Zombie(Entity):
    hitbox: Hitbox
    eventListener: EventListener
    visibility: Visibility

    risen: bool
    timeLeft: float

    def __init__(self, pos: tuple[int, int] = (0, 0)):
        offset = (-60, -30)

        self.hitbox = Hitbox()
        self.hitbox.pos = pos
        self.hitbox.sz = (90, 130)
        self.eventListener = EventListener()
        self.eventListener._handlers[pygame.MOUSEBUTTONDOWN] = self.onClick
        self.visibility = Visibility()
        self.visibility.pos = pos
        self.visibility.addAnimation(constants.ZOMBIE_ANIM_RISE, 'rise', 1,  offset)
        self.visibility.addAnimation(constants.ZOMBIE_ANIM_IDLE, 'idle', 1, offset)
        self.visibility.addAnimation(constants.ZOMBIE_ANIM_LEAVE, 'leave', 0.5, offset)
        self.visibility.addAnimation(constants.ZOMBIE_ANIM_DEAD, 'dead', 1,  offset)
        self.risen = False
        self.timeLeft = 0

    def prep(self, dt):
        if self.visibility.toggle == False:
            self.visibility.toggle = True

        # dead or not initialized
        if self.risen == False:
            # only does thing when the 'previous' zombie left
            if self.visibility.animation['leave'].toggle == True:
                return

            # set timer for the next zombie to rise
            if self.timeLeft <= 0:
                self.timeLeft = random.uniform(3, 10)  # secs

            # if timer already exists, count down
            else:
                self.timeLeft -= dt
                if self.timeLeft <= 0:
                    self.risen = True
                    self.timeLeft += 5  # set time to stay for 5 seconds
                    self.visibility.playAnimation('rise')
        else:
            # risen / alive
            # finished rising
            if self.visibility.animation['rise'].toggle == False and self.visibility.animation['idle'].toggle == False:
                # loop the idle animation
                self.visibility.playAnimation('idle', True)

            self.timeLeft -= dt

            if self.timeLeft <= 0:
                # leave
                pygame.event.post(constants.E_ZOMBIE_MISS)
                self.risen = False
                self.visibility.playAnimation('leave')

    # DO NOT ALTER/ REGISTER A NEW EVENT LISTENER FOR MOUSECLICK
    def onClick(self, _, dt):
        if self.hitbox.isPointInHitbox(pygame.mouse.get_pos()) and self.risen:
            pygame.mixer.Channel(5).play(constants.SOUND_HAMMER_BONK)
            pygame.event.post(constants.E_ZOMBIE_HIT)
            HitParticle()
            # gameSpace.score.registerHit()
            self.risen = False
            self.visibility.playAnimation('dead')

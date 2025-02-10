import pygame

# to transfer info to the scene manager


class SpriteData:
    pos: tuple[int, int]
    offset: tuple[int, int]
    sprite: pygame.Surface

    def __init__(self, pos: tuple[int, int], offset: int,  sprite: pygame.Surface):
        self.pos = pos
        self.offset = offset
        self.sprite = sprite


class Static:
    offset: tuple[int, int]
    sprite: pygame.Surface

    def __init__(self, sprite: pygame.Surface = pygame.Surface((0, 0)), offset: tuple[int, int] = (0, 0)):
        self.sprite = sprite
        self.offset = offset

    def getSprite(self) -> tuple[tuple[int, int], pygame.Surface]:
        return (self.offset, self.sprite)


class Animation:
    toggle: bool
    loop: bool
    offset: tuple[int, int]
    duration: int
    currFrame: int
    sprites: list[pygame.Surface]
    accTime: int

    def __init__(self, sprites: list[pygame.Surface] = [], offset: tuple[int, int] = (0, 0)):
        self.toggle = False
        self.loop = False
        self.currFrame = 0
        self.sprites = sprites

        self.accTime = 0
        self.offset = offset
        self.duration = 0

    def reset(self):
        self.toggle = False
        self.currFrame = 0
        self.accTime = 0
        self.loop = False

    def getSprite(self, dt: float, speed: int) -> tuple[tuple[int, int], pygame.Surface]:
        timeStep = self.duration / speed / (len(self.sprites) - 1 or 1)
        ret = self.currFrame
        tmp = self.accTime
        self.accTime += dt

        if self.currFrame < len(self.sprites):
            if (tmp / timeStep) >= 1:
                self.currFrame += tmp / timeStep
                self.currFrame = int(self.currFrame)
                self.accTime = tmp % timeStep
        elif not self.loop:
            self.reset()
            return (self.offset, self.sprites[-1])
        else:
            self.currFrame = 0
            ret = 0

        return (self.offset, self.sprites[ret])


class Visibility:
    toggle: bool
    static: Static
    animation: dict[str, Animation]
    pos: tuple[int, int]

    def __init__(self, pos: tuple[int, int] = (0, 0)):
        self.toggle = True
        self.static = Static()
        self.animation = {}
        self.pos = pos

    def getSpriteData(self, dt: float, speed: int, pos: tuple[int, int] = None) -> SpriteData:
        if not self.toggle:
            return SpriteData((0, 0), (0, 0), pygame.Surface((0, 0)))
        # priority over animation first
        for _, anim in self.animation.items():
            if anim.toggle:
                offset, sprite = anim.getSprite(dt, speed)
                return SpriteData(pos or self.pos, offset, sprite)
        return SpriteData(pos or self.pos, self.static.offset, self.static.sprite)

    def playAnimation(self, name: str, loop: bool = False):
        for key in self.animation:
            self.animation[key].toggle = False

        if name in self.animation:
            self.animation[name].reset()
            self.animation[name].toggle = True
            self.animation[name].loop = loop

    def addAnimation(self, sprites: list[pygame.Surface], name: str, duration: int, offset: tuple[int, int] = (0, 0)):
        self.animation[name] = Animation(sprites, offset)
        self.animation[name].duration = duration

    def setStatic(self, sprite: pygame.Surface, offset: tuple[int, int] = (0, 0)):
        self.static.sprite = sprite
        self.static.offset = offset

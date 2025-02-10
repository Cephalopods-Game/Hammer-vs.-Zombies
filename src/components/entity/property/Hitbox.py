class Hitbox:
    pos: tuple[int, int]
    sz: tuple[int, int]

    def __init__(self, pos: tuple[int, int] = (0, 0), sz: tuple[int, int] = (0, 0)):
        self.pos = pos
        self.sz = sz

    def isPointInHitbox(self, pos: tuple[int, int]) -> bool:
        x, y = pos
        x1, y1 = self.pos
        x2, y2 = self.sz

        return x1 <= x <= x1 + x2 and y1 <= y <= y1 + y2

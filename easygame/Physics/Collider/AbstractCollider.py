from easygame.vector import Vector3


class Collision:
    def __init__(self,hitPos:Vector3,didHit:bool):
        self.hitPos = hitPos
        self.hit = didHit
class AbstractCollider:
    center:Vector3
    def __init__(self):
        pass
    def checkHit(self,ray)->Collision:
        raise NotImplementedError("Cant use AbstractCollider")
    def changePos(self,position):
        raise NotImplementedError("No")

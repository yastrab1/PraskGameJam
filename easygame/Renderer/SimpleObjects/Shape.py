from easygame.Physics.Collider.AbstractCollider import AbstractCollider


class Shape:
    def __init__(self,viewPort):
        viewPort.registerShape(self)
        self.collider:AbstractCollider = None
    def render(self):
        raise NotImplementedError("Not implemented")
    def move(self,pos):
        self.collider.changePos(pos)

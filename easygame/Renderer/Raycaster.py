from easygame.vector import Vector3


class Raycaster:
    @staticmethod
    def raycast(viewport, position, direction):
        pass


class Ray:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def lengthFromOrigin(self, point: Vector3):
        return (self.position - point).magnitude()

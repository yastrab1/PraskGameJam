from easygame.vector import Vector3


class Raycaster:
    @staticmethod
    def raycast(viewport, ray):
        collisions = []
        for obj in viewport.objects:
            collision =obj.collider.checkHit(ray)
            if not collision:
                continue
            collisions.append([collision,ray.lengthFromOrigin(collision.hitPos)])
            collisions = sorted(collisions, key=lambda x:x[1])
        return collisions[0][0]

class Ray:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def lengthFromOrigin(self, point: Vector3):
        return (self.position - point).magnitude()

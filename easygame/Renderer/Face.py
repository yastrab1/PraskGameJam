from easygame.Collider.AbstractCollider import Collision
from easygame.Renderer.Raycaster import Ray
from easygame.vector import Vector3


class Face:
    def __init__(self, vertices):
        self.vertices = vertices
        self.normal = self.calculateNormal()

    def calculateNormal(self):
        vec: Vector3 = self.vertices[0] @ self.vertices[1]
        return vec.normalize()

    def checkFaceHit(self, ray: Ray) -> Collision:
        normal = self.normal
        d = ((self.vertices[0] - ray.direction) * normal) / (normal * ray.direction)
        intersection = ray.direction * d + ray.position
        hit = True
        collision = Collision(intersection if hit else None, hit)
        return collision

    def inBounds(self, point:Vector3):
        result = (point - self.vertices[0]) * self.calculateNormal()
        return True if result == 0 else False

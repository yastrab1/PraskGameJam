from easygame.Collider.AbstractCollider import AbstractCollider, Collision
from easygame.Renderer.Face import Face
from easygame.Renderer.Raycaster import Ray
from easygame.vector import Vector3

class BallCollider(AbstractCollider):

    center: Vector3
    radius: float

    def __init__(self, center:Vector3, radius:float):
        self.center = center
        self.radius = radius

    def checkHit(self, ray: Ray) -> Collision:
        if (abs(ray.position*ray.direction) - abs(self.center*ray.direction))**2 - abs(ray.position*ray.position) + abs(self.center*self.center) + 2*abs(ray.position*self.center) + self.radius**2 < 0:
            return Collision(Vector3(), False)

        t = abs(self.center*ray.direction) - abs(ray.position, ray.direction) - (abs(ray.position*ray.direction) - abs(self.center*ray.direction))**2 - abs(ray.position*ray.position) + abs(self.center*self.center) + 2*abs(ray.position*self.center) + self.radius**2
        if t < 0:
            t = abs(self.center*ray.direction) - abs(ray.position, ray.direction) + (abs(ray.position*ray.direction) - abs(self.center*ray.direction))**2 - abs(ray.position*ray.position) + abs(self.center*self.center) + 2*abs(ray.position*self.center) + self.radius**2
        if t > 0:
            return Collision(ray.position + t*ray.direction, True)
        return Collision(Vector3(), False)
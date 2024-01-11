from easygame.Physics.Collider.AbstractCollider import AbstractCollider, Collision
from easygame.Renderer.Raycaster import Ray
from easygame.vector import Vector3

class BallCollider(AbstractCollider):

    center: Vector3
    radius: float

    def __init__(self, center: Vector3, radius: float):
        super().__init__()
        self.center = center
        self.radius = radius
    def changePos(self,position):
        self.center = position

    def checkHit(self, ray: Ray) -> Collision:
        if ray.position*ray.direction - self.center*ray.direction**2 - ray.position*ray.position + self.center*self.center + 2*ray.position*self.center + self.radius**2 < 0:
            return Collision(Vector3(), False)

        t = self.center*ray.direction - ray.position * ray.direction - (ray.position*ray.direction - self.center*ray.direction)**2 - ray.position*ray.position + self.center*self.center + 2*(ray.position*self.center) + self.radius**2
        if t < 0:
            t = (self.center*ray.direction) - (ray.position * ray.direction) + ((ray.position*ray.direction) - (self.center*ray.direction))**2 - (ray.position*ray.position) + (self.center*self.center) + 2*(ray.position*self.center) + self.radius**2
        if t > 0:
            return Collision(ray.position + t*ray.direction, True)
        return Collision(Vector3(), False)

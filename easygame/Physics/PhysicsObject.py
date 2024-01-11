from easygame.Renderer.Raycaster import Ray, Raycaster
from easygame.vector import Vector3

g = Vector3(0, 0, -.10)  # DO NOT CHANGE


class PhysicsObject:
    def __init__(self, viewPort, shape):
        self.viewPort = viewPort
        self.shape = shape
        self.velocity = Vector3(0, 0, 0)
        self.viewPort.registerPhysicsObject(self)

    def step(self, timeDelta):
        ray = Ray(self.shape.collider.center, g)
        collision = Raycaster.raycast(self.viewPort, ray)
        bottomPoint = collision.hitPos
        gravRay = Ray(bottomPoint - Vector3(0, 0, 0.1), g)
        gravityCollision = Raycaster.raycast(self.viewPort, gravRay)
        floorPos = gravityCollision.hitPos
        diff = floorPos - bottomPoint
        if diff.magnitude() < 1:
            self.velocity = Vector3(0, 0, 0)
        else:
            self.velocity += g * timeDelta
        print(self.velocity)
        self.shape.move(self.velocity)

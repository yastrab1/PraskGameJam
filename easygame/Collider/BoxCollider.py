from easygame.Collider.AbstractCollider import AbstractCollider, Collision
from easygame.Renderer.Face import Face
from easygame.Renderer.Raycaster import Ray
from easygame.vector import Vector3


class BoxCollider(AbstractCollider):
    def __init__(self, sideLengths: Vector3, corner: Vector3):
        super().__init__()
        self.vertices = [
            Vector3(corner.x,corner.y,corner.z),
            Vector3(corner.x+sideLengths.x,corner.y,corner.z),
            Vector3(corner.x,corner.y+sideLengths.y,corner.z),
            Vector3(corner.x+sideLengths.x,corner.y+sideLengths.y,corner.z),
            Vector3(corner.x,corner.y,corner.z+sideLengths.z),
            Vector3(corner.x+sideLengths.x,corner.y,corner.z+sideLengths.z),
            Vector3(corner.x,corner.y+sideLengths.y,corner.z+sideLengths.z),
            Vector3(corner.x+sideLengths.x,corner.y+sideLengths.y,corner.z+sideLengths.z)]
        self.faces = [
            Face([self.vertices[0],self.vertices[1],self.vertices[2],self.vertices[3]]),
            Face([self.vertices[3],self.vertices[2],self.vertices[7],self.vertices[6]]),
            Face([self.vertices[6],self.vertices[7],self.vertices[5],self.vertices[4]]),
            Face([self.vertices[4],self.vertices[5],self.vertices[1],self.vertices[0]]),
            Face([self.vertices[1],self.vertices[5],self.vertices[7],self.vertices[2]]),
            Face([self.vertices[4],self.vertices[0],self.vertices[3],self.vertices[6]])
        ]

    def checkHit(self,ray:Ray) -> Collision:
        collisions = []
        for face in self.faces:
            collision = face.checkFaceHit(ray)
            if not collision.hit:
                continue
            collisions.append([collision,ray.lengthFromOrigin(collision.hitPos)])
        collisions = sorted(collisions,key=lambda x:x[1])
        for collision in collisions:
            x,y,z = collision.hitPos

        return collisions[0][0]


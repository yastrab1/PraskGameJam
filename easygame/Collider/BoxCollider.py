from easygame.Collider.AbstractCollider import AbstractCollider, Collision
from easygame.Renderer.Raycaster import Ray
from easygame.vector import Vector3


class BoxCollider(AbstractCollider):
    def __init__(self,sideLengths:Vector3,corner:Vector3):
        self.vertices = [
            [corner],
            [Vector3(corner.x+sideLengths.x,corner.y,corner.z)],
            [Vector3(corner.x,corner.y+sideLengths.y,corner.z)],
            [Vector3(corner.x+sideLengths.x,corner.y+sideLengths.y,corner.z)],
            [corner.x,corner.y,corner.z+sideLengths.z],
            [corner.x+sideLengths.x,corner.y,corner.z+sideLengths.z],
            [corner.x,corner.y+sideLengths.y,corner.z+sideLengths.z],
            [corner.x+sideLengths.x,corner.y+sideLengths.y,corner.z+sideLengths.z]
        ]
        self.faces = [
            [self.vertices[0],self.vertices[1],self.vertices[2],self.vertices[3]],
            [self.vertices[3],self.vertices[2],self.vertices[7],self.vertices[6]],
            [self.vertices[6],self.vertices[7],self.vertices[5],self.vertices[4]],
            [self.vertices[4],self.vertices[5],self.vertices[1],self.vertices[0]],
            [self.vertices[1],self.vertices[5],self.vertices[7],self.vertices[2]],
            [self.vertices[4],self.vertices[0],self.vertices[3],self.vertices[6]]
        ]
    def checkFaceHit(self,face,ray:Ray) -> Collision:
        normal = self.calculateNormal(face)
        d = (face[0]-ray)*normal/(normal*ray.direction)
        intersection = ray.direction*d+ray.position
        hit = self.inBounds(intersection,face)
        collision = Collision(intersection if hit else None,hit)
        return collision
    def checkHit(self,ray:Ray) -> Collision:
        collisions = []
        for face in self.faces:
            collision = self.checkFaceHit(face,ray)
            if not collision.hit:
                continue
            collisions.append([collision,ray.lengthFromOrigin(collision.hitPos)])
        collisions = sorted(collisions,key=lambda x:x[1])
        return collisions[0][0]

    def calculateNormal(self,face):
        vec:Vector3 = face[0]@face[1]
        return vec.normalize()
    def inBounds(self,point,face):
        result = (point-face[0])*self.calculateNormal(face)
        return True if result == 0 else False

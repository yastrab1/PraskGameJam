from easygame.Physics.Collider.BallCollider import BallCollider
from easygame.Renderer.Raycaster import Ray
from easygame.vector import Vector3

ball = BallCollider(Vector3(0, 0, 0), 5)

ray = Ray(Vector3(-5, 1.1, 0), Vector3(1, 0, 0))

print(ball.checkHit(ray).hit)

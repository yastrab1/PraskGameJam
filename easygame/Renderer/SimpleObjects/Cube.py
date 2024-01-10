from OpenGL.GL import *

from easygame.Renderer.SimpleObjects.Shape import Shape

vertices= (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

# maps how to connected vertices
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)

# rgb in float 0-1 values
colors = (
    (1,0,0), #r
    (0,1,0), #g
    (0,0,1), #b
    (0,1,0), #g
    (1,1,1), #wh
    (0,1,1), #cy
    (1,0,0), #r
    (0,1,0), #g
    (0,0,1), #b
    (1,0,0), #r
    (1,1,1), #wh
    (0,1,1), #cy
)

# surfaces are groups of vertices
# indexes to the vertices list
surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
)

class Cube(Shape):
    def __init__(self,  viewPort,position, sides, color):
        super().__init__(viewPort)
        self.position = position
        self.sides = sides
        self.color = color
        self.vertices = [[vertex[posIndex]*sides[posIndex]for posIndex in range(3)]for vertex in vertices]
        print(self.vertices)
    def render(self):
        glBegin(GL_QUADS)
        for surface in surfaces:
            x = 0
            for vertex in surface:
                x += 1
                glColor3fv(self.color)
                glVertex3fv(self.vertices[vertex])
        glEnd()

        # render lines between vertices
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glColor3fv([1,1,1])
                glVertex3fv(self.vertices[vertex])
        glEnd()
    def setColor(self,color):
        self.color = color

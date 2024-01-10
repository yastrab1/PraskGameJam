from OpenGL.GL import *

from easygame.Renderer.SimpleObjects.Shape import Shape

class Mesh(Shape):
    def __init__(self,  viewPort, position, triangles, material):
        super().__init__(viewPort)
        self.position = position
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

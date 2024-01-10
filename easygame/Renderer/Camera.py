from OpenGL.raw.GL.VERSION.GL_1_0 import glTranslatef, glRotatef
from OpenGL.raw.GLU import *


class Camera:
    def __init__(self,position,rotation=None,screenSize=(1980,1200)):
        self.position = position
        self.rotation = rotation
        gluPerspective(45, (screenSize.x / screenSize.y), 0.1, 50.0)

        if not rotation:
            return
        self.rotate(rotation)
    def setPosition(self,position):
        self.position = position
        glTranslatef(position.x,position.y,position.z)
    def rotate(self,eulerAngles):
        glRotatef(eulerAngles[0], 1, 0, 0)
        glRotatef(eulerAngles[1], 0, 1, 0)
        glRotatef(eulerAngles[2], 0, 0, 1)
    def translate(self,position):
        self.position += position
        glTranslatef(position.x,position.y,position.z)

from OpenGL.raw.GL.VERSION.GL_1_0 import glTranslatef, glRotatef
from OpenGL.raw.GLU import *


class Camera:
    def __init__(self,position,rotation,screenSize):
        self.position = position
        self.rotation = rotation
        gluPerspective(45, (screenSize.x / screenSize.y), 0.1, 50.0)
        # move perspective by x, y, z (-5 to be back from cube)
        self.rotate(rotation)
    def setPosition(self,position):
        self.position = position
        glTranslatef([position.x,position.y,position.z])
    def rotate(self,quaternion):
        glRotatef(quaternion.eulerX, 1, 0, 0)
        glRotatef(quaternion.eulerX, 0, 1, 0)
        glRotatef(quaternion.eulerX, 0, 0, 1)


import math

from OpenGL.raw.GL.VERSION.GL_1_0 import *
from OpenGL.raw.GLU import *

from easygame.vector import Vector3


class Camera:
    def __init__(self,position,rotation=None,screenSize=(1980,1200)):
        self.position = position
        self.rotation = rotation
        gluPerspective(45, (screenSize.x / screenSize.y), 0.1, 5000.0)
        self._currentLookingPoint = Vector3(1,0,0)
        if not rotation:
            return
        self.rotate(rotation)
    def setPosition(self,position):
        self.position = position
        glTranslatef(position.x,position.y,position.z)
    def setRotation(self,eulerAngles):
        self.rotation = eulerAngles
        glTranslatef(-self.position.x,-self.position.y,-self.position.z)
        glRotatef(eulerAngles[0],1,0,0)
    def rotate(self,eulerAngles):
        self.rotation+=eulerAngles
        self.setRotation(self.rotation)
    def translate(self,position):
        glMatrixMode(GL_MODELVIEW)
        self.position += position
        glTranslatef(position.x,position.y,position.z)

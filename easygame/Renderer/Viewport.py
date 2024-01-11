import pygame
from OpenGL.raw.GL.VERSION.GL_1_0 import *

from easygame.Physics.PhysicsObject import PhysicsObject
from easygame.Renderer.SimpleObjects import Shape


class Viewport:
    def __init__(self):
        self.objects = []
        self.physicsObjects = []
        self.prevTime = 0
    def registerShape(self, object:Shape):
        self.objects.append(object)
    def registerPhysicsObject(self,object:PhysicsObject):
        self.physicsObjects.append(object)
    def render(self):

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        for obj in self.objects:
            obj.render()
        currentTime = pygame.time.get_ticks()
        for obj in self.physicsObjects:
            obj.step((currentTime - self.prevTime)/1000)
        self.prevTime = currentTime

from OpenGL.raw.GL.VERSION.GL_1_0 import *

from easygame.Renderer.SimpleObjects import Shape


class Viewport:
    def __init__(self):
        self.objects = []
    def register(self,object:Shape):
        self.objects.append(object)
    def render(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        for obj in self.objects:
            obj.render()

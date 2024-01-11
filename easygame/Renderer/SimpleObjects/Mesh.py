from OpenGL.GL import *
import pywavefront
from easygame.Renderer.SimpleObjects.Shape import Shape

class Mesh(Shape):
    def __init__(self,viewPort,path):
        super().__init__(viewPort)
        self.loadFromFile(path)
        self.color = (1,1,1)
        print("Finished loading")
    def loadFromFile(self,path):
        # scene = pywavefront.Wavefront(path)
        # for name,material in scene.materials.items():
            # print("material format"+material.vertex_format)
        pass
            # self.vertices = material.vertices
    def render(self):
        pass
    def setColor(self,color):
        self.color = color

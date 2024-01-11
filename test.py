import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from easygame.Input import InputSystem
from easygame.Renderer.Camera import Camera
from easygame.Renderer.SimpleObjects.Cube import Cube
from easygame.Renderer.SimpleObjects.Mesh import Mesh
from easygame.Renderer.Viewport import Viewport
from easygame.vector import Vector3, Vector2


# https://pythonprogramming.net/coloring-pyopengl-surfaces-python-opengl



def main():
    inputSystem = InputSystem()
    pygame.init()
    display = (1280, 720)
    # DOUBLEBUF is a type of buffering where there are
    # two buffers to comply with monitor refresh rates
    # OPENGL says we will be doing opengl calls
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    camera = Camera(Vector3(0,0,0),rotation=(50,25,0),screenSize=Vector2(*display))
    viewPort = Viewport()

    fish = Mesh(viewPort, "13007_Blue_Green_Reef_Chromis_v1.obj")
    cube = Cube(viewPort,Vector3(10,10,10),(10,10,10),(0,0,0))
    cube2 = Cube(viewPort,Vector3(20,20,20),(5,10,2),(0,0,0))
    r, g, b = 0, 0, 0
    # game loop
    while True:

        # pygame events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        inputSystem.step(events)
        if inputSystem.isKeyPressed(pygame.K_a):
            camera.translate(Vector3(0.1,0,0))
        if inputSystem.isKeyPressed(pygame.K_d):
            camera.translate(Vector3(-0.1, 0, 0))
        if inputSystem.isKeyPressed(pygame.K_w):
            camera.translate(Vector3(0,0.1,0))
        if inputSystem.isKeyPressed(pygame.K_s):
            camera.translate(Vector3(0,-0.1,0))
        if inputSystem.isKeyPressed(pygame.K_q):
            camera.translate(Vector3(0,0,0.1))
        if inputSystem.isKeyPressed(pygame.K_e):
            camera.translate(Vector3(0, 0, -0.1))
        if inputSystem.isKeyPressed(pygame.K_LEFT):
            camera.rotate((1,0,0))
        if inputSystem.isKeyPressed(pygame.K_RIGHT):
            camera.rotate((-1,0,0))
        if inputSystem.isKeyPressed(pygame.K_UP):
            camera.rotate((0,1,0))
        if inputSystem.isKeyPressed(pygame.K_DOWN):
            camera.rotate((0,-1,0))
        if inputSystem.isKeyPressed(pygame.K_PAGEUP):
            camera.rotate((0,0,1))
        if inputSystem.isKeyPressed(pygame.K_PAGEDOWN):
            camera.rotate((0,0,-1))

        # render cube lines
        viewPort.render()

        colors = updateColors(r,g,b)
        r,g,b = colors
        cube.setColor((r,g,b))
        cube2.setColor((r,g,b))
        # update display
        pygame.display.flip()
        # update loop sleep
        pygame.time.wait(10)
def updateColors(r,g,b):
    if r<1:
        r+=1/10
        return r,g,b
    if g<1:
        g+=1/10
        r=0
        return r,g,b
    if b<1:
        b+=1/10
        g=0
        r=0
        return r,g,b
    return 0,0,0
main()

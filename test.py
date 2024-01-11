import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from easygame.Input import InputSystem
from easygame.Renderer.Camera import Camera
from easygame.Renderer.Raycaster import Raycaster, Ray
from easygame.Renderer.SimpleObjects.Cube import Cube
from easygame.Renderer.SimpleObjects.Mesh import Mesh
from easygame.Renderer.Viewport import Viewport
from easygame.vector import Vector3, Vector2


# https://pythonprogramming.net/coloring-pyopengl-surfaces-python-opengl



def main():
    prevTime = 0
    inputSystem = InputSystem()
    pygame.init()
    display = (1280,720)
    # DOUBLEBUF is a type of buffering where there are
    # two buffers to comply with monitor refresh rates
    # OPENGL says we will be doing opengl calls
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    camera = Camera(Vector3(0,0,0),rotation=(0,0,0),screenSize=Vector2(*display))
    viewPort = Viewport()

    cubes = []
    for i in range(4):
        cube = Cube(viewPort, Vector3(i,i,i), Vector3(1, 1, 1), (i*5, i*5, i*5),True)
        cubes.append(cube)
    r, g, b = 0, 0, 0
    # nonPhysicsCube = Cube(viewPort,Vector3(-10,-10,-10),Vector3(20,20,1),(255,255,255),False)
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

        for i in range(len(cubes)):
            cube = cubes[i]
            color = updateColors(*cube.color)
            cubes[i].setColor(color)

        colors = updateColors(r,g,b)
        r,g,b = colors
        # prevTime = pygame.time.get_ticks()
        # Raycaster.raycast(viewPort,Ray(camera.position,Vector3(1,0,0))).hitPos
        # afterTime = pygame.time.get_ticks()

        # update display
        pygame.display.flip()
        # update loop sleep
        # diff = afterTime-prevTime
        # fps = 1000/diff
        # print(fps)
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

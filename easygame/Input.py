import pygame.key


class InputSystem:
    def __init__(self):
        self.keyHooks = {}

    def registerHookOnKeyPress(self,key,hook):
        """Fires when a key is pressed"""
        if not key in self.keyHooks.keys():
            self.keyHooks[key] = []
        self.keyHooks[key].append(hook)
    def isKeyPressed(self,key):
        return pygame.key.get_pressed()[key]
    def step(self,events):
            for event in events:
                if event.type == pygame.KEYDOWN:
                    for key,value in self.keyHooks.items():
                        for hook in value:
                            hook()

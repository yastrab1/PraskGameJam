from easygame.Renderer.SimpleObjects import Shape


class Viewport:
    def __init__(self):
        self.objects = []
    def register(self,object:Shape):
        self.objects.append(object)
    def render(self):
        for obj in self.objects:
            obj.render()

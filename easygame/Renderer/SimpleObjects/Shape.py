class Shape:
    def __init__(self,viewPort):
        viewPort.register(self)
        self.collider = None
    def render(self):
        raise NotImplementedError("Not implemented")

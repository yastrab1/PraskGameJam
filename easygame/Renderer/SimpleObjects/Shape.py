class Shape:
    def __init__(self,viewPort):
        viewPort.register(self)
    def render(self):
        raise NotImplementedError("Not implemented")

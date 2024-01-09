import numpy as np


class Vector2:

    _this: np.ndarray

    def __init__(self, a: float = 0, b: float = 0):
        _this = np.array((a, b))

    def __getattribute__(self, item):
        if item == "x":
            return self._this[0]
        elif item == "y":
            return self._this[1]

    def __setattr__(self, key, value):
        if key == "x":
            self._this[0] = value
        if key == "y":
            self._this[1] = value

    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5

    def __add__(self, b):
        if type(b) != Vector2:
            raise TypeError(f"Cannot add Vector2 and {type(b)}")
        return Vector2(self.x + b.x, self.y + b.y)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __sub__(self, b):
        if type(b) != Vector2:
            raise TypeError(f"Cannot subtract {type(other)} from Vector2")
        return Vector2(self.x - b.x, self.y - b.y)

    def __mul__(self, b):
        if type(b) == Vector2:
            return self.dot(b._this)
        elif type(b) in (int, float):
            return Vector2(self.x * b, self.y * b)

    def __truediv__(self, b):
        if type(b) in (float, int):
            if b == 0:
                raise ZeroDivisionError("Cannot divide Vector2 by zero")
            return Vector2(self.x/b, self.y/b)
        raise TypeError(f'Cannot divide Vector2 by {type(b)}')


class Vector3:
    _this:np.ndarray
    def __init__(self,x,y,z):
        self._this = np.ndarray([0,0,0])
        self._this.x = x
        self._this.y = y
        self._this.z = z
    def __getattribute__(self, item):
        if item == "x":
            return self._this[0]
        if item == "y":
            return self._this[1]
        if item == "z":
            return self._this[2]
    def __setattr__(self, key, value):
        if key == "x":
            self._this[0] = value
        if key == "y":
            self._this[1] = value
        if key == "z":
            self._this[2] = value
    def __mul__(self, other):
        return Vector3(self.x * other.x, self.y * other.y,self.z*other.z)
    def __matmul__(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z* other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector3(x,y,z)

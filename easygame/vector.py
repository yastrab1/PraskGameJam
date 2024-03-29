import numpy
import numpy as np


class Vector2:

    x: float
    y: float

    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x}, {self.y}]"

    def __repr__(self):
        return str(self)

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
            raise TypeError(f"Cannot subtract {type(b)} from Vector2")
        return Vector2(self.x - b.x, self.y - b.y)

    def __mul__(self, b):
        if type(b) == Vector2:
            return Vector2(self.x*b.x, self.y*b.y)
        elif type(b) in (int, float):
            return Vector2(self.x * b, self.y * b)
        elif type(b) == np.ndarray:
            if b.shape == (2,):
                return self.x * b[0] + self.y * b[1]
            elif b.shape == (2, 3):
                return b@np.array([self.x, self.y])
            elif b.shape == (2, 2):
                return b@np.array([self.x, self.y])
            else:
                raise TypeError(f"Cannot multiply Vector3 and np.ndarray of shape {b.shape}")

    def __truediv__(self, b):
        if type(b) in (float, int):
            if b == 0:
                raise ZeroDivisionError("Cannot divide Vector2 by zero")
            return Vector2(self.x/b, self.y/b)
        raise TypeError(f'Cannot divide Vector2 by {type(b)}')


class Vector3:

    x: float
    y: float
    z: float

    def __init__(self, x:float=0, y:float=0, z:float=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"[{self.x}, {self.y}, {self.z}]"

    def __repr__(self):
        return str(self)

    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**.5

    def __add__(self, other):
        if type(other) != Vector3:
            raise TypeError(f"Cannot add Vector3 and {type(other)}")
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if type(other) != Vector3:
            raise TypeError(f"Cannot subtract Vector3 and {type(other)}")
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)


    def __mul__(self, other):
        if isinstance(other,Vector3):
            return self.x * other.x+self.y * other.y+self.z*other.z
        elif isinstance(other,int) or isinstance(other,float) or isinstance(other,numpy.float64):
            return Vector3(self.x*other, self.y*other, self.z*other)
        elif type(other) is type(np.ndarray):
            if other.shape == (3,):
                return self.x * other[0] + self.y * other[1] + self.z * other[2]
            elif other.shape == (3, 3):
                return other@np.array([self.x, self.y, self.z])
            elif other.shape == (3, 2):
                return other@np.array([self.x, self.y, self.z])
            else:
                raise TypeError(f"Cannot multiply Vector3 and np.ndarray of shape {other.shape}")
        else:
            raise TypeError(f"Cannot multiply Vector3 and {type(other)}")
    def __rmul__(self, other):
        return self*other
    def __matmul__(self, other):
        y = self.y * other.z - self.z * other.y
        z = self.z* other.x - self.x * other.z
        x = self.x * other.y - self.y * other.x
        return Vector3(x,y,z)
    def __truediv__(self, other):
        return Vector3(self.x/other, self.y/other, self.z/other)

    def magnitude(self):
        return np.sqrt(self.x**2+self.y**2+self.z**2)
    def normalize(self):
        return self/self.magnitude()
    def getAxisByIndex(self, item):
        if item == 0:
            return self.x
        if item == 1:
            return self.y
        if item == 2:
            return self.z

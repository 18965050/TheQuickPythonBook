x = 5 + 2 - 3 * 2

print(x)

y=0.2
import math
print(math.ceil(y))

x = ["first", "second", "third", "fourth"]

print(x[-1:-4])

print(x[-1:1])

print(x[1:-1])

print(x[-4:-1])

x = {1: "one", 2: "two"}

x[("Delorme", "Ryan", 1995)] = (1, 2, 3)

# x[["Delorme", "Ryan", 1995]] = (1, 2, 3)    #error: dict的key一定是不可变类

print(x.keys())

# def funct2(x, y=1, z):  #error: 默认参数要从最后一个开始
#     return x + 2 * y + z ** 2

"""sh module. Contains classes Shape, Square and Circle"""
class Shape:
    """Shape class: has method move"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        self.x = self.x + deltaX
        self.y = self.y + deltaY

class Square(Shape):
    """Square Class:inherits from Shape"""
    def __init__(self, side=1, x=0, y=0):
        Shape.__init__(self, x, y)
        self.side = side

class Circle(Shape):
    """Circle Class: inherits from Shape and has method area"""
    pi = 3.14159
    def __init__(self, r=1, x=0, y=0):
        Shape.__init__(self, x, y)
        self.radius = r
    def area(self):
        """Circle area method: returns the area of the circle."""
        return self.radius * self.radius * self.pi
    def __str__(self):
        return "Circle of radius %s at coordinates (%d, %d)" \
               % (self.radius, self.x, self.y)
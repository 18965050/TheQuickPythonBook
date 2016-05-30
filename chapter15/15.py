# class Circle:
#     pi = 3.14159		#类变量
#     def __init__(self, radius):
#         self.radius = radius	#实例变量
#
#     def area(self):
#         return self.radius * self.radius * Circle.pi     #Circle.pi不能写成pi, 但可以写成self.__class__.pi
#
# circle=Circle(5)
# print(circle.area())


# """circle module: contains the Circle class."""
# class Circle:
#     """Circle class"""
#     # Variable containing a list of all circles which have been created.
#     all_circles = []
#     pi = 3.14159
#     def __init__(self, r=1):
#         """Create a Circle with the given radius"""
#         self.radius = r
#         self.__class__.all_circles.append(self)
#     def area(self):
#         """determine the area of the Circle"""
#         return self.__class__.pi * self.radius * self.radius
#
#     @staticmethod
#     def total_area():
#         total = 0
#         for c in Circle.all_circles:
#             total = total + c.area()
#         return total
#
# c1 = Circle(1)
# c2 = Circle(2)
# print(Circle.total_area())
#
#
# class P:
#     z="hello"
#
# class C(P):
#     pass
#
# c=C()
# print(c.z)
# print(C.z)
# print(P.z)
#
# C.z="world"
# print(c.z)
# print(C.z)
# print(P.z)

# class Mine:
#     def __init__(self):
#         self.x = 2
#         # Define __y as private by using leading double underscores.
#         self.__y = 3
#     def print_y(self):
#         print(self.__y)
#
# m=Mine()
# print(m.x)
# # print(m.__y)
#
# class Temperature:
#     def __init__(self):
#         self._temp_fahr = 0
#     @property
#     def temp(self):
#         return (self._temp_fahr - 32) * 5/9
#     @temp.setter
#     def temp(self, new_temp):
#         self._temp_fahr = new_temp * 9/5 + 32
#
# t = Temperature()
# print(t._temp_fahr)
# print(t.temp)
#
# t.temp = 34
# print(t._temp_fahr)
# print(t.temp)

class Circle:
    def __init__(self, name, parent):
        self.__name = name
        self.__parent = parent
        self.__child = None
        if parent:
            parent._child = self
    def cleanup(self):
        self.__child = self.__parent = None
    def __del__(self):
        print("__del__ called on", self.__name)

def test1():
    a = Circle("a", None)
    b = Circle("b", a)

def test2():
    c = Circle("c", None)
    d = Circle("d", c)
    # d.cleanup()

test1()
test2()
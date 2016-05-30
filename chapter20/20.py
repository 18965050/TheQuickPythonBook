# class Spam:
#     def __init__(self, x):
#         self.x = x
#
#     def show(self):
#         print(self.x)
#
# def init(self, x):
#     self.x = x
# def show(self):
#     print(self.x)
#
# Spam = type("Spam", (object,), {'__init__': init, 'show': show})
#
# d=Spam("3")
# d.show()

#
# class NewType(type):
#     def __init__(cls, name, bases, methods):
#         print("Creating from NewType")
#         type.__init__(cls, name, bases, methods)
#         cls.new_attr = "test"
#
# def __init__(self, x):
#     self.x = x
#
# def show(self):
#     print(self.x)
#
# spam = NewType("Spam", (object,), {'__init__':__init__, 'show':show})
#
# print(spam.new_attr)
#
# my_spam = Spam("test")
#
# print(type(Spam))
#
# print(type(spam))

from abc import ABCMeta

# class MyABC(metaclass=ABCMeta):
#     pass

from abc import ABCMeta, abstractmethod
class MyABC(metaclass=ABCMeta):
    @abstractmethod
    def overrideme(self):
        print("in ABC")

my_MyABC = MyABC()
# print(type(my_MyABC))


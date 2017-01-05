file_object = open("myfile", 'r')

file_object.close()

class A:
    pass

class B(A):
    pass

class C:
    pass

class D(B,C):
    pass

d=D()
print(isinstance(d,B))
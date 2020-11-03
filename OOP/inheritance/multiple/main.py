class A:
    def a_method(self):
        print('This is a method form A')

class B:
    def b_method(self):
        print('This is a method form B')

# multiple inheritance
class C(A,B):
    def c_method(self):
        print('This is a method form C')

c_object = C()
c_object.a_method()
c_object.b_method()
c_object.c_method()


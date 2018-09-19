class Parent(object):
    def spam(self):
        print('Parent.spam')

p = Parent()
p.spam()


class A(Parent):
    def spam(self):
        print('A.spam')
        super().spam()

a = A()
a.spam()


class B(A):
    def spam(self):
        print('B.spam')
        super().spam()

b = B()
b.spam()

print(B.__mro__) # method resolution 


class C(Parent):
    def spam(self):
        print('C.spam')
        super().spam()

c = C()
c.spam()


class D(Parent):
    def spam(self):
        print('D.spam')
        super().spam()

d = D()
d.spam()        


class E(A, C, D):
    pass

e = E()
e.spam()


class F(D, C, A):
    pass

f = F()
f.spam()

print(F.__mro__)

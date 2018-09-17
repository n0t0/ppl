class Parent(object):
    def __init__(self, value):
        self.value = value 

    def spam(self):
        print('Parent.spam', self.value)

    def grok(self):
        print('Parent.grok')
        self.spam()

p = Parent(42)
print(p.value)

p.spam()
p.grok()


class Child1(Parent):
    def yow(self):
        print('Child1.yow')

c = Child1(22)
print(c.value)
c.spam()
c.grok()
c.yow()


class Child2(Parent):
    def spam(self):
        print('Child2.spam', self.value)

c2 = Child2(23)
print(c2.value)
c2.spam()
c2.grok()


class Child3(Parent):
    def spam(self):
        print('Child3.spam')
        super().spam()  # Invokes the original spam()

c3 = Child3(42)
c3.spam()
c3.grok()


class Child4(Parent):
    def __init__(self, value, extra):
        self.extra = extra
        super().__init__(value)   # Initialize parent 

c4 = Child4(42, 36)
print(c4.extra)


class Parent2(object):
    def yow(self):
        print('Parent2.yow')


class Child5(Parent, Parent2):
    pass

c5 = Child5(42)
c5.spam()
c5.yow()
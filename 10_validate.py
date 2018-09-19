class Typed(object):
    expected_type = object 

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected {}'.format(self.expected_type))
        instance.__dict__[self.name] = value


class Integer(Typed):
    expected_type = int


class Point(Typed):
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2,3)
print(p.x)
print(p.y)
# p.x = 'a lot' # blows up 
p.z = 45 
print(p.z)
p.z = 'a lot'
print(p.z)


class Float(Typed):
    expected_type = float


class Holding(object):
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares 
        self.price = price
    
    @property 
    def cost(self):
        return self.shares * self.price


h = Holding('AA', '2016-11-20', 300, 10.4)
print(h.shares)

class String(Typed):
    expected_type = str
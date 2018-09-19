import csv 

class Holding(object):
    
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, newprice):
        if not isinstance(newprice, float):
            raise TypeError('Expected float')
        self._price = newprice

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, newshares):
        if not isinstance(newshares, int):
            raise TypeError('Expected int')
        self._shares = newshares

    def __repr__(self):
        return 'Holding({!r},{!r},{!r},{!r})'.format(self.name, self.date, self.shares, self.price)

    def __str__(self):
        return '{} shares of {} at ${:0.2f}'.format(self.shares, self.name, self.price)

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

h = Holding('AA', '2017-09-21', 100, 32.4)
print(h)
print(h.__dict__)
# print(h.__dict__['shares'])
h.__dict__['yow'] = 42
print(h.yow)

g = Holding('IBM', '2017-04-14', 50, 45.5)
print(g.__dict__)
 
print(h.__class__)
print(Holding.__dict__)
print(Holding.__dict__['cost']) # find it in the dictionary 
# print(Holding.__dict__['cost'](h)) # pass `h` to it 

#### Naming Convention ####

class Spam(object):
    def __init__(self, value):
        self._value = value # "Private or Internal"

s = Spam(42)
s._value

#### Managed Atributes with Properties #### 

h = Holding('AA', '2017-09-21', 100, 32.4)

# @property

#### Managed Atributes with Descriptors #### 

h = Holding('AA', '2017-09-21', 100, 32.4)
p = _
print(type(_))
# holding = {'name': 'AA', 'date': '2007-06-11', 'shares': 100, 'price': 32.2}
# print(holding['name'])

class Holding(object):
    
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date 
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price 

    def sell(self, nshares):
        self.shares -= nshares 

# 3 attributes ( get, set, delete)

h = Holding('AA', '2007-06-22', 100, 44.7)
print(h.name)
h.shares = 50
print(h.shares)
del h.shares
# print(h.shares)
h.shares = 75

# Create an antribute 

h.time = '08:54am'
print(h.time)
 
print(h.name)
print(h.shares)
print(h.price)
print(h.cost())

getattr(h, 'name')
print(h.name)
setattr(h, 'name', 'AAPL') # h.name = 'APPL' 
getattr(h, 'name')
print(h.name)

output_columns = ['name', 'shares', 'price']

for colname in output_columns:
    print(colname, '=', getattr(h, colname))


def print_table(objects, colnames):
    """
    Create a formatted table showing attributes fom a list of objects 
    """ 

    for colname in colnames:
        print('{:>10s}'.format(colname), end=' ')
    print()
    
    for obj in objects: 
        for colname in colnames:
            print('{:>10s}'.format(str(getattr(obj, colname))), end=' ')
        print()


# t = ('AA', '2011-06-07', 100, 32.2)
# print(t)

# print(len(t))

# name, date, shares, price = t
# print(name)
# print(t)


import csv 
import glob

def read_portfolio(filename, *, errors='warn'):
    """
    Read a CSV file to compute base pay + overtime pay as a total pay
    """

    portfolio = [] 
    # total = 0.0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            try:
                row[3] = float(row[3])
                row[4] = float(row[4])
            except ValueError as err:
                print('Row:', rowno, 'Bad row:', row)
                print('Row:', rowno, 'Reason:', err)
                continue 
            # record = tuple(row)   
            record = { 
                'id': row[0],
                'name': row[1],
                'jobtitle': row[2],
                'basepay': row[3],
                'overtimepay': row[4]
            }
            portfolio.append(record)    
    return portfolio

portfolio = read_portfolio('data.csv')
# print(portfolio)
total = 0.0

for holding in portfolio:
    total += holding['basepay'] * holding['overtimepay']

print('Total pay:', total)

import json

data = json.dumps(portfolio)
# print(data)
port = json.loads(data)
# print(port)

names = []
for holding in portfolio:
    names.append(holding['name'])

print(names)

total = sum([holding['basepay'] + holding['overtimepay'] for holding in portfolio])
print(total)

names = [holding['name'] for holding in portfolio]
print(names)

more100 = [holding['name'] for holding in portfolio if holding['basepay']>30000.0]
print(more100)

namestr = ','.join(names)
print(namestr)

unique_names = {namestr}

import urllib.request 

u = urllib.request.urlopen('http://finance.yahoo.com/d/quotes.csv?s={}&f=l1'.format(namestr))
data = u.read()
pricedata = data.split()

for name, price in zip(unique_names, pricedata):
    print (name, '=', price)

prices = dict(zip(unique_names, pricedata))

current_value = 0.0
for holding in portfolio:
    current_value += holding['shares'] * prices[holding['name']]

currenct_value = sum([ holding['shares'] * prices[holding['name'] for holding in portfolio])

change = current_value - total
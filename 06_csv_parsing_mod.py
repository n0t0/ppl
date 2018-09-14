f = open('ticker_data.csv', 'r')
import csv 

rows = csv.reader(f)
row = next(rows)
print(row)

types = [str, str, int, float]

for func, val in zip(types, row):
    print(func, val)


converted = [ func(val) for func, val in zip(types, row) ]
print(converted)


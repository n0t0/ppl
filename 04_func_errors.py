import csv 
import glob

def portfolio_cost(filename):
    """
    This will compute columns 3 and 4 from a file as a total cost
    """
    total = 0.0
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
            total += row[3] * row[4]
    return total


total = portfolio_cost('data.csv')
print('Total cost:', total)

files = glob.glob('*.py')
print(files)
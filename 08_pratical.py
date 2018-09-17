def print_table(objects, colnames, formatter):
    """
    Create a formatted table showing attributes fom a list of objects 
    """ 

    formatter.headings(conames)
    for obj in objects:
        rowdata = [str(getattr(obj, colname)) for colname in colnames] 
        formatter.row(rowdata)

    # Emit table headers 
    for colname in colnames:
        print('{:>10s}'.format(colname), end=' ')
    print()
    
    for obj in objects: 
        # Emit a row of table data
        for colname in colnames:
            print('{:>10s}'.format(str(getattr(obj, colname))), end=' ')
        print()


class TableFormat(object):
    # Serves a design spec for making table (use inheritance to customize)
    def headings(self, headers):
        raise NotImplementedError

    def row(self, rowdata):
        raise NotImplementedError


class TextTableFormatter(TableFormat):
    def headings(self, headers):
        for header in headers:
            print('{:>10s}'.format(header), end=' ')
        print()

    def row(self, rowdata):
        for item in rowdata:
            print('{:>10s}'.format(item), end=' ')
        print()


import table 
formatter = table.TextTableFormatter()
table.print_table


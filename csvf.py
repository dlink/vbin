#!/usr/bin/env python

# Goal:
# csv -s FILE        # show header
# csv -p FILE        # pretty format
# csv -c12,4 FILE    # dislpay columns 12 and 4
# csv -p -c12,4 FILE # dislpay columns 12 and 4, formated
# csv -d'|' -c1-3    # display columns 1-3, delimiter = |
# csv -d'' -p FILE   # pretty format, with no delimiter
# csv -f "1=blue;3=red" # filter lines where col-1 = 'blue' and col-3 = 'red'
# csv -f "1=blue|3=red" # filter lines where col-1 = 'blue' or col-3 = 'red'
# csv -f "(1=blue|3=red);3=green" # filter lines where col-1 = 'blue' or col-3 = \
'red'
# csv -f "1 in (blue,green)"
# csv -f "1 ~ ^abc.*$"

import sys
import csv
import re

SHOW_TRACEBACK = 0

class CSVError(Exception): pass

class CSV(object):
    
    def __init__(self, file):
        self.file = file
        self.delimiter = ','
        self.colspec = None
        self.pretty_print = False
        self.lengths = []
        self.show_header = False
        self.process_successful = False

    def process(self):
        results = []
        try:
            rows = csv.reader(self.fp, delimiter=self.delimiter,
                              escapechar='\\')
            for n, row in enumerate(rows):
                newrow = []
                if self.columns:
                    # use user spec columns:
                    i = 0
                    for n in self.columns:
                        newrow.append(self.processCell(i, row[n-1]))
                        i += 1
                else:
                    # use all columns
                    for i, cell in enumerate(row):
                        newrow.append(self.processCell(i, cell))
                results.append(newrow)
                if self.show_header:
                    break
            self.process_successful = True

        except Exception, e:
            if SHOW_TRACEBACK:
                raise
            results = "%s: %s" % (e.__class__.__name__, e)
        return results        
    
    def processCell(self, i, cell):        
        '''Given current column counter, and raw cell data
           Behavior: Keep max lengths up-to-date
                     Add double quotes on Cell if nec.
           Return: Cell as STRING
        '''
        if i > len(self.lengths)-1:
            self.lengths.append(0)
        self.lengths[i]=max(len(cell),self.lengths[i])
        if ',' in cell:
            return '"%s"' % cell
        return cell

    @property
    def fp(self):
        '''Open file and return file pointer
           use stdin for -
        '''
        if '_fp' not in self.__dict__:
            if self.file == '-':
                self._fp = sys.stdin
            else:
                self._fp = open(self.file, 'r')
        return self._fp;
    
    @property
    def columns(self):
        if '_columns' not in self.__dict__:
            if not self.colspec:
                # no colspec
                self._columns = None
            else:
                self._columns = []
                for x in self.colspec.split(','):
                    if re.match('[0-9]*-[0-9]*', x):
                        # range of columns
                        start, fin = map(int, x.split('-'))
                        self._columns.extend(range(start, fin+1))
                    elif x.isdigit():
                        self._columns.append(int(x))
                    else:
                        raise CSVError('invalid column in colspec: %s' % x)
            if 0:
                print 'columns:', self._columns
        return self._columns
    
    def showHeader(self, table):
        o = ''
        for i, x in enumerate(table[0]):
            o += "%s. %s\n"  % (i+1, x)
        return o

    def prettyPrint(self, table):
        o = ''
        for row in table:
            i = 0
            line = []
            for field in row:
                if i < len(row)-1:
                    s = "%s," % field
                    o += s.ljust(self.lengths[i]+2)
                else:
                    o += "%s\n" % field
                i += 1
        return o
    

    def toStr(self):
        results = self.process()

        # show_header?
        if self.show_header:
            return self.showHeader(results)

        # pretty_print?
        if self.pretty_print and self.process_successful:
            return self.prettyPrint(results)

        # Handle anything:
        o = ''
        if isinstance(results, (list, tuple)):
            #print 'r:', results
            if results and isinstance(results[0], (list, tuple)):
                for row in results:
                    o += ",".join(map(str, row)) + '\n'
            else:
                o += "\n".join(map(str, results))
        else:
            o = results
        return o
    
if __name__ == '__main__':
    import argparse

    p = argparse.ArgumentParser(description="CSV file utility.")
    p.add_argument('file')
    p.add_argument('-c', dest='colspec', metavar='<colspec>',
                        help='List or range of column numbers.  eq. - 2,1,4-6')
    p.add_argument('-d', dest='delimiter', metavar='<delimiter>',
                        default=',',
                        help='Set delimiter.  Default is comma (,)')
    p.add_argument('-p', dest='pretty_print', action='store_true',
                        help='Pretty-Print output')
    p.add_argument('-s', dest='show_header', action='store_true',
                        help='show column headers')
    args = p.parse_args()

    f = CSV(args.file)
    if args.show_header:
        f.show_header = True
    else:
        f.colspec      = args.colspec
        f.delimiter    = args.delimiter
        f.pretty_print = args.pretty_print
    print f.toStr().strip()

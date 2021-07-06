#!/usr/bin/env python

import sys
import csv
from openpyxl import load_workbook

class XlsxError(Exception): pass

class Xlsx(object):
    
    def toCsv(self, filename):
        writer = csv.writer(sys.stdout)
        wb = load_workbook(filename)
        ws = wb.active
        recs = []
        for row in ws.values:
            row2 = []
            for value in row:
                if isinstance(value, str):
                    value = value.encode('utf-8')
                row2.append(value)
            writer.writerow(row2)


if __name__ == '__main__':
    import argparse

    # Set up Args:
    p = argparse.ArgumentParser(description="xlsx file to csv converter.")
    p.add_argument('file')
    args = p.parse_args()

    # parse
    print(Xlsx().toCsv(args.file))

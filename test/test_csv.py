#!/usr/bin/env python

import unittest
from csvf import CSV

'''
conf = ConfigFile()
book = 'feature_test'
saved_pdf = '%s/%s.pdf' % (conf.storage.tests, book)
'''
INFILE = 'books.csv'
TEST_2_7_8 = 'books_2_7_8.test'
TEST_26_2 = 'books_26_2.test'
TEST_24_to_26_2 = 'books_24_to_26_2.test'

class TestCSV(unittest.TestCase):

    def setUp(self):
        self.csv = CSV(INFILE)

    def test_echo_output(self):
        self.assertEqual(self.csv.toStr(), read(INFILE))

    def test_columns(self):
        self.csv.colspec = '2,7,8'
        self.assertEqual(self.csv.toStr(), read(TEST_2_7_8))

    def test_columns_rearrange(self):
        self.csv.colspec = '26,2'
        self.assertEqual(self.csv.toStr(), read(TEST_26_2))

    def test_columns_range(self):
        self.csv.colspec = '24-26,2'
        self.assertEqual(self.csv.toStr(), read(TEST_24_to_26_2))

def read(file):
    return open(file, 'r').read()

if __name__ == '__main__':
    unittest.main()

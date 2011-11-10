#!/usr/bin/env python
import unittest

TEST_MODULES = [
    # format:
    #'snakd.test.test_file',
    'urls_test',
]

def all():
    return unittest.defaultTestLoader.loadTestsFromNames(TEST_MODULES)

if __name__ == '__main__':
    import tornado.testing
    tornado.testing.main()
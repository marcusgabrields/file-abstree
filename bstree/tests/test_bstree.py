import os
import unittest

from bstree import BSTree


class BSTreeTestCase(unittest.TestCase):

    FILE_PATH = os.path.dirname(os.path.realpath(__file__))
    FILE_NAME = FILE_PATH + '/BSTreeTestCase.bin'.lower()

    def setUp(self):
        self._file = open(self.FILE_NAME, 'wb')
        self.bst = BSTree(self._file)
    
    def tearDown(self):
        self._file.close()
        os.remove(self.FILE_NAME)

    def test_can_insert_a_element(self):
        self.bst.insert('Gabriel')
        self.assertEqual(len(self.bst), 1)
    
    def test_can_insert_more_than_one_element(self):
        self.bst.insert('Gabriel')
        self.bst.insert('João')
        self.assertEqual(len(self.bst), 2)
import os
import unittest

from bstree import BSTree


class BSTreeTestCase(unittest.TestCase):

    FILE_PATH = os.path.dirname(os.path.realpath(__file__))
    FILE_NAME = FILE_PATH + '/BSTreeTestCase.bin'.lower()

    def test_can_insert_a_element(self):
        _file = open(self.FILE_NAME, 'wb')
        bst = BSTree(_file)
        bst.insert('Gabriel')
        self.assertEqual(len(bst), 1)
        _file.close()
        # os.remove(self.FILE_NAME)
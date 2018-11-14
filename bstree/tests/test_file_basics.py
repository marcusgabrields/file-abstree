import os
import unittest


class FileBasicsTestCase(unittest.TestCase):

    FILE_PATH = os.path.dirname(os.path.realpath(__file__))
    FILE_NAME = FILE_PATH + '/FileBasicsTestCase.bin'.lower()

    def setUp(self):
        self._file = open(self.FILE_NAME, 'wb')
    
    def tearDown(self):
        self._file.close()
        os.remove(self.FILE_NAME)
    
    def test_can_create_a_fili(self):
        self.assertTrue(os.path.exists(self.FILE_NAME))
        self.assertTrue(os.path.isfile(self.FILE_NAME))
    

if __name__ == '__main__':
    unittest.main()
import struct


class BSTree:
    
    STRING_SIZE = 10
    
    def __init__(self, _file):
        self.root = None
        self._file = _file
        self.size = 0
    
    def insert(self, data):
        if not self.root:
            self._file.seek(0, 2)
            new_node = struct.pack('{}s'.format(self.STRING_SIZE), data.encode())
            self._file.write(new_node)
            self.size = self.size + 1
    
    def __len__(self):
        return self.size
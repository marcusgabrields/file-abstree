import struct


class BSTree:
    
    STRING_SIZE = 10
    
    def __init__(self, _file):
        self.root = None
        self._file = _file
        self.size = 0
    
    def insert(self, data):
        if self.root == None:
            self.root = self.__pack(0, data)
            self.size = self.size + 1
        else:
            pass
        
    def _insert(data, key):
        pass
    
    def __unpack(self, key):
        self._file.seek(key)
        node = struct.unpack('10s i i i', self._file.read(24))
        node = (node[0].decode().strip('\x00'), node[1], node[2], node[3])
        return node
    
    def __pack(self, key, data, left_child=-1, right_child=-1, deleted=0):
        new_node_key = self._file.seek(key)
        new_node = struct.pack('10s i i i'.format(self.STRING_SIZE), data.encode(), left_child, right_child, deleted)
        self._file.write(new_node)
        return new_node_key

    def __len__(self):
        return self.size
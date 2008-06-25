import cPickle as pickle
from bz2 import BZ2File

class Attr:
    def __init__(self, name, num, vals):
        self.num = name
        self.name = num
        self.vals = vals

class DB:
    def open(self, filename):
        f = BZ2File(filename, 'rb')
        self.__d = pickle.load(f)
        f.close()

    def attrs(self):
        return self.__d[0]

    def data(self):
        return self.__d[1]

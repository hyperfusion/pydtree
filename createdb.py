# the attributes file is read as a list of attributes (row names), one on each line
# the data file is read in as a list of comma-separated strings on separate lines
#       (there should be an extra field for the class)

from db import Attr
import re
def gencols(file):
    cols = []
    r = re.compile('(.+):(.+)')
    f = open(file, 'r')
    for num, line in enumerate(f):
        name, vals = r.match(line).groups()
        vals = vals.split(',')
        cols.append(Attr(num, name, vals))
    f.close()
    return cols

def genrows(file):
    rows = []
    f = open(file, 'r')
    for line in f:
        rows.append(line.strip().split(','))
    f.close()
    return rows

import sys
import cPickle as pickle, bz2
if __name__ == '__main__':
    if len(sys.argv) < 4 or sys.argv[1] == '-h':
        print 'usage: createdb.py [database] [attributes] [data]'
        sys.exit(1)

    f = bz2.BZ2File(sys.argv[1], 'wb')
    dump = pickle.dump([gencols(sys.argv[2]), genrows(sys.argv[3])], f, 2)
    f.close()

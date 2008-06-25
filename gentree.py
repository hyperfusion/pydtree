def choosebest(data, attrs):
    # fixme plz
    return attrs[0]

def gentree(data, attrs):
    classes = [row[-1] for row in data]

    # if there are no attributes or the data's empty, return the best guess
    # (the majority classification)
    if len(data) == 0: return None
    if len(attrs) == 0:
        return max(set(classes), key=lambda x: classes.count(x)) # performance?

    # if all the data classes are the same, then just return that classification
    if classes.count(classes[0]) == len(classes):
        return classes[0]

    best = choosebest(data, attrs)
    tree = { best.name: { } }

    for val in best.vals:
        newdata = [a for a in data if a[best.num] == val]
        newattrs = [a for a in attrs if a.num != best.num]
        tree[best.name][val] = gentree(newdata, newattrs)

    return tree

import sys
from bz2 import BZ2File
import cPickle as pickle
from db import DB
if __name__ == '__main__':
    if len(sys.argv) < 3 or sys.argv[1] == '-h':
        print 'usage: gentree.py [database] [tree]'
        sys.exit(1)

    db = DB()
    db.open(sys.argv[1])
    tree = gentree(db.data(), db.attrs())

    f = BZ2File(sys.argv[2], 'wb')
    pickle.dump(tree, f, 2)
    f.close()

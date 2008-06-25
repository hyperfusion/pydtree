# not very good code.

from bz2 import BZ2File
import cPickle as pickle

def printchildren(file, tree):
    # if at a leaf node, we're done
    if tree is None or type(tree) != type({}):
        return

    node = tree.items()[0]
    attr = node[0]
    subtree = node[1]
    for choice, choicesubtree in subtree.iteritems():
        if choicesubtree is None: return
        if type(choicesubtree) == type(''):
            print >>file, '\t"'+attr+'"', '->', '"'+choicesubtree+'"', '[label="' + choice + '"];'
            continue
        for choiceresult in choicesubtree:
            print >>file, '\t"'+attr+'"', '->', '"'+choiceresult+'"', '[label="' + choice + '"];'
        printchildren(file, choicesubtree)

import sys
if __name__ == '__main__':
    if len(sys.argv) < 3 or sys.argv[1] == '-h':
        print 'usage: treetodot.py [tree] [graph.dot]'
        sys.exit(1)

    tree = pickle.load(BZ2File(sys.argv[1]))

    f = file(sys.argv[2], 'w')
    print >>f, 'digraph tree {'
    printchildren(f, tree)
    print >>f, '}'
    f.close()

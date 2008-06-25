from db import DB
import sys, os

if __name__ == '__main__':
    if len(sys.argv) < 3 or sys.argv[1] == '-h':
        print 'usage: dumpdb.py [all|attrs|data] [database]'
        sys.exit(1)

    if not os.path.exists(sys.argv[2]):
        print >>sys.stderr, 'file', sys.argv[2], 'does not exist'
        sys.exit(1)

    db = DB()
    db.open(sys.argv[2])

    if sys.argv[1] == 'attrs' or sys.argv[1] == 'all':
        for name, vals in sorted(db.attrs().items()):
            print name[1] + ':' + ','.join(vals)

    if sys.argv[1] == 'data' or sys.argv[1] == 'all':
        for row in db.data():
            print ','.join(row)

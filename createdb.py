# the attributes file is read as a list of attributes (row names), one on each line
# the data file is read in as a list of comma-separated strings on separate lines
#       (there should be an extra field for the class)

import re
def gencols(file, cur):
    cur.execute('create table attrs (name text, vals text)')
    cols = []
    r = re.compile('(.+):(.+)')
    f = open(file, 'r')
    for line in f:
        name, vals = r.match(line).groups()
        cols.append(name + ' text')
        cur.execute('insert into attrs values (?, ?)', (name, vals))
    f.close()
    cols.append('CLASS text')
    cur.execute('create table data (' + ', '.join(cols) + ')')

def genrows(file, cur):
    f = open(file, 'r')
    for line in f:
        row = ','.join(map(lambda x: "'" + x + "'", line[:-1].split(',')))
        cur.execute('insert into data values (' + row + ')')
    f.close()

import sys
import sqlite3
if __name__ == '__main__':
    if len(sys.argv) < 4 or sys.argv[1] == '-h':
        print 'usage: createdb.py [database] [attributes] [data]'
        sys.exit(1)

    con = sqlite3.connect(sys.argv[1])
    cur = con.cursor()
    gencols(sys.argv[2], cur)
    genrows(sys.argv[3], cur)
    con.commit()

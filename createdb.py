# the attributes file is read as a list of attributes (row names), one on each line
# the data file is read in as a list of comma-separated strings on separate lines
#       (there should be an extra field for the class)

def gencols(file):
    cols = []
    f = open(file, 'r')
    for line in f:
        cols.append(line[:-1] + ' text')
    f.close()
    cols.append('CLASS')
    return ', '.join(cols)

def genrows(file):
    table = []
    f = open(file, 'r')
    for line in f:
        table.append(','.join(map(lambda x: "'" + x + "'", line[:-1].split(','))))
    f.close()
    return table

import sys
import sqlite3
if __name__ == '__main__':
    if len(sys.argv) < 4 or sys.argv[1] == '-h':
        print 'usage: createdb.py [database] [attributes] [data]'
        sys.exit(1)

    con = sqlite3.connect(sys.argv[1])
    con.execute('create table data (' + gencols(sys.argv[2]) + ')')
    cur = con.cursor()
    for row in genrows(sys.argv[3]):
        cur.execute('insert into data values (' + row + ')')
    con.commit()

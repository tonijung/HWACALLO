'''
This is meant to run from the command line. The exact command is:
<python location> <dbf2csv.py file location> <dbf_file location> <csv_file location>

From http://blog.cgarrard.com/2010/08/converting-dbf-to-csv-with-python.html
Note that first you must download the dbfpy module from:
http://dbfpy.sourceforge.net/
'''

#!/usr/bin/env python

import csv
from dbfpy import dbf
import sys

dbf_fn = sys.argv[1]
csv_fn = sys.argv[2]

in_db = dbf.Dbf(dbf_fn)
out_csv = csv.writer(open(csv_fn, 'wb'))

names = []
for field in in_db.header.fields:
    names.append(field.name)
    out_csv.writerow(names)

for rec in in_db:
    out_csv.writerow(rec.fieldData)

in_db.close()

print "FIN"

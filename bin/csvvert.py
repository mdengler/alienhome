#!/usr/bin/env python
"""

Displays a CSV file's contents vertically.

Example:

$ cat | ~/bin/csvvert.py
Year,Make,Model,Length
1981,Ford,Capri Ghia,2.34
1986,Ford,Reliant Regal,2.34
1990,Ford,Sierra RS Cosworth,2.38

  Year: 1981
  Make: Ford
 Model: Capri Ghia
Length: 2.34

  Year: 1986
  Make: Ford
 Model: Reliant Regal
Length: 2.34

  Year: 1990
  Make: Ford
 Model: Sierra RS Cosworth
Length: 2.38


"""

import csv
import os
import sys


def get_fields_reader(csv_lines):
    fields = list(csv.reader(csv_lines[0:1]))[0]
    csvreader = csv.DictReader(csv_lines)
    return fields, csvreader


def print_vertically(csv_lines):
    fields, csvreader = get_fields_reader(csv_lines)

    max_fieldname_length = max([len(f) for f in fields])
    lineformat = "%%%is: %%s%%s" % max_fieldname_length

    for row in csvreader:
        for field in fields:
            sys.stdout.write(lineformat % (field, row[field], os.linesep))
        sys.stdout.write(os.linesep)



if __name__ == "__main__":

    if len(sys.argv) <= 1:
        print_vertically(sys.stdin.readlines())
    else:
        for filename in sys.argv[1:]:
            if filename == "-":
                fh = sys.stdin
            else:
                fh = open(filename)
            print_vertically(fh.readlines())

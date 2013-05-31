#!/usr/bin/env python
"""

cut, but for CSV files

Example:

$ cat <<CSV | ~/bin/csvcut.py -f 1
Year,Make,Model,Length
1981,Ford,Capri Ghia,2.34
1986,Ford,Reliant Regal,2.34
1990,Ford,Sierra RS Cosworth,2.38
CSV
1981
1986
1990

"""

import csv
import decimal
import optparse
import os
import sys


def maybe_normalize(input_string, normalize):
    output_string = input_string
    if normalize:
        output_string = output_string.strip()
        maybe_decimal = None
        try:
            maybe_decimal = decimal.Decimal(output_string.replace(",", ""))
            output_string = "%s" % maybe_decimal
        except decimal.InvalidOperation:
            pass
    return output_string


def get_fields_reader(csv_lines):
    fields = list(csv.reader(csv_lines[0:1]))[0]
    csvreader = csv.DictReader(csv_lines)
    return fields, csvreader


def cut_dict(csv_lines, field_indexes, csvout=None, numeric_normalization=False):
    fields, csvreader = get_fields_reader(csv_lines)

    if csvout is None:
        fields_in_output = [fieldname
                            for index, fieldname in enumerate(fields)
                            if index + 1 in field_indexes]
        csvout = csv.DictWriter(sys.stdout, fieldnames=fields_in_output)

    for row in csvreader:
        outrow = dict(
            [(fieldname, maybe_normalize(input_column, numeric_normalization))
              for fieldname, input_column in row.iteritems()
              if fieldname in fields_in_output])

        csvout.writerow(outrow)


def cut_array(csv_lines, field_indexes, csvout=None, numeric_normalization=False):
    csvreader = csv.reader(csv_lines)

    if csvout is None:
        csvout = csv.writer(sys.stdout)

    if len(field_indexes) == 0:
        fields_in_first_line = csv.reader(csv_lines[0:1]).next()
        field_indexes = range(1, len(fields_in_first_line) + 1)

    for row in csvreader:
        if "".join(row).strip() == "":
            continue
        outrow = [maybe_normalize(row[index - 1], numeric_normalization)
                  for index in field_indexes]
        csvout.writerow(outrow)


def cut(csv_lines, field_indexes, header=False, csvout=None, numeric_normalization=False):
    if header:
        return cut_dict(csv_lines, field_indexes, csvout=csvout, numeric_normalization=numeric_normalization)
    else:
        return cut_array(csv_lines, field_indexes, csvout=csvout, numeric_normalization=numeric_normalization)



if __name__ == "__main__":

    parser = optparse.OptionParser()
    parser.add_option("-f", "--fields",
                      default="",
                      help="fields to parse, with commas and/or hyphens"
                      " indicating ranges in the customary way")
    parser.add_option("-x", "--header",
                      dest="header", action="store_true",
                      help="incoming CSV has a header row")
    parser.add_option("-n", "--numeric-normalize", action="store_true",
                      help="converts numeric columns to normalized version"
                      " via str(decimal.Decimal(column_data))")
    parser.add_option("--skip-leading-lines",
                      default=0, type="int",
                      help="skips input lines before processing (pass number of lines)")
    options, args = parser.parse_args()

    field_indexes = []
    for fieldspec in options.fields.split(","):
        if fieldspec == "":
            continue
        if "-" not in fieldspec:
            field_indexes.append(int(fieldspec))
        else:
            start, end = map(int, fieldspec.split("-"))
            field_indexes.extend(range(start, end + 1))

    if len(args) < 1:
        args.append("-")

    for filename in args:
        if filename == "-":
            fh = sys.stdin
        else:
            fh = open(filename)

        input_lines = fh.readlines()
        if options.skip_leading_lines != 0:
            input_lines = input_lines[options.skip_leading_lines:]

        cut(input_lines,
            field_indexes,
            header=options.header,
            numeric_normalization=options.numeric_normalize)


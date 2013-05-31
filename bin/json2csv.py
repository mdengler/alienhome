#!/usr/bin/env python

"""

Converts a file of json records like:

    {"Obs":1,"NAME":"SBE INC.","BHRET3":-77.1,"fulldate":19760108,"rMVOP":42.9174,"rMVMP":46.3313}
    {"Obs":1,"NAME":"SBE INC.","BHRET3":-77.1,"fulldate":19760108,"rMVOP":42.9174,"rMVMP":46.3313}
    ...

...into csv like:

    NAME,fulldate,BHRET3,Obs,rMVOP,rMVMP
    SBE INC.,19760108,-77.1,1,42.9174,46.3313
    ...

Copyright (c) 2012 Martin Dengler <martin@martindengler.com>
License: GPL v3+ (see COPYING file)

"""

import csv
import simplejson
import sys


csv_fh = None
fields = None

for line in sys.stdin.readlines():
    json = simplejson.loads(line.strip())

    if not isinstance(json, list):
        json = [json]

    for json in json:

        #one-time initialization / writing of headers
        json_fields = json.keys()
        if (csv_fh is None) or (set(fields) != set(json_fields)):
            fields = json_fields
            csv_fh = csv.DictWriter(sys.stdout, fields)
            csv_fh.writeheader()

        csv_fh.writerow(json)


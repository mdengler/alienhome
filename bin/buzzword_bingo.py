#! /usr/bin/env python

import itertools
import os
import random
import sys
import subprocess
from optparse import OptionParser

print_html = "html2ps | /usr/bin/lp -d %s"


DEFAULT_TITLE = "Buzzword Bingo!"


def generate_html(word_lists, size=5, title=None, sheet_id=""):
    if title is None:
        title = DEFAULT_TITLE

    if sheet_id != "":
        sheet_id = "This is sheet %s" % sheet_id

    size = int(size)
    multi_rows = []

    for word_list in word_lists:
        cells = []
        random.shuffle(word_list)
        word_list = word_list[: size * size]

        for i in range(size):
            cells.append(word_list[i * size : (i + 1) * size])

        if size % 2 != 0:
            mid_idx = size // 2
            cells[mid_idx][mid_idx] = "<b>BINGO!</b>"

        multi_rows.append(cells)

    def multi_row_to_html(multi_row):
        row_html = "<tr>\n"
        for multi_cell in zip(*multi_row):
            row_html += '<td width="%d%%" height="%d%%">%s</td>' % (
                (100 // size),
                (100 // size),
                "<br>".join(multi_cell),
            )
        row_html += "</tr>\n"
        return row_html

    rows_html = [
        multi_row_to_html(multi_row) for multi_row in zip(*multi_rows)
    ]

    return """<html>
    <head>
    <title>%(title)s</title>
    <style type="text/css">
    <!--
    H1 { font-size: 40pt; }
    TD {
    font-family: "DejaVu Sans Mono", "Liberation Mono",
                 "Lucida Console", "Lucida Sans Typewriter",
                 Consolas, "Courier New", Courier,
                 monospace;
    font-size: 24pt;
    }
    -->
    </style>
    </head>
    <body>
    <h1>%(title)s</h1>
    <table width="100%%" border="2px" cellpadding="10px">
    %(rows)s
    </table>

<p>
%(sheet_id)s
</p>

<h2 style="page-break-before: always">
Rules / Comments:
</h2>
<p>
<ol>
<li>When you hear any of these words/phrases said IN NORMAL CONVERSATION, you may mark the box with the word in it.</li>
<li>Discussing the words you have does not count as NORMAL CONVERSATION!</li>
<li>Deliberate discussing of the words in the box does not count as NORMAL CONVERSATION!</li>
<li>When you get three in a row, you MUST shout "BINGO!" and wave your sheet around.  If most people don't hear you, you do not win.</li>
<li>No cheating!</li>
<li>The middle square ("BINGO") can be marked whenver you need it; you do not need to hear someone say "BINGO".</li>
<li>In the SAME box, ANY of the phrases counts.  The different phrases are not related.</li>
<li>OVERHEARD conversation is OK, but deliberate conversation.</li>
<li>Rules will be judged by your peers.  Any disagreements will be resolved by Martin Dengler.  The judgement will be FINAL.</li>
<li>You may mark a box if you hear the words in the box in ANY language.  E.g.,: "Cafe de Coral" can be marked if you hear it in English OR Cantonese.</li>
<li>You MAY trick the same person into saying a word only once.  But it's not nice.  If you do it too much you will be disqualified.</li>
<li></li>
</ol>
</p>
<p>
</p>
<p>


    </body>
    </html>""" % {
        "title": title,
        "sheet_id": sheet_id,
        "rows": "\n".join(rows_html),
    }


def main():
    LPDEST = "LPDEST"

    parser = OptionParser()
    parser.add_option(
        "--print", action="store_true", help="Print table", dest="do_print"
    )
    parser.add_option("--printer", default=LPDEST, help="Printer to print to")
    parser.add_option(
        "--size",
        default=5,
        help="cells per row/column (should be an odd number and less than or equal to the square root of the number of words you're providing)",
    )
    parser.add_option(
        "--title", default=DEFAULT_TITLE, help="title of generated matrix"
    )
    parser.add_option("--sheet-id", default="", help="optional ID to add to sheet")
    options, args = parser.parse_args()

    word_lists = []
    for filename in args:
        if filename == "-":
            fh = sys.stdin
        else:
            fh = open(filename)
        word_lists.append([line.strip() for line in fh.readlines()])

    html = generate_html(
        word_lists, size=options.size, title=options.title, sheet_id=options.sheet_id
    )

    if options.do_print:
        if options.printer == LPDEST:
            options.printer = os.environ.get(LPDEST)
        printer = subprocess.Popen(
            print_html % options.printer, shell=True, stdin=subprocess.PIPE
        )
        printer.stdin.write(html)
        printer.stdin.write("\n")
        printer.stdin.close()
        printer.wait()
    else:
        print(html)


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import decimal
import itertools
import math
import os
import sys

from optparse import OptionParser

# TODO: allow y axis to be non-numeric, as in graphing uniq -c output: tail ~/doc/public_html/proj/vp_001/files_by_commits.txt
# TODO: understand dates as X axis

#amusing glyphs:
# •‧⁖⁘⁙⁚₀₁₂₃₄₅₆₇₈₉∙∘∴∶∷⊕⊖⊗⊘⊙⊚⊛⊜⊝⋅⋆⋮⋯⋰⋱⍉⌾⍟─━┄┉┈┅╌╍◉○◌◍◎●◐◦◯☉★☆⚪⚫⚬✩✪✫✬✭✮✯✰✚✛✜✢✣✤✶✷✸✹✺✻✿❀❍⦁⨀⦾⦿⨁⨂〠㊀㊁㊂㊃㊄㊅㊆㊇㊈㊉﷽
GLYPHS = {
    1:  "‧",
    2:  "•",
    3:  "⦁",
    4:  "●",
    5:  "",
    6:  "",
    }


def is_number(s):
    try:
        decimal.Decimal(s)
        return True
    except:
        return False


def getinput(input_fh):
    lineidx = 0
    points = {}

    for line in input_fh.readlines():

        line = line.strip()
        lineidx += 1

        num_parts = [decimal.Decimal(part) for part in line.split() if is_number(part)]

        if len(num_parts) > 1:
            x, y = num_parts[0:2]
        elif len(num_parts) == 1:
            x, y = lineidx, num_parts[0]
        else:
            x, y = lineidx, len(line)

        if y not in points:
            points[y] = {}

        if x not in points[y]:
            points[y][x] = 1
        else:
            points[y][x] += 1

    return points


def transform(points, rows, cols):
    ys = points.keys()
    xs = list(itertools.chain([x.keys()[0] for x in points.values()]))

    min_y, max_y = min(ys), max(ys)
    min_x, max_x = min(xs), max(xs)

    y_range = max(max_y - min_y, rows - 1)
    x_range = max(max_x - min_x, cols - 1)
    y_transform = y_range / decimal.Decimal(rows)
    x_transform = x_range / decimal.Decimal(cols)

    output_points = {}
    output_y = 0
    for y in sorted(points):
        output_y = int((y - min_y) / y_transform)

        if output_y not in output_points:
            output_points[output_y] = {}

        for x in sorted(points[y]):
            output_x = int((x - min_x) / x_transform)
            if output_x not in output_points[output_y]:
                output_points[output_y][output_x] = 1
            else:
                output_points[output_y][output_x] += 1

    return output_points, min_y, y_transform, min_x, x_transform


def dump_points(output_fh, rows, cols, points, min_y, y_transform, min_x, x_transform, draw_bars=False, use_glyphs=True):
    ys = points.keys()
    xs = list(itertools.chain([x.keys()[0] for x in points.values()]))

    min_y, max_y = min(ys), max(ys)
    min_x, max_x = min(xs), max(xs)

    row_tick_incr = rows / 10

    x_drop_bars = {}

    for y in range(rows, -1, -1):
        axis_str = "   |"
        if (y % row_tick_incr == 0) or (y == max_y):
            axis_str = "%3s|" % int((y * y_transform) + min_y)

        output_fh.write(axis_str)

        for x in range(cols + 1):
            output_char = ' '
            if y in points and x in points[y]:
                output_char = str(points[y][x])
                if use_glyphs:
                    output_char = GLYPHS.get(points[y][x], output_char)
                x_drop_bars[x] = output_char
            elif draw_bars and (x in x_drop_bars):
                output_char = x_drop_bars[x]
                output_char = "⋅"
            output_fh.write(output_char)

        output_fh.write(os.linesep)

    output_fh.write('   +' + '-' * cols + os.linesep)

    pointer_str = " "
    col_tick_maxlen = len(str(max_x)) + len(pointer_str) + 2
    col_tick_incr = int(math.ceil(cols / col_tick_maxlen))
    last_tick = 0
    for x in range(0, cols + 1, col_tick_incr):
        tick_num = int(x * x_transform) + min_x
        tick_str = "%s%s" % (tick_num, pointer_str)
        padding = col_tick_incr
        format_str = "%%%ss" % padding
        output_fh.write(format_str % tick_str)
        last_tick = x
    output_fh.write(os.linesep)


def ascii_scatter(output_fh, points, rows, cols, draw_bars=False, use_glyphs=False):
    output_points, min_y, y_transform, min_x, x_transform = \
        transform(points, rows, cols)
    dump_points(output_fh,
                rows, cols,
                output_points,
                min_y, y_transform,
                min_x, x_transform,
                draw_bars=draw_bars,
                use_glyphs=use_glyphs)


def pylab_scatter(points, draw_bars=False):
    # FUTURE: implement draw_bars=True, perhaps like
    # http://www.mail-archive.com/matplotlib-users@lists.sourceforge.net/msg03309.html
    ys = points.keys()
    xs = list(itertools.chain([x.keys()[0] for x in points.values()]))
    import pylab
    pylab.scatter(xs, ys)
    pylab.show()


def parse_options():
    parser = OptionParser()
    parser.add_option("-r", "--rows", default=20, type=int)
    parser.add_option("-c", "--cols", default=40, type=int)
    parser.add_option("-b", "--bars", action="store_true")
    parser.add_option("--use-pylab", action="store_true")
    parser.add_option("--glyphs", action="store_true")
    parser.add_option("-D", "--debug-dump-points", action="store_true")

    options, args = parser.parse_args()

    return (options.rows,
            options.cols,
            sys.stdin,
            sys.stdout,
            options.bars,
            options.use_pylab,
            options.glyphs,
            options.debug_dump_points,
            )



if __name__ == "__main__":
    rows, cols, input_fh, output_fh, draw_bars, use_pylab, use_glyphs, debug_dump_points = parse_options()
    points = getinput(input_fh)
    if debug_dump_points:
        print points
    if not use_pylab:
        ascii_scatter(output_fh, points, rows, cols, draw_bars, use_glyphs)
    else:
        pylab_scatter(points, draw_bars)


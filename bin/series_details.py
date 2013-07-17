#!/usr/bin/python

import math


def mean(values):
    """sum(values) / len(values)"""
    return sum(values) / len(values)

def median(values):
    counts = {}
    for v in values:
        if v not in counts:
            counts[v] = 0
        counts[v] = counts[v] + 1
    return sorted(counts.keys(),
                  lambda a, b: cmp(counts[b], counts[a]))[0]

def sample_standard_deviation(samples):
    """See http://mathworld.wolfram.com/StandardDeviation.html"""
    x_bar = mean(samples)
    deviations = []
    for xi in samples:
        deviations.append((xi - x_bar)**2)
    variance = sum(deviations) / float(len(samples) - 1)
    return math.sqrt(variance), variance

def first_float(line):
    try:
        return float(line)
    except:
        return float(line.split()[0])



if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    if len(args) > 0:
        series = map(float, args)
    else:
        series = [first_float(line.strip()) for line in sys.stdin.readlines()]

    if len(series) < 1:
        sys.stderr.write("zero-length input series\n")
        sys.exit(1)

    tests = {
        "vol": lambda s: sample_standard_deviation(s)[0],
        "variance": lambda s: sample_standard_deviation(s)[1],
        "mean": mean,
        "median": median,
        "sum": sum,
        "count": len,
        }
    results = []
    display_ordered = ("count", "sum", "mean", "median", "vol", "variance")
    for test in display_ordered:
        sys.stdout.write("%10s: " % test)
        result = tests[test](series)
        sys.stdout.write("%s\n" % result)
        results.append(result)
    sys.stdout.write("%s\n" % ",".join(tests.keys()))
    sys.stdout.write("%s\n" % ",".join(map(str, results)))

    sys.exit(0)

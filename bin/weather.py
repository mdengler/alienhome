#!/usr/bin/env python
default_city = "London,UK"
"""
Prints high temperatures and conditions for next few days of weather forecast

Default city: %s
""" % default_city

import os
import sys
from urllib import urlopen
from xml.etree.ElementTree import parse


weather_url = "http://api.wunderground.com/auto/wui/geo/ForecastXML/index.xml?query=%s"

def pairs(iterable):
    iterator = iter(iterable)
    while True:
        yield iterator.next(), iterator.next()

def every(iterable, step=2):
    iterator = iter(iterable)
    while True:
        yield iterator.next()
        for i in range(step):
            iterator.next()

def forecast(city):
    data = urlopen(weather_url % city)
    parsed = parse(data)
    temps = [el.text for el in parsed.findall("./simpleforecast/forecastday/*/celsius")]
    conds = [el.text for el in parsed.findall("./simpleforecast/forecastday/conditions")]
    days = pairs(temps)
    highs = every(temps)
    return ",".join(["%s/%s" % (h, c) for h, c in zip(highs, conds)])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cities = sys.argv[1:]
    else:
        cities = [default_city]
    for city in cities:
        print forecast(city)





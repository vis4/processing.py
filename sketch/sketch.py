
from p9 import *
import csv

cities = []


def setup():
    global cities
    size(360, 180, JAVA2D)
    db = csv.reader(open('../cities1000.txt', 'r'), dialect='excel-tab')
    for city in db:
        cities.append(map(float, city[4:6]))
    noLoop()


def draw():
    background(0)
    stroke(255)
    print "Processing w/o Java syntax"
    for lat, lon in cities:
        point(lon + 180, 90 - lat)

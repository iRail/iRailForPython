#!/usr/bin/env python

from irail.model import *
from irail import api

def test_getstations():
  r = api.get_stations()
  print "Version: " + r.version()
  print "Timestamp: " + r.timestamp()
  for station in r.stations():
    print station

if __name__=="__main__":
  test_getstations()

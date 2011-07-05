#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2011, Wouter Horré
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from irail.model import *
from irail.api import iRailAPI

def test_getstations():
  api = iRailAPI()
  r = api.get_stations()
  print "Version: " + r.version()
  print "Timestamp: " + r.timestamp()
  for station in r.stations():
    print station

def test_searchstations():
  api = iRailAPI()
  stations = api.search_stations("bru")
  print "--- Stations starting with bru ---"
  for station in stations:
    print station

def test_getschedules():
  api = iRailAPI()
  schedules = api.get_schedules_by_names("Courtrai", "Leuven")
  for schedule in schedules.connections():
    print schedule

def test_getliveboard():
  api = iRailAPI()
  schedule = api.get_liveboard_by_name("Gentbrugge")
  print schedule
  #schedule = api.get_liveboard_by_id("BE.NMBS.008893179")
  #print schedule

def test_getvehicle():
  api = iRailAPI()
  schedule = api.get_vehicle_by_id("Be.NMBS.P1234")
  print schedule

if __name__=="__main__":
#  test_getstations()
#  test_searchstations()   test_getschedules()
  test_getliveboard()
#  test_getvehicle()

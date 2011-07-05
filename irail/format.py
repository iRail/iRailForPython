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

import json

from model import *

class JsonFormat:

  def __init__(self):
    self.__format = "json"

  def format(self):
    return self.__format

  def __str__(self):
    return self.format()

  def __convert_station_list(self, dict):
    stations = []
    for s in dict['station']:
      stations.append(self.__convert_station(s))
    return StationList(dict['timestamp'], dict['version'], stations)

  def __convert_station(self, dict):
    return Station(dict['name'], dict['standardname'], dict['id'], dict['locationX'], dict['locationY'])

  def parse_stations(self, response):
    return self.__convert_station_list(json.load(response))

  def __convert_schedule_list(self, dict):
    schedules = []
    for s in dict['connection']:
      schedules.append(self.__convert_schedule(s))
    return ConnectionList(dict['timestamp'], dict['version'], schedules)

  def __convert_schedule(self, dict):
    departure = self.__convert_departure(dict['departure'])
    if dict.has_key('vias'):
      vias = self.__convert_vias(dict['vias'])
    else:
      vias = None
    arrival = self.__convert_arrival(dict['arrival'])
    return Connection(dict['id'], departure, vias, arrival, dict['duration'])

  def __convert_departure(self, dict):
    return self.__convert_connection_event(dict, Departure)

  def __convert_connection_event(self, dict, clazz):
    station = self.__convert_station(dict['stationinfo'])
    platform = dict['platform'] # TODO use platforminfo
    time = dict['time']
    delay = dict['delay']
    vehicle = dict['vehicle']
    direction = self.__convert_station(dict['direction'])
    return clazz(station, platform, time, delay, vehicle, direction)

  def __convert_arrival(self, dict):
    return self.__convert_connection_event(dict, Arrival)

  def __convert_vias(self, dict):
    return dict

  def parse_schedules(self, response):
    return self.__convert_schedule_list(json.load(response))

  def parse_liveboard(self, response):
      return self.__convert_liveboard(json.load(response))

  def __convert_liveboard(self, dict):
      return ObjectFactory(dict['departures']['departure'])

  def parse_vehicle(self, response):
      return self.__convert_vehicle(json.load(response))

  def __convert_vehicle(self, dict):
      return ObjectFactory(dict['vehicleinfo'])

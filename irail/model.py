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

class StationsResponse:

  def __init__(self, timestamp, version, stations):
    self.__timestamp = timestamp
    self.__version = version
    self.__stations = stations

  @classmethod
  def from_dict(self, dict):
    stations = []
    for s in dict['station']:
      stations.append(Station.from_dict(s))
    return self(dict['timestamp'], dict['version'], stations)

  def timestamp(self):
    return self.__timestamp

  def version(self):
    return self.__version

  def stations(self):
    return self.__stations

class Station:

  def __init__(self, name, standardname, id, locationX, locationY):
    self.__name = name
    self.__standardname = standardname
    self.__id = id
    self.__locationX = locationX
    self.__locationY = locationY

  @classmethod
  def from_dict(self, dict):
    return self(dict['name'], dict['standardname'], dict['id'], dict['locationX'], dict['locationY'])

  def name(self):
    return self.__name

  def standardname(self):
    return self.__standardname

  def id(self):
    return self.__id

  def locationX(self):
    return self.__locationX

  def locationY(self):
    return self.__locationY

  def __str__(self):
    return "Station " + self.id() + " | " + self.name() + " @ (" + self.locationY() + "," + self.locationX() + ")"


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

import urllib2
from model import *
from format import *
from exception import *

BASE_URL="http://api.irail.be/"
URLS={
    'stations':'stations'
}
DEFAULT_ARGS="?format=json"

class iRailAPI:

  def __init__(self, format=None, lang=None):
    self.set_format(format)
    self.set_lang(lang)

  def format(self):
    return self.__format

  def set_format(self, format):
    if format:
      self.__format = format
    else:
      self.__format = JsonFormat()

  def lang(self):
    return self.__lang

  def set_lang(self, lang):
    if lang:
      self.__lang = lang
    else:
      self.__lang = "EN"
  
  def do_request(self, method, args=None):
    url = BASE_URL + method
    url += "?format=" + str(self.format())
    url += "&lang=" + self.lang()
    if args:
      for key in args.keys():
        url += "&" + key + "=" + args[key]
    return urllib2.urlopen(url)
  
  def get_stations(self):
    """Retrieve the list of stations"""
    try:
      response = self.do_request(URLS['stations'])
      return self.__format.parse_stations(response)
    except Exception as e:
      raise iRailError(e)

  def search_stations(self, start):
    """Retrieve the list of stations that start with a given string"""
    stations = self.get_stations()
    return [station for station in stations.stations() if station.name().lower().startswith(start.lower())]

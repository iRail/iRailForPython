import urllib2
import json
from model import *

class iRailError:
  """Class representing an error in the iRail API"""
  def __init__(self, cause):
    self.__cause = cause

  def cause(self):
    return self.__cause

BASE_URL="http://api.irail.be/"
URLS={
    'stations':'stations'
}
DEFAULT_ARGS="?format=json"

def get_stations():
  """Retrieve the list of stations"""
  try:
    response = urllib2.urlopen(BASE_URL + URLS['stations'] + DEFAULT_ARGS)
    return StationsResponse.from_dict(json.load(response))
  except Exception as e:
    raise iRailError(e)

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


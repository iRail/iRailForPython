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

class iRailError(Exception):
  """Class representing an error in the iRail API"""
  def __init__(self, cause):
    self.__cause = cause

  def cause(self):
    return self.__cause

  def __str__(self):
    return "iRailError" + " with cause: " + str(self.cause())

class HTTPError(iRailError):
  def __init__(self, cause):
    iRailError.__init__(self, cause)

  def code(self):
    return self.cause().code

  def message(self):
    return self.cause().msg

  def __str__(self):
    return "HTTPError | code: " + str(self.code()) + " | message: " + self.message()

class ClientError(HTTPError):
  def __init__(self, cause):
    HTTPError.__init__(self, cause)

  def __str__(self):
    return "ClientError | code: " + str(self.code()) + " | message: " + self.message()

class ServerError(HTTPError):
  def __init__(self, cause):
    HTTPError.__init__(self, cause)

  def __str__(self):
    return "ServerError | code: " + str(self.code()) + " | message: " + self.message()


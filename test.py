#!/usr/bin/python2.7

import urllib
import urllib2

url = "http://192.168.1.26:8080/temps"
headers = {"Content-Type": "application/json", "Authorization": "Basic "}
data = {"param": "value"}
request = urllib2.Request(url)

for key, value in headers.items():
    request.add_header(key, value)

response = urllib2.urlopen(request)

print response.info().headers
print response.read()

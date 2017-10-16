from urllib.request import urlopen
import urllib
import json

place = input('Enter location:')
urlfinal = 'http://py4e-data.dr-chuck.net/geojson?' + urllib.parse.urlencode({'address':place})
handle = urlopen(urlfinal).read().decode()
print (json.loads(handle)['results'][0]['place_id'])
from urllib.request import urlopen
import json

urlloc = input('Enter location:')
print ('Retrieving ', urlloc)
handle = urlopen(urlloc).read().decode()
x = sum([int(each['count']) for each in json.loads(handle)['comments']])
print (x)
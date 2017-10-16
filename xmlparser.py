from urllib.request import urlopen
import xml.etree.ElementTree as ET

urlloc = input('Enter location:')
print ('Retrieving ', urlloc)
handle = urlopen(urlloc).read().decode()
tree = ET.fromstring(handle)
comment = tree.findall('comments/comment')
x = sum([int(each.find('count').text) for each in comment])
print (x)
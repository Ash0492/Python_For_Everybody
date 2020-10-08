import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')
if len(address)<1: address = 'http://py4e-data.dr-chuck.net/comments_42.xml'
print('retrieving' + address)

xml = urllib.request.urlopen(address).read()
print(str(len(xml))+ 'characters')

tree = ET.fromstring(xml)
counts = tree.findall('.//count')

sum = 0
for c in counts:
        sum = sum+int(c.text)
print(sum)

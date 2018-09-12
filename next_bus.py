import sys 

if len(sys.argv) != 3:
    raise SystemExit('Usage: next_bus.py route stopid')

# print('Command options:', sys.argv)
# raise SystemExit(0)

route = sys.argv[1]
stopid = sys.argv[2]

import urllib.request

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route={}&stop={}'.format(route,stopid))
data = u.read()
# print(data)

from xml.etree.ElementTree import XML 

doc = XML(data)

for pt in doc.findall('.//pt'):
    print(pt.text)
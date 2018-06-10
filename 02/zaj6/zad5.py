from xml.dom import minidom
import urllib.request
path = 'https://www.yr.no/place/Poland/Lublin/Lublin/forecast.xml'
sock = urllib.request.urlopen(path)

doc = minidom.parse(sock)
elements = doc.getElementsByTagName('sun')
for e in elements:
    res = e.getAttribute("rise")
    
print (res[11:])

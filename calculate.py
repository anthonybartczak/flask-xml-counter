import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("https://drive.google.com/uc?id=1BtVW0P91nobSx2BZsPKKVgz6pVTYw2KA&export=download").read().decode('ascii','ignore')
datafile = StringIO(data)
csvReader = csv.reader(datafile)
for row in csvReader:
    xmllink = row[0]
 #   xml = 'https://feeds.skapiec.pl/google-shop-38a3ae44ffe87509ef90a5773c9f1e88.xml'
    url = urllib.request.urlopen(xmllink)
    data = url.read()
    datadecoded = (data.decode())
    produkty = datadecoded.count("</item>")
    print(row[0], "liczba produktow to:  ", produkty)
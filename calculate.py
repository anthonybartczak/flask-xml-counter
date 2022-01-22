import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from io import StringIO
import csv

def calculate_item_count(url):
    # test URL "https://drive.google.com/uc?id=1BtVW0P91nobSx2BZsPKKVgz6pVTYw2KA&export=download"
    # xml = 'https://feeds.skapiec.pl/google-shop-38a3ae44ffe87509ef90a5773c9f1e88.xml'
    data = urlopen(url).read().decode('ascii','ignore')
    datafile = StringIO(data)
    csvReader = csv.reader(datafile)
    for row in csvReader:
        xmllink = row[0]
        url = urllib.request.urlopen(xmllink)
        data = url.read()
        datadecoded = (data.decode())
        #produkty = datadecoded.count("</item>")
        #print(row[0], "liczba produktow to:  ", produkty)
        return datadecoded.count("</item>")
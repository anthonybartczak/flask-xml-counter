from flask import Flask, render_template, request
import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from io import StringIO
import csv


app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html", )

@app.route("/get_item_count", methods=['POST'])
def get_item_count():
    print(request.form.get('url'))
    url = request.form.get('url')
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
        pcount = datadecoded.count("</item>")
        #print(row[0], "liczba produktow to:  ", produkty)
        #return datadecoded.count("</item>")
        return {
            "url": row[0],
            "count": pcount
        }

if __name__ == '__main__':
    app.run()
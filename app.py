from flask import Flask, render_template, request
import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from io import StringIO
import csv
import json


app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html", )

@app.route("/get_item_count", methods=['POST'])
def get_item_count():
    url = request.form.get('url')
    data = urlopen(url).read().decode('ascii','ignore')
    datafile = StringIO(data)
    csvReader = csv.reader(datafile)
    json_data = {}
    for row in csvReader:
        xmllink = row[0]
        url = urllib.request.urlopen(xmllink)
        data = url.read()
        datadecoded = (data.decode())
        pcount = datadecoded.count("</item>")
        json_data[row[0]] = pcount
    return json.dumps(json_data, indent = 4)

if __name__ == '__main__':
    app.run()
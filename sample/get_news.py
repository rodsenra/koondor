import sys
import codecs
import ujson
import requests

file_data = open(sys.argv[1], "rb").read()
news_meta = ujson.loads(file_data)['hits']['hits']
url_and_date = [(i['_source']['modified'], i['_id']) for i in news_meta]
sorted_urls = sorted(url_and_date)
for date, url in sorted_urls:
    print("Downloading " + url)
    response = requests.get(url, timeout=120)
    outfilename = "{0}.html".format(date)
    if response.status_code == 200:
        codecs.open(outfilename, "wb", encoding=response.encoding).write(response.text)
    else:
        print("Failed for {0} with {1}".format(url, response.status_code))

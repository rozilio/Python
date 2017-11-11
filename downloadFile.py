'''
download files from the web
** not working so well.. **
'''

import urllib.request
from urllib import request

url = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'

def download_file(csvUrl):
    response = request.urlopen(csvUrl)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest = r'file.csv'

    with open(dest, "w") as f:
        for line in lines:
            #print(line)
            f.write(line + "\n")

download_file(url)
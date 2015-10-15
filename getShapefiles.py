#!/usr/bin/env python

import urllib
from zipfile import ZipFile

dir = "C:/hwacallo/"

urls = ["http://biogeo.ucdavis.edu/data/gadm2/gadm_v2_shp.zip"]

def main():
    for url in urls:
        name, headers = urllib.urlretrieve(url)
        print "downloaded " + url
        zf = ZipFile(name)
        zf.extractall(dir + url[url.rfind('/'):-4])
        print "extracted " + url

if __name__ == '__main__':
    main()

print "FIN"

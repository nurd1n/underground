#!/usr/bin/env python
from mechanize import Browser
from bs4 import BeautifulSoup
import urllib2,cookielib
import re
import codecs
import sys
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)
site= "http://www.bing.com/images/search?q=Homelegance+3+Piece+Counter+Table+and+Stools+in+Blackurlbingview=detailv2urlbingqft=+filterui%3aimagesize-largeurlbingid=EEB12DBDF216398A41120573E8FD2A10AA5266ABurlbingselectedIndex=0urlbingccid=ilfcIjpFurlbingsimid=608032293238997632urlbingthid=OIP.M8a57dc223a45b80824082df18bfcba19o0"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = urllib2.Request(site, headers=hdr)

try:
    page = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.fp.read()

content = page.read()
soup = BeautifulSoup(content)
for text in soup.findAll(attrs={"class": "mainImage"}):
    print(text.get('src2'))

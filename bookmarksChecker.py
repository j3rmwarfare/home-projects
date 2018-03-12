import http.client
import urllib.request
import codecs
import pandas as pd
import re
import socket
import requests

def checkHtmlConnection(url):
    #print(url)
    #httpConnection = http.client.HTTPSConnection(url,timeout=10)
    
    #try:
    #    urlRequest = urllib.request.urlopen(url)
        #httpConnection.request("HEAD", '')
    #except socket.timeout:
    #    print("socket timeout")
    #    return(408)
    #return(httpConnection.getresponse().status == 200)
    #return(urlRequest.getcode())
    try:
        r = requests.get(url,timeout=5)
    except requests.exceptions.RequestException as e:
        print(e)
        return("failed")
    return(r.status_code)


filename="bookmarks_3_10_18.html"
newfile="bookmarks.new"
suspiciousFile="suspiciousBookmarks"

out = open(newfile,"w")
suspects = open(suspiciousFile,"w")
print("loading:", filename)

timeout = 5
socket.setdefaulttimeout(timeout)

f=codecs.open(filename, 'r')
#print(f.read())
for line in f.readlines():
    #print(line)
    if "HREF" in line:
        m = re.search('HREF="(.+?)"',line)
        url = m.group(1)
        print(url)
        status=checkHtmlConnection(url)
        if status == 200:
            print('exists: ',url)
            out.write(line)
        else:
            print('suspicious: ',url)
            suspects.write(line)

    else:
        out.write(line)

out.close()
suspects.close()
            

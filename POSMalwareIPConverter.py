# -*- coding: utf-8 -*-
import urllib
import json
serviceurl = "http://ip-api.com/json/"
f = open('ips.txt', 'r+')
w = open('where.data', 'w+')
count = 0
for line in f:
    if count > 150 : break
    try:
        url = urllib.urlopen(serviceurl+line)
        data = url.read()
        json_data = json.loads(data)
        w.write(json_data['city']+ '\n')
    except KeyError, e:
        print 'Error:', e
        continue
    except UnicodeEncodeError, e:
    	print 'Error:', e
    	continue
f.close()
w.close()
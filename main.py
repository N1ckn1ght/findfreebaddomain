from urllib.parse import urlparse
import requests
import json
import sys

print('Enter the amount of free for purchasing bad domains with https to find:')
count = int(input())
req = requests.get('https://reestr.rublacklist.net/api/v2/current/json')
js = req.json()
for i in js:
    for j in js[str(i)]:
        if 'https://' in j['link']:
            domain = urlparse(j['link']).netloc
            free = requests.get('http://api.whois.vu/?q=' + domain)
            free = free.json()['available']
            if (free == 'yes'):
                print(domain, 'is free for purchasing.')
                count -= 1
                if (count <= 0):
                    sys.exit()


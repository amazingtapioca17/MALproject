import json
import json_func as jf
import urllib
url='https://api.jikan.moe/v3/anime/2'
def extract(url):
    response=urllib.request.urlopen(url)
    data=response.read()
    response.close()
    text=data.decode(encoding = 'utf-8)')
    return text
data=extract(url)
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
          

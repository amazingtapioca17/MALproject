import json
import urllib.request
print('hi')
def extract(url):
    response=urllib.request.urlopen(url)
    data=response.read()
    response.close()
    text=data.decode(encoding = 'utf-8)')
    obj=json.loads(text)
def jsonprint(obj):
    for result in obj['results']:
        print(result['mal_id'],result['title'])

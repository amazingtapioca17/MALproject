import json
import urllib.request
NUM=0
failed_list=[]
url='https://api.jikan.moe/v3/anime/'
def extract(url,num):
    response=urllib.request.urlopen(url+str(num))
    data=response.read()
    response.close()
    text=data.decode(encoding = 'utf-8)')
    json_dict=json.loads(text)
    return json_dict
def json_dump(mal_id,data):
    with open(f'{mal_id}.json', 'w') as outfile:
        json.dump(data, outfile)
while False:
    NUM+=1
    try:
        json_dump(NUM,extract(url,NUM))
        print (f'{NUM}.json saved')
    except urllib.error.HTTPError:
        print (f'{NUM}.json failed')
        with open("test.txt", "a") as myfile:
            myfile.write(f"{NUM}\n")
        failed_list.append(NUM)
        if NUM>40000:
            break
with open('107.json') as json_file:
    json_data=json.load(json_file)
        
    
    


import json
import urllib.request
import category as cat
from collections import defaultdict
mal_id_list=[]
trait_dict=defaultdict(int)
anime_trait_dict=dict()
def extract(url):
    #extracts the json data into something useable, returns json file
    response=urllib.request.urlopen(url)
    data=response.read()
    response.close()
    text=data.decode(encoding = 'utf-8)')
    return(json.loads(text))
def anime_extract(obj):
    trait_dict[obj['type']]+=1
    anime_trait_dict[obj['mal_id']]=[]
    anime_trait_dict[obj['mal_id']].append(obj['type'])
    for genre in obj['genres']:
        anime_trait_dict[obj['mal_id']].append(genre['mal_id'])
        trait_dict[genre['mal_id']]+=1
def list_extract(mlist:'list of ids'):
    for anime_num in range(len(mlist)):
        print(f'{anime_num*100/len(mlist):.2f}% done')
        anime_extract(extract(urlcon2(mlist[anime_num])))
def searchprint(obj):
    #prints the results of the whole search
    global mal_id_list
    for result in obj['results']:
        print(result['mal_id'],result['title'])
        mal_id_list.append(result['mal_id'])
def anime_print(obj):
    #prints a single anime object details
    pass
def urlcon(score:float,*genre:str):
    #constructs the url using search constraints, currently using two genres first
    url='https://api.jikan.moe/v3/search/anime?'
    for g in sorted(genre):
        if g in cat.reverse_gd:
            url+=f'&genre={cat.reverse_gd[g]}'
    if type(score)==float or type(score)==int:
        url+=f'&score={score}'
    return url
def urlcon2(mal_id):
    #constructs a url for a single anime
    url='https://api.jikan.moe/v3/anime/'+str(mal_id)
    return url
def comp_print():
    #prints everything out together, currently uses two genres and a score
    page=0
    url=urlcon(float(input()),str(input()),str(input()))
    print(url)
    global mal_id_list
    mal_id_list=[]
    while True:
        try:
            page+=1
            print(f'page {page}')
            searchprint(extract(url+f'&page={page}'))
        except urllib.error.HTTPError:
            print('broke')
            print(mal_id_list)
            break
def splicer(td,grouplist):
    return sorted([(key,td[key]) for key in td],key=lambda t: abs(len(grouplist)/2-t[1]))[0][0]
def narrow_choices(mal_id_list):
    pass
    
    

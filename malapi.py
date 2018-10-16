import json_func as jf
import category as cat
import json
#first we have to narrow it down a lot.
#genre, score, protagonist type, maybe two genres?
#also make these all into functions lol
def firstq():
    return(str(input()),str(input()),input())
category1='https://api.jikan.moe/v3/anime/1'
genre=cat.reverse_gd['adventure']
category2="https://api.jikan.moe/v3/search/anime?genre=2&page=2&score>7.0"
category3=f"https://api.jikan.moe/v3/search/anime?genre={genre}&genre=5&page=1&score>8.0"
'''response=urllib.request.urlopen(category3)
data=response.read()
response.close()
text=data.decode(encoding = 'utf-8')
obj=json.loads(text)    
for result in obj["results"]:
    print (result["mal_id"],result["title"])'''
#this is a file writer
'''obj=jf.extract(category1)
with open('obj.json', 'w') as outfile:
    json.dump(obj, outfile)'''
#print(jf.extract(jf.urlcon2(5114)))
jf.comp_print()
jf.list_extract(jf.mal_id_list)
print(jf.trait_dict)
print(cat.gd[jf.splicer(jf.trait_dict,jf.mal_id_list)])
print(jf.anime_trait_dict)

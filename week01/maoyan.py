#!/usr/bin/env python3
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

user_agent = "User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'"
header = {'user-agent': user_agent}
my_top10_url = 'https://maoyan.com/films?showType=3'


response = requests.get(my_top10_url, headers = header)

bs_info = bs(response.text,'html.parser')
#print(bs_info)





movie_list=[]
#获取top10的影片信息
for items,tags in enumerate(bs_info.find_all('div', attrs={'class':'movie-item-hover'})):
    name = tags.find(class_='name').text
    print(name)
    movie_type = tags.find_all(class_='movie-hover-title')[1].text[5:].strip()
    print(movie_type)
    release_time = tags.find(class_='movie-hover-brief').text[7:].strip()
    print(release_time)
    movie_list.append((name,movie_type,release_time))
    if items == 10 :
        break

df = pd.DataFrame(data=movie_list)
df.to_csv('movies.csv')

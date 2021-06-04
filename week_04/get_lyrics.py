import os
import re
import time
import random
import numpy as np
import pandas as pd

import requests 

from bs4 import BeautifulSoup

curr_dir = os.path.dirname(os.path.realpath(__file__))


def get_url_extensions(artist):
    url = f'https://www.lyrics.com/artist/{artist}/'
    response = requests.get(url)
    url_ext = re.findall('href="/lyric(.+?)"',response.text)
    return url_ext
    

def save_html_sample(artist, sample_size):
    url_ext = get_url_extensions(artist)
    os.mkdir(curr_dir + f'/data/artists/{artist}')
    song_number = 0
    for song in random.choices(url_ext, k=sample_size):
        song_number += 1
        new_url = 'https://lyrics.com/lyric/' + song
        response = requests.get(new_url)  
        filename = curr_dir + f'/data/artists/{artist}/{song_number}.html'
        open(filename, 'w').write(response.text)
        print(new_url, response.status_code)
        time.sleep(10)
    return song_number

def get_lyrics_n_title(artist, num_files):
    titles = []
    lyrics = []
    artist_list = []
    for num in range(num_files):
        filename = curr_dir + f'/data/artists/{artist}/{num+1}.html'
        soup = BeautifulSoup(open(filename).read())
        title = soup.title.text
        title_clean = re.sub(r' Lyrics','',title)        
        try:          
            lyric = soup.find('pre').text
            lyric_clean = re.sub("\\n|\\'",' ',lyric)
            titles.append(title_clean)
            artist_list.append(artist)
            lyrics.append(lyric_clean)
            print(title_clean)            
        except:
            print(title_clean)
    return titles, lyrics, artist_list


def save_to_csv(titles, lyrics, artist_list):
    df = pd.DataFrame({'lyrics': lyrics, 'title': titles, 'artist': artist_list})
    df['lyrics'] = (df['title']+ ' ')*3 + ' ' + df['lyrics']
    df.to_csv(curr_dir + f'/data/{artist_list[0]}.csv')
    return f'Saved to data/{artist_list[0]}.csv'


scrape_artist = ''

save_html_sample(scrape_artist, 100)

titles, lyrics, artist_list = get_lyrics_n_title(scrape_artist, 100)

save_to_csv(titles, lyrics, artist_list)




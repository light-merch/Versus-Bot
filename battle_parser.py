import lyricsgenius as genius
from my_token import lyr_token

def get_lyrics(artist_name):
    api = genius.Genius(lyr_token)
    artist = api.search_artist(artist_name, max_songs=3)
    text = ''
    
    for song in artist.songs:
        text += song.lyrics
    
    with open(f'battle-mc/{artist_name}.txt', 'w') as f:
        f.write(text)

    with open('artists.txt', 'a') as f:
        f.write(artist_name)
        f.write(';')

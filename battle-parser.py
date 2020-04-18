import lyricsgenius as genius
from my_token import token

def get_lyrics(artist_name):
    api = genius.Genius(token)
    artist = api.search_artist(artist_name)
    text = ''
    
    for song in artist.songs:
        text += song.lyrics
    
    with open(f'battle-mc/{artist_name}.txt', 'w') as f:
        f.write(text)


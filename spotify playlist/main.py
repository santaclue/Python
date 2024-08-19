from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

Client_id=#your id
Client_Secret=# your secret


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=Client_id,
                                               client_secret=Client_Secret,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username=#your username))



date = input("Which year do you want to travel to?Type the date in YYYY-MM-DD format: ")

url = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(url)
web = response.text
soup = BeautifulSoup(web, "html.parser")
songs = soup.select(selector="li ul li h3")
song_names = [song.getText().strip() for song in songs]
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}",type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist on Spotify.Skipped.")
playlist = sp.user_playlist_create(user_id,name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"],items=song_uris)

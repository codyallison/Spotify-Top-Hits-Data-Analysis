import requests
from config import client_id
from config import client_secret

def get_spotify_token():
    auth_url = 'https://accounts.spotify.com/api/token'
    data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret}
    auth_response = requests.post(auth_url, data=data)
    access_token = auth_response.json().get('access_token')
    return access_token

def search_song_data(song_name):
    spotify_base_url= "https://api.spotify.com/v1"
    type='track'
    limit='1'
    
    headers = {'Authorization': 'Bearer {}'.format(get_spotify_token())}
    params = {'type':type,
              'limit':limit}
    
    search_endpoint = f"/search?query={song_name}"
    query_url = ''.join([spotify_base_url,search_endpoint])
    response = requests.get(query_url,headers=headers, params=params)
    results = response.json()
    return results

def search_track_data(trackID):
    spotify_base_url= f"https://api.spotify.com/v1/tracks/{trackID}"
    type='track'
    limit='1'
    
    headers = {'Authorization': 'Bearer {}'.format(get_spotify_token())}
    params = {'type':type,
              'limit':limit}
    
    response = requests.get(spotify_base_url,headers=headers, params=params)
    results = response.json()
    return results

def get_album_data(albumID):
    spotify_base_url= f"https://api.spotify.com/v1/albums/{albumID}"
    type='album'
    limit='1'
    
    headers = {'Authorization': 'Bearer {}'.format(get_spotify_token())}
    params = {'type':type,
              'limit':limit}
    
    response = requests.get(spotify_base_url,headers=headers, params=params)
    results = response.json()
    return results

def get_playlist_songs(playlist_id):
    spotify_base_url= "https://api.spotify.com/v1"

    headers = {
    'Authorization': 'Bearer {}'.format(get_spotify_token())}
    
    playlists_endpoint = f"/playlists/{playlist_id}" 
    playlist_url = ''.join([spotify_base_url,playlists_endpoint])
    response = requests.get(playlist_url,headers=headers)
    playlist = response.json()
    return playlist

def get_track_features(trackID):
    
    track_url = f"https://api.spotify.com/v1/audio-features/{trackID}"
    
    headers = {
    'Authorization': 'Bearer {}'.format(get_spotify_token())}
    
    response = requests.get(track_url, headers=headers)
    song_features = response.json()
    return song_features
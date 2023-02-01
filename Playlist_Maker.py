import pandas as pd
import spotipy
import spotipy.util as util

scope = 'playlist-modify-public'
username = "username"

token = util.prompt_for_user_token(username,scope,client_id="client_id", client_secret="client secret",redirect_uri='http://localhost:') 
sp = spotipy.Spotify(auth=token)

def CreatePlaylist(username, playlist_name):
    # Create Appropriately Titled Empty Playlist For Samples
    sp.user_playlist_create(username, name=playlist_name)
    print("Playlist Created.")
    return playlist_name

def GetTrackIDs(idcsv):
    df = pd.read_csv(idcsv)
    trackids = df["id"]
    return trackids

def GetPlaylistID(username, playlist_name):
    playlist_id = ''
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:  # iterate through playlists I follow
        if playlist['name'] == playlist_name:  # filter for newly created playlist
            playlist_id = playlist['id']
    print("Got Playlist ID.")
    return playlist_id

playlist_name = CreatePlaylist(username, playlist_name="ML Rap playlist")
track_ids = GetTrackIDs("rapdf.csv")
track_ids = list(dict.fromkeys(track_ids)) #remove duplicates
playlist_id = GetPlaylistID(username, playlist_name)

#Populate playlist with samples
sp.user_playlist_add_tracks(username, playlist_id, track_ids)

playlist_name = CreatePlaylist(username, playlist_name="ML Country playlist")
track_ids = GetTrackIDs("countrydf.csv")
track_ids = list(dict.fromkeys(track_ids)) #remove duplicates
playlist_id = GetPlaylistID(username, playlist_name)

#Populate playlist with samples
sp.user_playlist_add_tracks(username, playlist_id, track_ids)

playlist_name = CreatePlaylist(username, playlist_name="ML Rock playlist")
track_ids = GetTrackIDs("rockdf.csv")
track_ids = list(dict.fromkeys(track_ids)) #remove duplicates
playlist_id = GetPlaylistID(username, playlist_name)

#Populate playlist with samples
sp.user_playlist_add_tracks(username, playlist_id, track_ids)

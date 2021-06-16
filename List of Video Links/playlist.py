# pip install google-api-python-client
# 
#  https://www.youtube.com/playlist?list=PL-kIBfSqQg3vm9LJsLW-ct_egdWKv3WKR
# this is a youtube playlist link.
#  here code after https://www.youtube.com/playlist?list= 
# is the playlist id.
import os
from googleapiclient.discovery import build
api_key = os.environ.get("YT_API_KEY")
youtube = build('youtube', 'v3', developerkey=api_key)
request = youtube.playlists().list(
    part='contentDetails, snippet',
    playlistlId="Enter_Playlist_id"
)
pl_response = pl_request.execute()
for item in pl_response['items']:
	print(item)
	print()
import os
from googleapiclient.discovery import build
api_key = os.environ.get("YT_API_KEY")
youtube = build('youtube', 'v3', developerkey=api_key)
request = youtube.playlists().list(
    part='contentDetails, snippet',
    playlistlId="PLfqMhTWNBTe0b2nM6JHVCnAkhQRGiZMSJs"
)
pl_response = pl_request.execute()
for item in pl_response['items']:
	print(item)
	print()
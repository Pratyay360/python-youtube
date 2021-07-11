# CREATED BY PRATYAY
import os
import re
from datetime import timedelta
from googleapiclient.discovery import build


'''
ENTER API KEY COLLECTED FROM https://developers.google.com/youtube/v3/getting-started
'''
api_key = os.environ.get('API_KEY_HERE')

youtube = build('youtube', 'v3', developerKey=api_key)

hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')

total_seconds = 0


nextPageToken = None
while True:
    pl_request = youtube.playlistItems().list(
        part='contentDetails',
        ##
        ## Enter playlist id
        #  https://www.youtube.com/playlist?list=PL-kIBfSqQg3vm9LJsLW-ct_egdWKv3WKR
        # this is a youtube playlist link. 
        # here code after https://www.youtube.com/playlist?list= 
        # is the playlist id........
        playlistId="PLAYLIST_ID_HERE",
        maxResults=5000,
        pageToken=nextPageToken
    )

    pl_response = pl_request.execute()

    vid_ids = []
    for item in pl_response['items']:
        vid_ids.append(item['contentDetails']['videoId'])

    vid_request = youtube.videos().list(
        part="contentDetails",
        id=','.join(vid_ids)
    )

    vid_response = vid_request.execute()

    for item in vid_response['items']:
        duration = item['contentDetails']['duration']

        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        video_seconds = timedelta(
            hours=hours,
            minutes=minutes,
            seconds=seconds
        ).total_seconds()

        total_seconds += video_seconds

    nextPageToken = pl_response.get('nextPageToken')

    if not nextPageToken:
        break

total_seconds = int(total_seconds)

minutes, seconds = divmod(total_seconds, 60)
hours, minutes = divmod(minutes, 60)

print(f'{hours}:{minutes}:{seconds}')
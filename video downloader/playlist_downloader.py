# CREATED BY PRATYAY
'''
pip install pytube
paste playlist link then automatically heighest availavle youtube resolution will be downloaded of the whole Playlist.
'''
import pytube
playlist = pytube.Playlist('https://www.youtube.com/playlist?list=..................................') #Enter Playlist url here
print('Number of videos in playlist: %s' % len(playlist.video_urls))
for video_url in playlist.video_urls:
    youtube = pytube.YouTube(video_url)
    video = youtube.streams.get_highest_resolution()
    video.download('')
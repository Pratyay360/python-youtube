# CREATED BY PRATYAY
'''
pip install pytube
paste video link then automatically heighest availavle youtube resolution will be downloaded.
'''
import pytube
video_url = 'https://www.youtube.com/watch?v=..............................' # copy and paste url
youtube = pytube.YouTube(video_url)
video = youtube.streams.get_highest_resolution()
video.download('') 
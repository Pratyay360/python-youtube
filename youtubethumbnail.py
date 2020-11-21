import pyfiglet
import wget
#ascii_banner = pyfiglet.figlet_format("YouTube Thumbnail Downloader")
ascii_banner = "YouTube Thumbnail Downloader"
print(ascii_banner)
url= input("Enter YouTube URL : ")
id = url.split("=",1)[1]
thumbnailurl= 'https://img.youtube.com/vi/'+id + '/maxresdefault.jpg'
print("Downloading Thumbnail...")
thumbnail = wget.download(thumbnailurl)
print("\n" + "Thumbnail Downloaded")
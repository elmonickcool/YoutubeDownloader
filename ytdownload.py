
from pytube import YouTube
from pytube.cli import on_progress

from pytube.request import stream

url=input("Enter a Youtube Link:")
fe=input("Extension:") #File Extension ex. Mp4, 3gpp
yt = YouTube(url,on_progress_callback=on_progress)
print(yt.title)
print(yt.thumbnail_url)
print("Link Generating, Please Wait!") 
yt.streams.filter(file_extension=fe)

stream=yt.streams.get_by_itag(22)
print("Downloading....")

stream.download('Youtube/')

print("Download Successful!")


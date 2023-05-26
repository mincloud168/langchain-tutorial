from pytube import YouTube
import os
from moviepy.editor import AudioFileClip

def download_and_convert(url):
    # Create a YouTube object
    yt = YouTube(url)

    # Download the highest quality video
    stream = yt.streams.get_highest_resolution()
    stream.download(filename='temp_video.mp4')

    # Convert the video into mp3
    clip = AudioFileClip('temp_video.mp4')
    clip.write_audiofile('output.mp3')

    # Delete the temporary video file
    os.remove('temp_video.mp4')

# Use the function
yt_url = input("YT url:")
download_and_convert(yt_url)
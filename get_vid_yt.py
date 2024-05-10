from pytube import YouTube
import os

def download_video(url):
    yt = YouTube(url)
    out_path = '/mnt/c/Users/becode/Downloads'  # Path to Windows Downloads folder
    #out_path = os.path.join(os.path.expanduser('~'), 'Downloads')  # Path to Downloads folder
    print(f"Downloading video to: {out_path}")
    stream = yt.streams.first()
    print(f"Video file name: {stream.default_filename}")
    stream.download(output_path=out_path)

# Call the function with the URL of the video you want to download
#download_video("https://youtube.com/shorts/qUfU4JQ4RCM?si=rIQgYTut8xaK3ddQ")
download_video("https://youtu.be/tvTRZJ-4EyI?si=FMDZU4AQx12mYccY")

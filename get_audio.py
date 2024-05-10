import argparse
from pytube import YouTube
from urllib.error import HTTPError

def download_video(url):
    yt = YouTube(url)
    out_path = '/mnt/c/Users/becode/Downloads'  # Path to Windows Downloads folder
    print(f"Downloading audio to: {out_path}")
    stream = yt.streams.filter(only_audio=True).first()
    print(f"Audio file name: {stream.default_filename}")

    # Retry the download if it fails
    max_attempts = 5
    for attempt in range(max_attempts):
        try:
            stream.download(output_path=out_path)
            break
        except HTTPError:
            if attempt < max_attempts - 1:  # i.e. if not the last attempt
                print(f"Download failed, retrying ({attempt + 1}/{max_attempts})...")
            else:
                raise

# Define the argument parser
parser = argparse.ArgumentParser(description='Download audio from YouTube.')
parser.add_argument('url', type=str, help='The URL of the YouTube video.')

# Parse the arguments
args = parser.parse_args()

# Call the function with the URL passed as an argument
download_video(args.url)
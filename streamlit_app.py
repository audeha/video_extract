import streamlit as st
import tempfile
from st_files_connection import FilesConnection
from moviepy.editor import VideoFileClip

# Establish a connection using Streamlit's connection function
conn = st.connection('s3', type=FilesConnection)

# Ask the user to upload a video file
uploaded_video = st.file_uploader("Upload a video", type=['mp4', 'mov'])

# Check if a file has been uploaded
if uploaded_video is not None:
    # Upload the video to the bucket
    bucket_path = f"monbucketllama/{uploaded_video.name}"
    with conn.fs.open(bucket_path, 'wb') as f:
        f.write(uploaded_video.getvalue())
    st.success("Uploaded successfully!")

    # Download the video to a temporary local file
    with tempfile.NamedTemporaryFile(suffix=".mp4") as temp_file:
        conn.fs.download(bucket_path, temp_file.name)

        # Extract audio and save as mp3
        video_clip = VideoFileClip(temp_file.name)
        audio_clip = video_clip.audio

        # Save the audio to a temporary local file
        with tempfile.NamedTemporaryFile(suffix=".mp3") as temp_audio_file:
            audio_clip.write_audiofile(temp_audio_file.name)

            # Upload the audio file to the bucket
            audio_bucket_path = f"monbucketaudio/{uploaded_video.name}.mp3"
            with conn.fs.open(audio_bucket_path, 'wb') as f:
                f.write(temp_audio_file.read())

# Access the underlying filesystem object and list all files
files = conn.fs.ls('monbucketllama')

# Filter out video files with .mov and .mp4 extensions
video_files = [f for f in files if f.endswith('.mov') or f.endswith('.mp4')]

# Print the names of video files
for video_file in video_files:
    st.write(video_file)

if uploaded_video is not None:
    # Upload the video to the bucket
    bucket_path = f"monbucketllama/{uploaded_video.name}"
    with conn.fs.open(bucket_path, 'wb') as f:
        f.write(uploaded_video.getvalue())
    st.success("Uploaded successfully!")

    # Extract audio and save as mp3
    video_clip = VideoFileClip(bucket_path)
    audio_clip = video_clip.audio
    audio_path = f"monbucketaudio/{uploaded_video.name}.mp3"
    audio_clip.write_audiofile(audio_path)

# Access the underlying filesystem object and list all files
files = conn.fs.ls('monbucketllama')

# Filter out video files with .mov and .mp4 extensions
video_files = [f for f in files if f.endswith('.mov') or f.endswith('.mp4')]

# Print the names of video files
for video_file in video_files:
    st.write(video_file)

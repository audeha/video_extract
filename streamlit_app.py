import streamlit as st
import tempfile
from st_files_connection import FilesConnection
from moviepy.editor import VideoFileClip
import boto3
import time 

# Initialize the AWS Transcribe client
transcribe = boto3.client('transcribe')

# Establish a connection using Streamlit's connection function
conn = st.connection('s3', type=FilesConnection)

# Ask the user to upload a video file
uploaded_video = st.file_uploader("Upload a video", type=['mp4', 'mov'])

import tempfile
from moviepy.editor import VideoFileClip

if uploaded_video is not None:
    # Upload the video to the bucket
    bucket_path = f"monbucketllama/{uploaded_video.name}"
    with conn.fs.open(bucket_path, 'wb') as f:
        f.write(uploaded_video.getvalue())
    st.success("Uploaded successfully!")

    # Download the video to a temporary local file
    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as temp_file:
        conn.fs.download(bucket_path, temp_file.name)

        # Extract audio and save as mp3
        video_clip = VideoFileClip(temp_file.name)
        audio_clip = video_clip.audio

        # Save the audio to a temporary local file
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio_file:
            audio_clip.write_audiofile(temp_audio_file.name)

            # Upload the audio file to the bucket
            audio_bucket_path = f"monbucketaudio/{uploaded_video.name}.mp3"
            with conn.fs.open(audio_bucket_path, 'wb') as f:
                f.write(open(temp_audio_file.name, 'rb').read())
            
            # Create a transcription job
            transcribe.start_transcription_job(
                TranscriptionJobName='MyTranscriptionJob',
                Media={'MediaFileUri': f"s3://{audio_bucket_path}"},
                MediaFormat='mp3',
                LanguageCode='en-US',
                Settings={'ShowSpeakerLabels': True, 'MaxSpeakerLabels': 2}
            )

            # Wait for the transcription job to complete
            while True:
                status = transcribe.get_transcription_job(TranscriptionJobName='MyTranscriptionJob')
                if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
                    break
                print("Waiting for transcription job to complete...")
                time.sleep(10)

            # Print the URL of the transcription output
            print(status['TranscriptionJob']['Transcript']['TranscriptFileUri'])
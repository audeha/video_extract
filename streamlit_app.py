import boto3
import os
import sys 
import tempfile
import time
import traceback
import requests
#gefrom moviepy.editor import VideoFileClip
import streamlit as st
from st_files_connection import FilesConnection

# Initialize the AWS Transcribe client
transcribe = boto3.client('transcribe')

# Establish a connection using Streamlit's connection function
conn = FilesConnection('s3')

# Ask the user to upload a video or audio file
uploaded_file = st.file_uploader("Upload a video or audio", type=['mp4', 'mov', 'mp3'])

if uploaded_file is not None:
    # Upload the file to the bucket
    bucket_path = f"monbucketllama/{uploaded_file.name}"
    with conn.fs.open(bucket_path, 'wb') as f:
        f.write(uploaded_file.getvalue())
    st.success("Uploaded successfully!")

    # Download the file to a temporary local file
    with tempfile.NamedTemporaryFile(suffix=f".{uploaded_file.type.split('/')[-1]}", delete=False) as temp_file:
        conn.fs.download(bucket_path, temp_file.name)

    # Determine the file extension based on the uploaded file type
    file_extension = 'mp3' if uploaded_file.type == 'audio/mp3' else 'mp4'

    # Define the bucket path
    audio_bucket_path = f"monbucketaudio/{uploaded_file.name}.{file_extension}"

    try:
        # Upload the file to the bucket
        with conn.fs.open(audio_bucket_path, 'wb') as f:
            f.write(open(temp_file.name, 'rb').read())
    except Exception as e:
        print("Failed to upload file to S3:")
        print(str(e))
        print(traceback.format_exc())
        sys.exit(1)

    # Create a unique transcription job name
    base_name = os.path.basename(temp_file.name)  # Get the base name of the file
    sanitized_name = "".join(c for c in base_name if c.isalnum() or c in (' ', '.', '_'))  # Remove any special characters
    job_name = f"MyTranscriptionJob_{sanitized_name}"

        
    # Create a transcription job
    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': f"s3://{audio_bucket_path}"},
        MediaFormat='mp3',
        LanguageCode='en-US',
        Settings={'ShowSpeakerLabels': True, 'MaxSpeakerLabels': 2}
    )

    # Wait for the transcription job to complete
    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        print("Waiting for transcription job to complete...")
        time.sleep(10)

    # If the transcription job completed successfully, print the transcript
    if status['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
        transcript_file_uri = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
        transcript_text = requests.get(transcript_file_uri).json()['results']['transcripts'][0]['transcript']
        st.write(transcript_text)
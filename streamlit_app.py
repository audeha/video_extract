import streamlit as st
from st_files_connection import FilesConnection

# Establish a connection using Streamlit's connection function
conn = st.connection('gcs', type=FilesConnection)

# Ask the user to upload a video file
uploaded_video = st.file_uploader("Upload a video", type=['mp4', 'mov'])

# Check if a file has been uploaded
if uploaded_video is not None:
    # Specify the path in your bucket where the video will be stored
    # The filename will be the same as the uploaded file's name
    bucket_path = f"video_extract_streamlit/{uploaded_video.name}"

    # Upload the video to the bucket
    with conn.fs.open(bucket_path, 'wb') as f:
        f.write(uploaded_video.getvalue())
    st.success("Uploaded successfully!")

# Access the underlying filesystem object and list all files
files = conn.fs.ls('video_extract_streamlit')

# Filter out video files with .mov and .mp4 extensions
video_files = [f for f in files if f.endswith('.mov') or f.endswith('.mp4')]

# Print the names of video files
for video_file in video_files:
    st.write(video_file)

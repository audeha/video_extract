## Streamlit Video Extract App
This project is a Streamlit application designed to transcribe audio and video files into text. The goal is to extract key ideas as bullet points from meeting recordings or YouTube videos, providing a convenient way to review and reference important points.

# Features
Accepts MP3, MP4, and MOV files as input.
Outputs transcribed text from the audio content of the input file.
Utilizes AWS S3 for file storage and AWS Transcribe for transcription services.

# Usage
To use the application, simply upload your audio or video file. The application will then transcribe the file and present the key ideas as bullet points. </p>
First make sure you have all the needed libraries: `python3 pip install -r requirements`  </p>
Then run the script: `streamlit run streamlit_app.py`  </p>
If you want to get a video from youtube you must run: `python3 get_audio.py <paste your youtube url here>`  </p>
Then wait and the text will be printed in your app.

# Development
This project is currently under development. More features and improvements are coming soon.

# Technologies Used
Streamlit: An open-source app framework for Machine Learning and Data Science projects.
AWS S3: Amazon S3 (Simple Storage Service) is an object storage service that offers industry-leading scalability, data availability, security, and performance.
AWS Transcribe: Amazon Transcribe is an automatic speech recognition (ASR) service that makes it easy for developers to add speech-to-text capability to their applications.
Contributions
Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

# Author
audeha

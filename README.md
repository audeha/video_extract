# Streamlit Video Extract App
This project is a Streamlit application designed to transcribe audio and video files into text.  </p>
The goal is to extract key ideas as bullet points from meeting recordings or YouTube videos, providing a convenient way to review and reference important points.

## Features
Accepts MP3, MP4, and MOV files as input. </p>
Outputs transcribed text from the audio content of the input file. </p>
Utilizes AWS S3 for file storage and AWS Transcribe for transcription services.

## Usage
To use the application locally, you need to add your aws credentials. To do so create a new file called secrets.toml in the .streamlit folder.  </p>
`# .streamlit/secrets.toml` </p>
`AWS_ACCESS_KEY_ID = ""` </p>
`AWS_SECRET_ACCESS_KEY = ""` </p>
`AWS_DEFAULT_REGION = ""` </p>

First make sure you have all the needed libraries: `python3 pip install -r requirements`  </p>
If you want to get a video from youtube you must run: `python3 get_audio.py <paste your youtube url here>`  </p>
Then run the script: `streamlit run streamlit_app.py`  </p>
Then wait and the text will be printed in your app. </p>

Tu use the application online, go to https://videoextractaudeha.streamlit.app/ and upload your video. </p>
The application will then transcribe the file and present the key ideas as bullet points. </p>

Note that the input file must be in English. If your audio/video is in another language, you need to set your language in `LanguageCode` in the file streamlit_app.py.

## Development
This project is currently under development. More features and improvements are coming soon. </p>
Currently chances are it will not work if you don't run it from wsl because some paths are hardcoded. 

## Technologies Used
Streamlit: An open-source app framework for Machine Learning and Data Science projects. </p>
AWS S3: Amazon S3 (Simple Storage Service) is an object storage service that offers industry-leading scalability, data availability, security, and performance. </p>
AWS Transcribe: Amazon Transcribe is an automatic speech recognition (ASR) service that makes it easy for developers to add speech-to-text capability to their applications. </p>

## Contributions
Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

## Author
audeha

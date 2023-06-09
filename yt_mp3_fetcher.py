import os
from pytube import YouTube

# Prompt the user to enter a YouTube video URL
video_url = input("Enter the YouTube video URL: ")

# Create the 'sound_library' directory if it doesn't exist
directory = "./sound_library"
if not os.path.exists(directory):
    os.makedirs(directory)

try:
    # Create a YouTube object with the provided video URL
    yt = YouTube(video_url)

    # Download the audio in mp3 format
    audio = yt.streams.filter(only_audio=True).first()
    audio.download(directory)

    # Rename the downloaded file to the video title
    downloaded_file = audio.default_filename
    new_file = f"{directory}/{yt.title}.mp3"
    os.rename(f"{directory}/{downloaded_file}", new_file)

    print(f"Audio saved successfully as: {new_file}")

except Exception as e:
    print("An error occurred while downloading the audio:", str(e))

import os
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import YouTube

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Audio Downloader")
        self.resize(400, 200)

        self.url_label = QtWidgets.QLabel("Enter the YouTube video URL:", self)
        self.url_label.setGeometry(QtCore.QRect(20, 20, 200, 30))

        self.url_input = QtWidgets.QLineEdit(self)
        self.url_input.setGeometry(QtCore.QRect(20, 50, 360, 30))

        self.audio_class_label = QtWidgets.QLabel("Audio class:", self)
        self.audio_class_label.setGeometry(QtCore.QRect(250, 100, 100, 30))

        self.audio_class_dropdown = QtWidgets.QComboBox(self)
        self.audio_class_dropdown.setGeometry(QtCore.QRect(250, 130, 130, 30))
        self.populate_audio_classes()

        self.download_button = QtWidgets.QPushButton("Download Audio", self)
        self.download_button.setGeometry(QtCore.QRect(20, 100, 200, 30))
        self.download_button.clicked.connect(self.download_audio)

        self.status_label = QtWidgets.QLabel("", self)
        self.status_label.setGeometry(QtCore.QRect(20, 160, 360, 30))

    def populate_audio_classes(self):
        # Read the class names from the JSON file
        with open("audio_classes.json", "r") as file:
            audio_classes = json.load(file)

        # Populate the dropdown with the class names
        self.audio_class_dropdown.addItems(audio_classes)

    def download_audio(self):
        video_url = self.url_input.text()
        audio_class = self.audio_class_dropdown.currentText()

        # Create the 'sound_library' directory if it doesn't exist
        directory = "./sound_library"
        if not os.path.exists(directory):
            os.makedirs(directory)

        try:
            # Create a YouTube object with the provided video URL
            yt = YouTube(video_url)

            # Set the audio quality based on the selected class
            if audio_class == "High":
                audio = yt.streams.filter(only_audio=True).first()
            elif audio_class == "Medium":
                audio = yt.streams.filter(only_audio=True).filter(abr="128kbps").first()
            else:
                audio = yt.streams.filter(only_audio=True).filter(abr="64kbps").first()

            # Download the audio in mp3 format
            audio.download(directory)

            # Rename the downloaded file to the video title
            downloaded_file = audio.default_filename
            new_file = f"{directory}/{yt.title}.mp3"
            os.rename(f"{directory}/{downloaded_file}", new_file)

            self.status_label.setText(f"Audio saved successfully as: {new_file}")

        except Exception as e:
            self.status_label.setText("An error occurred while downloading the audio: " + str(e))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

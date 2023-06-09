import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton, QSlider
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QTimer

class AudioConfigWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Class configuration')
        self.setWindowIcon(QIcon('assets\ga_logo_trans.png'))  # Set the window icon

        self.setGeometry(0, 0, 600, 400)  # Set initial window size

        # Set the window flags to make the widget topmost
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        # Center the window on the screen
        window_geometry = self.frameGeometry()
        center_point = QApplication.desktop().availableGeometry().center()
        window_geometry.moveCenter(center_point)
        self.move(window_geometry.topLeft())

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        font = QFont()
        font.setPointSize(12)  # Increase the font size

        labels_layout = QHBoxLayout()

        label1 = QLabel('Select audio class:')
        label1.setFont(font)  # Apply the font
        labels_layout.addWidget(label1)

        audio_classes = ['Conspiracy', 'Sad', 'Inspirational', 'Monotone', 'Intriguing']
        combo_box1 = QComboBox()
        combo_box1.addItems(audio_classes)
        combo_box1.setFixedWidth(100)  # Set the width of the dropdown
        labels_layout.addWidget(combo_box1)

        layout.addLayout(labels_layout)

        sliders_layout = QHBoxLayout()

        label2 = QLabel('Enable keyframes:')
        label2.setFont(font)  # Apply the font
        sliders_layout.addWidget(label2)

        switch_slider = SwitchSlider()
        switch_slider.setFixedWidth(100)  # Set the width of the slider
        sliders_layout.addWidget(switch_slider)

        layout.addLayout(sliders_layout)

        layout.addStretch()  # Add stretchable space

        save_button = QPushButton('Save')
        save_button.setFont(font)  # Apply the font
        save_button.clicked.connect(lambda: self.save_config(combo_box1.currentText(), switch_slider.value()))
        layout.addWidget(save_button, alignment=Qt.AlignBottom)  # Align the save button to the bottom

        self.setLayout(layout)
        self.show()

    def save_config(self, audio_class, enable_keyframes):
        config = {
            'audio_class': audio_class,
            'enable_keyframes': enable_keyframes
        }
        with open('config.json', 'w') as config_file:
            json.dump(config, config_file)
        print('Configuration saved.')

class SwitchSlider(QSlider):
    def __init__(self):
        super().__init__(Qt.Horizontal)
        self.setRange(0, 1)
        self.setFixedSize(50, 30)
        self.setStyleSheet(
            '''
            QSlider::groove:horizontal {
                border: 1px solid #999999;
                height: 10px;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #BBBBBB, stop:1 #EEEEEE);
            }

            QSlider::sub-page:horizontal {
                background: #8CC63F;
            }

            QSlider::add-page:horizontal {
                background: #DDDDDD;
            }

            QSlider::handle:horizontal {
                background: #FFFFFF;
                border: 1px solid #999999;
                width: 20px;
                margin: -5px 0;
                border-radius: 5px;
            }
            '''
        )

    def value(self):
        return bool(super().value())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            event.accept()
            self.setValue(not self.value())
        else:
            super().mousePressEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    audio_config_widget = AudioConfigWidget()
    sys.exit(app.exec_())

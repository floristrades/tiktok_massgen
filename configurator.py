import sys
import os
import subprocess
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton, QSlider, QFrame, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QIcon, QFont, QColor
from PyQt5.QtCore import Qt
from functools import partial
 
class AudioConfigWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Class configuration')
        self.setWindowIcon(QIcon('assets/ga_logo_trans.png'))  # Set the window icon
        self.setGeometry(0, 0, 400, 700)  # Set initial window size
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
        
        profile_layout = QHBoxLayout()
        profile_layout.setContentsMargins(0, 0, 0, 0)  # Adjust top margin if needed
        profile_layout.setAlignment(Qt.AlignHCenter)  # Align the components in the middle of the horizontal axis
        profile_frame = QFrame()
        profile_frame.setStyleSheet("QFrame { border: 1px solid #82817e; border-radius: 8px; }")
        profile_layout.addWidget(profile_frame)
        profile_frame_layout = QHBoxLayout(profile_frame)
        profile_frame_layout.setContentsMargins(95, 15, 95, 15)  # Adjust margins if needed
        profile_label = QLabel('Profile Selection:')
        profile_label.setStyleSheet("QLabel { font-weight: bold; font-size: 16px; }")  # Remove the border around the label text
        profile_label.setFont(font)
        profile_frame_layout.addWidget(profile_label)
        self.profile_combo_box = QComboBox()
        self.profile_combo_box.setSizeAdjustPolicy(QComboBox.AdjustToContents)  # Adjust the size policy to fit the contents
        self.profile_combo_box.addItems(['Seamus', 'Luke belmar', 'Profile 3', 'Profile 4', 'Profile 5', 'Profile 6', 'Profile 7', 'Profile 8', 'Profile 9', 'Profile 10', 'Profile 11', 'Profile 12', 'Profile 13', 'Profile 14', 'Profile 15', 'Profile 16', 'Profile 17', 'Profile 18', 'Profile 19', 'Profile 20'])  # Add profile options
        self.profile_combo_box.setStyleSheet("QComboBox { font-size: 14px; }")
        profile_frame_layout.addWidget(self.profile_combo_box)
        

        # Add a stretch item to make the border stretch
        profile_frame_layout.addStretch()

        layout.addLayout(profile_layout)

        # Manage audio library button, create layout
        audioLib_layout = QHBoxLayout()
        audioLib_layout.setAlignment(Qt.AlignHCenter)  # Align the components in the middle of the horizontal axis
        audioLib_frame = QFrame()
        audioLib_frame.setStyleSheet("QFrame { border: 1px solid #82817e; border-radius: 8px; }")
        audioLib_layout.addWidget(audioLib_frame)
        audioLib_frame_layout = QHBoxLayout(audioLib_frame)
        audioLib_button = QPushButton("Manage audio library", self)
        audioLib_button.setFont(font)  # Apply the font
        audioLib_frame_layout.addWidget(audioLib_button)

        # Manage hashtags button
        hashtags_button = QPushButton("Manage hashtags", self)
        hashtags_button.setFont(font)  # Apply the font
        audioLib_frame_layout.addWidget(hashtags_button)
        # Connect the button's clicked signal to the method
        audioLib_button.clicked.connect(self.initialize_audioLib)
        hashtags_button.clicked.connect(self.initialize_hashtags)
        # Add a stretch item to make the border stretch
        audioLib_frame_layout.addStretch()
        layout.addLayout(audioLib_layout)
        self.setLayout(layout)
        self.show()

        # Audio class selection
        audio_label_layout = QHBoxLayout()
        audio_label = QLabel('Select audio class:')
        audio_label.setFont(font)  # Apply the font
        audio_label_layout.addWidget(audio_label)
        audio_classes = ['Conspiracy', 'Sad', 'Inspirational', 'Monotone', 'Intriguing']
        self.audio_class_box = QComboBox()
        self.audio_class_box.addItems(audio_classes)
        self.audio_class_box.setFixedWidth(125)  # Set the width of the dropdown
        audio_label_layout.addWidget(self.audio_class_box)
        layout.addLayout(audio_label_layout)

        # Enable keyframes
        keyframes_layout = QHBoxLayout()
        keyframes_label = QLabel('Enable keyframes:')
        keyframes_label.setFont(font)  # Apply the font
        keyframes_layout.addWidget(keyframes_label)
        self.keyframes_slider = SwitchSlider()
        self.keyframes_slider.setFixedWidth(125)  # Set the width of the slider
        keyframes_layout.addWidget(self.keyframes_slider)
        layout.addLayout(keyframes_layout)

        # Filter selection
        filter_layout = QHBoxLayout()
        filter_label = QLabel('Select filter:')
        filter_label.setFont(font)  # Apply the font
        filter_layout.addWidget(filter_label)
        filter_classes = ['True', 'False', '4K']
        self.filter_combo_box = QComboBox()
        self.filter_combo_box.addItems(filter_classes)
        self.filter_combo_box.setFixedWidth(125)  # Set the width of the dropdown
        filter_layout.addWidget(self.filter_combo_box)
        layout.addLayout(filter_layout)

        # Animation IN type selection
        animation_in_layout = QHBoxLayout()
        animation_in_label = QLabel('Select animation IN type:')
        animation_in_label.setFont(font)  # Apply the font
        animation_in_layout.addWidget(animation_in_label)
        animation_in_classes = ['In', 'Out', 'None']
        self.animation_in_combo_box = QComboBox()
        self.animation_in_combo_box.addItems(animation_in_classes)
        self.animation_in_combo_box.setFixedWidth(125)  # Set the width of the dropdown
        animation_in_layout.addWidget(self.animation_in_combo_box)
        layout.addLayout(animation_in_layout)

        # Animation IN timer selection
        animation_in_tmr_layout = QHBoxLayout()
        animation_in_tmr_label = QLabel('Select animation IN timer:')
        animation_in_tmr_label.setFont(font)  # Apply the font
        animation_in_tmr_layout.addWidget(animation_in_tmr_label)
        animation_classes = ['0.2', '0.3', '0.4']
        self.animation_in_tmr_combo_box = QComboBox()
        self.animation_in_tmr_combo_box.addItems(animation_classes)
        self.animation_in_tmr_combo_box.setFixedWidth(125)  # Set the width of the dropdown
        animation_in_tmr_layout.addWidget(self.animation_in_tmr_combo_box)
        layout.addLayout(animation_in_tmr_layout)

        # Hook selection
        hook_layout = QHBoxLayout()
        hook_label = QLabel('Enable hook:')
        hook_label.setFont(font)
        hook_layout.addWidget(hook_label)
        self.hook_slider = SwitchSlider()
        self.hook_slider.setFixedWidth(125)
        hook_layout.addWidget(self.hook_slider)
        layout.addLayout(hook_layout)

        # Overlays selection
        overlays_layout = QHBoxLayout()
        overlays_label = QLabel('Select overlays:')
        overlays_label.setFont(font)  # Apply the font
        overlays_layout.addWidget(overlays_label)
        overlays_classes = ['Yes', 'No', 'Gaining']
        self.overlays_combo_box = QComboBox()
        self.overlays_combo_box.addItems(overlays_classes)
        self.overlays_combo_box.setFixedWidth(125)  # Set the width of the dropdown
        overlays_layout.addWidget(self.overlays_combo_box)
        layout.addLayout(overlays_layout)

        # CC filter selection
        cc_filter_layout = QHBoxLayout()
        cc_filter_layout.setSpacing(0)  # Remove spacing between labels
        cc_filter_label = QLabel('Select CC filter:')
        cc_filter_label.setFont(font)  # Apply the font
        cc_filter_classes = ['Grey orange', 'Love city', 'Serang', 'Dark silver', 'Quality 1']
        self.cc_filter_combo_box = QComboBox()
        self.cc_filter_combo_box.addItems(cc_filter_classes)
        self.cc_filter_combo_box.setFixedWidth(125)  # Set the width of the dropdown

        # Create the red box with "PRO" label
        red_box = QFrame()
        red_box.setObjectName("redBox")
        red_box.setStyleSheet("QFrame#redBox { background-color: red; border-radius: 20px; }")
        red_box.setFixedSize(30, 20)  # Adjust the size of the red box
        red_box.setContentsMargins(0, 0, 0, 0)  # Remove margins

        pro_label = QLabel('PRO')
        pro_label.setObjectName("proLabel")
        pro_label.setStyleSheet("""
            QLabel#proLabel {
                color: white;
                font-size: 12px;
                background-color: red;
                padding: 1px;
                border-radius: 2px;
                position: absolute;
                top: -8px;
                right: -8px;
            }
        """)  # Apply CSS styling to position the label as an overlay with padding

        pro_layout = QHBoxLayout(red_box)
        pro_layout.addWidget(pro_label)
        pro_layout.setContentsMargins(0, 0, 0, 0)  # Remove layout margins
        cc_filter_layout.addWidget(cc_filter_label)
        cc_filter_layout.addWidget(red_box)
        spacer = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        cc_filter_layout.addItem(spacer)
        cc_filter_layout.addWidget(self.cc_filter_combo_box)
        layout.addLayout(cc_filter_layout)

        # Create a new section frame with styling
        section_frame = QFrame()
        section_frame.setStyleSheet("QFrame { border: 1px solid #82817e; border-radius: 8px; }")

        # Create a vertical layout for the new section
        new_section_layout = QVBoxLayout()
        new_section_layout.setSpacing(10)  # Adjust spacing between the new section components

        # Title header
        title_header_layout = QHBoxLayout()
        title_header_layout.setContentsMargins(0, 3, 0, 10)  # Adjust margins as needed
        title_label = QLabel("Text settings")
        title_label.setStyleSheet("QLabel { border: 1px solid #82817e; border-radius: 8px;font-weight: bold; font-size: 16px; }")  # Adjust font styling as needed
        title_header_layout.addWidget(title_label, alignment=Qt.AlignCenter)

        new_section_layout.addLayout(title_header_layout)

        # Auto-generated text selection
        auto_generated_layout = QHBoxLayout()
        auto_generated_layout.setSpacing(0)  # Remove spacing between labels
        label_auto_generated = QLabel('Auto-generated text:')
        label_auto_generated.setStyleSheet("QLabel { border: none; }")
        label_auto_generated.setFont(font)
        auto_generated_layout.addWidget(label_auto_generated)
        self.auto_generated_combo_box = QComboBox()
        self.auto_generated_combo_box.addItems(['Yes', 'No'])
        self.auto_generated_combo_box.setFixedWidth(125)
        auto_generated_layout.addWidget(self.auto_generated_combo_box)
        new_section_layout.addLayout(auto_generated_layout)

        # Highlight text color selection
        highlight_text_color_layout = QHBoxLayout()
        highlight_text_color_layout.setSpacing(0)
        highlight_label_text_color = QLabel('Highlighted text colour:')
        highlight_label_text_color.setStyleSheet("QLabel { border: none; }")
        highlight_label_text_color.setFont(font)
        highlight_text_color_layout.addWidget(highlight_label_text_color)
        self.highlight_text_color_combo_box = QComboBox()
        self.highlight_text_color_combo_box.addItems(['Yellow', 'Red', 'Turquoise'])
        self.highlight_text_color_combo_box.setFixedWidth(125)
        highlight_text_color_layout.addWidget(self.highlight_text_color_combo_box)
        new_section_layout.addLayout(highlight_text_color_layout)

        # Add the section frame to the new section layout
        section_frame.setLayout(new_section_layout)
        layout.addWidget(section_frame)

        # Text font selection
        font_layout = QHBoxLayout()
        font_layout.setSpacing(0)
        font_label_size = QLabel('Text font:')
        font_label_size.setStyleSheet("QLabel { border: none; }")
        font_label_size.setFont(font)
        font_layout.addWidget(font_label_size)
        self.font_combo_box = QComboBox()
        self.font_combo_box.addItems(['No fonts found'])
        self.font_combo_box.setFixedWidth(125)
        font_layout.addWidget(self.font_combo_box)
        new_section_layout.addLayout(font_layout)

        # Text outline selection
        text_outline_layout = QHBoxLayout()
        text_outline_layout.setSpacing(0)
        text_outline_size = QLabel('Text outline:')
        text_outline_size.setStyleSheet("QLabel { border: none; }")
        text_outline_size.setFont(font)
        text_outline_layout.addWidget(text_outline_size)
        self.text_outline_combo_box = QComboBox()
        self.text_outline_combo_box.addItems(['First option'])
        self.text_outline_combo_box.setFixedWidth(125)
        text_outline_layout.addWidget(self.text_outline_combo_box)
        new_section_layout.addLayout(text_outline_layout)

        # Text glow selection
        text_glow_layout = QHBoxLayout()
        text_glow_layout.setSpacing(0)
        text_glow_size = QLabel('Text glow:')
        text_glow_size.setStyleSheet("QLabel { border: none; }")
        text_glow_size.setFont(font)
        text_glow_layout.addWidget(text_glow_size)
        self.text_glow_combo_box = QComboBox()
        self.text_glow_combo_box.addItems(['Yes', 'No', 'Pro'])
        self.text_glow_combo_box.setFixedWidth(125)
        text_glow_layout.addWidget(self.text_glow_combo_box)
        new_section_layout.addLayout(text_glow_layout)

        # Text animation selection
        text_animation_layout = QHBoxLayout()
        text_animation_layout.setSpacing(0)
        text_animation_size = QLabel('Animation for text:')
        text_animation_size.setStyleSheet("QLabel { border: none; }")
        text_animation_size.setFont(font)
        text_animation_layout.addWidget(text_animation_size)
        self.text_animation_combo_box = QComboBox()
        self.text_animation_combo_box.addItems(['CAP: Shimmer + neg_glow', 'CAP: Ripple II', 'CAP: Ripple III', 'CAP: Spring', 'CAP: Word by word', 'ANI: Bounce in_0.2s'])
        self.text_animation_combo_box.setFixedWidth(125)
        text_animation_layout.addWidget(self.text_animation_combo_box)
        new_section_layout.addLayout(text_animation_layout)

        # Overlay animation IN selection
        overlay_animation_in_text_layout = QHBoxLayout()
        overlay_animation_in_text_layout.setSpacing(0)
        overlay_animation_in_text_size = QLabel('Overlay animation IN:')
        overlay_animation_in_text_size.setStyleSheet("QLabel { border: none; }")
        overlay_animation_in_text_size.setFont(font)
        overlay_animation_in_text_layout.addWidget(overlay_animation_in_text_size)
        self.overlay_animation_in_text_combo_box = QComboBox()
        self.overlay_animation_in_text_combo_box.addItems(['Unfold', 'Shake 3', 'Rock vertical', 'Rock horizontal', 'Zoom 1', 'Zoom 2'])
        self.overlay_animation_in_text_combo_box.setFixedWidth(125)
        overlay_animation_in_text_layout.addWidget(self.overlay_animation_in_text_combo_box)
        new_section_layout.addLayout(overlay_animation_in_text_layout)

        # Stroke size selection
        stroke_size_layout = QHBoxLayout()
        stroke_size_layout.setSpacing(0)
        label_stroke_size = QLabel('Stroke size:')
        label_stroke_size.setStyleSheet("QLabel { border: none; }")
        label_stroke_size.setFont(font)
        stroke_size_layout.addWidget(label_stroke_size)
        self.stroke_size_combo_box = QComboBox()
        self.stroke_size_combo_box.addItems(['35'])
        self.stroke_size_combo_box.setFixedWidth(125)
        stroke_size_layout.addWidget(self.stroke_size_combo_box)
        new_section_layout.addLayout(stroke_size_layout)

        # Caption selection
        caption_layout = QHBoxLayout()
        caption_layout.setSpacing(0)
        label_caption = QLabel('Caption:')
        label_caption.setStyleSheet("QLabel { border: none; }")
        label_caption.setFont(font)
        caption_layout.addWidget(label_caption)
        self.caption_combo_box = QComboBox()
        self.caption_combo_box.addItems(['Yes', 'No'])
        self.caption_combo_box.setFixedWidth(125)
        caption_layout.addWidget(self.caption_combo_box)
        new_section_layout.addLayout(caption_layout)

        # Add the new section layout to the main layout
        layout.addLayout(new_section_layout)

        # Save Button
        save_button = QPushButton('Save')
        save_button.setFont(font)  # Apply the font
        save_button.clicked.connect(self.save_config)

        # Create a vertical spacer to push the save button to the bottom
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        # Add the save button to the layout
        layout.addWidget(save_button, alignment=Qt.AlignBottom)  # Align the save button to the bottom of the window
        license_build_layout = QHBoxLayout()
        license_build_layout.setSpacing(0)  # Remove spacing between labels

        # Create a QVBoxLayout for license and build information
        license_build_vlayout = QVBoxLayout()
        license_label = QLabel('License status: Active')
        license_font = QFont()
        license_font.setPointSize(7)
        license_label.setFont(license_font)
        license_label.setContentsMargins(0, 0, 0, 0)  # Remove margins

        # Set the color of the word "Active" to green
        active_word_color = QColor('green')
        license_text = license_label.text().replace('Active', '<font color="{}">Active</font>'.format(active_word_color.name()))
        license_label.setText(license_text)

        # Create the build label
        build_label = QLabel('Build: 0.0.6')
        build_label.setFont(license_font)
        build_label.setContentsMargins(0, 0, 0, 0)  # Remove margins

        # Add the build and license labels to the license_build_vlayout
        license_build_vlayout.addWidget(build_label, alignment=Qt.AlignLeft)
        license_build_vlayout.addSpacing(0)  # Add a fixed spacing of 100px
        license_build_vlayout.addWidget(license_label, alignment=Qt.AlignLeft)

        # Add the license_build_vlayout to the license_build_layout
        license_build_layout.addLayout(license_build_vlayout)

        # Add the license_build_layout to the main layout
        layout.addLayout(license_build_layout)
        layout.addWidget(save_button, alignment=Qt.AlignBottom)  # Align the save button to the bottom of the window

        self.setLayout(layout)
        self.show()

    def initialize_audioLib(self):
        print("Initializing audio library...")
        file_path = os.path.abspath("yt_mp3_fetcher.pyw")
        subprocess.call(["start", file_path], shell=True)

    def initialize_hashtags(self):
        print("Initializing hashtags...")

    def save_config(self):
        try:
            with open('config.json', 'r') as file:
                profiles = json.load(file)
        except FileNotFoundError:
            profiles = {}

        # Update the profiles dictionary with the selected profile
        profiles[self.profile_combo_box.currentText()] = {
            'audio_class': self.audio_class_box.currentText(),
            'enable_keyframes': self.keyframes_slider.value(),
            'filter': self.filter_combo_box.currentText(),
            'animation_in_type': self.animation_in_combo_box.currentText(),
            'animation_in_timer': self.animation_in_tmr_combo_box.currentText(),
            'enable_hook': self.hook_slider.value(),
            'overlays': self.overlays_combo_box.currentText(),
            'cc_filter': self.cc_filter_combo_box.currentText(),
            'auto_gen_text': self.auto_generated_combo_box.currentText(),
            'highlighted_text_colour': self.highlight_text_color_combo_box.currentText(),
            'text_font': self.font_combo_box.currentText(),
            'text_outline': self.text_outline_combo_box.currentText(),
            'text_glow': self.text_glow_combo_box.currentText(),
            'animation_text': self.text_animation_combo_box.currentText(),
            'overlay_animation_in': self.overlay_animation_in_text_combo_box.currentText(),
            'stroke_size': self.stroke_size_combo_box.currentText(),
            'caption': self.caption_combo_box.currentText() 
        }

        with open('config.json', 'w') as file:
            json.dump(profiles, file, indent=4)

        # Optional: Provide feedback to the user
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
                border-radius: 8px;
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

class AudioLib(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Audio Library')
        self.setGeometry(0, 0, 400, 300)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    audio_config_widget = AudioConfigWidget()
    sys.exit(app.exec_())

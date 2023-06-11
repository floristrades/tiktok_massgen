import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton, QSlider, QFrame, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QIcon, QFont, QColor
from PyQt5.QtCore import Qt

class AudioConfigWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Class configuration')
        self.setWindowIcon(QIcon('assets/ga_logo_trans.png'))  # Set the window icon

        self.setGeometry(0, 0, 400, 700)  # Set initial window size

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

        library_vlayout = QVBoxLayout()

        profile_layout = QHBoxLayout()
        profile_layout.setContentsMargins(0, 0, 0, 0)  # Adjust top margin if needed
        profile_layout.setAlignment(Qt.AlignHCenter)  # Align the components in the middle of the horizontal axis

        profile_frame = QFrame()
        profile_frame.setStyleSheet("QFrame { border: 1px solid #82817e; border-radius: 8px; }")
        profile_layout.addWidget(profile_frame)

        profile_frame_layout = QHBoxLayout(profile_frame)
        profile_frame_layout.setContentsMargins(95, 15, 95, 15)  # Adjust margins if needed

        profile_label = QLabel('Profile Selection:')
        profile_label.setStyleSheet("QLabel { border: none; }")  # Remove the border around the label text
        profile_label.setFont(font)
        profile_frame_layout.addWidget(profile_label)

        profile_combo_box = QComboBox()
        profile_combo_box.setSizeAdjustPolicy(QComboBox.AdjustToContents)  # Adjust the size policy to fit the contents
        profile_combo_box.addItems(['Seamus magic formula', 'Luke belmar', 'Profile 3'])  # Add profile options
        profile_frame_layout.addWidget(profile_combo_box)

        # Add a stretch item to make the border stretch
        profile_frame_layout.addStretch()

        layout.addLayout(profile_layout)

        audioLib_layout = QHBoxLayout()
        audioLib_layout.setContentsMargins(0, 0, 0, 0)  # Adjust top margin if needed
        audioLib_layout.setAlignment(Qt.AlignHCenter)  # Align the components in the middle of the horizontal axis

        audioLib_frame = QFrame()
        audioLib_frame.setStyleSheet("QFrame { border: 1px solid #82817e; border-radius: 8px; }")
        audioLib_layout.addWidget(audioLib_frame)

        audioLib_frame_layout = QHBoxLayout(audioLib_frame)
        audioLib_frame_layout.setContentsMargins(10, 10, 10, 10)  # Adjust margins if needed

        audioLib_button = QPushButton("Manage audio library", self)
        audioLib_button.setFont(font)  # Apply the font
        audioLib_frame_layout.addWidget(audioLib_button)

        spacer = QSpacerItem(10, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)  # Adjust the size policy to Fixed
        audioLib_frame_layout.addItem(spacer)

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
        # dropdown
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

        # Enable keyframes
        # Slider
        sliders_layout = QHBoxLayout()

        label2 = QLabel('Enable keyframes:')
        label2.setFont(font)  # Apply the font
        sliders_layout.addWidget(label2)

        switch_slider = SwitchSlider()
        switch_slider.setFixedWidth(100)  # Set the width of the slider
        sliders_layout.addWidget(switch_slider)

        layout.addLayout(sliders_layout)

        # Filter selection
        # Dropdown
        filter_layout = QHBoxLayout()

        label3 = QLabel('Select filter:')
        label3.setFont(font)  # Apply the font
        filter_layout.addWidget(label3)

        filter_classes = ['True', 'False', '4K']
        filter_combo_box = QComboBox()
        filter_combo_box.addItems(filter_classes)
        filter_combo_box.setFixedWidth(100)  # Set the width of the dropdown
        filter_layout.addWidget(filter_combo_box)

        layout.addLayout(filter_layout)

        # Animation selection
        # Dropdown
        animation_layout = QHBoxLayout()

        label4 = QLabel('Select animation:')
        label4.setFont(font)  # Apply the font
        animation_layout.addWidget(label4)

        animation_classes = ['In', 'Out', 'None']
        animation_combo_box = QComboBox()
        animation_combo_box.addItems(animation_classes)
        animation_combo_box.setFixedWidth(100)  # Set the width of the dropdown
        animation_layout.addWidget(animation_combo_box)

        layout.addLayout(animation_layout)

        # Hook selection
        # Slider
        hook_layout = QHBoxLayout()

        label5 = QLabel('Enable hook:')
        label5.setFont(font)
        hook_layout.addWidget(label5)

        hook_slider = SwitchSlider()
        hook_slider.setFixedWidth(100)
        hook_layout.addWidget(hook_slider)

        layout.addLayout(hook_layout)

        # Overlays selection
        # Dropdown
        overlays_layout = QHBoxLayout()

        label6 = QLabel('Select overlays:')
        label6.setFont(font)  # Apply the font
        overlays_layout.addWidget(label6)

        overlays_classes = ['Yes', 'No', 'Gaining']
        overlays_combo_box = QComboBox()
        overlays_combo_box.addItems(overlays_classes)
        overlays_combo_box.setFixedWidth(100)  # Set the width of the dropdown
        overlays_layout.addWidget(overlays_combo_box)

        layout.addLayout(overlays_layout)

        # CC filter selection
        cc_filter_layout = QHBoxLayout()
        cc_filter_layout.setSpacing(0)  # Remove spacing between labels

        label7 = QLabel('Select CC filter:')
        label7.setFont(font)  # Apply the font

        cc_filter_classes = ['Grey orange', 'Love city', 'Serang', 'Dark silver', 'Quality 1']
        cc_filter_combo_box = QComboBox()
        cc_filter_combo_box.addItems(cc_filter_classes)
        cc_filter_combo_box.setFixedWidth(100)  # Set the width of the dropdown

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

        cc_filter_layout.addWidget(label7)
        cc_filter_layout.addWidget(red_box)

        spacer = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        cc_filter_layout.addItem(spacer)

        cc_filter_layout.addWidget(cc_filter_combo_box)

        # Add cc_filter_layout to the main layout
        layout.addLayout(cc_filter_layout)

        # Create a new section frame with styling
        section_frame = QFrame()
        section_frame.setStyleSheet("QFrame { border: 1px solid #82817e; border-radius: 8px; }")

        # Create a vertical layout for the new section
        new_section_layout = QVBoxLayout()
        new_section_layout.setSpacing(10)  # Adjust spacing between the new section components

        # Auto-generated text selection
        auto_generated_layout = QHBoxLayout()
        auto_generated_layout.setSpacing(0)  # Remove spacing between labels
        label_auto_generated = QLabel('Auto-generated text:')
         # Removes indiv borders
        label_auto_generated.setStyleSheet("QLabel { border: none; }")
        label_auto_generated.setFont(font)
        auto_generated_layout.addWidget(label_auto_generated)
        auto_generated_combo_box = QComboBox()
        auto_generated_combo_box.addItems(['Yes', 'No'])
        auto_generated_combo_box.setFixedWidth(100)
        auto_generated_layout.addWidget(auto_generated_combo_box)

        new_section_layout.addLayout(auto_generated_layout)

        # Text color selection
        text_color_layout = QHBoxLayout()
        text_color_layout.setSpacing(0)
        label_text_color = QLabel('Colour:')
        label_text_color.setStyleSheet("QLabel { border: none; }")
        label_text_color.setFont(font)
        text_color_layout.addWidget(label_text_color)
        text_color_combo_box = QComboBox()
        text_color_combo_box.addItems(['Red', 'Blue', 'Green'])
        text_color_combo_box.setFixedWidth(100)
        
        text_color_layout.addWidget(text_color_combo_box)
        new_section_layout.addLayout(text_color_layout)

        # Add the section frame to the new section layout
        section_frame.setLayout(new_section_layout)
        layout.addWidget(section_frame)

        # Stroke size selection
        stroke_size_layout = QHBoxLayout()
        stroke_size_layout.setSpacing(0)
        label_stroke_size = QLabel('Stroke size:')
        label_stroke_size.setStyleSheet("QLabel { border: none; }")
        label_stroke_size.setFont(font)
        stroke_size_layout.addWidget(label_stroke_size)
        stroke_size_combo_box = QComboBox()
        stroke_size_combo_box.addItems(['Small', 'Medium', 'Large'])
        stroke_size_combo_box.setFixedWidth(100)
        stroke_size_layout.addWidget(stroke_size_combo_box)

        new_section_layout.addLayout(stroke_size_layout)

        # Text animation selection
        text_animation_layout = QHBoxLayout()
        text_animation_layout.setSpacing(0)
        text_label_animation = QLabel('Animation:')
        text_label_animation.setStyleSheet("QLabel { border: none; }")
        text_label_animation.setFont(font)
        text_animation_layout.addWidget(text_label_animation)
        text_animation_combo_box = QComboBox()
        text_animation_combo_box.addItems(['Fade', 'Slide', 'Zoom'])
        text_animation_combo_box.setFixedWidth(100)
        text_animation_layout.addWidget(text_animation_combo_box)

        new_section_layout.addLayout(text_animation_layout)

        # Caption selection
        caption_layout = QHBoxLayout()
        caption_layout.setSpacing(0)
        label_caption = QLabel('Caption:')
        label_caption.setStyleSheet("QLabel { border: none; }")
        label_caption.setFont(font)
        caption_layout.addWidget(label_caption)
        caption_combo_box = QComboBox()
        caption_combo_box.addItems(['Yes', 'No'])
        caption_combo_box.setFixedWidth(100)
        caption_layout.addWidget(caption_combo_box)

        new_section_layout.addLayout(caption_layout)

        # Caption when yes selection
        caption_yes_layout = QHBoxLayout()
        caption_yes_layout.setSpacing(0)
        label_caption_yes = QLabel('Caption when yes:')
        label_caption_yes.setStyleSheet("QLabel { border: none; }")
        label_caption_yes.setFont(font)
        caption_yes_layout.addWidget(label_caption_yes)
        caption_yes_combo_box = QComboBox()
        caption_yes_combo_box.addItems(['Option 1', 'Option 2', 'Option 3'])
        caption_yes_combo_box.setFixedWidth(100)
        caption_yes_layout.addWidget(caption_yes_combo_box)

        new_section_layout.addLayout(caption_yes_layout)

        # Animation in selection
        animation_in_layout = QHBoxLayout()
        animation_in_layout.setSpacing(0)
        label_animation_in = QLabel('Animation in:')
        label_animation_in.setStyleSheet("QLabel { border: none; }")
        label_animation_in.setFont(font)
        animation_in_layout.addWidget(label_animation_in)
        animation_in_combo_box = QComboBox()
        animation_in_combo_box.addItems(['Option 1', 'Option 2', 'Option 3'])
        animation_in_combo_box.setFixedWidth(100)
        animation_in_layout.addWidget(animation_in_combo_box)

        new_section_layout.addLayout(animation_in_layout)

        # Animation when yes selection
        animation_yes_layout = QHBoxLayout()
        animation_yes_layout.setSpacing(0)
        label_animation_yes = QLabel('Animation when yes:')
        label_animation_yes.setStyleSheet("QLabel { border: none; }")
        label_animation_yes.setFont(font)
        animation_yes_layout.addWidget(label_animation_yes)
        animation_yes_combo_box = QComboBox()
        animation_yes_combo_box.addItems(['Option 1', 'Option 2', 'Option 3'])
        animation_yes_combo_box.setFixedWidth(100)
        animation_yes_layout.addWidget(animation_yes_combo_box)

        new_section_layout.addLayout(animation_yes_layout)

        # Text font selection
        text_font_layout = QHBoxLayout()
        text_font_layout.setSpacing(0)
        label_text_font = QLabel('Font:')
        label_text_font.setStyleSheet("QLabel { border: none; }")
        label_text_font.setFont(font)
        text_font_layout.addWidget(label_text_font)
        text_font_combo_box = QComboBox()
        text_font_combo_box.addItems(['Font 1', 'Font 2', 'Font 3'])
        text_font_combo_box.setFixedWidth(100)
        text_font_layout.addWidget(text_font_combo_box)

        new_section_layout.addLayout(text_font_layout)

        # Text glow selection
        text_glow_layout = QHBoxLayout()
        text_glow_layout.setSpacing(0)
        label_text_glow = QLabel('Text glow:')
        label_text_glow.setStyleSheet("QLabel { border: none; }")
        label_text_glow.setFont(font)
        text_glow_layout.addWidget(label_text_glow)
        text_glow_slider = SwitchSlider()
        text_glow_slider.setFixedWidth(100)
        text_glow_layout.addWidget(text_glow_slider)

        new_section_layout.addLayout(text_glow_layout)

        # Text glow color selection
        text_glow_color_layout = QHBoxLayout()
        text_glow_color_layout.setSpacing(0)
        label_text_glow_color = QLabel('Text glow colour:')
        label_text_glow_color.setStyleSheet("QLabel { border: none; }")
        label_text_glow_color.setFont(font)
        text_glow_color_layout.addWidget(label_text_glow_color)
        text_glow_color_combo_box = QComboBox()
        text_glow_color_combo_box.addItems(['Color 1', 'Color 2', 'Color 3'])
        text_glow_color_combo_box.setFixedWidth(100)
        text_glow_color_layout.addWidget(text_glow_color_combo_box)

        new_section_layout.addLayout(text_glow_color_layout)

        # Add the new section layout to the main layout
        layout.addLayout(new_section_layout)

        # Save Button
        save_button = QPushButton('Save')
        save_button.setFont(font)  # Apply the font
        save_button.clicked.connect(lambda: self.save_config(profile_combo_box.currentText(),
                                                            combo_box1.currentText(),
                                                            switch_slider.value(),
                                                            filter_combo_box.currentText(),
                                                            animation_combo_box.currentText(),
                                                            hook_slider.value(),
                                                            overlays_combo_box.currentText(),
                                                            cc_filter_combo_box.currentText(),
                                                            auto_generated_combo_box.currentText(),
                                                            text_color_combo_box.currentText(),
                                                            stroke_size_combo_box.currentText(),
                                                            ))

        # Create a vertical spacer to push the save button to the bottom
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # Add the spacer to the layout
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

    def initialize_hashtags(self):
        print("Initializing hashtags...")

    def save_config(self, profile, audio_class, enable_keyframes, selected_filter, selected_animation, enable_hook, selected_overlays, selected_cc_filter):
        config = {
            'audio_class': audio_class,
            'enable_keyframes': enable_keyframes,
            'filter': selected_filter,
            'animation': selected_animation,
            'enable_hook': enable_hook,
            'overlays': selected_overlays,
            'cc_filter': selected_cc_filter
        }
        with open('config.json', 'r') as config_file:
            profiles = json.load(config_file)
            profiles[profile] = config
        with open('config.json', 'w') as config_file:
            json.dump(profiles, config_file, indent=4)
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

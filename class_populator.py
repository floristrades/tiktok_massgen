import sys
import os
import json
import subprocess
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Class populator")
        self.layout = QVBoxLayout()
        self.sections = {}
        self.json_file_path = "./classes.json"

        self.section_labels = [
            "Audio classes", "Keyframes", "Filters", "Animation", "Hook", "Overlays", "CC filter",
            "Auto-generated text", "Text colour", "Stroke size", "Text animation", "Caption",
            "Caption when yes", "Animation in", "Animation when yes", "Text font", "Text outline",
            "Text glow", "Text glow colour"
        ]

        # Add UnknownClass1 to UnknownClass10
        for i in range(1, 30):
            self.section_labels.append(f"UnknownClass{i}")
        self.section_widgets = {}

        self.open_json()  # Open the JSON file

        self.create_section_layouts()
        self.add_class_button()

        self.setLayout(self.layout)

        # Set the window flags to make the window topmost
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.open_json_file()  # Open the JSON file in Notepad

    def open_json(self):
        if os.path.exists(self.json_file_path):
            with open(self.json_file_path, "r") as file:
                existing_data = json.load(file)
                self.sections = existing_data

    def open_json_file(self):
        if sys.platform == 'win32':
            subprocess.Popen(['notepad.exe', self.json_file_path])
        else:
            subprocess.Popen(['open', '-a', 'TextEdit', self.json_file_path])
            
    def create_section_layouts(self):
        grid_layout = QGridLayout()
        num_sections = len(self.section_labels)
        num_rows = (num_sections + 1) // 5  # Determine the number of rows in the grid layout

        for i, section_label in enumerate(self.section_labels):
            section_layout = QVBoxLayout()
            self.sections[section_label] = []
            self.section_widgets[section_label] = section_layout

            section_label_widget = QLabel(section_label)
            section_layout.addWidget(section_label_widget, alignment=Qt.AlignTop)  # Align section header to the top

            class_input_layout = QVBoxLayout()
            section_layout.addLayout(class_input_layout)

            class_input_widget = QLineEdit()
            self.sections[section_label].append(class_input_widget)
            class_input_layout.addWidget(class_input_widget)

            add_class_button = QPushButton("Add to class")
            add_class_button.clicked.connect(lambda checked, label=section_label: self.add_class(label))
            section_layout.addWidget(add_class_button)

            row = i % num_rows  # Determine the row for the current section
            col = i // num_rows  # Determine the column for the current section
            grid_layout.addLayout(section_layout, row, col)

        self.layout.addLayout(grid_layout)

    def add_class(self, section_label):
        section_classes = self.sections[section_label]
        class_input_widget = section_classes[0]

        if class_input_widget.text().strip():
            self.save_json()  # Save the JSON file
            class_input_widget.clear()

    def add_class_button(self):
        class_button = QPushButton("Add class")
        class_button.clicked.connect(self.save_json)
        #self.layout.addWidget(class_button)

    def save_json(self):
        existing_data = {}

        if os.path.exists(self.json_file_path):
            with open(self.json_file_path, "r") as file:
                existing_data = json.load(file)

        data = existing_data.copy()

        for section_label, section_classes in self.sections.items():
            classes = [class_input.text() for class_input in section_classes if class_input.text()]
            if classes:
                if section_label in data:
                    data[section_label].extend(classes)
                else:
                    data[section_label] = classes

        if not os.path.exists("./workerdata"):
            os.makedirs("./workerdata")

        with open(self.json_file_path, "w") as file:
            json.dump(data, file, indent=4)

        print("JSON saved.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

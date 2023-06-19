import cv2
import numpy as np
import pyautogui
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import win32gui
import win32con
import json
import time

time.sleep(2)

# Define button details
buttons = [
    {
        "name": "new_project",
        "image_paths": [r"main\button_reference\new_project.png"],
        "threshold": 0.8
    },
    {
        "name": "settings_main",
        "image_paths": [r"main\button_reference\settings_main.png"],
        "threshold": 0.7
    },
    {
        "name": "home_main",
        "image_paths": [r"main\button_reference\home.png", r"main\button_reference\home_alt.png", r"main\button_reference\home_alt2.png"],
        "threshold": 0.8
    },
    {
        "name": "search_project",
        "image_paths": [r"main\button_reference\search_project.png"],
        "threshold": 0.7
    },
    {
        "name": "maximize_app",
        "image_paths": [r"main\button_reference\maximize.png", r"main\button_reference\maximize_alt.png", r"main\button_reference\maximize_alt2.png"],
        "threshold": 0.7
    },
    # Add more buttons as needed
]

button_project = [
    {
        "name": "adjustment",
        "image_paths": [r"main\button_reference\project_page\adjustment.png"],
        "threshold": 0.8
    },
    {
        "name": "audio",
        "image_paths": [r"main\button_reference\project_page\audio.png"],
        "threshold": 0.8
    },
    {
        "name": "auto_snapping",
        "image_paths": [r"main\button_reference\project_page\auto_snapping.png"],
        "threshold": 0.8
    },
    {
        "name": "effects",
        "image_paths": [r"main\button_reference\project_page\effects.png"],
        "threshold": 0.8
    },
    {
        "name": "export",
        "image_paths": [r"main\button_reference\project_page\export.png"],
        "threshold": 0.8
    },
    {
        "name": "filters",
        "image_paths": [r"main\button_reference\project_page\filters.png"],
        "threshold": 0.8
    },
    {
        "name": "import_left",
        "image_paths": [r"main\button_reference\project_page\import_left.png"],
        "threshold": 0.8
    },
    {
        "name": "import",
        "image_paths": [r"main\button_reference\project_page\import.png"],
        "threshold": 0.8
    },
    {
        "name": "layout",
        "image_paths": [r"main\button_reference\project_page\layout.png"],
        "threshold": 0.8
    },
    {
        "name": "library",
        "image_paths": [r"main\button_reference\project_page\library.png"],
        "threshold": 0.8
    },
    {
        "name": "linkage",
        "image_paths": [r"main\button_reference\project_page\linkage.png"],
        "threshold": 0.8
    },
    {
        "name": "media",
        "image_paths": [r"main\button_reference\project_page\media.png"],
        "threshold": 0.8
    },
    {
        "name": "menu",
        "image_paths": [r"main\button_reference\project_page\menu.png"],
        "threshold": 0.8
    },
    {
        "name": "modify",
        "image_paths": [r"main\button_reference\project_page\modify.png"],
        "threshold": 0.8
    },
    {
        "name": "preview_axis",
        "image_paths": [r"main\button_reference\project_page\preview_axis.png"],
        "threshold": 0.8
    },
    {
        "name": "select_mode",
        "image_paths": [r"main\button_reference\project_page\select_mode.png"],
        "threshold": 0.8
    },
    {
        "name": "shortcut",
        "image_paths": [r"main\button_reference\project_page\shortcut.png"],
        "threshold": 0.8
    },
    {
        "name": "stickers",
        "image_paths": [r"main\button_reference\project_page\stickers.png"],
        "threshold": 0.8
    },
    {
        "name": "text",
        "image_paths": [r"main\button_reference\project_page\text.png"],
        "threshold": 0.8
    },
    {
        "name": "track_magnet",
        "image_paths": [r"main\button_reference\project_page\track_magnet.png"],
        "threshold": 0.8
    },
    {
        "name": "transition",
        "image_paths": [r"main\button_reference\project_page\transition.png"],
        "threshold": 0.8
    },
    # Add more buttons as needed
]

# Create a Tkinter window
window = tk.Tk()
window.title("Button Health Check")
window.geometry("400x300")
window.attributes("-topmost", True)  # Set window as topmost

# Create a ScrolledText widget to display the console log
log_text = ScrolledText(window, height=10, width=40, font=("Courier New", 8))
log_text.pack(padx=10, pady=10)

import json
import numpy as np

def check_button_presence(button):
    image_paths = button["image_paths"]
    threshold = button["threshold"]
    
    # Iterate over image paths
    for image_path in image_paths:
        reference_button_image = cv2.imread(image_path, 0)
    
        # Capture a screenshot
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
    
        # Perform template matching
        result = cv2.matchTemplate(screenshot, reference_button_image, cv2.TM_CCOEFF_NORMED)
        locations = np.where(result >= threshold)
    
        coordinates = []
    
        if len(locations[0]) > 0:
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            w, h = reference_button_image.shape[::-1]
        
            for pt in zip(*locations[::-1]):
                x = int(pt[0] + w // 2)  # Convert to Python int
                y = int(pt[1] + h // 2)  # Convert to Python int
                coordinates.append((x, y))
                break  # Exit the loop if button is found
    
        # Load existing data from the JSON file
        output_filename = "coordinates.json"
        existing_data = {}
        try:
            with open(output_filename, "r") as f:
                existing_data = json.load(f)
        except FileNotFoundError:
            pass
    
        # Update coordinates under the button name
        button_name = button["name"]
        existing_data[button_name] = coordinates[0] if coordinates else None
    
        # Save coordinates to the JSON file
        with open(output_filename, "w") as f:
            json.dump(existing_data, f)
    
        if coordinates:
            return coordinates[0]
    
    return None

def check_button_presence_project(button):
    image_paths = button["image_paths"]
    threshold = button["threshold"]

    # Iterate over image paths
    for image_path in image_paths:
        reference_button_image = cv2.imread(image_path, 0)

        # Capture a screenshot
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

        # Perform template matching
        result = cv2.matchTemplate(screenshot, reference_button_image, cv2.TM_CCOEFF_NORMED)
        locations = np.where(result >= threshold)

        coordinates = []

        if len(locations[0]) > 0:
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            w, h = reference_button_image.shape[::-1]

            for pt in zip(*locations[::-1]):
                x = int(pt[0] + w // 2)  # Convert to Python int
                y = int(pt[1] + h // 2)  # Convert to Python int
                coordinates.append((x, y))
                break  # Exit the loop if button is found

        # Load existing data from the JSON file
        output_filename = "coordinates.json"
        existing_data = {}
        try:
            with open(output_filename, "r") as f:
                existing_data = json.load(f)
        except FileNotFoundError:
            pass

        # Update coordinates under the button name
        button_name = button["name"]
        existing_data[button_name] = coordinates[0] if coordinates else None

        # Save coordinates to the JSON file
        with open(output_filename, "w") as f:
            json.dump(existing_data, f)

        if coordinates:
            return coordinates[0]

    return None


# Function to focus CapCut.exe windows
def focus_capcut_windows():
    capcut_windows = []
    
    def enum_handler(hwnd, _):
        if win32gui.GetWindowText(hwnd) == "CapCut":
            capcut_windows.append(hwnd)
    
    win32gui.EnumWindows(enum_handler, None)
    for hwnd in capcut_windows:
        win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
        win32gui.SetForegroundWindow(hwnd)

# Function to update the console log and summary
def update_log():
    total_buttons = len(buttons) + len(button_project)
    passed_count = 0
    
    log_text.delete("1.0", tk.END)  # Clear previous log
    
    # Focus CapCut.exe windows
    focus_capcut_windows()
    
    for button in buttons:
        button_name = button["name"]
        button_present = check_button_presence(button)
        
        if button_present:
            log_text.insert(tk.END, f"Button {button_name} has been found! Passed health check!\n")
            passed_count += 1
        else:
            log_text.insert(tk.END, f"Button {button_name} has not been found.\n")
    
    # After click_coordinates() has been executed, check buttons in button_project
    click_coordinates()
    
    for button in button_project:
        button_name = button["name"]
        button_present = check_button_presence_project(button)
        
        if button_present:
            log_text.insert(tk.END, f"Button {button_name} has been found! Passed health check!\n")
            passed_count += 1
        else:
            log_text.insert(tk.END, f"Button {button_name} has not been found.\n")
    
    # Update summary
    summary_text = f"Passed: {passed_count}/{total_buttons} ({(passed_count/total_buttons)*100:.2f}% Health)\n"
    log_text.insert(tk.END, summary_text)
    log_text.see(tk.END)  # Scroll to the end of the log
        
    # Calculate health percentage
    health_percentage = (passed_count / total_buttons) * 100

    # If health is 100%, click coordinates
    if health_percentage == 100:
        click_coordinates()

def click_coordinates():
    time.sleep(2)
    # Load coordinates from JSON file
    with open('coordinates.json') as file:
        coordinates = json.load(file)

    # Click the 'new_project' coordinates
    new_project_coords = coordinates.get('new_project')
    if new_project_coords:
        x, y = new_project_coords
        pyautogui.click(x, y, button='left')
        log_text.insert(tk.END, f"Init new_project at ({x}, {y})\n")
    else:
        log_text.insert(tk.END, "Coordinates for 'new_project' not found in JSON.\n")

    # Click the 'maximize_app' coordinates 1 second later
    maximize_app_coords = coordinates.get('maximize_app')
    if maximize_app_coords:
        x, y = maximize_app_coords
        time.sleep(1)
        pyautogui.click(x, y, button='left')
        log_text.insert(tk.END, f"Clicked maximize app at ({x}, {y})\n")
    else:
        log_text.insert(tk.END, "Coordinates for 'maximize_app' not found in JSON.\n")


# Call the update_log() function to start straight away
update_log()

# Create a button to trigger the check
check_button = tk.Button(window, text="Check", font=("Arial", 12), command=update_log)
check_button.pack()

# Start the Tkinter event loop
window.mainloop()

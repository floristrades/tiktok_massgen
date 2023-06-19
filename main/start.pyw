import tkinter as tk
import psutil
import time
import subprocess

def get_running_capcut_processes():
    processes = []

    for process in psutil.process_iter(['pid', 'name']):
        if 'capcut' in process.info['name'].lower():
            processes.append(process.info['name'])
    return processes

# Function to open the executable from the specified file path
def open_executable(filepath):
    try:
        subprocess.Popen(filepath)
    except Exception as e:
        print("Failed to open executable:", str(e))

# Create a Tkinter window
window = tk.Tk()
window.title("Private build capcut editor")
window.geometry("400x300+800+0")  # Set the window size and position

# Create a text widget to display the output
output_text = tk.Text(window, height=10, width=40)
output_text.pack(side=tk.RIGHT, padx=10, pady=10)


def update_output():
    output_text.delete("1.0", tk.END)  # Clear previous output
    running_capcut_processes = get_running_capcut_processes()
    if len(running_capcut_processes) > 0:
        output_text.insert(tk.END, "Listening for processes...\n")
        output_text.insert(tk.END, "Found running CapCut processes:\n")
        output_text.insert(tk.END, "Initializing health check...\n")
        time.sleep(1)
        subprocess.Popen(['python', "main/health_check.pyw"])
        
        for name in running_capcut_processes:
            output_text.insert(tk.END, f"Name: {name}\n")
        window.destroy()
            
    else:
        try:
            output_text.insert(tk.END, "No running CapCut processes found!\n")
            time.sleep(0.5)
            with open('./filepaths.txt', 'r') as file:
                filepath = file.read().strip()
                if filepath:
                    output_text.insert(tk.END, "Manually launching CapCut...\n")
                    output_text.insert(tk.END, "Initializing health check...\n")
                    open_executable(filepath)
                    time.sleep(1)
                    subprocess.Popen(['python', "main/health_check.pyw"])
                    window.destroy()
                else:
                    output_text.insert(tk.END, "No file path specified in filepaths.txt.\n")
                    output_text.insert(tk.END, "Launching health_check.pyw...\n")
                    window.destroy()  # Close the current window
        
        except FileNotFoundError:
            output_text.insert(tk.END, f"filepaths.txt not found. EXPECTED PATH: {filepath}\nWhen filepaths are not found please add them manually.\n")
        
        # Launch health_check.py outside the loop
        #subprocess.Popen(['python', "main/health_check.pyw"])


# Create a button to update the output
update_button = tk.Button(window, text="Update", command=update_output)
update_button.pack(side=tk.BOTTOM, pady=10)

# Call the update_output function to initially display the output
update_output()
window.mainloop()

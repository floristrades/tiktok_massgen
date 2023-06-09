import os
import sqlite3

def create_database(database_file):
    conn = sqlite3.connect(database_file)
    c = conn.cursor()

    # Create a table to store filenames and classes
    c.execute('''CREATE TABLE IF NOT EXISTS files
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 filename TEXT,
                 audio_class TEXT)''')

    conn.commit()
    conn.close()

def log_filename(database_file, filename):
    conn = sqlite3.connect(database_file)
    c = conn.cursor()

    # Insert the filename and class as "undefined" into the database
    c.execute("INSERT INTO files (filename, audio_class) VALUES (?, ?)", (filename, "undefined"))

    conn.commit()
    conn.close()

def convert_filenames(directory, database_file):
    # Get the list of files in the directory
    files = os.listdir(directory)
    mp3_files = [file for file in files if file.endswith(".mp3")]

    # Calculate the total number of MP3 files
    total_files = len(mp3_files)

    # Create the database if it doesn't exist
    if not os.path.exists(database_file):
        open(database_file, 'w').close()  # Create an empty file

    create_database(database_file)

    # Iterate over the MP3 files and rename them
    for i, filename in enumerate(mp3_files):
        # Remove the file extension
        name, extension = os.path.splitext(filename)

        # Convert the name to lowercase
        name = name.lower()

        # Generate the new filename
        new_filename = f"{i+1}_{name}{extension}"

        # Rename the file
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

        # Log the filename in the database
        log_filename(database_file, new_filename)

    print(f"Converted {len(mp3_files)} filenames in directory: {directory}")

# Provide the directory path here
directory_path = "sound_library"

# Provide the database file path here
database_file_path = "databases/database.db"

convert_filenames(directory_path, database_file_path)

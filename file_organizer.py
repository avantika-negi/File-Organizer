import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize_files(directory):
    if not directory:
        messagebox.showerror("Error", "Please select a directory first.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Determine folder based on file extension
        file_extension = filename.split('.')[-1]
        folder_name = get_folder_name(file_extension)

        # Create folder if it does not exist
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Move file to the folder
        shutil.move(file_path, os.path.join(folder_path, filename))
    
    messagebox.showinfo("Success", "Files organized successfully.")

def get_folder_name(extension):
    folders = {
        'jpg': 'Images',
        'png': 'Images',
        'mp3': 'Music',
        'pdf': 'Documents',
        'py': 'Scripts',
        'txt': 'TextFiles',
    }
    return folders.get(extension, 'Others')

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_entry.delete(0, tk.END)  # Clear any existing text
        directory_entry.insert(0, directory)  # Insert new directory path

def start_organizing():
    directory = directory_entry.get()
    organize_files(directory)

# GUI setup
root = tk.Tk()
root.title("File Organizer")
root.geometry("400x200")

# Directory selection
directory_label = tk.Label(root, text="Select Directory:")
directory_label.pack(pady=10)

directory_entry = tk.Entry(root, width=50)
directory_entry.pack()

browse_button = tk.Button(root, text="Browse", command=select_directory)
browse_button.pack(pady=5)

# Organize button
organize_button = tk.Button(root, text="Organize Files", command=start_organizing)
organize_button.pack(pady=20)

# Start GUI loop
root.mainloop()
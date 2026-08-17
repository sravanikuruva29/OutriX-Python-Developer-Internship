"""
OutriX Python Developer Internship - Task 3
File Organizer Tool
Tools: Python, os, shutil

Run:
    python task3_file_organizer.py

The program asks for a directory and organizes files into:
    Images, Documents, PDFs, Videos, Audio, Archives, Others

Files already inside category folders are ignored.
"""

import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"},
    "Documents": {".doc", ".docx", ".txt", ".rtf", ".odt"},
    "PDFs": {".pdf"},
    "Videos": {".mp4", ".avi", ".mkv", ".mov", ".wmv", ".webm"},
    "Audio": {".mp3", ".wav", ".aac", ".flac", ".ogg"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Spreadsheets": {".xls", ".xlsx", ".csv"},
    "Presentations": {".ppt", ".pptx"},
}


def get_category(extension):
    extension = extension.lower()

    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def unique_destination(folder, filename):
    """Avoid overwriting an existing file."""
    destination = os.path.join(folder, filename)

    if not os.path.exists(destination):
        return destination

    name, extension = os.path.splitext(filename)
    counter = 1

    while True:
        new_name = f"{name}_{counter}{extension}"
        destination = os.path.join(folder, new_name)

        if not os.path.exists(destination):
            return destination

        counter += 1


def organize_folder(directory):
    moved_count = 0

    for filename in os.listdir(directory):
        source = os.path.join(directory, filename)

        # Ignore directories.
        if not os.path.isfile(source):
            continue

        extension = os.path.splitext(filename)[1]
        category = get_category(extension)

        target_folder = os.path.join(directory, category)
        os.makedirs(target_folder, exist_ok=True)

        destination = unique_destination(target_folder, filename)
        shutil.move(source, destination)
        moved_count += 1

    return moved_count


def choose_folder():
    directory = filedialog.askdirectory(title="Select Folder to Organize")

    if not directory:
        return

    try:
        count = organize_folder(directory)

        messagebox.showinfo(
            "Completed",
            f"Organization completed successfully.\n\n"
            f"Files organized: {count}"
        )

    except PermissionError:
        messagebox.showerror(
            "Permission Error",
            "Permission denied. Try selecting another folder."
        )
    except OSError as error:
        messagebox.showerror("Error", str(error))


root = tk.Tk()
root.title("OutriX - File Organizer")
root.geometry("500x300")
root.resizable(False, False)

tk.Label(
    root,
    text="File Organizer Tool",
    font=("Arial", 20, "bold")
).pack(pady=25)

tk.Label(
    root,
    text="Select a folder and automatically organize files\n"
         "into folders based on their file type.",
    font=("Arial", 11),
    justify="center"
).pack(pady=10)

tk.Button(
    root,
    text="Choose Folder & Organize",
    font=("Arial", 12, "bold"),
    width=25,
    height=2,
    command=choose_folder
).pack(pady=25)

tk.Label(
    root,
    text="Images | Documents | PDFs | Videos | Audio | Archives | Others",
    font=("Arial", 9)
).pack(pady=5)

root.mainloop()

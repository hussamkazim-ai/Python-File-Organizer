import os
import shutil


# Specifying extensions and folder names
extensions = {
    ".jpeg": "Images",
    ".png": "Images",
    ".mp4": "Videos",
    ".json": "Documents",
    ".txt": "Documents",
    ".html": "Documents",
    ".deb": "Apps",
    ".exe": "Apps",
}

# Storing all the file names in files variable
files = os.listdir() 

# Looping through all the files and moving them to the folders
for file in files:
    root, ext = os.path.splitext(file)
    for extension in extensions:
        if ext == extension:
            folder = extensions[extension]
            destination = os.path.join(folder, file)
            if not os.path.exists(folder):
                os.makedirs(folder)
            shutil.move(file, destination)
            
            

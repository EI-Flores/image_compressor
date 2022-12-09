from PIL import Image
import os, sys

# Don't forget change your user 
downloadsFolders = "C:\\Users\\ingfl\\Downloads\\"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolders):
        name, extension = os.path.splitext(downloadsFolders + filename)

        # Check if we are working with a image
        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolders + filename)
            # values of quality are optional 
            picture.save(downloadsFolders + "Compressed_"+ filename, optimize=True, quality=60)
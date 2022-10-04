# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib

# Find the path to my Desktop

# Create a new folder

# Filter for screenshots only

# Create a new path for each file

# Move the screenshot there

import glob
import shutil

og = 'macintosh HD/Users/tylervila/Desktop/Testing/starting point'

ng = 'Macintosh HD/Users/tylervila/Desktop/Testing/ending point'

for f in glob.glob('/Users/tylervila/Desktop/Testing/starting point/*.jpg'):
    shutil.move(f,'/Users/tylervila/Desktop/Testing/ending point')



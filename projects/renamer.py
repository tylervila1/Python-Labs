# Move and rename all .png files on your Desktop

# Identify all screenshots on your Desktop

# Create a new directory

# Move and rename all screenshots





import glob
import shutil

og = 'macintosh HD/Users/tylervila/Desktop'

ng = 'Macintosh HD/Users/tylervila/Desktop/Testing/ending point'

for f in glob.glob('/Users/tylervila/Desktop/*.mov'):
    shutil.move(f,'/Users/tylervila/Desktop/screenshot')


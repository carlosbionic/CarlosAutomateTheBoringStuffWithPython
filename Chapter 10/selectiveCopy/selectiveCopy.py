#! python3
# selectiveCopy.py - walks through a folder and copies 
# pdf or jpg files to a new folder.

import shutil, os
from pathlib import Path

cwd = Path.cwd()
folder = cwd / 'folderTreeTest' # Make folder absolute

for foldername, subfolders, filenames in os.walk(folder):
	for filename in filenames:
		if filename.endswith('.jpg'):
			print()
			print(Path(foldername) / filename, 'to', cwd / 'newFolder')
			shutil.copy(Path(foldername) / filename, cwd / 'newFolder')

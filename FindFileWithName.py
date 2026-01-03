import os
import subprocess
# Specify the directory path
name = input('sheiyvane failis saxeli: ')
directory_path = 'C:/Users/pc/Desktop'

# Get a list of files in the directory
file_names = os.listdir(directory_path)

# Filter out directories, if needed
files = [file for file in file_names if os.path.isfile(os.path.join(directory_path, file))]

file_name_list = []
# Print the file names
for file in files:
    file_name_list.append(file)

if name in file_name_list:
    print(directory_path, name)
else:
    print("can't find file")

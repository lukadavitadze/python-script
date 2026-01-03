import os
# Specify the folder path  
folder_path = '/home/'

# Get a list of files in the folder
files = os.listdir(folder_path)

# Filter out directories, if you only want files
files = [file for file in files if os.path.isfile(os.path.join(folder_path, file))]

# Output the list of files
file_list = []
for file in files:
    file_list.append(file)
#print(file_list)
for i in file_list:
    with open(f'{i}','r') as f:    
        readFile = f.read()
        # SOS xazebi ar auriot 
        # pirvel listshi unknown shecvla / anu pirvleli unknown
        readFile = readFile.replace('####','####') 
        # meore listshi pirvlei 
        readFile = readFile.replace('####','####')
        # mesame listshi meore
        readFile = readFile.replace('####','####') 
    with open(f'{i}','w') as file:
        file.write(readFile)

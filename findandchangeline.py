import os
# Specify the folder path /home/sysop/Documents/luka_temp/shtl  / C:/Users/xuligan/Desktop/python sc/shtl
folder_path = '/home/sysop/Documents/luka_temp/mzeg'

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
        readFile = readFile.replace('-Unknown-                                                   MARKER NAME','MZEG                                                        MARKER NAME\nMzetamze                                                    MARKER NUMBER') 
        # meore listshi pirvlei 
        readFile = readFile.replace('-Unknown-           -Unknown-                               OBSERVER / AGENCY','IES and NSMC        Ilia State University                   OBSERVER / AGENCY')
        # mesame listshi meore
        readFile = readFile.replace('-Unknown-           -Unknown-                               ANT # / TYPE','762-12439           TPSCR.G5            TPSH                ANT # / TYPE') 
    with open(f'{i}','w') as file:
        file.write(readFile)
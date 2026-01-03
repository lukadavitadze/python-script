import os

def find_folders_by_name(folder_name, search_path='C:\\'):
    matched_folders = []
    
    # Walk through all directories and subdirectories
    for dirpath, dirnames, filenames in os.walk(search_path):
        if folder_name in dirnames:
            matched_folders.append(os.path.join(dirpath, folder_name))
    
    return matched_folders

# Ask for the folder name
folder_name = input("Enter the name of the folder you're looking for: ")

# Ask for the path to start the search (default is C:\\ drive)
search_path = input("Enter the path to start the search (or press Enter to search from C:\\): ")
if not search_path:
    search_path = 'C:\\'  # Default to C:\\ if no input is provided

# Find all folders with the given name
folders = find_folders_by_name(folder_name, search_path)

# Output the results
if folders:
    print(f"Found {len(folders)} folder(s) with the name '{folder_name}':")
    for folder in folders:
        print(folder)
else:
    print(f"No folders found with the name '{folder_name}'.")

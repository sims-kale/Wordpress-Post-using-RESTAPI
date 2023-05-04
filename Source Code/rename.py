import logging
import os
import re

logging.basicConfig(filename='Source Code/rename.log', level=logging.INFO)

folder_path ="D:/Downloads/Images/Images"
new_folder_path = "D:/Downloads/New Folder"
if not os.path.exists(new_folder_path):
    os.mkdir(new_folder_path)

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    
    if filename.endswith(".jpg"):
        logging.info("Filename: " +filename)
        print(filename)
        # Split the filename into its name and extension
        name, extension = os.path.splitext(filename)

        new_name = name.replace("by", '').replace("in", '')
        rename= new_name.replace(" ", "-").replace("--","-")+ extension
        print(rename)
        logging.info("Rename File: "+ rename)
        pattern = r"\d+\.\w+$"
        match = re.search(pattern, filename)

    # if match:
    #     # Extract the number from the matched pattern
    #     number = match.group(0).split('.')[0]
    #     # Create the new filename with the extracted number
    #     new_filename = f"{new_name}{number}{extension}"
    #     logging.info("Rename: " + new_filename)
            
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(new_folder_path, filename)
            
        os.rename(old_path, new_path)

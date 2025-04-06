# ACCESS ALL THE FILES IN THE DIRECTORY 
# CREATE FOLDERS FOR EACH FILE TYPE
# CREATE A FUNCTION THAT TAKES A FILE AS INPUT
# CHECKS THE FILE TYPE
# MOVES THE FILE TO THE FOLDER CREATED FOR THAT TYPE

import os
import json

def read_config(file):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Configuration file {file} not found! Using default settings.")
        return {}

def create_folders(directory):
    for dir in directory:
        try:
            os.mkdir(dir)
            print(f"{dir:30} created ")
        except OSError:
            print(f'{dir:20} Already Exists')


def get_folder(ext,directory):
    for folder,extensions in directory.items():
        if ext in extensions:
            return folder
    return 'Other'

def main(directory):
    for filename in os.listdir():
        if filename != __file__ and filename[0] != '.' and '.' in filename:
            ext = os.path.basename(filename).split('.')[-1]
            folder = get_folder(ext,directory)
            if not os.path.isfile(os.path.join(folder,filename)):
                os.rename(filename,os.path.join(folder,filename))
                print(f"Moved {filename} to {folder}")
                

if __name__=="__main__":
    file="types.json"
    config=read_config(file)
    create_folders(config)
    main(config)
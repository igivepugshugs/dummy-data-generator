'''
app.py

This program will ask the user to input the desired size of the fake data and then the program will create it.
'''
import os
import random
from faker import Faker

def generate_files_in_folder(target_size_mb, folder_path):
    '''
    inputs the desired folder size and the path to create the data.
    '''
    fake = Faker()
    os.makedirs(folder_path, exist_ok=True)
    
    target_size_bytes = target_size_mb * 1024 * 1024
    current_size = 0
    
    # do until the current size is the same size as the target size
    while current_size < target_size_bytes:
        file_name = f"{fake.file_name()}"
        file_path = os.path.join(folder_path, file_name)
        file_size = random.randint(1, 1024 * 1024)  # Random file size between 1 byte and 1MB
        
        if current_size + file_size > target_size_bytes:
            file_size = target_size_bytes - current_size  # Adjust to not exceed target size
        
        with open(file_path, 'wb') as f:
            f.write(os.urandom(file_size))
        
        current_size += file_size

    current_directory = os.getcwd()
    print(f"Folder '{current_directory + '/' + folder_path}' created with total size: {current_size / (1024 * 1024)} MB.\n")

# This is where the program starts and asks the user for the desired size of data.
target_size_bytes = int(input("\nEnter desired fake data folder size in MB. NUMBER ONLY: "))

generate_files_in_folder(target_size_bytes, "fake_data")  # Creates a folder with approximately 10MB of random files


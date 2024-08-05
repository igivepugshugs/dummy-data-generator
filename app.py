import os
from faker import Faker

# Initialize Faker instance
fake = Faker()

# Define the root directory where folders and files will be created
root_dir = "fake_data"

# Create the root directory if it doesn't exist
os.makedirs(root_dir, exist_ok=True)


# Number of folders and files to create
num_folders = 7
files_per_folder = 10

# Function to generate fake data and write to a file
def generate_fake_file_data(file_path):
    with open(file_path, 'w') as file:
        for _ in range(10):  # Number of lines of fake data per file
            name = fake.name()
            address = fake.address().replace("\n", ", ")
            email = fake.email()
            phone = fake.phone_number()
            file.write(f"Name: {name}\n")
            file.write(f"Address: {address}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Phone: {phone}\n")
            file.write("-" * 40 + "\n")

# Create folders and files with dummy data
for i in range(1, num_folders + 1):
    folder_name = f"folder_{i}"
    folder_path = os.path.join(root_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    for j in range(1, files_per_folder + 1):
        file_name = f"file_{j}.txt"
        file_path = os.path.join(folder_path, file_name)
        generate_fake_file_data(file_path)

print(f"Created {num_folders} folders with {files_per_folder} files each in '{root_dir}' directory.")

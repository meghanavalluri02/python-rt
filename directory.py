import os

directory = "my_data_folder"
file_path = os.path.join(directory, "notes.txt")

try:
    os.makedirs(directory, exist_ok=True)

    with open(file_path, 'w') as file:
        file.write('Important notes')

    print('File written successfully.')

except IOError as e:
    print(f"An error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

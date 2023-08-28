import re
import os


def open_folder(folder_path):
    # List all files in the folder
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths
    print('Folder has {} files.'.format(len(file_paths)))

def clean_text(input_file_path):
    # Open the file in read mode
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    print("Original text: ", text)
    print("\n")

    # Remove section headings
    cleaned_text = re.sub(r'===(.*?)===', '', text)
    cleaned_text = re.sub(r'==(.*?)==', '', cleaned_text)

    # Remove remaining markup and formatting
    cleaned_text = re.sub(r"''+|'''", '', cleaned_text)
    cleaned_text = re.sub(r'\[.*?\]', '', cleaned_text)

    # Remove excessive newlines and spaces
    cleaned_text = re.sub(r'\n+', '\n', cleaned_text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    print("Cleaned text:", cleaned_text)
    print("\n\n\n")

    # # Write cleaned content to the output file
    # with open(output_file_path, 'w', encoding='utf-8') as output_file:
    #     output_file.write(cleaned_text)

    # print("Manipulated content saved to {}".format(output_file_path))


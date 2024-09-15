#github_url: https://github.com/Bipuojha1/softwarenow_assignment2.git


import pandas as pd
import os

# Base directory path for the files
base_path = r'D:\CDU\SEM-2\Software Now\Assignment 2\Question1'

# List of CSV file names and their respective text columns
csv_files = [
    ('CSV1.csv', 'SHORT-TEXT'), 
    ('CSV2.csv', 'TEXT'), 
    ('CSV3.csv', 'TEXT'), 
    ('CSV4.csv', 'TEXT')
]

# List to store text information from all files
all_texts = []

# Read each CSV file and extract text information
for (file, text_column) in csv_files:
    file_path = os.path.join(base_path, file)  # Full path to the CSV file
    try:
        # Read CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Check if the specified text column exists in the DataFrame
        if text_column in df.columns:
            # Extract text information and append to the list
            all_texts.extend(df[text_column].astype(str).tolist())
        else:
            print(f"Column '{text_column}' not found in {file}. Skipping this file.")

    except FileNotFoundError:
        print(f"File '{file_path}' not found. Please check the file path.")

# Define output directory and ensure it exists
output_dir = r'D:\CDU\SEM-2\Software Now\Assignment 2\Question1\task1'
os.makedirs(output_dir, exist_ok=True)

# Write text information to a new text file in the specified output directory
output_file = os.path.join(output_dir, 'singlefile.txt')
with open(output_file, 'w', encoding='utf-8') as f:
    for text in all_texts:
        f.write(text + '\n')

print(f'Text information written to {output_file}.')

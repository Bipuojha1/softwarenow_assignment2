#github_url: https://github.com/Bipuojha1/softwarenow_assignment2.git

import csv
from collections import Counter
from transformers import AutoTokenizer

def count_unique_tokens(input_file, output_csv, model_name='bert-base-uncased', chunk_size=1024*1024):
    """
    Count unique tokens in the text file and save the top 30 tokens to a CSV file.
    
    :param input_file: Path to the input .txt file containing the text.
    :param output_csv: Path to the output CSV file to save the top 30 tokens.
    :param model_name: Pretrained model name to load the tokenizer.
    :param chunk_size: Size of the text chunks to read at once (in bytes).
    """
    # Load the pretrained tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Initialize Counter to count token occurrences
    token_counts = Counter()

    # Read and process the text file in chunks
    with open(input_file, 'r', encoding='utf-8') as file:
        while True:
            # Read a chunk of the file
            chunk = file.read(chunk_size)
            if not chunk:
                break

            # Tokenize the text chunk
            tokens = tokenizer(chunk, truncation=True, padding=False, return_tensors='pt')
            # Flatten the tokens tensor to list
            tokens_list = tokenizer.convert_ids_to_tokens(tokens['input_ids'].flatten())
            # Update token counts
            token_counts.update(tokens_list)

    # Get the top 30 most common tokens
    top_30_tokens = token_counts.most_common(30)

    # Write the results to a CSV file
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Token', 'Count'])  # Write header
        csv_writer.writerows(top_30_tokens)

    print(f"Top 30 tokens and their counts have been saved to {output_csv}")

# Define file paths
input_file = r"D:\CDU\SEM-2\Software Now\Assignment 2\Question1\singlefile.txt"
output_csv = r"D:\CDU\SEM-2\Software Now\Assignment 2\Question1\task3\top_30_tokens.csv"

# Call the function
count_unique_tokens(input_file, output_csv)

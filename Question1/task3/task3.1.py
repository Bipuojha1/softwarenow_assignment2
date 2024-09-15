import csv
from collections import Counter
import re

# Define the file paths
input_file = r"D:\CDU\SEM-2\Software Now\Assignment 2\Question1\singlefile.txt"
output_csv = r"D:\CDU\SEM-2\Software Now\Assignment 2\Question1\task3\top_30_commonwords.csv"

# Step 1: Read the text from the .txt file
with open(input_file, 'r', encoding='utf-8') as file:
    text = file.read()

# Step 2: Use regular expressions to find all words
words = re.findall(r'\b\w+\b', text.lower())  # Extract words and convert to lowercase

# Step 3: Count the occurrences of each word using Counter
word_counts = Counter(words)

# Step 4: Get the Top 30 most common words
top_30_words = word_counts.most_common(30)

# Step 5: Write the results to a CSV file
with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Word', 'Count'])  # Write header
    csv_writer.writerows(top_30_words)

print(f"Top 30 words and their counts have been saved to {output_csv}")

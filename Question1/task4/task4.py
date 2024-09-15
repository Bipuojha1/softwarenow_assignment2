import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from collections import Counter
import csv

# Load the SciSpacy model
def load_scipy_model(model_name='en_core_sci_sm'):
    """
    Load the SciSpacy model for NER.
    """
    nlp = spacy.load(model_name)
    return nlp

def extract_entities_spacy(text_file_path, nlp_model, chunk_size=1000):
    """
    Extract named entities from the text file using SciSpacy.
    """
    entities = {'Disease': [], 'Drug': []}
    with open(text_file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            doc = nlp_model(chunk)
            for ent in doc.ents:
                if ent.label_ in ['Disease', 'Drug']:
                    entities[ent.label_].append(ent.text)
    return entities

# Load the BioBERT model with a suitable NER head
def load_biobert_model():
    """
    Load the BioBERT model for NER.
    """
    tokenizer = AutoTokenizer.from_pretrained('dmis-lab/biobert-v1.1')
    model = AutoModelForTokenClassification.from_pretrained('dmis-lab/biobert-v1.1')
    nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy='simple')
    return nlp

def extract_entities_biobert(text_file_path, biobert_nlp, chunk_size=1000):
    """
    Extract named entities from the text file using BioBERT.
    """
    entities = {'Disease': [], 'Drug': []}
    with open(text_file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            ner_results = biobert_nlp(chunk)
            for result in ner_results:
                if result['entity'] in ['Disease', 'Drug']:
                    entities[result['entity']].append(result['word'])
    return entities

# Function to count unique tokens and save to CSV
def count_and_save_top_tokens(text_file, output_csv, model_name='bert-base-uncased', chunk_size=1024*1024):
    """
    Count unique tokens in the text file and save the top 30 tokens to a CSV file.
    
    :param text_file: Path to the input .txt file.
    :param output_csv: Path to the output CSV file.
    :param model_name: Pretrained model name to load the tokenizer.
    :param chunk_size: Size of the text chunks to read at once (in bytes).
    """
    from transformers import AutoTokenizer
    from collections import Counter

    # Load the pretrained tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Initialize Counter to count token occurrences
    token_counts = Counter()

    # Read and process the text file in chunks
    with open(text_file, 'r', encoding='utf-8') as file:
        while True:
            # Read a chunk of the file
            chunk = file.read(chunk_size)
            if not chunk:
                break

            # Tokenize the text chunk
            tokens = tokenizer(chunk, truncation=True, padding=False, return_tensors='pt', clean_up_tokenization_spaces=False)
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

def compare_entities(entities1, entities2):
    """
    Compare the entities detected by SciSpacy and BioBERT.
    """
    comparison = {}
    for entity_type in ['Disease', 'Drug']:
        count1 = len(entities1[entity_type])
        count2 = len(entities2[entity_type])
        comparison[entity_type] = {
            'SciSpacy Count': count1,
            'BioBERT Count': count2,
            'Difference': count1 - count2,
            'Most Common SciSpacy': Counter(entities1[entity_type]).most_common(5),
            'Most Common BioBERT': Counter(entities2[entity_type]).most_common(5),
        }
    return comparison

def main(input_file):
    # Load models
    spacy_model = load_scipy_model('en_core_sci_sm')
    biobert_nlp = load_biobert_model()

    # Extract entities using SciSpacy
    entities_spacy = extract_entities_spacy(input_file, spacy_model)
    # Extract entities using BioBERT
    entities_biobert = extract_entities_biobert(input_file, biobert_nlp)

    # Output CSV file path for tokens
    output_csv = r"D:\CDU\SEM-2\Software Now\Assignment 2\Question1\task3\top_30_tokens.csv"
    
    # Count and save top tokens
    count_and_save_top_tokens(input_file, output_csv)

    # Compare results
    comparison = compare_entities(entities_spacy, entities_biobert)
    
    print("Comparison of entities detected by SciSpacy and BioBERT:")
    for entity_type, data in comparison.items():
        print(f"\n{entity_type} entities:")
        print(f"SciSpacy Count: {data['SciSpacy Count']}")
        print(f"BioBERT Count: {data['BioBERT Count']}")
        print(f"Difference: {data['Difference']}")
        print(f"Most Common SciSpacy: {data['Most Common SciSpacy']}")
        print(f"Most Common BioBERT: {data['Most Common BioBERT']}")

if __name__ == "__main__":
    input_file = r"D:\CDU\SEM-2\Software Now\Assignment 2\Question1\singlefile.txt"
    main(input_file)

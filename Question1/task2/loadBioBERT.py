#github_url: https://github.com/Bipuojha1/softwarenow_assignment2.git


from transformers import AutoTokenizer, AutoModelForTokenClassification

# Load the BioBERT model
tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-v1.1")
model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-v1.1")

print("BioBERT model loaded successfully.")

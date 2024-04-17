import spacy
import re

# python -m spacy download en_core_web_sm
# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

def extract_info(text):
    # Create a Document object
    doc = nlp(text)

    # Token characteristics
    token_info = [(token.text, token.lemma_, len(token), token.pos_) for token in doc]

    # Regular expressions over strings
    regex_matches = re.findall(r'\b[A-Z]{2,}\b', text)  # Find all uppercase words

    # Sentence delimiters
    sentences = [sent.text for sent in doc.sents]

    return token_info, regex_matches, sentences

recipe_files = ["training/prvni.txt", "training/druhej.txt", "training/treti.txt", "training/ctvrtej.txt"]
    
# Loop over each file
for file_name in recipe_files:
    # Open the file
    with open(file_name, 'r') as file:
        # Read the text
        text = file.read()

        # Call the function with the text from the file
        token_info, regex_matches, sentences = extract_info(text)

        # Print the results
        print(f"Results for {file_name}:\n")
        print("Token Info (text, lemma, length, POS):")
        for info in token_info:
            print(info)

        print("\nRegex Matches:")
        for match in regex_matches:
            print(match)

        print("\nSentences:")
        for sentence in sentences:
            print(sentence)
        print("\n\n")



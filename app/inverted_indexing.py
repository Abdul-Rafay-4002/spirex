import pickle

# Inverted Index creation function
def create_inverted_index(documents):
    """Create an inverted index from the given documents."""
    inverted_index = {}
    for doc_id, content in documents.items():
        words = content.split()  # Split document into words
        for word in words:
            if word not in inverted_index:
                inverted_index[word] = []
            inverted_index[word].append(doc_id)
    return inverted_index

# Function to save index to a file
def save_index_to_disk(index, filename):
    """Save the index to a file using pickle."""
    with open(filename, 'wb') as file:
        pickle.dump(index, file)
    print(f"Index saved to {filename}")

# Function to load index from a file
def load_index_from_disk(filename):
    """Load the index from a file using pickle."""
    with open(filename, 'rb') as file:
        return pickle.load(file)

if __name__ == "__main__":
    documents = {
        'doc1': "apple banana cherry",
        'doc2': "apple date cherry",
        'doc3': "fig grape apple"
    }

    # Create the inverted index
    inverted_index = create_inverted_index(documents)
    print("Inverted Index:", inverted_index)

    # Save the inverted index to disk
    save_index_to_disk(inverted_index, "inverted_index.pkl")

    # Test loading the index from disk
    loaded_inverted_index = load_index_from_disk("inverted_index.pkl")
    print("Loaded Inverted Index:", loaded_inverted_index)

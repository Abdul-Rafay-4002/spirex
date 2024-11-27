import pickle

def create_forward_index(documents):
    """Create a forward index from the given documents."""
    forward_index = {}
    for doc_id, content in documents.items():
        forward_index[doc_id] = content.split()
    return forward_index

def save_index_to_disk(index, filename):
    """Save the index to a file using pickle."""
    with open(filename, 'wb') as file:
        pickle.dump(index, file)
    print(f"Index saved to {filename}")

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

    # Create the forward index
    forward_index = create_forward_index(documents)
    print("Forward Index:", forward_index)

    # Save the forward index to disk
    save_index_to_disk(forward_index, "forward_index.pkl")

    # Test loading the index from disk
    loaded_forward_index = load_index_from_disk("forward_index.pkl")
    print("Loaded Forward Index:", loaded_forward_index)

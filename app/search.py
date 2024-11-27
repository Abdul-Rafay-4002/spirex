from forward_indexing import create_forward_index
# Function to process a single word query
def process_single_word_query(query, inverted_index):
    query = query.lower().strip()  # Normalize the query
    if query in inverted_index:
        return inverted_index[query]  # Return documents containing the word
    else:
        return []  # Return an empty list if the word is not found


# Function to process a multi-word query
def process_multi_word_query(query, inverted_index):
    words = query.lower().split()  # Tokenize and normalize the query
    result_set = None
    
    for word in words:
        if word in inverted_index:
            # Get the documents for the word
            documents = set(inverted_index[word])
            if result_set is None:
                result_set = documents  # Initialize with the first word's documents
            else:
                result_set = result_set.intersection(documents)  # AND operation
    
    if result_set:
        return list(result_set)  # Return documents that contain all words
    else:
        return []  # Return an empty list if no documents are found


# Final search function combining both types of queries
def search(query, inverted_index):
    query = query.strip()
    if ' ' in query:  # Multi-word query
        return process_multi_word_query(query, inverted_index)
    else:  # Single word query
        return process_single_word_query(query, inverted_index)

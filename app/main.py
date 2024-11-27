from flask import Flask, request, jsonify
from search import search
from inverted_indexing import create_inverted_index

app = Flask(__name__)

# Example documents (for demonstration)
documents = {
    'doc1': "apple banana cherry",
    'doc2': "apple date cherry",
    'doc3': "fig grape apple"
}

# Create the inverted index
inverted_index = create_inverted_index(documents)

@app.route('/')
def home():
    return "Welcome to SPIREX!"

@app.route('/search', methods=['GET'])
def search_query():
    query = request.args.get('query')
    if query:
        results = search(query, inverted_index)  # Perform the search
        return jsonify({"query": query, "results": results})
    else:
        return jsonify({"message": "Please provide a query."})

if __name__ == "__main__":
    app.run(debug=True)

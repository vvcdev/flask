from flask import Flask, jsonify, request
from duckpy import Client

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')  # Get the search parameter from the URL
    if not query:
        return jsonify({"error": "Empty search query"}), 400

    try:
        client = Client()
        results = client.search(query)
        # Transform results into JSON-friendly format
        search_results = []
        for result in results:
            search_results.append({
                'title': result.title,
                'url': result.url,
                'description': result.description
            })

        return jsonify(search_results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Change host to '0.0.0.0' to make the app accessible from any network interface
    app.run(debug=True, host='0.0.0.0')

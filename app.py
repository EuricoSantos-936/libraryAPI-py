from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'O senhor dos anéis',
        'autor': 'J.R.R. Tolkien'
    },
]

# Search all books


@app.route("/books")
def get_books():
    return jsonify(books)


app.run(port=5000, host='localhost', debug=True)

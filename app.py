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


@app.route("/books", method=["GET"])
def get_books():
    return jsonify(books)

# Find book by id


@app.route('/books/<int:id>', method=["GET"])
def get_book_bt_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)


app.run(port=5000, host='localhost', debug=True)

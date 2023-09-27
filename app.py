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


@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)

# Find book by id


@app.route("/books/<int:id>", methods=["GET"]) # type: ignore
def get_book_bt_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

#  Modify book

@app.route('/books/<int:id>', methods=["PUT"]) # type: ignore
def modify_book(id):
    modified_book = request.get_json()
    for index,book in enumerate(books):
        if book.get('id') == id:
            books[index].update(modified_book)
            return jsonify(books[index])

# Add book
@app.route("/books", methods=["POST"])
def add_book():
    new_book = request.get_json()
    books.append(new_book)  

    return jsonify(books)

app.run(port=5000, host='localhost', debug=True)

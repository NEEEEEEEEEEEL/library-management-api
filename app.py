from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
books = []
members = []

# Utility function for generating IDs
def generate_id(data):
    return max([item['id'] for item in data], default=0) + 1

# Book Endpoints
@app.route('/books', methods=['GET'])
def get_books():
    title = request.args.get('title')
    author = request.args.get('author')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))

    filtered_books = books

    if title:
        filtered_books = [book for book in filtered_books if title.lower() in book['title'].lower()]
    if author:
        filtered_books = [book for book in filtered_books if author.lower() in book['author'].lower()]

    start = (page - 1) * per_page
    end = start + per_page
    return jsonify(filtered_books[start:end])

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    book = {
        'id': generate_id(books),
        'title': data['title'],
        'author': data['author'],
        'year': data.get('year', None),
        'genre': data.get('genre', None)
    }
    books.append(book)
    return jsonify(book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    book = next((book for book in books if book['id'] == book_id), None)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    book.update({
        'title': data.get('title', book['title']),
        'author': data.get('author', book['author']),
        'year': data.get('year', book.get('year')),
        'genre': data.get('genre', book.get('genre'))
    })
    return jsonify(book)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return '', 204

# Member Endpoints
@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(members)

@app.route('/members', methods=['POST'])
def add_member():
    data = request.json
    member = {
        'id': generate_id(members),
        'name': data['name'],
        'email': data['email']
    }
    members.append(member)
    return jsonify(member), 201

@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    data = request.json
    member = next((member for member in members if member['id'] == member_id), None)
    if not member:
        return jsonify({'error': 'Member not found'}), 404

    member.update({
        'name': data.get('name', member['name']),
        'email': data.get('email', member['email'])
    })
    return jsonify(member)

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    global members
    members = [member for member in members if member['id'] != member_id]
    return '', 204

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)

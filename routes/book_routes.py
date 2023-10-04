from flask import Blueprint, request, jsonify
from ..models.book import Book
from ..app import session

book_routes = Blueprint('book_routes', __name__)


@book_routes.route('/books', methods=['GET'])
def get_books():
    books = session.query(Book).all()
    return jsonify([book.__dict__ for book in books])


@book_routes.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = session.query(Book).get(book_id)
    if book:
        return jsonify(book.__dict__)
    return jsonify({"message": "Livre non trouvé"}), 404


@book_routes.route('/books', methods=['POST'])
def create_book():
    data = request.json
    book = Book(**data)
    session.add(book)
    session.commit()
    return jsonify(book.__dict__), 201


@book_routes.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    book = session.query(Book).get(book_id)
    if book:
        for key, value in data.items():
            setattr(book, key, value)
        session.commit()
        return jsonify(book.__dict__)
    return jsonify({"message": "Livre non trouvé"}), 404


@book_routes.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = session.query(Book).get(book_id)
    if book:
        session.delete(book)
        session.commit()
        return jsonify({"message": "Livre supprimé"})
    return jsonify({"message": "Livre non trouvé"}), 404

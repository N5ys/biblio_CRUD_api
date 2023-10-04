from flask import Blueprint, request, jsonify
from ..models.author import Author
from ..app import session

author_routes = Blueprint('author_routes', __name__)


@author_routes.route('/authors', methods=['GET'])
def get_authors():
    authors = session.query(Author).all()
    return jsonify([author.__dict__ for author in authors])


@author_routes.route('/authors/<int:author_id>', methods=['GET'])
def get_author(author_id):
    author = session.query(Author).get(author_id)
    if author:
        return jsonify(author.__dict__)
    return jsonify({"message": "Auteur non trouvé"}), 404


@author_routes.route('/authors', methods=['POST'])
def create_author():
    data = request.json
    author = Author(**data)
    session.add(author)
    session.commit()
    return jsonify(author.__dict__), 201


@author_routes.route('/authors/<int:author_id>', methods=['PUT'])
def update_author(author_id):
    data = request.json
    author = session.query(Author).get(author_id)
    if author:
        for key, value in data.items():
            setattr(author, key, value)
        session.commit()
        return jsonify(author.__dict__)
    return jsonify({"message": "Auteur non trouvé"}), 404


@author_routes.route('/authors/<int:author_id>', methods=['DELETE'])
def delete_author(author_id):
    author = session.query(Author).get(author_id)
    if author:
        session.delete(author)
        session.commit()
        return jsonify({"message": "Auteur supprimé"})
    return jsonify({"message": "Auteur non trouvé"}), 404

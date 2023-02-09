from flask import Flask, request, jsonify
from flask_migrate import Migrate
from typing import List, Tuple


"""
App Config
"""

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres@localhost:5432/library"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
from models import db, Book

db.init_app(app)
migrate = Migrate(app, db)


"""
Controllers
"""


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/books", methods=["GET"])
def get_books() -> List[Tuple[str, str, List[str]]]:
    """
    Returns a list of books in the Library, including their name, author, and genres

    Returns:
        List[Tuple[str, str, List[str]]]: A list of tuples,
        each containing the title, author and genres of a book
    """
    books = Book.query.all()
    return [
        (book.title, book.author, [genre.name for genre in book.genres])
        for book in books
    ]


@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()
    try:
        book = Book(
            title=data["title"],
            author=data["author"],
            publication_date=data["publication_date"],
            genre_names=data["genres"]
        )
        db.session.add(book)
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    
    return jsonify({"message": "Book created successfully"}), 201

"""
Launch, debug mode, port config
"""

if __name__ == "__main__":
    app.run()

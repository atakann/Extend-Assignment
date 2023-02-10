from flask import Flask, request, jsonify
from flask_migrate import Migrate
from typing import List, Optional, Dict, Union


"""
App Config
"""

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres@localhost:5432/library"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
from models import db, Book, Genre

db.init_app(app)
migrate = Migrate(app, db)


"""
Controllers
"""


@app.route("/")
def index():
    return jsonify(hello="World!")


@app.route("/books", methods=["GET"])
def get_books(
    genres: Optional[List[str]] = None,
    author: Optional[str] = None,
    sort: Optional[str] = None,
) -> dict:
    """
    Get books by genres and author, or sorted by publication date

    Args:
        genres (List[str], optional): a list of genre names to filter by
        author (str, optional): an author name to filter by
        sort (str, optional): arg to indicate sort order ('asc' or 'desc')

    Returns:
        dict: a dictionary containing status code and book data
    """
    data = request.get_json()
    author = data.get("author")
    genres = data.get("genres")
    sort = data.get("sort")
    books = Book.query

    if author:
        books = books.filter_by(author=author)
    if genres:
        books = books.join(Book.genres).filter(Genre.name.in_(genres))
    if sort == "asc":
        books = books.order_by(Book.publication_date.asc())
    elif sort == "desc":
        books = books.order_by(Book.publication_date.desc())

    books = books.all()

    result = []
    for book in books:
        result.append(
            {
                "title": book.title,
                "author": book.author,
                "genres": [genre.name for genre in book.genres],
            }
        )

    return result


@app.route("/books", methods=["POST"])
def create_book() -> dict:
    """
    Create a new book and associate it with a given genre

    Returns:
        dict: a dictionary containing status code and message
    """
    data = request.get_json()
    title = data.get("title")
    author = data.get("author")
    publication_date = data.get("publication_date")
    genre_names = data.get("genres")

    if not all([title, author, publication_date, genre_names]):
        return {"message": "All fields are required"}, 400

    book = Book(title=title, author=author, publication_date=publication_date)

    for genre_name in genre_names:
        genre = Genre.query.filter_by(name=genre_name).first()
        if genre is None:
            genre = Genre(name=genre_name)
            db.session.add(genre)
        book.genres.append(genre)

    db.session.add(book)
    db.session.commit()

    return (
        jsonify({"message": "Book successfully created", "Book Title": book.title}),
        201,
    )


@app.route("/genres", methods=["GET"])
def get_genres() -> dict:
    """
    Retrieve all genres from the library database


    Returns:
        list: a dictionary with:
            - status_code : HTTP status code
            - message: a list of dictionaries with genre:
                - id: integer, the id of the genre
                - name: string, the name of the genre
    """

    genres = Genre.query.all()
    return jsonify(
        {
            "status_code": 200,
            "message": [{"id": genre.id, "name": genre.name} for genre in genres],
        }
    )


@app.route("/genres", methods=["PUT"])
def update_genre() -> dict:
    """
    Update a genre in the library database

    Returns:
        A JSON object with keys:
            - status_code: HTTP Status Code
            - message: error message or result dictionary
                - id: integer, the id of the genre
                - name: string, the name of the genre
    """
    data = request.get_json()
    genre_name = data.get("genre_name")
    new_name = data.get("new_name")
    genre = Genre.query.filter_by(name=genre_name).first()
    if not genre:
        return (
            jsonify(
                {
                    "status_code": 404,
                    "message": f"Genre with name '{genre_name}' not found.",
                }
            ),
            404,
        )

    genre.name = new_name
    db.session.commit()

    return (
        jsonify({"status_code": 200, "message": {"id": genre.id, "name": genre.name}}),
        200,
    )


"""
Launch, debug mode, port config
"""

if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()

    #     # Add some genres to the database
    #     fiction = Genre(name="Fiction")
    #     non_fiction = Genre(name="Non-Fiction")
    #     mystery = Genre(name="Mystery")

    #     db.session.add(fiction)
    #     db.session.add(non_fiction)
    #     db.session.add(mystery)

    #     # Add some books to the database
    #     book1 = Book(
    #         title="The Great Gatsby",
    #         author="F. Scott Fitzgerald",
    #         publication_date="1925-04-10",
    #     )
    #     book2 = Book(
    #         title="To Kill a Mockingbird",
    #         author="Harper Lee",
    #         publication_date="1960-07-11",
    #     )
    #     book3 = Book(
    #         title="Pride and Prejudice",
    #         author="Jane Austen",
    #         publication_date="1813-01-28",
    #     )

    #     db.session.add(book1)
    #     db.session.add(book2)
    #     db.session.add(book3)

    #     # Associate the books with their respective genres
    #     book1.genres.append(fiction)
    #     book2.genres.append(fiction)
    #     book2.genres.append(mystery)
    #     book3.genres.append(fiction)

    #     db.session.commit()

    app.run()

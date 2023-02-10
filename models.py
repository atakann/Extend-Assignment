from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
"""
Models
"""


class Book(db.Model):
    """
    A model representing a Book in the Library
    """

    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    publication_date = db.Column(db.Date, nullable=False)
    # many-to-many relationship between books and genres
    # secondary specifies the join table
    genres = db.relationship("Genre", secondary="book_genres", backref="books", lazy=True)

    def __repr__(self) -> str:
        return f"<Book {self.title} by {self.author}>"


class Genre(db.Model):
    """
    A model representing a Genre in the Library
    """

    __tablename__ = "genres"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"<Genre {self.name}>"


# Join table for many-to-many relationship. Single book can belong to one or more
# genres and a single genre can be associated with one or more books.

book_genres = db.Table(
    "book_genres",
    db.Column("book_id", db.Integer, db.ForeignKey("books.id"), primary_key=True),
    db.Column("genre_id", db.Integer, db.ForeignKey("genres.id"), primary_key=True),
)

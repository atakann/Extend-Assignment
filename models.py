from app import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)
"""
Models
"""


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    publication = db.Column(db.Date, nullable=False)
    # many-to-many relationship between books and genres
    # secondary specifies the join table
    genres = db.relationship(
        "Genre", secondary="book_genres", backref=db.backref("books", lazy="dynamic")
    )

    def __repr__(self) -> str:
        return f'<Book {self.title} by {self.author}>'


class Genre(db.Model):
    __tablename__ = "genres"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    def __repr__(self) -> str:
        return f'<Genre {self.name}>'


# Join table for many-to-many relationship. Single book can belong to one or more
# genres and a single genre can be associated with one or more books.

book_genres = db.Table(
    "book_genres",
    db.Column("book_id", db.Integer, db.ForeignKey("books.id"), primary_key=True),
    db.Column("genre_id", db.Integer, db.ForeignKey("genres.id"), primary_key=True),
)

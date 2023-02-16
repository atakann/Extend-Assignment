from app import app, db, Book, Genre
from datetime import date

with app.app_context():
    # create the database schema
    db.create_all()

    if not Book.query.all():
        # Create some genre objects if the database is not already populated
        fiction = Genre(name="Fiction")
        non_fiction = Genre(name="Non-Fiction")
        mystery = Genre(name="Mystery")

        # Add the genres to the database
        db.session.add(fiction)
        db.session.add(non_fiction)
        db.session.add(mystery)

        # Commit the changes to the database
        db.session.commit()

        # Create some book objects
        book1 = Book(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
            publication_date=date(1925, 4, 10),
        )
        book2 = Book(
            title="To Kill a Mockingbird",
            author="Harper Lee",
            publication_date=date(1960, 7, 11),
        )
        book3 = Book(
            title="Pride and Prejudice",
            author="Jane Austen",
            publication_date=date(1813, 1, 28),
        )
        book4 = Book(
            title="Atomic Habits",
            author="James Clear",
            publication_date=date(2018, 10, 16),
        )

        # Add the books to the database
        db.session.add(book1)
        db.session.add(book2)
        db.session.add(book3)
        db.session.add(book4)

        # Associate the books with their respective genres
        book1.genres.append(fiction)
        book2.genres.append(fiction)
        book2.genres.append(mystery)
        book3.genres.append(fiction)
        book4.genres.append(non_fiction)

        # Commit the changes to the database
        db.session.commit()

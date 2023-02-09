Library App
-----

## Introduction

Library App

Objective is to build a Library App with REST API endpoints, that connects to PostgreSQL to store and query book information.

## Overview

There will be a model named Book with attributes of,
- Title
- Author
- Publication Date
- Genre (Philosopy, Economy, History etc.) (One or more genres)

The user will have capabilities of,

* creating new books
* searching for books using filters of **genre or author**, and sort them according to **publication date**
* the query response should have the **Name, Author and Genres** of the book

* User should be able to update genres, **Genre** should be editable.

## Tech Stack

Tech stack will include the following,
 * **Flask** as Python web-framework
 * **PostgreSQL** as Database
 * **SQLAlchemy ORM** as ORM


CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    publication_date DATE
);

CREATE TABLE genres (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE book_genres (
    book_id INTEGER,
    genre_id INTEGER,
    PRIMARY KEY (book_id, genre_id),
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (genre_id) REFERENCES genres(id)
);

INSERT INTO genres (name) VALUES
           ('Fantasy'),
           ('Science Fiction'),
           ('Mystery'),
           ('Romance');

INSERT INTO books (name, author, publication_date) VALUES
           ('The Lord of the Rings', 'J.R.R. Tolkien', '1954-07-29'),
           ('Dune', 'Frank Herbert', '1965-06-01'),
           ('Murder on the Orient Express', 'Agatha Christie', '1934-01-01'),
           ('Pride and Prejudice', 'Jane Austen', '1813-01-28');
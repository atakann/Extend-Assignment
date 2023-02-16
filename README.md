## Library App

## Introduction

Library App

Objective is to build a Library App with REST API endpoints, that connects to PostgreSQL to store and query book information.

The Library App is a REST API for a library that connects to a PostgreSQL database to store and query book information, and edit genre information. The API allows users to create new books, search for books using filters of genre or author, and sort books by publication date. The API also allows the user to update genres.

## Overview

The Library App is built using Flask, PostgreSQL, SQLAlchemy ORM.

The app has one model named `Book`with the following attributes:

-   Title
-   Author
-   Publication Date
-   Genre (Philosopy, Economy, History etc.) (One or more genres)

The user has the following capabilities:

-   creating new books
-   searching for books using filters of **genre or author**, and sort them according to **publication date**
-   the query response should have the **Name, Author and Genres** of the book

-   User should be able to update genres, **Genre** should be editable.

## Tech Stack

Tech stack will include the following,

-   **Flask** as Python web-framework
-   **PostgreSQL** as Database
-   **SQLAlchemy ORM** as ORM
-   **Docker** and **Docker Compose** for containerization and deployment

The application uses Flask to handle HTTP requests and responses, SQLAlchemy ORM to communicate with PostgreSQL database. Docker and Docker Compose are used to containerize the application and its dependencies, making it easy to run and deploy the application.

## Notes

* **Formatting**:
    * black is used to format the code
* **Database**:
    * seeds.py script populates the database after it is created with some examples
* **Testing**:
    * I have used Postman to test the API endpoints, which gives example responses back from example requests.


## How to Use
To run the Library App, you'll need Docker and Docker Compose installed on your computer.

### Clone the Repository
First, clone the repository to your local machine:
```
git clone https://github.com/atakann/Extend-Assignment.git
```

### Build the Docker Image & Start the Application
Navigate to the project directory and build the Docker image:

```
docker-compose build
```

Start the application using the following command:

```
docker-compose up
```

You can now test the API endpoints using a tool like Postman. Some examples are given in the **API Endpoints** section below.


## API Endpoints

The Library App has the following API endpoints:

### GET /books

This endpoint returns a list of books filtered by author and genre, and can be sorted by publication date. It accepts the following query parameters:

-   `author`: the author name to filter the books by
-   `genres`: a list of genre names to filter the books by. Multiple genres can be provided by separating them with commas
-   `sort`: the sort order for the books by publication date. Can be either `asc`or `desc`

The response of this endpoint is a JSON object containing a list of books, where each book has the following fields:

-   `title`: title of the book
-   `author`: author of the book
-   `genres`: a list of genres of the book

Example request:

```
GET /books?author=Jane%20Austen&genres=Fiction&sort=asc
```

Example response:

```
[
   {
       "title": "Pride and Prejudice",
       "author": "Jane Austen",
       "genres": [
           "Fiction"
       ]
   }
]
```

### POST /books

This endpoint is used to create a new book. It accepts the following JSON data in the request body:

-   `title`: title of the book (required)
-   `author`: author of the book (required)
-   `publication_date`: publication date of the book in `YYYY-MM-DD`format (required)
-   `genres`: list of genre names that the book belongs to (required)

The response of this endpoint is a JSON object containing the message "Book successfully created" and the title of the created book.

Example request:

```
POST /books
Content-Type: application/json

{
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "publication_date": "1988-01-01",
    "genres": [
        "Fiction",
        "Philosophy"
    ]
}
```

Example response:

```
{
    "Book Title": "The Alchemist",
    "message": "Book successfully created"
}
```

### GET /genres

This endpoint returns the list of all genres available in the database.

The response of this endpoint is a JSON object containing a list of genres and has the following fields:
* `id`: the ID of the genre
* `name`: the name of the genre

Example request:

```
GET /genres
```

Example response: 
```
{
    "message": [
        {
            "id": 1,
            "name": "Fiction"
        },
        {
            "id": 2,
            "name": "Non-Fiction"
        }
    ]
}
```

### PUT /genres
This endpoint is used to update the name of a genre in the database. It accepts the following JSON data in the request body:
* `genre_name`: name of the genre to be updated (required)
* `new_name`: new name for the genre (required)

The response of this endpoint is a JSON object containing a message with the ID and the new name of the updated genre.

Example request:

```
PUT /genres
Content-Type: application/json

{
    "genre_name": "Philosophy",
    "new_name": "Spirituality"
}
```

Example response:

```
{
    "message": {
        "id": 3,
        "name": "new_name of the genre"
    }
}
```
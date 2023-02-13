Library App
-----

## Introduction

Library App

Objective is to build a Library App with REST API endpoints, that connects to PostgreSQL to store and query book information.

The Library App is a REST API for a library that connects to a PostgreSQL database to store and query book information, and edit genre information. The API allows users to create new books, search for books using filters of genre or author, and sort books by publication date. The API also allows the user to update genres.

## Overview

The Library App is built using Flask, PostgreSQL, SQLAlchemy ORM.

The app has one model named `Book`with the following attributes:

- Title
- Author
- Publication Date
- Genre (Philosopy, Economy, History etc.) (One or more genres)

The user has the following capabilities:

* creating new books
* searching for books using filters of **genre or author**, and sort them according to **publication date**
* the query response should have the **Name, Author and Genres** of the book

* User should be able to update genres, **Genre** should be editable.

## Tech Stack

Tech stack will include the following,
 * **Flask** as Python web-framework
 * **PostgreSQL** as Database
 * **SQLAlchemy ORM** as ORM
 * **Docker** and **Docker Compose** for containerization and deployment
 
 The application uses Flask to handle HTTP requests and responses, SQLAlchemy ORM to communicate with PostgreSQL database. Docker and Docker Compose are used to containerize the application and its dependencies, making it easy to run and deploy the application.


## API Endpoints
The Library App has the following API endpoints:

### GET /books
This endpoint returns a list of books filtered by author and genre, and can be sorted by publication date. It accepts the following query parameters:
* `author`: the author name to filter the books.
* `genres`: a list of genre names to filter the books. Multiple genres can be provided by separating them with commas.
* `sort`: the sort order for the books by publication date. Can be either `asc`or `desc`

The response of this endpoint is a JSON object containing a list of books, where each book has the following fields:
* `title`: title of the book
* `author`: author of the book
* `genres`: a list of genres of the book




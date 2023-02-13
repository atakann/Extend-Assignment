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

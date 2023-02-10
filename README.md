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

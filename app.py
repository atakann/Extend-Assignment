from flask import Flask
from flask_migrate import Migrate


"""
App Config
"""

app = Flask(__name__)

from models import db, Book

migrate = Migrate(app, db)


"""
Controllers
"""


@app.route("/")
def index():
    return "Hello, World!"


"""
Launch, debug mode, port config
"""

if __name__ == "__main__":
    app.run()

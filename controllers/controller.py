from flask import render_template, request, redirect

from app import app
from models.book import Book
from models.library import get_book_list, books_list

@app.route("/")
def index():
    book_list = get_book_list()
    return render_template("index.html", book_list = book_list)

@app.route("/book/<number>")
def single_book(number):
    return render_template("single_book.html", book = books_list[int(number)])
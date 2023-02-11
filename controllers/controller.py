from flask import render_template, request, redirect

from app import app
from models.book import Book
from models.library import get_book_list, books_list, create_new_book, delete_book

@app.route("/")
def index():
    book_list = get_book_list()
    return render_template("index.html", book_list = book_list)

@app.route("/book/<index>")
def single_book(index):
    return render_template("single_book.html", book = books_list[int(index)])

@app.route("/books", methods=["POST"])
def create():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    checked_out = True if 'checked out' in request.form else False
    checked_in = True if 'checked in' in request.form else False

    new_book = Book(title=title, author=author, genre=genre, checked_out=checked_out, checked_in=checked_in)
    create_new_book(new_book)
    return redirect("/")

@app.route("/books/<index>/delete", methods=["POST"])
def destroy(index):
    delete_book(int(index))
    return redirect("/")



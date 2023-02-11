from models.book import Book

book_1 = Book("Shoe Dog", "Phil Knight", "Biography")
book_2 = Book("Born to Run", "Christopher McDougall", "Memoir")
book_3 = Book("Green Lights", "Matthew McConaughey", "Philosophy/Poetry")

books_list = [book_1, book_2, book_3]

def get_book_list():
    return books_list

